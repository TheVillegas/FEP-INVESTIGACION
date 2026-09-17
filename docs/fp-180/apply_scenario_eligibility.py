# -*- coding: utf-8 -*-
"""FP-180 — Apply the scenario eligibility conditions written in FP-177.

FP-177 section 4 lists the eligible categories of each scenario, and four of
those entries carry an explicit condition:

    E2, native tools      "para la parte de su proveedor"
    E3, multicloud        "si integran datos de clúster"
    E4, native tools      "cuando soporten estimación previa"
    E5, Kubernetes        "cuando el servicio compartido se ejecute en clúster"

Three of them are eligibility conditions: they decide whether the product enters
the scenario at all, and the matrix already respects them. The E2 one is
different: the product does enter, but with its scope limited, and the matrix
was not applying it.

A native tool in E2 was scored M1 = M2 = 0, which reads as "verified absence of
multicloud consolidation". Since Multicloud is a critical criterion of E2, all
seven native tools were flagged as failing it. But FP-177 admits them to E2 only
"para la parte de su proveedor": the scenario does not ask them to consolidate
other providers, so failing them for it contradicts the eligibility rule the
team itself wrote.

The correct state is NA with a scope justification. This NA is legitimate in a
way the ones corrected earlier were not: it is the *scenario* declaring the
indicator has no object, not the evaluator deciding another product covers the
function. It rests on the text of FP-177, which is exactly what the earlier ones
lacked.

Usage: python apply_scenario_eligibility.py
"""
from __future__ import annotations

import datetime as dt
import shutil
import sys
from pathlib import Path

import openpyxl

from apply_scope_corrections import (BASE_W, evaluate, read_scores,
                                     rebuild_charts, write_results_sheet)

HERE = Path(__file__).resolve().parent
WORKBOOK = HERE / "FP-180_matriz_comparativa.xlsx"
REPORT = HERE / "elegibilidad-por-escenario.md"
TODAY = dt.date.today().isoformat()

TARGET_SCENARIO = "E2"
TARGET_CATEGORY = "Cloud nativa"
TARGET_INDICATORS = ("M1", "M2")

EVIDENCE = ("Alcance declarado por el escenario: FP-177 §4 admite a las herramientas cloud "
            "nativas en E2 «para la parte de su proveedor», de modo que el escenario no les "
            "exige consolidar costos de otros proveedores. El indicador no tiene objeto para "
            "esta categoría bajo la unidad de análisis de E2, por lo que corresponde NA y no "
            "un 0 de ausencia verificada.")

NOTE = ("Condición de elegibilidad FP-177 §4 aplicada ({date}): el valor pasa de {old} a NA. "
        "Este NA lo declara el escenario, no el evaluador: E2 admite a las nativas solo para "
        "la parte de su proveedor. Antes de esta corrección, las siete herramientas nativas "
        "figuraban incumpliendo Multicloud, que es criterio crítico de E2, por no hacer algo "
        "que el escenario no les pide.")


def apply_condition(sheet) -> list[dict]:
    header = [c.value for c in sheet[1]]
    col = {h: i + 1 for i, h in enumerate(header)}
    changes = []
    for row in range(2, sheet.max_row + 1):
        if sheet.cell(row, col["Escenario"]).value != TARGET_SCENARIO:
            continue
        if sheet.cell(row, col["Categoria"]).value != TARGET_CATEGORY:
            continue
        indicator = sheet.cell(row, col["Indicador"]).value
        if indicator not in TARGET_INDICATORS:
            continue
        cell = sheet.cell(row, col["Valor (0-3/NE/NA)"])
        old = cell.value
        if str(old).strip().upper() == "NA":
            continue                                   # idempotent
        cell.value = "NA"
        sheet.cell(row, col["Tipo de evidencia"]).value = "Justificacion de alcance"
        sheet.cell(row, col["Evidencia"]).value = EVIDENCE
        note_cell = sheet.cell(row, col["Notas"])
        note = NOTE.format(date=TODAY, old=old)
        note_cell.value = f"{note_cell.value} | {note}" if note_cell.value else note
        changes.append({"prod": sheet.cell(row, col["Producto"]).value,
                        "ind": indicator, "old": old})
    return changes


def write_report(changes, before, after) -> None:
    lines = [
        "# FP-180 — Condición de elegibilidad de E2 aplicada",
        "",
        f"> Generado por `apply_scenario_eligibility.py` el {TODAY}. Corrección derivada del "
        "texto de FP-177, sin decisión metodológica nueva.",
        "",
        "## Qué dice FP-177",
        "",
        "La sección 4 enumera las categorías elegibles de cada escenario, y cuatro entradas "
        "llevan condición explícita:",
        "",
        "| Escenario | Categoría | Condición | Tipo |",
        "|---|---|---|---|",
        "| E2 | nativas | «para la parte de su proveedor» | **alcance** |",
        "| E3 | multicloud | «si integran datos de clúster» | elegibilidad |",
        "| E4 | nativas | «cuando soporten estimación previa» | elegibilidad |",
        "| E5 | Kubernetes | «cuando el servicio compartido se ejecute en clúster» | contexto |",
        "",
        "Las tres últimas deciden si el producto entra al escenario, y la matriz ya las "
        "respeta. La de E2 es distinta: el producto entra, pero con su alcance acotado, y esa "
        "no se estaba aplicando.",
        "",
        "## El problema corregido",
        "",
        "Las herramientas nativas en E2 estaban puntuadas `M1 = M2 = 0`, que significa ausencia "
        "verificada de consolidación multinube. Como Multicloud es criterio crítico de E2, las "
        "siete figuraban **incumpliendo un criterio crítico por no hacer algo que el escenario "
        "no les pide**.",
        "",
        "El estado correcto es `NA` con justificación de alcance. Conviene notar la diferencia "
        "con los `NA` corregidos en `correcciones-aplicadas.md`: aquellos los ponía el "
        "evaluador razonando que otro producto del mismo proveedor cubría la función, y eran "
        "ausencia verificada disfrazada. Este lo declara el escenario en el texto aprobado por "
        "el equipo, que es precisamente el respaldo que a los otros les faltaba.",
        "",
        f"## Celdas corregidas ({len(changes)})",
        "",
        "| Producto | Indicador | Antes | Ahora |",
        "|---|---|---:|---|",
    ]
    for c in sorted(changes, key=lambda x: (x["prod"], x["ind"])):
        lines.append(f"| {c['prod']} | {c['ind']} | {c['old']} | `NA` |")

    lines += ["", "## Efecto en los resultados", ""]
    moved = [k for k in before
             if before[k]["score"] != after[k]["score"]
             or abs(before[k]["coverage"] - after[k]["coverage"]) > 0.01]
    if moved:
        lines += ["| Escenario | Producto | S antes | S después | Cobertura antes | Cobertura después |",
                  "|---|---|---|---|---:|---:|"]
        for k in sorted(moved):
            o, n = before[k], after[k]
            fmt = lambda r: (f"{r['score']:.2f}" if r["score"] is not None else "Insuf.")
            lines.append(f"| {k[0]} | {k[2]} | {fmt(o)} | {fmt(n)} | "
                         f"{o['coverage']:.1f}% | {n['coverage']:.1f}% |")
    else:
        lines.append("Ningún par cambia de puntaje: las nativas en E2 ya estaban por debajo "
                     "del umbral de cobertura por otras celdas. El efecto es sobre el "
                     "incumplimiento crítico informado, que desaparece porque nunca "
                     "correspondió.")

    lines += [
        "",
        "## Hallazgo relacionado, no aplicado",
        "",
        "La condición de E4 —nativas «cuando soporten estimación previa»— habilita un caso que "
        "la matriz tampoco cubre: **IBM Cloud Cost Estimator cumple esa condición y no está "
        "evaluado en E4**. Toda la evidencia recogida para ese producto describe estimación "
        "previa al despliegue, es decir, corresponde a E4 y no a E1, donde hoy figura por "
        "pertenecer a la categoría nativa.",
        "",
        "Eso resolvería sin reclasificar nada la tensión registrada en "
        "`alternativas-adicionales.md`: el producto no está mal categorizado, está evaluado en "
        "el escenario equivocado. Requiere decisión del equipo antes de aplicarse.",
        "",
    ]
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if not WORKBOOK.exists():
        print(f"ERROR: no se encontro {WORKBOOK}")
        return 1

    shutil.copy2(WORKBOOK, WORKBOOK.with_suffix(".xlsx.bak"))
    workbook = openpyxl.load_workbook(WORKBOOK)
    sheet = workbook["Puntuacion"]

    before, _ = read_scores(sheet)
    before_results = {k: evaluate(v, BASE_W) for k, v in before.items()}

    changes = apply_condition(sheet)
    print(f"Celdas corregidas: {len(changes)}")

    after, _ = read_scores(sheet)
    after_results = {k: evaluate(v, BASE_W) for k, v in after.items()}

    write_results_sheet(workbook, after)
    rebuild_charts(workbook)
    workbook.save(WORKBOOK)
    if changes:
        write_report(changes, before_results, after_results)
        print(f"Informe: {REPORT.name}")
    else:
        print(f"Sin celdas pendientes; se conserva {REPORT.name} tal como estaba.")

    crit = sum(1 for k, v in after.items()
               if k[0] == "E2" and any(x == "NA" for x in v.get("Multicloud", [])))
    print(f"Pares de E2 con Multicloud marcado NA: {crit}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
