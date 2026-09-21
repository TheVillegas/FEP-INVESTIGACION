# Sección final FP-49 para Overleaf

Este archivo es un contenedor de Markdown: copiá únicamente el bloque `latex` al informe en Overleaf. El contenido conceptual fue adaptado mecánicamente de los artefactos verificados FP-167, FP-168 y FP-170; no reemplaza la revisión de las fuentes originales. El análisis crítico, la aplicación al caso del proyecto, las conclusiones, las recomendaciones y el párrafo de aporte propio quedan reservados para autoría humana, conforme al punto 6.1 de las indicaciones.

```latex
% Requiere en el preámbulo: \usepackage{graphicx} para \resizebox.
\section{Marco conceptual de FinOps}
\label{sec:marco-conceptual-finops}

La práctica de FinOps conecta el consumo y los costos tecnológicos con decisiones orientadas al valor. En este marco conceptual se presentan el ciclo de fases, las personas que participan en las decisiones y la asignación de costos. El alcance es conceptual: no incluye datos aplicados, resultados medidos ni una política de asignación para una organización concreta.

% TODO (HUMANO): incorporar al cierre de la introducción el párrafo que distinga
% qué proviene de la ficha y qué constituye aporte propio del grupo.
% TODO (HUMANO): desarrollar la discusión crítica de la evidencia y cualquier
% análisis comparativo; estas partes deben ser de autoría humana.

\subsection{Fases de FinOps}
\label{subsec:fases-finops}

La FinOps Foundation organiza la práctica de FinOps en tres fases: \textbf{Informar, Optimizar y Operar}. Estas permiten comprender el consumo y los costos tecnológicos, identificar oportunidades de mejora e implementar cambios orientados al valor para la organización. Las fases forman un ciclo continuo: los resultados de las acciones ejecutadas generan información para revisar las decisiones y detectar nuevas oportunidades \cite{finops-phases}.
% \cite{finops-phases}: FP-167, referencia [1], FinOps Foundation, ``FinOps Phases''.

\begin{description}
  \item[Informar: comprender el consumo y los costos.] Su propósito es proporcionar visibilidad sobre el uso de los recursos tecnológicos y sus costos asociados. Para ello, se recopilan, organizan y analizan datos que permitan identificar qué recursos se consumen, cuánto cuestan y a qué equipos, productos o actividades corresponden \cite{finops-phases}. En un entorno cloud, esta información permite distribuir los costos entre responsables y relacionar el gasto con el funcionamiento de los servicios. También proporciona una base para elaborar presupuestos, realizar previsiones y analizar indicadores de costo unitario. El resultado es una visión compartida que permite a ingeniería, finanzas y la organización tomar decisiones fundamentadas. Como el consumo de la nube puede variar, la información sobre costos y uso debe revisarse periódicamente.

  \item[Optimizar: identificar y priorizar mejoras.] Esta fase utiliza la información disponible para identificar, evaluar y priorizar oportunidades de mejora. Estas pueden abordar el uso de los recursos, por ejemplo mediante el ajuste de capacidad infrautilizada, o las tarifas, mediante la evaluación de opciones de contratación adecuadas al consumo previsto \cite{finops-phases}. Su objetivo no consiste únicamente en reducir el gasto: las alternativas deben evaluarse considerando el valor que aportan y los compromisos entre costo, calidad y velocidad. Una reducción de capacidad no representa necesariamente una mejora si perjudica el servicio o los objetivos de la organización \cite{finops-principles}. La optimización del uso suele requerir colaboración con Engineering; la optimización de tarifas y compromisos contractuales, con Procurement y Leadership. El resultado es un conjunto de oportunidades priorizadas para su pronta ejecución o para escenarios futuros.
  % \cite{finops-principles}: FP-167, referencia [2], FinOps Foundation, ``FinOps Principles''.

  \item[Operar: ejecutar y sostener las mejoras.] Esta fase transforma las oportunidades seleccionadas en acciones concretas. Los equipos involucrados implementan los cambios, coordinan responsabilidades y establecen mecanismos para dar seguimiento a sus resultados. Estas acciones pueden modificar el consumo o las condiciones económicas de los recursos, además de mejorar los procesos y las capacidades de la práctica FinOps \cite{finops-phases}. Una vez ejecutados los cambios, sus efectos se evalúan al regresar a la fase Informar. Esta retroalimentación permite comprobar los resultados, actualizar la información y orientar nuevas decisiones. Así, FinOps funciona como una práctica de mejora continua, en la que distintos equipos pueden trabajar simultáneamente en diferentes fases y a ritmos distintos.
\end{description}

% FIGURA PLACEHOLDER: ciclo iterativo Informar--Optimizar--Operar.
% TODO (HUMANO): decidir si se incorporará una figura, crearla o verificar sus
% derechos de uso, numerarla y explicar su aporte en el texto.

\subsection{Roles y participación: personas de FinOps}
\label{subsec:personas-finops}

Las \emph{Core Personas} son los grupos principales que participan directamente en las decisiones FinOps y en la responsabilidad compartida sobre el valor del uso tecnológico \cite{finops-personas}. Se consideran exactamente seis personas oficiales: \textbf{Engineering (Ingeniería), Finance (Finanzas), Procurement (Adquisiciones), Product (Producto), FinOps Practitioner (Profesional de FinOps) y Leadership (Liderazgo)}. ``Negocio'' describe contexto, resultados u objetivos; no constituye una séptima \emph{Core Persona}.
% \cite{finops-personas}: FP-168, referencia [1], FinOps Foundation, ``FinOps Personas''.

\begin{itemize}
  \item \textbf{Engineering (Ingeniería).} Influye directamente en el consumo mediante la arquitectura, el dimensionamiento y la operación. Decide patrones técnicos, horarios, capacidad, eliminación de recursos ociosos y respuesta a anomalías, equilibrando costo, velocidad, calidad, seguridad y confiabilidad \cite{finops-engineering}.
  % \cite{finops-engineering}: FP-168, referencia [2], FinOps Foundation, ``Engineering''.

  \item \textbf{Finance (Finanzas).} Aporta el contexto financiero para presupuestar, prever, clasificar y reportar el gasto tecnológico. Analiza variaciones, asignación e implicaciones contables y participa en compromisos financieros, sin aprobar por defecto toda decisión técnica \cite{finops-finance}.
  % \cite{finops-finance}: FP-168, referencia [3], FinOps Foundation, ``Finance''.

  \item \textbf{Procurement (Adquisiciones).} Ejerce responsabilidad financiera y de gobierno comercial sobre proveedores, licencias y contratos. Decide estrategias de abastecimiento, negociación, renovación, compromisos y condiciones, para lo cual necesita previsiones antes de los hitos contractuales \cite{finops-procurement}.
  % \cite{finops-procurement}: FP-168, referencia [4], FinOps Foundation, ``Procurement''.

  \item \textbf{Product (Producto).} Conecta estrategia, demanda y hoja de ruta con el consumo tecnológico. Decide alcance, prioridad y secuencia de iniciativas considerando valor, margen, experiencia y tiempo de salida \cite{finops-product}.
  % \cite{finops-product}: FP-168, referencia [5], FinOps Foundation, ``Product''.

  \item \textbf{FinOps Practitioner (Profesional de FinOps).} Coordina datos y conversaciones entre áreas, pero no reemplaza sus decisiones. Normaliza y asigna costos, prepara análisis, facilita indicadores y mantiene una cadencia adecuada para cada categoría tecnológica \cite{finops-practitioner}.
  % \cite{finops-practitioner}: FP-168, referencia [6], FinOps Foundation, ``FinOps Practitioner''.

  \item \textbf{Leadership (Liderazgo).} Establece objetivos, límites de decisión, recursos y mecanismos de rendición de cuentas. Prioriza inversiones y resuelve escalaciones cuando costo, riesgo o impacto exceden la autoridad operativa \cite{finops-leadership}.
  % \cite{finops-leadership}: FP-168, referencia [7], FinOps Foundation, ``Leadership''.
\end{itemize}

\begin{table}[htbp]
  \centering
  \caption{Resumen de las Core Personas de FinOps.}
  \label{tab:core-personas-finops}
  \scriptsize
  % TABLA PLACEHOLDER DE MAQUETACIÓN: verificar legibilidad y orientación en el informe final.
  \resizebox{\textwidth}{!}{%
  \begin{tabular}{|p{2.8cm}|p{3.3cm}|p{3.3cm}|p{3.3cm}|p{3.3cm}|p{3.6cm}|p{3.3cm}|}
    \hline
    \textbf{Aspecto} & \textbf{Engineering} & \textbf{Finance} & \textbf{Procurement} & \textbf{Product} & \textbf{FinOps Practitioner} & \textbf{Leadership} \\ \hline
    Tipo de responsabilidad & Operativa & Financiera & Financiera y gobierno comercial & Operativa y valor & Coordinación transversal & Gobierno estratégico \\ \hline
    Beneficios & Costo visible desde diseño y operación & Mejor asignación, forecast y reporte & Mejor negociación y uso contractual & Costo conectado con margen y hoja de ruta & Datos comparables y responsabilidad distribuida & Alineación, previsibilidad y control de riesgo \\ \hline
    Objetivos & Soluciones eficaces, costo-eficientes y asignables & Presupuestar, prever, clasificar y reportar & Contratar con valor y gestionar proveedores & Crecer, proteger margen y reducir tiempo de salida & Dar transparencia y facilitar decisiones & Alinear inversión con estrategia y límites \\ \hline
    Métricas clave (candidatas) & Utilización; costo por servicio; gasto asignado & Precisión del forecast; variación presupuestaria; costo unitario & Uso de compromisos; cumplimiento contractual; costo por licencia & Margen; costo por funcionalidad; tiempo de salida & Precisión del forecast; cobertura de asignación; consistencia de reportes & Eficiencia de inversión; impacto en ingresos/COGS; cumplimiento presupuestario \\ \hline
    Tres roles habituales & Software Engineer; Solutions Architect; DevOps Engineer & Financial Analyst; Budget Analyst; IT Financial Management Manager & Sourcing Specialist; Contract Manager; Vendor Manager & Product Analyst; Product Manager; Product Owner & FinOps Practitioner; FinOps Analyst; FinOps Team Lead & CEO; CFO; CTO \\ \hline
    Decisiones principales & Arquitectura, capacidad, horarios y anomalías & Presupuesto, forecast, asignación y reporte & Negociación, renovación y compromisos & Alcance, prioridad y secuencia & Normalización, indicadores y cadencia & Estrategia, políticas, recursos y escalamiento \\ \hline
  \end{tabular}%
  }
\end{table}

Las \emph{Allied Personas} son disciplinas tradicionales o emergentes cuya actividad se cruza con FinOps y que coordinan con sus profesionales cuando sus datos, controles o decisiones resultan pertinentes \cite{finops-personas}. Entre ellas se encuentran ITAM, ITFM, Sostenibilidad, ITSM/ITIL y Seguridad. Como categorías del framework, no implican asignaciones concretas para el equipo del curso.

% TODO (HUMANO): asignar personas y responsabilidades concretas al caso del
% proyecto, si corresponde. Los artefactos fuente no contienen esa aplicación.

\subsection{Asignación de costos}
\label{subsec:asignacion-costos}

La asignación de costos relaciona el gasto cloud con los destinos que lo consumen o se benefician de él. Dentro del framework de FinOps, pertenece al dominio \emph{Understand Usage \& Cost}, que reúne cuatro capacidades vigentes: \emph{Data Ingestion}, \emph{Allocation}, \emph{Reporting \& Analytics} y \emph{Anomaly Management} \cite{finops-understand-usage-cost}. Estas capacidades intercambian datos, metadatos, análisis y retroalimentación; su orden de exposición no representa un proceso lineal obligatorio.
% \cite{finops-understand-usage-cost}: FP-170, referencia [1], FinOps Foundation, ``Understand Usage & Cost''.

La \textbf{asignación de costos} atribuye un costo a un destino, como un producto, servicio, equipo, unidad organizativa o centro de costo. La atribución puede apoyarse en cuentas, jerarquías, etiquetas, datos de consumo u otras evidencias. La estrategia debe declarar alcance, periodo, granularidad, jerarquía de destinos y tratamiento de excepciones para que la asignación sea comprensible y repetible \cite{finops-allocation}.
% \cite{finops-allocation}: FP-170, referencia [3], FinOps Foundation, ``Allocation''.

\subsubsection{Costos directos, compartidos y no asignados}

\begin{description}
  \item[Costo directo.] Costo atribuible a un único destino sin necesidad de reparto.
  \item[Costo compartido.] Costo que beneficia a varios destinos y requiere una decisión de distribución o retención central.
  \item[Costo no asignado.] Costo que todavía no tiene un destino válido conforme a la política declarada.
\end{description}

Los costos pueden ser directos o compartidos por su relación con los destinos; \emph{no asignado} describe su estado de atribución, no una tercera naturaleza excluyente. Un costo no asignado no debe confundirse con uno compartido: en el compartido se conoce la naturaleza común del gasto; en el no asignado falta información o un mecanismo aplicado para atribuirlo. La práctica de \emph{informed ignore} permite retener centralmente un costo compartido mediante una decisión consciente de no distribuirlo, sin clasificarlo como costo no identificado \cite{finops-allocation}.

Los fondos compartidos reúnen costos de capacidades, plataformas o servicios comunes. Su distribución requiere un \textbf{conductor de asignación} que represente la participación de cada destino. Puede basarse en mediciones de uso o en un indicador sustituto con una relación causal comprensible respecto del costo. Entre los conductores candidatos se encuentran solicitudes, tiempo de CPU, capacidad de almacenamiento, usuarios activos o gasto directo. La selección depende de su capacidad para representar la causa o el grado de uso, de su medición consistente y de su comprensión por quienes revisan la asignación.

\subsubsection{Etiquetas y políticas de asignación}

El \textbf{etiquetado} incorpora metadatos a cuentas, recursos o registros de consumo. Ejemplos genéricos son \texttt{owner}, para el responsable; \texttt{product}, para el producto o servicio; \texttt{environment}, para el entorno; y \texttt{cost\_center}, para el destino financiero. Son categorías mínimas de identificación, no una taxonomía adoptada.

Las etiquetas facilitan clasificar y agrupar costos y pueden aportar evidencia para una asignación directa o delimitar un reparto \cite{finops-allocation}. Sin embargo, una etiqueta no equivale a una política de asignación. El metadato describe el recurso o consumo; la política establece qué costos se distribuyen, hacia qué destinos, mediante qué regla y durante qué periodo. En servicios compartidos, conocer el responsable o entorno no determina cómo repartir el costo.

\subsubsection{Showback y chargeback}

El \textbf{showback} comunica los costos asignados y las reglas que los sustentan, pero no transfiere esos importes contablemente. Su propósito es dar visibilidad sobre consumo, propiedad y responsabilidad, de modo que los destinatarios puedan interpretar y cuestionar la información presentada \cite{finops-reporting-analytics,finops-invoicing-chargeback}.
% \cite{finops-reporting-analytics}: FP-170, referencia [4], FinOps Foundation, ``Reporting & Analytics''.
% \cite{finops-invoicing-chargeback}: FP-170, referencia [6], FinOps Foundation, ``Invoicing & Chargeback''.

El \textbf{chargeback} utiliza la información de asignación y reporte para trasladar o registrar costos en presupuestos, centros de costo o sistemas financieros. A diferencia del showback, produce una imputación interna formal y requiere políticas contables, destinos financieros, conciliación, cierres y mecanismos de corrección \cite{finops-invoicing-chargeback}. No exige un pago externo adicional: el pago de la factura al proveedor y la distribución interna de esa responsabilidad son procesos distintos. Adoptar chargeback depende de la política contable de la organización y no indica automáticamente un nivel superior de madurez.

\subsubsection{Tasa, cobertura y conservación}

La \textbf{tasa de asignación} es un valor práctico por unidad que permite distribuir un fondo compartido mediante el conductor elegido; no es la cobertura de asignación. La \textbf{cobertura de asignación} responde a una pregunta distinta: qué parte del costo total tiene un destino válido según la política y la granularidad declaradas \cite{finops-allocation}. Un importe retenido en un destino central explícito puede contar como costo con destino en la cobertura general, pero no como costo distribuido a productos; ambas vistas deben diferenciarse.

La \textbf{conservación} exige que lo distribuido entre los destinos, más cualquier importe retenido de manera intencional, coincida con el fondo inicial. Las diferencias pequeñas producidas por redondeos deben conciliarse y quedar documentadas. Si no existe un conductor utilizable o el total medido es cero, no se debe forzar el reparto: el importe se retiene y documenta hasta contar con una regla válida. Los créditos y reembolsos pueden distorsionar los porcentajes, por lo que la política debe indicar si se tratan de forma neta, bruta o separada.

% TODO (HUMANO): definir y justificar la política de asignación aplicable al caso
% del proyecto, incluidos destinos, conductores, periodo y tratamiento de excepciones.
% TODO (HUMANO): incorporar datos verificados del caso para calcular tasa y
% cobertura y comprobar conservación. Los artefactos fuente no contienen esos datos.
% TODO (HUMANO): realizar la aplicación concreta al caso de licitación del grupo.
% TODO (HUMANO): redactar conclusiones y recomendaciones; esta parte está
% expresamente reservada para autoría humana.
```

## Verificación contra las indicaciones y la ficha

Las citas siguientes reproducen literalmente las líneas pertinentes de `INVESTIGACION/Indicaciones Trabajo de Investigacion 2026.md`.

| Requisito extraído (cita precisa) | Estado | Evidencia o acción pendiente |
|---|---|---|
| “El trabajo debe presentar los conceptos del tema indicado en el título, con las características principales señaladas en la ficha que se entrega más adelante.” | cubierto | La sección presenta fases, personas y asignación de costos. |
| “El análisis no puede ser una copia extraída de Internet: se chequeará.” | requiere decisión humana | El bloque adapta los artefactos verificados; el grupo debe revisar las fuentes originales y sostener su análisis. |
| “La ficha define el piso exigible, no el techo. Cumplir literalmente la ficha permite aprobar; distinguirse requiere aporte propio, en los términos del punto 4 de estas indicaciones.” | pendiente | El aporte propio está reservado mediante comentarios `TODO (HUMANO)`. |
| “Identificación del aporte. El informe debe incluir, al cierre de la introducción, un párrafo breve que distinga qué proviene de la ficha y qué es aporte del grupo. Ese párrafo se usa como referencia al evaluar el análisis crítico.” | pendiente | Debe redactarlo el grupo al cierre de la introducción. |
| “Qué se valora. Comparaciones no evidentes, evidencia contradictoria bien tratada, aplicación concreta al caso de licitación del propio grupo, mediciones o pruebas realizadas por el equipo, y una recomendación con la que el grupo se comprometa.” | pendiente | Contenido reservado para autoría humana; los artefactos no incluyen aplicación ni mediciones del caso. |
| “Marco FinOps: fases informar, optimizar y operar; roles y responsabilidades entre ingeniería, finanzas y adquisiciones.” | cubierto | Subsecciones de fases y personas. |
| “Asignación de costos: etiquetado, showback frente a chargeback, costos compartidos y tasa de asignación.” | cubierto | Subsección de asignación de costos. |
| “Las herramientas de inteligencia artificial pueden usarse como apoyo, pero toda afirmación, cifra y referencia debe verificarse contra su fuente original. Una referencia inexistente o una cifra sin respaldo se evalúa como error grave.” | requiere decisión humana | Deben sustituirse los `\cite{}` por claves bibliográficas verificadas y comprobarse cada fuente original. |
| “El análisis comparativo y la justificación de los criterios utilizados.” | pendiente | Autoría humana obligatoria según 6.1. |
| “Las conclusiones y recomendaciones.” | pendiente | Autoría humana obligatoria según 6.1. |
| “El párrafo de aporte propio y la discusión crítica de la evidencia.” | pendiente | Autoría humana obligatoria según 6.1. |
| “La producción de cifras, citas o referencias: estas se obtienen de la fuente, no del modelo.” | requiere decisión humana | No se añadieron cifras nuevas; el grupo debe verificar y producir las referencias definitivas desde las fuentes. |
| “Se admite el uso de IA, declarándose, para: búsqueda inicial de fuentes que luego se verifican en el original, traducción, corrección gramatical y de estilo, apoyo de formato y diagramación, y generación de código auxiliar identificado como tal.” | cubierto | El uso de este archivo se identifica como apoyo de formato y adaptación; la declaración final debe completarla cada integrante. |
| “El nivel de uso declarado por sección del informe, no un nivel global único.” | pendiente | Completar la declaración por esta sección y por cada sección restante. |
| “Las herramientas y versiones utilizadas en cada caso.” | pendiente | Completar herramienta y versión reales. |
| “Para los niveles 2 y 3, los prompts efectivamente empleados, evidencia trazable: enlace o exportación de las conversaciones utilizadas y el historial de versiones del documento (historial de Google Docs, control de cambios de Word o repositorio con sus commits), de modo que sea posible reconstruir cómo se escribió el texto.” | pendiente | Adjuntar prompt, conversación e historial si se declara nivel 2 o 3. |
| “La declaración de cada integrante. Cada uno declara su propio uso: nadie declara por otro. La declaración es individual aunque el informe sea grupal.” | requiere decisión humana | Cada integrante debe completar y firmar su propia declaración. |
| “Todo informe incluye un anexo de declaración, aunque el nivel declarado sea 0.” | pendiente | Incorporar el anexo completo al informe. |

## Bloque listo para completar: declaración de uso de IA

> **Importante:** el nivel debe reflejar el uso real y ser declarado por cada integrante. La calificación del nivel no se completa automáticamente. Dado que una herramienta generó esta sección completa a partir de artefactos proporcionados, el grupo debe contrastar el uso real con la definición institucional de **Nivel 3** y decidirlo responsablemente; no debe declarar un nivel inferior al real.

| Campo obligatorio | Completar por el integrante |
|---|---|
| Nombre completo | `[NOMBRE DEL INTEGRANTE]` |
| Sección del informe | `Marco conceptual de FinOps: fases, roles y asignación de costos` |
| Nivel declarado (0–3) | `[NIVEL REAL]` |
| Herramienta y versión | `[HERRAMIENTA Y VERSIÓN EXACTAS]` |
| Uso realizado | `[DESCRIBIR EL APOYO REAL: adaptación de artefactos, formato LaTeX u otro]` |
| Prompts efectivamente empleados (obligatorio para niveles 2 y 3) | `[PEGAR PROMPT COMPLETO]` |
| Evidencia trazable (obligatoria para niveles 2 y 3) | `[ENLACE O EXPORTACIÓN DE LA CONVERSACIÓN]` |
| Historial de versiones (obligatorio para niveles 2 y 3) | `[ENLACE AL HISTORIAL O REPOSITORIO]` |
| Validación humana de afirmaciones | `[FUENTES ORIGINALES REVISADAS, POR QUIÉN Y FECHA]` |
| Validación humana de cifras | `No se incorporaron cifras nuevas; [CONFIRMAR TRAS REVISIÓN]` |
| Validación humana de referencias | `[CLAVES BIBLIOGRÁFICAS Y FUENTES ORIGINALES VERIFICADAS]` |
| Confirmación de autoría humana reservada | `[CONFIRMAR que análisis comparativo, conclusiones, recomendaciones, aporte propio y discusión crítica fueron redactados por el grupo]` |
| Firma | `[FIRMA]` |
| Fecha | `[FECHA]` |
