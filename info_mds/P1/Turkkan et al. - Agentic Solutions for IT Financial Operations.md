# Agentic Solutions for IT Financial Operations

> **Pilar:** P1
> **Clasificación:** Declarada en la matriz
> **Evidencia de clasificación:** Fila académica del CSV titulada “Agentic Solutions for IT Financial Operations”, código P1.
> **Archivo fuente:** papers-pdf/Turkkan et al. - Agentic Solutions for IT Financial Operations.pdf
> **Uso previsto:** Lectura personal y apoyo documental; requiere validación humana antes de incorporarse al informe.

## 1. Título

*Agentic Solutions for IT Financial Operations*.

## 2. Autor y fecha

- **Autores verificados en el PDF:** Bekir O. Turkkan, Pavankumar Murali, Chandrasekhar Narayanaswami y Vadim Sheinin, de IBM Research. El documento indica que Turkkan y Murali contribuyeron en igual medida.
- **Fecha bibliográfica utilizada:** 2026, por su inclusión en la *Fortieth AAAI Conference on Artificial Intelligence (AAAI-26)* y el aviso de copyright 2026.
- **Discrepancia documentada:** el nombre del archivo omite el año; la matriz declara 2026 y el propio PDF confirma AAAI-26. Se usa **2026**.

## 3. Problema que trata

Los datos de facturación cloud presentan taxonomías, métricas y precios heterogéneos que cambian continuamente. Los profesionales de FinOps necesitan responder consultas, explicar anomalías y obtener información accionable con rapidez, pero los agentes generales fallan en tareas financieras complejas por errores de esquema, consultas SQL incorrectas, alucinaciones y mala descomposición de tareas.

## 4. Qué quiere hacer

Presentar y evaluar un **FinOps Data Insights Agent** que permita conversar en lenguaje natural con datos financieros de TI. El objetivo es mejorar la precisión en consultas FinOps mediante planificación, selección de herramientas, validación de entradas y salidas, reflexión y descomposición de consultas complejas.

## 5. Cómo lo hace

Describe cuatro iteraciones del agente. La v0.1 combina ReAct, CrewAI y una herramienta SQL propia; la v0.2 refina prompts a partir de trayectorias; la v0.3 incorpora una canalización Text2SQL con enlazado de esquema, optimización de prompt, inferencia, linter y ejecutor; la v0.4 agrega una herramienta universal que ejecuta Python y divide cálculos complejos en pasos simples. La evaluación usa datos de muestra en formato FOCUS almacenados en MySQL, seis escenarios de ITBench y cuatro familias de modelos, con diez ejecuciones por escenario (secciones **System Overview**, **Landscape...** y **Evaluation**).

## 6. Resultados

- La primera versión confundía columnas y alucinaba resultados; la estructuración del flujo redujo esos fallos, aunque el ajuste de prompts resultó dependiente del modelo.
- Text2SQL mejoró el desempeño de todos los modelos, pero mantuvo dificultades con consultas anidadas complejas.
- La descomposición de consultas y el uso combinado de Text2SQL y Python elevó la exactitud hasta **90 %** en los escenarios evaluados (sección **Evaluation**, figura 1, p. 41704).
- En **Future Work and Discussion**, los autores informan que la v0.4 supera 90 % de exactitud y mejora en más de 80 % respecto de versiones previas en los benchmarks citados. Es un resultado sobre datos de muestra y una métrica binaria por ejecución, no sobre facturación productiva.

## 7. Discusión y trabajo futuro

Los fallos restantes incluyen errores sintácticos en SQL o Python, llamadas repetidas a herramientas y errores semánticos de columnas o valores. Los autores trabajan en verificadores sintácticos y semánticos y en análisis de trayectorias. También reconocen que el acceso directo a los datos puede dificultar la adopción y proponen sustituir esa capa por una API.

## 8. Conclusión del paper

El documento no contiene una sección independiente titulada “Conclusion”. En su discusión final, los autores sostienen que la arquitectura planificadora con Text2SQL, ejecución de Python y descomposición de tareas mejora sustancialmente la exactitud de un agente de información FinOps. Al mismo tiempo, dejan explícito que persisten errores y que son necesarios controles adicionales.

## Relación preliminar con INV-01

Puede apoyar la lectura de visibilidad de costos, estandarización FOCUS y automatización para transformar datos de facturación en información comprensible, vinculadas con 3.1–3.5 y 4.1–4.3 de INV-01. No demuestra por sí solo asignación correcta, ahorro real ni aptitud para decisiones autónomas en producción.

## Limitaciones de esta síntesis

El paper tiene tres páginas y carácter de demostración. La evaluación usa un dataset FOCUS de muestra, seis escenarios y no informa costo operativo del agente ni validación con facturas reales. Las cifras deben verificarse humanamente en la figura y el texto del PDF; esta síntesis no autoriza trasladarlas como conclusión del informe.

## Texto extraído del PDF

> **Advertencia de conversión:** extracción textual automática de 3 páginas (13899 caracteres). Se conservaron títulos, párrafos, referencias y contenido textual por página. La disposición multicolumna, las figuras, las tablas y las ecuaciones pueden no mantener su alineación o representación visual; verifique esos elementos en el PDF original.

### Página PDF 1

The Fortieth AAAI Conference on Artificial Intelligence (AAAI-26)


                 Agentic Solutions for IT Financial Operations


    Bekir O. Turkkan*, Pavankumar Murali*, Chandrasekhar Narayanaswami, Vadim Sheinin

                                    IBM Research


                      Abstract                              Recent advances in agent-based systems (e.g.: (Yao et al.
                                                            2023)) address IT incident resolution, compliance, risk man-  The dynamic nature of cloud spending and pricing structures
                                                       agement etc., but do not perform well for IT FinOps tasks  pose challenges for practitioners in IT Financial Operations
   (FinOps). Recent advances in agentic systems enables them        such as identifying root cause for an anomalous increase in
   to instead rely on agents for complex FinOps tasks such as        spend for a specific service or application. Consequently,
  drawing insights from their data through natural language         there is an urgent need to develop agents that utilize and
   queries. In this work, we present an IT FinOps Data Insights         correctly interpret IT billing systems, business mappings,
  Agent, that implements “chat with your data” approach to          tags, hyperscaler pricing structures, organizational IT sys-
   support practitioners in their daily tasks. Our agent achieves       tem topologies and hierarchies, resource utilization and ob-
  up to 90% accuracy across ITBench FinOps scenarios.               servability metrics to assist practitioners in decision-making.
                                                                  In this demonstration, we present versions of our FinOps
                Introduction                        Data Insights Agent with an intent to enable FinOps practi-
As organizations shift their infrastructure to the cloud, hy-       tioners to interact with their data and draw insights through
perscalers employ a dynamic, on-demand pricing structure       natural language queries. The performance of our agent is
making cost management a complex and continuous chal-      evaluated on the data insights benchmarks defined in (Jha
lenge. As per the FinOps Foundation’s 2025 State of FinOps        et al. 2025). We also share our learnings based on agent
report (FinOps Foundation 2025c), over 20% of large orga-        trajectories, common errors encountered and improvement
nizations spent upwards of $1B a year on their cloud infras-       strategies that were found to be successful in improving our
tructure. Organizations receive billing data in various forms,       agent’s performance. Although we focus on Cloud FinOps
taxonomies, and metrics. The ability to interpret heteroge-       tasks for evaluation, the agentic architecture, tools used,
neous IT billing data is key for monitoring IT systems, di-       analysis and improvement methods apply more broadly
agnosis and remediation of events. FinOps practitioners face       to other FinOps domains and scopes(FinOps Foundation
considerable challenges in synthesizing insights from these      2025c).
disparate data sources in a time-sensitive manner to drive
action recommendation and cost and resource optimization.
                                                        System Overview  To address these challenges, autonomous and goal-driven
AI agents are being used to handle complex tasks in IT Au-     Our FinOps Data Insights Agent, built using a Langgraph
tomation and FinOps. These agents consume user queries       architecture, enables  practitioners  to  interact with  their
in natural language and perform tasks that involve tasks       data through natural language queries and obtain finan-
such as analyzing cloud bills, extracting data insights, de-        cial data in fully customized formats by using Langchain’s
tecting anomalies, identifying causal factors for various     ChatPromptTemplate. It is a planning agent that un-
types of events, and making proactive recommendations for      derstands a natural language query from a user, analyzes it
cost optimization without constant human intervention. Ma-      and constructs a detailed execution plan. Each step in the
jor cloud providers are integrating such agents into their      plan specifies (i) the input derived from the previous step,
platforms to enhance FinOps practices and, in turn, en-         (ii) the tool required for execution, and (iii) the expected
able users to manage cloud spend across their portfolios      output format for subsequent processing or for generating
(FinOps Foundation 2025a). For example, AWS offers Cost       the final response. The agent follows the plan and validates
Explorer (AWS 2025)and Cost Anomaly Detection (AWS       the input–output formats at each step. As part of the reflec-
2024) which FinOps practitioners can use to recommend       tion process, the agent evaluates its own actions and outputs
ideal compute resources to balance performance and cost as       to self-correct and improve its performance if necessary. Re-
well as identify unexpected spending hikes.                         flection could entail backtracking and redoing the incorrect
   *These authors contributed equally.                                steps or reformulating the entire execution plan. Finally, the
Copyright © 2026, Association for the Advancement of Artificial      agent returns a final response to the user to ensure an accu-
Intelligence (www.aaai.org). All rights reserved.                         rate and coherent response.


                                                  41703

### Página PDF 2

Landscape of FinOps Data Insights Agents
In this section, we present our approach towards developing
a high-performing FinOps agent. Through iterative prompt
tuning by analyzing agent trajectories, integrating advanced
tools, and decomposing complex tasks, we systematically
enhanced the agent’s performance. Agent v.0.1 was devel-
oped using a ReAct framework(Yao et al. 2023) with Cre-
wAI(crewAI 2025). This agent used a custom tool for SQL
operations that employed an LLM Backend to generate SQL
queries based on the user, system, and agent prompts. We
provided information about the data with examples and col-
umn names along with the description of the tasks. This ver-
                                                             Figure 1: Average performance of the FinOps Data Agent
sion of our agent struggled to identify the right columns
                                                                across six ITBench scenarios over ten runs per scenario.
of the data and hallucinated significantly to complete the
prompted task in the desired output format.
  Next, for Agent v.0.2 we analyzed the trajectories from
Agent v.0.1 to identify common errors and the areas where                     Evaluation
the agent needed more guidance. We optimized the agent
and system prompts to lead our agent to a more structured     To evaluate our agents, we used a sample dataset in FO-
workflow and to avoid the errors from the earlier version.    CUS format from FinOps Foundation(FinOps Foundation
Tuning and structuring prompts improved the agent’s per-      2025b) and stored it into a MySQL database as a single ta-
formance in tool calling and reduced hallucinations. How-       ble. We adopt six FinOps scenarios defined in the ITBench
ever, the performance in SQL generation was limited and it      framework (Jha et al. 2025) which involves tasks includ-
required tuning for each underlying LLM.                       ing basic data retrieval and aggregation (easy), data extrac-
  To improve the SQL generation, we replaced the cus-       tion from structured data objects (medium), and construc-
tom SQL tool with an advanced Text2SQL tool(Rossiello       tion of multiple nested queries (difficult). We have evalu-
et al. 2025) in Agent v.0.3. The Text2SQL tool is designed       ated our proposed approach with state of the art LLM mod-
to facilitate natural language interaction with data via em-       els as follows, gpt-4o, llama-3.3-70b-instruct,
bedded execution pipelines and leveraging LLM technology.     llama4-mavericks, and mistral-large.
We used a pipeline including a schema linker, prompt opti-         Figure 1 presents the evaluation results for accuracy
mizer, LLM inference, SQL linter, and SQL executor com-       across all six scenarios, averaged over ten independent runs.
ponents. Each pipeline starts with a plain English query.     The accuracy for a run can be either 100 when the agent’s
Then, schema linker identifies related fields and tables from      output matches the ground truth values, or 0 when it does not
the database using structured database information which in-      match. Our findings indicate that the applied prompt-tuning
cludes table and field names, types, descriptions, and exam-       strategy is model dependent. We tuned prompts with Llama
ple values (Glass et al. 2025). Prompt optimizer reconstructs      3.3-70b model trajectories which results in performance
the user and system prompts to be used for LLM inference.      gains only for Llama models. Incorporating the Text2SQL
Next, an LLM is invoked to generate required SQL code for       tool for database operations improves the performance for
the task. The generated code is evaluated by the SQL linter        all models significantly, although challenges remain in han-
to ensure execution without errors. Finally, SQL executor re-       dling complex queries. Decomposing user queries into sim-
turns the result of generated SQL query. While the agent is       pler tasks enhances the performance substantially, with ac-
capable of generating meaningful SQL queries, its accuracy      curacy reaching up to 90% across the evaluated models.
can diminish when addressing highly complex tasks that re-
quire multiple levels of nested queries.
  For highly complex queries, we developed Agent v.0.4             Future Work and Discussion
by integrating Text2SQL tool with a new customized uni-
versal tool that executes the Python code generated by the      FinOps tasks require accurate data insights. Our evaluations
LLM. This planning agent is guided to construct an execu-       indicate Agent v.0.4 has a greater than 90% accuracy and
tion plan with simpler tasks to minimize reliance on deeply      outperforms the previous versions by greater than 80% when
nested SQL statements. It uses the Text2SQL tool to retrieve       tested on benchmarks defined in (Jha et al. 2025).
data using straightforward queries and delegates more com-         In unsuccessful runs, we found our agent fails due to one
plex calculations to the universal tool. The agent is guided       or more of the following: (i) syntactic errors in generated
with detailed tool descriptions, their capabilities, and exam-    SQL query or Python script (ii) repeated tool calling when
ples in decomposing a user query into simpler tasks and del-      not needed (iii) semantic errors such as using the wrong col-
egating them to the provided tools. Agent v.0.4 stores the     umn names or values. Our current efforts include developing
output from Text2SQL as a .csv file and passes the file infor-       syntactic and semantic checkers as well as evaluating trajec-
mation along with the executed SQL query to the universal       tories to alleviate such issues. Requiring direct access to data
tool which leverages the SQL query to learn field names and     may involve challenges for adoption but our approach allows
values.                                                          replacing data layer with API to overcome these challenges.


                                                  41704

### Página PDF 3

References
AWS. 2024.   Faster anomaly resolution with enhanced
root  cause  analysis  in AWS  Cost  Anomaly  Detec-
tion.   https://aws.amazon.com/blogs/aws-cloud-financial-
management/faster-anomaly-resolution-with-enhanced-
root-cause-analysis-in-aws-cost-anomaly-detection/.
Accessed: 2025-09-06.
AWS. 2025. AWS Cost Explorer. https://aws.amazon.com/
aws-cost-management/aws-cost-explorer/. Accessed: 2025-
09-06.
crewAI. 2025.   crewAI.   https://github.com/crewAIInc/
crewAI. Accessed: 2025-09-06.
FinOps Foundation. 2025a.  FinOps X 2025 Cloud An-
nouncements: AI Agents and  Increased FOCUS Sup-
port. https://www.finops.org/insights/finops-x-2025-cloud-
announcements/. Accessed: 2025-09-06.
FinOps  Foundation.  2025b.   FOCUS  sample  data.
https://github.com/FinOps-Open-Cost-and-Usage-
Spec/FOCUS-Sample-Data/tree/main. Accessed: 2025-09-
06.
FinOps Foundation. 2025c. State of FinOps: 2025 Report.
https://data.finops.org/. Accessed: 2025-09-06.
Glass, M.; Eyceoz, M.; Subramanian, D.; Rossiello, G.; Vu,
L.; and Gliozzo, A. 2025.  Extractive Schema Linking for
Text-to-SQL. arXiv:2501.17174.
Jha, S.; Arora, R.; Watanabe, Y.; Yanagawa, T.; Chen, Y.;
Clark, J.; Bhavya, B.; Verma, M.; Kumar, H.; Kitahara, H.;
Zheutlin, N.; Takano, S.; Pathak, D.; George, F.; Wu, X.;
Turkkan, B. O.; Vanloo, G.; Nidd, M.; Dai, T.; Chatter-
jee, O.; Gupta, P.; Samanta, S.; Aggarwal, P.; Lee, R.; Mu-
rali, P.; wook Ahn, J.; Kar, D.; Rahane, A.; Fonseca, C.;
Paradkar, A.; Deng, Y.; Moogi, P.; Mohapatra, P.; Abe, N.;
Narayanaswami, C.; Xu, T.; Varshney, L. R.; Mahindru, R.;
Sailer, A.; Shwartz, L.; Sow, D.; Fuller, N. C. M.; and Puri,
R. 2025.  ITBench: Evaluating AI Agents across Diverse
Real-World IT Automation Tasks. arXiv:2502.05352.
Rossiello, G.; Pham, N.; Glass, M.; Lee, J.; and Subrama-
nian, D. 2025.  Rationalization Models for Text-to-SQL.
arXiv:2502.06759.
Yao, S.; Zhao, J.; Yu, D.; Du, N.; Shafran, I.; Narasimhan,
K.; and Cao, Y. 2023. ReAct: Synergizing Reasoning and
Acting in Language Models. arXiv:2210.03629.


                                                  41705
