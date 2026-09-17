# -*- coding: utf-8 -*-
"""FP-180 — Evaluate IBM Cloud Cost Estimator in E4, where FP-177 admits it.

FP-177 section 4 lists native tools as eligible in E4 "cuando soporten estimación
previa". IBM Cloud Cost Estimator is exactly that, and all the evidence gathered
for it describes estimation before deployment: configuring plan, usage, currency
and region; comparing configurations; the estimate computed inside the project
validation step.

The product was only present in E1, E2, E3, E5 and E6 because it belongs to the
native category, and it scored in none of them. Its zeros in Visibilidad and
Asignacion are correct — a calculator does not break down real spend — but they
measure it against a scenario that is not its own.

This pass adds its E4 rows. There, the indicators that have no object before
deployment become NA, the same treatment already applied to Infracost and to both
pricing calculators, and its documented strengths fall on the critical criteria
of the scenario: Precio and Integracion.

The product is not reclassified: it stays a native tool, and is now also
evaluated in the scenario where FP-177 admits it.

Usage: python apply_ibm_e4.py
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

import openpyxl

from apply_scope_corrections import (BASE_W, CRITICAL, evaluate, read_scores,
                                     rebuild_charts, unevidenced_critical,
                                     write_results_sheet)

HERE = Path(__file__).resolve().parent
WORKBOOK = HERE / "FP-180_matriz_comparativa.xlsx"
REPORT = HERE / "ibm-cost-estimator-e4.md"
VERIFIED = "2026-09-16"

PRODUCT = "IBM Cloud Cost Estimator"
CATEGORY = "Cloud nativa"
SCENARIO = "E4"

CRITERION_OF = {"V": "Visibilidad", "A": "Asignacion", "O": "Optimizacion",
                "AU": "Automatizacion", "M": "Multicloud", "I": "Integracion",
                "AD": "Adopcion", "P": "Precio", "D": "Dependencia"}
ORDER = ["V1", "V2", "A1", "A2", "O1", "O2", "AU1", "AU2", "M1", "M2",
         "I1", "I2", "AD1", "AD2", "P1", "P2", "D1", "D2"]

PREDEPLOY_NA = ("Justificacion de alcance: en E4 la unidad de analisis es el cambio propuesto "
                "antes del despliegue, de modo que el indicador no tiene objeto. Mismo criterio "
                "aplicado a Infracost y a las calculadoras de precios de AWS y Azure.")

VALUES = {
    "V1": (2, "Oficial",
           "Desglosa la estimacion por producto y configuracion del catalogo: el usuario "
           "selecciona el plan de precios y los detalles de configuracion, agrega el producto a "
           "la estimacion e ingresa su uso previsto para calcular el costo, obteniendo el "
           "detalle por componente que este escenario evalua.",
           "https://cloud.ibm.com/docs/account?topic=account-cost"),
    "V2": ("NA", "Justificacion de alcance", PREDEPLOY_NA, ""),
    "A1": ("NA", "Justificacion de alcance", PREDEPLOY_NA, ""),
    "A2": ("NA", "Justificacion de alcance", PREDEPLOY_NA, ""),
    "O1": (1, "Comercial",
           "La pagina de producto declara que la herramienta permite «get tips on how to save "
           "money». Es evidencia comercial del proveedor, por lo que FP-177 §2.1 limita el "
           "indicador a 1.",
           "https://www.ibm.com/products/cloud/cloud-calculator"),
    "O2": ("NA", "Justificacion de alcance",
           "Al no generar recomendaciones de optimizacion propias y documentadas (ver O1), no "
           "aplica evaluar la explicacion de impacto ni el seguimiento de una recomendacion. "
           "Mismo criterio aplicado a las calculadoras de AWS y Azure.", ""),
    "AU1": (0, "Oficial (ausencia verificada)",
            "Es una herramienta de estimacion: no ejecuta ni bloquea acciones o despliegues. La "
            "estimacion forma parte de un paso de validacion, pero la decision de desplegar "
            "queda fuera de la herramienta.",
            "https://cloud.ibm.com/docs/secure-enterprise?topic=secure-enterprise-cost-estimate-project"),
    "AU2": ("NA", "Justificacion de alcance",
            "Al no ejecutar acciones (ver AU1), no aplica evaluar salvaguardas de una ejecucion "
            "automatizada.", ""),
    "M1": (0, "Oficial (ausencia verificada)",
           "Estima exclusivamente productos del catalogo de IBM Cloud; no consolida costos de "
           "otros proveedores.",
           "https://cloud.ibm.com/docs/account?topic=account-cost"),
    "M2": (0, "Oficial (ausencia verificada)",
           "Mismo alcance de diseno que M1.",
           "https://cloud.ibm.com/docs/account?topic=account-cost"),
    "I1": (2, "Oficial",
           "Integra los datos propios del escenario —la configuracion declarada del cambio— "
           "dentro del flujo de proyectos y arquitecturas desplegables: «After saving, the "
           "validation checks are run and a new cost estimate is computed», tomando los "
           "parametros configurados del proyecto.",
           "https://cloud.ibm.com/docs/secure-enterprise?topic=secure-enterprise-cost-estimate-project"),
    "I2": (2, "Oficial",
           "El costo estimado esta incorporado al paso de revision previo al despliegue: se "
           "presenta en el «validation modal» bajo la seccion «Cost estimate successful», junto "
           "a las verificaciones de validacion del proyecto. Es integracion con el flujo "
           "operativo del escenario, no una exportacion manual.",
           "https://cloud.ibm.com/docs/secure-enterprise?topic=secure-enterprise-cost-estimate-project"),
    "AD1": ("NE", "Pendiente",
            "No se encontro documentacion oficial sobre roles y accesos diferenciados para los "
            "perfiles de este escenario (desarrollador, DevOps, arquitecto, revisor de IaC).", ""),
    "AD2": ("NE", "Pendiente",
            "No se encontro guia oficial de habilitacion, ownership o seguimiento de uso "
            "sostenido asociada a la herramienta.", ""),
    "P1": (2, "Oficial",
           "Permite configurar plan de precios, uso, moneda y region, y «see how your pricing is "
           "determined». Los supuestos estan declarados de forma explicita: la estimacion «does "
           "not include all resources, usage, licenses, fees, discounts, or taxes» y esta "
           "«subject to change as the architecture is customized».",
           "https://cloud.ibm.com/docs/secure-enterprise?topic=secure-enterprise-cost-estimate-project ; "
           "https://cloud.ibm.com/docs/account?topic=account-cost"),
    "P2": (2, "Oficial",
           "Permite comparar configuraciones alternativas antes de decidir, con el detalle de "
           "como se determina cada precio, que es la comparacion contextual que E4 evalua.",
           "https://cloud.ibm.com/docs/account?topic=account-cost"),
    "D1": (2, "Oficial",
           "Las estimaciones se exportan y descargan como cotizacion desde la herramienta, en "
           "formato utilizable fuera de ella.",
           "https://cloud.ibm.com/docs/account?topic=account-cost"),
    "D2": ("NE", "Pendiente",
           "No se encontro documentacion sobre dependencias propietarias ni camino de salida o "
           "configuracion reversible de las estimaciones almacenadas.", ""),
}

NOTE = ("Producto incorporado a E4 ({date}) por la condicion de elegibilidad de FP-177 §4, que "
        "admite herramientas nativas en este escenario «cuando soporten estimacion previa». No se "
        "reclasifica el producto: sigue siendo cloud nativa, y ahora tambien se evalua en el "
        "escenario donde FP-177 lo admite. Sus indicadores sin objeto antes del despliegue se "
        "marcan NA con el mismo criterio aplicado a Infracost y a las calculadoras de AWS y Azure.")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if not WORKBOOK.exists():
        print(f"ERROR: no se encontro {WORKBOOK}")
        return 1

    shutil.copy2(WORKBOOK, WORKBOOK.with_suffix(".xlsx.bak"))
    workbook = openpyxl.load_workbook(WORKBOOK)
    sheet = workbook["Puntuacion"]
    header = [c.value for c in sheet[1]]
    col = {h: i for i, h in enumerate(header)}

    questions, existing = {}, set()
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if not row[col["Escenario"]]:
            continue
        questions.setdefault(row[col["Indicador"]], row[col["Pregunta observable"]])
        existing.add((row[col["Escenario"]], row[col["Producto"]], row[col["Indicador"]]))

    added = 0
    for indicator in ORDER:
        if (SCENARIO, PRODUCT, indicator) in existing:
            continue
        value, ev_type, evidence, source = VALUES[indicator]
        prefix = "".join(ch for ch in indicator if ch.isalpha())
        sheet.append({
            col["Escenario"] + 1: SCENARIO,
            col["Categoria"] + 1: CATEGORY,
            col["Producto"] + 1: PRODUCT,
            col["Criterio"] + 1: CRITERION_OF[prefix],
            col["Indicador"] + 1: indicator,
            col["Pregunta observable"] + 1: questions.get(indicator, ""),
            col["Valor (0-3/NE/NA)"] + 1: value,
            col["Tipo de evidencia"] + 1: ev_type,
            col["Evidencia"] + 1: evidence,
            col["Fuente"] + 1: source,
            col["Fecha de verificacion"] + 1: VERIFIED if source else "",
            col["Notas"] + 1: NOTE.format(date=VERIFIED),
        })
        added += 1

    print(f"Filas agregadas: {added}")

    after, _ = read_scores(sheet)
    results = {k: evaluate(v, BASE_W) for k, v in after.items()}
    write_results_sheet(workbook, after)
    rebuild_charts(workbook)
    workbook.save(WORKBOOK)

    key = next((k for k in results if k[0] == SCENARIO and k[2] == PRODUCT), None)
    r = results[key] if key else None

    lines = [
        "# FP-180 — IBM Cloud Cost Estimator evaluado en E4",
        "",
        f"> Generado por `apply_ibm_e4.py` el {VERIFIED}. Queda a validacion humana.",
        "",
        "## Por que",
        "",
        "FP-177 §4 admite herramientas nativas en E4 «cuando soporten estimacion previa». IBM "
        "Cloud Cost Estimator es exactamente eso, y toda la evidencia recogida para el producto "
        "describe estimacion antes del despliegue.",
        "",
        "Estaba presente solo en E1, E2, E3, E5 y E6 por pertenecer a la categoria nativa, y no "
        "puntuaba en ninguno. Sus ceros en Visibilidad y Asignacion son correctos —una "
        "calculadora no desglosa gasto real— pero lo median contra un escenario que no es el "
        "suyo.",
        "",
        "**El producto no se reclasifica**: sigue siendo cloud nativa, y ahora tambien se evalua "
        "donde FP-177 lo admite. Eso resuelve la tension registrada en "
        "`alternativas-adicionales.md` sin tocar la poblacion acordada.",
        "",
        "## Resultado",
        "",
    ]
    if r and r["score"] is not None:
        failed = [c for c in CRITICAL[SCENARIO] if c in r["means"] and r["means"][c] < 1]
        lines += [f"**S linea base {r['score']:.2f} ({r['band']}), cobertura "
                  f"{r['coverage']:.1f}%.**", ""]
        lines.append("Criterios criticos de E4: " +
                     ("cumple Precio e Integracion." if not failed
                      else "incumple " + ", ".join(failed) + "."))
    elif r:
        lines.append(f"Cobertura {r['coverage']:.1f}%: sigue bajo el umbral del 70%.")

    lines += ["", "## Estado de E4 tras esta pasada", "",
              "| Producto | S linea base | Banda | Cobertura |", "|---|---:|---|---:|"]
    scored = [(k, v) for k, v in results.items()
              if k[0] == SCENARIO and v["score"] is not None]
    for k, res in sorted(scored, key=lambda kv: -kv[1]["score"]):
        band = res["band"]
        if unevidenced_critical(SCENARIO, res):
            band = "Sin banda (critico sin evidencia)"
        lines.append(f"| {k[2]} | {res['score']:.2f} | {band} | {res['coverage']:.1f}% |")
    lines += ["",
              "Con esta incorporacion, E4 permite comparar entre si las tres calculadoras "
              "nativas de estimacion previa —AWS, Azure e IBM— en el escenario que les "
              "corresponde.", ""]
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Informe: {REPORT.name}")

    print(f"\nE4 tras la incorporacion:")
    for k, res in sorted(scored, key=lambda kv: -kv[1]["score"]):
        print(f"   {k[2]:<30} {res['score']:>6.2f}  {res['band']:<8} cob {res['coverage']:.1f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
