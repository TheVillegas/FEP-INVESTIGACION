# -*- coding: utf-8 -*-
"""FP-180 — Scope correction pass over the comparison matrix.

Problem this fixes
------------------
The first scoring pass used ``NA`` ("no aplicable") for cells whose recorded
justification actually states a *verified absence* ("no ofrece", "no calcula",
"no expone", "no ejecuta") or a *missing investigation* ("la documentacion
revisada no describe", "no se identifico").

Under the FP-177 methodology those three states are not interchangeable:

* ``0``  = absence or non-compliance **verified** against the indicator anchor.
* ``NE`` = not evidenced; excluded from the score and it **reduces coverage**.
* ``NA`` = not applicable; excluded from the score and it **renormalises the
  weights**, redistributing the missing weight over the remaining criteria.

Because ``NA`` renormalises, marking a verified absence as ``NA`` removes the
penalty and redistributes that weight to the criteria where the product does
well. A narrow product then outscores a broad one that genuinely covers the
scenario. That is the "missing data turned into an advantage" outcome the
FP-180 completion criteria forbid.

This script reclassifies those cells from the evidence text already recorded in
the workbook. It adds no new research and changes no evidence or source: every
correction is traceable to the justification the cell already carried.

``NA`` is kept only where the indicator has no object for the product under the
scenario's unit of analysis (for example AU2 "safeguards before acting" when
AU1 is 0: there is no execution to safeguard).

Outputs
-------
* The workbook, with the corrected values, a traceability note per changed cell
  and a ``Resultados`` sheet holding the computed values (the formula sheet
  keeps its formulas, but openpyxl writes no cached results, so without this
  mirror the file shows no numbers unless it is opened in Excel/LibreOffice).
* ``correcciones-aplicadas.md``, the cell-by-cell change report.

Usage: python apply_scope_corrections.py
"""
from __future__ import annotations

import collections
import datetime as dt
import shutil
import sys
import unicodedata
from pathlib import Path

import openpyxl
from openpyxl.chart import BarChart, Reference

HERE = Path(__file__).resolve().parent
WORKBOOK = HERE / "FP-180_matriz_comparativa.xlsx"
REPORT = HERE / "correcciones-aplicadas.md"
TODAY = dt.date.today().isoformat()

# --- Methodology constants (FP-177) ---------------------------------------

CRITERIA = ["Visibilidad", "Asignacion", "Optimizacion", "Automatizacion",
            "Multicloud", "Integracion", "Adopcion", "Precio", "Dependencia"]
BASE_W = {c: 100.0 / 9.0 for c in CRITERIA}
SENS_W = {"Visibilidad": 15, "Asignacion": 15, "Optimizacion": 15, "Precio": 12,
          "Automatizacion": 10, "Integracion": 10, "Multicloud": 8,
          "Adopcion": 8, "Dependencia": 7}
CRITICAL = {"E1": ["Visibilidad", "Asignacion"], "E2": ["Multicloud", "Precio"],
            "E3": ["Optimizacion", "Automatizacion"], "E4": ["Precio", "Integracion"],
            "E5": ["Asignacion", "Visibilidad"], "E6": ["Visibilidad", "Integracion"]}

ABSENCE = "Oficial (ausencia verificada)"
PENDING = "Pendiente"

# --- Corrections ----------------------------------------------------------
# (product, indicator) -> (new value, evidence type, reason for the change)
# "verified absence" -> 0 ; "not investigated / not described" -> NE.

R_ABSENCE = ("La justificación registrada afirma una ausencia verificada contra "
             "documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde "
             "al valor 0, no a NA.")
R_PENDING = ("La justificación registrada indica que la documentación revisada no "
             "describe la función o que no se investigó: en FP-177 eso corresponde a "
             "NE (reduce cobertura), no a NA (renormaliza pesos).")
R_SCOPE_SPLIT = ("La justificación es una decisión de alcance del evaluador para evitar "
                 "doble conteo entre productos del mismo proveedor, no una propiedad "
                 "verificada del producto: se marca NE hasta investigarlo.")

CORRECTIONS: dict[tuple[str, str], tuple[object, str, str]] = {
    # --- AWS Cost Optimization Hub ---
    ("AWS Cost Optimization Hub", "V1"): (0, ABSENCE, R_ABSENCE),
    ("AWS Cost Optimization Hub", "V2"): (0, ABSENCE, R_ABSENCE),
    ("AWS Cost Optimization Hub", "A1"): (0, ABSENCE, R_ABSENCE),
    ("AWS Cost Optimization Hub", "A2"): (0, ABSENCE, R_ABSENCE),
    ("AWS Cost Optimization Hub", "AU1"): (0, ABSENCE, R_ABSENCE),
    ("AWS Cost Optimization Hub", "M1"): (0, ABSENCE, R_ABSENCE),
    ("AWS Cost Optimization Hub", "M2"): (0, ABSENCE, R_ABSENCE),
    ("AWS Cost Optimization Hub", "P1"): (0, ABSENCE, R_ABSENCE),
    ("AWS Cost Optimization Hub", "P2"): (0, ABSENCE, R_ABSENCE),
    ("AWS Cost Optimization Hub", "AD2"): ("NE", PENDING, R_PENDING),
    ("AWS Cost Optimization Hub", "D1"): ("NE", PENDING, R_SCOPE_SPLIT),
    ("AWS Cost Optimization Hub", "D2"): ("NE", PENDING, R_SCOPE_SPLIT),
    # AU2 stays NA: with AU1 = 0 there is no execution whose safeguards to assess.

    # --- Google Cloud Billing ---
    ("Google Cloud Billing", "O1"): (0, ABSENCE, R_ABSENCE),
    ("Google Cloud Billing", "O2"): (0, ABSENCE, R_ABSENCE),

    # --- Google Cloud FinOps Hub ---
    ("Google Cloud FinOps Hub", "V1"): (0, ABSENCE, R_ABSENCE),
    ("Google Cloud FinOps Hub", "V2"): (0, ABSENCE, R_ABSENCE),
    ("Google Cloud FinOps Hub", "A1"): (0, ABSENCE, R_ABSENCE),
    ("Google Cloud FinOps Hub", "A2"): (0, ABSENCE, R_ABSENCE),
    ("Google Cloud FinOps Hub", "M1"): (0, ABSENCE, R_ABSENCE),
    ("Google Cloud FinOps Hub", "M2"): (0, ABSENCE, R_ABSENCE),
    ("Google Cloud FinOps Hub", "P1"): (0, ABSENCE, R_ABSENCE),
    ("Google Cloud FinOps Hub", "P2"): (0, ABSENCE, R_ABSENCE),
    # AU1 = 1 (review-and-apply), so AU2 does have an object here:
    ("Google Cloud FinOps Hub", "AU2"): ("NE", PENDING, R_PENDING),
    ("Google Cloud FinOps Hub", "D1"): ("NE", PENDING, R_SCOPE_SPLIT),
    ("Google Cloud FinOps Hub", "D2"): ("NE", PENDING, R_SCOPE_SPLIT),

    # --- OpenCost ---
    ("OpenCost", "O2"): (0, ABSENCE, R_ABSENCE),
    ("OpenCost", "P1"): ("NE", PENDING,
                         "La justificación NA reinterpreta P1 como estimación previa al "
                         "despliegue; FP-177 define P1 como exposición de precio, moneda, "
                         "región, unidad y supuestos, que sí tiene objeto para una "
                         "herramienta de costo de clúster. Queda NE hasta investigarlo."),
    ("OpenCost", "P2"): ("NE", PENDING,
                         "Mismo motivo que P1: el indicador tiene objeto y no fue investigado."),
    # AU2 stays NA: AU1 = 0.

    # --- Kubecost / Cast AI (same P1/P2 reinterpretation) ---
    ("Kubecost", "P1"): ("NE", PENDING,
                         "La justificación NA reinterpreta P1 como estimación previa al "
                         "despliegue; el indicador tiene objeto y no fue investigado."),
    ("Kubecost", "P2"): ("NE", PENDING, "Mismo motivo que P1."),
    ("Cast AI", "P1"): ("NE", PENDING,
                        "La justificación NA reinterpreta P1 como estimación previa al "
                        "despliegue; el indicador tiene objeto y no fue investigado."),
    ("Cast AI", "P2"): ("NE", PENDING, "Mismo motivo que P1."),

    # --- StormForge: every justification says the reviewed docs do not describe it ---
    ("StormForge", "V1"): ("NE", PENDING, R_PENDING),
    ("StormForge", "V2"): ("NE", PENDING, R_PENDING),
    ("StormForge", "A1"): ("NE", PENDING, R_PENDING),
    ("StormForge", "A2"): ("NE", PENDING, R_PENDING),
    ("StormForge", "M1"): ("NE", PENDING, R_PENDING),
    ("StormForge", "M2"): ("NE", PENDING, R_PENDING),
    ("StormForge", "P1"): ("NE", PENDING, R_PENDING),
    ("StormForge", "P2"): ("NE", PENDING, R_PENDING),

    # --- Infracost: AU1 is a verified absence; V2/A1/A2/AU2 stay NA (see module docstring) ---
    ("Infracost", "AU1"): (0, ABSENCE, R_ABSENCE),

    # --- Cloud Custodian ---
    ("Cloud Custodian", "V1"): (0, ABSENCE, R_ABSENCE),
    ("Cloud Custodian", "V2"): (0, ABSENCE, R_ABSENCE),
    ("Cloud Custodian", "A1"): (0, ABSENCE, R_ABSENCE),
    ("Cloud Custodian", "A2"): (0, ABSENCE, R_ABSENCE),
    ("Cloud Custodian", "O2"): (0, ABSENCE, R_ABSENCE),
    ("Cloud Custodian", "P1"): (0, ABSENCE, R_ABSENCE),
    ("Cloud Custodian", "P2"): (0, ABSENCE, R_ABSENCE),
}

NOTE_TEMPLATE = ("Corrección de alcance FP-180 ({date}): el valor pasa de NA a {new}. "
                 "{reason} La evidencia y la fuente originales no se modifican.")


def strip_accents(text: object) -> str:
    return "".join(ch for ch in unicodedata.normalize("NFD", str(text))
                   if unicodedata.category(ch) != "Mn").strip()


def band(score: float) -> str:
    if score < 50 / 3:
        return "Insufficient"
    if score < 50:
        return "Basic"
    if score < 250 / 3:
        return "Solid"
    return "Advanced"


def evaluate(indicators: dict[str, list], weights: dict[str, float]) -> dict:
    """Apply the FP-177 calculation to one scenario x product pair."""
    applicable, evidenced, means = [], [], {}
    for criterion, values in indicators.items():
        usable = [v for v in values if v != "NA"]
        if not usable:                       # every indicator NA -> criterion NA
            continue
        applicable.append(criterion)
        if any(v == "NE" for v in usable):   # applicable but not evidenced
            continue
        evidenced.append(criterion)
        means[criterion] = sum(usable) / len(usable)

    w_applicable = sum(weights[c] for c in applicable)
    if not w_applicable:
        return {"coverage": 0.0, "score": None, "band": "Sin criterios aplicables",
                "means": means, "applicable": applicable}

    coverage = 100.0 * sum(weights[c] for c in evidenced) / w_applicable
    if coverage < 70.0:
        return {"coverage": coverage, "score": None, "band": "Insufficient evidence",
                "means": means, "applicable": applicable}

    w_evidenced = sum(weights[c] for c in evidenced)
    score = sum(100.0 * weights[c] / w_evidenced * means[c] / 3.0 for c in evidenced)
    return {"coverage": coverage, "score": score, "band": band(score), "means": means,
            "applicable": applicable}


def unevidenced_critical(scenario: str, result: dict) -> list[str]:
    """Critical criteria of the scenario that apply but were never evidenced.

    Team decision of 2026-09-17: a critical criterion left without evidence
    removes the comparative band, exactly as insufficient coverage does. The pair
    keeps its score but cannot be placed in the scenario or carried into a
    recommendation, because the criterion that defines the scenario was never
    verified.

    A critical criterion marked NA does not count here: NA means the scenario
    itself does not require it of that product — as FP-177 section 4 does for
    native tools in E2, admitted only "para la parte de su proveedor" — which is
    a declared scope, not a gap in the evidence.
    """
    return [c for c in CRITICAL.get(scenario, [])
            if c in result.get("applicable", []) and c not in result["means"]]


def read_scores(sheet) -> tuple[dict, list]:
    header = [c.value for c in sheet[1]]
    col = {h: i for i, h in enumerate(header)}
    pairs: dict[tuple, dict] = collections.OrderedDict()
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if not row[col["Escenario"]]:
            continue
        raw = row[col["Valor (0-3/NE/NA)"]]
        value = raw if isinstance(raw, (int, float)) else str(raw).strip().upper()
        key = (row[col["Escenario"]], row[col["Categoria"]], row[col["Producto"]])
        criterion = strip_accents(row[col["Criterio"]])
        pairs.setdefault(key, collections.defaultdict(list))[criterion].append(value)
    return pairs, header


def apply_corrections(sheet) -> list[dict]:
    header = [c.value for c in sheet[1]]
    col = {h: i + 1 for i, h in enumerate(header)}   # 1-based for cell access
    changes = []
    for row in range(2, sheet.max_row + 1):
        product = sheet.cell(row, col["Producto"]).value
        indicator = sheet.cell(row, col["Indicador"]).value
        target = CORRECTIONS.get((product, indicator))
        if not target:
            continue
        cell = sheet.cell(row, col["Valor (0-3/NE/NA)"])
        if str(cell.value).strip().upper() != "NA":
            continue                                  # already corrected; stay idempotent
        new_value, evidence_type, reason = target
        cell.value = new_value
        sheet.cell(row, col["Tipo de evidencia"]).value = evidence_type
        note_cell = sheet.cell(row, col["Notas"])
        note = NOTE_TEMPLATE.format(date=TODAY, new=new_value, reason=reason)
        note_cell.value = f"{note_cell.value} | {note}" if note_cell.value else note
        changes.append({"escenario": sheet.cell(row, col["Escenario"]).value,
                        "producto": product, "indicador": indicator,
                        "nuevo": new_value, "razon": reason})
    return changes


def write_results_sheet(workbook, pairs) -> None:
    """Mirror the computed values so the file is readable without a spreadsheet engine."""
    if "Resultados" in workbook.sheetnames:
        del workbook["Resultados"]
    sheet = workbook.create_sheet("Resultados", 4)
    sheet.append([
        "Escenario", "Categoria", "Producto", "Cobertura base (%)",
        "Cobertura sensibilidad (%)", "S linea base (0-100)", "S sensibilidad (0-100)",
        "Banda linea base", "Banda sensibilidad", "Criterios criticos incumplidos",
    ])
    for (scenario, category, product), indicators in pairs.items():
        base = evaluate(indicators, BASE_W)
        sens = evaluate(indicators, SENS_W)
        failed = [c for c in CRITICAL.get(scenario, [])
                  if c in base["means"] and base["means"][c] < 1]
        unevidenced = unevidenced_critical(scenario, base)

        flag = ", ".join(f"{c} incumplido" for c in failed)
        if unevidenced:
            flag += (" | " if flag else "") + \
                "sin evidencia: " + ", ".join(unevidenced)

        # Team decision: an unevidenced critical criterion removes the band.
        base_band, sens_band = base["band"], sens["band"]
        if unevidenced and base["score"] is not None:
            base_band = "Sin banda (critico sin evidencia)"
        if unevidenced_critical(scenario, sens) and sens["score"] is not None:
            sens_band = "Sin banda (critico sin evidencia)"

        sheet.append([
            scenario, category, product,
            round(base["coverage"], 2), round(sens["coverage"], 2),
            round(base["score"], 2) if base["score"] is not None else "Insufficient evidence",
            round(sens["score"], 2) if sens["score"] is not None else "Insufficient evidence",
            base_band, sens_band, flag or "-",
        ])
    sheet.freeze_panes = "A2"
    for column, width in zip("ABCDEFGHIJ", (12, 20, 30, 18, 22, 20, 20, 22, 22, 46)):
        sheet.column_dimensions[column].width = width


def rebuild_charts(workbook) -> None:
    """Rebuild one bar chart per scenario, bound to the Resultados sheet."""
    if "Graficos" in workbook.sheetnames:
        del workbook["Graficos"]
    charts = workbook.create_sheet("Graficos")
    charts["A1"] = ("Graficos de S por escenario, vinculados a la hoja Resultados. "
                    "Los pares marcados 'Insufficient evidence' no aparecen con barra: "
                    "esa ausencia es el resultado, no un dato faltante.")
    results = workbook["Resultados"]
    rows_by_scenario = collections.defaultdict(list)
    for idx, row in enumerate(results.iter_rows(min_row=2, values_only=True), start=2):
        rows_by_scenario[row[0]].append(idx)

    anchor_row = 3
    for scenario in sorted(rows_by_scenario):
        if scenario == "VALIDACION":       # synthetic control row, not a scenario
            continue
        rows = rows_by_scenario[scenario]
        chart = BarChart()
        chart.type = "col"
        chart.title = f"{scenario} - S linea base y S sensibilidad por producto"
        chart.y_axis.title = "S (0-100)"
        chart.x_axis.title = "Producto"
        chart.height, chart.width = 8, 24
        data = Reference(results, min_col=6, max_col=7, min_row=1,
                         max_row=max(rows))                 # includes the header row
        categories = Reference(results, min_col=3, min_row=min(rows), max_row=max(rows))
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(categories)
        charts.add_chart(chart, f"A{anchor_row}")
        anchor_row += 17


def write_report(changes, before, after) -> None:
    by_product = collections.defaultdict(list)
    for change in changes:
        key = (change["producto"], change["indicador"], change["nuevo"], change["razon"])
        by_product[change["producto"]].append(key)

    lines = [
        "# FP-180 — Correcciones de alcance aplicadas",
        "",
        f"> Generado por `apply_scope_corrections.py` el {TODAY}. "
        "Propuesta de corrección metodológica pendiente de validación del equipo.",
        "",
        "## Por qué",
        "",
        "La primera pasada de puntuación usó `NA` en celdas cuya justificación registrada "
        "afirma una **ausencia verificada** («no ofrece», «no calcula», «no expone», «no "
        "ejecuta») o una **falta de investigación** («la documentación revisada no "
        "describe», «no se identificó»).",
        "",
        "En FP-177 los tres estados no son intercambiables: `0` es ausencia verificada y "
        "penaliza; `NE` no evidencia y reduce la cobertura; `NA` no aplica y **renormaliza "
        "los pesos**, repartiendo el peso ausente entre los criterios restantes. Marcar una "
        "ausencia verificada como `NA` elimina la penalización y la convierte en ventaja: "
        "un producto angosto supera a uno amplio que sí cubre el escenario. Es justamente "
        "lo que el criterio de término de FP-180 prohíbe.",
        "",
        "Esta pasada **no agrega investigación nueva ni modifica evidencia o fuentes**: "
        "cada cambio se deriva del texto que la propia celda ya tenía registrado.",
        "",
        "`NA` se conserva donde el indicador no tiene objeto para el producto en la unidad "
        "de análisis del escenario (por ejemplo AU2, «salvaguardas antes de actuar», cuando "
        "AU1 es 0: no hay ejecución que resguardar).",
        "",
        f"## Celdas corregidas ({len(changes)} filas; "
        f"{len({(c['producto'], c['indicador']) for c in changes})} celdas únicas)",
        "",
        "| Producto | Indicador | NA → | Motivo |",
        "|---|---|---|---|",
    ]
    for product in sorted(by_product):
        for _, indicator, new, reason in sorted(set(by_product[product])):
            lines.append(f"| {product} | {indicator} | `{new}` | {reason} |")

    lines += ["", "## Efecto en los resultados", "",
              "| Escenario | Producto | S base antes | S base después | Banda antes | Banda después |",
              "|---|---|---:|---:|---|---|"]
    for key in before:
        old, new = before[key], after[key]
        if old["score"] == new["score"] and old["band"] == new["band"]:
            continue
        fmt = lambda r: (f"{r['score']:.2f}" if r["score"] is not None else "—")
        lines.append(f"| {key[0]} | {key[2]} | {fmt(old)} | {fmt(new)} | "
                     f"{old['band']} | {new['band']} |")

    lines += ["", "## Qué sigue sin resolver", "",
              "Esta corrección no toca el segundo defecto de fondo: la puntuación sigue "
              "siendo idéntica para un mismo producto en todos sus escenarios, de modo que "
              "la unidad de análisis producto × escenario que declara FP-177 todavía no "
              "está implementada. Requiere re-evaluar los indicadores sensibles al "
              "escenario (V1, V2, A2, O1, AU1, M1, M2, I1, I2, P2, AD1) contra las entradas "
              "y salidas de cada escenario, con investigación documental adicional.", ""]
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if not WORKBOOK.exists():
        print(f"ERROR: no se encontro {WORKBOOK}")
        return 1

    backup = WORKBOOK.with_suffix(".xlsx.bak")
    shutil.copy2(WORKBOOK, backup)
    print(f"Respaldo: {backup.name}")

    workbook = openpyxl.load_workbook(WORKBOOK)
    scores = workbook["Puntuacion"]

    before, _ = read_scores(scores)
    before_results = {k: evaluate(v, BASE_W) for k, v in before.items()}

    changes = apply_corrections(scores)
    print(f"Filas corregidas: {len(changes)}")

    after, _ = read_scores(scores)
    after_results = {k: evaluate(v, BASE_W) for k, v in after.items()}

    write_results_sheet(workbook, after)
    rebuild_charts(workbook)
    workbook.save(WORKBOOK)
    if changes:
        write_report(changes, before_results, after_results)
        print(f"Informe: {REPORT.name}")
    else:
        # Nothing left to correct: keep the report of the pass that did the work.
        print(f"Sin cambios pendientes; se conserva {REPORT.name} tal como estaba.")

    changed = sum(1 for k in before_results
                  if before_results[k]["score"] != after_results[k]["score"])
    print(f"Pares con resultado modificado: {changed} de {len(before_results)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
