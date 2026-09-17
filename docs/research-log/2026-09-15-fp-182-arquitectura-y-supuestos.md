# Bitácora de investigación — FP-182

## Decisión vigente — 2026-09-16

- Se usa una API web contenedorizada como **escenario ilustrativo TI-06**, porque el repositorio no contiene un caso productivo más específico.
- La plataforma común es Azure Container Apps Consumption en Chile Central y East US.
- PostgreSQL cambia de “GP 1 vCore” a **General Purpose 2 vCores**, mínimo desplegable documentado.
- La línea base desactiva HA y usa backup automático de 7 días; no usa Azure Backup LTR.
- Se incorporan franquicias de Container Apps y 100 GB/mes de egress gratuitos.
- El egress usa tarifa continental de Microsoft Premium Global Network.

## Corrección de registro anterior

El registro del 15-09-2026 que indicaba que FP-183 seguía en GCP o que faltaban todas las partidas quedó **superado**. FP-183, FP-184 y FP-185 ya usan la base Azure corregida. Sigue pendiente el costo de esfuerzo operativo y la validación humana.

## Fuentes y método

- Papers FP-48: metodología de rightsizing, provisión bajo incertidumbre, políticas de precio, egress y experimentación.
- Documentación oficial: precios, franquicias, SKU, backup y disponibilidad regional.
- IA: apoyo de nivel 3 para estructuración, cálculo y trazabilidad; revisión humana obligatoria.
