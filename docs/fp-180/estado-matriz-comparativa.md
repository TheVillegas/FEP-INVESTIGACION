# FP-180 — Estado de la matriz comparativa y cálculo de resultados

> **Estado:** Motor de cálculo terminado y validado contra el ejemplo sintético de FP-177. Las 17
> herramientas de la población de FP-51/FP-179 están investigadas con evidencia real, citada e
> individual, en sus escenarios elegibles. Documento estructurado con asistencia de IA; queda a
> validación humana del equipo antes de dar por cumplidos los criterios de término de FP-180.
>
> **Revisión 2026-09-16:** una auditoría posterior detectó dos defectos de fondo. El primero
> —uso de `NA` donde correspondía `0` o `NE`, que convertía datos faltantes en ventaja— está
> corregido; ver §7 y `correcciones-aplicadas.md`. El segundo —la puntuación no varía entre
> escenarios, de modo que la unidad producto × escenario de FP-177 aún no está implementada—
> sigue abierto; ver §8.

## 1. Qué se construyó

El archivo `FP-180_matriz_comparativa.xlsx` implementa, como fórmulas de Excel reproducibles, la
metodología aprobada en `docs/fp-177/metodologia-comparativa-borrador.md` y la matriz de indicadores
de `docs/fp-177/matriz-criterios-y-ponderaciones-borrador.md`:

- Hoja **Pesos**: pesos de línea base (100/9 % cada criterio) y de sensibilidad, editables.
- Hoja **Puntuacion**: una fila por Escenario × Producto × Indicador (18 indicadores: V1,V2,A1,A2,
  O1,O2,AU1,AU2,M1,M2,I1,I2,AD1,AD2,P1,P2,D1,D2), con valor (0-3/NE/NA), tipo de evidencia, evidencia,
  fuente, fecha de verificación y notas.
- Hoja **Calculo**: una fila por Escenario × Producto (61 pares, incluida la fila de validación). Calcula,
  con fórmulas que leen directamente de Puntuacion y Pesos: aplicabilidad y evidenciación por criterio,
  `C_c` (media por criterio), cobertura de evidencia, `S` normalizado (0-100) en línea base y en
  sensibilidad, banda (Insufficient/Basic/Solid/Advanced) e incumplimientos de criterios críticos por
  escenario.
- Hoja **Resultados**: espejo legible de los valores calculados (cobertura, `S` en ambos perfiles,
  banda y criterios críticos incumplidos) por cada par Escenario × Producto. Existe porque el libro
  se genera con openpyxl, que no escribe valores en caché: sin este espejo, quien abra el archivo
  sin Excel ni LibreOffice no ve ningún número. La hoja **Calculo** conserva las fórmulas.
- Hoja **Graficos**: un gráfico de barras por escenario (S línea base y S sensibilidad por producto),
  vinculado a la hoja Resultados — se actualiza al reejecutar `apply_scope_corrections.py`.

**Validación del motor de cálculo:** se cargó el ejemplo sintético «Herramienta Aurora» de la sección 6
de `metodologia-comparativa-borrador.md` como fila de control (Escenario = `VALIDACION`, no es un
producto real). El motor reproduce exactamente los valores del documento: **S línea base = 51,85** y
**S sensibilidad = 54,00** (verificado tras recalcular el libro con LibreOffice headless).

## 2. Las 17 herramientas de la población quedaron investigadas

Se investigó, contra documentación oficial publicada y con citas directas, cada una de las 17
herramientas de la población de FP-51/FP-179, en sus escenarios elegibles:

| Categoría | Herramientas | Escenarios elegibles |
|---|---|---|
| Cloud nativa | AWS Cost Explorer, AWS Cost Optimization Hub, Azure Cost Management, Google Cloud Billing, Google Cloud FinOps Hub | E1,E2,E3,E5,E6 |
| Multicloud | Cloudability, CloudHealth, CloudZero, Vantage, Finout, nOps | E1,E2,E5,E6 (CloudZero también E3) |
| Kubernetes | OpenCost, Kubecost, Cast AI, StormForge | E3,E5 |
| Estimación temprana | Infracost, Cloud Custodian | E4 |

Ningún indicador recibe el valor 3 en ninguna herramienta (ver límite metodológico, sección 3). La
profundidad de evidencia por producto no es uniforme: algunas plataformas (nOps, CloudZero, Finout,
Cast AI, Infracost) tienen documentación técnica oficial extensa y bien indexada, mientras que otras
(Cloudability, Vantage, StormForge) tienen documentación más fragmentada o parcialmente inaccesible,
lo que se refleja honestamente en más indicadores `NE` ("pendiente de investigar", no cero) y, por lo
tanto, en menor cobertura — ver sección 4.

Hallazgos transversales relevantes para FP-181:

- **AWS, Azure y GCP dividen la función igual**: un producto amplio de visibilidad/asignación/
  automatización/precio/dependencia (Cost Explorer / Cost Management / Billing) y un producto angosto
  de recomendaciones de optimización (Cost Optimization Hub / FinOps hub). Ningún nativo consolida
  multicloud (M1=M2=0 en los tres).
- **CloudZero, Finout y nOps documentan un esquema de normalización declarado** para consolidar
  multicloud (AnyCost/Common Bill Format, FOCUS, FOCUS Export respectivamente), lo que les da M1=M2=2;
  CloudHealth y Vantage consolidan varios proveedores pero sin ese mapeo explícito documentado (M2 más
  débil o NE); Cloudability no tiene evidencia oficial suficiente para calificar más allá de 1.
  Cast AI, OpenCost y Kubecost -categorizados como "Kubernetes"- no consolidan facturación multicloud
  (M1=M2=0): operan clúster por clúster, aunque valoran los recursos con las APIs de precio de varios
  proveedores.
- **Automatización real de ejecución** (AU1≥2, no solo recomendaciones) se documentó en: AWS Budgets,
  Azure budgets/Action Groups, GCP Budgets programáticos, CloudHealth Policies, Vantage Autopilot
  (parcial, solo AWS), nOps Commitment Management (AWS+GCP+Azure, con implementaciones separadas por
  proveedor), Cast AI (autoscaling/Spot/bin packing) y StormForge (auto-aplicación de recomendaciones).
  OpenCost y CloudZero Optimize son explícitamente "solo recomendación" (AU1=0), documentado por el
  propio proveedor.
- **Límite de alcance de StormForge**: es una herramienta de rightsizing de workloads de Kubernetes,
  no de visibilidad/asignación de costo; sus indicadores de Visibilidad, Asignación, Multicloud y
  Precio se marcaron `NA` con justificación de alcance.
- **Límite de alcance de Infracost**: estima costo antes del despliegue a partir de IaC (Terraform/
  CloudFormation/CDK); no es una herramienta de asignación organizacional ni de trazabilidad a
  facturación real, por lo que V2/A1/A2 se marcaron `NA`. Es, en cambio, la herramienta con mejor
  evidencia de Precio (P1=P2=2) de toda la población.
- **Tensión de clasificación a revisar por el equipo — Cloud Custodian**: está en la población como
  herramienta de "estimación temprana" (E4), pero la documentación oficial revisada lo describe como
  un motor de políticas/remediación sobre recursos **ya desplegados** (con `--dryrun`, acciones
  automáticas de detener/eliminar/etiquetar, y notificación previa), no como una herramienta que
  estime costo antes del despliegue. Sus indicadores de Precio se marcaron `NA` con esa nota explícita;
  se sugiere al equipo revisar si corresponde reclasificarlo (queda documentado en la hoja
  Instrucciones para no perder la trazabilidad de la decisión).
- **Limitación de acceso — Cloudability**: la documentación técnica oficial de IBM Docs
  (`ibm.com/docs/en/cloudability-...`) devolvió error 403 en todos los intentos de acceso durante esta
  investigación (2026-09-16). Toda la evidencia disponible es de páginas comerciales de apptio.com, por
  lo que, aplicando la propia metodología ("evidencia comercial exclusiva limita el indicador a 1"),
  ningún indicador de Cloudability supera el valor 1. Se sugiere al equipo reintentar el acceso a IBM
  Docs (posiblemente bloqueado por red/región) y actualizar esas filas si logra consultarla.

## 3. Límite metodológico de esta investigación

La verificación se hizo **contra documentación oficial publicada**, sin acceso práctico a una cuenta
real de AWS/Azure/GCP ni a las consolas de los productos comerciales. Por eso **ningún indicador
recibe el valor 3**: la metodología exige doble evidencia (documentación primaria + estudio
independiente, demostración reproducible o verificación práctica del equipo) para ese valor, y aquí
solo se dispone de la primera. Quedan marcados como candidatos fuertes a subir a 3 si el equipo aporta
esa segunda evidencia (ver columna «Notas» en Puntuacion): AWS V2 (reconciliación CUR-factura), GCP
FinOps hub AD2 (FinOps score), Vantage Autopilot AU1/AU2, nOps Commitment Management AU1/AU2, entre
otros con evidencia oficial particularmente completa.

## 4. Cruce con los papers académicos de FP-48 (revisión explícita a pedido del equipo)

Se revisaron los 13 PDF de `FP-48 TINV02/Papers academicos - FP-48/`. Solo un paper nombra
herramientas de la población de FP-51 — **Manurung y Aji (2025)**, que registra a 6 organizaciones
reales usando explícitamente AWS Cost Explorer, Cast.ai e Infracost ("We use AWS Cost Explorer,
cast.ai, and infracost.", P2), y encuentra que el 100% (6/6) carece de showback/chargeback pese a ello
("[Gap] Cost ownership is centralized, no showback/chargeback", Tabla 4).

Según la propia metodología de FP-177 ("se excluye inferir resultados de herramientas desde evidencia
académica que estudia prácticas... no el producto evaluado"), esa evidencia describe **uso real y
brechas organizacionales**, no verifica ni refuta una capacidad del producto. Por eso se registró como
**nota de contexto** (columna Notas) en las filas AD2 de AWS Cost Explorer, Cast AI e Infracost — las
tres herramientas que el paper nombra — y **no se usó para subir ni bajar ningún puntaje numérico**.
Queda como insumo explícito para el análisis de sensibilidad/limitaciones de FP-181. Los demás 12
papers ya están reflejados en `docs/fp-177/` (metodología, criterios y escenarios) y no nombran
productos comerciales adicionales de la población.

## 5. Cobertura obtenida y filas que siguen en NE

La investigación priorizó profundidad y cita verificable por sobre completar artificialmente el 100%
de las 18 filas de cada producto. Como resultado, varios productos quedan con cobertura de evidencia
por debajo del 70% en uno o más escenarios y su resultado se marca automáticamente **"Insufficient
evidence"** (no es un error de fórmula: es el propio mecanismo de la metodología funcionando como está
diseñado). Antes de que el equipo cierre FP-180, conviene decidir si:

1. se completan las filas `NE` restantes con más investigación (documentación oficial adicional,
   verificación práctica en una cuenta de prueba, o una segunda fuente independiente para subir
   indicadores ya en 2 a 3), o
2. se acepta "Insufficient evidence" como resultado válido y documentado para esos pares
   Escenario-Producto en el informe final de FP-181.

Los candidatos con más filas `NE` son las plataformas multicloud con documentación más fragmentada
(Cloudability, Vantage, Finout parcialmente, CloudHealth) y las herramientas de Kubernetes distintas de
OpenCost (Kubecost, Cast AI, StormForge), que no siempre documentan de forma pública funciones como
roles/permisos o guías de gobernanza propias.

## 6. Cómo continuar

1. Abrir `FP-180_matriz_comparativa.xlsx` y editar directamente la hoja **Puntuacion**: cambiar
   `Valor`, `Tipo de evidencia`, `Evidencia`, `Fuente` y `Fecha de verificacion` de cada fila `NE`
   pendiente, o para subir un indicador de 2 a 3 con una segunda fuente independiente. La hoja Calculo
   se recalcula sola (fórmulas, no valores fijos).
2. No editar la hoja Calculo a mano: si una fórmula parece incorrecta, corregirla en el motor y
   avisar al equipo, para que el cambio se propague a todos los productos. Tras cualquier edición
   de Puntuacion, reejecutar `python apply_scope_corrections.py` para regenerar la hoja Resultados
   y los gráficos (el script es idempotente: no vuelve a tocar celdas ya corregidas).
3. Antes de cerrar FP-180, revisar la sección 5 (filas en NE y cobertura <70%), la tensión de
   clasificación de Cloud Custodian (sección 2) y el bloqueo de acceso a la documentación de
   Cloudability (sección 2), y decidir cómo tratarlos.
4. Verificar que ningún NA carezca de justificación explícita en la columna Notas (todas las filas NA
   de este libro la tienen) y que ninguna fila puntuada carezca de Fuente (verificado
   programáticamente: 0 filas puntuadas sin fuente en esta versión).
5. FP-181 (interpretación y recomendaciones) **no puede todavía redactar recomendaciones por
   escenario**: mientras la puntuación no varíe entre escenarios (§8), la matriz no distingue E1 de
   E3 para un mismo producto. Sí puede trabajar la lectura por producto y por categoría, teniendo en
   cuenta que 27 de 61 pares están en "Insufficient evidence" y que el hallazgo de Manurung y Aji
   (2025) sobre showback/chargeback (sección 4) es un insumo cualitativo, no un ajuste de puntaje.

## 7. Corrección aplicada: `NA` mal usado como ausencia verificada

La primera pasada de puntuación marcó `NA` en 55 celdas únicas cuya justificación registrada afirma
en realidad una **ausencia verificada** («no ofrece», «no calcula», «no expone», «no ejecuta») o una
**falta de investigación** («la documentación revisada no describe», «no se identificó»). En FP-177
los tres estados tienen efectos distintos: `0` penaliza, `NE` reduce la cobertura y `NA`
**renormaliza los pesos**, repartiendo el peso ausente entre los criterios restantes.

El efecto era el prohibido por el criterio de término de FP-180: el dato faltante se convertía en
ventaja. El caso testigo es AWS Cost Optimization Hub, que puntuaba **66,67 (Solid)** en E1 —con
Visibilidad y Asignación, los dos criterios críticos de E1, en `NA`— por encima de AWS Cost Explorer
(51,85), que sí cubre ambos.

`apply_scope_corrections.py` reclasifica esas celdas a partir del texto que cada una ya tenía
registrado, sin agregar investigación ni modificar evidencia ni fuentes. `NA` se conserva donde el
indicador no tiene objeto (por ejemplo AU2, «salvaguardas antes de actuar», cuando AU1 es 0).

Resultado: 163 filas corregidas, 19 de 61 pares cambian su puntaje. AWS Cost Optimization Hub pasa a
19,05 (Basic) e incumple los criterios críticos de cada escenario; Google Cloud FinOps Hub, de 50,00
a 23,81; Infracost, de 56,67 a 47,22; Cloud Custodian pasa de "Insufficient evidence" a 19,05 con
incumplimiento crítico en Precio, lo que refuerza la tensión de clasificación ya señalada en §2. El
detalle celda por celda está en `correcciones-aplicadas.md`. La fila de control «Herramienta Aurora»
sigue reproduciendo S=51,85 / S=54,00, de modo que el motor de cálculo no se vio afectado.

**Esta reclasificación es una propuesta metodológica y requiere validación del equipo**, porque
ajusta cómo se aplica la escala de FP-177, no solo un dato.

## 8. Defecto abierto: la puntuación no varía entre escenarios

Los 15 productos que aparecen en más de un escenario tienen **valores y textos de evidencia
idénticos en todos ellos** (verificado: cero diferencias de valor y cero diferencias de texto). Es
decir, las 61 filas de la hoja Calculo contienen 17 evaluaciones replicadas, no 61 evaluaciones
producto × escenario.

Eso contradice FP-177 §1, que fija la unidad de resultado en producto × escenario y exige probar
cada producto «con las mismas entradas del escenario». Con la matriz así, «recomendación por
escenario» —el entregable de FP-181 y del informe FP-54— no tiene de dónde salir.

Resolverlo exige re-evaluar, escenario por escenario, los indicadores sensibles al contexto: V1, V2,
A2, O1, AU1, M1, M2, I1, I2, P2 y AD1. Ejemplo concreto: I1 pregunta si la herramienta integra «los
datos requeridos del escenario»; para AWS Cost Explorer la evidencia citada respalda la ingesta de
datos de facturación (E1), pero no dice nada sobre métricas de clúster y `requests/limits`, que son
las entradas mínimas de E3. El valor 2 no es trasladable de E1 a E3 sin evidencia propia.

Es investigación documental adicional, no un ajuste de fórmulas. Antes de emprenderla conviene que el
equipo decida el tratamiento provisional de las celdas replicadas: marcarlas `NE` hasta investigarlas
—honesto, pero baja la cobertura y lleva a más pares a "Insufficient evidence"— o conservarlas con la
limitación declarada mientras se completa la investigación.
