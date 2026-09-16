# FP-185 — Bitácora de comparación regional

## Resultado corregido

| Región | Gasto cloud modelado 60 meses |
|---|---:|
| Chile Central | USD 23.256,32 |
| East US | USD 16.474,60 |
| Diferencia | USD -6.781,72 (-29,2 %) |

La comparación mantiene idénticas arquitectura, demanda, horizonte, moneda y reglas. Las primeras cinco hojas del workbook FP-185 son copia exacta de FP-183 y la hoja `FP-185 Comparación` registra su SHA-256.

## Diferencias regionales relevantes

- PostgreSQL General Purpose v3/v4/v5 está disponible en ambas regiones.
- HA zone-redundant está disponible en ambas, pero queda desactivada en la línea base.
- Backup geo-redundante está disponible en East US y no en Chile Central.
- La residencia depende de la configuración de cada servicio/workspace; no se afirma automáticamente por el nombre de la región.
- Chile Central tiene menor latencia **esperada** para usuarios en Chile, pero falta medirla.

## Conclusión provisional

East US es más barato en el gasto cloud modelado. Chile Central puede aportar proximidad y residencia, pero la decisión no debe cerrarse sin medir latencia, validar transferencia internacional y completar el esfuerzo operativo.

## Evidencia

- `docs/fp-185/comparacion-regional-santiago-eastus.xlsx`
- `docs/fp-183/modelo-tco-linea-base-5-anos.xlsx`
- Microsoft Learn: PostgreSQL overview y Azure Monitor workspace design.
- Azure Product Availability by Region.
