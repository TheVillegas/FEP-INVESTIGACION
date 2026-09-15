Article
FinOps-Aware Budget-Constrained Optimization for Cloud
Resource Management
Choong-HeeCho
DivisionofComputerScienceandEngineering,SahmyookUniversity,Hwarangro815,
Seoul01795,RepublicofKorea;cch@syu.ac.kr
Abstract
WiththeriseofFinancialOperations(FinOps),cloudresourcemanagementrequiresthe
enforcement of strict budgetary guardrails rather than soft cost objectives. However,
discrete Virtual Machine (VM) types often cause structural infeasibility, which existing
methodsfailtoaddress.WeformulatetheBudget-ConstrainedVMResizingproblemunder
temporalhardconstraintsandestablishtheNP-hardnessofthescalarizedproblemasa
completenessresult. Tosolvethis,weproposetheBudget-awareDual(BD)solver,which
utilizesadualvariableasashadowpricetodynamicallysteercandidatedecisionstoward
budget feasibility without opaque penalty tuning. Extensive experiments demonstrate
thatBDsignificantlyimprovesbudgetfeasibilityandoperationalstabilitycomparedto
thebaselines. Intherun-ratesetting,BDreducescandidatebudgetviolationstozeroonce
thebudgetentersfeasibleregimesatα≥0.6andsubstantiallyreducesoperationalchurn,
decreasingthechangeratefrom53.95%to7.80%inanoscillatoryworkloadscenario. BD
alsoexhibitsnear-linearscalabilityandremainsmorethan100×fasterthanNSGA-IIat
largefleetsizes. Thisframeworkprovidesatheoreticallygroundedandscalableapproach
forbalancingeconomicefficiency,operationalstability,andstrictbudgetcompliance.
Keywords: FinOps;cloudresourcemanagement;budget-constrainedoptimization;cloud
cost management; hard budget constraints; dual-based optimization; multi-objective
optimization;cloudcomputing
1. Introduction
Operatingmoderncloudservicesrequiresthesolutionofabroadsetofoptimization
problems across multiple layers of the stack [1]. At the infrastructure layer, operators
must provide and place resources, decide how to pack workloads onto instances, and
reacttochangingdemandthroughschedulingandscaling. AttheapplicationandSite
ReliabilityEngineering(SRE)layers,theymustmaintainreliabilitytargetswhilenavigating
AcademicEditor:GeorgeDrosatos transientloadspikes,taillatency,andfailures. Atthebusinessandoperationslayers,they
mustcontrolspending,managecapacitycommitments,andenforceorganizationalpolicies.
Received:24February2026
Revised:11March2026 Theseconcernsaretightlycoupled: achangethatimprovescostefficiencycandegrade
Accepted:27March2026 reliability,andanactionthatimprovesperformancecantriggersustainedspendincreases.
Published:29March2026 Asaresult,manycloud-operationaltasksarenaturallyframedasonline,multi-objective
Copyright:©2026bytheauthor. decision-makingproblemsunderuncertainty.
LicenseeMDPI,Basel,Switzerland.
Withinthislandscape,VirtualMachine(VM)resizingisafundamentaloperational
Thisarticleisanopenaccessarticle
mechanism[2]. CloudprovidersofferarichmenuofVMspecifications, andoperators
distributedunderthetermsand
canadjustVMtypesasworkloadsevolvetoreducewastewhilemaintainingsufficient
conditionsoftheCreativeCommons
Attribution(CCBY)license. headroomfortaildemand. Inlarge-scaleVMfleets,however,resizingcannotbetreated
Appl.Sci.2026,16,3302 https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 2of48
as a purely cost-minimization task. Changing VM specifications can incur migration
orrestartoverheadsandmaydegradeoperationalstabilitywhenperformedfrequently.
Consequently,practicalresizingpoliciesmustbalanceeconomicefficiency,tail-safety(e.g.,
overloadrisk),andoperationalstabilityunderuncertainty,andtheymustdosoinanonline
settingwheredecisionsaremadewindowbywindow.
WiththegrowingadoptionofFinancialOperations(FinOps)practices,budgetsarein-
creasinglytreatedasoperationalguardrailsratherthanretrospectiveaccountingtargets[3].
Importantly, budgets in practice are often specified over time and appear in multiple,
structurallydifferentforms. Examplesincludearun-ratemodelthatlimitsspendingper
decisionwindow,anabsolutecumulativemodelthatcapstotalspendingoverahorizon,
anincrementalcumulativemodelthatlimitscumulativegrowth-drivenexpansions(e.g.,
scale-up cost increments), and a rolling model that constrains spending over a sliding
window[4]. Undersuchtemporalhard-budgetpolicies,aresizingpolicymustproduce
actions that are consistent with an explicit feasibility notion aligned with deployment:
feasibledecisionsarenotmerelythosethatreduceviolationsonaverage,butthosethat
remainfeasible(orminimizeunavoidableinfeasibility)undertheactivebudgetpolicy.
TheserequirementsbecomemorechallengingwhencombinedwithadiscreteVM-
type pool [5]. Under tight budgets or abrupt workload shifts, there can exist decision
windowsinwhichnoassignmentfromthediscretepoolsatisfiestheactivebudget. We
refer to this regime as structural infeasibility. Operationally, a window is structurally
infeasible if even the lowest-cost assignment in the discrete VM-type pool violates the
activebudgetconstraint(i.e.,thebudgetcannotbesatisfiedevenafterreducingallVMs
to the cheapest available type). In this case, the objective cannot be to guarantee zero
violations,becausezeroviolationsmaybeimpossible;instead,thepolicyshouldminimize
unavoidable violations while maintaining an acceptable sizing quality–stability trade-
off. Moreover, real controllers do not execute a candidate decision directly. Candidate
assignmentsmustpassasharedcompliancegatethatcheckstheactivetemporalbudget
policy and produces a post-gate decision that can actually be deployed. If evaluation
mixescandidate-leveloutcomeswithpost-processingoutcomes,reportedmetricssuchas
costsavingandviolationratebecomeambiguousandcomparisonsacrossmethodscan
beunfair.
PriorworkoncloudresourcemanagementandVMresizinghasexploredabroad
spectrum of approaches, ranging from heuristics and metaheuristics to reinforcement-
learning-basedpolicies[2,6,7]. However,whenbudgetsaretreatedasfirst-classtemporal
hardconstraints,severallimitationsremain. Existingmethodsoftenincorporatebudgets
indirectlythroughtuning-sensitivepenaltyterms,assumeasinglecanonicalbudgetform,
orfailtoclearlydistinguishstructurallyinfeasibleregimesfromalgorithm-dependentbe-
haviorunderdiscreteVMtypes. Moreover,method-specificpost-processingorrepairrules
canaltertheeffectiveevaluationtarget,complicatingfaircomparisonsacrossbaselines.
Inthispaper,weaddressthesegapsbyformulatingVMresizingasanonlinemulti-
objectiveoptimizationproblemundertemporalhard-budgetconstraints,wheretheobjec-
tivescaptureasizingquality–stabilitytrade-off. Sizingqualityreflectsbothwasteandtail-
safetythroughoverload-relatedterms,whilestabilitycapturesresizing-inducedchanges.
Westudymultipletemporalbudgetpolicies—run-rate,absolutecumulative,incremental
cumulative,androlling—andanalyzehowtheirstructuraldifferencesinducedistinctfeasi-
bilitydynamicsandtrade-offs. Toreflectoperationaldeploymentandeliminateambiguity,
weapplyasharedcompliancegatetothecandidatedecisionproducedbyeverymethod
andcomputeallreportedmetricsfromtheresultingpost-gatedecisions. Unlessstatedoth-
erwise,costandstabilitymetricsarecomputedfrompost-gatedecisions;weadditionally
reportcandidate(pre-gate)feasibilitydiagnosticstoassessbudgetinternalization.
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 3of48
Ontopofthisframework,weproposeaBudget-awareDual(BD)solver. BDdoesnot
relyonadhocpenaltytuningtomitigatebudgetviolations. Instead,itintroducesadual
variableνthatrepresentsbudgetpressureasashadowprice. Whenthebudgetistight,ν
increasesandshiftsdecisionstowardfeasibility;whenthebudgetisrelaxed,νdecreases
andtheconstraintbecomesinactive. Weprovidetheoreticalintuitionforthemonotone
behaviorofνwithrespecttothebudgetlevelandvalidatethisbehaviorempiricallyacross
structurallydifferenttemporalbudgetformulations. Thisdual-variableperspectivemakes
BDbotheffectiveandinterpretable: itsbehaviorcanbeunderstoodthroughthelensof
budgetpressureratherthanopaqueheuristicrules.
Toclarifythefocusofourstudy,weinvestigatethreecloselyrelatedquestions. First,
weexaminehowdifferenttemporalhard-budgetsemantics—suchasrun-rate,absolute
cumulative,incremental,androllingbudgets—affectfeasibilitydynamicsandthetrade-off
betweensizingqualityandoperationalstabilitywhentheVM-typepoolisdiscreteand
structuralinfeasibilitymayarise. Second,weinvestigatewhetheraresizingpolicyguided
byasingleinterpretabledualsignal,denotedbyνandinterpretedasashadowpriceof
budgetpressure,caneffectivelyinternalizehardbudgetconstraintswhilesimultaneously
suppressingexcessiveoperationalchurn. Third,weanalyzehowevaluationmethodology
influencesconclusionsaboutbudgetfeasibilityandeconomicperformance. Inparticular,
weexaminewhethermixingcandidatedecisionswithrepairedpost-processingoutcomes
obscuresalgorithmicbehavior,andhowapplyingacommoncompliancegateacrossall
methodsaffectscomparabilityandtheinterpretationofunavoidableviolationscausedby
structuralinfeasibility. Together,thesequestionsguidetheformulationoftheoptimization
framework, the design of the BD solver, and the experimental evaluation presented in
thispaper.
Toaddressthesequestions,thisworkmakesthefollowingcontributions:
• WedefineanoperationallygroundedproblemsettingforonlineVMresizingunder
temporalhardbudgetswithadiscreteVM-typepool,explicitlymodelingstructural
infeasibility. We also establish NP-hardness of the resulting scalarized problem to
placeBC-VMRwithintheknowncombinatorialcomplexitylandscape.
• Weunifyfourtemporalbudgetmodels—per-windowrun-rate,absolutecumulative,
rolling, and incremental cumulative—within a single framework, and empirically
evaluatetheproposedsolveronthreerepresentativefamilies: theper-windowrun-
ratebudget,theabsolutecumulativebudget,andtheincrementalcumulativebudget.
Thesethreefamiliesareselectedbecausetheyprovidetheclearestcontrastsamonglo-
calspendingcaps,horizon-levelcumulativecontrol,andgrowth-constrainedupsizing,
whiletherolling-budgetvariantisusedonlyasasupplementarydiagnostic.
• We propose the Budget-aware Dual (BD) solver, which integrates temporal hard-
budget constraints through an interpretable dual variable ν rather than tuning-
dependentpenaltiesorbespokerepairrules. WefurtherformalizeBDasanonline
projecteddual-ascentmethodbasedonLagrangianrelaxation. Fortherun-ratebudget
case,whichisstage-wiseseparable,weestablishstandardregretandviolationbounds
underacontinuousrelaxationandempiricallyquantifytherelaxation-to-integergap
usingaprimal–duallowerbound.
• We conduct comprehensive simulator-based experiments using a behavior-driven
syntheticworkloadgeneratorandrepresentativebaselines(Static,Greedy,PRG,and
NSGA-II),reportingoperationallymeaningfulmetricssuchascostsaving,post-gate
budgetviolationrate,andchangerate,withauxiliaryanalysesofoverloadriskand
operationalchurnwhereappropriate.
Theremainderofthispaperisorganizedasfollows. Section2reviewsrelatedwork.
Section3definestheproblemsetting,objectives,andtemporalhard-budgetconstraints.
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 4of48
Section 4 discusses computational aspects of the formulation. Section 5 presents the
BDsolver anditstheoreticalproperties. Section 6presents anddiscussesexperimental
results,highlightingdual-variablebehaviorvalidation,comparisonsacrossbudgetmodels,
and performance under diverse workload regimes. Section 7 concludes and outlines
futuredirections.
2. RelatedWork
2.1. ComputationalHardnessofCloudOptimization
Cloud computing provides cost efficiency and elasticity; however, resource manage-
mentatthedatacenterscale—includingVMplacement,allocation,resizing,scheduling,load
balancing,consolidation,andSLA/QoSenforcement—fundamentallyreducestocombina-
torialoptimizationproblems,manyofwhichhavebeenrepeatedlyshowntobeNP-hardor
NP-complete[6,8–10].VMplacementandallocationnaturallyreducetovariantsoftheBin
PackingProblem,inheritingitscomputationalintractabilitywhenminimizingthenumberof
activeserversforenergyorcostefficiency[5,11,12]. Inheterogeneousenvironments,these
problemsfurtherreducetotheGeneralizedAssignmentProblemorknapsack-typeformu-
lationswithbinaryselectionconstraints,reinforcingNP-hardness[13–15]. VMresizingor
right-sizingsimilarlyinvolvesselectingoneconfigurationfromafiniteVMtypesetunder
multi-dimensionalresourceconstraintsandiscommonlymodeledasamulti-dimensionalor
multiple-choiceknapsackproblem[16,17].Taskscheduling,loadbalancing,andenergy-aware
consolidationinheritthehardnessofclassicalscheduling,binpacking,andsetcoverformula-
tions,particularlywhenextendedtomulti-resourceandenergy-cost-awaresettings[18–20].
ProvisioningunderSLA/QoSconstraintsfurtherconnectstoNP-hardcombinatorialauction
orsocialwelfaremaximizationproblemsduetotheneedtoselectfeasiblecombinationsthat
jointlysatisfyperformanceconstraints[21–23].Collectively,theseresultsestablishcloudopti-
mizationasaclassofproblemswhosecomputationalintractabilityistheoreticallyguaranteed,
renderingexactsolutionsimpracticalatscaleandmotivatingthewidespreadrelianceonap-
proximation,heuristic,metaheuristic,andlearning-basedmethodsforobtaininghigh-quality
feasiblesolutions[24–27].
2.2. Cost-AwareCloudOptimization
Incloudcomputingenvironments,resourcemanagementenablesdynamicscalability
by elastically provisioning resources in response to workload variations. Despite this
flexibility, accuratelypredictingandoptimizingresourceusageremainsafundamental
challenge due to workload uncertainty and system heterogeneity [28]. Given the NP-
hardness reviewed in Section 2.1, cost has long been incorporated into cloud resource
managementobjectivestoreflecttheeconomicnatureofcloudservices[10].
However,aconsistentcharacteristicacrosscost-awarecloudoptimizationresearch
is that cost is commonly treated as a soft objective rather than as a strict feasibility
constraint[1,2,29,30]. Inmanyformulations,costappearsasonecomponentofamulti-
objective function alongside performance or QoS metrics, allowing trade-offs through
weighted combinations rather than enforcing explicit budget limits. This modeling ap-
proachimplicitlyassumesthatcostcanberelaxedinfavorofperformancegains,which
limitsitsapplicabilityinfinanciallyconstrainedoperationalsettings.
Arepresentativeexampleofthisparadigmisthewidelyadoptedcost–performance
trade-offmodel,oftenexpressedintheformcost+αperformance. Suchformulationshave
beenextensivelyappliedtoVMprovisioning,taskscheduling,andworkflowoptimization,
wheretheweightingparameterαcontrolstherelativeimportanceofmonetarycostversus
performanceobjectives[31,32]. WhilethisapproachiseffectiveinexploringPareto-efficient
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 5of48
trade-offsforNP-hardproblems,itreliesonheuristicweightselectionandprovidesno
guaranteethattheresultingsolutionsrespectpredefinedbudgetboundaries.
Cost-awareconsiderationsarealsocentraltoenergy-awareVMconsolidation,where
reducing the number of active physical servers lowers energy consumption and opera-
tionalexpenses[33]. Intheseapproaches, costistypicallyderivedfromenergymodels
andincorporatedintotheoptimizationobjectivetogetherwithperformanceorstability
metrics. Nevertheless, even in this context, cost remains a secondary optimization tar-
getratherthanahardconstraint,andbudgetviolationsmaystilloccurunderdynamic
workloadconditions.
Thisrelianceonsoftcostobjectivesexposesimportantlimitationsinpracticalcloud
operations. Without explicit budget enforcement, optimization outcomes may exceed
allowable spending, particularly in the presence of highly dynamic and unpredictable
workloads[7,34]. FromaFinOpsperspective[3],whichemphasizescostaccountabilityand
continuouscostgovernanceacrossengineering,finance,andbusinessfunctions,existing
cost-awarecloudoptimizationframeworksremaininsufficientwhenbudgetcompliance
must be enforced. These limitations motivate optimization models that treat budget
constraintsasfirst-class,enforceableconditionsratherthanadjustableobjectives.
2.3. ConstraintModelinginCost-AwareCloudOptimization
Asmallerbodyofworkmodelscostasanexplicitfeasibilityconstraintratherthan
as a soft objective. In early cost-aware formulations, multi-objective goals were com-
monlyscalarizedintoweightedsingle-objectivefunctions,whichdonotguaranteebudget
compliancewhenperformanceoravailabilityobjectivesdominate[35,36].
To address this limitation, subsequent studies introduced single hard budget con-
straintsthatexplicitlyboundtotalcostoverafixedoptimizationhorizon,therebyenforcing
costfeasibilityasastrictconstraintratherthanatunableobjective[36]. Whilesuchmodels
improve budget compliance compared to soft-objective approaches, they are typically
definedoverastatichorizonandfailtocapturetemporalspendingdynamicsarisingfrom
time-varyingworkloads,fluctuatingdemand,andcomplexpricingschemes. Consequently,
fixedbudgetconstraintsmayeitherbeoverlyconservativeorinsufficienttoregulateshort-
term spending spikes, motivating the development of time-indexed and history-aware
budgetconstraintmodels.
2.4. TemporalBudgetConstraints
Somestudiesfurtherconsidertime-dependenthardfeasibilityconstraintsthatimpose
feasibilityrequirementsatmultipletimepoints.Examplesincludeper-windowrun-ratelimits,
cumulativebudgettrajectories,incrementallimitsandrolling-horizonconstraints,andrelated
onlinefeasibilitysettings,whichmorecloselyreflectreal-worldFinOpspractices[37–40].
Arelatedlineofresearchexaminesfeasibility-drivenonlinecombinatorialscheduling
underwaiting-timeconstraints. Duqueetal.[37]studyonlineover-timeprocessing,where
tasksarrivedynamically,processingtimesareunknown,andtheobjectiveistomaximize
thenumberofsolvedinstancesunderwaiting-timelimits. Althoughthatsettingdiffers
fromcloudVMresizingundertemporalbudgets,itisrelevantherebecauseitshowshow
hardfeasibilityrequirementscanfundamentallyreshapeonlineoptimizationobjectives.
Oursettingdiffersinthecontrolvariable(VM-typeassignmentratherthanjobsequencing),
thefeasibilitysemantics(temporalbudgetconstraintsratherthanwaiting-timeconstraints),
andthedeploymentlayer(candidateresizingdecisionssubsequentlyfilteredthrougha
compliancegate). Introducingtime-dependentbudgetconstraintschangesthestructure
ofcloudresourceoptimizationintwodistinctways. First,somepoliciesaretime-indexed
yetstage-wiseseparable,suchasper-windowrun-ratecaps,wherefeasibilityischecked
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302
6of48
independentlyineachwindowanddoesnotdependonpastspending. Second,temporally
coupledpolicies—includingcumulativebudgets,rolling-horizoncaps,andincremental
limits—makefeasibilityattimetdependontherealizedcosthistory.
Thiscouplingbreaks
thestage-wiseseparabilityexploitedbymanycost-awareheuristicsandcanrenderlocally
optimaldecisionsinfeasibleforfuturewindowsunderhistory-dependentpolicies.
Many budget-aware approaches address this complexity by focusing on a single
budgetmodelatatime[39,40]. InVMprovisioningandresizing,representativemethods
enforce feasibility using heuristic or rule-based mechanisms tied to a specific budget
interpretation [38,41]. Similarly, workflow scheduling studies typically handle a single
globalbudgetbyheuristicallydecomposingitintoper-taskorper-stagesub-budgets[39,42].
AlthoughNP-hardnessisoftenacknowledged,formalanalysisisinmanycasesconfined
tosimplifiedsingle-budgetsettings[38,39,41,42].
More recent work on cost-aware scheduling has introduced formal optimization
modelsandNP-hardnessresults[43]. However,inmanyformulations,costismodeledas
asingle-dimensionalobjectiveorconstraint,withoutexplicitsupportforheterogeneous
ortime-varyingbudgetpolicies[38,39,41–43]. Inpractice,diversebudgetcontrols—such
ascustombudgetperiodsorspendingalerts—arecommonlyenforcedthroughexternal
governancemechanismsratherthanintegratedintotheoptimizationlogic[4,44].
However,existingbudget-awareformulationsareoftentiedtoaspecificbudgeting
policy,makingitdifficulttoreuseobjectivesandsolversacrossdifferenttemporalbudget
models. More broadly, prior work varies along several axes that are critical in FinOps-
drivenoperations: whetherbudgetsareenforcedashardfeasibilityconstraintsoronly
assoftobjectives; whattemporalsemanticsthebudgetexpresses(run-rate,cumulative,
rolling,incremental);howinfeasibilityishandled;whetheradiscreteVM-typepoolinduces
structurallyinfeasiblewindows;whetheroperationalstabilityismodeled;andwhether
evaluation distinguishes candidate decisions from deployable actions. To make these
distinctionsexplicitandtopositionourcontribution,weprovideastructuredcomparison
inTable1. TheconcretebudgetmodelsusedinthispaperareformalizedinSection3.7,
andthecorrespondingbudget-constrainedresizingproblemandsolverarepresentedin
Sections3–5(withthealgorithmdetailedinSection5).
Table1.Structuredcomparisonofrepresentativebudget-awareoptimizationapproachesbybudget
semantics,feasibility/repairhandling,stabilitymodeling,evaluationprotocol,andinterpretability.
|      | Budget | Feasibility |           | Evaluation |                  |
| ---- | ------ | ----------- | --------- | ---------- | ---------------- |
| Work |        |             | Stability |            | Interpretability |
|      | Model  | Handling    |           | Protocol   |                  |
Low
| Thanasiasetal. | Budget              | Online    |     |                |             |
| -------------- | ------------------- | --------- | --- | -------------- | ----------- |
|                |                     |           | No  | Candidate-only | (rule-based |
| (2016)[38]     | +deadlineconstraint | Heuristic |     |                |             |
heuristics)
Low
| Rizvi&Ramesh | Single-horizon   | Heuristic     |     |                |           |
| ------------ | ---------------- | ------------- | --- | -------------- | --------- |
|              |                  |               | No  | Candidate-only | (workflow |
| (2020)[39]   | budgetconstraint | decomposition |     |                |           |
heuristics)
Low
| Rajasekar&Santhiya | Budget-constrained | Heuristic  |     |                |            |
| ------------------ | ------------------ | ---------- | --- | -------------- | ---------- |
|                    |                    |            | No  | Candidate-only | (heuristic |
| (2024)[40]         | scheduling         | scheduling |     |                |            |
schedulingrules)
Moderate
| Radhika&Sadasivam | Budget-aware | Decision |     |                |                  |
| ----------------- | ------------ | -------- | --- | -------------- | ---------------- |
|                   |              |          | No  | Candidate-only | (decisionscoring |
| (2021)[41]        | objective    | model    |     |                |                  |
model)
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302
7of48
Table1.Cont.
|            |            | Budget       | Feasibility |           | Evaluation     |                  |
| ---------- | ---------- | ------------ | ----------- | --------- | -------------- | ---------------- |
|            | Work       |              |             | Stability |                | Interpretability |
|            |            | Model        | Handling    |           | Protocol       |                  |
|            |            |              |             |           | Candidate-only | Moderate         |
|            |            | Waiting-time | Online      |           | (online        | (algorithmic     |
| Duqueetal. | (2018)[37] |              |             | Implicit  |                |                  |
|            |            | constraint   | scheduling  |           | scheduling     | scheduling       |
|            |            |              |             |           | decisions)     | model)           |
Temporalhard
High
|          |     | budgets(run-rate, | Dual-based |          | Candidate+ |                |
| -------- | --- | ----------------- | ---------- | -------- | ---------- | -------------- |
| Thiswork |     |                   |            | Explicit |            | (interpretable |
|          |     | cumulative,       | control    |          | post-gate  |                |
dualvariableν)
rolling,incremental)
2.5. ComparativePositioningandNovelty
Table1highlightsthatmostexistingapproachestreatbudgetseitherassoftobjectives
orassingle-horizonconstraintsandtypicallyevaluatecandidatedecisionswithoutdistin-
guishingdeployableactions. Incontrast,BC-VMRexplicitlymodelsstructuralinfeasibility
inducedbydiscreteVM-typepoolsandevaluatesallmethodsunderacommoncompliance
gatealignedwithdeployment.
Importantly,thecontributionofthisworkdoesnotlieinintroducinganewhardness
archetypeitself,sincebudget-constrainedresourceallocationnaturallyexhibitsknapsack-
likecombinatorialstructure. Instead,thenoveltyarisesfromthewayseveraloperational
aspectsareaddressedtogetherwithinasingleformulation. Inparticular,thisworksimulta-
neouslyconsidersmultipletemporalhard-budgetsemantics,explicitlymodelsstructural
infeasibilitycausedbydiscreteVM-typepools,andevaluatesresizingdecisionsthrough
adeployment-alignedcompliancegatethatseparatescandidateanddeployableactions.
Tothebestofourknowledge,priorbudget-awarecloudoptimizationstudiesdonotinte-
gratetheseoperationalconsiderationswithinaunifiedonlineVMresizingframeworkand
evaluationprotocol.
3. ProblemFormulation
3.1. OverviewandNotation
We consider a cloud platform that manages a fleet of N virtual machines (VMs).
Time is discretized into T decision windows indexed by t ∈ {1,...,T}, each of fixed
durationhhours. Forexample,a5-minwindowcorrespondstoh = 1 . VMsareindexed
12
by i ∈ {1,...,N}. At the beginning of each window t, the platform selects a VM type
(instancespecification)foreachVMandkeepstheselectedtypeunchangedthroughoutthe
window. Weconsidertworesourcedimensions,CPUandmemory. LetR {cpu, mem}
andindexresourcesbyr ∈ R. Forreadability,Table2summarizesthemainnotationused
ℛ ≔
throughoutthepaper.
Table2.SummaryofkeynotationusedintheBC-VMRformulation.
|     |     | Symbol                                                      |     | Meaning |     |     |
| --- | --- | ----------------------------------------------------------- | --- | ------- | --- | --- |
|     |     | ν Dualvariable(shadowpriceofbudgetpressure)usedbyBD.        |     |         |     |     |
|     |     | α Budgetmultipliercontrollingbudgetstrictnessinexperiments. |     |         |     |     |
ρ Stabilityweightinthescalarizedobjective(quality–stabilitytrade-off).
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 8of48
Table2.Cont.
Symbol Meaning
λ Overload–wastetrade-offweightinthesizing-qualityobjective.
η Dualupdatestepsize(learningrate).
ν Upperboundforνintheprojecteddualupdate.
max
w ,w CPUandmemoryweightsusedwhenaggregatingoverloadandwaste.
cpu mem
h Decisionwindowlength(hours).
T Decisionhorizonlength(numberofwindows).
N NumberofVMsinthefleet.
K DiscreteVM-typeset(instance-typepool).
x VM-typeassignmentvectoratdecisionwindowt.
t
Cost (x ) Totalrealizedplatformcostindecisionwindowt.
t t
Temporalhard-budgetresidual/feasibilityfunctionappliedtothe
g (·)
t realizedcosthistoryuptotimet.
Atahighlevel,theformulationusesfourwindow-levelsignalsperVM:meandemand
µfortypicalload,taildemandqforburstprotection,volatilityσforshort-termvariability,
andentropyHforirregularity. Thesesignalsfeedintoasizing-qualitytermthatpenalizes
bothwasteandrisk-weightedtailshortfall,whileaseparatestabilitytermpenalizesresizing
events. Thebudgetresidualg thenenforcesthechosentemporalspendingrule.
t
3.2. VMTypeSetandCostModel
LetKdenoteafinitesetofVMtypes(instancetypes).Eachtypek ∈ Kischaracterized
byitsCPUcapacitycap (k),memorycapacitycap (k),andhourlypriceprice(k). For
cpu mem
r ∈ R, we write cap (k) to denote the capacity of resource r provided by type k. The
r
maximumcapacityovertheVM-typepoolisdefinedas
capmax maxcap (k).
r r
k∈K
ℛ ≔
Thisquantitywillbeusedasanormalizationscalewhenrequired.
IfaVMisassignedtypekduringadecisionwindowoflengthh,theincurredcostin
thatwindowis
cost(k) price(k)·h.
Let x
i,t
∈ K denote the VM ℛtyp≔e assigned to VM i in window t, and let
x (x ,...,x )denotetheassignmentvectorattimet.Thetotalplatformcostinwindow
t 1,t N,t
tis
ℛ ≔ N
∑
Cost (x ) cost(x ).
t t i,t
i=1
ℛ ≔
ThisexplicitcostmodelisrequiredbecausethebudgetconstraintsinSection3.7apply
toactualspendratherthanproxyutilizationmetrics.
3.3. WorkloadObservationsasWindow-LevelStatistics
Resizing decisions must be robust to bursty and volatile workloads. Rather than
summarizingtheworkloadofaVMbyasingleaveragevalue,werepresenteachdecision
windowbyasmallsetofwindow-levelstatisticsthatcapturebothtypicaldemandand
tailvariability.
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302
9of48
ForeachVM i, resourcer ∈ R, andwindow t, let d (l) denotethe l-thobserved
i,t,r
=
resourcedemandsamplewithinthewindow,forl 1,...,L,measuredinunitsconsis-
(·).
tentwithcap r UndertheexperimentalconfigurationinTable3(decisionwindowis
20minandsamplingintervalis5min),eachwindowcontains L = 4demandsamples,
whereeachsamplecorrespondstoaninterval-aggregateddemandvaluegeneratedbythe
simulator. With=4samplesperwindow,theempirical0.95quantileeffectivelybehaves
asanear-maximumtailproxy;wethereforeuseq i,t,r asalightweighttailindicatorrather
thanahigh-precisionpercentileestimate. Fromthesesamples,theplatformcomputesthe
followingfourstatistics:
Table3.Experimentalconfigurationandhyperparameters.
|     | Item |     |     | Symbols/Values |     |          |          |     |     |     | Notes |     |
| --- | ---- | --- | --- | -------------- | --- | -------- | -------- | --- | --- | --- | ----- | --- |
|     |      |     |     |                |     | (cid:16) | (cid:17) |     |     |     |       |     |
1
| Decisionwindow |     |     |     | h   | =20min | =   | h   |     |     | Fixedacrossexperiments |     |     |
| -------------- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | ---------------------- | --- | --- |
3
| Decisionhorizon  |     |     |     |     | T    | =18 |     |     |     | Fixedacrossexperiments |     |     |
| ---------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | ---------------------- | --- | --- |
| Samplinginterval |     |     |     |     | 5min |     |     |     |     | Fixedacrossexperiments |     |     |
)15
|             |     |     |       |     | (c ,m                | ,p      |     |     |     |                      |     |     |
| ----------- | --- | --- | ----- | --- | -------------------- | ------- | --- | --- | --- | -------------------- | --- | --- |
| VM-typepool |     |     |       |     | k                    | k k k=1 |     |     |     | FixedfiniteVMtypeset |     |     |
|             |     |     | where |     | p istheper-hourprice |         |     |     |     |                      |     |     |
k
=50
| Fleetsize(default) |     |     |     |     | N   |     |     |     |     | UsedinSections6.3and6.4 |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- |
Fleetsize
|     |     |     | N ∈ | {50,100,200,500,1000,10,000} |     |     |     |     |     | UsedinSection6.2.2 |     |     |
| --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | ------------------ | --- | --- |
(scalabilitysweep)
CalibratedusingStaticonareference
| Basebudgetpolicy |     |     | B   | calibratedonce;heldfixed |     |     |     |     |                                |     |     |     |
| ---------------- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | ------------------------------ | --- | --- | --- |
|                  |     |     |     | 0                        |     |     |     |     | workload;fixedacrossruns/seeds |     |     |     |
Budgetstrengthlevels α ∈ {0.1,0.2,...,1.0}(fullsweep) UsedinSections6.2–6.4
Fixedacrossexperiments;
|                 | NSGA-II |     |             |     |       |        |     |      |     | selection=NSGA-II;  |     |     |
| --------------- | ------- | --- | ----------- | --- | ----- | ------ | --- | ---- | --- | ------------------- | --- | --- |
|                 |         |     | pop =50;gen |     | =50;p | =0.7;p |     | =0.3 |     |                     |     |     |
|                 |         |     |             |     |       | c      | m   |      |     |                     |     |     |
| hyperparameters |         |     |             |     |       |        |     |      |     | two-pointcrossover; |     |     |
uniformintegermutation
Fixedacrossexperiments
η =1.0
Dualupdatestepsize
(Section6.1.2)
Riskamplificationweights β =0.3;β =0.4 Fixedacrossallscenarios
|     |     |     |     |     | 1   | 2   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Overload–waste
=0.5
|     |     |     |     |     | λ   |     |     |     |     | Fixedacrossexperiments |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- |
trade-off
| Stabilityweight |     |     |         |         | ρ   | =10 |     |     |     | UsedinSections6.3and6.4 |                 |           |
| --------------- | --- | --- | ------- | ------- | --- | --- | --- | --- | --- | ----------------------- | --------------- | --------- |
|                 |     |     |         |         |     |     |     |     |     | Im pl emen              | t a t io n u se | s w a n d |
|                 |     |     | (cid:0) | (cid:1) |     |     |     |     |     |                         |                 | c pu      |
Resourceweights w cpu , w mem = (0.8, 0.2); w cpu +w mem =1 (cid:0)
|     |     |     |     |     |     |     |     |     |     | 1− w | ) f o r m e m | o ry w ei g h t. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------- | ---------------- |
cpu
=109
| Dualupperbound |     |     |             |     | ν max   |     |           |          |     | Fixedacrossexperiments |     |     |
| -------------- | --- | --- | ----------- | --- | ------- | --- | --------- | -------- | --- | ---------------------- | --- | --- |
|                |     | •   |             |     |         | 1∑L | d         | (l)      |     |                        |     |     |
|                |     |     | Meandemand: |     | µ i,t,r |     | l=1 i,t,r |          |     |                        |     |     |
|                |     |     |             |     |         | L   |           | (cid:16) |     | (cid:17)               |     |     |
(l)}L
|     |     | •   | Taildemand(p95): |     |     | q Quantile |     | {d         |     | .   |     |     |
| --- | --- | --- | ---------------- | --- | --- | ---------- | --- | ---------- | --- | --- | --- | --- |
|     |     |     |                  |     | ℛ   | ≔i,t,r     |     | 0.95 i,t,r |     | l=1 |     |     |
(cid:113)
|     |     |     |                                  |     |     |     |       |     | L    |       | )2    |     |
| --- | --- | --- | -------------------------------- | --- | --- | --- | ----- | --- | ---- | ----- | ----- | --- |
|     |     | •   | Volatility(standarddℛev≔iation): |     |     |     | σ     | 1∑  | (d   | (l)−µ |       |     |
|     |     |     |                                  |     |     |     | i,t,r | L   | l =1 | i,t,r | i,t,r |     |
• Irregularity(entropy): ForeachVMi,windowt,andresourcer,wedefinetheraw
ℛ ≔
Shannonentropyas
B
∑bin
|     |     |     |     |     |     |     | Hraw  | − p   | (b)log | p (b)   |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----- | ------ | ------- | --- | --- |
|     |     |     |     |     |     |     | i,t,r | i,t,r |        | 2 i,t,r |     |     |
b=1
ℛ ≔
whereb ∈1,...,B indexesdiscretizeddemandbinsand p (b)denotestheempiri-
|     |     |     |     |     |     | bin |     |     |     |     | i,t,r |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
=
calprobabilitymass. Intheexperiments,weuseB bin 10equal-widthbinsovera
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302
10of48
fixedabsoluterange[0, capmax]. Theprobabilities p (b)areobtainedbyhistogram-
|     |     | r   | i,t,r |     |
| --- | --- | --- | ----- | --- |
mingnon-negativedemandsamplesclippedtothisrangeforentropycomputation
only. Overloadbeyondallocatedcapacityishandledseparatelybythetail/overload
terms. Wenormalizeentropyas
Hraw
|     |     | H   | i,t,r |     |
| --- | --- | --- | ----- | --- |
i,t,r
log B
2 bin
|     |     | ℛ   | ≔   |     |
| --- | --- | --- | --- | --- |
∈ [0,1].
sothatH i,t,r Unlessotherwisestated,H i,t,r isusedinsubsequentformulations
(e.g., in ω(σ,H)). Because each decision window contains only a small number of
samples under our default monitoring granularity, H is used here as a coarse
i,t,r
irregularitydescriptorratherthanasahigh-precisioninformation-theoreticestimate.
capmax]andthenormalizationbylog
| Thefixedabsoluterange[0, |     |     |     | B bin makeentropy |
| ------------------------ | --- | --- | --- | ----------------- |
|                          |     | r   |     | 2                 |
dimensionless,comparableacrossresources,andindependentofthecurrentlyselected
VMtype. Weuseequal-widthbinningwith B = 10todistinguishconcentrated,
bin
dispersed,andburstydemandshapeswithoutfittingafine-graineddensityfroma
verysmallsampleset.
Collectively,(µ )characterizebaselinedemand,tailbehavior,intra-
|     | i,t,r ,q i,t,r ,σ i,t,r | ,H i,t,r |     |     |
| --- | ----------------------- | -------- | --- | --- |
windowvariability,andunpredictability,respectively,andwillbeusedtomodelthetrade-
offbetweencostefficiencyandoverloadrisk. Atthebeginningofwindowt,theplatform
observesstatisticscomputedfromthemostrecentcompletedwindow(i.e.,windowt−1)
| andusesthemtodeterminetheassignmentx |     |     | t . |     |
| ------------------------------------ | --- | --- | --- | --- |
3.4. DecisionVariablesandResizingStability
Ineachdecisionwindowt,exactlyoneVMtypeisassignedtoeachVM:
|     | x ∈ K, | ∀i ∈ {1,...,N}, | ∀t ∈ {1,...,T} |     |
| --- | ------ | --------------- | -------------- | --- |
i,t
| Fornotationalconvenience,wedefinecap |     |     | (x ) cap (k)wherek | = x . |
| ------------------------------------ | --- | --- | ------------------ | ----- |
|                                      |     |     | r i,t r            | i,t   |
Practical resizing systems often limit excessive configuration changes due to mi-
ℛ ≔
gration overhead and operational instability. To capture resizing stability, we define a
changeindicator
|     | chg | I{x ̸= x | }, ∀i, ∀t ≥2 |     |
| --- | --- | -------- | ------------ | --- |
|     |     | i,t i,t  | i,t−1        |     |
whereI{·}denotestheindicatℛor≔function(andwesetchg 0byconvention).
i,1
Optionally,aminimumdwell-timeconstraintcanbeimposedtopreventrapidoscilla-
ℛ ≔
tions. LetDdenotetheminimumnumberofconsecutivewindowsthataVMmustremain
onaselectedtypebeforeanotherchangeisallowed. Thisrequirementcanbewrittenas
t+D−1
∑
|     |     | chg ≤1, | ∀i, ∀t ≤ T−D+1. |     |
| --- | --- | ------- | --------------- | --- |
i,τ
τ=t
3.5. ModelingOver-ProvisioningandOverloadRisk
Resizingdecisionsmustbalancetwocompetinggoals: reducingwasteduetoover-
provisioningandavoidingoverloadduetounder-provisioning. Toformalizethistrade-off,
wedefineresource-leveloverloadandwastequantitiesforeachVM,decisionwindow,and
Weusethepositive-partoperator[a]+ max{0,a}.
resourcedimension.
ThroughoutSections3.5and3.6,thestatisticsµ ,q ,σ andH denotethemost
|     |     |     | i,t,r i,t,r i,t,r | i,t,r |
| --- | --- | --- | ----------------- | ----- |
ℛ ≔
recent workload observations available at the decision time of window t, i.e., statistics
computedfromtheimmediatelyprecedingcompletedwindow. Thisconventionpreserves
anonlinedecision-makinginterpretationwithoutintroducingadditionalindices.
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302
11of48
3.5.1. OverloadRisk(Under-Provisioning)
Overloadriskariseswhentheallocatedcapacityisinsufficienttoaccommodatehigh
(tail)demand. Wedistinguishbetweenarawtailshortfall(aphysicalcapacityviolationat
thetail)andarisk-weightedoverloadterm,reflectingthatthesameshortfallisoperationally
moresevereunderhighlyvolatileorirregularworkloads.
ForeachVMi,windowt,andresourcer,wedefinetherawtailshortfallas
|     |     |         | (x ) | [q −cap | (x )]+ |     |
| --- | --- | ------- | ---- | ------- | ------ | --- |
|     |     | δ i,t,r | t    | i,t,r   | i,t    |     |
r
|        |                               |     | ℛ ≔        |     | (x )istheallocatedcapacity. |        |
| ------ | ----------------------------- | --- | ---------- | --- | --------------------------- | ------ |
| whereq | i,t,r isthe95th-percentiledem |     | a ndandcap |     | i,t                         | Tomod- |
r
ulateoverloadseverityundervolatileorirregularworkloads,weintroduceaworkload-
dependentweightingfactor
|     |     |     | ω     | ω(σ , | H )   |     |
| --- | --- | --- | ----- | ----- | ----- | --- |
|     |     |     | i,t,r | i,t,r | i,t,r |     |
whereσ andH denotethestandℛard≔deviationandentropyofdemandsampleswithin
|     | i,t,r i,t,r |     |     |     |     |     |
| --- | ----------- | --- | --- | --- | --- | --- |
window,respectively. Weassumeω(·)isnonnegative,monotonenon-decreasingineach
argument, and lower-bounded by 1, so that higher variability or irregularity yields a
strongerpenaltyforoverloadrisk. Importantly,ω i,t,r istreatedasafunctionofobserved
workload statistics only (i.e., it does not depend on the decision variable x ). In the
i,t
experiments,weinstantiateω usingaboundedadditiveform(reportedinSection6.1),
i,t,r
which guarantees ω ∈ [1, ω ] for numerical stability while preserving monotone
i,t,r max
riskamplification.
Therisk-weightedoverloadtermisthendefinedas
|     |     |      | (x    | )         | ·δ (x ) |     |
| --- | --- | ---- | ----- | --------- | ------- | --- |
|     |     | over | i,t,r | t ω i,t,r | i,t,r t |     |
ℛ ≔
Thisconstructionpenalizesassignmentsthatprovideinsufficientheadroomduring
bursts, while assigning larger penalties to the same tail shortfall when the workload
exhibitshighervariabilityorirregularity. Theboundedadditiveformofωisintentional.
Volatilityandirregularityaretreatedastwoindependentfirst-ordersignalsthatamplify
thesamerawtailshortfall,whiletheadditiveformpreservesinterpretabilityandavoids
multiplicativeblow-upwhenbothsignalsarelarge. Wethereforeuseωasalightweight,
decision-independentriskamplifierratherthanasaseparatepredictivemodel.
3.5.2. Waste(Over-Provisioning)
Conversely, waste occurs when the allocated capacity consistently exceeds typical
(baseline)demand,leadingtopersistentunusedresources. ForeachVMi,windowt,and
| resourcer | ∈ R,wedefinethewasteamountas |     |     |     |     |     |
| --------- | ---------------------------- | --- | --- | --- | --- | --- |
]+
|     |     | waste | (x )    | [cap (x | )−µ .     |     |
| --- | --- | ----- | ------- | ------- | --------- | --- |
|     |     |       | i,t,r t | r       | i,t i,t,r |     |
whereµ isthemeandemandwithinwindowt. ℛ ≔ Thistermquantifiesunusedcapacityrel-
i,t,r
ativetotypicaldemandandencouragesdownsizingwhenallocatedresourcessubstantially
exceedaverageneeds.
3.5.3. AggregatedOverloadandWasteMetrics
Tofacilitateobjectiveformulationandsystem-levelevaluation,weaggregateoverload
riskandwasteacrossallVMsandresourcedimensions. Thetotaloverloadriskandwaste
inwindowtaredefinedas
N
|     |     | Over | (x ) | ∑ ∑ w | over (x ), |     |
| --- | --- | ---- | ---- | ----- | ---------- | --- |
|     |     |      | t t  |       | r i,t,r t  |     |
i=1r∈R
|     |     |     | ℛ ≔ |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 12of48
N
∑ ∑
Waste (x ) w waste (x ).
t t r i,t,r t
i=1r∈R
ℛ ≔
The weights w reflect the relative importance of CPU and memory resources and
r
are shared consistently across all objective terms. These weights are treated as tunable
parameters that can be adjusted depending on the operational context or experimental
setting,ratherthanbeingfixedconstants. Wenormalizeeachresourcebyafixedcapacity
scalecapmaxsothatCPUandmemorycontributeasdimensionlessratios. Becausethisisa
r
constantscalingindependentofthedecisionvariables,itdoesnotalterthecombinatorial
structureorthehardnessresults.
Theseaggregatedquantitiessummarizesystem-widetail-safetyloss(risk-weighted
shortfalls)andover-provisioningloss,respectively,andareuseddirectlyintheobjective
functionsinSection3.6.
3.6. ObjectiveFunctions
BasedontheworkloadstatisticsandsizingmetricsintroducedinSections3.3–3.5,we
formulateVMresizingasamulti-objectiveoptimizationproblemthatbalancesresource
efficiency, tail safety, and operational stability under explicit budget constraints. For
a planning horizon of T decision windows, the objectives and constraints are defined
asfollows:
T
∑
f (x ) (Waste (x )+λOver (x )), (1)
1 1:T t t t t
t=1
ℛ ≔
T N
∑ ∑
f (x ) chg , (2)
2 1:T i,t
t=2i=1
ℛ ≔
s.t.x ∈ K,∀i,t (3)
i,t
g (Cost (x ),...,Cost (x )) ≤0, ∀t (4)
t 1 1 t t
Thefirstobjective f capturesoverallsizingqualitybyaggregating, overtime, the
1
trade-offbetweenover-provisioningandunder-provisioning. ThetermWaste (x )mea-
t t
suresunusedcapacityrelativetomeandemand,whileOver (x )measuresrisk-weighted
t t
tailshortfallsbasedonp95demand,asdefinedinSection3.5. Becauseoverloadriskisal-
readyweightedattheVM–resourcelevelaccordingtoworkloadvolatilityandirregularity,
thesamephysicalshortfallincursalargerpenaltyforburstyorunpredictableworkloads.
Theparameterλ ≥0controlstherelativeimportanceoftailsafetyversusresourceefficiency
andistreatedasatunableparameterthatcanbeadjusteddependingonoperationalpriori-
tiesorexperimentalscenarios. AlthoughcloudpricingisexplicitlydefinedinSection3.2,
monetarycostisnotdirectlyminimizedintheobjectivefunction. Instead,costisenforced
asahardfeasibilityconstraintthroughthebudgetmodelsinSection3.7,whiletheobjective
functionfocusesonbalancingresourcewasteandoverloadriskwithinthefeasiblebudget
region. This separation reflects a FinOps-oriented design, where budget compliance is
mandatoryandperformance–efficiencytrade-offsareoptimizedunderthatconstraint.
Thesecondobjective f capturesoperationalstabilitybypenalizingfrequentresizing
2
actions. Theindicatorchg ,introducedinSection3.4,equalsonewhenVMichangesits
i,t
assignedtypebetweenconsecutivewindowsandzerootherwise. Byminimizing f ,the
2
formulationdiscouragesexcessiveconfigurationchangesthatmayincurmigrationover-
headoroperationaldisruption. Thisformulationintentionallypenalizestheoccurrenceof
resizingeventsratherthantheirmagnitude,reflectingtheoperationalriskandcoordination
overheadassociatedwithanyconfigurationchange,irrespectiveofitssize.
The budget constraint is expressed in a generic form through the function g (·),
t
which enforces feasibility over the realized platform cost sequence {Cost (x )}. This
t t
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302
13of48
abstraction allows the same objective structure to accommodate different operational
(·)isinstantiatedtorepresentconcrete
| budgetingpolicies. | InSection3.7,theconstraintg |     |     | t   |     |
| ------------------ | --------------------------- | --- | --- | --- | --- |
scenariossuchasper-windowrun-ratelimits,absolutecumulativebudgets,incremental
growthconstraints,androlling-horizonbudgets.
Overall,theproposedformulationyieldsaclearParetotrade-offbetweensizingquality
andoperationalstability,whileexplicitlyenforcingbudgetfeasibilitythroughconstraints
rather than objectives. This separation enables flexible FinOps-aware policy modeling
withoutalteringthecoreoptimizationstructure.
3.7. BudgetConstraints
Cloud cost control in practice is governed by externally imposed FinOps policies,
which must be satisfied as hard feasibility requirements rather than soft optimization
preferences. Inourformulation,budgetconstraintsareimposeddirectlyontherealized
platformcost,notonproxymetricssuchasutilizationorallocatedcapacity. Specifically,
|                                            |     |     |     |               | (x ),asdefinedinSection3.2,andall |
| ------------------------------------------ | --- | --- | --- | ------------- | --------------------------------- |
| thetotalcostincurredinwindowtisgivenbyCost |     |     |     | t             | t                                 |
| budgetmodelsoperateonthesequence{Cost      |     |     |     | (x ),...,Cost | (x )}.                            |
|                                            |     |     |     | 1 1           | t t                               |
Toaccommodatediversereal-worldbudgetingpolicieswithinaunifiedframework,
weexpressbudgetfeasibilitythroughagenericconstraintfunction
|     | g   | (Cost (x ),...,Cost |     | (x )) ≤0, | ∀t ∈ {1,...,T} |
| --- | --- | ------------------- | --- | --------- | -------------- |
|     | t   | 1 1                 |     | t t       |                |
whichcorrespondstoconstraint(4)inSection3.6. Fornotationalconvenience,weequiva-
lentlywrite
|     |     | g t (x 1:t )| | |g t (Cost | (x ),...,Cost | t (x t )) |
| --- | --- | ------------- | ---------- | ------------- | --------- |
|     |     |               |            | 1 1           |           |
sincetherealizedcostsequenceℛup≔totimetisuniquelydeterminedbyx . Differentoper-
1:t
ationalbudgetpoliciesareobtainedbyinstantiatingg t (·)appropriately. Thisabstraction
allowstheobjectivestructuretoremainunchangedwhileenablingflexiblemodelingof
short-termratelimits,long-termcumulativecaps,growthconstraints,androlling-horizon
budgets. Allbudgetparametersareassumednonnegativeforallt.
These four models represent, respectively, (i) instantaneous per-window caps,
(ii) long-horizon cumulative caps, (iii) limits on abrupt cost increases, and (iv) sliding-
horizoncapsoverrecentwindows.
3.7.1. Run-Rate(Per-Window)Budget
Therun-ratebudgetenforcesastrictupperboundonthecostincurredineachindi-
vidualdecisionwindow. LetB (t)denotethemaximumallowedcostinwindowt.
rate_pw
Thecorrespondingconstraintis
|     |     | Cost | (x ) ≤ | B (t),  | ∀t, |
| --- | --- | ---- | ------ | ------- | --- |
|     |     |      | t t    | rate_pw |     |
orequivalently,
rate_pw
|     |     | g   | =Cost | (x )−B      | (t) ≤0. |
| --- | --- | --- | ----- | ----------- | ------- |
|     |     | t   |       | t t rate_pw |         |
Thisbudgetmodeldirectlylimitsinstantaneousspendingandpreventsshort-termcost
spikes. Becausefeasibilitymustbesatisfiedindependentlyineverywindow,noborrowing
ofbudgetacrosstimeisallowed. Asaresult,therun-ratebudgetisconservativeunder
burstyworkloadsbutalignswellwithoperationalsettingswheremaintainingastableburn
rateisessential.
Fromananalyticalperspective,therun-rateformulationalsohasanimportantstruc-
turalproperty. Therun-ratebudgetmodelalsoenablesatractableanalyticalformulation
because the budget constraint is applied independently at each decision window. This
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302
14of48
separabilityallowsthediscreteVMassignmentproblemtoberelaxedintoacontinuous
formulation,whichenablestheprimal–dualanalysisdevelopedinSection5. Incontrast,
cumulative, rolling, andincrementalbudgetmodelsintroduceinter-temporalcoupling
acrosswindows, whichsignificantlycomplicatestheoreticalanalysis. Forthesebudget
semantics,theBDsolveristhereforeevaluatedprimarilythroughempiricalexperiments.
3.7.2. AbsoluteCumulativeBudget
The absolute cumulative budget constrains the total cost accumulated up to each
decisionwindow. LetB (t)denotethemaximumallowablecumulativecostbythe
abs_cum
| endofwindowt. | Theconstraintisexpressedas |     |     |     |     |     |     |
| ------------- | -------------------------- | --- | --- | --- | --- | --- | --- |
t
∑
|     |     |     | Cost | (x ) ≤ | B       | (t), | ∀t, |
| --- | --- | --- | ---- | ------ | ------- | ---- | --- |
|     |     |     | τ    | τ      | abs_cum |      |     |
τ=1
orequivalently,
t
|     | gabs_cum |     | = ∑ |        | (x )−B |         | (t) ≤0. |
| --- | -------- | --- | --- | ------ | ------ | ------- | ------- |
|     | t        |     |     | Cost τ | τ      | abs_cum |         |
τ=1
Unliketherun-ratemodel,thecumulativebudgetallowstemporaryoverspending
as long as it is compensated by lower spending in other windows. This formulation
naturally captures common FinOps practices such as daily, weekly, or monthly bud-
get caps, and it supports arbitrary cumulative budget trajectories without altering the
optimizationstructure.
3.7.3. IncrementalBudget(Upsizing-DrivenCostCap)
Theincrementalbudgetlimitshowmuchtheplatformisallowedtoincreasespend
viascale-up(upsizing)actionsbetweenconsecutivedecisionwindows. Unlikeabsolute
cumulativebudgets,thismodelconstrainsonlyupsizing-drivencostincreasesonaper-
(t)denotetheper-
| windowbasis,withoutlimitingtotalaccumulatedspend. |     |     |     |     |     |     | LetB inc_cum |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ |
windowcaponupsizing-drivencostincrementsatwindowt. Wemeasurethenetplatform
costchangebetweenconsecutivewindowsasCost (x )−Cost (x )andchargeonly
|     |     |     |     |     |     | t t | t−1 t−1 |
| --- | --- | --- | --- | --- | --- | --- | ------- |
)]+
its positive part, i.e., [Cost (x )−Cost t−1 (x t−1 . Hence, downsizing-induced savings
|     |     | t t |     |     |        |     |     |
| --- | --- | --- | --- | --- | ------ | --- | --- |
|     |     |     |     | (x  | )−Cost | (x  | ) < |
donotcreatebudgetcredit: whenCost t t t−1 t−1 0,thechargedincrement
is zero. Since B (t) ≥ 0, this positive-part charging can be enforced by the affine
inc_cum
| constraintbelow. | Fort ≥2,theconstraintisgivenby |     |        |     |      |         |     |
| ---------------- | ------------------------------ | --- | ------ | --- | ---- | ------- | --- |
|                  | Cost                           | (x  | )−Cost |     | (x ) | ≤ B     | (t) |
|                  |                                | t   | t      | t−1 | t−1  | inc_cum |     |
whichcanbewrittenas
|            | inc |        | (x )−Cost |     | (x )−B |         | (t) ≤0 |
| ---------- | --- | ------ | --------- | --- | ------ | ------- | ------ |
|            | g t | Cost t | t         | t−1 | t−1    | inc_cum |        |
| withginc = | ℛ ≔ |        | =         |     |        |         |        |
0byconv en tion. Fort 1,wetreatx 1 asgiven;alternatively,arun-ratecap
1
| Cost (x ) ≤ B | (1)maybeapplied. |     |     |     |     |     |     |
| ------------- | ---------------- | --- | --- | --- | --- | --- | --- |
| 1 1 rate_pw   |                  |     |     |     |     |     |     |
Althoughindexedcumulatively,feasibilityisevaluatedwindow-wise;thus,thecon-
straintfunctionsasaper-windowcaponupsizing-drivencostincreasesratherthanasa
cumulativespendinglimit. Thismodelenforcesfinancialsmoothnessbylimitingabrupt
costescalationswhileallowingdownsizingactions. Theincrementalbudgetthereforecom-
plementstheresizing-stabilityobjective f ,whichpenalizesthefrequencyofconfiguration
2
changesbutdoesnotdirectlyconstraintheirfinancialimpact. SinceB (t) ≥ 0,the
inc_cum
affineconstraintprovidesanexactrepresentationofthepositive-partcap.
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 15of48
Weusethisaffineformasthebudgetresidual ginc intheBDsolvertopreservethe
t
per-windowseparability. Thiswindow-wiseformulationisintentional,asitenablesthe
incrementalbudgettobeintegratedintotheBDsolverwithoutbreakingthestage-wise
structurerequiredforscalableonlineoptimization.
3.7.4. RollingBudget
Therollingbudgetconstrainsspendingoveraslidinghorizonoffixedlength. Let
W ∈ Z+ denotetherolling-horizonlengthinthenumberofdecisionwindows, andlet
B (t)denotethemaximumallowedcostoverthemostrecentW windowsendingatt.
roll
Theconstraintiswrittenas
t
∑
Cost (x ) ≤ B (t),
τ τ roll
τ=max{1,t−W+1}
orequivalently,
t
groll ∑ Cost (x )−B (t) ≤0.
t τ τ roll
τ=max{1,t−W+1}
ℛ ≔
The rolling budget lies between per-window and fully cumulative constraints. It
allowsshort-livedcostburstswhilepreventingsustainedoverspendingoveranyrecent
horizon of length W. This formulation closely reflects continuous budget monitoring
practicesandiswellsuitedtorolling-windowFinOpspolicies.
3.8. Budget-ConstrainedVMResizingProblem
Wearenowreadytoformallydefinethebudget-constrainedVMresizingproblem.
OveraplanninghorizonofTdecisionwindows,theplatformselects,ateachwindowt,
aVMtypeassignmentvectorx = (x ,...,x ) ∈ KN,wherex denotestheVMtype
t 1,t N,t i,t
assigned to VM i during window t. Let x (x ,...,x ) denote the full resizing plan.
1:T 1 T
Budgetfeasibilityisenforcedthroughtheconstraintfamily
ℛ ≔
g (x ) ≤0, ∀t ∈ {1,...,T} (5)
t 1:t
whereCost (x )istherealizedplatformcostinwindowt,andg (·)isinstantiatedbyone
t t t
ofthebudgetmodelsintroducedinSection3.7(run-rate,absolutecumulative,incremental,
orrolling). Thefeasiblesetisthereforedefinedas
F {x |x ∈ K∀i,t,g (x ) ≤0∀t}, (6)
1:T i,t t 1:t
ℛ ≔
optionally augmented with operational constraints such as minimum dwell time
whenrequired.
3.8.1. Bi-ObjectiveFormulation
Using the objective functions defined in Section 3.6, we formulate the Budget-
Constrained VM Resizing problem, hereafter referred to as BC-VMR, as the following
bi-objectiveoptimization:
min (f (x ),| f (x )) (7)
1 1:T 2 1:T
x1:T ∈F
where f aggregates,overtime,thetrade-offbetweenresourcewasteandrisk-weighted
1
overload, and f penalizes resizing frequency to capture operational stability. A feasi-
2
ble solution x∗ ∈ F is Pareto optimal if no other feasible sequence weakly improves
1:T
both objectives and strictly improves at least one. The Pareto frontier thus character-
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 16of48
izesthefundamentaltrade-offbetweensizingqualityandresizingstabilityunderhard
budgetcompliance.
3.8.2. ScalarizedFamily
While the problem is inherently bi-objective, concrete operating points are often
required for algorithm design and experimental evaluation. We therefore introduce a
scalarizedvariantofBC-VMR,denotedbyBC-VMRρforρ≥0:
min F (x ), F (x ) = f (x )+ρ f (x ) (8)
ρ 1:T ρ 1:T 1 1:T 2 1:T
x1:T ∈F
VaryingρselectsdifferentPareto-efficientoperatingregimes,whichisusefulbothfor
practicaldeploymentandforcomparativeevaluationusingmetricssuchashypervolume.
3.8.3. Stage-WiseStructureandPer-WindowInterpretation
Thescalarizedobjectiveadmitsanadditivestage-wiserepresentation:
T T N
F ρ (x 1:T )
∑
(Waste t (x t )+λOver t (x t ))+ρ
∑ ∑I{x
i,t ̸= x i,t−1 }, (9)
t=1 t=2i=1
ℛ ≔
where each per-window cost depends on the current assignment x and, through the
t
change indicator, on the previous assignment x t−1 . Moreover, as shown in Section 3.5,
Waste (·) and Over (·) decompose across VMs and resource dimensions, revealing a
t t
per-VM separable structure within each window. This representation does not im-
ply a dynamic programming solution, but it exposes structural properties that will be
exploitedalgorithmically.
3.8.4. ComputationalImplication
Evenforasingledecisionwindow,theassignmentspacehascardinality|K|N
,and
budgetconstraintsintroduceknapsack-likecouplingacrossVMsand, forsomebudget
models, across time. As a result, the problem is combinatorial and computationally in-
tractable at scale for exact methods. This observation motivates the complexity anal-
ysis in Section 4 and the proposed dual-variable-based solution strategy in Section 5,
whichleveragestheper-VMstructurewhileenforcingbudgetfeasibilitythroughaglobal
shadowprice.
4. ComplexityAnalysis
This section establishes the computational intractability of the BC-VMR problem
formulatedinSection3.8. SinceVMtypesarediscreteandbudgetfeasibilityconstraints
coupledecisionsthroughrealizedcosts,theresultingoptimizationproblemisinherently
combinatorial. The goal of this section is to position BC-VMR within the established
combinatorialcomplexitylandscape,ratherthantoclaimanewhardnessarchetype. We
proveNP-hardnessforthescalarizedfamilyintroducedinEquation(8),whichimmediately
impliesthattheexactcharacterizationoftheParetofrontierofthebi-objectiveproblemin
Equation(7)isintractableintheworstcase.
4.1. NP-HardnessAnalysis
ToestablishNP-hardness,wefirstconsiderthecorrespondingdecisionversionofthe
scalarizedprobleminEquation(8).
Definition1. Fixρ ≥ 0. GivenaninstanceofBC-VMR(ρ)andathresholdΘ,decidewhether
thereexistsafeasibleresizingplanx ∈ FsuchthatF (x ) ≤Θ.
1:T ρ 1:T
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302
17of48
Lemma1. ThedecisionprobleminDefinition1belongstoNP.
Proof of Lemma 1. A certificate consists of a concrete resizing plan x . Feasibility
1:T
can be verified by evaluating constraints (3) and (4), where the cost function Cost (·)
t
(·)
follows Section 3.2 and the budget function g t is instantiated by one of the models
inSections3.7.1–3.7.4. TheobjectivevalueiscomputedusingEquations(1)and(2)and
substitutedintoEquation(8). Allrequiredcomputationsarepolynomialinthenumberof
□
VMsN,thenumberofwindowsT,andthesizeoftheVMtypeset|K|.
We next show that the BC-VMR decision problem is computationally intractable
even under a highly simplified setting. In particular, we focus on the run-rate budget
model,whichimposesaper-windowcostcapandrepresentsthemostbasicformofbudget
constraint. Byreducingfromtheclassical0–1Knapsackdecisionproblem,wedemonstrate
thatthisrestrictedcaseisalreadyNP-complete.
Undertherun-ratebudgetmodel(Section3.7.1),thedecisionprobleminDefinition1
Lemma2.
isNP-complete. Hence,BC-VMR(ρ)isNP-hardevenwhenT = 1,thestabilityobjective(2)is
inactive,andonlyasingleresourcedimensioncontributestoEquation(1).
Proof of Lemma 2. We reduce from the 0–1 Knapsack decision problem. Consider a
knapsackinstancewithitems i = 1,...,N, weights p, values v, capacity C, andtarget
|     |     |     |     |     |     |     | i   | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
valueV. WeconstructaBC-VMRinstanceasfollows.
=
We set T 1 and activate a single resource dimension (Section 3.5.3), so that the
scalarizedobjectiveinEquation(8)reducestominimizingEquation(1). Forthereduction,
wefixthetrade-offparametersbysettingλ =1andw =1forthesingleactiveresource
r
dimension. Moreover,wefixtheoverloadamplificationfactortoaconstantω = ω ≥1
i,t,r
foralli,t. ThischoiceonlyscalesallvaluesuniformlyanddoesnotaffectNP-hardness.
|     |     |     | 1+∑N |     | +maxv,q |     | =   | = i· |     |
| --- | --- | --- | ---- | --- | ------- | --- | --- | ---- | --- |
Define the spacing constant M i=1 v i i i µ i M. If the overload
i
amplificationfactorinSection3.5.1satisfiesω(·) ≥ 1,wefixallVMstoshareaconstant
ℛ ≔
| valueω;thisuniformlyscalesallv |     |     | i   | anddoesnotaffectNP-hardness. |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- |
Foreachitemi,weintroducetwoVMtypes:
| cap(b) | =i ·M, | cost(b) | =   | c +p, |     | cap(a | ) =iM−v, | cost(a ) | = c , |
| ------ | ------ | ------- | --- | ----- | --- | ----- | -------- | -------- | ----- |
| i      |        |         | i   | 0     | i   |       | i        | i i      | 0     |
wherec > 0isaconstantbaselinecostconsistentwithSection3.2. Thesingle-window
0
budgetissettoB′
Nc +C.
0
Assigningtype b i yieldszerowasteandzerotailshortfall, whereasassigningtype
|     | ℛ ≔ |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a yieldsatailshortfallofexactlyv withzerowaste. Anymismatchassignmentusinga
| i   |     |     |     | i   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
typeintendedforadifferentindex j ̸= iincursapenaltyexceeding∑ v . Specifically,if
|     |     |     |     |     |     |     |     | k k |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
j <i,theallocatedcapacityisbelowq,causingatailshortfallofatleast(i−j)M ≥ M;if
i
≥1+∑
j >i,theallocatedcapacityexceedsµ,resultinginwasteofatleastM−maxv v .
|     |     |     |     | i   |     |     |     |     | k k |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
≤ ∑
| Therefore,forallthresholdsΘ |     |     |     | i v,wemayrestrictattentiontoassignmentsselecting i |     |     |     |     |     |
| --------------------------- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
only{a,b}foreachVM.
i i
Let z ∈ {0,1} indicate whether b is selected. The run-rate budget constraint
| i   |     |     |     |     | i   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
reducesto
|     |     | ∑      |      | ∑   |         | ′   | ∑     |       |     |
| --- | --- | ------ | ---- | --- | ------- | --- | ----- | ----- | --- |
|     |     | cost(a | i )+ | p i | z i ≤ B | ⇐⇒  | p i z | i ≤C, |     |
|     |     | i      |      | i   |         |     | i     |       |     |
andtheobjectivesatisfies
|     |     | ∑   |        |     | ∑    |     | ∑   |         |     |
| --- | --- | --- | ------ | --- | ---- | --- | --- | ------- | --- |
|     | F   | =   | v (1−z | ) ≤ | v −V | ⇐⇒  |     | v z ≥V. |     |
|     |     | ρ   | i      | i   | i    |     |     | i i     |     |
|     |     | i   |        |     | i    |     | i   |         |     |
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 18of48
Thus,theknapsackinstanceadmitsafeasiblesolutionifandonlyiftheconstructed
BC-VMR(ρ)instancehasafeasibleplanwithF ≤ ∑ v −V. Thereductionispolynomial,
ρ i i
□
andtogetherwithLemma1,thedecisionproblemisNP-complete.
Corollary 1. Under the absolute cumulative budget model (Section 3.7.2), BC-VMR(ρ)
isNP-hard.
ProofofCorollary1. For T = 1,thecumulativeconstraintreducestoasingle-window
□
budgetcapidenticaltotherun-ratemodel. Lemma2appliesdirectly.
Corollary2. Undertheincrementalbudgetmodel(Section3.7.3),BC-VMR(ρ)isNP-hard.
Proof of Corollary 2. Consider T = 2 and fix x such that Cost (x ) is constant. The
1 1 1
incremental constraint at t = 2 becomes a single-window cost cap up to an additive
□
constant,reducingtotherun-ratecase. Lemma2applies.
Corollary3. Undertherollingbudgetmodel(Section3.7.4),BC-VMR(ρ)isNP-hard.
ProofofCorollary3. SettingtherollinghorizontoW =1reducestherollingconstraintto
□
aper-windowbudgetcapidenticaltotherun-ratemodel. Lemma2applies.
Theorem1. ForeachbudgetmodelinSections3.7.1–3.7.4,computingagloballyoptimalsolution
ofBC-VMR(ρ)isNP-hard. Consequently,exactcomputationoftheParetofrontierofBC-VMR
(Section3.8.1)isintractableintheworstcaseunlessP = NP.
ProofofTheorem1. Lemma2establishesNP-hardnessfortherun-ratemodel. Corollaries
1–3showthattheremainingbudgetmodelseachcontainaparameterregimethatreduces
□
totherun-ratecase. Therefore,allfourinstantiationsyieldNP-hardglobaloptimization.
4.2. ImplicationsandDiscussion
TheNP-hardnessresultholdsevenunderextremesimplifications, includingasin-
gledecisionwindow,theabsenceofresizing-stabilitycosts,andasingleactiveresource
dimension. The full multi-window BC-VMR problem with cross-window budget cou-
plingisthereforeatleastashard,motivatingscalableapproximationmethodssuchasthe
dual-variable-basedapproachdevelopedinSection5.
BeyondtheNP-hardnessresult,itisusefultocharacterizestructuralinfeasibilitymore
explicitly. Underthebaserun-ratemodelwithoutadditionaldwell-timerestrictions,let
k ∈ K denote the lowest-cost VM type in the pool. Then, window t is structurally
min
infeasiblewhenever
N·cost(k ) > B (t),
min rate_pw
becauseevenassigningeveryVMtothecheapestavailabletypestillexceedstheactive
budgetcap. Equivalently,anecessaryconditionforwindow-levelfeasibilityis
B (t) ≥ N·cost(k ).
rate_pw min
Thisclosed-formthresholdexplainsthefeasibilitytransitionobservedinSection6:
asthebudgetmultiplierαincreases,thefeasibleregionexpandsuntiltherun-ratebudget
becomes large enough to accommodate the lowest-cost assignment; beyond that point,
feasiblecandidatedecisionsbecomeavailableandviolationratescollapserapidly.
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 19of48
5. ProposedMethod
ThissectionpresentstheproposedBudget-awareDual(BD)solverforthebudget-
constrainedVMresizingproblem. Thegoalistoobtainpracticallydeployablesolutions
forBC-VMR(ρ)underhardbudgetfeasibility,whilepreservingthecoretrade-offbetween
sizingqualityandresizingstability.
5.1. ProblemRecapandAlgorithmicChallenges
WeconsiderthescalarizedfamilyBC-VMR(ρ)definedinEquation(8)overthefeasible
setF specifiedbyconstraints(3)and(4). TheobjectiveF admitsthestage-wiserepresen-
ρ
tationinEquation(9),wherethewindow-leveltermsdependonthecurrentassignment
x t and, through the change indicator, on the previous assignment x t−1 . Moreover, the
wasteandoverloadcomponentswithineachwindowdecomposeacrossVMsandresource
dimensions,revealingaper-VMseparablestructureinside f .
1
Despitethisstructure,Section4establishesthatcomputingagloballyoptimalsolution
ofBC-VMR(ρ)isNP-hardundereachbudgetmodelinSections3.7.1–3.7.4. Hence,exact
methods, dynamic programming, or full Pareto-frontier enumeration are not viable at
scale. PracticalVMresizingcontrollersrequire(i)near-real-timedecisionsperwindow,
(ii)scalabilitytolargeN,and(iii)strictbudgetawarenessinthesensethatbudgetpolicies
remainfeasibilityrequirementsratherthanadditionalobjectives.
5.2. KeyIdea: Dual-BasedBudgetAwarenessUnderHardConstraints
Thecentraldifficultyisthatbudgetsareimposedonrealizedspend,i.e.,onthecost
sequence (cid:8) Cost (x )}T throughEquation(5)whichisthegenericfeasibilityconstraint.
t t t=1
BecauseVMtypesarediscrete,itispossiblethat,insomewindows,noassignmentx ∈ KN
t
satisfiesthebudgetcapimpliedby g (e.g.,duetoacoarsetypesetorhighlyrestrictive
t
caps). Insuchregimes,budgetviolationsarestructurallyunavoidableregardlessofthe
algorithm. ThisobservationmotivatesreportingtheBudgetViolationRateinSection6asan
operationalmetric,anditalsomotivatestheneedforasolverthatreactstobudgetpressure
inaprincipledandstableway.
BDintroducesanonnegativedualvariableνthatactsasashadowpriceforthebudget
constraint. Importantly,νisnotusedtoredefinebudgetsassoftpreferences. Instead,ν
providesaglobal,quantitativesignalofbudgettightnessthatguidestheselectiontoward
lower-costassignments,especiallywhenthefeasiblesetbecomesemptyincertainwindows.
Conceptually,whenthebudgetistight,νincreasesandmakesexpensiveVMtypesless
attractive; when the budget is loose (or effectively inactive), ν decreases and ceases to
throttledecisions.
Fromanoperationalperspective,budgetpoliciesaretreatedashardfeasibilityrequire-
mentsanddefineadmissibleoperatingregimes. Algorithmically,however,thediscrete
VM type set may render the feasible set empty in certain windows. In such cases, BD
operates as an online primal–dual controller that reacts to budget pressure and mini-
mizesthemagnitudeandfrequencyofunavoidableviolations,ratherthanrelaxingthe
constraintitself.
A key computational advantage follows: for a fixed value of ν at a given window,
theresultingcost-awaredecisioncanbemadeindependentlyperVM,sincetheobjective
terms already admit a per-VM decomposition within each window. This yields a per-
windowruntimethatscalesapproximatelyasO(N|K|),whichisessentialforthelarge-scale
experimentsinSection6andforpracticaldeploymentsettings.
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302
20of48
It is also informative to examine a simplified boundary case. When the run-rate
(per-window)budgetmodelisusedandresizingstabilityisdisabled,thedecisionineach
window reduces to selecting one VM type for each VM under a single cost cap. This
structure corresponds to a multiple-choice knapsack problem, where each VM forms a
choicegroupandthecontrollerselectsonetypepergroupsubjecttothebudgetlimit. Such
problemsadmitpseudo-polynomialdynamicprogrammingalgorithmsandapproximation
schemes. However,oncetemporalcouplingisintroducedthroughcumulative,rolling,or
incrementalbudgetmodels,thisstage-wiseseparabilitydisappearsanddecisionsbecome
coupled across time. In these settings, scalable online control mechanisms such as the
proposedBDsolverbecomenecessary.
5.3. Budget-AwareReformulationoftheScalarizedProblem
WestartfromBC-VMR(ρ)inEquation(8)underfeasibilityconstraints(3)and(4). BD
doesnotredefinetheoriginaloptimizationproblem. Instead,itintroducesaLagrangian-
| stylesurrogateobjective.Foragivennonnegativedualsequenceν,wedefinethefollowing |     |     |     | t   |     |
| ------------------------------------------------------------------------------ | --- | --- | --- | --- | --- |
surrogatecostfunction:
T
∑
|     | minF (x )|+| | ν g (x  | ), ν ≥0 ∀t. |     | (10) |
| --- | ------------ | ------- | ----------- | --- | ---- |
|     | x1:T ρ 1:T   | t t 1:t | t           |     |      |
t=1
ForeachbudgetmodelinSection3.7,thewindow-wiseresidualcanbeexpressedin
anaffineformwithrespecttothecurrent-windowcost,
|     | g (x )| = | |a Cost (x )|+|c | (x ),   |     |     |
| --- | --------- | ---------------- | ------- | --- | --- |
|     | t 1:t     | t t t            | t 1:t−1 |     |     |
where a ≥ 0isaknowncoefficient(inallbudgetmodelsconsideredhere, a = 1)and
| t   |     |     |     | t   |     |
| --- | --- | --- | --- | --- | --- |
c dependsonlyontherealizedhistoryuptot−1andbudgetparameters(e.g.,cumula-
t
| tive/rollingcarry-overterms). | Hence,intheprimalstepwithfixedν, |                       |     | t   |     |
| ----------------------------- | -------------------------------- | --------------------- | --- | --- | --- |
|                               | ν g |                            | = |ν a Cost (x )|+|νc | ,   |     |     |
|                               | t t                              | t t t t               | t t |     |     |
andthetermνc isconstantwithrespecttox andcanbedroppedfromtheminimization.
| t t |     | t   |     |     |     |
| --- | --- | --- | --- | --- | --- |
∑N
Finally,sinceCost t (x t ) = cost(x ),thesurrogateobjectivedecomposesacrossVMs,
|     | i=1 | i,t |     |     |     |
| --- | --- | --- | --- | --- | --- |
yieldingtheper-VMselectionruleinEquation(11).
ThisexpressionreusestheexistingnotionsF ,andg (·). Fortherate-based,absolute
ρ t
cumulative, and rolling budget models, and for the incremental budget model when
writteninitsequivalentaffineform(Section3.7.3), g (·)isaffineinthecurrent-window
t
cost Cost t (x t ) given the realized cost history. Therefore, the augmentation in Equation
(10) introduces a linear cost pressure proportional to ν t at each decision window. The
dualvariablesν aretreatedasexogenousparametersduringtheprimaldecisionateach
t
window. TheBDalgorithmalternatesbetweenminimizingthissurrogatewithrespecttox
t
forfixedν,andupdatingν viaprojectedascentbasedontherealizedbudgetresidual,as
t t
detailedinAlgorithm1.
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302
21of48
Algorithm1BD(Budget-awareDual)Solver
Input:VMtypesetK,decisionhorizonT,previousassignmentx (orx given),workload
|     |     |     |     |     |     |     |     |     | 0 1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
statistics(µ )asdefinedinSection3.3,andabudgetfeasibilityfunction
|     |     | i,t,r ,q | i,t,r ,σ i,t,r | ,H i,t,r |     |     |     |     |     |     |     |
| --- | --- | -------- | -------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
g (·)fromSection3.7
t
|     | 1. Initializethedualvariable |     |     |     | ν ←0 |     |     |     |     |     |     |
| --- | ---------------------------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
1
|     | 2. Foreachdecisionwindowt |            |     |              | = 1,2,...,T: |     |     |     |     |     |     |
| --- | ------------------------- | ---------- | --- | ------------ | ------------ | --- | --- | --- | --- | --- | --- |
|     | 2.1                       | ForeachVMi |     | = 1,2,...,N: |              |     |     |     |     |     |     |
2.1.1Evaluatethelocalaugmentedobjectiveinducedbythesurrogateformula-
tioninEquation(10)
2.1.2SelecttheVMtypex accordingtotheper-VMdecisionruledefinedin
i,t
Equation(11),usingthemostrecentworkloadstatistics
(x )accordingtoSection3.2
|     | 2.2 | ComputetherealizedplatformcostCost |     |     |     |        | t t           |     |       |     |     |
| --- | --- | ---------------------------------- | --- | --- | --- | ------ | ------------- | --- | ----- | --- | --- |
|     | 2.3 | Updatethecosthistory{Cost          |     |     | (x  | ),Cost | (x ),...,Cost |     | (x )} |     |     |
|     |     |                                    |     |     | 1   | 1      | 2 2           |     | t t   |     |     |
|     | 2.4 | Evaluatethebudgetresidualg         |     |     | (x  | )      |               |     |       |     |     |
t 1:t
2.5 Updatethedualvariablebyprojectedascent
|     |     |     |     |     |     | (cid:18)(cid:104) |     |     | (cid:19) |     |     |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | -------- | --- | --- |
∼(cid:105)+
|     |     |     |     |     | ν ←min |     | ν +ηg | ,ν    | .   |     |     |
| --- | --- | --- | --- | --- | ------ | --- | ----- | ----- | --- | --- | --- |
|     |     |     |     |     | t+1    |     | t     | t max |     |     |     |
ν >0isafixedupperboundusedtopreventnumericalexplosionofthedual
max
variable.
|     | Output: sequentialresizingdecisions{x |     |     |     |     | }T  |     |     |     |     |     |
| --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t t=1
Under the per-window run-rate budget model defined in Section 3.7.1, the budget
residualbecomesstage-wiseseparableanddependsonlyonthecurrent-windowassignment:
rate_pw(x
|     |     |     |     | g   | ) =Cost | (x )−B |         | (t) |     |     |     |
| --- | --- | --- | --- | --- | ------- | ------ | ------- | --- | --- | --- | --- |
|     |     |     |     | t   | t       | t t    | rate_pw |     |     |     |     |
Inthiscase,theprimaldecisionperformedbyBDcanbeinterpretedasminimizing
theper-windowLagrangian
|     |          | (cid:16) |            |     |         |       |     | (cid:17) | rate_pw(x |     |     |
| --- | -------- | -------- | ---------- | --- | ------- | ----- | --- | -------- | --------- | --- | --- |
|     | L (x ,ν) | = Waste  | (x )+λOver |     | (x )+ρΣ | N I{x | ̸=  | x }      | +νg       | ),ν | ≥0  |
|     | t t      |          | t t        |     | t t     | i =1  | i,t | i,t−1    | t         | t   |     |
where ν represents the shadow price associated with the hard budget constraint. The
correspondingdualfunctionisdefinedas
|     |     |     |     |     | d (ν) = | min L (x | ,ν) |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | -------- | --- | --- | --- | --- | --- |
|     |     |     |     |     | t       | t        | t   |     |     |     |     |
xt ∈KN
which is concave in ν, since it is the pointwise infimum of affine functions of ν. For
any minimizer x (ν), a valid dual subgradient is given by the realized budget residual
t
rate_pw(x
|     | g t ). | Consequently,theupdateusedinAlgorithm1, |     |     |     |     |     |     |     |     |     |
| --- | ------ | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t
|     |     |     |     |        | (cid:16) | (cid:16) | ∼(cid:17) | (cid:17) |     |     |     |
| --- | --- | --- | --- | ------ | -------- | -------- | --------- | -------- | --- | --- | --- |
|     |     |     |     | ν =min | max      | 0,ν +ηg  | ,ν        | ,        |     |     |     |
|     |     |     |     | t+1    |          | t        | t         | max      |     |     |     |
can be interpreted as a projected dual subgradient-ascent step applied to the run-rate
Lagrangiandualproblem. Equivalently,thisupdateadmitstheinterpretationofavirtual-
∼
|     | queueupdate,wherethenormalizedresidualg |     |     |     |     | isdefinedinSection5.4. |     |     |     |     |     |
| --- | --------------------------------------- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- |
t
|     | Thepracticalconsequenceisthat,forafixedν,thewindow-leveldecisionreducesto |     |     |     |     |     | t   |     |     |     |     |
| --- | ------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
aper-VMtypeselectionrule. Usingtheper-resourceoverloadandwastequantitiesfrom
Section3.5,VMiatwindowtselects
|         | (cid:34) |       |           |       |             |     |       |         | (cid:35) |     |      |
| ------- | -------- | ----- | --------- | ----- | ----------- | --- | ----- | ------- | -------- | --- | ---- |
| ∈argmin | ∑ (waste |       | (k)+λover |       | (k))|+|ρI{k | ̸=  | }|+|ν | cost(k) |          |     |      |
| x i,t   | w r      | i,t,r |           | i,t,r |             | x   | i,t−1 | t       | ,        |     | (11) |
k∈K
r∈R
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 22of48
wherewaste (k)andover (k)denotethequantitiesdefinedinSection3.5,evaluatedby
i,t,r i,t,r
fixingx = kwhilekeepingallothercomponentsofx unchangedintheper-VMselection
i,t t
step;cost(k)followsSection3.2. Thisrulemakesexplicithowν convertsbudgetpressure
t
intoasimpleadditivebiastowardcheaperinstancetypeswhilepreservingtheexisting f
1
− f trade-offencodedbythefirsttwoterms.
2
5.4. TheBDAlgorithm
We now describe the online BD procedure that alternates between (i) selecting x
t
usingthecost-awareper-VMruleand(ii)updatingthedualvariablebasedontherealized
budgetresidual. Themethodoperatesinasliding-windowfashionconsistentwiththe
interpretationinSection3.8.3.
Thedualvariableisupdatedbasedontherealizedbudgetresidual,whichisnormal-
ized by a characteristic budget scale in practice to ensure dimensional consistency and
numericalstability. Thenormalizedresidualisdefinedas
∼ g t
g ,
t
B
ℛ ≔
where B denotes a characteristic budget scale associated with the active budget model.
Here, the realized budget residual is computed with respect to the post-gate deployed
configuration,ensuringthatthedualupdatereflectsexecution-levelfeasibilityratherthan
the raw candidate output. An additional upper projection ν is applied to prevent
max
numerical explosion and to ensure stable cost-aware behavior over long horizons and
undercumulativebudgetmodels,withtheconcretenormalizationusedintheexperiments
describedinSection6. TheresultingprimalstephascomplexityO(N|K|) perwindow,
since each VM evaluates a finite number of candidate types, enabling BD to maintain
practicalruntimesevenatlargeN,asexaminedinSection6.
5.5. TheoreticalPropertiesoftheDualVariable
Wesummarizetwokeypropertiesofthedualvariablethatmotivatetheexperimental
validation in Section 6.2. These properties are guided by the standard shadow-price
interpretation of Lagrangian multipliers and serve as design targets for the dual-based
solver. BecauseBC-VMRisadiscreteNP-hardcombinatorialproblem,wedonotclaim
thestatementsbelowasKKTguaranteesfortheoriginalprogram;rather,theydescribe
theexpectedshadow-pricebehaviorofthedual-controlsignalinducedbythesurrogate
primal–dualupdateinAlgorithm1andarevalidatedempiricallyinSection6.2.
Proposition1. Considertwobudgetsettingsthatdifferonlybyarelaxationofthebudgetlimits
in g (·) (i.e., the constraint becomes weakly easier to satisfy for all t). Then the corresponding
t
steady-statedualvariablelevelν∗ isexpectednottoincreaseunderthisrelaxation. Equivalently,
tighterbudgetstypicallyinducelargershadowprices,whilelooserbudgetstypicallyinducesmaller
shadowprices. Throughoutthisproposition,thebudgetresidualunderlyingνisinterpretedasthe
realizedresidualafterthecommoncompliancegate,sothatthedualvariableconsistentlyreflects
deployment-levelfeasibilityratherthancandidate-leveloutcomes.
ProofofProposition1. Underarelaxedbudget,anyresizingplanfeasibleunderthetighter
budget remains feasible, and the budget residual g (·) becomes weakly smaller for the
t
samecostsequence. Inthedualinterpretation,νmeasuresthemarginalbenefitofrelaxing
thebudgetconstraint;whentheconstraintisrelaxedexogenously,thismarginalvalueis
□
notexpectedtoincrease.
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 23of48
Proposition2. Ifthebudgetconstraintisinactive(i.e.,therealizedcostssatisfyg (·) < 0over
t
therelevanthorizon),thenthecorrespondingdualvariableisexpectedtoapproachzero,ν∗ ≈ 0;
conversely,astrictlypositivedualvariableindicatesthatthebudgetconstraintiseffectivelyactive.
Proof of Proposition 2. When the budget constraint is inactive, additional relaxation
provides no benefit. Hence the shadow price should be zero; otherwise, decreasing ν
□
wouldstrictlyimprovetheaugmentedobjectivewithoutharmingfeasibility.
Section6.2empiricallyvalidatesthesetwopropertiesbyexamininghowthemeasured
dualvariablerespondstosystematicbudgettightening/relaxationandwhetheritconverges
tonear-zeroinwell-fundedregimes.
5.6. MinimalPrimal–DualBoundsintheRun-RateCase
WenextanalyzethetheoreticalbehavioroftheBDupdateundertherun-ratebudget
model. RecallthatAlgorithm1performsaprojectedsubgradientascentsteponthedual
∼
variableν,wherethesubgradientcorrespondstothenormalizedresidual g definedin
t t
Section 3.7.1. This residual measures the instantaneous deviation between the realized
spendingrateandthepermittedrun-ratebudget. Theanalysisbelowcharacterizestwo
fundamentalpropertiesofthisupdaterule. First,thedualsequenceν achievesastandard
t
subgradientregretboundrelativetothebestfixeddualvalueinhindsight. Second,the
resultingprimaldecisionsexhibitvanishingaveragebudgetviolationovertime. These
guaranteesprovideaminimaltheoreticaljustificationthattheBDupdateactsasastable
budget-regulation mechanism in the run-rate regime. Formally, the following theorem
establishesregretandviolationboundsforthedualupdate.
Theorem 2. Under the continuous relaxation of the run-rate budget model (Section 3.7.1), and
assumingexactminimizationoftherelaxedper-windowprimalsubproblem,supposethatthenormalized
(cid:12)∼(cid:12)
residualsatisfies(cid:12)g (cid:12)≤Gforallt.Thenthedualiteratesν generatedbyAlgorithm1satisfy
(cid:12) t(cid:12) t
1 ν2 ηG2
T
[max 0≤ν≤νmax Σd t (ν)−Σd t (ν t )] ≤
2
m
η
a
T
x +
2
.
Moreover,thenormalizedtime-averageviolationmagnitudesatisfies
1 (cid:104)∼(cid:105) (cid:18) 1 (cid:19)
Σ g =O √ .
t
T + T
ProofofTheorem2. Underthecontinuousrun-raterelaxation,theupdateinAlgorithm
1correspondstoprojectedsubgradientascentappliedtotheconcavedualfunctiond (ν).
t
∼
Sinced (ν)isconcaveandthenormalizedresidualg isboundedbyG,theclassicalregret
t t
boundforprojectedsubgradientmethodsoverthecompactdomain[0,ν ]applies,which
max
(cid:16) (cid:17)
establishestheclaimedinequality.Choosingη= νm√ax yieldsanO √1 dualregretrate.The
G T T
sameprimal–dualargumentimpliesthatthetime-averageviolationmagnitudealsodecays
(cid:16) (cid:17)
atrateO √1 . Underthecontinuousrelaxation,thetime-averageobjectiveapproaches
T
□
therelaxedoptimumatthesamerate.
Theorem2appliesspecificallytotherun-ratebudgetmodelunderacontinuousrelax-
ation,wherethebudgetconstraintisstage-wiseseparableandthedualupdatecorresponds
toastandardprojectedsubgradientmethod. Fortemporallycoupledbudgetmodelssuch
astheabsolutecumulative,rolling,andincrementalbudgets,feasibilitydependsonthe
realizedcosthistoryandthestage-wiseseparabilityusedintheanalysisnolongerholds.
Consequently,wedonotclaimanalogousregretorviolationguaranteesforthosemod-
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 24of48
els. TheirbehavioristhereforeevaluatedempiricallyinSection6ratherthanestablished
throughformalguarantees.
6. ResultsandDiscussion
Thissectionevaluatestheproposedbudget-constrainedVMresizingframeworkand
theBDsolver. Theexperimentsaredesignedinfourstages. Inthefirststage,wevalidate
thefundamentaltheoreticalclaimsoftheframeworkbyempiricallyexaminingwhether
thedualvariableν exhibitsthemonotonicityandcomplementary-slackness-likebehavior
t
expected from the shadow-price interpretation in Section 5. This step ensures that the
Lagrangian-basedformulationoperatesasintendedwhenembeddedwithinadynamic
workloadenvironment. Inthesecondstage,weinvestigatethescalabilityandcomputa-
tionalcomplexityofBDbymeasuringitsexecutiontimeasthenumberofmanagedVMs
increasesfromtenstotensofthousands. Thisanalysisaddressesacriticalrequirementfor
real-worldapplicability,ashyperscalecloudplatformsmustperformresizingdecisions
withinstrictlatencybudgetsandcannotrelyonsolverswhoseruntimegrowssuperlin-
earlywiththesystemsize. ThethirdstagecomparesBDagainstseveralrepresentative
baselinealgorithms—Static,Greedy,PRG,andNSGA-II—undermultiplebudgetregimes.
Byevaluatingcostsaving, multi-objectiveutility, andbudgetfeasibility, weassesshow
effectively BD balances the core FinOps trade-offs between economic efficiency, perfor-
mance preservation, and budget compliance. Finally, in the fourth stage, we examine
therobustnessofBDwhentheunderlyingworkloadcharacteristicschange. Tothisend,
weconstructrepresentativeworkloadscenarioswithvaryingtemporalvariability. The
primary quantitative evaluation is conducted on a Typical workload, while additional
scenario-basedanalysesexaminetransient,sustained,andoscillatorydemanddynamics.
ThisstageevaluateswhetherBDmaintainsconsistentbehavioracrossdiverseoperating
conditionsorwhetheritsperformanceissensitivetothestructureofworkloadfluctuations.
6.1. ExperimentalEnvironment
AllexperimentsareconductedonaVMresizingsimulatorthatimplementstheopti-
mizationproblemdefinedinSection3. Thesimulatoroperatesinasliding-windowfashion.
For each time window, we compute for every VM the mean, 95th percentile, standard
deviation,andentropyofCPUandmemorydemand. Toensuredimensionalconsistency
withthecapacitytermscap (·)inSection3,ourworkloadgeneratorproducesabsolute
r
resource-demandsamplesd (l)(measuredinvCPUforr =cpuandGiBforr =mem).
i,t,r
Given an assigned type x , the corresponding utilization ratio is computed only
i,t
(cid:18) (cid:19)
forreportingandmonitoringpurposesasu (l) = min di,t,r (l) , 1 ,r ∈ {cpu, mem}.
i,t,r cap
r
(xi,t )
Importantly,allwindow-levelstatistics(µ ,q ,σ ,H )usedbythemodelarecom-
i,t,r i,t,r i,t,r i,t,r
puted from the absolute demand samples d (l) and therefore do not depend on the
i,t,r
chosen VM type x ; u (l) is not used in any objective, constraint, or gate evaluation.
i,t i,t,r
Basedonthesestatistics,itselectsonespecificationfromafinitepoolofVMtypes. Each
specificationischaracterizedbyitsvCPUcount,memorycapacity,andanhourlyprice
normalizedfromthepricetableofapubliccloudprovider. Inourimplementation,the
VM-typepoolspansfrom1vCPU/1GiBto16vCPU/32GiBandisorderedbyincreasing
cost. Thepoolfollowsacoarse-grainedprogressionatthelowendandincludesasmall
numberofmid-tierdiagonaltypesthatscaleCPUandmemoryasymmetrically,preventing
thefeasiblesetfromdegeneratingtoasinglespecificationundertransientworkloadshifts.
TheimplementationiswritteninPython3.xandrunsonthesameserveracrossallexperi-
ments(IntelXeonSilver-classCPUwith64GBofRAM),sothatexecutiontimesofdifferent
algorithms are directly comparable. At the beginning of window t, we compute work-
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 25of48
loadstatisticsfromtheimmediatelyprecedingwindowt−1andchoosetheassignment
x accordingly.
t
Intheexperimentalevaluation,theworkload-dependentamplificationfactorω(σ,H)
isinstantiatedusingalightweightboundedadditiveform. ForeachVMi,windowt,and
resourcer,weset
(cid:26) (cid:27)
σ
ω =1+β ·min 1,| i,t,r +β ·H
i,t,r 1 capmax 2 i,t,r
r
where H ∈ [0,1]isthenormalizedentropydefinedinSection3. Thisinstantiationis
i,t,r
monotonein σ and H, boundedfornumericalstability, and dependsonlyonobserved
workloadstatistics(notonthechosenVMtype).Theadditivestructureisusedintentionally
ratherthanasanarbitraryconvenience. Itpreservesadirectinterpretationofβ andβ as
1 2
separateamplificationstrengthsforvolatilityandirregularity,whileavoidingtheinstability
thatcanarisefrommultiplicativeinteractionswhenbothsignalsaresimultaneouslylarge.
The coefficient β controls sensitivity to workload volatility (intra-window variability),
1
while β controlssensitivitytoworkloadirregularitycapturedbyentropy. Inallexperi-
2
ments,wefix β = 0.3and β = 0.4togiveslightlymoreweighttoirregularitythanto
1 2
short-termvariance,whilekeepingtheamplificationboundedandeasytointerpret. This
choiceensuresmonotonicriskamplificationandnumericalstability,consistentwiththe
monotonicityandboundednessrequirementsdescribedinSection3.5.1.
6.1.1. Behavior-DrivenWorkloadGeneration
Toevaluatetheresizingframeworkunderrealisticanddiverseoperatingconditions,
weemployabehavior-basedworkloadgeneratorthatproducesdetailedCPUandmemory
timeseriesforeveryvirtualmachine. Ratherthanassumingasimpleaverageutilization
level,thegeneratorexplicitlyconstructstemporalpatternsthatreflecthowcloudservices
varyovertime. Fourbehaviortypesareimplemented,capturingawiderangeofdemand
dynamicsobservedinpractice.
Thefirsttype,referredtoasthestaticpattern,modelsservicewhoseresourceusage
remainsnearlyconstant.Forthesevirtualmachines,eachsampleinthetimeseriesisdrawn
fromanarrowGaussiandistributionaroundafixedmean,resultinginwindowsthatexhibit
lowvarianceandstablep95values. Thispatternservesasabaselineforunderstanding
howthealgorithmsbehavewhendemandispredictable.
The second type corresponds to ramp-up and ramp-down behaviors. Here, the
workloadgraduallyincreasesordecreasesbyinterpolatingbetweenasampledstartlevel
andasampledendleveloveraconfigurablenumberofintervals. Oncethetransitionis
completed,theworkloadeitherstabilizesatthenewlevelorfluctuatesmildlyaroundit.
Thisformofcontrollednon-stationarityintroduceswindowsinwhichmeandemandand
p95evolvecontinuously,therebytestingwhetherthesolverreactssmoothlytogradual
demandshifts.
Thethirdtypeistheidle-burstbehavior,designedtocaptureapplicationsthatspend
longperiodsatverylowutilizationbutoccasionallyexperienceintensedemandspikes.
The generator creates alternating idle and burst segments, drawing idle samples from
anarrowdistributionnearzeroandburstsamplesfromadistributionwithbothhigher
meanandlargervariance. Becausethedurationandmagnitudeofburstsarerandomized,
theresultingtimeseriescontainssuddenpeaksthatincreaseentropyandwidenthegap
betweenmeanandp95. Thispatternstressestheresizinglogicbyforcingittobalancelong
idleperiodsagainstrarebutcriticalbursts.
Thefourthtype,periodic-burst,introducesregularcyclicspikes. Thegeneratorcon-
structsrepeatingcycles,eachconsistingofanidlephasefollowedbyaburstphase. Since
thecyclelengthandburstdurationfollowconsistentvaluesacrossrepetitions,theresulting
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 26of48
workloadexhibitspredictableoscillations. Thisallowsustoexaminewhetherthesolver
canexploitperiodicstructuretoanticipatefuturedemandratherthanreactingsolelyto
instantaneousfluctuations.
Demandtracesaregeneratedinabsoluteunits(vCPUandGiB)byscalingeachbehav-
ior’sutilizationratiosbytheglobalcapsofthetypeofpool(16vCPUand32GiB).Static
tracesfollowaGaussianmodelwithlowmeanandsmallvariance,whileramp-up/down
traceslinearlyinterpolatebetweensampledstartandendlevelsandthencontinuewith
mildnoise. Burst-typetracesalternatebetweenidlesegmentsandhigh-demandsegments:
idle-burstusesirregularburstintervalsanddurations,whereasperiodic-burstrepeatsa
fixedperiodwithashortburstphase. Acrossallbehaviortypes,CPUandmemorytraces
aregeneratedindependentlyusingthesametemplateandthenscaledtoeachVMcapacity
units. For monitoring, utilization ratios are capped at 1, while the underlying demand
samplesremainunclipped. Thesimulatorcomputesper-windowstatistics(mean,standard
deviation,95thpercentile,andentropy)fromthesedemandtraces,andthesewindow-level
statisticsarefedintotheobjectivetermsandfeasibilitychecks,influencingoverload-risk
evaluationandheadroomrequirements. Byassigningheterogeneousbehaviortypesacross
VMsandrandomizingbursttiming,rampduration,amplitude,andnoiselevels,theaggre-
gateworkloadspansbothsmoothandhighlyvolatileregimes,exercisingresizingdecisions
understeadydemand,gradualtransitions,abruptspikes,andperiodicfluctuations.
Unlessotherwisestated,theworkloadgeneratorsamplesitsparametersfromfixed
rangesthataresharedacrossallexperiments. Burstintervalsaredrawnuniformlyfrom
5 to 60 min, burst durations from 5 to 30 min, and burst amplitudes from 0.6 to 1.2 of
the VM capacity. Ramp-up and ramp-down traces use ramp lengths between 30 and
120min,whileGaussiannoiseisaddedwithastandarddeviationofatmost10%ofthe
meandemandlevel. Forscenarioconstruction,theworkloadmixtureisfixedperscenario:
theSteadyworkloadconsistsentirelyofstatictraces,theTypicalworkloadusesamixture
of50%static,30%ramp(20%ramp-upand10%ramp-down),and20%idle-bursttraces,
andtheBurstyworkloaduses30%ramp,50%idle-burst,and20%periodic-bursttraces.
6.1.2. ExperimentalBudgetConstraints
Budgetconstraints are modeledprimarilyusing twoof thefour budget modelsin
Section3.7: therun-ratebudgetB andtheabsolutecumulativebudgetB . The
rate_pw abs_cum
strengthofthebudgetiscontrolledbyascalarmultiplierαappliedtoacalibratedbase
budgetB :
0
B(α) = α·B .
0
ThebasebudgetB iscalibratedonceusingtheStaticpolicyonareferenceworkload
0
realizationandisthenheldfixedacrossallevaluationrunsandrandomseeds. Thisdesign
reflects practical FinOps settings in which budgets are specified in advance based on a
reference calibration run and are not adjusted to each realized workload trace. Conse-
quently, even the Static policy may violate the nominal budget level under α = 1.0 on
somerealizations.
Fortherun-ratebudget,thebaseleveliscalibratedfromthepeak(maximum)per-
windowcostobservedundertheStaticpolicyinthecalibrationrun.
(cid:16) (cid:17)
Brate maxCost xstatic , B = α·Brate.
0 t rate_pw 0
t
ℛ ≔
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 27of48
Intheabsolutecumulativemodel,theentirebudgetallowanceisavailablefromthe
beginning of the horizon and is consumed cumulatively over time, rather than being
releasedaccordingtoapredefinedtrajectory.
T (cid:16) (cid:17) T
Bcum ∑ Cost xstatic , ∑ Cost (x ) ≤ α·Bcum.
0 t t t 0
t=1 t=1
ℛ ≔
Fortheincrementalbudget,weuseatime-invariantper-windowincrementcapover
thehorizon B (t) α·Binc forall t ≥ 2. BecausetheStaticpolicykeepsconfigura-
inc_cum 0
tionsfixedandwouldyieldadegeneratezeroincrementunderdirectcalibration,weset
ℛ ≔
Binc Brate(thecalibratedpeakper-windowspend)asacommonreferencescale. Withthis
0 0
choice,themultiplierαdirectlycontrolstheallowedrelativegrowthperwindowunderthe
ℛ ≔
incrementalbudgetmodel.
ForthedualupdateintheBDsolver,weuseanormalizedbudgetresidualtoobtaina
dimensionlessquantity. Specifically,therawresidualg ,definedinSection3.7,isscaledby
t
acharacteristicbudgetlevelas
g ∼ := g t ,B ∈ (cid:8) Brate,Bcum(cid:9) .
t 0 0
B
Here, B denotes the calibrated base budget corresponding to the active budget
model (run-rate or absolute cumulative). This normalization ensures dimensional con-
sistency of the dual variable and improves numerical stability across different budget
modelsandbudgetmagnitudes. Fortheincrementalbudget,wereuse B = Brate = Binc
0 0
fornormalization.
Inallexperiments,weuseafixedstepsizeη =1.0forthedualupdate. Becausethe
budgetresidualisnormalized,asinglestepsizewassufficienttoobtainstablebehavior
acrossallbudgetmodels.
Wesweepα ∈ {0.1,0.2,...,1.0}tostudytheeffectofbudgetstrength. Unlessstated
otherwise,allreportedresultsareobtainedfromthisfullαsweep. Becausethebudgetis
fixedacrossrealizations,thislevelmaystillbeinsufficientforsomeworkloadtraces,and
constraintviolationscanpersist. Therun-rateandabsolutecumulativemodelsareused
ascanonicalextremesinthemainexperiments;weadditionallyincludetheincremental
cumulativemodelinSection6.3tocontrastgrowth-limitingpolicieswithabsolutespending
caps,whiletherollingmodelisdiscussedinSection6.2.
6.1.3. BaselineAlgorithmsandProposedSolver
SinceBC-VMR(ρ)isNP-hardevenunderhighlysimplifiedsettings(Section4),we
focusonscalableheuristicanddual-basedsolversratherthanexactoptimization. Accord-
ingly, the baselines include lightweight heuristics and a meta-heuristic (NSGA-II) that
approximatestheParetofrontbutisnotintendedforreal-timedeployment. Underthis
setting,weevaluateatotaloffiverepresentativealgorithmsthatreflectdifferentdesign
trade-offsbetweenoptimality, scalability, andoperationalpracticality. TheStaticpolicy
keepstheinitialspecificationforeachVMthroughouttheentirehorizonandservesasa
QoSupperboundthatignorescostandbudget. Greedyisasimpledownsizing-onlyheuris-
ticthat,ineachwindow,selectsalower-costVMspecificationwhendoingsoimproves
thesizing-qualityobjective;itdoesnotexplicitlyincorporatethebudgetconstraintduring
candidategeneration. BDistheproposeddual-variablesolver. ProportionateRatioGreedy
(PRG) selects VM specifications based on a utility-to-cost ratio, and likewise generates
candidateswithoutdirectlyenforcingthebudgetconstraint. Ateachwindow,Greedyand
PRGgeneratecandidatesindependentlyforeachVMbasedonlyonthecurrentwindow
statistics. Neitherbaselineenforcesthebudgetconstraintduringcandidategeneration;
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 28of48
budgetfeasibilityisapplieduniformlyafterwardthroughthecommoncompliancegate.
Tiesarebrokendeterministicallybyselectingthelowest-costspecification. NSGA-IIisa
multi-objectiveevolutionaryalgorithmandactsasanoptimization-qualitybaselinerather
than a practical online policy. At each decision window t, NSGA-II searches over the
currentassignmentvectorx (onegeneperVMrepresentingtheselectedtype),evaluates
t
theobjectivesusingthewindow-levelstatisticsfromt−1,andcomputesthestabilityterm
based on whether each VM changes relative to its previous assignment x i,t−1 ; the best
feasibleindividual(ifany)isusedasthecandidatedecisionbeforeapplyingthecommon
compliancegate. ForscalabilityexperimentsweonlyconsiderBD,Greedy,andNSGA-II
becausetheyrepresent,respectively,theproposedsolver,averylightweightheuristic,and
aheavybutpowerfulmeta-heuristic.
Allalgorithmsoperateonlineanduseonlystatisticscomputedfromthemostrecent
completed window. For evaluation, we apply the common compliance gate described
abovetothecandidatedecisionproducedbyeachmethod. Concretely,whenthecandidate
violatesthebudgetwhileafeasibleassignmentexists,thegatedeterministicallyrepairs
thecandidateby(i)keepingthecurrentspecificationwhenitisalreadybudget-feasible,
(ii)otherwisereplacingthehighest-costVMassignmentswiththegloballycheapesttypes
intheVM-typepool,and(iii)ifneeded,iterativelydownsizingtheremaininghighest-cost
VMs until the total cost satisfies the constraint. For NSGA-II, the candidate is chosen
byfeasibility-firstselectionwithinthenondominatedset(thebestfeasibleindividualif
oneexists);theselectedcandidateisthenalsopassedthroughthesamecompliancegate
toensurethatfeasibilityisinterpretedidenticallyacrossallmethods. Unlessotherwise
stated,NSGA-IIusesthefixedsettinginTable3(pop =50,gen =50, p =0.7, p =0.3),
c m
correspondingto2500fitnessevaluationsperdecisionwindow,withnoearlystoppingor
wall-clocktruncation.
6.1.4. EvaluationProtocol
To avoid ambiguity between a candidate decision and the final deployable action,
we evaluate every method using the same two-step protocol in each decision window.
First,thealgorithmproducesacandidateassignmentbasedonthemostrecentworkload
statistics. Second,thecandidateispassedthroughacommonbudget-compliancegatethat
checkstheactivetemporalbudgetpolicy. Ifthecandidateviolatesthebudgetbutafeasible
assignmentexistswithinthediscreteVM-typepool,thegatedeterministicallyrepairsthe
decisionbyprogressivelyreducingcostwhilepreservingthealgorithm’sintentasmuch
as possible (see the deterministic procedure in Section 6.1.3). If no feasible assignment
existsforthatwindowunderthegivenbudgetandVM-typepool(i.e.,theactivebudgetis
violatedevenbythelowest-costassignmentintheVM-typepool),thedecisionismarkedas
structurallyinfeasibleandtherepairedactionbecomesthelowest-costassignmentavailable;
anyremainingoverspendisthenunavoidablebydefinition. Unlessstatedotherwise,all
reportedmetricsarecomputedfromthefinalpost-gatedecisions,sincethesecorrespond
to what would actually be executed in an operational controller. This gate is applied
immediatelyaftereachalgorithmproducesitscandidatedecisionforwindowtandbefore
anycostaccumulation,budget-residualevaluation,ormetriccomputation.
6.1.5. PerformanceMetrics
Wereportthreeprimarymetricsthroughouttheexperiments.
Cost Saving is defined as the percentage reduction in the time-weighted total cost
relativetotheStaticpolicy. Thismetricdirectlyquantifiestheeconomicbenefitachieved
underbudgetconstraints.
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302
29of48
Budget Violation Rate (post-gate) is defined as the fraction of decision windows in
whichthefinaldecisionafterthecommoncompliancegatestillviolatestheactivebudget
constraint. Thismetricreflectsdeployment-levelfeasibility. Fordiagnosticpurposes,we
also report the Candidate Violation Rate (pre-gate), defined as the fraction of windows
inwhichthecandidatedecisionviolatesthebudgetwhenevaluatedbeforethegate(i.e.,
g t (·) >0onthecandidate).Finally,theStructuralInfeasibilityRateisthefractionofwindows
in which even the minimum-cost assignment in the discrete VM-type pool violates the
cap,inwhichcaseanypost-gateoverspendisunavoidablebydefinition. Unlessstated
otherwise,costsavingandstabilitymetricsarecomputedfrompost-gatedecisions.
Operational Stability is measured using the change rate, defined as the fraction of
virtualmachineswhoseassignedtypediffersfromthepreviouswindowafterapplying
the compliance gate. This metric captures operational churn associated with resizing
actionsandreflectsmigrationoverheadandpotentialservicedisruption. Changeratesare
computedwithrespecttothefinalpost-gatedeployedconfigurations,ensuringconsistency
withexecution-levelfeasibilityandtheevaluationprotocolinSection6.1.4.
Foreachconfiguration,werun10independentrandomseedsandreportmean±standard
deviation.Unlessotherwisestated,allalgorithmsareevaluatedusingthesameseedset.Table3
summarizestheexperimentalconfigurationandhyperparametersusedacrossSections6.2–6.4.
Table4liststhediscreteVM-typepoolusedinourexperiments,includingvCPUcount,memory
size(GB),andper-hourprice(normalizedunits).PricesinTable4arenormalizedbydividing
rawhourlypricesbythecheapesttypepriceandscalingtointegerunitsforreadability;all
budgetsarecalibratedinthesamenormalizedunits.Whilewefixthismonitoringgranularity
for controlled comparison, the formulation and simulator directly support finer sampling
(largerL)withoutchanginganyalgorithmiccomponent.
Table 4. Discrete VM-type pool K used in the simulator (15 types) with per-hour price p
k
(normalizedunits).
| vCPUc | vMemory(GB)m |     | Price/hp |     |
| ----- | ------------ | --- | -------- | --- |
| k     |              | k   |          | k   |
| 1     | 1            |     | 60       |     |
| 2     | 2            |     | 100      |     |
| 2     | 3            |     | 130      |     |
| 2     | 4            |     | 160      |     |
| 4     | 8            |     | 300      |     |
| 4     | 16           |     | 420      |     |
| 6     | 16           |     | 520      |     |
| 8     | 16           |     | 600      |     |
| 10    | 20           |     | 720      |     |
| 10    | 24           |     | 820      |     |
| 12    | 24           |     | 880      |     |
| 12    | 28           |     | 1000     |     |
| 14    | 28           |     | 1080     |     |
| 14    | 32           |     | 1160     |     |
| 16    | 32           |     | 1200     |     |
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 30of48
6.2. TheoreticalValidation
6.2.1. MonotonicityandComplementarySlacknessoftheDualVariable
Thissectionverifieswhetherthetheoreticalpropertiesofthedualvariableνderived
in Section 5 are indeed observed in the simulator. Specifically, we assess whether the
empiricallymeasuredsteady-stateduallevelν∗ decreasesmonotonicallyasthebudgetis
relaxed,andwhetherν∗ approacheszerowhenthebudgetconstraintbecomesinactive.
Unlessstatedotherwise,ν*iscomputedasthemeanofν afterdiscardingtheinitial20%of
t
windowsasaburn-inperiod. Allworkload,cost,andspecificationsettingsarefixed;only
thebudgetmultiplierαisvariedfrom0.0to1.0inincrementsof0.1. Ineachrun,theBD
algorithmupdatestheper-windowdualvariableν,andwerecordthemeanofν overthe
t t
remainingwindowsasν*. Atthesametime,wemeasurethepre-gateconstraintviolation
rateasthefractionofdecisionwindowsinwhichthecorrespondingbudgetconstraintis
violatedwhenevaluatedonthecandidatedecision,i.e.,g (·) >0.
t
Fortherun-ratebudget,Figure1reportstheempiricallymeasuredsteady-statedual
level ν* together with the candidate (pre-gate) budget violationrate as functions of the
budgetmultiplierα. Undertightbudgets,ν*remainsextremelylarge,andthecandidate
violation rate is high, indicating strong budget pressure. As α increases, ν* decreases
monotonically,consistentwiththeshadow-pricemonotonicityintuition(∂ν ≤0).
∂B
Figure1.Duallevelandcandidatefeasibilityundertherun-rate(per-window)budget.Steady-state
duallevelν*(shadowpriceofbudgetpressure)andcandidate(pre-gate)budgetviolationrateas
functionsofthebudgetmultiplierαundertherun-ratebudgetmodelBrate_pw. αcontrolsbudget
strictness(smallerα=tighterbudget).Dualaxisusesalogscale.
Aroundα ≈ 0.6,thecandidateviolationraterapidlydropstonearzero,indicating
thatmostcandidatedecisionsbecomefeasible. Thisfeasibilitykneeisconsistentwiththe
structuralinterpretationdiscussedinSection4: oncethebudgetbecomeslargeenoughto
accommodatethelowest-costassignmentintheVM-typepool,feasiblecandidatedecisions
becomeavailableandviolationratescollapserapidly. Inlockstep,ν∗ decreasesbyseveral
ordersofmagnitudeandconvergestowardzero,whichisempiricallyconsistentwiththe
complementary-slacknessintuition
ν·g(x) =0,
suggesting that the dual variable tends to become negligible when the corresponding
constraintbecomesinactive. Inthislow-α(tight-budget)regime,asubsetofwindowscan
bestructurallyinfeasibleunderthediscreteVM-typepool(i.e.,eventheminimum-costas-
signmentviolatesthecap),inwhichcasepost-gateoverspendisunavoidablebydefinition;
accordingly,weusethecandidate(pre-gate)violationcurvehereasadiagnosticofprimal-
dualbehavior,whiledeployment-levelfeasibilityisassessedusingpost-gateoutcomesin
Section6.3. Practically,Figure1showsthatBDdoesnotimposeunnecessarythrottlingin
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 31of48
well-fundedregimes: oncethebudgetbecomessufficientlyrelaxed,thealgorithmdrives
thepenaltytowardzeroandstopsinterferingwiththeprimaldecisions.
Figure2presentsthesamevalidationfortheabsolutecumulativebudgetmodel. We
againplotthesteady-stateduallevelν∗ andthecandidate(pre-gate)budgetviolationrate
as functions of α. In contrast to the run-rate budget, the violation rate decreases more
gradually as α increases, reflecting the history-coupled nature of cumulative feasibility
underafixedex-antecalibratedcap. ConsistentwithProposition1, ν∗ decreasesasthe
budget is relaxed, remaining large while the cumulative constraint is frequently active.
Onceαreachesthepointwherethecumulativeconstraintbecomeseffectivelyslack(near
α = 1.0inthissweep),theviolationrateapproacheszeroand ν∗ collapsestowardzero
byseveralordersofmagnitude. Thisindicatesthatthemonotonicitybehaviorofthedual
variableisnotonlyobservedintherate-basedmodelbutalsounderstructurallydifferent
temporalbudgetformulations.
Figure2.Duallevelandcandidatefeasibilityundertheabsolutecumulativebudget.Steady-state
duallevelν∗andcandidate(pre-gate)budgetviolationrateversusαundertheabsolutecumulative
budgetmodelB ,illustratinghistory-coupledfeasibilityandthecorrespondingdecayofν∗as
abs_cum
theconstraintbecomesslack.
Applying the same α-sweep procedure to additional budget variants yields quali-
tativelyconsistentbehavior. Inparticular,theincrementalcumulativemodelreinforces
the same monotonic trends while adding a distinct growth-limiting perspective to the
comparison. For the main empirical trade-off analysis, however, we focus on the per-
window run-rate, absolute cumulative, and incremental cumulative budgets, because
thesethreefamiliesprovidetheclearestrepresentativecontrastsamonglocalspending
caps,long-horizoncumulativelimits,andupsizing-drivengrowthconstraints. Wetreat
therolling-budgetvariantonlyasasupplementarydiagnosticratherthanasaprimary
comparison axis, which keeps the main comparison focused while still supporting the
broaderapplicabilityoftheframework. Acrosstheadditionalvariants,relaxingthebudget
drivesthedualvariabletowardzeroandreducestheviolationrate,whereastighteningthe
budgetincreasesboththedualvariableandbudgetpressure,consistentwiththemono-
tonictrendsobservedundertherun-rateandabsolutecumulativemodels. Overall,these
resultsreinforcethesamequalitativepicturecapturedbythemaincomparisonfamilies
andsupportthetheoreticalfoundationsoftheproposedframework. Thisdiagnosticfo-
cusesoncandidatepre-gateviolationstorelatedual-variablebehaviortobudgetpressure;
deployment-levelfeasibilityisreflectedbythepost-gateoutcomediscussedinSection6.1.5.
6.2.2. ScalabilityAnalysis
This section examines the computational scalability of the resizing algorithms as
the fleet size increases. We vary the number of VMs N from 50 to 10,000 and measure
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 32of48
theruntimerequiredbyBD,Greedy,andNSGA-IItocomputeresizingdecisionsunder
identicalhardwareandsoftwareconditions.
Figure3summarizesruntimescalabilitybyplottingtheper-decisionexecutiontime
against fleet size N ∈ {50,...,10,000} on log–log axes. For each N, we report both
the average and the 95th-percentile (p95) wall-clock runtime across repeated runs, so
that the figure not only captures typical decision latency but also tail-latency behavior
relevant to real controllers. The magnitude gap is already visible at small scales: at
N =50,NSGA-IIrequiresontheorderof∼103msperdecision(avg;p95slightlyhigher),
whereasBDremainsaroundafewmillisecondsandGreedystaysbelow1ms. AsNgrows,
this separation widens rather than collapses. At N = 1000, NSGA-II rises to roughly
∼104ms,whileBDisstillonlytensofmillisecondsandGreedyremainswithinthesingle-
digitmillisecondsrange. AtthelargestscaleN =10,000,NSGA-IIreachesapproximately
∼ 105 ms, whereas BD stays around ∼ 102–103 ms and Greedy around ∼ 101–102 ms,
yieldingapersistenthightwo-digittolowthree-digitadvantageofBDoverNSGA-IIeven
athyperscale.
Figure3. ExecutionTimeversusNumberofVirtualMachines. Per-decisionwall-clockruntime
versusfleetsizeN(log–logaxes)forBD,Greedy,andNSGA-II.Linesreportaverageandp95decision
latencyacrossrepeatedrunsunderidenticalhardware/softwaresettings.
Two trends stand out from these concrete values. First, NSGA-II exhibits a steep
growthcurveasNincreases,reflectingtheinherentcomputationalburdenofevolutionary
multi-objective search over an N-dimensional discrete assignment vector. Second, BD
scales much more gently and remains close to linear growth, consistent with the per-
windowcomplexityO(N|K|)inducedbytheper-VMselectionruleinEquation(11)and
thelightweightdualupdate. TheGreedyheuristicremainsthefastestamongthethree,
butitsslopegrowsmorenoticeablywith NthanBD,whilestillremainingfarbelowthe
evolutionarybaseline. Importantly,thegapbetweenaverageandp95runtimesissmallfor
BDacrossthesweep,indicatingstableexecutiontimeandlimitedtail-latencyamplification
evenatlargescales. Overall,Figure3demonstratesthatBDmaintainspracticaldecision
latencyatfleetsizeswhereNSGA-IIbecomescomputationallyprohibitive,underscoring
BD’ssuitabilityforlarge-scaleVMresizingscenarioswhilepreservingasubstantialruntime
advantageacrossthetestedrange.Accordingly,Figure3shouldbeinterpretedasafleet-size
scalabilityresultunderafixedVM-typepool(|K| =15),afixeddecisionhorizon(T =18),
andfixedNSGA-IIsettings(pop =50,gen =50,i.e.,2500fitnessevaluationsperdecision
window). Itisnotintendedasabudget-equalizedcomparisonacrosssolverparadigms. We
alsodonotmodelexplicitmigrationlatency,control-planeoverhead,ormemoryfootprint;
thecurrentresultsshouldthereforebereadascontroller-leveloptimizationevidencerather
thananend-to-enddeploymentstudy.
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302
33of48
Beyondfleetsize,VMresizingdecisionsinpracticearealsoinfluencedbythesizeofthe
availableVM-typepool|K|andthetemporalplanninghorizonT.
Thesetwodimensions
influenceboththecomputationalscalabilityofthecontrollerandtheefficiencyoffeasible
assignmentswithinthediscreteconfigurationspace. Wethereforefurtherexaminehow
BDbehavesas|K|and T vary,andhowthegranularityoftheVM-typepoolaffectsthe
efficiencyoffeasibleconfigurations.
Table5showsthattheper-windowruntimeofBDgrowspredictablywith|K|.
Atthe
baselinehorizon T = 18,increasingthepoolsizefrom |K| = 6to10and15raisesthe
meanruntimefrom14.65±0.73to19.92±0.68and26.71±0.80ms/window. Bycontrast,
atthebaselinepoolsize|K|=15,increasingthehorizonfromT =9toT =36changesthe
per-windowruntimeonlymodestly,from26.51±1.36to28.42±1.59ms/window,whereas
thetotalhorizonruntimegrowsfrom238.55±12.26to1022.99±57.35ms.
Thisbehavioris
consistentwiththeO(N|K|)per-windowstructureimpliedbyEquation(11)andwiththe
onlinesliding-windowimplementationofBD.
Table5.ComputationalscalabilityofBDwithrespecttoVM-typepoolsizeanddecisionhorizon.
Runtime Runtime
|K|
| Configuration |     | T             |              |
| ------------- | --- | ------------- | ------------ |
|               |     | (ms/Window)   | (ms/Horizon) |
| Baseline      | 15  | 18 26.71±0.80 | 480.71±14.46 |
14.65±0.73 263.67±13.22
| ReducedVM-typepool  | 6   | 18            |              |
| ------------------- | --- | ------------- | ------------ |
| ModerateVM-typepool | 10  | 18 19.92±0.68 | 358.51±12.27 |
| ShortHorizon        | 15  | 9 26.51±1.36  | 238.55±12.26 |
28.42±1.59 1022.99±57.35
| LongHorizon           | 15  | 36            |              |
| --------------------- | --- | ------------- | ------------ |
| Smallpool+longhorizon | 6   | 36 14.90±0.65 | 536.53±23.40 |
Table6examinesthestructuralimpactofVM-poolgranularity. Usingidenticalwork-
loadsnapshots,wecomputethecheapestfeasibleassignmentavailablewithineachcandi-
dateVM-typepool. Relativetothefullpool(|K| =15),reducingthepoolto|K|=10 and
|K|=6 increasestheoraclefeasible-costgapto8.08±0.63%and11.17±1.06%,respectively,
whiletheexcessnormalizedslackgaprisesto3.70±0.35%and4.83±0.29%. Theinfeasible
snapshotrateremains28.92±3.65%acrossalltestedpoolsbecauseeachsub-poolretains
themaximum-capacityVMtype. Consequently,theeffectofpoolgranularityappearsnot
inbinaryfeasibilitybutintheefficiencyoffeasibleassignments.
Table6.StructuralimpactofVM-typepoolgranularity.
| OracleFeasible | CostGapvs. | ExcessSlack | Infeasible |
| -------------- | ---------- | ----------- | ---------- |
|K|
| Cost/Snapshot   | FullPool(%) | Gap(%)    | SnapshotRate(%) |
| --------------- | ----------- | --------- | --------------- |
| 6 835.79±21.56  | 11.17±1.06  | 4.83±0.29 | 28.92±3.65      |
| 10 823.67±21.08 | 8.08±0.63   | 3.70±0.35 | 28.92±3.65      |
| 782.15±24.00    | 0.00±0.00   | 0.00±0.00 | 28.92±3.65      |
15
Taken together, these results indicate that the resizing framework maintains pre-
dictablecontroller-levelscalabilitywithrespectto|K|andT,whilethediscreteVM-type
poolintroducesmeasurablediscretizationlosswhenthepoolbecomescoarse.
6.2.3. Primal–DualLowerBoundandRelaxation-to-IntegerGap
Toconnecttherelaxation-basedboundsinSection5.6totheoriginaldiscretedecisions
of BD, we quantify a primal–dual lower bound in the run-rate model and report the
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 34of48
associatedrelaxation-to-integergap. Letd (ν)denotetherun-ratedualfunctionintroduced
t
inSection5.3,andlet
N
ℓ t (x t ) Waste t (x t )+λOver t (x t )+ρ
∑I{x
i,t ̸= x i,t−1 }
i=1
ℛ ≔
denotethecorrespondingper-windowprimalobjectiveinEquation(9). Weapproximate
the dual lower bound d∗ t = max 0≤ν≤νmax d t (ν) via a simple 1D grid search over ν (log-
spaced),whichisinexpensivebecausetheinnerminimizationreusesthesameper-VMscan
overKasEquation(11). Wethenreporttherelativeprimal–dualgapforBD(candidate
decisions)as
ℓ (x )−d∗
Gap (%) =100× t t t ,
t max[1,|d∗|]
t
andsummarizethemean/medianofGap overwindowsandseeds. Wereportthismetric
t
onlyforwindowsthatarenotstructurallyinfeasibleundertherun-ratebudget. Across
thesewindows,95.29%ofGap valuesareexactly0%(p99=23.18%),indicatingthatthe
t
duallowerboundistypicallytightinthefeasiblerun-rateregime.
6.3. Budget-AwarePerformanceTrade-Offs
Thissectionevaluatesbudget-awareperformancetrade-offsonarepresentativeTypi-
calworkloadusingthreetemporalhard-budgetmodels: (a)absolutecumulativeB ,
abs_cum
(b) per-window run-rate B , and (c) incremental cumulative B . The Typical
rate_pw inc_cum
workloadcombinesstaticdemandwithramptransitionsandintermittentbursts,reflecting
realisticmixeddynamics. Wecomparefouronlinealgorithms—Static,Greedy,PRG,and
theproposedBD—undertenrandomseeds. Wesetρ =10toemphasizeresizingstability
bypenalizingfrequentconfigurationchanges. Wesweepthecommonbudgetmultiplier
α ∈ {0.1,0.2,...,1.0}. Unlessstatedotherwise,costandstabilitymetricsinthissectionare
computedfromthefinalpost-gatedecisionsproducedbythecommoncompliancegate
(Section6.1.4). Forbudgetfeasibility,wereporttheCandidateViolationRate(pre-gate)to
quantifyhowstronglyeachmethodinternalizestheactivebudgetpolicy.
We focus the main comparison on the per-window run-rate budget, the absolute
cumulativebudget,andtheincrementalcumulativebudgetbecausethesethreefamilies
providetheclearestrepresentativecontrastsamongtemporalhard-budgetsemantics. The
per-windowrun-ratebudgetisolatesstrictlylocalspendingcontrolandisalsotheana-
lyticallymosttractablecaseduetowindow-wiseseparability. Theabsolutecumulative
budget represents fully history-coupled budget control over the horizon, while the in-
crementalcumulativebudgetcapturesadistinctgrowth-limitingregimethatconstrains
upsizing-drivencostincreasesratherthantotalaccumulatedspend. Takentogether,these
three models span the principal trade-off patterns of interest in our study—stage-wise
caps,long-horizoncumulativelimits,andgrowth-constrainedresizing—whilekeeping
theempiricalcomparisonfocusedandinterpretable. Wethereforetreattherolling-budget
variantonlyasasupplementarydiagnosticratherthanasaprimarycomparisonfamilyin
thissection.
6.3.1. CostEfficiency
Figure4reportscostsavingrelativetoStaticasthebudgetmultiplierα ∈0.1,0.2,...,
1.0varies,revealingmarkedlydifferentbehaviorsacrosstemporalhard-budgetsemantics.
Under the per-window run-rate model (Figure 4b), BD shows a pronounced plateau
followedbyaclearknee: savingsremainessentiallyunchangedatabout ∼ 49.3%over
α = 0.1–0.4, then gradually decline as the budget relaxes—46.4% at α = 0.5, 40.2% at
α =0.6,31.6%atα =0.7,and26.5%atα =0.8—beforedroppingfurtherto15.5%atα =0.9
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 35of48
and2.9%atα =1.0. PRGattainsevenlargersavingsintheverytightregime(e.g.,88.2%
atα = 0.1,77.2%atα = 0.2,and56.9%atα = 0.4),butsteadilyconvergestowardBDas
thebudgetloosens(e.g.,39.9%atα =0.6,27.5%atα =0.8)andbecomessimilarlysmallat
α =1.0(1.6%). Incontrast,Greedyremainsnearlyconstantat36.0%acrossallα,indicating
weakresponsivenesstobudgettighteningorrelaxationwhensavingsaremeasuredrelative
toStatic.
Figure4.Costsavingvs.budgetstrengthα(post-gate).Costsaving(%)relativetoStaticasafunction
ofthebudgetmultiplierαunder(a)absolutecumulativeB
abs_cum
,(b)run-rateper-windowBrate_pw,
and(c)incrementalcumulativeB ;metricsarecomputedfrompost-gate(deployable)decisions
inc_cum
(mean±stdover10seeds).
Undertheabsolutecumulativemodel(Figure4a),savingsaremorestronglyshaped
by history coupling. BD decreases smoothly from 49.3% at α = 0.1 to 39.7% (α = 0.2),
28.8% (α = 0.4), 18.6% (α = 0.6), 9.1% (α = 0.8), and 2.9% (α = 1.0). PRG is notably
lessconsistent: itachievesmoderatesavingsatsometight-budgetpoints(e.g.,20.3%at
α =0.2and18.8%atα =0.4)butcollapsestosingle-digitsavingsforlooserbudgets(e.g.,
5.1%atα =0.6)andbecomesverysmallbyα =1.0(1.6%). Greedyagainappearsalmost
budget-insensitive(about36.0%acrossα),butthisapparentadvantagemustbeinterpreted
jointlywithfeasibilityandstabilityoutcomes,becausecumulativeconstraintscanreward
aggressiveearlydownsizingthatreshapestheremainingfeasiblecosttrajectory.
Finally, under the incremental model (Figure 4c), BD and PRG show consistently
smallcostsavingsacrossthesweep: BDstaysatabout2.9%forallα,whilePRGis5.7%
atα =0.1andapproximately1.6%forα ≥0.2. Greedyremainsnearlyconstantat36.0%.
Thispatternisconsistentwiththeincrementalbudgetsemanticsinoursimulator,which
chargeonlypositive(scale-up)costincreasesandignoresavingsfromdownsizingwhen
computingfeasibility;asaresult,varyingαhaslimitedleverageontherealizedcostsavings
forstability-awarepoliciesinthissetting(ρ =10).
Overall, Figure 4 suggests that the proposed BD most effectively converts budget
flexibility into economic benefit under the run-rate model, while the cumulative and
incrementalfamilieshighlightwhysavingsaloneareinsufficientandmustbeevaluated
togetherwithfeasibilityandoperationalstability(Sections6.3.2–6.3.4).
6.3.2. BudgetFeasibility
Inthissection,weevaluatebudgetfeasibilityundertemporalhard-budgetpolicies
usingadiagnosticviewthatisolatesalgorithmicbudgetawarenessfromthesharedde-
ploymentmechanism. Thecandidateviolationrateisdefinedasthefractionofdecision
windows in which the candidate decision violates the active budget constraint before
applyingthecommoncompliancegate. Thismetricquantifieshowstronglyeachmethod
internalizestheactivebudgetpolicy(i.e.,howmuchitreliesonthegatetobecomedeploy-
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 36of48
able). Deployment-levelfeasibilityiscapturedbythepost-gateviolationrate(Section6.1.5):
under our deterministic common gate, any avoidable violation is repaired whenever a
feasibleassignmentexistsinthediscreteVM-typepool;therefore,post-gateviolationsoccur
onlyinstructurallyinfeasiblewindows. Accordingly,wefocusonthepre-gatecandidate
violationrateasaregimediagnostic.
Figure 5b shows that feasibility under the per-window run-rate model B ex-
rate_pw
hibits a sharp threshold behavior consistent with its stage-wise separable nature. BD
transitionsrapidlyfromfrequentviolationsunderverytightbudgetstoafeasibleregime
withessentiallyzeroviolations: itscandidateviolationrateisaroundthelow-to-mid90%
rangeatα =0.1,dropstoroughlythemid-50%rangebyα =0.4,fallstoaroundthelow
teens near α = 0.5, and reaches 0.0% once α ≳ 0.6. A clear feasibility knee is therefore
observedaroundα ≈ 0.6,beyondwhichviolationsremainat0.0%. Incontrast,Greedy
remains infeasible deeper into the sweep: it stays above roughly 50% through α = 0.5
andstillshowssubstantialviolationsaroundα =0.6,onlyreaching0.0%aroundα ≈0.7.
PRG maintains 0.0% violations across all values of α, while Static violates the run-rate
budgetseverelythroughoutmostoftherange(remainingabove50%evennearα = 0.9)
andreaches0.0%onlyatα =1.0. TheseresultsindicatethatBDachievesstrictfeasibilityin
apracticallyrelevantregimewherenon-budget-awareheuristicscontinuetoincurfrequent
violations,effectivelyconvertingbudgetrelaxationintooperationallyexecutabledecisions
ratherthanmerelyreducingcost.
Figure5. Candidatebudgetviolationratevs. budgetstrengthα(pre-gate). Candidate(pre-gate)
violationrate(%)versusαunder(a)absolutecumulativeB
abs_cum
,(b)per-windowrun-rateBrate_pw,
and(c)incrementalcumulativeB (mean±stdover10seeds).In(c),theStaticviolationrateis
inc_cum
0forallα,sothedottedStaticcurveisnotseparatelyvisible.
Figure5aillustratesthatfeasibilityundertheabsolutecumulativebudgetB is
abs_cum
substantiallymorechallengingduetohistorycoupling,wherebyearlyspendingdecisions
constraintheremainingfeasiblecosttrajectory. Underthismodel,BDandPRGremain
highlyinfeasibleacrosstight-to-moderateregimesandonlyapproach0.0%violationsatthe
fullynominalsettingα =1.0,reflectingtheintrinsicdifficultyofsatisfyingacumulative
constraintwhenthetrajectoryiscoupledovertime. Greedy,bycontrast,reducesviolations
muchfasterandreaches0.0%earlier(aroundα ≈0.7). However,suchfeasibilityimprove-
mentsmustbeinterpretedjointlywithoperationalstability(Section6.3.3),ascumulative
budgetscanfavorstrategiesthatreshapethecosttrajectoryviaaggressiveearlydownsizing
andfrequentreconfiguration.
Finally, Figure 5c shows that the incremental cumulative budget B , which
inc_cum
primarilyconstrainsupsizingincrements(i.e.,thetotalpositivecostincreasescausedby
scale-upactionswithinawindow),yieldsadistinctfeasibilitypattern. Staticistrivially
feasibleunderthesesemantics,andbothBDandPRGmaintain0.0%violationsacrossthe
entiresweep. Incontrast,Greedyviolatestheincrementalconstraintfrequentlyundertight
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 37of48
budgets(near90%aroundα =0.1)andimprovesonlygraduallyasαincreases,remaining
nonzero even at α = 1.0. This behavior indicates that even cost-efficient heuristics can
triggerrepeatedupsizingspikesthatviolategrowthconstraints,whereasBDpreserves
strictfeasibilitywithoutrelyingonaggressivereconfiguration.
Overall,Figure5confirmsthatthefeasibilityadvantageofBDismostpronounced
under the run-rate budget B . A clear feasibility knee appears around α ≈ 0.6,
rate_pw
beyondwhichBDachieves0.0%candidateviolations(forα ≥ 0.6)whilestillmaintaining
strongcostsavings. Thistransitionalignswiththestructuralfeasibilitythresholddiscussed
inSection4,wheretherun-ratebudgetbecomessufficienttoaccommodatethelowest-cost
assignmentintheVM-typepool. Undercumulativebudgets,feasibilitybecomesinherently
history-dependentandmustthereforebeinterpretedjointlywithoperationalstability. In
contrast,underincrementalbudgetsfeasibilityistypicallymaintainedbystability-aware
policies,althoughnon-budget-awareheuristicsmaystillviolatethegrowthconstraint.
6.3.3. OperationalStability
Inthissection,weevaluateoperationalstabilitybyanalyzingthechangerate,defined
asthefractionofvirtualmachineswhoseconfigurationismodifiedwithinadecisionwin-
dow. Whilefrequentreconfigurationcanhelpreducecostorenforcefeasibility,excessive
changesincurmigrationoverhead,control-planeload,andpotentialservicedisruption.
Therefore, apracticallydesirablemethodshouldmaintainalowchangeratewhilestill
achievingcostefficiencyandbudgetfeasibility. Ourobjectiveistoobservehowchange
ratesevolveasthebudgetisrelaxedandhowthisevolutiondependsonthesemanticsof
thebudgetmodel.
Figure 6b shows that under the per-window run-rate budget model B , BD
rate_pw
maintainsconsistentlylowchangeratesacrosstheentiresweepofα. Concretely,BDstays
inthelowteensundertightbudgets(around12%atα = 0.1),thendecreasessteadilyas
thebudgetrelaxes,reachingonlyafewpercentbyα ≈0.6andapproachingabout1%at
α =1.0. Incontrast,PRGexhibitsstronglyincreasingchurnasαgrows: itrisesfromthe
lowteensatα = 0.1toexceed60%inthemoderate-to-looseregimeandfurtherexceeds
≳
70%forα 0.7. Greedyremainsnearlyconstantatroughly52%regardlessofα,indicating
persistent aggressive reconfiguration. Static trivially shows a 0.0% change rate but, as
showninSection6.3.2,failstomaintainfeasibilityundertightbudgets. Together,these
resultsdemonstratethatBDuniquelycombinesfeasibility(Figure5b)withoperational
stabilityunderastage-wiseseparablebudget,whereasPRGandGreedyrelyonfrequent
reconfigurationtosatisfyconstraintsorextractsavings.
Figure6.Changeratevs.budgetstrengthα(post-gate).Post-gatechangerate(%)versusαunder
(a)absolutecumulativeB
abs_cum
,(b)per-windowrun-rateBrate_pw,and(c)incrementalcumulative
B (mean±stdover10seeds).
inc_cum
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 38of48
UndertheabsolutecumulativebudgetmodelB (Figure6a),historycoupling
abs_cum
amplifiesinstabilityforfeasibility-orientedheuristics.BDagainremainsstable,withchange
ratesaroundthelowteensundertightbudgetsanddecreasingtowardnear-zeroasαap-
proaches 1.0. By contrast, PRG shows a steady increase in churn as the budget relaxes,
reachingthemid-60%rangebyα=1.0. Greedyagainstaysflatatabout52%,consistent
with its budget-insensitive behavior. This pattern indicates that under cumulative con-
straints, PRG effectively trades stability for feasibility by repeatedly reshaping the cost
trajectory,whereasBDpreservesstabilitywhilegraduallytransitioningtowardfeasibility.
Figure 6c presents the incremental cumulative budget model B , where the
inc_cum
budgetprimarilythrottlescostincreases. Inthissetting,BDmaintainsanalmostnegligible
and nearly flat change rate (about 1%) across all values of α, indicating strong stability.
PRGandGreedy,however,showpersistentlyhighchangerates—aroundthemid-60%and
low-50% ranges, respectively—despite the incremental constraint. This highlights that
suppressingcostescalationsalonedoesnotpreventexcessivereconfigurationforheuristics
thatlackexplicitstabilityawareness.
Overall,Figure6demonstratesthatBDconsistentlyachieveslowoperationalchurn
across all budget families, while PRG and Greedy rely on frequent reconfiguration to
achievefeasibilityorcostreduction. CombinedwiththefeasibilityresultsinSection6.3.2
and the cost efficiency trends in Section 6.3.1, these findings confirm that BD attains a
favorablebalancebetweencostsavings,budgetcompliance,andoperationalstability—an
essentialpropertyforpractical,large-scaleVMmanagement.
6.3.4. Trade-OffDecomposition
Costefficiency,budgetfeasibility,andoperationalstabilitydonotalwaysimprove
simultaneously. Relyingonasinglemetriccanthereforeobscuremeaningfuldifferences
betweenalgorithms.Figure7presentsadecomposedviewofthemulti-objectiveoutcomeat
arepresentativeoperatingpointwithα =0.6andρ =10underthreetemporalhard-budget
models B , B ,and B . Thevalueα = 0.6correspondstoamid-budget
abs_cum rate_pw inc_cum
regimenearthefeasibilitytransitionobservedinthebudgetsweep,andρ=10maintains
thestabilityemphasisusedthroughoutthemainevaluation.
Figure7.Normalizedtrade-offdecompositionatα=0.6.Stackedcomponents(costsaving,candidate
violation,overloadratio,andchurn)under(a)absolutecumulativeB ,(b)per-windowrun-
abs_cum
rateBrate_pw,and(c)incrementalcumulativeB
inc_cum
;valuesaremin–maxnormalizedwithineach
budgetmodel.
Foreachbudgetfamily,acompositescoreisconstructedfromfourcomponentsderived
fromthesameper-windowstatisticsusedinSections6.3.1–6.3.3. Thecomponentsarecost
savingrelativetoStatic,candidatepre-gateviolationrate,weightedoverloadratio,and
operationalchurncomputedfromchangerateandmigrationspervirtualmachine. Each
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 39of48
componentismin–maxnormalizedtotheinterval [0,1] withinthesamebudgetfamily
acrossallalgorithmsandαvalues.Forviolation,overload,andchurn,thenormalizedvalue
isinvertedsothatlargervaluesconsistentlyrepresentbetterperformance. Thetrade-off
scoreisthendefinedas
S =0.35S +0.35S +0.15S +0.15S .
trade_off saving violation overload churn
Figure7stackstheseweightedcontributions, andthetotalbarheightcorresponds
to S . Theweightingemphasizeseconomicbenefitandbudgetcompliancewhile
trade_off
preservingmeaningfulcontributionsfromoverloadriskandoperationalstability.
Under B ,Greedyattainsthelargestcompositescoreofapproximately0.690,
abs_cum
mainlyduetostrongsavingandfeasibilitycontributions. However,itschurncontribution
remainsverysmallatapproximately0.032,reflectinghighlyreactiveresizingbehavior. BD
achievesalowertotalofapproximately0.532butexhibitsamorebalanceddistribution,
withasubstantiallylargerchurnshareofapproximately0.129andacomparableoverload
contribution. Thisprofilebetterreflectsdeployment-orientedstabilityrequirements.
UnderB ,theseparationismorepronounced. BDachievesthehighestscoreat
rate_pw
approximately0.784bycombiningthemaximalfeasibilitycontributionofapproximately
0.35withmeaningfulsavingandsubstantialoverloadandchurnshares. PRGalsoachieves
themaximalfeasibilitytermbutshowsamuchsmallerchurncontributionofapproximately
0.021,indicatingfrequentresizingunderstrictper-windowcaps.
UnderB ,feasibilitydifferencesarereducedbecausetheincrementalconstraint
inc_cum
limitsonlypositivecostincreases. Oncescale-upactionsarecontrolled,candidateviola-
tions largely disappear and the violation component saturates. In this regime, ranking
isprimarilydeterminedbystability-relatedterms. BDachievesthehighesttotalscoreof
approximately0.669becauseitmaintainsstrongerchurnandoverloadcontributionsthan
theothernon-staticmethodswhilestillpreservingnon-zerosaving.
ThedecompositionclarifiesthepracticaladvantageofBD.Acrossdifferentbudget
semantics,BDavoidsdominancebyasinglemetricandmaintainsaconsistentbalance
betweeneconomicefficiency,budgetawareness,andoperationalstabilityatadeployment-
relevantoperatingpoint.
6.3.5. ParameterSensitivityofBD
BDintroducesseveralhyperparametersinthedualupdate(η and ν )aswellas
max
(cid:0) (cid:1)
trade-offweightsintheobjective(λ,ρ,and w ,w ). Toassesswhethertheresults
cpu mem
inSection6.3relyondelicatetuning,weconductalocalone-factor-at-a-timesensitivity
analysis at a representative operating point: the Typical workload under the run-rate
(per-window)budgetwithα = 0.6andarepresentativefleetsize N = 100. Wevaryone
parameter at a time while keeping all others fixed to the reference setting used for this
(cid:0) (cid:1) (cid:1)
analysis(η = 1.0, ν = 109, λ = 0.5, ρ = 10,and w ,w = (0.8,0.2 ). Foreach
max cpu mem
setting,werun10randomseedsandreportcostsaving,candidate(pre-gate)violationrate,
andpost-gatechangerateasdefinedinSection6.1.5. ResultsaresummarizedinTable7.
Overall,BDremainsfullyfeasibleatthecandidatelevelacrossalltestedsettingsat
thisoperatingpoint,yielding0.0%candidateviolations(mean±std=0.0±0.0)inTable7.
In this feasible run-rate regime, the dual-update hyperparameters η and ν show no
max
measurableeffectwithinthetestedranges. Specifically, sweeping η from0.2to2.0and
ν from 103 to 109 leaves both cost saving and change rate essentially unchanged, at
max
48.64 ± 1.68%and21.11 ± 1.23%, respectively. ThisindicatesthatBDdoesnotrequire
fine-grainedtuningofthedualstepsizeorthedualprojectionboundtomaintainfeasibility
andstablebehavioroncetherun-ratebudgetentersafeasibleregion.
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302
40of48
Table 7. Local sensitivity of BD hyperparameters under the Typical workload and the run-rate
(per-window)budgetat α = 0.6. Fleetsize N = 100. Reportedvaluesaremean ± standard
deviationover10randomseeds.Costsavingandchangeratearecomputedfrompost-gatedecisions,
whilecandidateviolationrateiscomputedfrompre-gatecandidatedecisions.
Candidate
| Parameter | Value | CostSaving(%) |     | ChangeRate(%) |
| --------- | ----- | ------------- | --- | ------------- |
Violation(%)
|     |     | 48.64±1.68 | 0.0±0.0 | 21.11±1.23 |
| --- | --- | ---------- | ------- | ---------- |
0.2
|     | 0.5 | 48.64±1.68 | 0.0±0.0 | 21.11±1.23 |
| --- | --- | ---------- | ------- | ---------- |
η
|     | 1.0 | 48.64±1.68 | 0.0±0.0 | 21.11±1.23 |
| --- | --- | ---------- | ------- | ---------- |
|     |     | 48.64±1.68 | 0.0±0.0 | 21.11±1.23 |
2.0
|     | 1×103 | 48.64±1.68 | 0.0±0.0 | 21.11±1.23 |
| --- | ----- | ---------- | ------- | ---------- |
|     | 1×105 | 48.64±1.68 | 0.0±0.0 | 21.11±1.23 |
ν
max
|     | 1×107 | 48.64±1.68 | 0.0±0.0 | 21.11±1.23 |
| --- | ----- | ---------- | ------- | ---------- |
|     | 1×109 | 48.64±1.68 | 0.0±0.0 | 21.11±1.23 |
|     |       | 50.71±1.62 | 0.0±0.0 | 38.52±2.20 |
0.1
|     | 0.3 | 49.57±1.61 | 0.0±0.0 | 26.20±1.55 |
| --- | --- | ---------- | ------- | ---------- |
λ
|     | 0.5 | 48.64±1.68 | 0.0±0.0 | 21.11±1.23 |
| --- | --- | ---------- | ------- | ---------- |
|     | 1.0 | 48.59±1.54 | 0.0±0.0 | 17.28±0.68 |
|     | 5   | 49.98±1.68 | 0.0±0.0 | 18.97±1.29 |
|     | 10  | 48.64±1.68 | 0.0±0.0 | 21.11±1.23 |
ρ
|           | 20            | 47.82±1.48 | 0.0±0.0 | 22.36±1.26 |
| --------- | ------------- | ---------- | ------- | ---------- |
|           | (0.2,0.8)     | 49.73±1.69 | 0.0±0.0 | 18.93±1.11 |
| (cid:0)   | )             | 48.76±1.58 | 0.0±0.0 | 19.79±1.30 |
| w cpu , w | mem (0.5,0.5) |            |         |            |
|           | (0.8,0.2)     | 48.64±1.68 | 0.0±0.0 | 21.11±1.23 |
Incontrast,theoverloademphasisλmateriallyaffectsresizingaggressivenessand,
indirectly, operationalchurn. Increasing λ from0.1to1.0reducesthechangeratefrom
38.52±2.20%to17.28±0.68%,whilecostsavingchangesonlymodestlyfrom50.71±1.62%
to48.59±1.54%.
Thisindicatesthatstrongertail-safetyweightingcansuppressreactive
resizingwithoutmateriallyerodingeconomicbenefitatthisoperatingpoint.
(cid:0) (cid:1)
Varying the stability weight ρ and the resource aggregation weights w ,w
cpu mem
changes the quantitative values slightly but does not alter the qualitative conclusions.
Across ρ ∈ {5,10,20}, cost saving remains within a narrow band (49.98±1.68% at
=5versus47.82±1.48%atρ =20),andchangeratevariesmoderately(18.97±1.29%at
ρ
ρ =5versus22.36±1.26%atρ =20). Similarly,shiftingtheaggregationweightsbetween
CPU-andmemory-emphasizedsettingsyieldsonlymodestchanges(e.g.,49.73±1.69%
|     |     | (cid:0) | (cid:1) | (cid:1) |
| --- | --- | ------- | ------- | ------- |
savingand18.93±1.11%changerateat w ,w = (0.2, 0.8 ,versus48.64±1.68%
cpu mem
savingand21.11±1.23%changerateat(0.8,0.2)).
Takentogether,Table7confirmsthat
themainconclusionsofSection6.3arerobusttomoderatehyperparametervariations. To
assess whether the conclusions depend on the specific workload-risk instantiation, we
alsoverifiedinsupplementaryrobustnesschecksthatvaryingtheentropyresolutionB
bin
andtheamplificationweights(β ,β )aroundthedefaultsetting. Acrossthesevariants,
1 2
thefeasibilitytransitionandthequalitativerankingofBD,Greedy, andPRGremained
unchanged, indicating that the main conclusions do not hinge on a single choice of en-
tropydiscretizationoramplificationstrength. Inparticular,therun-ratefeasibilityknee
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 41of48
remainednearα ≈0.6,whileBD’spost-gatecostsavingchangedonlymodestlyacrossthe
testedvariants.
6.4. Scenario-BasedBehavioralAnalysis
While Section 6.3 evaluates budget-aware performance under temporal hard con-
straints,thoseresultsintertwineintrinsicresizingbehaviorwithcompliance-gatefeasibility
repairandbudget-inducedthrottling. Inordertoexaminethestructuralbehavioralprop-
erties of each policy independent of budget enforcement, we temporarily disable the
temporalbudgetconstraintinthissection. Thisisolationallowsustoanalyzetheintrinsic
dynamicsofresizingdecisionswithouttheconfoundingeffectsoffeasibilitycorrectionor
dual-inducedbudgetpressure. Specifically,weseektoisolatethreeaspectsofalgorithmic
behavior: economicresponsivenesstoworkloadvariation,stabilityregulationthroughthe
change-penaltyparameterρ,andtemporalreactionpatternsunderdistinctworkloaddy-
namics.Byremovingbudgetfeasibilityconstraints,weobservehoweachmethodinternally
balancesthesizing-qualityobjective f andthestabilityobjective f acrossqualitatively
1 2
differentdemandregimes.
AcrossFigures8–10,weevaluateStaticandGreedybaselines,BDunderρ∈{0.5,2,5,10},
andanofflineNSGA-IIreference.Thecentralobjectiveofthissectionistodemonstratethat
BDformsapolicyfamilyparameterizedbyρ,whereρactsasaninterpretablecontrolknob
thatcontinuouslyshiftstheoperatingpointbetweenresponsivenessandconservatism.Rather
thanbeingtunedtoaspecificworkload,BDexhibitsstructurallyconsistentbehavioracross
transientspikes,sustainedshifts,andoscillatoryregimes.
Figure8.Transientspikeworkload:migrationfrequencyandmigrationefficiency(budgetsdisabled).
Behavioralresponseunderatransientspike-dominatedworkload:(a)averagenumberofmigrationsper
VMand(b)migrationefficiency(costsavingpermigration)forStatic,Greedy,BDwithρ∈0.5,2,5,10,
andNSGA-II.Budgetsaredisabledtoisolateintrinsicstability–responsivenessbehavior.
Figure 9. Sustained demand shift workload: adaptation vs. conservatism (budgets disabled).
Behavioralresponseunderasustainedramp-downworkload:(a)averagenumberofmigrationsper
VMand(b)per-VM f (wasteplusoverloadpenalty)forStatic,Greedy,BDwithρ∈{0.5,2,5,10},
1
andNSGA-II.Lower f indicatesbettersizingquality.
1
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 42of48
Figure10.Oscillatoryworkload:churnandmigrationburstiness(budgetsdisabled).Behavioralre-
sponseunderanoscillatoryworkload:(a)averageconfigurationchangerateand(b)migrationbursti-
ness(standarddeviationofper-VMmigrationcounts)forStatic,Greedy,BDwithρ∈{0.5,2,5,10},
andNSGA-II.
6.4.1. TransientSpike-DominatedWorkload
Figure 8 evaluates behavior under spike-dominated workloads, where short-lived
burstsoccurintermittentlyoveramostlylow-utilizationbackground. Theprimaryfailure
modeinthisregimeisover-reactiveresizing,inwhichthecontrollerrepeatedlyupsizes
anddownsizesinresponsetoephemeralspikes,inducingexcessivemigrationoverhead.
Figure 8a reports the average number of migrations per virtual machine. Greedy
exhibitsheavyreconfigurationwith8.31migrationsperVM,indicatingstrongspikechas-
ing. In contrast, BD at ρ = 0.5 reduces migration activity to 1.08 migrations per VM
while simultaneously increasing cost saving from 38.71% (Greedy) to 59.48%. This in-
dicatesthatBDcanextracthighereconomicbenefitwithsubstantiallyfewerdisruptive
actions. Asρincreases,BDfurthersuppressesmigrationactivity(e.g.,0.57atρ = 2and
approximately0.11–0.14atρ ∈5,10),illustratingacontrollableshifttowardconservative,
low-churnbehavior.
Figure 8b reports migration efficiency (cost saving per migration), defined as
CostSaving(%)
,whichhighlightsthequalityofresizingactionsratherthantheir
AverageMigrationsperVM
frequency. Greedyachievesonly4.66saving-unitspermigration,whereasBDachieves
55.19atρ = 0.5andremainshighatρ = 2(34.63),demonstratingthatBDconvertseach
migrationintosubstantiallylargereconomicbenefit. NSGA-IIimprovesoverGreedyin
efficiency (17.35) but remains notably less migration-efficient than BD in this transient-
spikeregime. Overall,Figure8supportsakeyclaimofthepaper: BDavoidsthrashingand
achieveshigheconomicbenefitwithminimaloperationaldisruption,particularlywhen
transientspikesdominate.
6.4.2. SustainedShiftWorkload
Figure 9 evaluates behavior under sustained demand shifts with a gradual ramp-
down pattern. In this regime, desirable behavior is controlled adaptation: the policy
shoulddownsizetoremovepersistentover-provisioning,butshouldnotrelyonaggressive,
high-frequencyreconfiguration.
Figure9areportsaveragemigrationsperVM.Greedyachievesstrongsavings(48.30%)
butatveryhighoperationaloverhead(11.11migrationsperVM)andahighchangerate
(51.62%). BDatρ =0.5preservesmostofthesavings(41.70%)whilereducingmigrations
to2.14perVMandthechangerateto10.01%,demonstratingthatstability-awarecontrol
canretaineconomicbenefitwithoutincurringpersistentchurn. Asρincreases,BDbecomes
progressivelymoreconservative;atρ =2,themigrationcountdropsto0.10perVM(change
rate 0.47%), but savings collapse to 2.63%, indicating that excessive stability emphasis
suppressesadaptation.
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 43of48
Figure9breportstheper-VMvalueof f (wasteplusoverloadpenalty),whichreflects
1
how well the policy aligns capacity to sustained demand. Greedy attains the lowest
f (3.41), but only by aggressive reconfiguration. BD at ρ = 0.5 achieves a competitive
1
f (4.59) while drastically reducing churn, whereas BD at ρ = 2 returns close to Static
1
behavior (f = 11.29 vs. 11.73 for Static). NSGA-II provides an offline reference with
1
f =5.32and7.90migrationsperVM,showingthathigher-qualitysolutionsarepossible
1
but often at substantially higher operational cost than BD stability-favorable operating
points. Overall,Figure9highlightsacentralmessage: ρselectsqualitativelydifferentBD
policies,andmoderateρyieldsapracticallydeployablebalancebetweenadaptationand
stabilityundersustainedshifts.
6.4.3. OscillatoryWorkload
Figure10evaluatesbehaviorunderoscillatoryworkloadsthatmixmultiplevariability
sources. Such regimes often induce chattering, where frequent back-and-forth resizing
producesoperationalinstabilitywithlimitednetbenefit.
Figure10areportstheaveragechangerate. Greedyexhibitsseverethrashingwitha
53.95%changerate, whileBDreducesthechangeratebyanorderofmagnitudeforall
testedρvalues(e.g.,10.39%atρ = 0.5and7.80%atρ = 2). NSGA-IIalsoreduceschurn
relativetoGreedy(16.25%)butremainsnotablylessstablethanBDinthebalancedregime.
Figure10breportsmigrationburstiness(thestandarddeviationofper-VMmigration
counts),capturingwhetherresizingactionsareconcentratedonasubsetofVMs. Greedy
showsstrongconcentration(3.23),indicatingmigrationhotspots. BDsubstantiallyreduces
burstiness(e.g.,0.83atρ =0.5and0.77atρ =2),showingthatBDnotonlyreducesoverall
churnbutalsoavoidsconcentratingoperationaldisruption. Importantly,BDachievesthese
stabilitygainswhilemaintainingstrongsavings: 49.76%atρ = 0.5and35.95%atρ = 2,
comparedto28.27%forGreedy. Thisconfirmsthatstability-awareresizingcandominate
reactiveheuristicseveninhighlyoscillatoryenvironments.
6.5. Real-TraceValidation
6.5.1. ExperimentalSetupUsingRealTrace
Inthissection,weconductexperimentsusingareal-worldworkloadtracederived
fromtheGoogleClusterData(2011)dataset[45]. Specifically,weusethetask_usagerecords
to construct a VM-like fleet by treating each (job_id, task_index) pair as an individual
workloadinstance. Acontiguous24-hsliceofthetraceisextractedandaggregatedat5-min
intervals,resultingin288decisionwindowsforafleetof50VMs.
Becausetheoriginaltracevaluesrepresentnormalizedutilizationratiosratherthan
absoluteresourcedemand,weapplyasimplecalibrationtoalignthetracewiththeVM
capacityscaleusedinthesimulator. Letcpu_p95andmem_p95denotetheglobal95th
percentileofCPUandmemorydemandobservedinthetrace. Thesevaluesarescaledso
that thep95 demand corresponds to approximately 70% ofthe maximum VM capacity
inthetypepool(16vCPUand32GB).Thiscalibrationpreservesthetemporaldynamics
of the workload while ensuring that resizing decisions exercise a meaningful range of
instancetypes. Usingthiscalibratedtrace, weevaluatethesamesetofpoliciesusedin
the main experiments—Static, Greedy, PRG, and the proposed BD solver—under two
representativetemporalhard-budgetmodels: theper-windowrun-ratebudgetandthe
absolutecumulativebudget. Thebudgetmultiplierαissweptfrom0.1to1.0whilethe
stability weight ρ is fixed at 2. All performance metrics follow the evaluation protocol
definedinSection6.1.5andarecomputedfromthefinalpost-gatedecisionsproducedby
thecommoncompliancegate.
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 44of48
6.5.2. BudgetTrade-OffsUnderRealWorkloads
Figures11–13summarizethereal-traceevaluationresultsobtainedusingtheGoogle
ClusterDataworkload.
Figure11.Real-tracecostsavingvs.budgetstrictness(post-gate).Costsaving(%)relativetoStaticon
theGoogleClusterData(2011)[45]traceversusbudgetmultiplierαundertwotemporalhard-budget
models: (a)absolutecumulative B
abs_cum
and(b)per-windowrun-rate Brate_pw. Allmetricsare
computedfrompost-gate(deployment-level)decisionsproducedbythecommoncompliancegate;
ρ=2.
Figure12. Real-tracebudgetfeasibilityvs. budgetstrictness(post-gateviolationrate). Post-gate
(deployment-level) budget violation rate (%) versus α on the Google ClusterData trace under
(a)absolutecumulativeB
abs_cum
and(b)per-windowrun-rateBrate_pw.Post-gateviolationsrepre-
sentwindowsthatremaininfeasibleafterapplyingthecommoncompliancegate(e.g.,structurally
infeasibleregimesunderthediscreteVM-typepool);ρ=2.
Figure 13. Real-trace operational churn vs. budget strictness (post-gate change rate). Change
rate (%) versus α on the Google ClusterData trace under (a) absolute cumulative B and
abs_cum
(b) per-window run-rate Brate_pw. Change rate is computed from post-gate configurations and
reflectsdeployment-leveloperationalchurn(fractionofVMschangingtypeperwindow);ρ=2.
Under the run-rate budget model (Figures 11b–13b), BD demonstrates a clear fea-
sibility transition as the budget is relaxed. For example, at α ≈ 0.6, BD achieves
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 45of48
approximately 39% cost saving while maintaining a very low change rate of about
2–3%andlimitingpost-gateviolationstoroughly5–6%ofwindows. Incontrast,Greedy
attainscomparablecostsavingsbutexhibitssubstantiallyhigheroperationalchurn(around
64%changerate)andsignificantlyhigherviolationratesinthesameregime. PRGoften
achieveszeroviolationsbutincursmuchhigherconfigurationchangesthanBD,indicating
thatfeasibilityisobtainedthroughaggressivereconfiguration.
Undertheabsolutecumulativebudgetmodel(Figures11a–13a),feasibilityimproves
moregraduallyasαincreasesbecausetheconstraintcouplesspendingacrosstime. Never-
theless,BDconsistentlymaintainsverylowoperationalchurnthroughoutthesweepand
eventuallyreachesfullfeasibilityathigherαvalueswhilestillprovidingmeaningfulcost
savings. Incontrast,Greedyachievesfeasibilityearlierbutonlyatthecostofpersistently
highreconfigurationrates.
Overall,thereal-traceexperimentconfirmsthatthequalitativebehaviorobservedin
syntheticworkloadspersistsunderrealisticdemanddynamics. Inparticular,BDmaintains
a favorable balance between economic efficiency, budget compliance, and operational
stability. These results indicate that the proposed dual-based control mechanism gen-
eralizesbeyondsimulator-generatedworkloadsandremainseffectiveunderreal-world
workloadvariability.
7. Conclusions
ThispaperinvestigatedFinOps-awarecloudresourcemanagementthroughonline
VMresizingundertemporalhardbudgets. InrealisticdeploymentswithadiscreteVM-
type pool, strict budget feasibility cannot be assumed: some decision windows can be
structurallyinfeasible,andcandidateassignmentsmustpassacommoncompliancegateto
becomedeployableactions. Buildingontheseoperationalconstraints,weformulatedthe
Budget-ConstrainedVMResizing(BC-VMR)problem,unifiedmultipletemporalbudget
semanticswithinasingleframework(run-rate,absolutecumulative,incrementalcumu-
lative,androlling),andestablishedNP-hardnessforsimplifiedscalarizedvariantsasa
complexity-positioningresult. Together,theseresultsmotivatescalableonlinemethods
thatexplicitlymanageviolationminimizationandstability-awaretrade-offs,ratherthan
relyingonexactoptimizationortreatingbudgetsastunablesoftpenalties.
Within this framework, we proposed the BD solver, which incorporates temporal
hard-budgetconstraintsviaaninterpretabledualvariableνthatactsasashadowpriceof
budgetpressure. Theexperimentalresultssupporttheintendedbehaviorofthisdesign: ν
decreasesmonotonicallyasbudgetsarerelaxedandapproacheszerowhenthecorrespond-
ingconstraintbecomesinactive,consistentlyacrossbudgetmodels. Inthemainsynthetic
run-rateevaluation,BDreducesthecandidate(pre-gate)budgetviolationrateto0.0%once
α ≥ 0.6;afterthecommoncompliancegate,anyremainingdeployment-levelviolation
is confined to structurally infeasible windows. At the same time, BD improves opera-
tionalstabilityrelativetoutility-drivenheuristics,reducingresizing-inducedchurnfrom
53.95%(Greedy)to7.80%(BD,ρ = 2)intheoscillatoryscenariowhileretainingmeaningful
costsavings. Thecomparativeanalysisfurtherhighlightsthattemporalbudgetseman-
ticsarenotinterchangeable: differentbudgetmodelsinducedistinctfeasibilitydynamics
andstability–efficiencytrade-offs,andcontrollersmustbeevaluatedunderaconsistent
compliance-gateprotocoltoensurefair,deployment-alignedcomparisons. Finally,scal-
ability experiments show that BD remains practical at large fleet sizes; at N = 10,000
it requires 102–103 ms per decision window, whereas NSGA-II requires approximately
105ms.
Mostexperimentsinthisstudyremainsimulator-based,althoughSection6.5adds
a complementary validation on a public Google trace. Within this scope, we focused
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 46of48
ontwocoreobjectivestoanalyzefeasibilityandoperationalstabilityunderhardbudget
constraints: the objective function f , capturing the waste–overload trade-off, and the
1
stability-orientedobjectivefunction f ,penalizingreconfigurationfrequency. Whilethe
2
overloadcomponentalreadyincorporatestaildemandandworkload-riskamplification
signals derived from variability and irregularity (e.g., σ and entropy through ω), our
formulationremainsintentionallylightweightandsimulator-drivenandthereforedoesnot
captureeveryoperationaldimensionencounteredinproduction(e.g.,explicitSLA/latency
objectives, heterogeneous migration costs, or forecast uncertainty). These limitations
motivateextensionstowardricherobjectivesandmorerealistictraceswhilepreserving
thedeployment-alignedhardbudgetandcommoncompliancegateevaluationprotocol
establishedinthispaper.
One such direction is to extend the current lightweight overload-risk term into a
moreexplicitandseparatelycontrollableburst-riskcomponent. Certainworkloadsmay
appearstableonaveragewhilestillexhibitingshort-liveddemandspikesthatsubstantially
increase operational risk. In these cases, average-based metrics can underestimate the
likelihood of transient overload events. Future work may therefore incorporate burst-
riskobjectivesbasedonwithin-windowvariability,combiningstatisticalmeasuressuchas
standarddeviation,thegapbetweenp95andmeandemand,andentropy-baseduncertainty
indicators,enablingmoreconservativeresizingdecisionsforspike-proneworkloads.
Anotherpromisingdirectionistoaccountforworkloadirregularityandunpredictabil-
ity. Evenwhenworkloadssharesimilarmeanandvariance,theirtemporalpatternscan
differsignificantly,leadingtodistinctoperationalimplications. Periodicfluctuationsand
irregulardemandpatternscallfordifferentadaptationstrategies,particularlyinlong-term
capacityplanningandautomatedcontrol. Incorporatingirregularity-awarepenaltyobjec-
tiveslinkedtoentropythresholdsortail-demandcriteriawouldallowresizingpoliciesto
explicitlydistinguishbetweenpredictableandunpredictableworkloads.
Beyondinstantaneousoverloadriskandreconfigurationfrequency,futurestudiesmay
alsoconsiderminimizingthetemporalvolatilityofresourceusagepatternsthemselves.
Stable and consistent usage trajectories offer practical benefits for monitoring, capacity
planning,andoperationalautomation. Volatility-orientedobjectivesthatcombinenormal-
izedstandarddeviationandentropymeasurescouldthereforefavorsolutionswithmore
consistentresourceusagewhencostefficiencyandaverageperformancearecomparable.
Theseextensionscanbesupportedthroughamulti-objectiveoptimizationperspective
thatsystematicallyexplorestrade-offsamongcostefficiency,stability,burstrisk,irregular-
ity,andvolatility. Pareto-frontanalysismaybeusedtocharacterizestructuraltrade-offs
andidentifybalancedoperatingregimes, whileobjectiveweightscouldbeextendedto
adaptive parameters responsive to workload characteristics or budget pressure. In ad-
dition,augmentingthecurrentwindow-baseddecisionstructurewithprediction-aware
mechanismsthatexploithistoricaltime-seriesinformationmayenablemoreproactiveand
robustresizingstrategies. Together,thesedirectionsprovideaclearpathwayforextending
theproposedbudget-awareframeworktowardmorerealisticandcomprehensivecloud
operationscenarios.
Funding:ThisresearchwassupportedbytheMSIT(MinistryofScience,ICT),Korea,undertheNa-
tionalProgramforExcellenceinSW,supervisedbytheIITP(InstituteforInformationcommunications
TechnologyPlanning&Evaluation)in2026(2021-0-01440).
DataAvailabilityStatement:Thedatasupportingthefindingsofthisstudyareavailablefromthe
correspondingauthoruponreasonablerequest.
ConflictsofInterest:Theauthordeclaresnoconflictsofinterest.
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 47of48
References
1. Mann,Z.Á.ResourceOptimizationAcrosstheCloudStack.IEEETrans.ParallelDistrib.Syst.2018,29,169–182.[CrossRef]
2. Sayadnavard, M.H.; ToroghiHaghighat, A.; Rahmani, A.M.AMulti-ObjectiveApproachforEnergy-EfficientandReliable
DynamicVMConsolidationinCloudDataCenters.Eng.Sci.Technol.Int.J.2022,26,100995.[CrossRef]
3. FinOpsFoundation.FinOpsFramework.Availableonline:https://www.finops.org/framework/(accessedon10March2026).
4. Amazon Web Services. AWS Budgets. Available online: https://aws.amazon.com/aws-cost-management/aws-budgets/
(accessedon10March2026).
5. Ren,R.;Tang,X.;Li,Y.;Cai,W.CompetitivenessofDynamicBinPackingforOnlineCloudServerAllocation.IEEE/ACMTrans.
Netw.2017,25,1324–1331.[CrossRef]
6. Guo,W.;Tian,W.;Ye,Y.;Xu,L.;Wu,K.CloudResourceSchedulingwithDeepReinforcementLearningandImitationLearning.
IEEEInternetThingsJ.2021,8,3576–3586.[CrossRef]
7. Osypanka,P.;Nawrocki,P.ResourceUsageCostOptimizationinCloudComputingUsingMachineLearning.IEEETrans.Cloud
Comput.2022,10,2079–2089.[CrossRef]
8. Yu,L.;Chen,L.;Cai,Z.;Shen,H.;Liang,Y.;Pan,Y.StochasticLoadBalancingforVirtualResourceManagementinDatacenters.
IEEETrans.CloudComput.2020,8,459–472.[CrossRef]
9. Mishra,S.K.;Sahoo,B.;Parida,P.P.LoadBalancinginCloudComputing:ABigPicture.J.KingSaudUniv.Comput.Inf.Sci.2020,
32,149–158.[CrossRef]
10. Alyahya,K.;Rowe,J.E.LandscapeAnalysisofaClassofNP-HardBinaryPackingProblems. Evol. Comput. 2019,27,47–73.
[CrossRef]
11. Moges,F.; Abebe,S.Energy-AwareVMPlacementAlgorithmsfortheOpenStackNeatConsolidationFramework. J.Cloud
Comput.2019,8,2.[CrossRef]
12. Ibrahim,A.;Noshy,M.;Ali,H.A.;Badawy,M.PAPSO:APower-AwareVMPlacementTechniqueBasedonParticleSwarm
Optimization.IEEEAccess2020,8,81747–81764.[CrossRef]
13. Shabeera, T.P.; Madhu Kumar, S.D.; Salam, S.M.; Murali Krishnan, K. Optimizing VM Allocation and Data Placement for
Data-IntensiveApplicationsinCloudUsingACOMetaheuristicAlgorithm.Eng.Sci.Technol.Int.J.2017,20,616–628.[CrossRef]
14. Liu,Y.;Gao,C.;Zhang,Z.;Lu,Y.;Chen,S.;Liang,M.;Tao,L.SolvingNP-HardProblemswithPhysarum-BasedAntColony
System.IEEE/ACMTrans.Comput.Biol.Bioinform.2017,14,108–120.[CrossRef]
15. Zhang,H.;Liu,W.;Zhang,Z.;Lu,W.;Xie,J.JointTargetAssignmentandPowerAllocationinMultipleDistributedMIMORadar
Networks.IEEESyst.J.2021,15,694–704.[CrossRef]
16. Taillandier,F.;Fernandez,C.;Ndiaye,A.RealEstatePropertyMaintenanceOptimizationBasedonMultiobjectiveMultidimen-
sionalKnapsackProblem.Comput.-AidedCiv.Infrastruct.Eng.2017,32,227–251.[CrossRef]
17. Corus,D.;Oliveto,P.S.;Yazdani,D.FastImmuneSystem-InspiredHypermutationOperatorsforCombinatorialOptimization.
IEEETrans.Evol.Comput.2021,25,956–970.[CrossRef]
18. Cai,W.;Chan,H.C.B.;Wang,X.;Leung,V.C.M.CognitiveResourceOptimizationfortheDecomposedCloudGamingPlatform.
IEEETrans.CircuitsSyst.VideoTechnol.2015,25,2038–2051.[CrossRef]
19. Xiao,H.;Hu,Z.;Li,K.Multi-ObjectiveVMConsolidationBasedonThresholdsandAntColonySysteminCloudComputing.
IEEEAccess2019,7,53441–53453.[CrossRef]
20. Nazir,J.;Iqbal,M.W.;Alyas,T.;Hamid,M.;Saleem,M.;Malik,S.;Tabassum,N.LoadBalancingFrameworkforCross-Region
TasksinCloudComputing.Comput.Mater.Contin.2022,70,1479–1490.[CrossRef]
21. Choi,Y.;Lim,Y.OptimizationApproachforResourceAllocationonCloudComputingforIoT.Int.J.Distrib.Sens.Netw.2016,
12,3479247.[CrossRef]
22. Zhang,X.;Wu,C.;Li,Z.;Lau,F.C.M.ATruthful(1−ε)-OptimalMechanismforOn-DemandCloudResourceProvisioning.IEEE
Trans.CloudComput.2020,8,735–748.[CrossRef]
23. Li,Y.;Zhao,C.;Tang,X.;Cai,W.;Liu,X.;Wang,G.;Gong,X.TowardsMinimizingResourceUsagewithQoSGuaranteeinCloud
Gaming.IEEETrans.ParallelDistrib.Syst.2021,32,426–440.
24. Kieffer,E.;Danoy,G.;Brust,M.R.;Bouvry,P.;Nagih,A.TacklingLarge-ScaleandCombinatorialBi-LevelProblemswithaGenetic
ProgrammingHyper-Heuristic.IEEETrans.Evol.Comput.2020,24,44–56.[CrossRef]
25. Solozabal,R.;Ceberio,J.;Sanchoyerto,A.;Zabala,L.;Blanco,B.;Liberal,F.VirtualNetworkFunctionPlacementOptimization
withDeepReinforcementLearning.IEEEJ.Sel.AreasCommun.2020,38,292–303.
26. JafarnejadGhomi,E.;Rahmani,A.M.;Qader,N.N.ServiceLoadBalancing,Scheduling,andLogisticsOptimizationinCloud
ManufacturingbyUsingGeneticAlgorithm.Concurr.Comput.Pract.Exp.2019,31,e5329.[CrossRef]
27. Gamsiz,M.;Özer,A.H.AnEnergy-AwareCombinatorialVirtualMachineAllocationandPlacementModelforGreenCloud
Computing.IEEEAccess2021,9,18625–18648.[CrossRef]
28. Wan,B.;Dang,J.;Li,Z.;Gong,H.;Zhang,F.;Oh,S.ModelingAnalysisandCost-PerformanceRatioOptimizationofVirtual
MachineSchedulinginCloudComputing.IEEETrans.ParallelDistrib.Syst.2020,31,1518–1532.[CrossRef]
https://doi.org/10.3390/app16073302

Appl.Sci.2026,16,3302 48of48
29. Sardaraz,M.;Tahir,M.AParallelMulti-ObjectiveGeneticAlgorithmforSchedulingScientificWorkflowsinCloudComputing.
Int.J.Distrib.Sens.Netw.2020,16,1550147720949142.[CrossRef]
30. Zuo, L.; Shu, L.; Dong, S.; Zhu, C.; Hara, T.AMulti-ObjectiveOptimizationSchedulingMethodBasedontheAntColony
AlgorithminCloudComputing.IEEEAccess2015,3,2687–2699.[CrossRef]
31. Shrimali,B.;Patel,H.Multi-ObjectiveOptimizationOrientedPolicyforPerformanceandEnergyEfficientResourceAllocationin
CloudEnvironment.J.KingSaudUniv.Comput.Inf.Sci.2020,32,860–869.[CrossRef]
32. Konjaang,J.K.;Xu,L.Multi-ObjectiveWorkflowOptimizationStrategy(MOWOS)forCloudComputing.J.CloudComput.2021,
10,11.[CrossRef]
33. Yousefipour,A.;Rahmani,A.M.;Jahanshahi,M.EnergyandCost-AwareVirtualMachineConsolidationinCloudComputing.
Softw.Pract.Exp.2018,48,1758–1774.
34. Kim,I.K.;Wang,W.;Qi,Y.;Humphrey,M.ForecastingCloudApplicationWorkloadswithCloudInsightforPredictiveResource
Management.IEEETrans.CloudComput.2022,10,1848–1863.[CrossRef]
35. Cohen,M.C.;Keller,P.W.;Mirrokni,V.;Zadimoghaddam,M.OvercommitmentinCloudServices: BinPackingwithChance
Constraints.Manag.Sci.2019,65,3255–3271.[CrossRef]
36. Wu,Q.;Ishikawa,F.;Zhu,Q.;Xia,Y.;Wen,J.Deadline-ConstrainedCostOptimizationApproachesforWorkflowSchedulingin
Clouds.IEEETrans.ParallelDistrib.Syst.2017,28,3401–3412.[CrossRef]
37. Duque, R.; Arbelaez, A.; Díaz, J.F.OnlineOverTimeProcessingofCombinatorialProblems. Constraints2018, 23, 310–334.
[CrossRef]
38. Thanasias,V.;Lee,C.;Hanif,M.;Kim,E.;Helal,S.VMCapacity-AwareSchedulingwithinBudgetConstraintsinIaaSClouds.
PLoSONE2016,11,e0160456.[CrossRef]
39. Rizvi, N.; Ramesh, D. HBDCWS: Heuristic-Based Budget and Deadline Constrained Workflow Scheduling Approach for
HeterogeneousClouds.SoftComput.2020,24,18971–18990.[CrossRef]
40. Rajasekar,P.;Santhiya,P.Budget-BasedResourceProvisioningandSchedulingAlgorithmforScientificWorkflowsonIaaSCloud.
Multimed.ToolsAppl.2024,83,50981–51007.
41. Radhika,E.G.;Sadasivam,G.S.BudgetOptimizedDynamicVirtualMachineProvisioninginHybridCloudUsingFuzzyAnalytic
HierarchyProcess.ExpertSyst.Appl.2021,183,115398.[CrossRef]
42. Arabnejad,H.;Barbosa,J.G.ABudgetConstrainedSchedulingAlgorithmforWorkflowApplications. J.GridComput. 2014,
12,665–679.[CrossRef]
43. Xiao, L.; Xiao, Z.; Wu, D.; Hu, M.; Zhou, Y. CRS: A Cost-Aware Resource Scheduling Framework for Deep Learning Task
OrchestrationinMobileClouds.IEEETrans.Mob.Comput.2025,24,600–613.
44. Bandapati, G. FinOps-Driven Strategies for Large-Scale Cloud Cost Optimization. Int. J. Intell. Syst. Appl. Eng. 2024,
12,2203–2209.
45. GoogleCluster-UsageTraces.Availableonline:https://github.com/google/cluster-data/(accessedon10March2026).
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.
https://doi.org/10.3390/app16073302