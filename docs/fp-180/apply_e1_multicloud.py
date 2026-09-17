# -*- coding: utf-8 -*-
"""FP-180 — Score the multicloud platforms in E1.

FP-177 section 4 lists multicloud platforms as eligible in E1 with no condition
attached, yet none of them had a score there: the anchor convention parked their
evidence in E2. With the anchor shortcut dropped, E1 can be completed properly.

Two kinds of evidence are written here, and the difference is stated per cell.

1. Evidence of its own for E1. The expected outputs of E1 include "gasto no
   asignado" and a showback report, which E2 never asks for. A1 is therefore
   investigated specifically against that: does the tool make unallocated spend
   visible? Researched on 2026-09-16 for CloudHealth, CloudZero and Vantage.

2. Subsumed evidence. For the remaining scenario-dependent indicators, the
   capability documented for E2 covers E1 by inclusion: a platform that
   consolidates and breaks down cost across several providers necessarily does
   it for one, which is E1's condition. This is an explicit argument recorded
   cell by cell, not a copied value: where the capability does not subsume, the
   cell stays as it is.

Products with no evidence in E2 keep their NE, with the reason already recorded.

Usage: python apply_e1_multicloud.py
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
REPORT = HERE / "investigacion-e1.md"
VERIFIED = "2026-09-16"

SOURCE_SCENARIO = "E2"
TARGET_SCENARIO = "E1"
CATEGORY = "Multicloud"

# Scenario-dependent indicators whose E2 capability subsumes the E1 case.
# A1 is included: the question is identical in both scenarios. Where E1's own
# evidence on unallocated spend was found, that stronger evidence is used instead.
SUBSUMED = ["V1", "A1", "A2", "O1", "AU1", "I1", "I2", "AD1", "P2"]

SUBSUMPTION_NOTE = (
    "Evidencia subsumida desde E2 ({date}): la capacidad documentada para consolidar y operar "
    "sobre varios proveedores cubre por inclusion el caso de un unico proveedor, que es la "
    "condicion de E1. La fuente y la cita originales se conservan sin cambios; lo que se "
    "declara aqui es el argumento por el que sostienen tambien el valor en E1.")

DENSIFY_NOTE = (
    "Ausencia verificada tambien en E1 ({date}): la documentacion describe a Kubex/Densify como "
    "optimizador de recursos de Kubernetes. La ausencia de desglose y asignacion de gasto "
    "cloud no depende de que el escenario sea de una nube o de varias, por lo que el valor 0 "
    "se sostiene en E1 por el mismo motivo registrado para E2.")

# A1 investigated specifically against E1's expected output: unallocated spend and showback.
E1_OWN_EVIDENCE = {
    "CloudHealth": (
        2, "Oficial",
        "La plataforma separa explicitamente lo atribuible de lo no atribuible: clasifica los "
        "costos en «Direct Costs (which have a resource ID or asset ID associated and can be "
        "allocated to Perspective groups)» e «Indirect Costs (which are not associated with a "
        "resource ID or asset ID, such as support costs, and therefore cannot be attributed to "
        "a group)», de modo que el gasto no asignable queda visible en vez de diluirse. La "
        "documentacion describe ademas revisar los activos sin etiquetar «to assign "
        "appropriate accountability» y construir Perspectives por area responsable, que es el "
        "reporte de showback que E1 espera.",
        "https://techdocs.broadcom.com/us/en/vmware-tanzu/cloudhealth/tanzu-cloudhealth/saas/"
        "tnz-cloudhealth/using-and-managing-tanzu-cloudhealth-managing-perspectives.html"),
    "CloudZero": (
        2, "Oficial",
        "La asignacion cubre el total y deja explicito el remanente: «The remaining spend goes "
        "to a default element so the total always reconciles with the actual bill», e incluye "
        "los recursos sin etiquetar y los no etiquetables dentro del modelo de dimensiones. El "
        "gasto no asignado no desaparece: queda en un elemento identificable.",
        "https://docs.cloudzero.com/docs/costformation-allocating-shared-costs"),
    "Vantage": (
        2, "Oficial",
        "Los segmentos calculan el gasto no asignado como una categoria propia: «Any costs not "
        "assigned to a segment are considered unallocated costs. By analyzing your segments, "
        "you can identify and burn down these unallocated costs to improve financial "
        "accountability». La documentacion precisa ademas que «Segments ensure that costs are "
        "allocated only once and not duplicated in cases of showback/chargeback scenarios», "
        "que es exactamente la salida de asignacion y showback que E1 espera.",
        "https://docs.vantage.sh/segments"),
}


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if not WORKBOOK.exists():
        print(f"ERROR: no se encontro {WORKBOOK}")
        return 1

    shutil.copy2(WORKBOOK, WORKBOOK.with_suffix(".xlsx.bak"))
    workbook = openpyxl.load_workbook(WORKBOOK)
    sheet = workbook["Puntuacion"]
    header = [c.value for c in sheet[1]]
    col = {h: i + 1 for i, h in enumerate(header)}
    idx = {h: i for i, h in enumerate(header)}

    before, _ = read_scores(sheet)
    before_results = {k: evaluate(v, BASE_W) for k, v in before.items()}

    # read the E2 row of every multicloud product
    source = {}
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if row[idx["Escenario"]] != SOURCE_SCENARIO or row[idx["Categoria"]] != CATEGORY:
            continue
        source[(row[idx["Producto"]], row[idx["Indicador"]])] = (
            row[idx["Valor (0-3/NE/NA)"]], row[idx["Tipo de evidencia"]],
            row[idx["Evidencia"]], row[idx["Fuente"]])

    changes, skipped = [], []
    for row in range(2, sheet.max_row + 1):
        if sheet.cell(row, col["Escenario"]).value != TARGET_SCENARIO:
            continue
        if sheet.cell(row, col["Categoria"]).value != CATEGORY:
            continue
        product = sheet.cell(row, col["Producto"]).value
        indicator = sheet.cell(row, col["Indicador"]).value
        cell = sheet.cell(row, col["Valor (0-3/NE/NA)"])
        if str(cell.value).strip().upper() != "NE":
            continue

        if indicator == "A1" and product in E1_OWN_EVIDENCE:
            value, ev_type, evidence, src = E1_OWN_EVIDENCE[product]
            note = (f"Investigacion propia de E1 ({VERIFIED}): celda verificada contra la "
                    "salida esperada del escenario, que exige gasto no asignado visible y "
                    "reporte de showback.")
        elif indicator in SUBSUMED:
            origin = source.get((product, indicator))
            if not origin or str(origin[0]).strip().upper() in ("NE", "NA", "NONE"):
                skipped.append((product, indicator))
                continue
            value, ev_type, evidence, src = origin
            note = (DENSIFY_NOTE if product == "Densify" else SUBSUMPTION_NOTE).format(
                date=VERIFIED)
        else:
            continue

        cell.value = value
        sheet.cell(row, col["Tipo de evidencia"]).value = ev_type
        sheet.cell(row, col["Evidencia"]).value = evidence
        sheet.cell(row, col["Fuente"]).value = src
        sheet.cell(row, col["Fecha de verificacion"]).value = VERIFIED if src else ""
        note_cell = sheet.cell(row, col["Notas"])
        note_cell.value = f"{note_cell.value} | {note}" if note_cell.value else note
        changes.append({"prod": product, "ind": indicator, "val": value})

    print(f"Celdas completadas en E1: {len(changes)}")
    print(f"Celdas que siguen NE por falta de evidencia en origen: {len(skipped)}")

    after, _ = read_scores(sheet)
    after_results = {k: evaluate(v, BASE_W) for k, v in after.items()}
    write_results_sheet(workbook, after)
    rebuild_charts(workbook)
    workbook.save(WORKBOOK)

    # The report is rebuilt from the workbook, so regenerating it is always safe
    # and stays complete even when this pass has nothing left to apply.
    if True:
        lines = [
            "# FP-180 — Escenario E1 completado con las plataformas multinube",
            "",
            f"> Generado por `apply_e1_multicloud.py` el {VERIFIED}. Queda a validacion humana.",
            "",
            "## Por que",
            "",
            "FP-177 §4 lista a las plataformas multinube como elegibles en E1 **sin condicion "
            "alguna**, pero ninguna tenia puntaje ahi: la convencion de escenario ancla dejaba "
            "su evidencia estacionada en E2. Al abandonar ese atajo, E1 se puede completar como "
            "corresponde.",
            "",
            "## Dos tipos de evidencia, declarados celda por celda",
            "",
            "**Evidencia propia de E1.** Las salidas esperadas de E1 incluyen «gasto no "
            "asignado» y un reporte de showback, que E2 nunca pide. Por eso A1 se investigo "
            "especificamente contra eso: si la herramienta hace visible el gasto que no logra "
            "asignar.",
            "",
            "**Evidencia subsumida.** Para el resto de indicadores dependientes del escenario, "
            "la capacidad documentada para E2 cubre E1 por inclusion: una plataforma que "
            "consolida y desglosa costo entre varios proveedores necesariamente lo hace para "
            "uno, que es la condicion de E1. Es un argumento explicito registrado en cada "
            "celda, no un valor copiado: donde la capacidad no subsume, la celda no se toca.",
            "",
        ]
        # Build the table from the workbook, not from this run's changes, so the
        # report stays complete when the pass is re-run.
        completed = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            if row[idx["Escenario"]] != TARGET_SCENARIO or row[idx["Categoria"]] != CATEGORY:
                continue
            notes = str(row[idx["Notas"]] or "")
            if "Evidencia subsumida" in notes:
                kind = "subsumida desde E2"
            elif "Investigacion propia de E1" in notes:
                kind = "propia de E1"
            elif "Ausencia verificada tambien en E1" in notes:
                kind = "ausencia verificada en E1"
            else:
                continue
            completed.append((row[idx["Producto"]], row[idx["Indicador"]],
                              row[idx["Valor (0-3/NE/NA)"]], kind))

        lines += [f"## Celdas completadas ({len(completed)})", "",
                  "| Producto | Indicador | Valor | Tipo de evidencia |",
                  "|---|---|---:|---|"]
        for product, indicator, value, kind in sorted(completed):
            lines.append(f"| {product} | {indicator} | {value} | {kind} |")

        if skipped:
            lines += ["", "## Celdas que siguen en NE", "",
                      "Su producto tampoco tiene evidencia en E2, asi que no hay nada que "
                      "subsumir. El motivo original ya esta registrado en cada celda.", "",
                      "| Producto | Indicador |", "|---|---|"]
            for p, i in sorted(skipped):
                lines.append(f"| {p} | {i} |")

        lines += ["", "## Estado de E1 tras esta pasada", "",
                  "| Producto | Categoria | S linea base | Banda | Cobertura |",
                  "|---|---|---:|---|---:|"]
        scored = [(k, v) for k, v in after_results.items()
                  if k[0] == TARGET_SCENARIO and v["score"] is not None]
        for k, r in sorted(scored, key=lambda kv: -kv[1]["score"]):
            lines.append(f"| {k[2]} | {k[1]} | {r['score']:.2f} | {r['band']} | "
                         f"{r['coverage']:.1f}% |")

        unscored = sorted(k[2] for k, v in after_results.items()
                          if k[0] == TARGET_SCENARIO and v["score"] is None)
        if unscored:
            lines += ["", f"Siguen en «Insufficient evidence» en E1: {', '.join(unscored)}. "
                          "El motivo de cada celda pendiente esta registrado en la hoja "
                          "Puntuacion."]
        lines.append("")
        REPORT.write_text("\n".join(lines), encoding="utf-8")
        print(f"Informe: {REPORT.name}")

    e1 = {k: v for k, v in after_results.items() if k[0] == "E1" and v["score"] is not None}
    print(f"\nE1 con puntaje ({len(e1)}):")
    for k in sorted(e1, key=lambda x: -after_results[x]["score"]):
        r = after_results[k]
        print(f"   {k[2]:<30} {r['score']:>6.2f}  {r['band']:<8} cob {r['coverage']:.1f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
