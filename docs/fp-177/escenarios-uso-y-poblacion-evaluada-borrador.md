# FP-177 — Escenarios de uso y población evaluada

> **Estado:** Borrador generado con IA; pendiente de validación humana. Ningún escenario está aprobado hasta que el equipo lo firme.
>
> **Contexto seleccionado:** GENERAL (no específico de ONEBYTE). Este documento operacionaliza el alcance de Jira para revisión del equipo; no presenta una metodología final aprobada ni asigna puntajes de proveedores. La metodología y matriz comunes propuestas se documentan en `metodologia-comparativa-borrador.md` y `matriz-criterios-y-ponderaciones-borrador.md`.

## 1. Propósito, alcance y unidad de análisis

**Propósito.** Proponer un conjunto acotado y comparable de escenarios para evaluar herramientas y prácticas de gestión de costos cloud según los nueve criterios de FP-177: visibilidad, asignación, optimización, automatización, multicloud, integración, adopción, precio y dependencia.

**Alcance.** La población evaluada comprende **productos** y **perfiles de usuario/organización**. La comparación se realiza en condiciones declaradas por escenario, con datos de entrada mínimos equivalentes. Los criterios provienen de la decisión de alcance de Jira FP-177; la evidencia académica respalda contextos, problemas y límites, pero no decide por sí sola la selección ni la puntuación de herramientas.

**Unidad de análisis.** Cada observación es el ajuste entre una **categoría de producto elegible** y un **perfil organizacional**, ante un escenario con entradas y salidas definidas. No es una afirmación de rendimiento general ni una clasificación definitiva de un proveedor.

**Inclusión.** Se incluyen herramientas disponibles para organizaciones cloud que puedan tratar al menos una salida del escenario con información verificable y configuración reproducible. Se incluyen perfiles que usan recursos cloud públicos, híbridos o servicios compartidos, cuando disponen de los datos mínimos indicados.

**Exclusión.** Se excluyen comparaciones basadas solo en material comercial no verificable, productos sin relación con la salida del escenario, puntajes agregados entre escenarios distintos y conclusiones sobre una organización particular. También se excluye inferir resultados de herramientas desde evidencia académica que estudia prácticas, arquitecturas o cargas de trabajo, no el producto evaluado.

## 2. Población de productos

La agrupación se conserva **exactamente** según la decisión de alcance de **FP-51**:

1. **Herramientas cloud nativas:** AWS Cost Explorer, AWS Cost Optimization Hub, Azure Cost Management, Google Cloud Billing y Google Cloud FinOps Hub.
2. **Plataformas multicloud:** Cloudability, CloudHealth, CloudZero, Vantage, Finout y nOps.
3. **Herramientas de Kubernetes:** OpenCost, Kubecost, Cast AI y StormForge.
4. **Herramientas de estimación temprana/políticas:** Infracost y Cloud Custodian, con la salvedad de clasificación indicada abajo.
5. **FOCUS** se trata como un **estándar transversal**, no como producto de proveedor.

**Decisión pendiente de clasificación:** `Cloud Custodian` requiere validación del equipo. Es una herramienta de *policy-as-code* y no principalmente una herramienta de estimación; por ello no debe clasificarse automáticamente en “estimación temprana/políticas” sin firma humana.

## 3. Población de usuarios y organizaciones

| Perfil | Roles primarios | Aplicabilidad y límite |
|---|---|---|
| Organización de nube única | Responsable FinOps/costos, ingeniería cloud, finanzas | Una cuenta o proveedor predominante; no se usa para afirmar capacidad multicloud. |
| Empresa multicloud | Responsable FinOps central, arquitectura empresarial, compras/finanzas | Dos o más proveedores o entornos con consolidación necesaria; requiere datos normalizados por proveedor. |
| Equipo intensivo en Kubernetes/plataforma | Platform engineer, SRE, responsable de clúster, FinOps | Cargas contenidas y datos de clúster/namespace; no representa cargas sin Kubernetes. |
| Equipo de predespliegue/IaC | Desarrollador, DevOps, arquitecto de soluciones, revisor de IaC | Estimación o control antes del despliegue; no sustituye la medición de gasto real posterior. |
| Entorno de servicios compartidos/multi-tenant | Operaciones de plataforma, propietario de servicio, finanzas/chargeback | Servicios compartidos por varias entidades; exige reglas explícitas de atribución. |
| Carga distribuida/científica grande | Operador de infraestructura, gestor de datos/workloads, finanzas de proyecto | Cómputo y datos distribuidos de gran escala; la transferencia de red y acuerdos comerciales pueden dominar el costo. |

La evidencia de Manurung y Aji cubre seis arquitectos de infraestructura cloud de SaaS, fintech, viajes, consultoría y e-grocery, con gasto anual de USD 1M–12,5M; informa perfiles comparables, no una distribución universal de organizaciones (`01_Manurung_Aji_2025_FinOps_Implementation.pdf`, pp. 709–718). Cloud PricingOps sustenta la colaboración entre ingeniería, finanzas y liderazgo/negocio, no una jerarquía obligatoria de roles (`applsci-14-11946-v2.pdf`, §3.1, pp. 6–7).

## 4. Escenarios comparables propuestos

### E1 — Visibilidad y asignación en una nube única
- **Objetivo:** verificar si la herramienta permite explicar gasto y uso por cuenta, servicio, etiqueta y unidad responsable.
- **Perfil organizacional:** organización de nube única.
- **Carga/contexto:** servicios de aplicación y datos con presupuestos y responsables definidos.
- **Entradas mínimas:** exportación de costos/uso; inventario de recursos; etiquetas o estructura de cuentas; mapeo de responsable o centro de costo.
- **Categorías elegibles:** herramientas cloud nativas; plataformas multicloud; FOCUS como formato transversal cuando sea aplicable.
- **Salidas esperadas:** desglose trazable, gasto no asignado y reporte de asignación/showback.
- **Criterios principales tensionados:** visibilidad, asignación, integración, adopción.
- **Base de evidencia:** problemas de propiedad, presupuesto y gobernanza en organizaciones tecnológicas (`01_Manurung_Aji_2025_FinOps_Implementation.pdf`, pp. 709–718); colaboración de ingeniería, finanzas y negocio (`applsci-14-11946-v2.pdf`, §3.1, pp. 6–7). La selección de criterios es decisión de Jira FP-177.
- **Limitaciones conocidas:** las seis entrevistas de Manurung y Aji no generalizan estadísticamente; las etiquetas incompletas limitan cualquier salida.
- **Decisión humana:** [ ] Aprobar  [ ] Modificar  [ ] Rechazar<br>
  **Fundamento:** ____________________  **Revisor/a:** ____________________  **Fecha:** __________

### E2 — Consolidación multicloud y comparación de precios
- **Objetivo:** examinar la consolidación de costos y la lectura de diferencias de precio entre proveedores sin convertirla en un puntaje de proveedor.
- **Perfil organizacional:** empresa multicloud.
- **Carga/contexto:** servicios funcionalmente comparables repartidos entre dos o más nubes.
- **Entradas mínimas:** datos de facturación/uso por proveedor, catálogo de servicios, moneda/período y reglas de normalización.
- **Categorías elegibles:** plataformas multicloud; herramientas cloud nativas para la parte de su proveedor; FOCUS como estándar transversal.
- **Salidas esperadas:** vista consolidada, supuestos de normalización y comparación de componentes de precio.
- **Criterios principales tensionados:** multicloud, precio, visibilidad, dependencia, integración.
- **Base de evidencia:** el marco Cloud PricingOps trata análisis, comparación y predicción de políticas de precios entre servicios y proveedores (`applsci-14-11946-v2.pdf`, §3.3, pp. 7–8). La necesidad de evaluar multicloud es alcance Jira FP-177.
- **Limitaciones conocidas:** precios, descuentos y contratos cambian; equivalencia funcional entre servicios no debe suponerse.
- **Decisión humana:** [ ] Aprobar  [ ] Modificar  [ ] Rechazar<br>
  **Fundamento:** ____________________  **Revisor/a:** ____________________  **Fecha:** __________

### E3 — Optimización y automatización en Kubernetes
- **Objetivo:** evaluar la capacidad de detectar y operar recomendaciones basadas en utilización dentro de un clúster, dejando trazada la intervención humana o automática.
- **Perfil organizacional:** equipo intensivo en Kubernetes/plataforma.
- **Carga/contexto:** cargas contenidas con variación de demanda, namespaces y asignaciones de recursos.
- **Entradas mínimas:** costos del proveedor, métricas de clúster/workload, requests/limits y mapeo namespace-equipo.
- **Categorías elegibles:** herramientas de Kubernetes; herramientas cloud nativas; plataformas multicloud si integran datos de clúster.
- **Salidas esperadas:** costo por namespace/workload, recomendaciones de dimensionamiento y registro de automatización/política.
- **Criterios principales tensionados:** optimización, automatización, asignación, integración, adopción.
- **Base de evidencia:** Manurung y Aji identifican prácticas de *rightsizing* y la necesidad de formalizar políticas, sin evaluar herramientas Kubernetes (`01_Manurung_Aji_2025_FinOps_Implementation.pdf`, pp. 709–718). Los criterios y categorías son decisiones FP-51/FP-177.
- **Limitaciones conocidas:** una recomendación no prueba ahorro realizado; métricas de corto plazo pueden no representar picos de carga.
- **Decisión humana:** [ ] Aprobar  [ ] Modificar  [ ] Rechazar<br>
  **Fundamento:** ____________________  **Revisor/a:** ____________________  **Fecha:** __________

### E4 — Estimación y política antes del despliegue
- **Objetivo:** evaluar estimaciones de costo y controles/políticas sobre cambios de infraestructura antes de producción.
- **Perfil organizacional:** equipo de predespliegue/IaC.
- **Carga/contexto:** cambio propuesto en artefactos IaC con recursos y regiones declarados.
- **Entradas mínimas:** repositorio o fragmento IaC, parámetros de despliegue, precios/uso asumido y reglas de política.
- **Categorías elegibles:** herramientas de estimación temprana/políticas; herramientas cloud nativas cuando soporten estimación previa.
- **Salidas esperadas:** estimación por cambio, supuestos explícitos, hallazgos de política y evidencia de integración con el flujo de revisión.
- **Criterios principales tensionados:** precio, automatización, integración, adopción, dependencia.
- **Base de evidencia:** estudio de costo en artefactos Terraform y acciones de desarrolladores para selección, asignación y optimización (`Mining for cost awareness in the infrastructure as code artifacts of cloud-based applications An exploratory study.pdf`, §1). La inclusión como escenario es una decisión de alcance FP-177.
- **Limitaciones conocidas:** el estudio se centra en Terraform; una estimación previa depende de supuestos y no reemplaza la factura real.
- **Decisión humana:** [ ] Aprobar  [ ] Modificar  [ ] Rechazar<br>
  **Fundamento:** ____________________  **Revisor/a:** ____________________  **Fecha:** __________

### E5 — Atribución en servicio compartido/multi-tenant
- **Objetivo:** examinar la asignación de consumo y costo cuando múltiples entidades usan un servicio compartido.
- **Perfil organizacional:** entorno de servicios compartidos/multi-tenant.
- **Carga/contexto:** aplicaciones o clientes concurrentes sobre recursos no exclusivos.
- **Entradas mínimas:** métricas de uso de recurso, identificadores de entidad/solicitud cuando existan, reglas de reparto y período de observación.
- **Categorías elegibles:** herramientas cloud nativas; plataformas multicloud; herramientas de Kubernetes cuando el servicio compartido se ejecute en clúster.
- **Salidas esperadas:** consumo/costo atribuido, porción no atribuible, método de reparto y trazabilidad de sus supuestos.
- **Criterios principales tensionados:** asignación, visibilidad, integración, adopción.
- **Base de evidencia:** los desafíos de contabilización con servicios compartidos, identidades no visibles y compartición subinstancia se describen en `04_Resource_Accounting_of_Shared_IT_Resources_in_Multi-Tenant_Clouds.pdf`, pp. 302–307. La traducción a criterio de herramienta responde a FP-177.
- **Limitaciones conocidas:** la atribución fina puede requerir instrumentación que la herramienta no provee; no se debe confundir exactitud de medición del estudio con exactitud del producto.
- **Decisión humana:** [ ] Aprobar  [ ] Modificar  [ ] Rechazar<br>
  **Fundamento:** ____________________  **Revisor/a:** ____________________  **Fecha:** __________

### E6 — Carga distribuida/científica de gran escala
- **Objetivo:** evaluar visibilidad de costo total, integración de datos/workloads y sensibilidad a red en una carga distribuida de gran escala.
- **Perfil organizacional:** carga distribuida/científica grande.
- **Carga/contexto:** procesamiento y almacenamiento distribuidos con transferencia de datos, elasticidad o *bursting*.
- **Entradas mínimas:** uso de cómputo, almacenamiento y red; precios/contrato aplicable; datos de workflow y transferencias; horizonte temporal.
- **Categorías elegibles:** herramientas cloud nativas; plataformas multicloud; FOCUS como estándar transversal cuando admita los datos disponibles.
- **Salidas esperadas:** componentes del costo total, costo/red por workflow, alertas o controles y supuestos contractuales.
- **Criterios principales tensionados:** precio, integración, visibilidad, optimización, dependencia.
- **Base de evidencia:** evaluación ATLAS/CERN de TCO, integración y costos de red en una infraestructura científica distribuida (`s41781-024-00128-x.pdf`, resumen y §§2–4). La selección de criterios es decisión FP-177.
- **Limitaciones conocidas:** el caso ATLAS usa una arquitectura, contrato y escala particulares; no permite generalizar precios ni resultados de un proveedor.
- **Decisión humana:** [ ] Aprobar  [ ] Modificar  [ ] Rechazar<br>
  **Fundamento:** ____________________  **Revisor/a:** ____________________  **Fecha:** __________

## 5. Matriz de cobertura cualitativa

**Clave:** P = Primario; S = Secundario; NC = No central. Es cobertura del diseño de escenarios, no puntaje de proveedor.

| Escenario | Visibilidad | Asignación | Optimización | Automatización | Multicloud | Integración | Adopción | Precio | Dependencia |
|---|---|---|---|---|---|---|---|---|---|
| E1 Nube única | P | P | S | NC | NC | S | S | S | NC |
| E2 Multicloud | P | S | S | NC | P | P | S | P | P |
| E3 Kubernetes | P | P | P | P | S | P | S | S | S |
| E4 IaC previo | S | S | S | P | S | P | P | P | P |
| E5 Multi-tenant | P | P | S | NC | NC | P | S | S | NC |
| E6 Científico distribuido | P | S | P | S | S | P | S | P | P |

## 6. Amenazas a la validez y evidencia faltante

- No hay en la evidencia mapeada un benchmark actual, directo y neutral de proveedores que permita puntuar productos de forma definitiva.
- La evidencia académica informa problemas y contextos; no prueba capacidades, precio vigente, facilidad de adopción o dependencia de una herramienta comercial concreta.
- Los precios, descuentos, créditos, contratos y catálogos cambian con el tiempo; todo ejercicio debe fechar sus insumos.
- La comparabilidad depende de normalizar período, moneda, unidades, etiquetas, descuentos y componentes de red.
- Los estudios citados tienen límites de contexto: seis participantes y muestreo intencional en Manurung y Aji; Terraform en Feitosa et al.; y el caso ATLAS/CERN en una organización científica concreta.
- Las salidas de asignación pueden ser inválidas sin identificadores, etiquetas o instrumentación suficiente; los recursos compartidos agravan esa amenaza.
- Falta acordar umbrales de aceptación, fuentes de datos permitidas, alternativas adicionales por categoría y la clasificación definitiva de `Cloud Custodian`.

## 7. Validación requerida

Antes de cualquier evaluación, el equipo debe: (1) aprobar o modificar cada escenario; (2) confirmar categorías y productos incluidos; (3) resolver la clasificación de `Cloud Custodian`; (4) definir fuentes, período y reglas de normalización; (5) aprobar la metodología y matriz comunes en `metodologia-comparativa-borrador.md` y `matriz-criterios-y-ponderaciones-borrador.md`; y (6) firmar el bloque de decisión de cada escenario.

**Estado final de este artefacto:** **Borrador generado con IA; pendiente de validación humana; ningún escenario está aprobado hasta que el equipo lo firme.**
