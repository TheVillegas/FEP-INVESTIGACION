# Diseño de plantilla TCO a 60 meses

La plantilla compara la misma arquitectura entre **Chile Central** y **East US** durante **60 meses**. No incorpora valores de FP-182: los campos que requieren ese insumo permanecen vacíos y con estado **Pendiente**.

## Modelo de dos hojas

| Hoja | Propósito | Estructura |
|---|---|---|
| **Parámetros** | Centraliza los supuestos globales y el catálogo de precios/fuentes. | Una única tabla editable con registros de tipo `Configuración` o `Precio/fuente`. Incluye identificador, región, valor/precio, unidad, moneda, fuente, URL, fecha de corte, estado y notas. |
| **Ítems TCO** | Registra el costo comparable a nivel de componente/región/entorno/categoría. | Una tabla filtrable: cada fila es un ítem de costo. Incluye consumo mensual, precio unitario, meses, costo mensual, TCO a 60 meses, referencia al catálogo y estado. |

Ambas hojas contienen una instrucción breve y congelan la fila de encabezados. Las tablas usan filtros y anchos de columna acotados para trabajar sin áreas decorativas vacías.

## Reglas de carga y cálculo

1. Conservar el período de comparación en 60 meses y cargar ambas regiones: Chile Central y East US.
2. Completar valores, SKU, consumo, moneda y precios únicamente con evidencia validada de FP-182 y su fuente oficial.
3. Registrar cada precio con región, unidad, moneda, fecha de corte, URL y estado antes de usarlo en un ítem TCO.
4. Las columnas **Costo mensual** y **TCO 60 meses** sólo calculan cuando existen los insumos necesarios; de otro modo quedan vacías. No se interpreta un dato faltante como cero.
5. Mantener **Pendiente** hasta que el ítem tenga trazabilidad suficiente; usar filtros por región, categoría o estado para revisar faltantes.

## Filas iniciales

La hoja **Parámetros** contiene el período y las dos regiones exigidas, más filas pendientes para moneda, fecha de corte, redondeo y precios regionales. La hoja **Ítems TCO** trae pares de filas pendientes para las categorías de cómputo, almacenamiento, red, licencias, soporte y operaciones en cada región. Estas filas son estructura de carga, no estimaciones ni valores de FP-182.
