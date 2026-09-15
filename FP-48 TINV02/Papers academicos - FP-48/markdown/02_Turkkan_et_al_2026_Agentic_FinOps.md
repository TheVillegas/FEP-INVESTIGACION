TheFortiethAAAIConferenceonArtificialIntelligence(AAAI-26)
|     |     |     | Agentic |     | Solutions | for IT | Financial | Operations |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --------- | ------ | --------- | ---------- | --- | --- | --- | --- | --- | --- |
BekirO.Turkkan*,PavankumarMurali*,ChandrasekharNarayanaswami,VadimSheinin
IBMResearch
|     |     |     | Abstract |     |     |     | Recentadvancesinagent-basedsystems(e.g.:(Yaoetal. |     |     |     |     |     |     |     |
| --- | --- | --- | -------- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
2023))addressITincidentresolution,compliance,riskman-
Thedynamicnatureofcloudspendingandpricingstructures
|     |     |     |     |     |     |     | agement | etc., but | do not | perform | well | for IT | FinOps | tasks |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ------ | ------- | ---- | ------ | ------ | ----- |
posechallengesforpractitionersinITFinancialOperations
suchasidentifyingrootcauseforananomalousincreasein
(FinOps).Recentadvancesinagenticsystemsenablesthem
|            |      |           |             |        |     |               | spend for | a specific | service |     | or application. |     | Consequently, |     |
| ---------- | ---- | --------- | ----------- | ------ | --- | ------------- | --------- | ---------- | ------- | --- | --------------- | --- | ------------- | --- |
| to instead | rely | on agents | for complex | FinOps |     | tasks such as |           |            |         |     |                 |     |               |     |
drawing insights from their data through natural language there is an urgent need to develop agents that utilize and
queries.Inthiswork,wepresentanITFinOpsDataInsights correctly interpret IT billing systems, business mappings,
Agent, that implements “chat with your data” approach to tags, hyperscaler pricing structures, organizational IT sys-
supportpractitionersintheirdailytasks.Ouragentachieves temtopologiesandhierarchies,resourceutilizationandob-
upto 90%accuracyacrossITBenchFinOpsscenarios. servabilitymetricstoassistpractitionersindecision-making.
Inthisdemonstration,wepresentversionsofourFinOps
Introduction
DataInsightsAgentwithanintenttoenableFinOpspracti-
As organizations shift their infrastructure to the cloud, hy- tionerstointeractwiththeirdataanddrawinsightsthrough
|            |        |            |     |           |         |           | natural language |     | queries. | The | performance |     | of our agent | is  |
| ---------- | ------ | ---------- | --- | --------- | ------- | --------- | ---------------- | --- | -------- | --- | ----------- | --- | ------------ | --- |
| perscalers | employ | a dynamic, |     | on-demand | pricing | structure |                  |     |          |     |             |     |              |     |
making cost management a complex and continuous chal- evaluated on the data insights benchmarks defined in (Jha
lenge.AspertheFinOpsFoundation’s2025StateofFinOps et al. 2025). We also share our learnings based on agent
report(FinOpsFoundation2025c),over20%oflargeorga- trajectories, common errors encountered and improvement
nizationsspentupwardsof$1Bayearontheircloudinfras- strategiesthatwerefoundtobesuccessfulinimprovingour
|     |     |     |     |     |     |     | agent’s performance. |     | Although |     | we focus | on  | Cloud FinOps |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | -------- | --- | -------- | --- | ------------ | --- |
tructure.Organizationsreceivebillingdatainvariousforms,
taxonomies, and metrics. The ability to interpret heteroge- tasks for evaluation, the agentic architecture, tools used,
neous IT billing data is key for monitoring IT systems, di- analysis and improvement methods apply more broadly
agnosisandremediationofevents.FinOpspractitionersface to other FinOps domains and scopes(FinOps Foundation
| considerablechallengesinsynthesizinginsightsfromthese |              |     |                     |     |        |          | 2025c). |     |     |     |     |     |     |     |
| ----------------------------------------------------- | ------------ | --- | ------------------- | --- | ------ | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| disparate                                             | data sources |     | in a time-sensitive |     | manner | to drive |         |     |     |     |     |     |     |     |
actionrecommendationandcostandresourceoptimization. SystemOverview
Toaddressthesechallenges,autonomousandgoal-driven
AIagentsarebeingusedtohandlecomplextasksinITAu-
|            |             |     |              |         |      |               | Our FinOps    | Data    | Insights | Agent,        | built   | using       | a Langgraph |        |
| ---------- | ----------- | --- | ------------ | ------- | ---- | ------------- | ------------- | ------- | -------- | ------------- | ------- | ----------- | ----------- | ------ |
| tomation   | and FinOps. |     | These agents | consume |      | user queries  |               |         |          |               |         |             |             |        |
|            |             |     |              |         |      |               | architecture, | enables |          | practitioners |         | to interact | with        | their  |
| in natural | language    | and | perform      | tasks   | that | involve tasks |               |         |          |               |         |             |             |        |
|            |             |     |              |         |      |               | data through  | natural |          | language      | queries | and         | obtain      | finan- |
such as analyzing cloud bills, extracting data insights, de- cial data in fully customized formats by using Langchain’s
tecting anomalies, identifying causal factors for various ChatPromptTemplate. It is a planning agent that un-
typesofevents,andmakingproactiverecommendationsfor
|     |     |     |     |     |     |     | derstands | a natural | language |     | query from | a user, | analyzes | it  |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | -------- | --- | ---------- | ------- | -------- | --- |
costoptimizationwithoutconstanthumanintervention.Ma-
|           |           |     |             |      |        |            | and constructs |     | a detailed | execution |      | plan. Each | step     | in the |
| --------- | --------- | --- | ----------- | ---- | ------ | ---------- | -------------- | --- | ---------- | --------- | ---- | ---------- | -------- | ------ |
| jor cloud | providers | are | integrating | such | agents | into their |                |     |            |           |      |            |          |        |
|           |           |     |             |      |        |            | plan specifies | (i) | the input  | derived   | from | the        | previous | step,  |
platforms to enhance FinOps practices and, in turn, en- (ii) the tool required for execution, and (iii) the expected
able users to manage cloud spend across their portfolios output format for subsequent processing or for generating
(FinOpsFoundation2025a).Forexample,AWSoffersCost thefinalresponse.Theagentfollowstheplanandvalidates
| Explorer | (AWS | 2025)and | Cost | Anomaly | Detection | (AWS |     |     |     |     |     |     |     |     |
| -------- | ---- | -------- | ---- | ------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
theinput–outputformatsateachstep.Aspartofthereflec-
| 2024) which | FinOps | practitioners |     | can | use to | recommend |     |     |     |     |     |     |     |     |
| ----------- | ------ | ------------- | --- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
tionprocess,theagentevaluatesitsownactionsandoutputs
idealcomputeresourcestobalanceperformanceandcostas toself-correctandimproveitsperformanceifnecessary.Re-
wellasidentifyunexpectedspendinghikes. flectioncouldentailbacktrackingandredoingtheincorrect
stepsorreformulatingtheentireexecutionplan.Finally,the
*Theseauthorscontributedequally.
Copyright©2026,AssociationfortheAdvancementofArtificial agentreturnsafinalresponsetotheusertoensureanaccu-
Intelligence(www.aaai.org).Allrightsreserved. rateandcoherentresponse.
41703

LandscapeofFinOpsDataInsightsAgents
Inthissection,wepresentourapproachtowardsdeveloping
| a high-performing |     | FinOps | agent. | Through |     | iterative | prompt |     |     |     |     |     |
| ----------------- | --- | ------ | ------ | ------- | --- | --------- | ------ | --- | --- | --- | --- | --- |
tuningbyanalyzingagenttrajectories,integratingadvanced
| tools, and | decomposing |         | complex       | tasks, | we     | systematically |           |     |     |     |     |     |
| ---------- | ----------- | ------- | ------------- | ------ | ------ | -------------- | --------- | --- | --- | --- | --- | --- |
| enhanced   | the         | agent’s | performance.  |        | Agent  | v.0.1 was      | devel-    |     |     |     |     |     |
| oped using | a           | ReAct   | framework(Yao |        | et al. | 2023)          | with Cre- |     |     |     |     |     |
wAI(crewAI2025).ThisagentusedacustomtoolforSQL
operationsthatemployedanLLMBackendtogenerateSQL
| queries | based | on the | user, system, |     | and agent | prompts. | We  |     |     |     |     |     |
| ------- | ----- | ------ | ------------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- |
providedinformationaboutthedatawithexamplesandcol-
umnnamesalongwiththedescriptionofthetasks.Thisver-
|         |           |           |     |             |     |       |         | Figure 1: Average | performance | of the FinOps | Data | Agent |
| ------- | --------- | --------- | --- | ----------- | --- | ----- | ------- | ----------------- | ----------- | ------------- | ---- | ----- |
| sion of | our agent | struggled |     | to identify | the | right | columns |                   |             |               |      |       |
acrosssixITBenchscenariosovertenrunsperscenario.
| of the | data and | hallucinated |     | significantly |     | to complete | the |     |     |     |     |     |
| ------ | -------- | ------------ | --- | ------------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
promptedtaskinthedesiredoutputformat.
| Next, | for Agent | v.0.2 | we  | analyzed | the | trajectories | from |     |     |     |     |     |
| ----- | --------- | ----- | --- | -------- | --- | ------------ | ---- | --- | --- | --- | --- | --- |
Evaluation
Agentv.0.1toidentifycommonerrorsandtheareaswhere
| the agent | needed | more | guidance. | We  | optimized |     | the agent |     |     |     |     |     |
| --------- | ------ | ---- | --------- | --- | --------- | --- | --------- | --- | --- | --- | --- | --- |
and system prompts to lead our agent to a more structured To evaluate our agents, we used a sample dataset in FO-
workflow and to avoid the errors from the earlier version. CUS format from FinOps Foundation(FinOps Foundation
2025b)andstoreditintoaMySQLdatabaseasasingleta-
| Tuning | and structuring |     | prompts | improved |     | the agent’s | per- |     |     |     |     |     |
| ------ | --------------- | --- | ------- | -------- | --- | ----------- | ---- | --- | --- | --- | --- | --- |
ble.WeadoptsixFinOpsscenariosdefinedintheITBench
| formance | in tool | calling | and | reduced | hallucinations. |     | How- |     |     |     |     |     |
| -------- | ------- | ------- | --- | ------- | --------------- | --- | ---- | --- | --- | --- | --- | --- |
ever,theperformanceinSQLgenerationwaslimitedandit framework (Jha et al. 2025) which involves tasks includ-
requiredtuningforeachunderlyingLLM. ingbasicdataretrievalandaggregation(easy),dataextrac-
To improve the SQL generation, we replaced the cus- tion from structured data objects (medium), and construc-
|         |      |      |             |          |     |                |     | tion of multiple | nested queries | (difficult). | We have | evalu- |
| ------- | ---- | ---- | ----------- | -------- | --- | -------------- | --- | ---------------- | -------------- | ------------ | ------- | ------ |
| tom SQL | tool | with | an advanced | Text2SQL |     | tool(Rossiello |     |                  |                |              |         |        |
atedourproposedapproachwithstateoftheartLLMmod-
etal.2025)inAgentv.0.3.TheText2SQLtoolisdesigned
|               |         |          |     |             |      |      |         |                 | gpt-4o, llama-3.3-70b-instruct, |     |     |     |
| ------------- | ------- | -------- | --- | ----------- | ---- | ---- | ------- | --------------- | ------------------------------- | --- | --- | --- |
| to facilitate | natural | language |     | interaction | with | data | via em- | els as follows, |                                 |     |     |     |
beddedexecutionpipelinesandleveragingLLMtechnology. llama4-mavericks,andmistral-large.
Weusedapipelineincludingaschemalinker,promptopti- Figure 1 presents the evaluation results for accuracy
mizer,LLMinference,SQLlinter,andSQLexecutorcom-
acrossallsixscenarios,averagedovertenindependentruns.
ponents. Each pipeline starts with a plain English query. The accuracy for a run can be either 100 when the agent’s
Then,schemalinkeridentifiesrelatedfieldsandtablesfrom outputmatchesthegroundtruthvalues,or0whenitdoesnot
thedatabaseusingstructureddatabaseinformationwhichin- match.Ourfindingsindicatethattheappliedprompt-tuning
cludestableandfieldnames,types,descriptions,andexam- strategyismodeldependent.WetunedpromptswithLlama
plevalues(Glassetal.2025).Promptoptimizerreconstructs
|     |     |     |     |     |     |     |     | 3.3-70b model | trajectories | which results | in performance |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------ | ------------- | -------------- | --- |
theuserandsystempromptstobeusedforLLMinference. gains only for Llama models. Incorporating the Text2SQL
Next,anLLMisinvokedtogeneraterequiredSQLcodefor tool for database operations improves the performance for
thetask.ThegeneratedcodeisevaluatedbytheSQLlinter allmodelssignificantly,althoughchallengesremaininhan-
toensureexecutionwithouterrors.Finally,SQLexecutorre- dlingcomplexqueries.Decomposinguserqueriesintosim-
turnstheresultofgeneratedSQLquery.Whiletheagentis
|     |     |     |     |     |     |     |     | pler tasks enhances | the performance | substantially, |     | with ac- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --------------- | -------------- | --- | -------- |
capableofgeneratingmeaningfulSQLqueries,itsaccuracy curacyreachingupto90%acrosstheevaluatedmodels.
candiminishwhenaddressinghighlycomplextasksthatre-
quiremultiplelevelsofnestedqueries.
For highly complex queries, we developed Agent v.0.4 FutureWorkandDiscussion
| by integrating |     | Text2SQL | tool | with | a new | customized | uni- |     |     |     |     |     |
| -------------- | --- | -------- | ---- | ---- | ----- | ---------- | ---- | --- | --- | --- | --- | --- |
versal tool FinOpstasksrequireaccuratedatainsights.Ourevaluations
|      | that          | executes | the      | Python | code         | generated | by the    |                |             |                  |          |     |
| ---- | ------------- | -------- | -------- | ------ | ------------ | --------- | --------- | -------------- | ----------- | ---------------- | -------- | --- |
|      |               |          |          |        |              |           |           | indicate Agent | v.0.4 has a | greater than 90% | accuracy | and |
| LLM. | This planning |          | agent is | guided | to construct |           | an execu- |                |             |                  |          |     |
outperformsthepreviousversionsbygreaterthan80%when
tionplanwithsimplertaskstominimizerelianceondeeply
nestedSQLstatements.ItusestheText2SQLtooltoretrieve testedonbenchmarksdefinedin(Jhaetal.2025).
datausingstraightforwardqueriesanddelegatesmorecom- Inunsuccessfulruns,wefoundouragentfailsduetoone
plex calculations to the universal tool. The agent is guided or more of the following: (i) syntactic errors in generated
withdetailedtooldescriptions,theircapabilities,andexam- SQL query or Python script (ii) repeated tool calling when
plesindecomposingauserqueryintosimplertasksanddel- notneeded(iii)semanticerrorssuchasusingthewrongcol-
egating them to the provided tools. Agent v.0.4 stores the umnnamesorvalues.Ourcurrenteffortsincludedeveloping
outputfromText2SQLasa.csvfileandpassesthefileinfor- syntacticandsemanticcheckersaswellasevaluatingtrajec-
mationalongwiththeexecutedSQLquerytotheuniversal toriestoalleviatesuchissues.Requiringdirectaccesstodata
toolwhichleveragestheSQLquerytolearnfieldnamesand mayinvolvechallengesforadoptionbutourapproachallows
| values. |     |     |     |     |     |     |     | replacingdatalayerwithAPItoovercomethesechallenges. |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- |
41704

References
AWS. 2024. Faster anomaly resolution with enhanced
root cause analysis in AWS Cost Anomaly Detec-
tion. https://aws.amazon.com/blogs/aws-cloud-financial-
management/faster-anomaly-resolution-with-enhanced-
root-cause-analysis-in-aws-cost-anomaly-detection/.
Accessed:2025-09-06.
AWS.2025. AWSCostExplorer. https://aws.amazon.com/
aws-cost-management/aws-cost-explorer/.Accessed:2025-
09-06.
crewAI. 2025. crewAI. https://github.com/crewAIInc/
crewAI. Accessed:2025-09-06.
FinOps Foundation. 2025a. FinOps X 2025 Cloud An-
nouncements: AI Agents and Increased FOCUS Sup-
port. https://www.finops.org/insights/finops-x-2025-cloud-
announcements/. Accessed:2025-09-06.
FinOps Foundation. 2025b. FOCUS sample data.
https://github.com/FinOps-Open-Cost-and-Usage-
Spec/FOCUS-Sample-Data/tree/main. Accessed:2025-09-
06.
FinOps Foundation. 2025c. State of FinOps: 2025 Report.
https://data.finops.org/. Accessed:2025-09-06.
Glass,M.;Eyceoz,M.;Subramanian,D.;Rossiello,G.;Vu,
L.; and Gliozzo, A. 2025. Extractive Schema Linking for
Text-to-SQL. arXiv:2501.17174.
Jha, S.; Arora, R.; Watanabe, Y.; Yanagawa, T.; Chen, Y.;
Clark,J.;Bhavya,B.;Verma,M.;Kumar,H.;Kitahara,H.;
Zheutlin, N.; Takano, S.; Pathak, D.; George, F.; Wu, X.;
Turkkan, B. O.; Vanloo, G.; Nidd, M.; Dai, T.; Chatter-
jee,O.;Gupta,P.; Samanta,S.;Aggarwal,P.;Lee,R.; Mu-
rali, P.; wook Ahn, J.; Kar, D.; Rahane, A.; Fonseca, C.;
Paradkar, A.; Deng, Y.; Moogi, P.; Mohapatra, P.; Abe, N.;
Narayanaswami,C.;Xu,T.;Varshney,L.R.;Mahindru,R.;
Sailer,A.;Shwartz,L.;Sow,D.;Fuller,N.C.M.;andPuri,
R. 2025. ITBench: Evaluating AI Agents across Diverse
Real-WorldITAutomationTasks. arXiv:2502.05352.
Rossiello, G.; Pham, N.; Glass, M.; Lee, J.; and Subrama-
nian, D. 2025. Rationalization Models for Text-to-SQL.
arXiv:2502.06759.
Yao, S.; Zhao, J.; Yu, D.; Du, N.; Shafran, I.; Narasimhan,
K.; and Cao, Y. 2023. ReAct: Synergizing Reasoning and
ActinginLanguageModels. arXiv:2210.03629.
41705