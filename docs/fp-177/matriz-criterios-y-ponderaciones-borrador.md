# FP-177 — Matriz de criterios y ponderaciones

> **Estado:** Criterios, pesos, escala y conjuntos críticos confirmados por consenso del equipo; documento estructurado con asistencia de IA.
>
> Uso conjunto con `metodologia-comparativa-borrador.md` y `escenarios-uso-y-poblacion-evaluada-borrador.md`. No es una evaluación de proveedores.

## 1. Instrucciones de uso

La misma matriz se aplica a cada producto elegible dentro de su escenario. Antes de puntuar, registrar escenario, producto/versión, fecha de corte, región, moneda, unidades, entradas equivalentes y justificación previa de cualquier `NA`. Cada indicador recibe `0`, `1`, `2`, `3`, `NE` o `NA` según la metodología. `NE` no es cero; evidencia comercial exclusiva limita el indicador a 1; un 3 necesita documentación primaria más estudio independiente, demo reproducible o verificación práctica del equipo.

**No doble conteo:** cada hallazgo se asigna al indicador cuyo objeto mide. Una misma integración puede probar integración, pero no prueba por sí sola adopción; un desglose puede probar visibilidad, pero no atribución; una recomendación puede probar optimización, pero no automatización hasta que exista ejecución o control operativo verificable.

## 2. Matriz operacional

| Criterio e indicador | Pregunta observable | Evidencia admisible | Anclas 0 / 1 / 2 / 3 | Prevención de doble conteo |
|---|---|---|---|---|
| **Visibilidad — V1. Desglose de costo/uso** | ¿Desagrega costo y uso por cuenta/proyecto, servicio y período? | Exportación, documentación oficial, demo reproducible | 0: desglose verificado ausente; 1: consulta/manual básica; 2: vistas definidas y filtrables; 3: vistas integradas, actualizadas automáticamente y con doble evidencia. | No puntuar aquí la propiedad del gasto. |
| **Visibilidad — V2. Trazabilidad al dato fuente** | ¿Permite rastrear un total hasta registros o fuente de facturación? | Exportación auditables, documentación, verificación de equipo | 0: no trazable; 1: enlace/manual parcial; 2: detalle exportable y reproducible; 3: trazabilidad automatizada y conciliable con doble evidencia. | No sustituye asignación a responsable. |
| **Asignación — A1. Cobertura de asignación** | ¿Calcula gasto asignado/no asignado por responsable, centro o entidad? | Reporte de asignación, reglas configuradas, demo | 0: no calcula; 1: asignación manual/ad hoc; 2: reglas definidas con no asignado visible; 3: asignación integrada y automática con doble evidencia. | El detalle técnico de V1 no basta. |
| **Asignación — A2. Reglas de reparto compartido** | ¿Explicita y aplica reglas para costo compartido/multi-tenant? | Configuración, documentación, prueba con datos del escenario | 0: sin regla verificable; 1: reparto manual; 2: regla versionada y reproducible; 3: regla automatizada, trazable y verificada doblemente. | No medir métricas de uso como integración. |
| **Optimización — O1. Detección de oportunidades** | ¿Detecta desperdicio, rightsizing o compromiso relevante al escenario? | Recomendación generada, documentación, demo | 0: no detecta; 1: sugerencia manual/reactiva; 2: recomendaciones definidas con datos actuales; 3: priorización integrada/data-driven y doble evidencia. | No cuenta la ejecución automática. |
| **Optimización — O2. Explicación y seguimiento** | ¿Explica supuesto/impacto y permite seguir una recomendación? | Detalle de recomendación, exportación, evidencia de seguimiento | 0: sin explicación; 1: texto o cálculo manual; 2: impacto y estado trazables; 3: ciclo integrado de medición/realización con doble evidencia. | Ahorro estimado no prueba adopción. |
| **Automatización — AU1. Ejecución/control** | ¿Ejecuta o bloquea acciones/políticas de costo con control verificable? | Política, historial, API/IaC, demo | 0: no ejecuta/controla; 1: acción manual asistida; 2: flujo automatizado definido con aprobación/control; 3: operación automática integrada, con registro y doble evidencia. | No confundir una alerta con acción. |
| **Automatización — AU2. Salvaguardas** | ¿Ofrece aprobación, reversión, registro o límites antes de actuar? | Auditoría, configuración, prueba reproducible | 0: salvaguarda ausente; 1: control manual informal; 2: aprobación/registro definido; 3: salvaguardas automáticas auditables y doble evidencia. | No volver a puntuar la recomendación O1. |
| **Multicloud — M1. Consolidación normalizada** | ¿Consolida al menos dos proveedores bajo el mismo esquema declarado? | Conectores, salida consolidada, FOCUS si aplica, demo | 0: no consolida; 1: agregación manual; 2: consolidación definida con normalización declarada; 3: integrada/automática y doblemente verificada. | No evalúa precio comparable. |
| **Multicloud — M2. Manejo de diferencias** | ¿Hace visibles proveedor, cobertura y diferencias semánticas? | Diccionario, mapeo, reporte, documentación | 0: las oculta o no informa; 1: nota manual; 2: mapeo y límites explícitos; 3: validación automatizada/data-driven con doble evidencia. | No atribuir capacidades de lock-in. |
| **Integración — I1. Ingesta/intercambio** | ¿Integra datos requeridos (facturación, uso, clúster o IaC) del escenario? | API/conector documentado, prueba de ingestión | 0: no integra; 1: importación manual; 2: conector/API definido y reproducible; 3: integración automatizada, monitorizada y doble evidencia. | No mide la calidad del desglose V1. |
| **Integración — I2. Flujo operativo** | ¿Se integra con el flujo de trabajo relevante (alerta, ticket, CI/CD o reporte)? | Configuración, historial, demo reproducible | 0: sin flujo; 1: exportación/manual; 2: integración definida con evidencia de uso; 3: flujo integrado y automatizado con doble evidencia. | No puntuar aceptación de usuarios. |
| **Adopción — AD1. Accesibilidad por rol** | ¿Soporta acceso/entrega para los roles del escenario? | Roles documentados, prueba, guía oficial | 0: rol requerido no puede acceder; 1: acceso central/manual; 2: roles y vistas definidos; 3: acceso integrado con uso verificable y doble evidencia. | No mide gobernanza de costos en sí. |
| **Adopción — AD2. Habilitación y gobernanza** | ¿Ofrece guías, ownership o mecanismos de seguimiento para uso sostenido? | Guía oficial, registro de equipo, evidencia de uso | 0: ausente; 1: documentación aislada; 2: proceso/guía definido; 3: adopción medida e integrada con doble evidencia. | No contar funcionalidades de optimización. |
| **Precio — P1. Transparencia de supuestos** | ¿Expone precio, moneda, región, unidad, período y supuestos relevantes? | Calculadora/reporte/exportación, documentación oficial | 0: no expone; 1: dato manual/parcial; 2: supuestos visibles y reproducibles; 3: actualización integrada/data-driven y doble evidencia. | No mide comparación multicloud. |
| **Precio — P2. Comparación/estimación contextual** | ¿Permite estimar o comparar componentes sin ocultar límites de equivalencia? | Salida de escenario, documentación, demo | 0: no permite; 1: cálculo manual básico; 2: cálculo definido con límites explícitos; 3: cálculo integrado y validado doblemente. | No tratar precio como ahorro realizado. |
| **Dependencia — D1. Portabilidad de datos** | ¿Exporta datos/resultados en formato utilizable y documentado? | Exportación, API, estándar, prueba | 0: exportación ausente/bloqueada; 1: exportación manual limitada; 2: exportación/API definida y reproducible; 3: interoperable y automatizada con doble evidencia. | No puntuar conectores de I1 dos veces. |
| **Dependencia — D2. Acoplamiento y reversibilidad** | ¿Documenta dependencias propietarias y un camino de salida/configuración reversible? | Documentación contractual/técnica, prueba, estándar | 0: acoplamiento sin salida verificable; 1: salida manual no probada; 2: límites y salida documentados; 3: salida verificada/reproducible con doble evidencia. | No inferir dependencia desde ser cloud nativo. |

## 3. Pesos y fórmulas

| Criterio | Línea base exacta | Perfil de sensibilidad humano |
|---|---:|---:|
| Visibilidad | 100/9 % | 15 % |
| Asignación | 100/9 % | 15 % |
| Optimización | 100/9 % | 15 % |
| Precio | 100/9 % | 12 % |
| Automatización | 100/9 % | 10 % |
| Integración | 100/9 % | 10 % |
| Multicloud | 100/9 % | 8 % |
| Adopción | 100/9 % | 8 % |
| Dependencia | 100/9 % | 7 % |
| **Total** | **100 %** | **100 %** |

La línea base conserva `100/9` sin redondear. El perfil de sensibilidad es **normativo y seleccionado por humanos; no proviene de un artículo**.

Para un criterio `c`, `I_c` contiene solo sus indicadores aplicables y `C_c = Σx_ci / |I_c|`. Un indicador `NA` se excluye de `I_c`; si todos son `NA`, el criterio completo se excluye del conjunto aplicable `A`. Si queda algún indicador aplicable en `NE`, el criterio no está evidenciado y su peso completo reduce la cobertura. Para criterios aplicables `A`: `W'_c = 100W_c / Σ(W_j, j∈A)`. Cobertura: `100Σ(W_c de criterios aplicables evidenciados)/Σ(W_c de criterios aplicables)`. Si cobertura <70 %, resultado: **Insufficient evidence**. Para calcular tras `NE`, `W''_c = 100W'_c / Σ(W'_j de criterios aplicables evidenciados)`; puntaje normalizado: `S = Σ(W''_cC_c/3)`.

`NA` requiere justificación previa y se renormaliza; `NE` no equivale a 0 y reduce cobertura. Las bandas usan los puntos medios exactos de 0–3 normalizado: `[0, 50/3)` Insufficient; `[50/3, 50)` Basic; `[50, 250/3)` Solid; `[250/3, 100]` Advanced (`50/3 ≈ 16,6667`; `250/3 ≈ 83,3333`). Calcular sin redondeo y presentar a dos decimales.

## 4. Conjuntos críticos por escenario

| Escenario | Criterios críticos confirmados (mínimo `C_c ≥ 1`) |
|---|---|
| E1 | Visibilidad, Asignación |
| E2 | Multicloud, Precio |
| E3 | Optimización, Automatización |
| E4 | Precio, Integración |
| E5 | Asignación, Visibilidad |
| E6 | Visibilidad, Integración |

Los conjuntos críticos están confirmados por consenso del equipo; no son umbrales derivados de los artículos.

**Estado final:** **Criterios, pesos, escala y conjuntos críticos confirmados por consenso del equipo; documento estructurado con asistencia de IA.**
