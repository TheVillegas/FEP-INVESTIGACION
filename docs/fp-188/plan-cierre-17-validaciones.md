# Plan de cierre de las 17 validaciones de TINV-06

## Criterio de uso

Este plan separa tres niveles de evidencia:

1. **Dato reutilizable del repositorio:** puede precargarse porque tiene valor, unidad y fuente local identificable.
2. **Propuesta académica:** permite calcular el escenario, pero sigue siendo un proxy, supuesto o estimación.
3. **Validación de cierre:** requiere medición, dato interno o aprobación del responsable; solo esta evidencia permite cerrar el registro.

La revisión del 21-09-2026 encontró información reutilizable para 13 de las 17 validaciones. Ninguna dispone todavía de toda la evidencia formal necesaria para presentarse como dato productivo aprobado. Las cuatro sin valor reutilizable son VAL-01, VAL-02, VAL-08 y VAL-09.

## Procedimiento por validación

### STO-03 — Operaciones Blob

- **Disponible en el repositorio:** Blob Storage Hot LRS, 500 GB iniciales y crecimiento anual de 20 %. Las operaciones están excluidas por falta de volumen.
- **Precarga permitida:** capacidad y crecimiento; no registrar las operaciones como cero.
- **Cómo cerrarla:** habilitar métricas de la cuenta de almacenamiento durante un período representativo y exportar, por mes, operaciones de escritura, lectura, listado, otras operaciones, recuperación de datos y transferencia por nivel.
- **Evidencia mínima:** exportación CSV/JSON de Azure Monitor o Cost Management, período, recurso y consulta utilizada.
- **Destino:** actualizar FP-183 `Fuentes y Cotizaciones` y recalcular FP-183 a FP-188.

### OBS-03 — Consultas y retención adicional de Monitor

- **Disponible en el repositorio:** 50 GB/mes de ingesta Basic Logs, 30 días de retención y escenario optimizado de 40 GB/mes.
- **Precarga permitida:** ingesta y retención base; consultas y retención adicional siguen vacías.
- **Cómo cerrarla:** medir GB escaneados por consultas, frecuencia de consulta y días de retención efectiva por tabla durante un período representativo.
- **Evidencia mínima:** exportación de uso/facturación de Log Analytics, política de retención y lista de tablas consultadas.
- **Destino:** valorizar consultas y retención adicional en FP-183 y revisar la palanca de logs de FP-184.

### OPT-04 — Costo por palanca

- **Disponible en el repositorio:** FP-187 estima 50 h totales: 8 h de revisión y plan, 12 h de rightsizing, 10 h de programación de no producción, 8 h de logs y 12 h de control/documentación. La tarifa proxy es USD 8,534526164/h.
- **Precarga permitida:** 10 h para no producción y 8 h para logs como estimaciones de ingeniería. No asignar automáticamente las 12 h de rightsizing a egress: son actividades distintas. Las 20 h comunes tampoco deben duplicarse entre palancas.
- **Cómo cerrarla:** estimar por separado no producción, logs y egress; distribuir las horas comunes con una regla documentada y multiplicar horas aprobadas por costo empresa o tarifa aprobada.
- **Evidencia mínima:** estimación firmada, ticket o timesheet con actividad, responsable, horas y tarifa.
- **Destino:** completar `docs/fp-184/escenario-optimizado-fp-184.xlsx`, hoja `Fuentes`, celdas B17:C19.

### FIN-10 — WACC o tasa interna

- **Disponible en el repositorio:** 5,5 % anual, Tasa Social de Descuento 2026 del MDSF, cargada en FP-187 como proxy público.
- **Precarga permitida:** 5,5 % únicamente para el escenario académico; no nombrarla WACC corporativo.
- **Cómo cerrarla:** Finanzas debe informar la tasa exigida para decisiones internas, su base nominal/real, moneda y fecha de vigencia.
- **Evidencia mínima:** política financiera, correo de aprobación o acta con tasa y responsable.
- **Destino:** FP-187 `Supuestos!B8`; recalcular VAN, TIR y PRI.

### FIN-11 — Costo empresa cargado

- **Disponible en el repositorio:** USD 8,534526164/h, derivado de ingreso neto INE, jornada de 42 h y CLP 954,85/USD.
- **Precarga permitida:** usar USD 8,53/h como proxy público académico, claramente etiquetado.
- **Cómo cerrarla:** sumar remuneración bruta, cargas patronales, beneficios y overhead aplicables; dividir por horas productivas del período y convertir a USD con una fecha definida.
- **Evidencia mínima:** cálculo de Finanzas/RR. HH. anonimizado y aprobación del responsable.
- **Destino:** FP-187 `Supuestos!B14`; recalcular implementación, operación y métricas financieras.

### FIN-12 — Horas reales de implementación

- **Disponible en el repositorio:** estimación bottom-up de 50 h por alternativa regional.
- **Precarga permitida:** 50 h como estimación de ingeniería, con el desglose visible en `Supuestos!A34:C40` de FP-187.
- **Cómo cerrarla:** registrar horas reales por actividad o aprobar formalmente la estimación antes de ejecutar.
- **Evidencia mínima:** timesheet, tickets con horas o estimación aprobada y fechada.
- **Destino:** FP-187 `Supuestos!B35:B40`.

### FIN-13 — Horas reales de operación

- **Disponible en el repositorio:** 1 h/mes: 0,5 h de revisión de costo/uso, 0,25 h de anomalías/reporte y 0,25 h de seguimiento.
- **Precarga permitida:** 1 h/mes como estimación de ingeniería para una carga pequeña.
- **Cómo cerrarla:** medir al menos tres ciclos mensuales o aprobar el runbook y su esfuerzo esperado.
- **Evidencia mínima:** timesheets, tickets recurrentes o acta de aprobación del runbook.
- **Destino:** FP-187 `Supuestos!B44:B47`.

### VAL-01 — Latencia medida en Chile Central

- **Disponible en el repositorio:** solo la hipótesis de menor latencia por proximidad; no existe endpoint ni despliegue medible.
- **Cómo cerrarla:** desplegar el mismo artefacto y configuración en Chile Central; ejecutar pruebas desde la población objetivo en horarios normal y pico; registrar p50, p95, p99, errores y tamaño de muestra.
- **Evidencia mínima:** script/comando, fecha, origen, endpoint, resultados sin procesar y resumen estadístico.
- **Destino:** FP-185 `FP-185 Comparación!B15` y documentación de prueba.

### VAL-02 — Latencia medida en East US

- **Disponible en el repositorio:** no existe medición ni endpoint.
- **Cómo cerrarla:** repetir exactamente el protocolo de VAL-01 contra East US, manteniendo cliente, carga, tamaño de muestra y horario comparables.
- **Evidencia mínima:** los mismos artefactos de VAL-01 y una comparación pareada.
- **Destino:** FP-185 `FP-185 Comparación!C15`.

### VAL-03 — Residencia aprobada en Chile Central

- **Disponible en el repositorio:** la arquitectura contempla Container Apps, PostgreSQL, Blob y Monitor en Chile Central; se advierte que réplicas, logs, backups y exportaciones deben verificarse por servicio.
- **Precarga permitida:** inventario de servicios y región objetivo; no registrar “aprobado”.
- **Cómo cerrarla:** completar una ficha por servicio con región primaria, réplica, backup, logs, soporte, exportaciones y subprocesadores; Legal, Seguridad y Datos deben aprobarla.
- **Evidencia mínima:** matriz firmada o ticket aprobado con enlaces a la configuración real.
- **Destino:** FP-185 y sección 3 de FP-188.

### VAL-04 — Residencia aprobada en East US

- **Disponible en el repositorio:** los datos quedarían en EE. UU. según la configuración; se requiere revisar transferencia internacional y contrato.
- **Precarga permitida:** inventario técnico y riesgo identificado; no registrar autorización legal.
- **Cómo cerrarla:** aplicar la misma ficha de VAL-03 y adjuntar evaluación de transferencia internacional, contrato, subprocesadores y controles compensatorios.
- **Evidencia mínima:** aprobación de Legal/Seguridad/Datos y referencia contractual.
- **Destino:** FP-185 y sección 3 de FP-188.

### VAL-05 — RPO/RTO aprobados

- **Disponible en el repositorio:** backup automático de PostgreSQL por siete días; sin LTR/GRS en la línea base.
- **Precarga permitida:** retención técnica de siete días; no derivar de ella un RPO o RTO.
- **Cómo cerrarla:** Negocio define pérdida tolerable y tiempo máximo de recuperación; el equipo ejecuta una restauración y contrasta el resultado con esos objetivos.
- **Evidencia mínima:** RPO, RTO y retención aprobados, más acta o log de una prueba de recuperación.
- **Destino:** FP-182, FP-183 y gate de continuidad de FP-188.

### VAL-06 — Requisito de HA

- **Disponible en el repositorio:** escenario base sin HA, SLA público de referencia de 99,9 % y disponibilidad de HA en ambas regiones.
- **Precarga permitida:** `HA = No` para la línea base académica y `99,9 %` como referencia del servicio sin HA.
- **Cómo cerrarla:** Continuidad compara el SLO aprobado con el SLA y el RPO/RTO; si no alcanza, se crea un escenario equivalente con HA para ambas regiones.
- **Evidencia mínima:** decisión firmada con criticidad, SLA/SLO requerido y justificación.
- **Destino:** FP-182, FP-183, FP-185 y FP-188.

### VAL-07 — Requisito de soporte pagado

- **Disponible en el repositorio:** Azure Basic Support sin costo adicional; el contrato de entrada declara que el plan pago no es requerido en el escenario base.
- **Precarga permitida:** `Basic Support / USD 0 adicional` para el escenario académico.
- **Cómo cerrarla:** Operación define horario de cobertura, severidades, tiempo de respuesta y canales. Si Basic no los cubre, cotiza el plan correspondiente.
- **Evidencia mínima:** decisión aprobada y, si corresponde, cotización o página oficial del plan con fecha.
- **Destino:** FP-183 `Fuentes y Cotizaciones` y TCO.

### VAL-08 — SLO de latencia

- **Disponible en el repositorio:** no existe umbral, percentil ni población aprobados.
- **Cómo cerrarla:** Producto define la operación crítica y el usuario objetivo; SRE propone indicador, por ejemplo latencia extremo a extremo en p95, ventana de medición y presupuesto de error. El equipo aprueba el umbral antes de comparar regiones.
- **Evidencia mínima:** ficha SLI/SLO versionada con fórmula, umbral, percentil, población, ventana y dueño.
- **Destino:** gate regional de FP-185 y FP-188.

### VAL-09 — Métricas reales de rendimiento

- **Disponible en el repositorio:** no hay aplicación desplegada, infraestructura como código ni telemetría real. FP-186 solo identifica vCores PostgreSQL y vCPU de producción como variables sensibles.
- **Cómo cerrarla:** ejecutar una prueba controlada con carga representativa y capturar CPU, memoria, conexiones, latencia, errores, throughput, réplicas y escalado; repetir para cada configuración candidata.
- **Evidencia mínima:** configuración, dataset/carga, período, dashboard/exportación y criterio de rollback.
- **Destino:** FP-186, rightsizing de FP-184 y recomendación de FP-188.

### VAL-10 — Aprobación del escenario ilustrativo

- **Disponible en el repositorio:** escenario completo y consistente: Azure Container Apps, PostgreSQL Flexible Server, Blob, Monitor, dos regiones, 60 meses y USD.
- **Precarga permitida:** descripción del escenario; no atribuirle uso productivo real.
- **Cómo cerrarla:** el equipo confirma por escrito que este será el caso defendido o registra las modificaciones requeridas. Después se congela una versión o hash de los artefactos de entrada.
- **Evidencia mínima:** acta, comentario de Jira o aprobación del responsable con fecha y versión.
- **Destino:** encabezado de FP-182 y cierre de FP-188.

## Orden recomendado

1. Cerrar VAL-10 para congelar el caso académico.
2. Definir VAL-08, VAL-05, VAL-06 y VAL-07 porque determinan qué debe medirse y cotizarse.
3. Completar FIN-10 a FIN-13 y OPT-04 para recalcular FP-187.
4. Ejecutar VAL-01, VAL-02 y VAL-09 con un despliegue comparable.
5. Completar STO-03 y OBS-03 con telemetría del mismo período.
6. Obtener VAL-03 y VAL-04 antes de emitir la recomendación regional final.

## Plantilla mínima de evidencia

Para cada ID registrar: valor, unidad, alcance/región, período, método de obtención, fuente o archivo, responsable, fecha, resultado de aprobación y artefactos que deben recalcularse. Una fuente pública puede respaldar tarifas o método, pero no reemplaza telemetría ni una aprobación interna.
