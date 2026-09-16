# FP-177 — Metodología comparativa

> **Estado:** Método confirmado por consenso del equipo; documento estructurado con asistencia de IA.
>
> Este documento traduce decisiones humanas confirmadas para FP-177. No puntúa productos ni autoriza una recomendación.

## 1. Objeto y alcance

Se aplicará **una matriz común de nueve criterios** a cada escenario elegible de `escenarios-uso-y-poblacion-evaluada-borrador.md`: visibilidad, asignación, optimización, automatización, multicloud, integración, adopción, precio y dependencia. La unidad de resultado es **producto × escenario**; no se publicará un ranking universal entre categorías incompatibles.

Cada producto de un escenario se probará con: mismas entradas del escenario, misma fecha de corte de evidencia, mismas reglas de moneda, región y unidades cuando correspondan, y las mismas reglas de datos faltantes. Se debe registrar versión del producto, configuración, fuente y fecha de cada evidencia antes de puntuar.

La matriz operacional está en `matriz-criterios-y-ponderaciones-borrador.md`.

## 2. Evidencia y reglas de puntuación

### 2.1 Jerarquía de evidencia

Se prefieren documentación oficial, estándares y artículos académicos. El material comercial se identifica como tal y puede documentar una afirmación, pero si un indicador cuenta **solo** con evidencia comercial, su puntaje máximo es **1**. La ausencia de evidencia no demuestra ausencia de capacidad: se registra `NE`.

Un puntaje **3** exige doble evidencia: documentación primaria **más** un estudio independiente, demostración reproducible o verificación práctica del equipo. La matriz define evidencia admisible por indicador; el evaluador debe conservar enlaces, versiones, fecha de acceso y resultado reproducible.

### 2.2 Escala 0–3 y estados especiales

| Valor/estado | Significado operativo |
|---|---|
| `0` | Ausencia o incumplimiento **verificado** frente al ancla del indicador. Es una adaptación del proyecto FP-177. |
| `1` | Práctica básica, manual, reactiva o ad hoc. |
| `2` | Práctica definida, proactiva y sostenida. |
| `3` | Práctica integrada, basada en datos y automatizada; requiere doble evidencia. |
| `NE` | No evidenciado: no se conoce el valor; queda fuera del cálculo y de la cobertura. |
| `NA` | No aplicable: solo se admite si se justifica antes de puntuar el producto; queda fuera del cálculo y activa renormalización. |

Los significados 1–3 adaptan Crawl/Walk/Run de Manurung y Aji: *Crawl* manual/reactivo (1), *Walk* definido/proactivo (2) y *Run* integrado, automatizado y basado en datos (3) (`01_Manurung_Aji_2025_FinOps_Implementation.pdf`, sección **Methodology**, p. 712). El valor 0 no procede de esa escala: es una adaptación explícita de FP-177 para distinguir ausencia/incumplimiento verificado de falta de evidencia.

## 3. Cálculo

Sea `I_c` el conjunto de indicadores aplicables del criterio `c`; `x_ci` su valor 0–3; `W_c` el peso del criterio; y `A` el conjunto de criterios aplicables. Un indicador `NA` se excluye de `I_c` antes de calcular la media. Si todos los indicadores de un criterio son `NA`, el criterio completo pasa a `NA` y se excluye de `A`. Si queda al menos un indicador aplicable, la media se calcula sobre esos indicadores; pero cualquier indicador aplicable en `NE` impide considerar evidenciado el criterio completo y reduce la cobertura por el peso total de ese criterio.

**Media aritmética por criterio** (solo si todos los indicadores aplicables de ese criterio tienen valor):

`C_c = (Σ x_ci) / |I_c|`

La media aritmética es una decisión humana por transparencia. Tiene apoyo metodológico limitado en que Manurung y Aji calculan la media aritmética de dominios FinOps para obtener una puntuación de madurez; ese trabajo no valida estos nueve criterios ni pesos (`01_Manurung_Aji_2025_FinOps_Implementation.pdf`, sección **Methodology**, p. 712).

**Cobertura de evidencia:**

`Cobertura = 100 × (Σ W_c para c aplicable y evidenciado) / (Σ W_c para c aplicable)`

Un criterio es “evidenciado” si sus indicadores aplicables están puntuados 0–3. Si la cobertura es menor de **70 %**, el resultado se marca **Insufficient evidence** y no recibe banda comparativa.

**Renormalización por `NA`:**

`W'_c = 100 × W_c / (Σ W_j para j en A)`

`NE` no se convierte en cero ni en `NA`: se excluye del puntaje, pero reduce la cobertura. Si se permite calcular porque la cobertura llega al 70 %, los pesos se renormalizan sobre los criterios aplicables y evidenciados para no atribuir valor a lo desconocido:

`W''_c = 100 × W'_c / (Σ W'_j para j aplicable y evidenciado)`

**Puntaje normalizado (0–100):**

`S = Σ (W''_c × C_c / 3)`

Se calcula por separado con `W` de línea base y con `W` de sensibilidad. La línea base usa nueve pesos exactamente iguales: `100/9 %` por criterio (11,111… %); se conserva la fracción `100/9` o precisión completa durante el cálculo y se redondea solo al presentar el resultado.

## 4. Perfiles de ponderación

| Criterio | Línea base | Sensibilidad |
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

Los pesos de sensibilidad son un **perfil normativo seleccionado por humanos**, no derivado de un artículo. Estudios de decisiones multicriterio pueden usar pesos contextuales, pero no transfieren pesos a FP-177; por ello no se usan como respaldo para estos valores.

La sensibilidad se considera material si cambia el nivel descriptivo o el orden entre herramientas **comparables dentro del mismo escenario y categoría**.

## 5. Bandas, redondeo y umbrales críticos

El puntaje se conserva con precisión completa durante cálculos y se muestra a dos decimales. Las bandas se asignan con el valor sin redondear usando los puntos medios exactos de la escala 0–3 normalizada: `[0, 50/3)` **Insufficient**; `[50/3, 50)` **Basic**; `[50, 250/3)` **Solid**; `[250/3, 100]` **Advanced**. Como referencia visual, `50/3 ≈ 16,6667` y `250/3 ≈ 83,3333`. En comunicación abreviada pueden mostrarse como 0–16, 17–49, 50–82 y 83–100, pero prevalecen los intervalos exactos. La condición de cobertura menor a 70 % prevalece sobre cualquier banda.

Además, cada escenario tendrá criterios críticos con `C_c >= 1`. El conjunto confirmado es: E1 visibilidad/asignación; E2 multicloud/precio; E3 optimización/automatización; E4 precio/integración; E5 asignación/visibilidad; E6 visibilidad/integración. Un incumplimiento crítico se informa junto al puntaje y no se oculta con la media.

## 6. Ejemplo sintético (ficticio; no corresponde a un proveedor)

Para el producto ficticio **Herramienta Aurora** en E1, supóngase que todos los criterios son aplicables y evidenciados, y que las medias de criterio son: visibilidad 3; asignación 2; optimización 1; automatización 1; multicloud 0; integración 2; adopción 2; precio 1; dependencia 2.

Con base igualitaria: `S = (100/9) × (3+2+1+1+0+2+2+1+2)/3 = 51,851…`, presentado como **51,85 (Solid)**. Con el perfil de sensibilidad: `S = (15×3 + 15×2 + 15×1 + 10×1 + 8×0 + 10×2 + 8×2 + 12×1 + 7×2)/3 = 54,00 (Solid)`. El ejemplo muestra el cálculo, no capacidad real ni recomendación.

**Estado final:** **Método confirmado por consenso del equipo; documento estructurado con asistencia de IA.**
