# -*- coding: utf-8 -*-
"""FP-181 — Sensitivity analysis and per-criterion profiles.

FP-181 must explain "limitaciones y sensibilidad a las ponderaciones". FP-177
defines when that sensitivity is material: it changes the descriptive level or
the ordering "entre herramientas comparables dentro del mismo escenario y
categoria". Both conditions are evaluated here, per scenario and per category,
rather than by eyeballing the two score columns.

It also emits the per-criterion means of every scored pair, which is what turns
a score into an interpretation: where a product is strong, where it is weak, and
which of its criteria were never evidenced.

Reads the FP-180 workbook; writes nothing to it.

Usage: python analisis_sensibilidad.py
"""
from __future__ import annotations

import collections
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "fp-180"))

from apply_scope_corrections import (BASE_W, CRITICAL, SENS_W, evaluate,  # noqa: E402
                                     read_scores, unevidenced_critical)

MATRIX = (Path(__file__).resolve().parents[1] / "fp-180" /
          "FP-180_matriz_comparativa.xlsx")
CRITERIA = ["Visibilidad", "Asignacion", "Optimizacion", "Automatizacion", "Multicloud",
            "Integracion", "Adopcion", "Precio", "Dependencia"]


def band_of(result):
    return result["band"]


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    workbook = openpyxl.load_workbook(MATRIX)
    pairs, _ = read_scores(workbook["Puntuacion"])

    rows = []
    for (scenario, category, product), indicators in pairs.items():
        if scenario == "VALIDACION":
            continue
        base = evaluate(indicators, BASE_W)
        sens = evaluate(indicators, SENS_W)
        if base["score"] is None:
            continue
        rows.append({
            "esc": scenario, "cat": category, "prod": product,
            "base": base, "sens": sens,
            "sin_evid": unevidenced_critical(scenario, base),
            "fallidos": [c for c in CRITICAL.get(scenario, [])
                         if c in base["means"] and base["means"][c] < 1],
        })

    print("=" * 96)
    print("1. SENSIBILIDAD A LAS PONDERACIONES")
    print("=" * 96)
    print("FP-177: la sensibilidad es material si cambia el nivel descriptivo (banda) o el")
    print("orden entre herramientas comparables dentro del mismo escenario y categoria.\n")

    material = []
    by_group = collections.defaultdict(list)
    for r in rows:
        by_group[(r["esc"], r["cat"])].append(r)

    for (scenario, category), group in sorted(by_group.items()):
        if len(group) < 2:
            continue
        order_base = [g["prod"] for g in sorted(group, key=lambda g: -g["base"]["score"])]
        order_sens = [g["prod"] for g in sorted(group, key=lambda g: -g["sens"]["score"])]
        band_changes = [g for g in group if band_of(g["base"]) != band_of(g["sens"])]
        swapped = order_base != order_sens

        if swapped or band_changes:
            material.append((scenario, category, order_base, order_sens, band_changes))
            print(f"  [MATERIAL] {scenario} / {category}")
            if swapped:
                print(f"      orden base: {' > '.join(order_base)}")
                print(f"      orden sens: {' > '.join(order_sens)}")
            for g in band_changes:
                print(f"      banda {g['prod']}: {band_of(g['base'])} -> {band_of(g['sens'])}")
        else:
            print(f"  [no material] {scenario} / {category}  ({len(group)} productos)")

    print(f"\n  Grupos comparables con sensibilidad material: {len(material)}")

    print("\n  Variacion individual base -> sensibilidad:")
    for r in sorted(rows, key=lambda r: -abs(r["sens"]["score"] - r["base"]["score"]))[:10]:
        delta = r["sens"]["score"] - r["base"]["score"]
        print(f"      {r['esc']} {r['prod']:<30} {r['base']['score']:>6.2f} -> "
              f"{r['sens']['score']:>6.2f}  ({delta:+.2f})")

    print()
    print("=" * 96)
    print("2. PERFIL POR CRITERIO DE CADA PAR PUNTUADO  (C_c, escala 0-3)")
    print("=" * 96)
    head = f"{'Esc':<4}{'Producto':<28}" + "".join(f"{c[:4]:>6}" for c in CRITERIA) + "   Cob%"
    print(head)
    for r in sorted(rows, key=lambda r: (r["esc"], -r["base"]["score"])):
        cells = ""
        for c in CRITERIA:
            if c in r["base"]["means"]:
                cells += f"{r['base']['means'][c]:>6.1f}"
            elif c in r["base"].get("applicable", []):
                cells += f"{'NE':>6}"
            else:
                cells += f"{'NA':>6}"
        print(f"{r['esc']:<4}{r['prod'][:27]:<28}{cells}   {r['base']['coverage']:.0f}")

    print()
    print("=" * 96)
    print("3. CRITERIOS CRITICOS: INCUMPLIDOS Y SIN EVIDENCIA")
    print("=" * 96)
    for r in sorted(rows, key=lambda r: (r["esc"], r["prod"])):
        if r["fallidos"] or r["sin_evid"]:
            partes = []
            if r["fallidos"]:
                partes.append("incumple " + ", ".join(r["fallidos"]))
            if r["sin_evid"]:
                partes.append("sin evidencia en " + ", ".join(r["sin_evid"]))
            print(f"   {r['esc']} {r['prod']:<30} {' | '.join(partes)}")

    print()
    print("=" * 96)
    print("4. FORTALEZA Y DEBILIDAD DOMINANTE POR PRODUCTO")
    print("=" * 96)
    by_product = collections.defaultdict(list)
    for r in rows:
        by_product[r["prod"]].append(r)
    for product, rs in sorted(by_product.items()):
        means = rs[0]["base"]["means"]
        if not means:
            continue
        best = max(means.items(), key=lambda kv: kv[1])
        worst = min(means.items(), key=lambda kv: kv[1])
        scens = ",".join(sorted(r["esc"] for r in rs))
        print(f"   {product:<30} [{scens:<14}] fuerte: {best[0]} {best[1]:.1f} | "
              f"debil: {worst[0]} {worst[1]:.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
