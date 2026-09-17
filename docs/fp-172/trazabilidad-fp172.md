# FP-172 — Trazabilidad de palancas y costos subestimados

## Alcance

Este registro acompaña la hoja `Palancas` del workbook maestro local de TINV-04. La hoja contiene 13 palancas, cada una con mecanismo, supuesto, ejemplo de cálculo, riesgo, fuente y fecha de consulta.

## Evidencia utilizada

| Palancas | Papers académicos FP-48 | Fuentes técnicas/oficiales | Uso en FP-172 |
|---|---|---|---|
| Rightsizing, apagado, capacidad spot | `05_Optimization of Resource Provisioning Cost in Cloud Computing.md`, `012-Optimizing cloud solutioning design.md`, `03_Cho_2026_FinOps_Budget_Optimization.md` | FinOps Optimize; Azure VM management; Azure Spot; Google Spot | Mecanismo, condición y riesgo |
| Compromisos y reservas | `01_Manurung_Aji_2025_FinOps_Implementation.md`, `03_Cho_2026_FinOps_Budget_Optimization.md`, `05_Optimization of Resource Provisioning Cost in Cloud Computing.md` | AWS Savings Plans; Google CUD; FinOps Rate Optimization | Comparación de tarifa bajo demanda frente a compromiso |
| Storage tiers y arquitectura | `05_Optimization of Resource Provisioning Cost in Cloud Computing.md`, `011-Cloud computing and its impact on economic and environmental performance.md`, `010-A comprehensive framework for cloud computing migration using.md`, `012-Optimizing cloud solutioning design.md` | Azure Blob access tiers; Azure serverless architecture | Condiciones de tiering y cambio arquitectónico |
| Egress y tráfico interzona | Paper ATLAS y `012-Optimizing cloud solutioning design.md` | Azure Bandwidth Pricing y documentación de redes | Costos por volumen, destino y ruta |
| Licenciamiento, soporte y no productivo | `01_Manurung_Aji_2025_FinOps_Implementation.md`, `03_Cho_2026_FinOps_Budget_Optimization.md`, `05_Optimization of Resource Provisioning Cost in Cloud Computing.md` | Azure licensing, support plans y VM auto-shutdown | Condición contractual y ventanas operativas |
| Backup y observabilidad | `01_Manurung_Aji_2025_FinOps_Implementation.md` | PostgreSQL backup pricing y Azure Monitor Logs | Retención, RPO/RTO y volumen de telemetría |

Los papers anteriores están registrados en la matriz FP-48. Las fuentes oficiales se consignan en la columna `Fuente oficial` de cada fila de `Palancas` y deben conservar su fecha de consulta al trasladarse a la matriz.

## Convención de cifras

Los ejemplos monetarios incluidos en la hoja son **ilustrativos** para mostrar el método de cálculo. No son cotizaciones ni tarifas vigentes. Antes de usar una cifra en FP-52, se debe sustituir el supuesto por una tarifa oficial reproducible, indicando proveedor, región, unidad, moneda, modalidad y fecha.

## Trazabilidad de IA y revisión humana

- Herramienta: Gentle AI/OpenCode.
- Finalidad: estructurar la tabla, redactar mecanismos y riesgos, y comprobar aritmética de ejemplos.
- Revisión humana pendiente: validar cada fuente en su original, reemplazar tarifas ilustrativas, confirmar supuestos y aprobar las decisiones antes de consolidar el Formulario A-6.
- La IA no sustituye la autoría, defensa oral ni validación del equipo.

## Criterio para pasar a revisión

- [x] 13 palancas documentadas.
- [x] Cada fila tiene mecanismo, supuesto, beneficio, riesgo, fuente y fecha.
- [x] Los cálculos visibles son aritméticamente reproducibles.
- [ ] Validar tarifas reales y configuración regional.
- [x] Incorporar/actualizar las 15 fuentes oficiales en la matriz FP-48.
- [ ] Registrar el aporte individual de cada integrante en el comentario de Jira FP-172.
