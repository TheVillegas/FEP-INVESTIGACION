# -*- coding: utf-8 -*-
"""FP-180 — Close the Precio criterion for the E2 platforms.

Precio is one of the two critical criteria of E2, and it was unevidenced in
CloudHealth, CloudZero and Vantage: only nOps had it scored. That produced the
distortion this matrix is meant to avoid — Vantage outranked nOps while nOps was
the only one measured on the criterion where it scored lowest.

This pass fills P1 and P2 for the three, from official documentation consulted
on 2026-09-16.

P1 asks whether the tool exposes price, currency, region, unit, period and the
relevant assumptions of the costs it reports. P2 asks whether it lets you
estimate or compare components without hiding the limits of the comparison.
Neither asks what the tool itself costs: that is FP-126's price matrix, a
separate artefact.

P1 is scenario-independent and is written to every scenario of the product;
P2 depends on the scenario and is written only to E2.

Usage: python apply_e2_price.py
"""
from __future__ import annotations

import collections
import datetime as dt
import shutil
import sys
from pathlib import Path

import openpyxl

from apply_scope_corrections import (BASE_W, evaluate, read_scores,
                                     rebuild_charts, write_results_sheet)

HERE = Path(__file__).resolve().parent
WORKBOOK = HERE / "FP-180_matriz_comparativa.xlsx"
REPORT = HERE / "investigacion-e2-precio.md"
VERIFIED = "2026-09-16"

SCENARIO_INDEPENDENT = {"P1"}          # P2 is scenario-dependent, anchored to E2

RESEARCH = {
    ("CloudHealth", "P1"): (
        2, "Oficial",
        "La documentacion define y distingue las metricas de costo y sus supuestos: «Effective "
        "Cost represents a cost inclusive of the impacts of all reduced rates and discounts, "
        "augmented with the amortization of relevant purchases (one-time or recurring) paid to "
        "cover future eligible charges». Declara ademas el origen del dato y el limite de su "
        "propio calculo: el costo amortizado se obtiene «from the AWS Cost and Usage report "
        "(CUR)» y «Tanzu CloudHealth only aggregates this value over the selected time period "
        "rather than calculating it». Los supuestos quedan visibles y reproducibles.",
        "https://techdocs.broadcom.com/us/en/vmware-tanzu/cloudhealth/tanzu-cloudhealth/saas/"
        "tnz-cloudhealth/working-with-reports-and-recommendation-of-tanzu-cloudhealth-cost-reports.html"),

    ("CloudHealth", "P2"): (
        2, "Oficial",
        "El rightsizing compara el tipo de instancia en uso contra el propuesto y declara que "
        "las recomendaciones «consider RI discounts, EDP, Convertible Reserved Instance, and "
        "Savings plan availed by the source instance type», y que el Effective Savings Rate "
        "«includes discounts obtained from Negotiated Contracts (such as EDP)». Es un calculo "
        "definido con los limites de equivalencia explicitados.",
        "https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/"
        "cloudhealth/saas/index/working-with-reports-and-recommendation-of-tanzu-cloudhealth-"
        "working-with-reports-recommendations/working-with-reports-and-recommendation-of-tanzu-"
        "cloudhealth-aws-rightsizing-new.html"),

    ("CloudZero", "P1"): (
        2, "Oficial",
        "Los Cost Types documentan, uno por uno, que calculo aplica cada vista sobre el dato de "
        "facturacion: Real Cost «shows only the spend that engineers can directly affect by "
        "filtering out taxes, support fees, and other overhead»; Amortized Cost «starts with "
        "Billed Cost (before discounts) and spreads upfront and recurring Reserved Instance "
        "(RI) and Savings Plan (SP) charges across the resources they apply to, based on "
        "usage»; e Invoiced Amortized Cost amortiza solo la porcion recurrente «to ensure that "
        "total cost for a billing period reflects only charges incurred in that period». Los "
        "supuestos de cada cifra estan declarados y son reproducibles.",
        "https://docs.cloudzero.com/docs/cost-types"),

    ("CloudZero", "P2"): (
        2, "Oficial",
        "On-Demand Cost «shows what you would pay for equivalent usage at on-demand rates, "
        "without any discounts, RIs, or SPs applied», lo que permite comparar el costo real "
        "contra una referencia tarifaria equivalente. El limite de la comparacion esta "
        "declarado explicitamente: «Billed Cost used as a fallback for line items without an "
        "on-demand rate», de modo que no se oculta donde la equivalencia no existe.",
        "https://docs.cloudzero.com/docs/cost-types"),

    ("Vantage", "P1"): (
        2, "Oficial",
        "El Data Dictionary documenta los campos del dato de costo y Vantage normaliza las "
        "unidades de uso para que sean comparables: «Vantage normalizes Usage Unit labels in "
        "the console for consistent spelling and capitalization». El reporte por uso declara "
        "para que proveedores hay dato de uso disponible, y los registros llevan marcada su "
        "procedencia de facturacion, de modo que precio, unidad, periodo y origen quedan "
        "visibles.",
        "https://docs.vantage.sh/data_dictionary ; https://docs.vantage.sh/usage_based_reporting"),

    ("Vantage", "P2"): (
        2, "Oficial",
        "La funcion Compare Pricing permite «explore an instance pricing comparison via "
        "ec2instances.info, which evaluates the current instance type used against the proposed "
        "instance type from the recommendation». Cada recurso recomendado muestra ademas «the "
        "past 30 days of accrued costs, savings if you follow the recommendation, and the "
        "recommended action», con el horizonte de la estimacion declarado.",
        "https://docs.vantage.sh/cost_recommendations"),
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

    before, _ = read_scores(sheet)
    before_results = {k: evaluate(v, BASE_W) for k, v in before.items()}

    changes = []
    for row in range(2, sheet.max_row + 1):
        scenario = sheet.cell(row, col["Escenario"]).value
        product = sheet.cell(row, col["Producto"]).value
        indicator = sheet.cell(row, col["Indicador"]).value
        target = RESEARCH.get((product, indicator))
        if not target or scenario == "VALIDACION":
            continue
        if indicator not in SCENARIO_INDEPENDENT and scenario != "E2":
            continue
        cell = sheet.cell(row, col["Valor (0-3/NE/NA)"])
        if str(cell.value).strip().upper() != "NE":
            continue
        value, ev_type, evidence, source = target
        cell.value = value
        sheet.cell(row, col["Tipo de evidencia"]).value = ev_type
        sheet.cell(row, col["Evidencia"]).value = evidence
        sheet.cell(row, col["Fuente"]).value = source
        sheet.cell(row, col["Fecha de verificacion"]).value = VERIFIED
        note_cell = sheet.cell(row, col["Notas"])
        note = (f"Investigacion del criterio Precio de E2 ({VERIFIED}): celda completada con "
                "evidencia propia verificada contra documentacion oficial. Precio es criterio "
                "critico de E2 y estaba sin evidenciar en este producto.")
        note_cell.value = f"{note_cell.value} | {note}" if note_cell.value else note
        changes.append({"esc": scenario, "prod": product, "ind": indicator})

    print(f"Celdas completadas: {len(changes)} filas")

    after, _ = read_scores(sheet)
    after_results = {k: evaluate(v, BASE_W) for k, v in after.items()}
    write_results_sheet(workbook, after)
    rebuild_charts(workbook)
    workbook.save(WORKBOOK)

    if changes:
        lines = [
            "# FP-180 — Criterio Precio de E2 completado",
            "",
            f"> Generado por `apply_e2_price.py` el {VERIFIED}. Evidencia verificada contra "
            "documentacion oficial. Queda a validacion humana.",
            "",
            "## Por que",
            "",
            "Precio es uno de los dos criterios criticos de E2 y estaba sin evidenciar en "
            "CloudHealth, CloudZero y Vantage: solo nOps lo tenia medido. Eso producia la "
            "distorsion que esta matriz busca evitar — Vantage superaba a nOps siendo que nOps "
            "era el unico medido en el criterio donde saco su nota mas baja.",
            "",
            "Conviene recordar que P1 y P2 **no miden cuanto cuesta la herramienta**. P1 "
            "pregunta si expone precio, moneda, region, unidad, periodo y supuestos de los "
            "costos que reporta; P2, si permite estimar o comparar componentes sin ocultar los "
            "limites de la equivalencia. El precio de adquisicion de cada herramienta es un "
            "artefacto distinto: la matriz de precios de FP-126.",
            "",
            f"## Celdas completadas ({len({(c['prod'], c['ind']) for c in changes})} unicas, "
            f"{len(changes)} filas)",
            "",
            "| Producto | Indicador | Valor | Fuente |",
            "|---|---|---:|---|",
        ]
        seen = set()
        for c in changes:
            key = (c["prod"], c["ind"])
            if key in seen:
                continue
            seen.add(key)
            lines.append(f"| {c['prod']} | {c['ind']} | {RESEARCH[key][0]} | "
                         f"{RESEARCH[key][3].split(' ; ')[0]} |")

        lines += ["", "## Efecto en los resultados", "",
                  "| Escenario | Producto | Antes | Despues | Cobertura antes | Cobertura despues |",
                  "|---|---|---|---|---:|---:|"]
        for k in before_results:
            o, n = before_results[k], after_results[k]
            if o["score"] == n["score"] and abs(o["coverage"] - n["coverage"]) < 0.01:
                continue
            fmt = lambda r: (f"{r['score']:.2f} ({r['band']})" if r["score"] is not None
                             else "Insufficient evidence")
            lines.append(f"| {k[0]} | {k[2]} | {fmt(o)} | {fmt(n)} | "
                         f"{o['coverage']:.1f}% | {n['coverage']:.1f}% |")
        lines.append("")
        REPORT.write_text("\n".join(lines), encoding="utf-8")
        print(f"Informe: {REPORT.name}")
    else:
        print(f"Sin celdas pendientes; se conserva {REPORT.name} tal como estaba.")

    e2 = {k: v for k, v in after_results.items() if k[0] == "E2" and v["score"] is not None}
    print(f"\nE2 con puntaje ({len(e2)}):")
    for k in sorted(e2, key=lambda x: -after_results[x]["score"]):
        r = after_results[k]
        crit = "Multicloud" in r["means"] and r["means"]["Multicloud"] < 1
        print(f"   {k[2]:<30} {r['score']:>6.2f}  {r['band']:<8} cob {r['coverage']:.1f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
