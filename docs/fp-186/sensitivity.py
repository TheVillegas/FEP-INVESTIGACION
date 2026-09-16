"""Reproduce FP-183 and run sensitivity, including discrete PostgreSQL SKUs."""
from pathlib import Path
import hashlib
import html
import json
import math
import openpyxl

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "docs/fp-183/modelo-tco-linea-base-5-anos.xlsx"
OUT = Path(__file__).resolve().parent


def evaluate(a, prices):
    """Mirror the twelve billable FP-183 lines after free-tier allocation."""
    result = []
    for month in range(int(a[7])):
        prod_cpu = max(a[8] * a[11] - a[23], 0)
        prod_mem = max(a[8] * a[12] - a[24], 0)
        prod_req = max(a[13] - a[25], 0) / 1e6
        remaining_cpu = max(a[23] - a[8] * a[11], 0)
        remaining_mem = max(a[24] - a[8] * a[12], 0)
        remaining_req = max(a[25] - a[13], 0)
        usage = [
            prod_cpu,
            prod_mem,
            prod_req,
            a[8] * a[26],
            a[14],
            a[15] * (1 + a[16]) ** (month / 12),
            max(a[17] - a[29], 0),
            a[18],
            a[27],
            max(a[19] * a[20] - remaining_cpu, 0),
            max(a[19] * a[21] - remaining_mem, 0),
            max(a[22] - remaining_req, 0) / 1e6,
        ]
        result.append([q * p for q, p in zip(usage, prices)])
    return result


def total(a, prices):
    return sum(map(sum, evaluate(a, prices)))


def main():
    original_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    book = openpyxl.load_workbook(SOURCE, data_only=True)
    assumptions = {r: book["Supuestos"].cell(r, 2).value for r in range(7, 34)}
    assert assumptions[7] == 60, "Review horizon before rerunning"
    assert all(assumptions[r] is not None for r in range(7, 30)), "Missing model input"

    # Continuous variables use a team-defined ±20% scenario. PostgreSQL vCores
    # use deployable GP sizes; 2 vCores is both the baseline and minimum.
    continuous = list(range(11, 23))
    scenarios = {
        r: [assumptions[r] * 0.8, assumptions[r], assumptions[r] * 1.2]
        for r in continuous
    }
    scenarios[26] = [2, 2, 4]
    names = {r: book["Supuestos"].cell(r, 1).value for r in scenarios}
    units = {r: book["Supuestos"].cell(r, 3).value for r in scenarios}
    regions = [("Chile Central", 7, "B7"), ("East US", 19, "C7")]
    prices, baselines, impacts, tests = {}, {}, {}, []

    for region, first, summary_cell in regions:
        prices[region] = [
            book["Fuentes y Cotizaciones"].cell(r, 6).value
            for r in range(first, first + 12)
        ]
        assert all(isinstance(v, (int, float)) and v >= 0 for v in prices[region])
        calculated = evaluate(assumptions, prices[region])
        for month in range(60):
            for i in range(12):
                cached = book["Modelo TCO"].cell(first + i, 7 + month).value
                assert isinstance(cached, (int, float)), "Missing Excel cache"
                assert math.isclose(calculated[month][i], cached, abs_tol=1e-8)
        base = total(assumptions, prices[region])
        assert math.isclose(base, book["Resumen"][summary_cell].value, abs_tol=0.01)
        baselines[region] = base
        tests.append(f"{region}: 720 costos mensuales y total conciliados con FP-183")
        impacts[region] = {}
        for row, values in scenarios.items():
            totals = []
            for value in values:
                changed = dict(assumptions)
                changed[row] = value
                totals.append(total(changed, prices[region]))
            assert totals[0] <= totals[1] <= totals[2]
            impacts[region][row] = totals
        tests.append(f"{region}: escenarios continuos y SKU PostgreSQL sin inversión de costo")

    scores = {
        r: sum(
            max(abs(v - baselines[k]) for v in impacts[k][r]) / baselines[k]
            for k in baselines
        ) / 2
        for r in scenarios
    }
    ranking = sorted(scenarios, key=lambda r: (-scores[r], r))
    selected = ranking[:2]

    def axis(row):
        if row == 26:
            return [2, 4, 8]
        return [assumptions[row] * f for f in (0.8, 0.9, 1, 1.1, 1.2)]

    axes = {str(r): axis(r) for r in selected}
    grids = {}
    for region in baselines:
        grid = []
        for x in axes[str(selected[0])]:
            line = []
            for y in axes[str(selected[1])]:
                changed = dict(assumptions)
                changed[selected[0]] = x
                changed[selected[1]] = y
                line.append(total(changed, prices[region]))
            grid.append(line)
        grids[region] = grid
        tests.append(
            f"{region}: matriz {len(grid)}x{len(grid[0])} con SKU discreto y variable continua"
        )

    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == original_hash
    tests.append("FP-183 permanece sin modificaciones (SHA-256)")
    data = dict(
        source=str(SOURCE.relative_to(ROOT)),
        sha256=original_hash,
        assumptions=assumptions,
        names=names,
        units=units,
        baselines=baselines,
        impacts=impacts,
        scenarios=scenarios,
        scores=scores,
        ranking=ranking,
        selected=selected,
        axes=axes,
        grids=grids,
        tests=tests,
    )
    (OUT / "resultados.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    esc = html.escape

    def table(headers, rows):
        return (
            "<table><thead><tr>"
            + "".join("<th>" + esc(str(x)) + "</th>" for x in headers)
            + "</tr></thead><tbody>"
            + "".join(
                "<tr>" + "".join("<td>" + esc(str(x)) + "</td>" for x in row) + "</tr>"
                for row in rows
            )
            + "</tbody></table>"
        )

    rows = []
    for r in ranking:
        low, base, high = scenarios[r]
        rows.append(
            [
                names[r], f"Supuestos!B{r}", units[r], f"{low:g} / {base:g} / {high:g}",
                *[f"{max(abs(x - baselines[k]) for x in impacts[k][r]):,.2f}" for k in baselines],
            ]
        )

    parts = [
        '<!doctype html><html lang="es"><meta charset="utf-8"><title>FP-186 Sensibilidad</title>',
        "<style>body{font:16px system-ui;max-width:1120px;margin:40px auto;padding:0 24px;color:#193249}h1,h2{color:#164d73}table{border-collapse:collapse;width:100%;margin:22px 0;font-size:14px}th,td{padding:10px;border-bottom:1px solid #ccd7df;text-align:right}th:first-child,td:first-child{text-align:left}th{background:#e8f0f5}.warning{background:#fff1d2;padding:18px;line-height:1.5}svg{max-width:100%;height:auto}</style>",
        "<h1>FP-186 · Sensibilidad del gasto cloud a 60 meses</h1>",
        "<p class='warning'>Análisis provisional del FP-183 corregido. El total no incluye esfuerzo operativo ni costos de implementación. No es una cotización ni una recomendación automática de región.</p>",
        "<h2>Resultado</h2><p>Las variables con mayor impacto son <strong>" + esc(names[selected[0]]) + "</strong> y <strong>" + esc(names[selected[1]]) + "</strong>.</p>",
        "<h2>Método</h2><p>Las variables continuas usan un escenario del equipo de −20 % y +20 %. PostgreSQL se evalúa con tamaños discretos desplegables de 2, 4 y 8 vCores; no se aplica un porcentaje fraccional a una SKU. Los papers respaldan la metodología de experimentación y optimización, no estos rangos.</p>",
        "<p>La evaluación conserva franquicias mensuales de Container Apps, 100 GB de egress gratuito y backup automático sin excedente. Las solicitudes que permanecen bajo la franquicia pueden mostrar impacto cero.</p>",
        "<h2>Ranking observado</h2>",
        table(["Variable", "Origen", "Unidad", "Bajo / base / alto", "Chile Central", "East US"], rows),
    ]

    for region in baselines:
        parts.append(f"<h2>{esc(region)} · base USD {baselines[region]:,.2f}</h2>")
        max_impact = max(max(abs(x - baselines[region]) for x in impacts[region][r]) for r in ranking)
        scale = 320 / max_impact
        svg = ['<svg viewBox="0 0 1100 450" role="img" aria-label="Gráfico tornado del cambio en costo"><line x1="700" y1="30" x2="700" y2="445" stroke="#555"/>']
        for i, r in enumerate(ranking):
            y = 42 + i * 30
            low, _, high = impacts[region][r]
            left = max(baselines[region] - low, 0) * scale
            right = max(high - baselines[region], 0) * scale
            svg.extend([
                f'<text x="0" y="{y+15}" font-size="13">{esc(names[r])}</text>',
                f'<rect x="{700-left}" y="{y}" width="{left}" height="20" fill="#198876"/>',
                f'<rect x="700" y="{y}" width="{right}" height="20" fill="#d77c26"/>',
            ])
        parts.append("".join(svg) + "</svg>")
        xrow, yrow = selected
        parts.append("<h3>Sensibilidad conjunta (USD)</h3><p>Filas: " + esc(names[xrow]) + ". Columnas: " + esc(names[yrow]) + ".</p>")
        parts.append(table(
            [names[xrow] + " / " + names[yrow], *[f"{v:g}" for v in axes[str(yrow)]]],
            [[f"{x:g}", *[f"{v:,.2f}" for v in grids[region][i]]] for i, x in enumerate(axes[str(xrow)])],
        ))

    parts.extend([
        "<h2>Verificación</h2><ul>" + "".join("<li>" + esc(t) + "</li>" for t in tests) + "</ul>",
        "<p>Ejecutar <code>python docs/fp-186/sensitivity.py</code>. Fuente: <code>" + esc(str(SOURCE.relative_to(ROOT))) + "</code>. SHA-256: <code>" + original_hash + "</code>.</p>",
        "<h2>Pendientes</h2><p>Validar rangos, SKU, HA, costos de operación e implementación y medir latencia antes de cerrar la recomendación.</p></html>",
    ])
    (OUT / "sensibilidad.html").write_text("\n".join(parts), encoding="utf-8")
    print(json.dumps({"selected": [names[r] for r in selected], "baselines": baselines, "tests": tests}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
