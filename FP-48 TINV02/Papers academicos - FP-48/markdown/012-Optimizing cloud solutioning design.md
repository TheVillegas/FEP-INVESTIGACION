Accepted Manuscript
Optimizingcloudsolutioningdesign
AlyMegahed,AhmedNazeem,PeifengYin,SamirTata,HamidReza
MotahariNezhad,TaigaNakamura
PII: S0167-739X(18)30615-0
DOI: https://doi.org/10.1016/j.future.2018.08.005
Reference: FUTURE4389
Toappearin: FutureGenerationComputerSystems
Receiveddate: 20March2018
Reviseddate: 30June2018
Accepteddate: 3August2018
Pleasecitethisarticleas:,Optimizingcloudsolutioningdesign,FutureGenerationComputer
Systems(2018),https://doi.org/10.1016/j.future.2018.08.005
ThisisaPDFfileofanuneditedmanuscriptthathasbeenacceptedforpublication.Asaserviceto
our customers we are providing this early version of the manuscript. The manuscript will undergo
copyediting, typesetting, and review of the resulting proof before it is published in its final form.
Please note that during the production process errors may be discovered which could affect the
content,andalllegaldisclaimersthatapplytothejournalpertain.

Optimizing Cloud Solutioning Design
Aly Megahed , Ahmed Nazeem , Peifeng Yin , Samir Tata , Hamid Reza
∗ ∗∗ ∗ ∗
∗∗
Motahari Nezhad and Taiga Nakamura
∗∗∗∗ ∗
IBMResearch-Almaden,
650HarryRd,SanJose,CA95120,USA
∗{ aly.megahed,peifengy,taiga } @us.ibm.com,∗∗ahmed.nazeem@ibm.com,
∗∗∗samir.tata@gmail.com,∗∗∗∗motahari@ieee.org
Abstract
The economics of the cloud model has been encouraging IT enterprises to mi-
gratefromon-premiseenvironmentstopublic,private,orhybridcloudsolutions.
To perform such a migration, a cloud offering needs to be chosen and a cloud
solution needs to be built. In industrial settings, cloud designers may spend
days or even weeks to come up with an acceptable cloud solution with at a low
cost/price. Like any manual process, it is obvious that such a cloud solution
design process is error prone, time consuming, and does not guarantee an opti-
mal output, e.g. a solution with a minimum cost/price. Different from existing
works that solve the problem from the user’s angle, we solve it from the cloud
provider’s prospective, who aims at offering customized cloud solutions for dif-
ferent user requirements at low costs. Such difference requires a unique way
of problem modeling. Through analyzing real business data, we abstract the
problem into a general attribute-value combinations and formulate a powerful
integer programming optimization model to solve it. The general form of the
optimization model allows various definitions of customer requirements as well
as cloud offerings. Our novel optimization approach for cloud solution design
satisfies client requirements, cloud offering constraints, and produces a solution
at a minimum cost in a short time, if one exists. We evaluated our solution on
realisticdataagainsttwobaselineapproaches. Thenumericalresultsshowboth
theeffectivenessandefficiencyofourapproachaswellasitspracticalpotential.
Keywords:
PreprintsubmittedtoFutureGenerationComputerSystems,TheInternationalJournalofeScienceJune29,2018

| Cloud Solution | Design; Cloud | Computing; |            | Optimization; | Integer |     |     |
| -------------- | ------------- | ---------- | ---------- | ------------- | ------- | --- | --- |
| Programming;   | Operations    | Research;  | Heuristics |               |         |     |     |
1. Introduction
CloudComputingisgainingmomentumintheInformationTechnology(IT)
scopeasanemergingcomputingparadigmformanaginganddeliveringservices
over the internet [1]. Due to its economic model based on pay-as-you-go plans,
5 IT enterprises are shifting from on-premise environments to public, private,
or hybrid clouds. Indeed, cloud environments have presented novel application
deploymentmodelsofferingmoreconvenientcosts,highavailability,andflexible
elasticity.
| Over the | last few years, | the rate | of  | adoption of | cloud computing | and | specif- |
| -------- | --------------- | -------- | --- | ----------- | --------------- | --- | ------- |
ically managed cloud hosting and migration among enterprise customers has
10
actuallyacceleratedsignificantly. Intheenterprisemarketplace,managedcloud
servicesarecommoninwhichanenterprisemigratessomeorallitsapplications
fromtheirowndatacenterstocloudandexpectsthecloudproviderstomanage
| it for them | [2].       |          |     |               |          |          |     |
| ----------- | ---------- | -------- | --- | ------------- | -------- | -------- | --- |
| The problem | of hosting | workload | of  | an enterprise | customer | (whether | new |
15
workloadormigration)intoanenterprisecloudserviceproviderisacomplexand
challenging problem. This is because the hosting entails provision of compute
resources(e.g.,virtualmachines),storage,andnetwork,andplatformresources
to host and run client applications with desired service levels on potentially
shared infrastructure components. The managed cloud hosting calls for mon-
20
itoring and management tools at various levels from infrastructure, compute,
storage, networking and application levels to provide transparency and moni-
| toring of such | service levels. |          |     |              |                   |     |         |
| -------------- | --------------- | -------- | --- | ------------ | ----------------- | --- | ------- |
| The migration  | job, in         | addition | to  | new workload | hosting, requires |     | analyz- |
ingtheexistingcustomerworkload,andinfrastructureneedsandconfigurations
25
and map, upgrade or optimize those in the service provider’s provisioning en-
vironment which adds to the complexity. Last but not least, the price of cloud
2

migrationorhostingjobforacustomer,andcostofrunningsuchaworkloadfor
theserviceprovider,isakeyfactoranddriverofanycloudhostingormigration
task.
30
Any cloud hosting or migration project entails a technical solution design
phase. The proposed technical solution to an enterprise customer details the
required compute, storage, networking, platform, application, monitoring and
management applications and resources along with associated service levels for
each. Thesolutiondesignprocessstartswithcapturinganddocumentingclient
35
requirements. The requirements include IT requirements, i.e. the specification
of the needed IT resources (at all level of stack from infrastructure to appli-
cation), or existing client environment (in case of a migration project), and
business-level requirements and objectives. While there are multiple business
level objectives, the most common is cost saving as the result of migrating to
40
or adopting cloud, as opposed to on-premise data center operation.
Inlargeclientcloudhostingormigrationprojects,solvingthesolutiondesign
problemisacomplexandtedioustask. ThisisbecausegivenaspecificclientIT
requirement, and different solution components and cloud delivery locations of
aserviceprovider,itisoftenpossibletogeneratemultiplesolutionalternatives.
45
Generating a detailed technical solution design for a cloud project can take a
team of IT architects days or weeks (depending on the scope and complexity of
requirements). Also, it is not guaranteed that the solution architects can find
the optimal (or the best alternative that is available among multiple possible
solutions) after such an exercise, both in terms of price for the customer and
50
cost of solution delivery for the client.
Theproblemthatwetackleinthispaperisthatofautomaticallycomputing
a cost optimized cloud solution for a given client IT requirements (including
thedeliverylocations,andalllevelsofinfrastructureandapplicationsneeds)by
finding the optimized combination of solution components, from a cost point of
55
view, offered by a service provider that meets client’s requirements. We model
ITrequirementsofaclientasasetofconstraintsexpressedoveragenericmodel
of functional and non-functional requirements of IT resources and applications.
3

Thesolutionelementsoftheserviceproviderareexpressedoveragenericcloud
60 IT resources model. In this model, various capabilities are modeled as objects
withtheirvariationsintermsofdifferentacceptablevaluesforanygivenobject’s
attribute. There are also solutioning rules that constrain value selection and
| enforce generation | of valid solution | combinations. |          |              |        |               |
| ------------------ | ----------------- | ------------- | -------- | ------------ | ------ | ------------- |
| In the literature, | while there       | are           | multiple | works (e.g., | [3, 4, | 5]) that come |
up with a price optimized solution for a client in leveraging a public cloud
65
resources (some by considering the mix of on-demand and reserved resources
(e.g. [3]), they all tackle the problem from a cloud client or consumer point
of view. In this paper, we propose a novel cloud solution design approach that
includesamathematicaloptimizationmodelthatproducesacloudsolutionwith
an optimal/minimum cost, from the service provider’s point of view. The key
70
advantage of our method is proposing a generic model for IT requirements and
cloudofferingsandsolutionelementsoverwhichcustomizedclientrequirements
canbeexpressed,andformulatetheproblemofcostoptimizedsolutiondesignas
anintegerprogrammingproblem. Wehaveimplementedtheproposedapproach,
andpresenttheresultofexperimentsandevaluationthatshowsthepracticality
75
| of the proposed | solution.              |     |             |         |            |           |
| --------------- | ---------------------- | --- | ----------- | ------- | ---------- | --------- |
| The rest        | of paper is structured |     | as follows. | Section | 2 presents | the state |
of the art related to the issue of migrating local IT environments to cloud
platforms. We then detail our optimization-based approach for cloud solution
designinSection3. Section4presentstheimplementationofourapproachand
80
itsexperimentationwithrespecttotwobaselinesolutionmethodsthatwehave
also implemented. Finally, Section 5 concludes our paper and presents some
| directions for   | future research. |            |       |          |             |            |
| ---------------- | ---------------- | ---------- | ----- | -------- | ----------- | ---------- |
| 2. Literature    | Review           |            |       |          |             |            |
| Many enterprises | choose           | to migrate | their | local IT | environment | to a cloud |
85
platformduetoitsadvantageonflexiblescalabilityandlowcost. Themigration
process also attracts researchers’ attention and many works focus on solving
4

different research issues.
Earlyworksareusuallyareportorcasestudy,analyzingthewholemigration
processofaparticularapplication/environment. In[6],BarkerandShenoygave
90
an empirical study of running latency-sensitive applications in cloud environ-
ment and reported nearly 75% service quality degrade for disk-bound latency-
sensitive tasks. In [7], Khajeh-Hosseini et. al. studied the migration of an IT
system in oil & gas industry in terms of the benefit and risk. In [8, 9], au-
thorsreportedtheexperienceofmigratingHackystat,anOpenSourceSoftware
95
(OSS) framework, to the cloud. A more recent work [10] surveyed undergradu-
ate students to reveal factors impacting end users’ switch to cloud.
Consideringbothbenefitandrisk, manyworksdevelopdiversifiedtoolsand
frameworkstofacilitatethedecisionmakingprocess. Lewiset. al.[11]developed
SMART methods to help enterprise determine their service functionality when
100
migratingtoaservice-orientedarchitecture(SOA)cloud. MisraandMondal[12]
proposedaReturnonInvestment(ROI)modeltoanalyzecompanies’scostand
benefit when incorperating cloud into their business. Saripalli and Pingali [13]
applythemultipleattributedecisionmethodologytohelpdecisionmakingwith
respect to different cloud decision objectives. In [14], a general decision pro-
105
cess, CloudStep, is presented to support legacy application migration to cloud.
Otherworksfocusonaparticularfactorsuchascostofdeployment[15,16],net-
work[17],securityandprivacy[18,19,20]. Particularlyin[21],Jamshidiet. al.
gave a literature review of selected 23 works on cloud migration, summarizing
itsmajormotivations,existingmethodsandtechniquesaswellaspredictingfu-
110
ture research dimensions. To bridge migration gap, TOSCA [22] was designed
to represent the application’s topology. Furthermore, Bergmayr et. al. [23]
developed CAML, a UML-based language to express deployments in cloud.
Besideshigh-levelanalysisandtheoreticalmodeling,thereareworksaiming
at reconfiguration of existing systems when migrated to cloud. In [24], Frey et.
115
al. showtheunmodifiedsystemhasscalabilityissues(eitherunder-provisionor
over-provision) after migrating to cloud. They propose several heuristic rules
to improve resource efficiency. In [25], a utility function was defined to find
5

optimal distribution of an application in cloud. Trummer et. al. [4] model the
120 applicationdeploymentasaconstraint-satisfyingoptimizationproblemandrely
on the constraint solver to get optimal solution in terms of cost. Aniceto et.
al.[3]aimatoptimizingthemixtureofon-demandandreservedinstanceincloud
to cover variable computation tasks at minimum cost. In [5], an auto-scaling
mechanism is proposed for VM start-up and shut-down activities in order to
completescientificcomputationtaskswithintimeandbudgetconstraints. Other
125
worksadoptdiversifiedtechniquessuchasevolutionaryoptimization[26,27,28],
particle swarm optimization [29], multi-goal genetic search algorithm [30], and
so on.
| In this | work, we also | focus on | the optimization | problem. However, | different |
| ------- | ------------- | -------- | ---------------- | ----------------- | --------- |
fromexistingworksthatsolvetheproblemfromtheuserangle,wesolveitfrom
130
the aspect of a cloud provider, who aims to offer customized cloud solutions
for different user requirements at low cost. Such difference requires a unique
way of problem modeling. By analyzing real business data, we abstract it into
a general attribute-value combination problem and take advantage of powerful
integer programming to solve it. The general form of the optimization model
135
allows variant definitions of customer requirements as well as cloud offerings.
| Evaluation      | shows promising     | results  | and practical | potential.                    |     |
| --------------- | ------------------- | -------- | ------------- | ----------------------------- | --- |
| 3. Approach     | for Cloud           | Solution | Design        |                               |     |
| 3.1. Approach   | Overview            |          |               |                               |     |
| Cloudproviders, | suchasIBMandAmazon, |          |               | delivermultipleCloudofferings |     |
140
thatprovideusersandcompanieswithaccesstoanintegratedsetofmanagedIT
resources including infrastructure, platform and applications. Managed IT in-
frastructureresourcesincludevirtualmachinesandnetwork. Managedplatform
| resources include | middleware | and | database. |     |     |
| ----------------- | ---------- | --- | --------- | --- | --- |
145 Thegeneralprocessacloudproviderfollowstodeliveracloudsolutionispre-
sented in Figure 1. It consists in three steps: Requirement capturing, Solution
| design and | Delivery specification. |     |     |     |     |
| ---------- | ----------------------- | --- | --- | --- | --- |
6

|     | 3.1.1. Step | 1:  | Requirement | capturing |     |     |     |     |     |     |
| --- | ----------- | --- | ----------- | --------- | --- | --- | --- | --- | --- | --- |
Cloud
|     | Client  |     |     |     |     |     |     |     | Provisioning |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |
Offering
|     | Requirements |     |     |     |     |     |     |     | Constraints |     |
| --- | ------------ | --- | --- | --- | --- | --- | --- | --- | ----------- | --- |
Constraints
|     | Step 1:     |     |     |     | Step 2:  |     |     |     | Step 3: |     |
| --- | ----------- | --- | --- | --- | -------- | --- | --- | --- | ------- | --- |
|     | Requirement |     |     |     | Solution |     |     |     |         |     |
Delivery
|     | Capturing |            |            |                                    | Design  |           |     |        | Specification |     |
| --- | --------- | ---------- | ---------- | ---------------------------------- | ------- | --------- | --- | ------ | ------------- | --- |
|     |           |            | Figure1:   | ApproachOverviewofCloudSolutioning |         |           |     |        |               |     |
|     | The       | first step | in a cloud | sales                              | deal is | capturing | the | client | requirements  | in- |
150 cludingapplicationhosting,infrastructureneeds,servicelevelrequirements,the
needfordisasterrecovery,databaseresiliency,backup,etc. Thisconsistsincon-
sidering a set of attributes that characterize cloud offerings. The requirement
consists in a set of constraints on the values those attributes can take. For ex-
ample, if we consider a VMware offering in IBM Cloud, we may consider a set
of attributes to formally describes the offering. These attributes may include:
155
|     | the | data | center selected |     | by the client | to host | his/her | workloads, |     |     |
| --- | --- | ---- | --------------- | --- | ------------- | ------- | ------- | ---------- | --- | --- |
•
|     | the | VMware | offering | type, | with values | such | as vCenter | and | vSphere, |     |
| --- | --- | ------ | -------- | ----- | ----------- | ---- | ---------- | --- | -------- | --- |
•
|     | the | number | of clusters | requested | by  | the client, |     |     |     |     |
| --- | --- | ------ | ----------- | --------- | --- | ----------- | --- | --- | --- | --- |
•
|     | the | number | of virtual | machines | per | cluster | to migrate |     | and their | charac- |
| --- | --- | ------ | ---------- | -------- | --- | ------- | ---------- | --- | --------- | ------- |
•
| 160 | teristics |        | in terms   | of CPU, | RAM and | storage, |           |         |     |        |
| --- | --------- | ------ | ---------- | ------- | ------- | -------- | --------- | ------- | --- | ------ |
|     | the       | server | size, with | values  | such as | Small,   | Standard, | Medium, | and | Large, |
•
|     | the | server | total cores | of  | a server, |     |     |     |     |     |
| --- | --- | ------ | ----------- | --- | --------- | --- | --- | --- | --- | --- |
•
|     | the | storage | type, with | values | such | as VSAN, | Endurance |     | and ISA, |     |
| --- | --- | ------- | ---------- | ------ | ---- | -------- | --------- | --- | -------- | --- |
•
|     | the | operation | System, | with | values | such as | AIX, RHL | and | Win, |     |
| --- | --- | --------- | ------- | ---- | ------ | ------- | -------- | --- | ---- | --- |
•
|     | the | Disaster | Recovery, | with | values | such as | Yes and | No. |     |     |
| --- | --- | -------- | --------- | ---- | ------ | ------- | ------- | --- | --- | --- |
165 •
7

etc.
•
| 3.1.2. Step | 2:     | Solution design |                    |     |             |         |     |           |
| ----------- | ------ | --------------- | ------------------ | --- | ----------- | ------- | --- | --------- |
| The         | second | step, within    | cloud solutioning, |     | is solution | design. |     | This step |
consistsindeterminingthesetofaccepted/possiblevaluesofthelistofattributes
| that describe | the | considered | cloud offering. |     |     |     |     |     |
| ------------- | --- | ---------- | --------------- | --- | --- | --- | --- | --- |
170
| Beside | client | requirement | that define | attribute | values | to be | included | or to |
| ------ | ------ | ----------- | ----------- | --------- | ------ | ----- | -------- | ----- |
be excluded in the solution, there are cloud offering constraints that should
be also satisfied by the solution. There are mainly two types of cloud offering
constraints. Thefirsttypeconcernstheconstraintsthatdefinesetsofcombina-
tions of attributes and their corresponding values that must be either included
175
together or excluded together in the solution. For example, let’s consider the
attributesserversizeandservertotalcoreswiththecorrespondingvaluesSmall
and 12. This combination of attributes and values are either included together
or excluded together in the solution. The second type of cloud offering con-
straints concerns constraints that define sets of combinations of attributes and
180
their values are never included together in the solution. For example, not all
VMware offerings are available in all possible data centers, not all server sizes
| are available | with        | all VMware             | offerings.    |     |          |             |           |     |
| ------------- | ----------- | ---------------------- | ------------- | --- | -------- | ----------- | --------- | --- |
| 3.1.3. Step   | 3:          | Delivery specification |               |     |          |             |           |     |
| The           | third step, | consists               | in specifying | the | delivery | information | necessary | to  |
185
provision the designed cloud solution. This specification includes the point of
delivery, or PoD, where the servers will be provisioned, the IP addresses of
servers, etc.
| 3.2. Need | for optimization |       |                 |     |         |               |     |          |
| --------- | ---------------- | ----- | --------------- | --- | ------- | ------------- | --- | -------- |
| In the    | general          | case, | solution design | may | come up | with multiple |     | possible |
190
solutions that satisfy client requirements and cloud offering constraints. The
differencebetweenthesesolutionswouldbethecost/price. Inindustrialsettings,
clouddesignersmayspendapproximativelyonedaytocomeupwithasolution
with a reduced cost. It is obvious that such a process is error prone, is time
8

consuming and does not guarantee an optimal solution, e.g. a solution with a
195
| minimum | cost. |     |     |     |     |     |     |     |
| ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Theobjectiveofthispaperistotackletheseissues,byprovidinganoptimiza-
tion model for cloud solution design that satisfy client requirements and cloud
offering constraints and producing a solution, if there is any, with a minimum
| 200 cost in a  | reasonable   | time.    |              |              |           |         |                 |       |
| -------------- | ------------ | -------- | ------------ | ------------ | --------- | ------- | --------------- | ----- |
| 3.3. Problem   | Abstraction  | and      | Optimization | Model        |           |         |                 |       |
| In this        | subsection,  | we first | abstract     | our problem, |           | then we | present the     | nota- |
| tion of our    | optimization | model,   | and          | finally we   | formulate | that    | model.          |       |
| 3.3.1. Problem | Abstraction  |          |              |              |           |         |                 |       |
| There          | are multiple | solution | attributes.  | We           | denote    | the     | set of solution | at-   |
205
tributes as the set S. For each solution attribute s S, there are multiple
∈
possible values that can be chosen. However, in the solution to be proposed to
the client, only one of these values (or none) is chosen for each attribute. Let
| the set V | be the set | of possible | values | for attribute | s   | S.  |     |     |
| --------- | ---------- | ----------- | ------ | ------------- | --- | --- | --- | --- |
s
∈
| There | is an associated | cost | codes | for multiple | combinations |     | of values | for a |
| ----- | ---------------- | ---- | ----- | ------------ | ------------ | --- | --------- | ----- |
210
subset of the attributes. Let the set of cost codes be F. Each cost code f F
∈
has a cost cost and the total solution cost is the sum of the costs of all cost
f
codes that are enabled in the solution. A cost code is enabled whenever all of
the combinations it is defined upon are included in the solution. For each cost
code f F, we define a set C for all combinations of attributes and their
| 215 |     |     | f   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
∈
values that enable it. That is, an element (v,s) C is a tuple of the attribute
|     |     |     |     |     | ∈ f |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
s S and its corresponding value v V that form one of the enablers of that
s
| ∈         |      |     |     | ∈   |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| cost code | f F. |     |     |     |     |     |     |     |
∈
| We define | the | set NA as | the set | of combinations |     | of all attributes | s   | S and |
| --------- | --- | --------- | ------- | --------------- | --- | ----------------- | --- | ----- |
∈
their corresponding values v V that are not allowed to be in our solution.
| 220 |     |     | ∈ S |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Similarly,wedefinethesetMI asthesetofcombinationsofattributess Sand
∈
theircorrespondingvaluesv V s thatmustbeincludedinthecurrentsolution.
∈
Set IT is the set of combinations of attributes and their corresponding values
9

thatmustbeeitherincludedtogetherorexcludedtogetherinthesolution. That
is, for each element (s,v,s,v ) of this set, if solution attribute s S and its
225 0 0
∈
corresponding value v V is included in the solution, then attribute s S,
s 0
∈ ∈
with its corresponding value v V , must be included in the solution, while if
0
∈
s0
the former is not included, the latter must be excluded, too. Additionally, set
IF includesthesetsofcombinationsofpairsofattributesandtheirvaluesthat
enables the following logic: For each element (set) in IF, if all attribute and
230
their values, except for the last attribute/value, are included in the solution,
thenthatlastattributeanditsvaluehavetobeincludedinthesolutionaswell.
Obviously, each element/set in IF has to be ordered (at least its last element
has to always exist last) to enable this logic. Further, set IFN includes the
forbidden combinations. That is, it contains the sets of combinations of pairs
235
of attributes and their values that cannot be included together in the solution.
Each element in this set is a set of pairs of 2 or more attribute/values.
We note that in any particular problem instance, not all the sets/logic we
defined above are necessarily included. So, in a problem instance, either none,
some, or all of the sets/logic we discuss here would be applicable. We include
240
all of them in our model to be able to handle the most general case, while
noting that including or excluding any of the constraints below does not affect
the solution time of our model for realistic instances as we will see in the next
sectionbelow. Table1summarizesthesetsusedinourmodel. Apartfromthese
aforementioned sets, the only other parameter/data input to the model is the
245
cost code values, cost , for each cost code f F.
f
∈
Withtheaforementioneddynamics, ourproblembecomes: whichattributes
and their values should be included in the soltion in order to minimize the to-
tal solution cost while satisfying all the given solution constraints? To solve
thisproblem,weformulateandsolveanintegerprogramming(IP)optimization
250
model. Wenextprovidethenotationforourmodelthenpresentitsmathemat-
ical formulation.
10

Table1: SetsofOurOptimizationModel
Set Name Set Description
S Set of solution attributes
V s Set of values for solution attribute s S
∈
F Set of cost codes
Set of pairs all attributes and their corresponding values that
C
f
enable cost code f F
∈
Set of pairs of all attributes and their corresponding values
NA
that are not allowed to be in our solution
Set of paris of all attributes and their corresponding values
MI
that must be included in our solution
Setofquintuples(s,v,s,v )ofattributesandtheircorrespond-
0 0
ing values that must be either included together Or excluded
IT
together in the solution, i.e., either (s,v) and (s,v ) are in-
0 0
cluded in the solution together, or both are excluded together
Set of combinations of attributes and their corresponding val-
ues that are required to follow the following logic: For each
element i IF, where i = (s ,v ),...,(s ,v ) , if all pairs
1 1 i i
IF ∈ { }
of (attribute, value) in i, except for (s ,v ) are included in the
i i
solution, then (s ,v )has tobe includedin itas well. i is the
i i
| |
cardinality of i IF
∈
Set of forbidden combinations of (attribute, value) pairs, i.e.,
combinations of (attributes, value) pairs that cannot be in-
IFN cluded simultaneously in the solution. Each element i of this
set is a set of two or more (attribute, value) pairs (s,v) : s
∈
S,v V . i is the cardinality of i IFN
s
∈ | | ∈
3.3.2. Model Notation
We define the following three sets of binary decision variables before formu-
lation our optimization model to solve our problem: variable Y is 1, if value
255 vs
11

v V forattributes S isincludedinoursolution,andzero,otherwise. Vari-
| ∈ s | ∈   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
able X f is 1, if cost code f F is enabled in our solution, and zero, otherwise.
∈
Variable cSlack is 1 if attribute s S is fulfilled in a customized way, and
|     | s   |     | ∈   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
zero otherwise. The reason we defined that latter variable is because not all
combination of attribute-values have a feature code. Such combinations lead
260
to customized solutions with custom and more expensive costs. That is why,
typically,solutiondesignerstrytousethefewestpossiblenumberofthesecom-
binations. Thewaywemodelthisisbyaddingthatbinaryvariablerepresenting
eachofthecustomizedattribute-valuecombinationschosenintheoptimalsolu-
265 tion,alongwithahighpenaltytominimizethechoiceofthesecustomsolutions
asmuchaspossible. Table2summarizesthedecisionvariablesofoursolutionn
model.
|     | Table2: | DecisionVariablesofOurOptimizationModel |     |     |     |     |
| --- | ------- | --------------------------------------- | --- | --- | --- | --- |
Variable
|     |     |     | Variable | Description |     |     |
| --- | --- | --- | -------- | ----------- | --- | --- |
Name
|     | 1, if value | v   | V for attribute | s S | is included | in our |
| --- | ----------- | --- | --------------- | --- | ----------- | ------ |
s
|     |     | ∈   |     | ∈   |     |     |
| --- | --- | --- | --- | --- | --- | --- |

Y
| vs  |  solution, | and |     |     |     |     |
| --- | --------------- | --- | --- | --- | --- | --- |
0 otherwise
1,attribute
|     |     | s   | S is fulfilled | in a customized |     | way, and |
| --- | --- | --- | -------------- | --------------- | --- | -------- |
∈
| cSlack s |    |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
0, otherwise
|     | 1, if cost | code | f F is enabled | in our | solution, | and |
| --- | ------------ | ---- | -------------- | ------ | --------- | --- |
| X   |              |      | ∈              |        |           |     |
| f   |             |      |                |        |           |     |
0, otherwise

| 3.3.3. Model | Formulation |             |        |                 |       |             |
| ------------ | ----------- | ----------- | ------ | --------------- | ----- | ----------- |
| We now       | present the | formulation | of our | IP optimization | model | as follows: |
12

|     | Min |     | cost f | .X f +cutomizationPenalty |     |     | cSlack s | (1) |
| --- | --- | --- | ------ | ------------------------- | --- | --- | -------- | --- |
∗
|     |     | f    | F    |       |     |     | s S |     |
| --- | --- | ---- | ---- | ----- | --- | --- | --- | --- |
|     |     | X∈   |      |       |     |     | X∈  |     |
|     |     | s.t. | Y vs | =1, s | S   |     |     | (2) |
|     |     |      |      | ∀     | ∈   |     |     |     |
v Vs
X∈
|     |     | X   |        | Y   | (C  | 1), f | F   | (3) |
| --- | --- | --- | ------ | --- | --- | ----- | --- | --- |
|     |     |     | f      | vs  | f   |       |     |     |
|     |     |     | ≥      | −   | |   | |− ∀  | ∈   |     |
|     |     |     | (v,Xs) | Cf  |     |       |     |     |
∈
|     |     | X      | f Y vs      | f F,(v,s)     |         | C f     |          | (4)  |
| --- | --- | ------ | ----------- | ------------- | ------- | ------- | -------- | ---- |
|     |     |        | ≤           | ∀ ∈           |         | ∈       |          |      |
|     |     |        |             | X f           | +cSlack | s 1,    | s S      | (5)  |
|     |     |        |             |               |         | ≥ ∀     | ∈        |      |
|     |     | f      | F, vX:(v,s) | Cf            |         |         |          |      |
|     |     | ∈      | ∃           | ∈             |         |         |          |      |
|     |     | Y      | =0,         | (s,v)         | NA      |         |          | (6)  |
|     |     | vs     |             | ∀ ∈           |         |         |          |      |
|     |     | Y      | =1,         | (s,v)         | MI      |         |          | (7)  |
|     |     | vs     |             | ∀ ∈           |         |         |          |      |
|     |     | Y      | =Y          | , (s,v,s0,v0) |         | IT      |          | (8)  |
|     |     | vs     | v0s0        | ∀             |         | ∈       |          |      |
|     |     |        |             | Y             |         | (i 2) Y | , i IF   | (9)  |
|     |     |       |             | vs            | −      | | |− ≤  | visi ∀ ∈ |      |
|     |     |        | (s,v) iX\{  | (si,vi)       |         |         |          |      |
|     |     |        | ∈           | }             |         |         |          |      |
|     |     |       |             |               |        |         |          |      |
|     |     |        | Y           | i 1,          | i       | IFN     |          | (10) |
|     |     |        | vs          | ≤| |−         | ∀       | ∈       |          |      |
|     |     | (sX,v) | i           |               |         |         |          |      |
∈
|     |     | X   | 0,1 | , f | F   |     |     | (11) |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- |
f
|       |           |     | ∈{       | } ∀ ∈       |     |           |                       |       |
| ----- | --------- | --- | -------- | ----------- | --- | --------- | --------------------- | ----- |
|       |           | Y   | 0,1      | , s         | S,  | v V       |                       | (12)  |
|       |           | vs  |          |             |     | s         |                       |       |
|       |           |     | ∈{       | } ∀ ∈       | ∀   | ∈         |                       |       |
| Where | objective |     | function | 1 minimizes |     | the total | cost of the solution, | which |
270
is the sum of the costs of all cost codes included in that solution in addition to
a customization penalty for selecting attribute values that are not part of any
selectedcostcode. Constraint2ensuresthatexactlyonevalueischosenforeach
solutionattribute. Constraints3and4setthelogicofenablingacostcode. That
is, a cost code is enabled if and only if all combinations of attributes and their
275
values, that enable that cost code, are included in the solution. Constraint 5
forcesthecustomizationpenaltyofanattributetooneifnocostcodethatcovers
this attribute is enabled in the solution. Constraint 6 ensures that attributes
and their values, that are not wanted by the client, are not included in the
280 solution. Similarly, constraint 7 forces attribute values, requested by the client,
13

to be included in the solution. Constraint 8 ensures that for each quintuples in
set IT, the corresponding attributes and values are either included together or
excludedtogether. Constraint9guaranteestherequiredlogicforsetIF,where
for each element in that set, if all attribute/value combinations in it, except
the last one, are included in the solution, then that last one has to be included
285
there as well. The logic corresponding to set IFN is captured in constraint
10, wherein if value v V is included in the solution for attribute s, then
s
∈
value v V is included in the solution for attribute s cannot be included in
∈
s0 0
the solution. Lastly, constraints 11 and 12 are the binary constraints for our
decision variables.
290
We end this section noting that our optimization model and approach aims
at finding the solution at a minimum cost not the price. Typically, service
providers get solutions at the least possible cost, and then they determine the
grossprofitmargintoaddtothiscostinordertocomeupwiththepricingthat
will increase the chances of the provider winning business. While we here aim
295
at finding the optimal-cost solution through our approach, finding the optimal
pricing is out of scope for this work. For price optimization given the cost, we
refer the reader, for instance, to the textbook of Phillips [31].
4. Implementation and Experimentation
In this section, we describe the data used in our experimentation that we
300
collected from a real cloud solutioning application of one of the world’s largest
cloud providers in Section 4.1. We then describe two baseline solution methods
for our problem in Section 4.2. Lastly, in Section 4.3, we provide the imple-
mentationofouroptimizationmethodaswellasthetwobaselinemethods,and
compare the results of applying all three methods to our realistic data.
305
4.1. Data Collection
For our experiments, we collected three types of real data from the large
cloud service provider for which this work was developed and implemented: i)
14

attributes and the domain of their possible values for defining solutions, ii) the
logic/constraints that define valid solutions (correlated to NA set), iii) combi-
310
nationsofattribute-valuepairsthatdefinefeaturecodeswiththecorresponding
costs(correspondingtoMIset),andiv)mandatory(IF)andforbideenattributes
(IFN) dependencies.
For the first one, we analyze real business data records and summarize 39
attributes, covering aspects such as data center location, data center type, OS,
315
databasetype,databasesize,datarecoveryservices,andsoon. Table3showsan
example of three attributes and their value choices. On average, each attribute
hasadomainof9.36valuechoices. Thus,thereareabout 1028combinationsin
∼
total,whichisobviouslyamassivesearchspace. Forii)andiii),afteranalyzing
existing costing data, we obtained 209 cost possibilities, of which each cost is
320
associated with 4.44 pairs of solution attribute & value. Table 4 shows three
examples of costing rules that are related to OS, data center type and data
recovery services. For confidentiality issue, we replace the real cost values with
different letters, representing different costs.
Finally, for mandatory (IF set) and forbidden attribute (IFN set) depen-
325
dencies, we obtain 4,383 and 2,161 respectively. The mandatory attribute de-
pendency are sets of attribute-value pairs that purely depend on others. For
example, some location only supports one particular data center type. So once
the client determines to migrate their IT environment to such location, there
is no choice of data center type. The forbidden attribute dependency are sets
330
of attribute-value pairs that are not allowed together. They are not covered by
cost possibilities since they are not directly correlated with cost. One example
illegalcombinationofOSanddatabasetype. Somedatabasecanonlyworkina
particular OS, e.g., linux. Thus choice of non-linux OS excludes the possibility
of installing such database.
335
4.2. Baseline Solution Methods
In this section, we describe two baseline methods that we compare to our
optimization method in the next section. The first baseline method is simply
15

Table3: ExampleofAttributeDomain
Attribute Domain
Operation System (OS) AIX 7, RHL 6, Win 2012
Data Center Type (DCT) Type I, Type II
Disaster Recovery (DR) Y, N
CPU cores 16, 32, 64
RAM 64, 128, 256
Service Level Level I, Level II, Level III
Table4: ExampleofCost
OS DCT DR Cost
Win 2012 Type I N x
AIX 7 Type I Y y
RHL 6 Type II Y y
choosing feasible attribute values at random from every attribute, putting in
consideration not to choose the values that are not allowed to be chosen and
340
choosing those that we must choose. Algorithm 1 illustrates this method. Note
thatweusethesamenotationinthissectionastheoneweusedinSection3.3.1.
In this algorithm, we proceed progressively to randomly pick one attribute
and one of its feasible values at each iteration. Given the partial solution con-
structedatanypointofthealgorithmevolution,thesetoffeasiblevaluesofthe
345
picked attribute is evaluated. If this set of feasible values is empty, we restart
the algorithm. To calculate the cost of our solution, we iterate over all cost
codes, check whether a cost code is enabled, and add its cost, if it is. Finally,
the customization penalty is added for attributes not covered by any of the
enabled feature codes.
350
The second baseline method that we present next is a greedy heuristic for
choosing a cheap solution. This heuristic illustrated in Algorithms 2, 3, and
16

| Algorithm              | 1 Baseline |     | Solution | Method | 1: Random |     | Selection |
| ---------------------- | ---------- | --- | -------- | ------ | --------- | --- | --------- |
| 1: RemainingAttributes |            |     | S        |        |           |     |           |
←
| 2: CurrentSolution |     |     | φ   |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
←
| 3: while | RemainingAttributes=φ |     |     |     | do  |     |     |
| -------- | --------------------- | --- | --- | --- | --- | --- | --- |
6
| 4: Choose |     | a random | attribute | s   | RemainingAttributes |     |     |
| --------- | --- | -------- | --------- | --- | ------------------- | --- | --- |
0 ∈
5: VV s0 v 0 V s0 s.t. the constraints implied by (NA, MI, IT, IF,
← { ∈
| IFN) | are | satisfied | given | CurrentSolution |     |     |     |
| ---- | --- | --------- | ----- | --------------- | --- | --- | --- |
}
| 6: if     | VV s0               | =φ then  |       |      |                 |     |     |
| --------- | ------------------- | -------- | ----- | ---- | --------------- | --- | --- |
| 7:        | RemainingAttributes |          |       | S;   | CurrentSolution |     | φ   |
|           |                     |          |       | ←    |                 |     | ←   |
| 8:        | Continue            |          |       |      |                 |     |     |
| 9: Choose |                     | a random | value | v VV |                 |     |     |
|           |                     |          |       | 00   | s0              |     |     |
∈
| 10: CurrentSolution     |     |     | CurrentSolution |                     |     | (v 00 ,s | 0 )    |
| ----------------------- | --- | --- | --------------- | ------------------- | --- | -------- | ------ |
|                         |     |     | ←               |                     |     | ∪{       | }      |
| 11: RemainingAttributes |     |     |                 | RemainingAttributes |     |          | s      |
|                         |     |     | ←               |                     |     |          | \{ 0 } |
| 12: TotalCost           |     | 0   |                 |                     |     |          |        |
←
| 13: for Cost | code | f F | do  |     |     |     |     |
| ------------ | ---- | --- | --- | --- | --- | --- | --- |
∈
| 14: if | ( (v,s)   | C ,(v,s) |                | CurrentSolution) |     | then |     |
| ------ | --------- | -------- | -------------- | ---------------- | --- | ---- | --- |
|        | ∀         | ∈ f      | ∈              |                  |     |      |     |
| 15:    | TotalCost |          | TotalCost+cost |                  | f   |      |     |
←
16: TotalCost TotalCost+customizationPenalty num of attributes not
|         |     | ←           |      |     |     |     | ∗   |
| ------- | --- | ----------- | ---- | --- | --- | --- | --- |
| covered | by  | any feature | code |     |     |     |     |
4 has 2 precedures:(i) CustomizeRemainingAttributes which selects values
randomly for the attributes not covered by the given Solution (CurrSol), and
(ii) GreedySearch which is a recursive function that constitutes the core of
355
thealgorithm. Thevalidityofthegivensolutionischeckedfirst. Ifthesolution
is valid, the algorithm proceeds by trying iteratively to add one feature code
at a time and proceeding recursively from this point in a depth first manner.
On the other hand, if the given solution is invalid, the algorithm bounds this
searchpath. Theorderoffeaturecodeexplorationisinascendingorderoftheir
360
cost. Once a full path of feature codes is explored, the procedure Customiz-
eRemainingAttributes is invoked to get a customized solution for attributes
not covered by the feature codes in the solution. Finally, the global variable
17

SolutionFound is used to exit the algorithm after finding the first feasible so-
365 lution. Discarding the use of this variable will turn the algorithm into a full
| enumeration | algorithm        | where | all   | feasible solutions |        | are enumerated. |                 |     |     |
| ----------- | ---------------- | ----- | ----- | ------------------ | ------ | --------------- | --------------- | --- | --- |
| Note        | that constraints |       | check | in Lines 13        | and 30 | can be          | time consuming, |     | and |
hence it needs to be implemented in an efficient way. To this end, we utilized
special problem pertinent structural properties to alleviate the computational
complexity involved in these steps. This is, therefore, one of the strong aspects
370
of our optimization model, that we can encode these constraints in a straight-
forward and simple manner with no deep knowledge of the problem structural
properties, whilestillgettingamoreefficientsolutionintermsofbothcostand
run-time. Further,suchoptimalsolutioncouldbesignificantlylowerthanthose
obtainedbythelimitedbaselinemethodsthatwearepresentinghere,aswewill
375
| show in      | the next   | subsection. |     |           |        |           |        |     |     |
| ------------ | ---------- | ----------- | --- | --------- | ------ | --------- | ------ | --- | --- |
| Algorithm    | 2 Baseline | Solution    |     | Method 2: | Greedy | Heuristic | - Part | 1   |     |
| 1: procedure | Main       |             |     |           |        |           |        |     |     |
| RemCodes     |            | F           |     |           |        |           |        |     |     |
2:
←
| 3: RemAttr |     | S   |     |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
←
| CurSol |     | φ   |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4:
←
| 5: TotCost |     | 0   |     |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
←
| global | : SolutionFound |     |     | False |     |     |     |     |     |
| ------ | --------------- | --- | --- | ----- | --- | --- | --- | --- | --- |
6:
←
| 7: Sort        | the cost | codes     | in set | F in ascending       | order | of  | cost in | cost f    |     |
| -------------- | -------- | --------- | ------ | -------------------- | ----- | --- | ------- | --------- | --- |
| 8: (TotalCost, |          | Solution) |        | GreedySearch(CurSol, |       |     |         | RemCodes, |     |
←
| RemAttr,             |     | TotCost)     |     |               |              |     |     |     |     |
| -------------------- | --- | ------------ | --- | ------------- | ------------ | --- | --- | --- | --- |
| 4.3. Implementation, |     | Experiments, |     | and Practical | Implications |     |     |     |     |
Weimplementedouroptimizationmethodaswellasthetwobaselinemeth-
ods. All implementations were done in the python programming language. We
solved the optimization model using the commercial solver CPLEX [32]. We
380
then constructed some experiments to examine the performance of our opti-
| mization | method | compared | to the | two baseline | method. |     |     |     |     |
| -------- | ------ | -------- | ------ | ------------ | ------- | --- | --- | --- | --- |
18

Algorithm 3 Baseline Solution Method 2: Greedy Heuristic - Part 2
1: procedure GreedySearch(CurrSol, RemCodes, RemAttr, TotCost)
2: if global:solutionFound then
3: return
4: if CheckConstraints(CurrSol,NA, MI, IT, IF, IFN) = False then
5: return
6: for f RemCodes (where we iterate on the sorted set F) do
∈
7: CurrSol 0 CurrSol (v,s) C f
← ∪{ ∈ }
8: RemCodes 0 RemCodes f
← \{ }
9: RemAttr 0 RemAttr s C f
← \{ ∈ }
10: TotCost 0 TotCost+cost f
←
11: GreedySearch(CurrSol 0 , RemCodes 0 , RemAttr 0 , TotCost 0 )
12: global:solutionFound True
←
13: returnCustomizeRemainingAttributes(RemAttr,TotCost,CurrSol)
We implemented the optimization model using the CPLEX 12.7 library for
Python 3.5. More specifically, we used the function cplex.Cplex.variables.add
toaddthemodelvariables,thefunctioncplex.Cplex().linear constraints.addto
385
add the model constraints, and the function cplex.Cplex().objective.set linear
to specifiy the model objective function, and finally cplex.Cplex().model.solve
to solve the optimization model.
We tried multiple settings to improve the optimization model performance,
but none of them proved to be significantly different from the default settings.
390
In particular, we tried adding cuts, changing the LP algorithm, solution pol-
ishing, changing the node selection criteria, changing the pivoting criteria, and
changing the branching criteria. But since none of these changes proved to
provide statistically different solutions, we ended up using the default CPLEX
settings.
395
The objective of these experiments is threefold. First, we aim at validating
theoptimalityofthesolutionsgottenfromouroptimizationapproach. Thatis,
19

| Algorithm | 4   | Baseline | Solution | Method | 2: Greedy | Heuristic | - Part 3 |
| --------- | --- | -------- | -------- | ------ | --------- | --------- | -------- |
1: procedureCustomizeRemainingAttributes(RemAttr, TotCost, CurrSol)
| 2:  | RemAttr | 0 RemAttr |     |     |     |     |     |
| --- | ------- | --------- | --- | --- | --- | --- | --- |
←
| 3:  | TotCost | TotCost |     |     |     |     |     |
| --- | ------- | ------- | --- | --- | --- | --- | --- |
0
←
| 4:  | CurrSol | 0 CurrSol |     |     |     |     |     |
| --- | ------- | --------- | --- | --- | --- | --- | --- |
←
| 5:  | while | RemAttr | =φ  | do  |     |     |     |
| --- | ----- | ------- | --- | --- | --- | --- | --- |
0 6
| 6:  | Choose | a random |     | attribute s 0 | RemAttr | 0   |     |
| --- | ------ | -------- | --- | ------------- | ------- | --- | --- |
∈
| 7:  | VV   | v             | V s.t. | the constraints |     | implied by (NA, | MI, IT, IF, |
| --- | ---- | ------------- | ------ | --------------- | --- | --------------- | ----------- |
|     | s0   | ←{ 0          | ∈ s0   |                 |     |                 |             |
|     | IFN) | are satisfied |        | given CurrSol   | 0   |                 |             |
}
| 8:  | if VV | =φ  | then |     |     |     |     |
| --- | ----- | --- | ---- | --- | --- | --- | --- |
s0
| 9:  |     | RemAttr | 0 RemAttr |     |     |     |     |
| --- | --- | ------- | --------- | --- | --- | --- | --- |
←
| 10: |     | TotCost | TotCost |     |     |     |     |
| --- | --- | ------- | ------- | --- | --- | --- | --- |
0
←
| 11: |     | CurrSol | 0 CurrSol |     |     |     |     |
| --- | --- | ------- | --------- | --- | --- | --- | --- |
←
| 12: |        | Continue |     |            |       |     |     |
| --- | ------ | -------- | --- | ---------- | ----- | --- | --- |
| 13: | Choose | a random |     | value v 00 | VV s0 |     |     |
∈
| 14: | CurrSol |                    | CurrSol | (v ,s                 | )   |     |     |
| --- | ------- | ------------------ | ------- | --------------------- | --- | --- | --- |
|     |         | 0 ←                |         | 0 ∪{ 00               | 0 } |     |     |
| 15: | RemAttr | 0                  | RemAttr | 0 s 0                 |     |     |     |
|     |         | ←                  |         | \{ }                  |     |     |     |
| 16: | TotCost |                    | TotCost | +CustomizationPenalty |     |     |     |
|     |         | TotC←ost,CurrSol 0 |         | 0                     |     |     |     |
return
|     |     |     | 0   | 0   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
thesesolutionscannotbeworsethanthoseofthebaselinemethodsforinstance,
and it should be equal to the solution found by the brute-force enumeration.
Second, we compare the efficiency of our optimization approach compared to
400
the two baseline methods. This is done via comparing the solution times of
each method. Lastly, the effectiveness of each method is compared through
calculating the relative increase in cost for each baseline method compared to
| the optimal | (minimal) |                  | cost. |        |             |                |          |
| ----------- | --------- | ---------------- | ----- | ------ | ----------- | -------------- | -------- |
| We          | explain   | our experimental |       | design | as follows: | We constructed | approxi- |
405
mately1000probleminstancesusingouraforementioendrealisticdataforCloud
solutioning attributes and their values, where in each instance, we restrict the
values that can be chosen for each attribute to a random subset of these val-
20

Figure2: HistogramofCostSavings%obtainedbyOurOptimizationMethodoverBaseline
methods
Figure3: HistogramofRun-TimeSavingsobtainedbyOurOptimizationMethodoverBase-
linemethods
21

ues. Additionally, we used a realistic embodiment for the constraints implied
IF and IFN. We solved all the instances with the constraints implied by (IF,
410
IFN) and without these constraints. All of our experiments were run on a 2.1
GHz24-coreIntel(R)Xeon(R)CPUE5-2683v4processorwith64MBofcache
memory and 256 GB of RAM.
We found that our optimization model is robust; it solves each of these
instances in less than 1 second. We also found that the optimal cost could be
415
significantly lower than that obtained by each of the two baseline methods.
Figures 2 and 3 show the distibutions of the cost savings and the run time
savings of the optimization method over both baseline methods (the greedy
heuristic and the random selection heuristic) with and without the constraints
implied by (IF, IFN). From the figures, we can note that following:
420
Comparing the Optimization Model to the Greedy Heuristic:
•
– The optimization model cost is signficatnly lower than the greedy
heuristic cost.
– The absence of the constraints implied by (IF, IFN) amplifies the
cost savings obtained by the optimization model.
425
– In the absence of the constraints implied by (IF, IFN), the opti-
mization model is slightly slower than the greedy heuristic.
– In the existence of the constraints implied by (IF, IFN), the opti-
mization model is faster than the greedy heuristic.
Comparing the Optimization Model to the Random Selection Heuristic:
430
•
– The optimization model cost is signficatnly lower than the random
selection cost.
– The optimization model is slightly faster than the random selection
cost.
– The constraints implied by (IF, IFN) has no signifcant effect on
435
the relative performance of the random selection method in terms of
22

|        | the    | cost. However,  | it increases   | the variability |       | of       | solution time | of the   |
| ------ | ------ | --------------- | -------------- | --------------- | ----- | -------- | ------------- | -------- |
|        | random | selection       | method.        |                 |       |          |               |          |
| Tables | 5      | and 6 summarize | the statistics | of              | these | results. | Looking       | at these |
results,onecanobviouslytelltheeffectivenessofouroptimizationmethodgiven
440
howhugeofacostsavingitcouldprovideforthesolutionproviderwhenusedin-
steadofanyofthebaselinemethods. Also,givenhowfastourmodelgetssolved
in, the efficiency of our method becomes clear, especially with the existence of
constraints on the attributes depdencies which are very common in practice.
445 Note that entries with negative values in Table 6 mean that the optimization
| model | is slower | than the corresponding |     | baseline | method | for | this entry. |     |
| ----- | --------- | ---------------------- | --- | -------- | ------ | --- | ----------- | --- |
Finally,wewouldliketomentionthatforthesakeofvalidation,wesolvedthe
enumerated instances using brute-force enumeration. As expected, the optimal
cost using brute-force enumretion is equal to that obtained using our optimiza-
tion model, and also as expected, the average run time increase compared to
450
| the optimization |     | model is           | about 62K    | folds. |     |           |       |           |
| ---------------- | --- | ------------------ | ------------ | ------ | --- | --------- | ----- | --------- |
| There            | are | multiple practical | implications | to     | our | approach. | Since | our model |
runs very quickly (in seconds), it can be easily deployed in a solutioning tool,
like the web-based application developed for the cloud service provider for this
this work was done. It also enables users to be able to change any parameters
455
of the problem inputs, and re-run the model to get the updated solution in
seconds.
| Also, | the | effort of deploying | our | optimization | model | compared | to  | that for |
| ----- | --- | ------------------- | --- | ------------ | ----- | -------- | --- | -------- |
heuristic solutions (e.g., the two baseline methods we presented) or manual
solutions is very similar, since any method will just be implemented in the
460
backend of the application and then deployed in production. This is confirmed
since we implemented the algorithms for all these methods for the sake of the
| experiments |     | above. |     |     |     |     |     |     |
| ----------- | --- | ------ | --- | --- | --- | --- | --- | --- |
Moreover,ourapproach/modelalsousesthesameinputsastheothermeth-
odsandthus,doesnotincorporateanyadditionaleffortinthatregard. Finally,
465
it has been shown that our model scales much better in the existence of inter-
23

| dependency | constraints | between | attributes. |     |     |
| ---------- | ----------- | ------- | ----------- | --- | --- |
Table5: CostSavingsStatisticsComparingOurOptimizationMethodversustheTwoBase-
lineMethods
|         |          | % Cost       | Decrease of | % Cost           | Decrease of |
| ------- | -------- | ------------ | ----------- | ---------------- | ----------- |
|         | Our      | Optimization | Method      | Our Optimization | Method      |
|         |          | over Greedy  | Heuristic   | over Random      | Heuristic   |
|         | With     | Con-         | No Con-     | With Con-        | No Con-     |
|         | straints |              | straints    | straints         | straints    |
| Minimum |          | 0            | 0           | 9%               | 6%          |
|         |          | 20%          | 23%         | 27%              | 24%         |
Maximum
| Average |     | 3%  | 8%  | 18% | 16% |
| ------- | --- | --- | --- | --- | --- |
Standard
|     |     | 3%  | 5%  | 3%  | 3%  |
| --- | --- | --- | --- | --- | --- |
Deviation
| 5. Conclusions |     | and Future | Work |     |     |
| -------------- | --- | ---------- | ---- | --- | --- |
Wetackledinthispapertheissueofcostoptimizationofacloudsolutionfor
470 a given client IT requirements. Our contribution consists of a novel approach
that incorporates finding the optimized combination of solution components,
from a cost point of view, offered by a service provider that meets client’s
requirements.
Wehaveimplementedouroptimizationmethodaswellastwobaselinemeth-
ods and compared the results of applying all three methods on realistic data.
475
Experimentationresultsshowtheeffectivenessofouroptimizationmethodsince
24

Table6: CostSavingsStatisticsComparingOurOptimizationMethodversustheTwoBase-
lineMethods
|         |     | % Run-Time |              | Decrease  | of   | % Run-Time |              | Decrease  | of   |
| ------- | --- | ---------- | ------------ | --------- | ---- | ---------- | ------------ | --------- | ---- |
|         |     | Our        | Optimization | Method    |      | Our        | Optimization | Method    |      |
|         |     | over       | Greedy       | Heuristic |      | over       | Random       | Heuristic |      |
|         |     |            | (in          | Seconds)  |      |            | (in Seconds) |           |      |
|         |     | With       | Con-         | No        | Con- | With       | Con-         | No        | Con- |
|         |     | straints   |              | straints  |      | straints   |              | straints  |      |
| Minimum |     | -0.19      |              | -0.88     |      | -0.35      |              | -0.6      |      |
|         |     | 108        |              | 0.05      |      | 0.57       |              | 0.9       |      |
Maximum
| Average |     | 1.57 |     | -0.17 |     | 0.04 |     | 0.05 |     |
| ------- | --- | ---- | --- | ----- | --- | ---- | --- | ---- | --- |
Standard
|     |     | 5.16 |     | 0.16 |     | 0.1 |     | 0.19 |     |
| --- | --- | ---- | --- | ---- | --- | --- | --- | ---- | --- |
Deviation
we have shown that it provides massive cost savings for the solution provider
| compared     | to the | baseline            | methods. |       |     |            |     |              |       |
| ------------ | ------ | ------------------- | -------- | ----- | --- | ---------- | --- | ------------ | ----- |
| In addition, |        | our experimentation |          | shows | the | efficiency | of  | our approach | as it |
480 getsexecutedinafewsecondsatmost,comparedtotheminutesofthebaseline
methods and the hours (to few days) it used to take human solutioners to get
a feasible solution for the considered problem. We have also shown that a
brute-force solution to our problem is not applicable at all as it takes hours for
| realistic-sized | instances.         |     |     |               |     |            |     |               |     |
| --------------- | ------------------ | --- | --- | ------------- | --- | ---------- | --- | ------------- | --- |
| Given           | the aforementioned |     |     | effectiveness | and | efficiency | of  | our approach, | as  |
485
well as the fact that the effort of implementing and deploying our optimization
approach compared to the other methods is similar, it is shown to be quite
| useful, applicable, |     | and | impactful | for real | service | providers. |     |     |     |
| ------------------- | --- | --- | --------- | -------- | ------- | ---------- | --- | --- | --- |
25

Wesolvedtheproblemofsolutioncostoptimization,inwhichweweretrying
490 to find the minimum possible solution that satisfied the client requirements.
After solution providers solve such costing minimization problem, they need to
”price”theirsolution. Thatis,theyneedtoaddsomegrossprofitontopofthe
cost in order to reach the price that they will offer to clients. Obviously, the
higher the price, the lower their chances of selling their solution versus other
competitors. Thus,aresearchquestion,thatisanaturalextensionofourwork,
495
is: what is the optimal price (or added gross profit on top of the optimal cost)
that would increase the chance of successfully winning the deal of selling the
cloud service to clients? Therefore, applying some of the pricing methods in
the literature of revenue management will be an interesting research direction
to this work.
500
References
[1] G. Pallis, Cloud computing: the new frontier of internet computing, IEEE
| internet | computing | 14  | (5) (2010) | 70–73. |     |     |     |
| -------- | --------- | --- | ---------- | ------ | --- | --- | --- |
[2] D. Linthicum, The case for managed service providers in your cloud strat-
505 egy, http://www.infoworld.com/article/2923441/cloud-computing/the-
| case-for-managed-service-providers-in-your-cloud-strategy.html, |         |       |      |            |     |     | [Online; |
| --------------------------------------------------------------- | ------- | ----- | ---- | ---------- | --- | --- | -------- |
| accessed                                                        | June 1, | 2017] | (May | 19, 2015). |     |     |          |
[3] I. San Aniceto, R. Moreno-Vozmediano, R. S. Montero, I. M. Llorente,
| Cloud capacity |     | reservation | for | optimal | service | deployment, | in: Second In- |
| -------------- | --- | ----------- | --- | ------- | ------- | ----------- | -------------- |
510 ternational Conference on Cloud Computing, GRIDs, and Virtualization,
| 2011, pp. | 52–59. |     |     |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- | --- |
[4] I. Trummer, F. Leymann, R. Mietzner, W. Binder, Cost-optimal out-
| sourcing        | of applications |          | into | the clouds, | in:    | Cloud Computing | Technology     |
| --------------- | --------------- | -------- | ---- | ----------- | ------ | --------------- | -------------- |
| and Science     | (CloudCom),     |          | 2010 | IEEE        | Second | International   | Conference on, |
| 515 IEEE, 2010, | pp.             | 135–142. |      |             |        |                 |                |
26

[5] M.Mao,J.Li,M.Humphrey,Cloudauto-scalingwithdeadlineandbudget
constraints, in: Grid Computing (GRID), 2010 11th IEEE/ACM Interna-
tional Conference on, IEEE, 2010, pp. 41–48.
[6] S. K. Barker, P. Shenoy, Empirical evaluation of latency-sensitive applica-
tion performance in the cloud, in: Proceedings of the first annual ACM
520
SIGMM conference on Multimedia systems, ACM, 2010, pp. 35–46.
[7] A. Khajeh-Hosseini, D. Greenwood, I. Sommerville, Cloud migration: A
case study of migrating an enterprise IT system to IaaS, in: Cloud Com-
puting(CLOUD),2010IEEE3rdInternationalConferenceon,IEEE,2010,
pp. 450–457.
525
[8] M. A. Chauhan, M. A. Babar, Migrating service-oriented system to cloud
computing: An experience report, in: Cloud Computing (CLOUD), 2011
IEEE International Conference on, IEEE, 2011, pp. 404–411.
[9] M. A. Babar, M. A. Chauhan, A tale of migration to cloud computing for
sharing experiences and observations, in: Proceedings of the 2nd interna-
530
tional workshop on software engineering for cloud computing, ACM, 2011,
pp. 50–56.
[10] S. C. Park, S. Y. Ryoo, An empirical investigation of end-users’ switching
toward cloud computing: A two factor theory perspective, Computers in
Human Behavior 29 (1) (2013) 160–170.
535
[11] G. Lewis, E. Morris, D. Smith, Service-oriented migration and reuse tech-
nique (smart), in: Software Technology and Engineering Practice, 2005.
13th IEEE International Workshop on, IEEE, 2005, pp. 222–229.
[12] S. C. Misra, A. Mondal, Identification of a company’s suitability for the
adoption of cloud computing and modelling its corresponding return on
540
investment,MathematicalandComputerModelling53(3)(2011)504–521.
27

[13] P. Saripalli, G. Pingali, Madmac: Multiple attribute decision methodol-
| ogy for adoption | of clouds, | in:       | Cloud | Computing |          | (CLOUD), | 2011 | IEEE |
| ---------------- | ---------- | --------- | ----- | --------- | -------- | -------- | ---- | ---- |
| International    | Conference | on, IEEE, | 2011, | pp.       | 316–323. |          |      |      |
[14] P. V. Beserra, A. Camara, R. Ximenes, A. B. Albuquerque, N. C. Men-
545
| don¸ca,Cloudstep: | Astep-by-stepdecisionprocesstosupportlegacyappli- |         |                 |           |     |           |     |          |
| ----------------- | ------------------------------------------------- | ------- | --------------- | --------- | --- | --------- | --- | -------- |
| cation migration  | to the                                            | cloud,  | in: Maintenance |           | and | Evolution | of  | Service- |
| Oriented          | and Cloud-Based                                   | Systems | (MESOCA),       |           |     | 2012 IEEE | 6th | Interna- |
| tional Workshop   | on the,                                           | IEEE,   | 2012,           | pp. 7–16. |     |           |     |          |
[15] A. Khajeh-Hosseini, I. Sommerville, J. Bogaerts, P. Teregowda, Decision
550
| support tools | for cloud | migration     | in the     | enterprise, |     | in: Cloud | Computing |          |
| ------------- | --------- | ------------- | ---------- | ----------- | --- | --------- | --------- | -------- |
| (CLOUD),      | 2011 IEEE | International | Conference |             | on, | IEEE,     | 2011,     | pp. 541– |
548.
[16] A.Khajeh-Hosseini,D.Greenwood,J.W.Smith,I.Sommerville,Thecloud
| adoption | toolkit: supporting |     | cloud adoption |     | decisions | in  | the enterprise, |     |
| -------- | ------------------- | --- | -------------- | --- | --------- | --- | --------------- | --- |
555
| Software: | Practice and | Experience | 42  | (4) (2012) | 447–465. |     |     |     |
| --------- | ------------ | ---------- | --- | ---------- | -------- | --- | --- | --- |
[17] E. Ahmed, A. Akhunzada, M. Whaiduzzaman, A. Gani, S. H. Ab Hamid,
R.Buyya,Network-centricperformanceanalysisofruntimeapplicationmi-
grationinmobilecloudcomputing,SimulationModellingPracticeandThe-
| ory 50 (2015) | 42–56. |     |     |     |     |     |     |     |
| ------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
560
[18] H. Mouratidis, S. Islam, C. Kalloniatis, S. Gritzalis, A framework to sup-
| port selection | of cloud   | providers | based    | on  | security   | and        | privacy | require- |
| -------------- | ---------- | --------- | -------- | --- | ---------- | ---------- | ------- | -------- |
| ments, Journal | of Systems | and       | Software | 86  | (9) (2013) | 2276–2293. |         |          |
[19] M.Pavlidis,H.Mouratidis,C.Kalloniatis,S.Islam,S.Gritzalis,Trustwor-
565 thyselectionofcloudprovidersbasedonsecurityandprivacyrequirements:
| Justifying | trust assumptions,  |           | in: International |           | Conference |     | on Trust, | Pri- |
| ---------- | ------------------- | --------- | ----------------- | --------- | ---------- | --- | --------- | ---- |
| vacy and   | Security in Digital | Business, |                   | Springer, | 2013,      | pp. | 185–198.  |      |
[20] H.Ma,Z.Hu,K.Li,H.Zhang,Towardtrustworthycloudserviceselection:
28

|     | a time-aware    | approach |           | using | interval | neutrosophic | set, | Journal | of Parallel |
| --- | --------------- | -------- | --------- | ----- | -------- | ------------ | ---- | ------- | ----------- |
| 570 | and Distributed |          | Computing | 96    | (2016)   | 75–94.       |      |         |             |
[21] P. Jamshidi, A. Ahmad, C. Pahl, Cloud migration research: a systematic
|     | review, IEEE | Transactions |     | on  | Cloud | Computing | 1 (2) | (2013) | 142–157. |
| --- | ------------ | ------------ | --- | --- | ----- | --------- | ----- | ------ | -------- |
[22] T. Binz, U. Breitenbu¨cher, O. Kopp, F. Leymann, Tosca: Portable auto-
|     | mated deployment |           | and | management |              | of cloud | applications, |     | in: Advanced |
| --- | ---------------- | --------- | --- | ---------- | ------------ | -------- | ------------- | --- | ------------ |
|     | Web Services,    | Springer, |     | 2014,      | pp. 527–549. |          |               |     |              |
575
[23] A. Bergmayr, J. Troya, P. Neubauer, M. Wimmer, G. Kappel, UML-
|     | based cloud   | application |         | modeling | with | libraries, | profiles, | and | templates, |
| --- | ------------- | ----------- | ------- | -------- | ---- | ---------- | --------- | --- | ---------- |
|     | in: CloudMDE@ |             | MoDELS, | 2014,    | pp.  | 56–65.     |           |     |            |
[24] S. Frey, W. Hasselbring, The cloudmig approach: Model-based migration
580 of software systems to cloud-optimized applications, International Journal
|     | on Advances | in  | Software | 4 (3 | and 4) | (2011) 342–353. |     |     |     |
| --- | ----------- | --- | -------- | ---- | ------ | --------------- | --- | --- | --- |
[25] V.Andrikopoulos,S.G.S´aez,F.Leymann,J.Wettinger,Optimaldistribu-
|     | tionofapplicationsinthecloud,in: |         |              |     |           | InternationalConferenceonAdvanced |     |        |     |
| --- | -------------------------------- | ------- | ------------ | --- | --------- | --------------------------------- | --- | ------ | --- |
|     | Information                      | Systems | Engineering, |     | Springer, | 2014,                             | pp. | 75–90. |     |
[26] M.J.Csorba,H.Meling,P.E.Heegaard,Antsystemforservicedeployment
585
|     | in private | and public | clouds, | in:         | Proceedings |      | of the 2nd | workshop | on Bio- |
| --- | ---------- | ---------- | ------- | ----------- | ----------- | ---- | ---------- | -------- | ------- |
|     | inspired   | algorithms | for     | distributed | systems,    | ACM, | 2010,      | pp.      | 19–28.  |
[27] H. Wada, J. Suzuki, Y. Yamano, K. Oba, Evolutionary deployment op-
|     | timization    | for service-oriented |     |     | clouds, | Software: | Practice | and | Experience |
| --- | ------------- | -------------------- | --- | --- | ------- | --------- | -------- | --- | ---------- |
|     | 41 (5) (2011) | 469–493.             |     |     |         |           |          |     |            |
590
[28] Z.I.M.Yusoh,M.Tang,Compositesaasplacementandresourceoptimiza-
|     | tionincloudcomputingusingevolutionaryalgorithms,in: |     |           |     |               |     |            | CloudComput- |             |
| --- | --------------------------------------------------- | --- | --------- | --- | ------------- | --- | ---------- | ------------ | ----------- |
|     | ing (CLOUD),                                        |     | 2012 IEEE | 5th | International |     | Conference | on,          | IEEE, 2012, |
|     | pp. 590–597.                                        |     |           |     |               |     |            |              |             |
29

[29] S. Pandey, L. Wu, S. M. Guru, R. Buyya, A particle swarm optimization-
595
| based heuristic   | for scheduling | workflow    | applications | in cloud comput- |
| ----------------- | -------------- | ----------- | ------------ | ---------------- |
| ing environments, | in: Advanced   | information | networking   | and applications |
(AINA),201024thIEEEinternationalconferenceon,IEEE,2010,pp.400–
407.
[30] S. Frey, F. Fittkau, W. Hasselbring, Search-based genetic optimization for
600
| deployment | and reconfiguration | of software | in the | cloud, in: Proceedings |
| ---------- | ------------------- | ----------- | ------ | ---------------------- |
ofthe2013InternationalConferenceonSoftwareEngineering,IEEEPress,
| 2013, pp. | 512–521. |     |     |     |
| --------- | -------- | --- | --- | --- |
[31] R.L.Phillips,Pricingandrevenueoptimization,StanfordUniversityPress,
2005.
605
[32] IBMILOGCPLEX,V12.1: User’smanualforCPLEX,InternationalBusi-
| ness Machines | Corporation | 46 (53) (2009) | 157. |     |
| ------------- | ----------- | -------------- | ---- | --- |
30

Authors’ Bibliographies
Aly Megahed
Aly Megahed is a research staff member at IBM's Almaden Research Center in San Jose, CA.
His current research interests span over building analytical tools for complex service
engagements, cloud computing, and IoT, and advancing research in analytics, machine learning,
and operations research. Dr. Megahed got his Ph.D. in Industrial Engineering from Georgia
Tech. He has done multiple analytical research/consultancy projects for 6 companies in the past
and has his work published in several academic journals and conferences, in addition to filing
multiple patent disclosures and winning multiple IBM internal awards as well as external ones.
Ahmed Nazeem
Ahmed Nazeem is a research staff member at IBM's Almaden Research Center in San Jose, CA.
In his current job, he develops analytical tools for complex service engagements, cloud
computing, and IoT, and advances research in cognitive computing, machine learning, and
operations research. Dr. Nazeem got his Ph.D. in Industrial Engineering from Georgia Tech. He
has his work published in several academic journals and conferences, in addition to filing
multiple patent disclosures.
Peifeng Yin
Peifeng Yin is a Research Staff Member at IBM's Almaden Research Center in San Jose, CA.
His research interests include service data analytics, machine learning, data mining, and their
applications in different areas. Dr. Yin got his Ph.D. in Computer Science and Engineering from
Pennsylvania State University. He has his works published in several conferences and journals,
in addition to filing multiple patent disclosures.
Samir Tata
Samir Tata is a Research Staff Member at IBM's Almaden Research Center in San Jose, CA.
Before joining IBM, he was a Professor at Telecom SudParis, part of Institut Mines-Telecom,
France. His current research interests include service oriented computing, business process
management, and their applications in virtual enterprises, cloud environments, and the Internet of
Things. He was chair of several international conference and workshops. He was/is member of
the steering or program committee of several international conferences.
Hamid Reza Motahari Nezhad
Hamid Reza Motahari Nezhad is a Research Group Lead for Cognitive Services, and Member of
IBM Academy of Technology at IBM Almaden Research Center. His research interests include
areas of data analytics, cognitive computing (NLP, text analytics and machine learning),
cognitive business process management, and cognitive enterprise services. He also holds a
Visiting Principal Research Fellow position with The University of New South Wales (UNSW),
Australia, where he is co-supervisor of Master's and PhD students in computer science, machine
learning, and cognitive computing. He has published more than 100 scholarly papers in
conferences and journals. He is a senior member of IEEE and a member of ACM. Contact him at
motahari@ieee.org

Taiga Nakamura
Taiga Nakamura is a Research Staff Member and Research Manager at IBM's Almaden Research
Center in San Jose, CA, where he currently leads the Cloud Services Analytics Research group.
He is conducting research on various aspects of solution design for Services and Software, in the
area of cognitive and model-based solutioning, cloud services optimization, solution
competitiveness, requirements and knowledge management, and quality analysis. Dr. Nakamura
received his PhD in Computer Science from the University of Maryland, College Park. He has
authored or coauthored more than 30 technical papers and articles, coauthored one book chapter,
and have many patents filed and issued. He is a member of ACM, IEEE, and a senior member of
IPSJ.

Autthors’ Picctures
Aly Megahed
Ahmed Nazeem:
Peifeng Yin

Samir TTata
Hamid RReza Motahhari Nezhad
Taiga NNakamura

Highlights
 We tackle the problem of cloud solution design.
 We formulate an optimization model that find lowest cost solution designs.
 We compare our approach to two baseline heuristics as well as a brute force method.
 Numerical results show the efficiency and effectiveness of our approach.