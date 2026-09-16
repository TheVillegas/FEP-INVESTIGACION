# FP-184 — Trazabilidad del escenario optimizado

## Base

- Fuente: `docs/fp-183/modelo-tco-linea-base-5-anos.xlsx` corregido.
- Chile Central: USD 23.256,32 en 60 meses.
- East US: USD 16.474,60 en 60 meses.
- Alcance: gasto cloud modelado; esfuerzo operativo pendiente.

## Palancas

| Palanca | Cambio | Ahorro bruto Chile | Ahorro bruto East US | Evidencia metodológica |
|---|---|---:|---:|---|
| No producción | 264 → 132 h/mes | USD 598,75 | USD 427,68 | Manurung, Cho, Chaisiri; escalado y apagado documentados por Microsoft. |
| Logs | 50 → 40 GB/mes | USD 420,00 | USD 300,00 | Gobierno FinOps y Azure Monitor. |
| Egress | 200 → 160 GB/mes | USD 434,40 | USD 208,80 | Paper ATLAS y Azure Bandwidth Pricing. |
| **Total bruto** | Partidas distintas | **USD 1.453,15** | **USD 936,48** | Sin doble conteo. |

La fórmula de egress compara `MAX(GB−100,0)` antes y después de la palanca; no cobra los primeros 100 GB.

## Costos de implementación

El workbook agrega una entrada por palanca y región. Permanecen vacías porque no existe evidencia para inventar esas cifras. Hasta completarlas:

- no se informa ahorro neto;
- no se informa costo optimizado neto;
- FP-184 debe mantenerse en revisión.

## Uso de papers

Los papers justifican el mecanismo de optimización y la necesidad de validar bajo incertidumbre. No justifican los porcentajes 50 %/20 % ni las tarifas; esos son escenarios editables del equipo y precios oficiales, respectivamente.
