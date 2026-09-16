# Diseño efectivo del modelo TCO a 60 meses

El workbook `modelo-tco-linea-base-5-anos.xlsx` tiene cinco hojas:

| Hoja | Contenido |
|---|---|
| `Resumen` | Totales regionales, alcance y limitaciones. |
| `Supuestos` | Entradas editables, franquicias y pendientes. |
| `Modelo TCO` | 60 columnas mensuales, 18 categorías por región y subtotales. |
| `Fuentes y Cotizaciones` | Configuración, unidad, precio, URL, fecha, modalidad y estado. |
| `Auditoría` | Cobertura, horizonte, regiones, franquicias y revisión de fórmulas. |

## Reglas

1. Los precios se conservan por unidad facturable y las franquicias se aplican en las fórmulas de consumo.
2. La franquicia de Container Apps se asigna primero a producción y luego a no producción.
3. PostgreSQL General Purpose usa 2 vCores; HA está fuera del caso base.
4. El egress factura `MAX(GB − 100, 0)` con tarifa continental.
5. El backup factura solo el excedente sobre el storage incluido; el caso base usa 0 GiB excedente.
6. Un input pendiente produce una celda vacía. No se reemplaza por cero.
7. El total actual es gasto cloud comparable; se convierte en TCO económico completo cuando se informen horas y tarifa de operación.

## Controles

- 60 meses por región.
- 36 categorías modeladas, 18 por región.
- 2 categorías pendientes: esfuerzo operativo, una por región.
- Reconciliación independiente de cada línea mensual.
- FP-185 clona exactamente las primeras cinco hojas y registra el SHA-256 de FP-183.
