Article
Design of Experiments-Based Adaptive Scheduling in
Kubernetes for Performance and Cost Optimization
YoungEonYoon,BoAhChoiandJongHyukLee*
DepartmentofAIandBigDataEngineering,DaeguCatholicUniversity,Gyeongsan-si38430,RepublicofKorea;
yeyoon0421@cu.ac.kr(Y.Y.);boahchoi@cu.ac.kr(B.C.)
* Correspondence:jonghyuk@cu.ac.kr
Abstract
InaKubernetesenvironment,theresourceallocationforPodshasadirectimpactonboth
performance and cost. When resource sizes are determined based on user experience,
under-provisioningcanleadtoperformancedegradationandexecutioninstability,while
over-provisioningcanresultinresourcewasteandincreasedcosts. Toaddresstheseissues,
thisstudyproposesanadaptiveschedulingmethodthatemploystheDesignofExperi-
ments(DoE)approachtodeterminetheoptimalresourcesizeforeachapplicationwith
minimalexperimentationandintegratestheresultsintoacustomKubernetesscheduler.
ExperimentswereconductedinaKubernetes-basedcloudenvironmentusingfiveapplica-
tionswithdiverseworkloadcharacteristics,includingCPU-intensive,memory-intensive,
andAIinferenceworkloads. Theresultsshowthattheproposedmethodimprovedthe
performancescore—calculatedastheharmonicmeanofexecutiontimeandcost—byan
averageofapproximately1.5times(rangingfrom1.15to1.59times)comparedwiththe
conventionalmaximumresourceallocationapproach. Moreover,forallapplications,the
difference in mean scores before and after optimal resource allocation was statistically
significant(p-value<0.05). Theproposedapproachdemonstratesscalabilityforachieving
both resource efficiency and service-level agreement (SLA) compliance across various
workloadenvironments.
Keywords: Kubernetes; adaptive scheduling; design of experiments (DoE); resource
AcademicEditor:JisuPark optimization; performance and cost optimization; custom scheduler; cloud computing;
Received:20August2025 workloadmanagement
Revised:12September2025
Accepted:13September2025
Published:16September2025
Citation: Yoon,Y.;Choi,B.;Lee,J. 1. Introduction
DesignofExperiments-Based
Inmoderncloudanddatacenterenvironments,virtualizationtechnologiesarewidely
AdaptiveSchedulinginKubernetes
adopted toimprovethe efficiency ofIT infrastructure utilization. However, traditional
forPerformanceandCost
Optimization.Appl.Sci.2025,15, virtualmachine(VM)–basedvirtualizationincludesanoperatingsystemineachinstance,
10098. https://doi.org/10.3390/ whichcanleadtoperformancedegradationcomparedtobare-metalsystems[1].Toaddress
app151810098 theselimitations,lightweightvirtualizationtechnologiessuchascontainershavegained
Copyright:©2025bytheauthors. attention,offeringhighportability,scalability,anddeploymentefficiency. Kubernetes[2],
LicenseeMDPI,Basel,Switzerland. thedefactocontainerorchestrationplatform,automaticallyselectstheoptimalnodeforPod
Thisarticleisanopenaccessarticle placementthroughfilteringandscoring. Inthisprocess,theresourcerequestconfiguration
distributedunderthetermsand
ofaPoddirectlyaffectsthestabilityandperformanceoftheapplication.
conditionsoftheCreativeCommons
Misconfiguredresourcerequestscancausedelaysinotherworkloadsduetoexcessive
Attribution(CCBY)license
resourceoccupationorresultinunnecessaryresourcewasteandcostincreases. Infact,
(https://creativecommons.org/
licenses/by/4.0/). recentindustryreportsindicatethatupto30%ofenterprisecloudspendingiswasteddueto
Appl.Sci.2025,15,10098 https://doi.org/10.3390/app151810098

Appl.Sci.2025,15,10098 2of16
over-provisioningandinefficientresourceutilization[3]. Despitethis,mostconfigurations
stillrelyheavilyonuserexperienceandrule-of-thumbpractices,whichlackconsistency
anddata-drivenrigor. Thesechallengesmotivatetheneedforlightweightandsystematic
methodsthatcanidentifyoptimalresourceallocationswithminimalexperimentation.
Toaddresstheseissues,priorresearchhasexploredarangeofschedulingstrategies.
Traditionalapproachesincludebatchanddynamicschedulersdesignedtobalanceresource
utilization[4,5]. Machinelearning–basedschedulersachievehighpredictiveaccuracy[6]
butrequireextensivetrainingdataandfrequentretraining,resultinginhighcomputational
overhead. Non-learning–based methods, such as adaptive, heuristic, or event-driven
schedulers,improveperformanceinlargeclusters[7–14],yettheyoftenlackstatisticalrigor.
Onlineschedulingframeworkshavealsobeenproposedtodynamicallyadapttoworkload
fluctuations[15],whileenvironment-awareschedulersaimtoimproveenergyefficiency
andsustainabilityindatacenters[16]. Morerecently,industrytoolssuchastheKubernetes
VerticalPodAutoscaler(VPA)[17]andKarpenter[18]haveautomatedresourcescaling,but
theyalsorelyonheuristicsorhistoricalmonitoringdata,whichmayintroduceinstability
underrapidlychangingworkloads.
Thesestudiesdemonstratesignificantadvancesbutalsohighlightpersistentgaps. ML-
basedschedulersarecostlytomaintain,heuristicapproachesmayyieldinconsistentresults,
andempiricalconfigurationcontinuestodominateinpractice,leadingtoinefficiency. In
contrast,theDesignofExperiments(DoE)methodologyoffersastatisticallyrigorousyet
lightweightframeworkforsystematicallyexploringresourceconfigurations. DoEhasnot
beenfullyappliedtoKubernetesscheduling,anditsabilitytoderiveapplication-specific
optimalsettingswithminimaltrialspresentsauniqueopportunitytobalanceperformance
andcostefficiency.
Inthisstudy,weproposeaDoE-basedadaptiveschedulingmethodthatdetermines
theoptimalresourceconfigurationforeachapplicationandintegratestheseresultsintoa
Kubernetescustomscheduler.ByapplyingResponseSurfaceMethodology(RSM)withCen-
tralCompositeDesign(CCD),ourapproachefficientlyestimatesbothlinearandquadratic
effects,enablingaccuratepredictionwithalimitednumberofexperiments. Thecontribu-
tionsofthisstudyareasfollows: (i)itintroducesDoEasanovelstatisticalfoundationfor
Kubernetesscheduling,providinganalternativetoempiricalandML-basedapproaches;
(ii)itdevelopsapredictivemodelforoptimalresourcesizingacrossdiverseapplication
workloads;and(iii)itdemonstratesintegrationintoaKubernetescustomscheduler,vali-
datingstatisticallysignificantimprovementsincost–performancetrade-offs.
AstructuredcomparisonofrepresentativeschedulingapproachesisprovidedinTable1.
Table1.Comparativesummaryofschedulingapproaches.
Approach KeyCharacteristics Advantages Limitations
Highaccuracyand Requireslargedatasets,
Predictsresourcedemand
Machinelearning–based adaptiveto frequentretraining,and
usingtrainedmodels
workloadchanges highoverhead
Rule-basedordynamic
Lightweightand Lackofstatisticalrigorand
Heuristic/Event-driven adjustments
fastadaptation resultsmayvary
duringexecution
Considersenergyefficiency Reducesenergycostand Maynotdirectlyoptimize
Environment-aware
andsustainability carbonfootprint applicationperformance
Statisticalexperimental Statisticallyvalidated, Currentlylimitedto
DoE-based(thisstudy) design(RSM+CCD)with minimalexperiments,and CPU/memoryand
limitedtrials systematicoptimization offlineoptimization

Appl.Sci.2025,15,10098 3of16
2. DesignofExperiments-BasedAdaptiveSchedulingMethod
2.1. OverviewoftheDesignofExperiments
TheDesignofExperiments(DoE)[19]isastatisticalmethodologydesignedtoobtain
themaximumamountofinformationfromtheminimumnumberofexperiments. Instead
ofevaluatingeverypossiblecombinationoffactors,DoEevaluatesonlyselectedexperi-
mentalpointsaccordingtothefactorlevels,therebyidentifyingtheoptimalconditions. A
conceptualdiagramisshowninFigure1.
Figure1.ConceptoftheDesignofExperiments.
Inthisstudy,DoEwasappliedtoidentifytheperformancecharacteristicsofeachap-
plicationwithminimalexperimentationandtoimplementanadaptiveschedulingmethod
thatdynamicallyadjustsresourceallocationinKubernetesenvironmentsbasedonthese
characteristics. ThegeneralDoEprocess,firstintroducedbyFisher[19]andlaterformal-
izedinmodernstatisticaltextssuchasMontgomery[20],consistsofthefollowingsteps:
(1)definingtheobjective,(2)selectingresponsevariables,(3)determiningexperimental
variables,(4)selectinganexperimentaldesignmethod,(5)conductingexperimentsand
analyzingresults,(6)buildingmodelsandverifyingfactors,and(7)standardizingresults
andidentifyingimprovements. Inourcontext,theresponsevariablewastheperformance
evaluationmetric,andtheexperimentalvariableswereCPUandmemorylevels.
Forthisstudy,ResponseSurfaceMethodology(RSM)withaCentralCompositeDe-
sign(CCD)wasadopted. RSMiswidelyusedtomodelandoptimizesystemsinfluenced
bymultiplefactors,particularlywhennon-linearrelationshipsareexpected,whileCCD
providesanefficientdesignforestimatingquadraticeffectswithrelativelyfewexperimen-
talruns. ThesefeaturesmaketheRSM–CCDcombinationwell-suitedtoourobjectiveof
derivingapplication-specificCPUandmemoryconfigurationswithminimalexperimenta-
tion. AlthoughRSMandCCDarewell-establishedtechniques,thenoveltyofthisworklies
inapplyingthemtoKubernetesschedulingforresourceoptimization—acontextthathas
notbeensystematicallyaddressedinpriorresearch.
2.2. ExperimentalDesignandEnvironmentConfiguration
Anoverviewoftheexperimentdesignedtodeveloptheoptimalresourcesizepre-
dictionmodelisshowninTable2. TheinfrastructurewasimplementedusingAmazon
WebServices(AWS)[21]ElasticComputeCloud(EC2)[22]instancesrunningtheUbuntu
24.04 operating system. For benchmarking, five applications with different workload
characteristics—selected from the Phoronix Test Suite [23]—were used, reflecting CPU-
bound,memory-bound,andAIinference–orientedworkloads. Theexperimentaldesign
andstatisticalanalysiswereconductedusingMinitab21[24]. Theexperimentalenviron-
mentandapplicationdescriptionsaresummarizedinTables3and4.

Appl.Sci.2025,15,10098
4of16
Table2.Experimentaldesign.
Category Description
Objective Determiningtheoptimalresourcesizetoensureapplicationperformance
Responsevariable Harmonicmeanofexecutiontimeandcost(Score)
Experimentalvariables CPU(2levels),andmemorysize(2levels)
Design 13randomizedexperimentsbasedonatwo-factorCentralcompositedesign
Table3.Experimentalenvironmentconfiguration.
| Category |     |                           |     | Description       |
| -------- | --- | ------------------------- | --- | ----------------- |
| Hardware |     | CPU                       |     | vCPU8cores        |
|          |     | Memory                    |     | 32GiB             |
| Software |     | OS                        |     | Ubuntu24.04       |
|          |     | Benchmarkingplatform      |     | PhoronixTestSuite |
|          |     | Statisticalanalysissystem |     | Minitab           |
Table4.ApplicationDetails.
Application Description
c-ray Measuresthetimerequiredtogenerateanimageusingraytracingwith8raysperpixel(CPU-bound).
build-apache MeasuresthetimerequiredtobuildtheApacheHTTPDwebserver(I/O-bound).
blender MeasurestherenderingtimeusingtheCyclesengineinBlender3Dgraphicssoftware(mixedCPU/GPUload).
tensorflow-lite Measuresthemodelinferencetimeinamobiledeeplearningframework(AIinference).
build-imagemagick MeasuresthetimerequiredtobuildtheImageMagickopen-sourceimageprocessingsoftware(mixedload).
Inthisstudy,atotalof13experimentsweregeneratedfromthetwo-factorCentral
CompositeDesign,consistingoffourfactorialpoints,fouraxialpoints,andfivereplicatesat
thecenterpoint. Thisconfigurationprovidessufficientinformationtoestimatebothlinear
and quadratic effects while maintaining experimental efficiency with a relatively small
numberofruns. Moreover,accordingtotheprinciplesofResponseSurfaceMethodology,
this design ensures adequate statistical power for detecting curvature and interaction
effects,therebyjustifyingthat13experimentsaresufficientforthescopeofthisstudy.
2.3. ExperimentalProcedure
Toexploretheoptimalresourcecombination,thisstudyappliedanexperimentalde-
signbasedonResponseSurfaceMethodology.Table5presentstheexperimentalfactorsand
theirrespectivelevelsforeachapplication. TheCPUandmemorylevelsweredetermined
throughpreliminarybenchmarkingtoensurethatperformancedifferencesbetweenlevels
wereclearlydistinguishable.
Table5.Factorlevelsbyapplication.
|                   | Application  |     | CPU(Core) | Memory(MiB) |
| ----------------- | ------------ | --- | --------- | ----------- |
|                   | c-ray        |     | 1,8       | 100,1000    |
|                   | build-apache |     | 1,8       | 300,1000    |
|                   | blender      |     | 1,8       | 1000,2000   |
| tensorflow-lite   |              |     | 1,8       | 500,1000    |
| build-imagemagick |              |     | 1,8       | 1200,2000   |
Sinceexecutiontimeandcosthavedifferentmeasurementunits,failingtonormalize
themmayresultinexcessiveweightingtowardonemetric,reducingthereliabilityofthe
results. Therefore,executiontimeandcostwerenormalizedseparatelytoenableaccurate

Appl.Sci.2025,15,10098
5of16
andbalancedcomparisons. Tojointlyevaluateperformanceandcostinasinglemetric,we
defineda“Score”astheharmonicmeanofthetwonormalizedvalues,ensuringabalanced
assessmentoftrade-offsbetweenexecutionefficiencyandresourceexpenditure. Inthis
study,weusedasimplifiedcostmodelbasedonlinearper-coreandper-MiBpricingto
capturetheprimaryeffectsofCPUandmemoryallocation.
Nevertheless,thisapproachhasseverallimitations. First,real-worldcloudenviron-
mentsinvolvemorecomplexcoststructures,includingspotinstancepricing,persistent
storage,andnetworkusage,whichwerenotreflectedinourmodel. Second,theevaluation
metricswererestrictedtoexecutiontimeandcost,whileotherimportantdimensionssuch
aslatency,throughput,SLAviolations,andenergyefficiencywereexcluded. Third,the
scopeofresourcefactorswaslimitedtoCPUandmemory,withoutconsideringadditional
resourcessuchasGPU,networkbandwidth,andstorageI/O.Futureworkwillextend
thecostmodel,evaluationmetrics,andresourcedimensionstoincorporatethesefactors,
therebyenhancingtherealismandapplicabilityoftheproposedmethodinproduction-scale
Kubernetesenvironments.
ThecostwascalculatedusingEquation(1),applyinganhourlyrateof0.0072USDper
CPUcoreandperGiBofmemory(basedontheAWSEC2Seoulregiont2instancepricing).
Executiontimeandcostwereeachnormalized,andasinglescorewascalculatedusingthe
harmonicmean,asinEquation(2). Theharmonicmeanhastheadvantageofbalancingthe
rateofchangeforindependentvariableswithdifferentunits. Thefinalscore,calculated
fromthenormalizedexecutiontimeTandcostC,isgivenbyEquation(3).
|     |     | (cid:18) | (cid:19) |     |
| --- | --- | -------- | -------- | --- |
Memory
|     |     | Cost= CPU+ | ×0.0072 |     |
| --- | --- | ---------- | ------- | --- |
(1)
1024
2×a×b,
|     |     | HarmonicMean | =   |     |
| --- | --- | ------------ | --- | --- |
a+b (2)
and
(cid:16) (cid:17) (cid:16) (cid:17)
2× 1 × 1
T
|     |     | Score= | C   |     |
| --- | --- | ------ | --- | --- |
(cid:16) (cid:17) (cid:16) (cid:17) (3)
1 + 1
T C
Table6showstherunorderandmeasurementvaluesforthec-rayapplicationafter
normalization,includingexecutiontimeandcostforeachCPUandmemoryconfiguration.
Table6.Normalizedc-rayexperimenttreatmentcombinationschedule.
| RunOrder | CPU(Core) | Memory(MiB) | ExecutionTime(s) | Cost(USD) |
| -------- | --------- | ----------- | ---------------- | --------- |
| 1        | 4.5       | 100         | 2.03             | 5.00      |
| 2        | 1         | 1000        | 9.92             | 2.00      |
| 3        | 8         | 550         | 1                | 9.50      |
| 4        | 8         | 100         | 1.00             | 9.00      |
| 5        | 8         | 1000        | 1.00             | 10.00     |
| 6        | 4.5       | 550         | 2.06             | 5.50      |
| 7        | 4.5       | 550         | 2.14             | 5.50      |
| 8        | 4.5       | 1000        | 2.68             | 6.00      |
| 9        | 4.5       | 550         | 2.17             | 5.50      |
| 10       | 1         | 100         | 9.87             | 1.00      |
| 11       | 4.5       | 550         | 2.02             | 5.50      |
| 12       | 1         | 550         | 10               | 1.50      |
| 13       | 4.5       | 550         | 2.03             | 5.50      |

Appl.Sci.2025,15,10098 6of16
2.4. DerivationofOptimalResourceSizebyApplication
Basedonthescoresderivedfromexecutiontimeandcost,responsesurfaceplotswere
generated,andoptimalresourcepointswereidentifiedusingaresponseoptimizationtool.
Figure2showstheresponsesurfaceplotforthec-rayapplication,whileFigure3presents
theoptimalresponsepoint. AccordingtoFigure3,theoptimalresourcesizeforc-raywas
4.68CPUcoresand100MiBofmemory,withadesirabilityvalueof0.9178.
Figure2.Responsesurfaceplotforc-ray.
Figure3.Responseoptimizationresultforc-ray.
The same method was applied to the other applications. Figures 4–7 present the
responsesurfaceplotsforeachapplication,andFigures8–11showtheircorresponding
optimalresourcepoints.
Figure4.Responsesurfaceplotforbuild-apache.

Appl.Sci.2025,15,10098 7of16
Figure5.Responsesurfaceplotforblender.
Figure6.Responsesurfaceplotfortensorflow-lite.
Figure7.Responsesurfaceplotforbuild-imagemagick.
Table 7 summarizes the optimal CPU and memory sizes derived for each applica-
tion. The results indicate that most applications achieved optimal performance at ap-
proximately 4.6 CPU cores, while the AI inference workload (tensorflow-lite) required
significantlyhigherCPUresources(7.01cores). Formemory,theoptimalsizerangedfrom
100to1200MiB, depending on the application’s characteristics. These derived optimal
resourcesizesweredirectlyappliedtotheKubernetescustomscheduler,enablingadaptive
scheduling that dynamically adjusts resource requests according to each application’s
performanceprofile. Toprovideaclearervisualization,Figure12presentsascatterplotof

Appl.Sci.2025,15,10098 8of16
theoptimalCPUandmemoryallocations,highlightingthedistinctresourcerequirements
acrossdifferentapplicationtypes.
Figure8.Responseoptimizationresultforbuild-apache.
Figure9.Responseoptimizationresultforblender.
Figure10.Responseoptimizationresultfortensorflow-lite.
Figure11.Responseoptimizationresultforbuild-imagemagick.

Appl.Sci.2025,15,10098 9of16
Table7.Optimalresourcesizeforeachapplication.
Application CPU(Core) Memory(MiB)
c-ray 4.68 100
build-apache 4.58 300
blender 4.69 1000
tensorflow-lite 7.01 636.36
build-imagemagick 4.62 1200
Figure12.ScatterplotofoptimalCPUcoresandmemorysizesforeachapplication.
Theworkload-specificresultsreflectthedistinctcomputationalcharacteristicsofeach
application. CPU-boundtaskssuchasc-rayandbuild-apacheshowedstrongsensitivityto
CPUscaling,withrelativelylowmemoryrequirements,highlightingtheirdependenceon
processorthroughput. Incontrast,blenderandbuild-imagemagickrequiredsubstantially
larger memory allocations due to their memory-intensive compilation and rendering
processes,eventhoughtheirCPUrequirementsconvergednear4.6cores. Thetensorflow-
liteworkloadexhibitedthehighestCPUdemand(7.01cores),reflectingtheparallelism
inherentinAIinferencetasks,whileitsmemoryrequirementwasmoderatecomparedtothe
otherapplications. Thesedifferencesconfirmthatworkloadtype—CPU-bound,memory-
intensive,orAIinference—directlyinfluencestheoptimalresourcebalance,underscoring
theneedforapplication-specificprofilingratherthanuniformresourceallocationpolicies.
3. PerformanceEvaluation
3.1. ComparisonofPerformanceBeforeandAfterApplyingtheOptimalResourceSize
Toverifytheeffectivenessoftheproposedadaptiveschedulingmethod,experiments
wereconductedunderthesameconditionsbycomparingthemaximumresourceallocation
method with the optimal resource size–based allocation method for each application.
Table8showsthechangesinexecutiontimeofthec-rayapplication. Whentheoptimal
resource size was applied, CPU and memory usage were reduced, resulting in longer
execution time. However, this is a natural consequence of the cost reduction achieved
throughresourcesavings.
Accordingtothenormalizedcomparisonofexecutiontime,cost,andscoreinTable9,
inthecaseofc-ray,althoughexecutiontimeincreasedto1.943,costdecreasedsignificantly
to5.201,resultinginanimprovementofthescorefrom0.182to0.280,about1.538times
higher. Thisdemonstratesthattheproposedmethodeffectivelyachievesabalancebetween
executiontimeandcost.

Appl.Sci.2025,15,10098
10of16
Table8.c-Rayexecutiontimebeforeandafteroptimalresourceallocation.
RunOrder ExecutionTimeBeforeAllocation(s) ExecutionTimeAfterAllocation(s)
|     | 1   |     | 141.745 |     |     |     |     | 245.088 |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | ------- | --- |
|     | 2   |     | 141.736 |     |     |     |     | 248.935 |     |
|     | 3   |     | 141.152 |     |     |     |     | 252.500 |     |
|     | 4   |     | 141.765 |     |     |     |     | 247.083 |     |
|     | 5   |     | 141.722 |     |     |     |     | 246.995 |     |
|     | 6   |     | 141.743 |     |     |     |     | 246.935 |     |
|     | 7   |     | 141.933 |     |     |     |     | 249.912 |     |
|     | 8   |     | 141.725 |     |     |     |     | 244.602 |     |
|     | 9   |     | 141.572 |     |     |     |     | 245.041 |     |
|     | 10  |     | 141.284 |     |     |     |     | 247.440 |     |
|     | 11  |     | 141.822 |     |     |     |     | 249.112 |     |
|     | 12  |     | 141.132 |     |     |     |     | 247.864 |     |
|     | 13  |     | 141.486 |     |     |     |     | 248.396 |     |
Table9.Normalizedperformancemetricsforc-raybeforeandafterresourceallocation.
|             |       | Resource   |     | ExecutionTime   |       |     |                 | Cost   |       |
| ----------- | ----- | ---------- | --- | --------------- | ----- | --- | --------------- | ------ | ----- |
| Application |       |            |     |                 |       |     |                 |        | Score |
|             |       | Allocation |     | (Normalization) |       |     | (Normalization) |        |       |
|             | c-ray |            | X   |                 | 1.000 |     |                 | 10.000 | 0.182 |
|             |       |            | O   |                 | 1.943 |     |                 | 5.201  | 0.280 |
The results for other applications (Table 10) also show the same trend. In partic-
ular, build-apache improved by about 1.593 times, blender by about 1.566 times, and
build-imagemagickbyabout1.549timesinperformanceefficiency. Therelativelysmaller
improvementintensorflow-liteisduetothenatureofAIinferencetasks,whereCPUpar-
allelcomputationplaysamajorrole,leavinglessroomforresourcereduction. Tofurther
highlighttheseimprovements,Figure13providesavisualcomparisonofthenormalized
performancescoresbeforeandafteroptimalresourceallocationacrossallapplications.
Table10.Normalizedperformancemetricsforeachapplicationbeforeandafterresourceallocation.
|                   |                 |     | Resource   |     | ExecutionTime   |       |     | Cost            |       |
| ----------------- | --------------- | --- | ---------- | --- | --------------- | ----- | --- | --------------- | ----- |
|                   | Application     |     |            |     |                 |       |     |                 | Score |
|                   |                 |     | Allocation |     | (Normalization) |       |     | (Normalization) |       |
|                   | build-apache    |     | X          |     |                 | 1.000 |     | 10.000          | 0.182 |
|                   |                 |     | O          |     |                 | 1.708 |     | 5.197           | 0.290 |
|                   | blender         |     | X          |     |                 | 1.000 |     | 10.000          | 0.182 |
|                   |                 |     | O          |     |                 | 1.866 |     | 5.159           | 0.285 |
|                   | tensorflow-lite |     | X          |     |                 | 1.000 |     | 10.000          | 0.182 |
|                   |                 |     | O          |     |                 | 1.138 |     | 8.383           | 0.210 |
| build-imagemagick |                 |     | X          |     |                 | 1.000 |     | 10.000          | 0.182 |
|                   |                 |     | O          |     |                 | 1.923 |     | 5.190           | 0.282 |
Whiletheseresultsdemonstratetheeffectivenessoftheproposedmethodacrossmul-
tipleapplicationtypes,theevaluationwaslimitedtoasmall-scaleAWSEC2environment
using benchmark workloads from the Phoronix Test Suite. These workloads, although
coveringCPU-bound,memory-bound,andinferencetasks,donotfullyrepresentthediver-
sityandcomplexityofproductionKubernetesclusters,wherefactorssuchasconcurrent
multi-containerservices,networklatency,nodeinterference,andstoragebottlenecksplay
critical roles. Future work will therefore validate the proposed approach in larger and
moreheterogeneousclusters,incorporatingtheseoperationalfactorstofurtherexamine
scalabilityandgeneralizability.

Appl.Sci.2025,15,10098
11of16

Figure13.Normalizedperformancescoresbeforeandafterapplyingoptimalresourceallocationfor
eachapplication.
Insummary,theDoE-basedadaptiveschedulingmethodoptimizesper-application
resourceusagebybalancingcostreductionandperformancemaintenance. Theconsistent
improvementsinscoreacrossalltestcaseshighlightitspotentialtoreduceoperational
costswhilepreservingservicequality(SLA)inreal-worldcloudenvironments.
3.2. NormalityTestofScores
Inthisstudy,apairedt-test[25]wasemployedtoverifywhetherthechangesinscores
beforeandafterapplyingtheproposedschedulingmethodwerestatisticallysignificant.
Thistestissuitableforpre-postcomparisonsofthesamegroupandrequirestheassumption
thatscoredatafollowanormaldistribution.Whenthesamplesizeislessthan30,normality
mustbeexaminedinadvance. Ifnormalityisnotsatisfied, anon-parametricWilcoxon
signed-ranktest[26]isapplied. Accordingly,thefollowinghypothesesweresetforthe
normalitytestofeachapplication:
| • Nullhypothesis(H | ): Thedatafollowanormaldistribution. |     |     |
| ------------------ | ------------------------------------ | --- | --- |
0
• Alternativehypothesis(H ): Thedatadonotfollowanormaldistribution.
1
Table11showsthescoresofthec-rayapplicationbeforeandafterresourceallocation,
aswellastheirdifferences. Sincethedifferencewascalculatedas(before–after),anegative
valueindicatesthatthescoreincreasedafterallocation.
Table11.c-Rayscoresbeforeandafteroptimalresourceallocation.
|     | ScoreBefore | ScoreAfter | DifferenceBetween |
| --- | ----------- | ---------- | ----------------- |
RunOrder
|     | Allocation | Allocation | TwoScores |
| --- | ---------- | ---------- | --------- |
| 1   | 0.182      | 0.281      | −0.099    |
| 2   | 0.182      | 0.280      | −0.098    |
| 3   | 0.182      | 0.278      | −0.096    |
| 4   | 0.182      | 0.280      | −0.098    |
−0.098
| 5   | 0.182 | 0.280 |        |
| --- | ----- | ----- | ------ |
| 6   | 0.182 | 0.280 | −0.098 |
| 7   | 0.182 | 0.279 | −0.097 |
| 8   | 0.182 | 0.281 | −0.099 |
| 9   | 0.182 | 0.280 | −0.098 |
−0.098
| 10  | 0.182 | 0.280 |        |
| --- | ----- | ----- | ------ |
| 11  | 0.182 | 0.279 | −0.097 |
| 12  | 0.182 | 0.279 | −0.097 |
−0.097894607
| 13  | 0.181818182 | 0.279712789 |     |
| --- | ----------- | ----------- | --- |
Table12presentsthenormalitytestresultsforeachapplication. Atasignificancelevel
of5%(p=0.05),ifp-value≥0.05,normalityissatisfied,andthepairedt-testwasapplied.
Otherwise,theWilcoxontestwasapplied. Theresultsshowthatallapplicationsexcept

Appl.Sci.2025,15,10098
12of16
build-apachesatisfiednormality. Sincebuild-apachehadarelativelylargeexecutiontime
variation,theskewnessofitsdatadistributionwashigh,necessitatinganon-parametrictest.
Throughtheseverificationprocedures,itwasconfirmedthattheperformanceimprovement
oftheproposedDoE-basedadaptiveschedulingmethodisalsostatisticallysignificant.
Table12.Normalitytestresultsforeachapplication.
|                   | Application     |     | p-Value | Normalized |     |
| ----------------- | --------------- | --- | ------- | ---------- | --- |
|                   | c-ray           |     | 0.618   |            | O   |
|                   | build-apache    |     | 0.001   |            | X   |
|                   | blender         |     | 0.051   |            | O   |
|                   | tensorflow-lite |     | 0.300   |            | O   |
| build-imagemagick |                 |     | 0.069   |            | O   |
3.3. StatisticalAnalysisofMeanScoreDifferences
Basedonthenormalitytestresults,eitherapairedt-testorWilcoxonsigned-ranktest
| wasappliedtoeachapplication. |     | Thehypothesesweresetasfollows: |     |     |     |
| ---------------------------- | --- | ------------------------------ | --- | --- | --- |
• Nullhypothesis(H ): Themeanscoresbeforeandafteroptimalresourceallocation
0
areequal.
•
Alternativehypothesis(H 1 ): Themeanscoresbeforeandafteroptimalresourcealloca-
tionaredifferent.
Table13showstheanalysismethodandp-valueforeachapplication. Allp-values
werebelowthesignificancelevelof0.05,leadingtotherejectionofthenullhypothesisand
theacceptanceofthealternativehypothesis. Particularlyfortheblender,thep-valuewas
aslowas3.601×10−42,indicatingthattheeffectofresourceoptimizationwasextremely
pronounced. TheseresultsdemonstratethattheproposedDoE-basedmethodfordeter-
miningoptimalresourcesizesnotonlyenhancesresourceefficiencybutalsosignificantly
improvesperformance(scores)inastatisticallymeaningfulway. Furthermore,consistent
significanceacrossfiveapplicationswithdifferentcharacteristicsconfirmsthegenerality
andpracticalapplicabilityoftheproposedmethodindiverseworkloadenvironments.
Table13.Meanscoredifferencetestresultsforeachapplication.
|     | Application | AnalysisTechniques |     |     | p-Value |
| --- | ----------- | ------------------ | --- | --- | ------- |
6.368×10−27
|     | c-ray        |                         | pairedt-test |     |       |
| --- | ------------ | ----------------------- | ------------ | --- | ----- |
|     | build-apache | Wilcoxonsigned-ranktest |              |     | 0.000 |
3.601×10−42
|     | blender         |     | pairedt-test |             |     |
| --- | --------------- | --- | ------------ | ----------- | --- |
|     | tensorflow-lite |     | pairedt-test | 3.723×10−25 |     |
2.204×10−32
| build-imagemagick |     |     | pairedt-test |     |     |
| ----------------- | --- | --- | ------------ | --- | --- |
Inaddition,unlikepriormachinelearning-basedapproachesthatoftenrequirecontin-
uousretrainingandextensivemonitoringdata,theproposedDoE-basedmethodachieves
statisticallyvalidatedoptimizationwithminimalexperimentaloverhead. Comparedto
heuristicorrule-basedschedulers,italsooffersamoresystematicandstatisticallygrounded
frameworkforderivingoptimalresourceconfigurations. Thesedistinctionsdemonstrate
that DoE can serve as a lightweight yet robust alternative for Kubernetes scheduling,
bridgingthegapbetweenempiricaltrial-and-errormethodsanddata-intensiveML-based
solutions. However, this study did not include direct experimental comparisons with
existingtoolssuchastheKubernetesVerticalPodAutoscaler(VPA),Karpenter,orAI-based
predictiveschedulers. Incorporatingsuchevaluationswillbeanimportantdirectionfor
futureworktofurthervalidatetherelativeadvantagesoftheproposedapproach.

Appl.Sci.2025,15,10098 13of16
4. ImplementationofaKubernetes-BasedCustomScheduler
Inthisstudy,theproposedDesignofExperiments(DoE)-basedpredictivemodelfor
application-specificoptimalresourcesizingwasappliedtoaKubernetescustomscheduler.
Theimplementationprocessconsistsofthefollowingsteps:
1. Developingtheschedulerprogram:
2. An example of the custom-scheduler.py function is provided in Appendix A
(FigureA1). ThiscodesnippetdemonstrateshowoptimalCPUandmemorysizes
derivedfromtheDoEmodelarereferencedthroughPodannotationstoselectasuit-
ablenode. Itfiltersthelistofnodesthatsatisfytherequiredresourcedemandand
performsnodescoringtoplacePodsonthemostsuitablenode.
3. Creatingthecontainerimage:
4. TheschedulerprogramwaspackagedintoacontainerimageusingtheDockerfile.
An example of the Dockerfile is provided in Appendix A (Figure A1). A custom
schedulerpodwasthengeneratedbasedonthisimage. Thecontainerimageincluded
Python3.8andtheKubernetesclientlibrary.
5. Assigningtheschedulerduringapplicationdeployment:
6. Inthepodconfigurationfileoftheapplication,theschedulerNamefieldwasspecified
withthenameofthecustomschedulerinsteadofthedefaultscheduler. Anexample
ofthisconfigurationisshowninAppendixA(FigureA2).
Throughthisprocess,theDoE-basedoptimalresourceinformationwasdirectlyinte-
gratedintotheKubernetesschedulingstage. Consequently,themethodachievedadaptive
resourceallocationtailoredtotheperformancecharacteristicsofeachapplicationwhile
simultaneouslyimprovingclusterresourceutilization.
Furthermore,theproposedapproachenhancespracticalapplicabilitysinceitcanbe
easilyextendedtodiverseworkloadenvironmentsbymodifyingonlyYAMLconfigurations,
withouttheneedtorebuildcontainerimages. Inpractice,theproposedscheduleroffers
severaladvantages.Itcanbeseamlesslyintegratedintoexistingclusterswithoutdisrupting
defaultschedulingmechanisms,therebysimplifyingadoptionforsystemadministrators.
By reducing unnecessary over-provisioning while preserving application performance,
itsupportsbothcostsavingsandSLAcompliance,whicharecriticalinenterprisecloud
environments. Inaddition,thelightweightstatisticalfoundationoftheDoEmodelensures
scalabilityandadaptabilitytoheterogeneousclustersandevolvingworkloaddemands,
enhancingitslong-termviabilityinproductionsettings.
As noted in Section 3.1, the current implementation was validated in a controlled
environment,andscenariossuchascompetingPods,multi-usersettings,andautoscaling
werenotincluded. Theseaspectswillbeaddressedinfutureworktofurtherdemonstrate
therobustnessofthecustomscheduler.
5. ConclusionsandFutureWork
This paper proposed a DoE-based adaptive scheduling method in Kubernetes en-
vironmentsthatdeterminestheoptimalresourcesizebyjointlyconsideringapplication
executiontimeandcost. Toovercomethelimitationsofconventionalexperience-basedre-
sourceconfiguration,aResponseSurfaceMethodologywasappliedtodesignandconduct
experimentsonfiveapplicationswithdistinctworkloadcharacteristics,therebyconstruct-
ingapredictivemodelforoptimalresourcesizing. WhenappliedtoaKubernetescustom
scheduler,theproposedmodelachievedanaveragescoreimprovementofapproximately
1.5×(rangingfrom1.15×to1.59×)comparedtotheconventionalmaximumresourceallo-
cationstrategy.Inallapplications,performanceimprovementswerefoundtobestatistically
significant,withp-values<0.05.

Appl.Sci.2025,15,10098 14of16
Whilethesefindingsdemonstratethepotentialoftheproposedapproach,theevalu-
ationwaslimitedtoasmall-scaleclusterandasetofbenchmarkapplications. Dynamic
workloadfluctuations,multi-tenantscenarios,andotherreal-worlddeploymentcomplexi-
tieswerenotfullyaddressed. Inparticular,realisticdeploymentsettingssuchascompeting
Pods, multiple users, and autoscaling mechanisms were not evaluated. Therefore, the
generalityoftheresultsshouldbeinterpretedwithcaution.
Future research will extend the model to a wider variety of workloads and large-
scale distributed cluster environments, while implementing dynamic prediction-based
schedulingthatleveragesreal-timemonitoringdata. Moreover,weplantodesignexperi-
mentsincorporatingcontrolledlevelsofnetworklatency,nodeinterference,andconcurrent
workloads, using metrics such as latency, throughput, and SLA violations to quantify
performance. Standardmonitoringandbenchmarkingtools(e.g.,Prometheus,cAdvisor,
andKubernetes-nativeautoscalingmodules)willbeusedtovalidatethesescenarios. Fur-
thermore,theproposedmethodwillbeintegratedwithAI-basedresourcemanagement
frameworks,withtheultimategoalofdevelopinganadvancedschedulerthatsimultane-
ouslyensuresresourceefficiencyandservicequalityincloudandbigdataenvironments.
ItisalsoworthnotingthattheDoEmethodologyitselfisinherentlyextensible: additional
resourcefactorssuchasGPU,networkbandwidth,andstorageI/O,aswellasevaluation
metrics like energy efficiency and SLA compliance, can be systematically incorporated
intotheexperimentaldesign. Thisflexibilityunderscoresthebroaderapplicabilityofour
approachbeyondtheCPUandmemorydimensionsexaminedinthisstudy.
Author Contributions: Conceptualization, Y.Y., B.C. and J.L.; methodology, Y.Y., B.C. and J.L.;
software,Y.Y.andB.C.;validation,Y.Y.andB.C.;formalanalysis,Y.Y.andB.C.;investigation,Y.Y.
andB.C.;resources,Y.Y.andB.C.;datacuration,Y.Y.andB.C.;writing—originaldraftpreparation,
Y.Y.;writing—reviewandediting,Y.Y.andJ.L.;visualization,Y.Y.andJ.L.;supervision,J.L.;project
administration, J.L.; fundingacquisition, J.L.Allauthorshavereadandagreedtothepublished
versionofthemanuscript.
Funding:ThisworkwassupportedbyresearchgrantsfromDaeguCatholicUniversityin2023.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Notapplicable.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
AppendixA
FigureA1showsasimplifiedfunctionselect_node_for_pod(pod)fromthecustom-
scheduler.pyscript,whichillustrateshowoptimalCPUandmemorysizesderivedfrom
theDoEmodelareusedduringnodeselection.
FigureA1.Examplefunctionselect_node_for_pod(pod)incustom-scheduler.py.

Appl.Sci.2025,15,10098 15of16
FigureA2presentsanexampleDockerfileforbuildingthecustomschedulercontainer
image,includingthePythonruntimeandtheKubernetesclientlibrary.
FigureA2.ExampleDockerfileforbuildingthecustomschedulercontainerimage.
FigureA3providesanexamplePodconfigurationYAMLfile,wherethescheduler-
NamefieldissettothecustomschedulerinsteadofthedefaultKubernetesscheduler.
FigureA3.ExamplePodconfigurationYAMLfilespecifyingthecustomscheduler.
References
1. Rejiba,Z.;Chamanara,J.CustomSchedulinginKubernetes:ASurveyonCommonProblemsandSolutionApproaches.ACM
Comput.Surv.2022,55,1–37.[CrossRef]
2. Kubernetes.Availableonline:https://kubernetes.io/(accessedon30July2025).
3. Boston Consulting Group. Cloud Cover: Price Swings, Sovereignty Demands, and Wasted Resources. Available online:
https://www.bcg.com/publications/2025/cloud-cover-price-sovereignty-demands-waste(accessedon6September2025).
4. Wang,Z.;Liu,H.;Han,L.;Huang,L.;Wang,K.ResearchandImplementationofSchedulingStrategyinKubernetesforComputer
ScienceLaboratoryinUniversities.Information2021,12,16.[CrossRef]
5. Li,D.;Wei,Y.;Zeng,B.ADynamicI/OSensingSchedulingSchemeinKubernetes. InProceedingsofthe4thInternational
ConferenceonHighPerformanceCompilation,ComputingandCommunications(HP3C),Guangzhou,China,20–22June2020;
pp.14–19.[CrossRef]
6. Dakic´,V.; Ðambic´,G.; Slovinac,J.; Redžepagic´,J.OptimizingKubernetesSchedulingforWebApplicationsUsingMachine
Learning.Electronics2025,14,863.[CrossRef]
7. Luo,J.;Zhao,X.;Ma,Y.;Pang,S.;Yin,J.MerKury:AdaptiveResourceAllocationtoEnhancetheKubernetesPerformancefor
Large-ScaleClusters. InProceedingsoftheACMWebConference2025(WWW’25),Sydney,Australia,28April–2May2025;
pp.4937–4948.[CrossRef]
8. Kim,T.Y.; Lee,J.R.; Kim,T.H.; Chun,I.G.; Park,J.; Jin,S.KubernetesSchedulerFrameworkImplementationwithRealtime
ResourceMonitoring.IEMEKJ.Embed.Syst.Appl.2020,15,129–137.[CrossRef]
9. Fu,Y.;Zhang,S.;Terrero,J.;Mao,Y.;Liu,G.;Li,S.;Tao,D.Progress-BasedContainerSchedulingforShort-LivedApplicationsina
KubernetesCluster.InProceedingsoftheIEEEInternationalConferenceonBigData(BigData2019),LosAngeles,CA,USA,
9–12December2019;pp.278–287.[CrossRef]
10. Menouer,T.KCSS:KubernetesContainerSchedulingStrategy.J.Supercomput.2021,77,4267–4293.[CrossRef]
11. Song,S.;Deng,L.;Gong,J.;Luo,H.GaiaScheduler:AKubernetes-BasedSchedulerFramework.InProceedingsofthe2018IEEE
ISPA/IUCC/BDCloud/SocialCom/SustainCom,Melbourne,Australia,11–13December2018;pp.252–259.[CrossRef]

Appl.Sci.2025,15,10098 16of16
12. Medel, V.; Rana, O.; Banares, J.A.; Arronategui, U.AdaptiveApplicationSchedulingunderInterferenceinKubernetes. In
ProceedingsoftheIEEE/ACM9thInternationalConferenceonUtilityandCloudComputing(UCC),Shanghai,China,6–9
December2016;pp.426–427.[CrossRef]
13. Cho,E.J.;Kim,Y.H.DesignofSchedulingArchitectureforPolicy-DrivenEventManagementinKubernetes.InProceedingsofthe
2021KICSFallConference,Jeju,RepublicofKorea,24–26November2021;pp.927–928.
14. ElHajAhmed,G.;Gil-Castineira,F.;Costa-Montenegro,E.KubCG:ADynamicKubernetesSchedulerforHeterogeneousClusters.
Softw.Pract.Exp.2021,51,213–234.[CrossRef]
15. Duque,R.;Arbelaez,A.;Díaz,J.F.OnlineoverTimeProcessingofCombinatorialProblems.Constraints2018,23,310–334.[CrossRef]
16. Townend,P.;Clement,S.;Burdett,D.;Yarg,R.;Shaw,J.;Slater,B.;Xu,J.ImprovingDataCenterEfficiencythroughHolistic
SchedulinginKubernetes.InProceedingsoftheIEEEInternationalConferenceonService-OrientedSystemEngineering(SOSE),
SanFrancisco,CA,USA,4–9April2019;pp.156–166.[CrossRef]
17. Kubernetes.VerticalPodAutoscaler(VPA).Availableonline:https://github.com/kubernetes/autoscaler/tree/master/vertical-
pod-autoscaler(accessedon5September2025).
18. AWS.Karpenter:AKubernetesNodeAutoscaler.Availableonline:https://karpenter.sh/(accessedon5September2025).
19. Fisher,R.A.TheDesignofExperiments.Br.Med.J.1936,1,554.[CrossRef]
20. Montgomery,D.C.DesignandAnalysisofExperiments,9thed.;Wiley:Hoboken,NJ,USA,2017.
21. AmazonWebServices.Availableonline:https://aws.amazon.com/(accessedon30July2025).
22. AmazonEC2.Availableonline:https://aws.amazon.com/ec2/(accessedon30July2025).
23. PhoronixTestSuite.Availableonline:https://phoronix-test-suite.com/(accessedon30July2025).
24. Minitab.Availableonline:https://minitab.co.kr/(accessedon30July2025).
25. Hsu,H.;Lachenbruch,P.A.PairedtTest.InWileyStatsRef:StatisticsReferenceOnline;Wiley:Hoboken,NJ,USA,2014.[CrossRef]
26. Woolson,R.F.WilcoxonSigned-RankTest.InWileyEncyclopediaofClinicalTrials;Wiley:Hoboken,NJ,USA,2008;pp.1–3.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.