# Bitácora de investigación — FP-182

> **Estado:** registro de trazabilidad. Las decisiones siguen pendientes de validación humana y no reemplazan la autoría exigida por el curso.

## Registro 1 — Corrección de plataforma para comparabilidad

- **Cambio:** se reemplazó la propuesta Google Cloud IaaS por Azure Container Apps en Chile Central y East US.
- **Motivo:** FP-48 posee precios públicos pareados para CPU, memoria y solicitudes de Azure Container Apps en ambas regiones; no posee precios GCP equivalentes registrados.
- **Evidencia:** `FP-48 TINV02/TINV_Matriz_de_Fuentes_final_2026-09-13.xlsm`, hojas `Matriz de precios` (filas 2–7) y `Alternativas` (fila 3).
- **Decisión:** usar Azure Container Apps como componente de aplicación común para comparar regiones sin mezclar proveedor, unidad ni configuración.
- **Límite:** la evidencia no cubre todavía datos, objetos, egreso, observabilidad, respaldo ni soporte. La comparación total y el TCO siguen bloqueados hasta cotizar esos componentes.
- **Fecha:** 2026-09-15.
- **Asistencia de IA:** nivel 3 para análisis y redacción. La aprobación de arquitectura, parámetros y conclusiones sigue siendo humana.

## Registro 2 — Regla de precios y replicabilidad

- **Regla:** conservar en ambos territorios imagen, CPU, memoria, solicitudes, horas, horizonte y moneda; variar solamente región y tarifa oficial del mismo medidor.
- **Fuente:** Jira FP-185 y requisito TI-06 de mantener constante arquitectura, volumen y periodo.
- **Control:** cada partida debe registrar producto/medidor, región, moneda, fecha, modalidad y URL. No se atribuye una diferencia a región si también cambia SKU o servicio.

## Registro 3 — Pendientes de continuidad

- Actualizar el modelo FP-183, que aún representa la arquitectura GCP anterior.
- Incorporar a FP-48 cotizaciones oficiales pareadas para las partidas no computacionales.
- Recién entonces calcular la tabla y el gráfico de FP-185 y seleccionar palancas/sensibilidades desde resultados completos.