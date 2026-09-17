# -*- coding: utf-8 -*-
"""FP-180 — Score E5, attribution in shared and multi-tenant services.

E5 had no scored pair at all. Its critical criteria are Asignacion and
Visibilidad, and its expected outputs are the attributed cost, the portion that
cannot be attributed, the split method and the traceability of its assumptions.

The indicator that defines this scenario is A2, the shared-cost split rule, so
that one is investigated on its own for E5 rather than carried over. The rest of
the scenario-dependent indicators are subsumed from each product's origin
scenario under the same explicit argument used for E1: the capability to break
down and allocate cost does not change because the workload is shared, and where
it does — the split rule itself — the evidence is its own.

Products whose origin scenario has no evidence keep their NE.

Usage: python apply_e5_multitenant.py
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
REPORT = HERE / "investigacion-e5.md"
VERIFIED = "2026-09-16"
SCENARIO = "E5"

ORIGIN_BY_CATEGORY = {"Cloud nativa": "E1", "Multicloud": "E2", "Kubernetes": "E3"}
SUBSUMED = ["V1", "A1", "O1", "AU1", "I1", "I2", "AD1", "P2"]   # A2 has its own evidence

SUBSUMPTION_NOTE = (
    "Evidencia subsumida desde {origin} ({date}): la capacidad de desglosar y asignar costo no "
    "cambia porque la carga sea compartida. Lo que si es propio de E5 —la regla de reparto del "
    "costo compartido— se evalua en A2 con evidencia investigada para este escenario. La fuente "
    "y la cita originales se conservan sin cambios.")

# A2 investigated specifically against E5: the shared-cost split rule.
E5_OWN_EVIDENCE = {
    "AWS Cost Explorer": (
        2, "Oficial",
        "Las split charge rules de las Cost Categories son exactamente la regla de reparto que "
        "E5 evalua: «You can use split charge rules to allocate charges between your cost "
        "category values. Splitting charges is useful when you have costs that aren't directly "
        "attributed to a single owner, such as costs shared by multiple teams, business units, "
        "and financial owners». Los metodos estan declarados —proporcional, fijo y equitativo— "
        "y los limites tambien: hasta 10 reglas por categoria, y un valor usado como origen no "
        "puede ser destino. Para servicios compartidos en contenedores, «using split cost "
        "allocation data, you can allocate your container costs to individual business units "
        "and teams, based on how your container workloads consume shared compute and memory "
        "resources».",
        "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/splitcharge-cost-categories.html ; "
        "https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html"),

    "Azure Cost Management": (
        2, "Oficial",
        "Las reglas de asignacion de costo distribuyen el gasto compartido entre entidades: "
        "«You can create cost allocation rules to distribute costs of subscriptions, resource "
        "groups, or tags to others», eligiendo origenes y destinos y definiendo el porcentaje. "
        "Los metodos de reparto estan documentados —distribucion pareja, proporcional al costo "
        "total y proporcional al costo de computo— igual que su limite operativo: «Rules are "
        "processed in the order in which they get created and can take up to 24 hours to take "
        "effect».",
        "https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/allocate-costs ; "
        "https://learn.microsoft.com/en-us/azure/cost-management-billing/finops/capabilities-shared-cost"),

    "Google Cloud Billing": (
        1, "Oficial",
        "A diferencia de AWS y Azure, la documentacion no describe una regla de reparto de "
        "costo compartido dentro del producto, y lo reconoce de forma explicita: «Some projects "
        "include shared resources that support many tenants, but billing reports can't "
        "granularly attribute usage to individual tenants». La guia recomienda resolverlo fuera "
        "de la herramienta, por proceso interno de la organizacion: «you might assign this to a "
        "shared IT cost center or split the cost proportionally among cost centers based on the "
        "number of workloads that use the platform». El reparto existe, pero es manual y "
        "externo al producto, que es el ancla 1 del indicador. Las etiquetas y el export a "
        "BigQuery sostienen el analisis posterior, no la regla de reparto en si.",
        "https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/"
        "manage-costs-attributions ; "
        "https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage"),

    "Vantage": (
        2, "Oficial",
        "La regla de reparto nombra literalmente el caso de E5: «With percent-based cost "
        "allocation, you can filter Cost Reports to show back shared resources, like support "
        "costs or multi-tenant databases, to the team or department that uses them». Las "
        "asignaciones encadenadas permiten repartos de varios pasos reproducibles, y los "
        "segmentos garantizan que cada costo se asigne una sola vez en escenarios de "
        "showback/chargeback.",
        "https://docs.vantage.sh/vantage_university_cost_allocation ; "
        "https://docs.vantage.sh/segments"),

    "CloudZero": (
        2, "Oficial",
        "CostFormation documenta el reparto del gasto compartido y no atribuible como funcion "
        "propia, y deja explicito el remanente: «The remaining spend goes to a default element "
        "so the total always reconciles with the actual bill». La porcion no atribuible —que E5 "
        "exige mostrar— queda identificable en lugar de repartirse en silencio, y la regla es "
        "declarativa y versionable.",
        "https://docs.cloudzero.com/docs/costformation-allocating-shared-costs ; "
        "https://docs.cloudzero.com/docs/cfdl-reference"),

    "CloudHealth": (
        2, "Oficial",
        "El prorrateo esta documentado para chargeback y showback, y separa lo atribuible de lo "
        "que no lo es: clasifica «Direct Costs (which have a resource ID or asset ID associated "
        "and can be allocated to Perspective groups)» frente a «Indirect Costs (which are not "
        "associated with a resource ID or asset ID, such as support costs, and therefore cannot "
        "be attributed to a group)». Las reglas de custom line items permiten reasignar cargos "
        "indirectos entre grupos.",
        "https://techdocs.broadcom.com/us/en/vmware-tanzu/cloudhealth/tanzu-cloudhealth/saas/"
        "tnz-cloudhealth/working-with-reports-and-recommendation-of-tanzu-cloudhealth-custom-line-items.html"),
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

    # index every product's origin-scenario rows
    source = {}
    for row in sheet.iter_rows(min_row=2, values_only=True):
        key = (row[idx["Producto"]], row[idx["Escenario"]], row[idx["Indicador"]])
        source[key] = (row[idx["Valor (0-3/NE/NA)"]], row[idx["Tipo de evidencia"]],
                       row[idx["Evidencia"]], row[idx["Fuente"]])

    changes, skipped = [], []
    for row in range(2, sheet.max_row + 1):
        if sheet.cell(row, col["Escenario"]).value != SCENARIO:
            continue
        category = sheet.cell(row, col["Categoria"]).value
        product = sheet.cell(row, col["Producto"]).value
        indicator = sheet.cell(row, col["Indicador"]).value
        cell = sheet.cell(row, col["Valor (0-3/NE/NA)"])
        if str(cell.value).strip().upper() != "NE":
            continue

        if indicator == "A2" and product in E5_OWN_EVIDENCE:
            value, ev_type, evidence, src = E5_OWN_EVIDENCE[product]
            note = (f"Investigacion propia de E5 ({VERIFIED}): regla de reparto del costo "
                    "compartido verificada contra la salida esperada del escenario, que exige "
                    "el metodo de reparto y la porcion no atribuible.")
        elif indicator in SUBSUMED:
            origin = ORIGIN_BY_CATEGORY.get(category)
            if not origin:
                continue
            got = source.get((product, origin, indicator))
            if not got or str(got[0]).strip().upper() in ("NE", "NA", "NONE"):
                skipped.append((product, indicator))
                continue
            value, ev_type, evidence, src = got
            note = SUBSUMPTION_NOTE.format(origin=origin, date=VERIFIED)
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

    print(f"Celdas completadas en E5: {len(changes)}")
    print(f"Celdas sin evidencia en el escenario de origen: {len(skipped)}")

    after, _ = read_scores(sheet)
    after_results = {k: evaluate(v, BASE_W) for k, v in after.items()}
    write_results_sheet(workbook, after)
    rebuild_charts(workbook)
    workbook.save(WORKBOOK)

    lines = [
        "# FP-180 — Escenario E5, atribucion en servicio compartido o multi-tenant",
        "",
        f"> Generado por `apply_e5_multitenant.py` el {VERIFIED}. Queda a validacion humana.",
        "",
        "## Por que",
        "",
        "E5 no tenia ningun par puntuado. Sus criterios criticos son Asignacion y Visibilidad, "
        "y sus salidas esperadas son el costo atribuido, **la porcion que no se puede "
        "atribuir**, el metodo de reparto y la trazabilidad de sus supuestos.",
        "",
        "## Como se puntuo",
        "",
        "El indicador que define este escenario es A2, la regla de reparto del costo "
        "compartido, asi que se investigo **por separado para E5** en lugar de arrastrarlo. El "
        "resto de los indicadores dependientes se subsumen desde el escenario de origen de cada "
        "producto con el mismo argumento explicito usado en E1: la capacidad de desglosar y "
        "asignar costo no cambia porque la carga sea compartida; donde si cambia —la regla de "
        "reparto— la evidencia es propia.",
        "",
        "La evidencia de A2 encontrada nombra el caso de E5 de forma directa: AWS documenta "
        "split charge rules para «costs shared by multiple teams, business units, and financial "
        "owners»; Vantage menciona literalmente «multi-tenant databases»; CloudHealth separa "
        "Direct de Indirect Costs; y CloudZero deja el remanente no atribuible en un elemento "
        "identificable.",
        "",
        f"## Celdas completadas ({len(changes)})",
        "",
        "| Producto | Indicador | Valor | Tipo |",
        "|---|---|---:|---|",
    ]
    for c in sorted(changes, key=lambda x: (x["prod"], x["ind"])):
        kind = "propia de E5" if c["ind"] == "A2" else "subsumida"
        lines.append(f"| {c['prod']} | {c['ind']} | {c['val']} | {kind} |")

    lines += ["", "## Estado de E5 tras esta pasada", "",
              "| Producto | Categoria | S linea base | Banda | Cobertura |",
              "|---|---|---:|---|---:|"]
    scored = [(k, v) for k, v in after_results.items()
              if k[0] == SCENARIO and v["score"] is not None]
    for k, r in sorted(scored, key=lambda kv: -kv[1]["score"]):
        lines.append(f"| {k[2]} | {k[1]} | {r['score']:.2f} | {r['band']} | "
                     f"{r['coverage']:.1f}% |")

    unscored = sorted((k[2], v["coverage"]) for k, v in after_results.items()
                      if k[0] == SCENARIO and v["score"] is None)
    if unscored:
        lines += ["", "Siguen sin puntaje en E5: " +
                  ", ".join(f"{n} ({c:.1f}%)" for n, c in unscored) + ".",
                  "", "El motivo de cada celda pendiente esta registrado en la hoja Puntuacion."]
    lines.append("")
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Informe: {REPORT.name}")

    e5 = [(k, v) for k, v in after_results.items()
          if k[0] == SCENARIO and v["score"] is not None]
    print(f"\nE5 con puntaje ({len(e5)}):")
    for k, r in sorted(e5, key=lambda kv: -kv[1]["score"]):
        print(f"   {k[2]:<30} {r['score']:>6.2f}  {r['band']:<8} cob {r['coverage']:.1f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
