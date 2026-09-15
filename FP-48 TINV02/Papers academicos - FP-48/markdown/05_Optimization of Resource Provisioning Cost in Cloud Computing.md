164 IEEETRANSACTIONSONSERVICESCOMPUTING, VOL.5, NO.2, APRIL-JUNE2012
|     | Optimization |     |         |         |         | of        | Resource |           |         | Provisioning |         |      |     |     |     |
| --- | ------------ | --- | ------- | ------- | ------- | --------- | -------- | --------- | ------- | ------------ | ------- | ---- | --- | --- | --- |
|     |              |     | Cost    |         | in      | Cloud     |          | Computing |         |              |         |      |     |     |     |
|     |              |     |         | Sivadon |         | Chaisiri, | Student  | Member,   |         | IEEE,        |         |      |     |     |     |
|     |              |     | Bu-Sung | Lee,    | Member, |           | IEEE,    | and Dusit | Niyato, |              | Member, | IEEE |     |     |     |
Abstract—Incloudcomputing,cloudproviderscanoffercloudconsumerstwoprovisioningplansforcomputingresources,namely
reservationandon-demandplans.Ingeneral,costofutilizingcomputingresourcesprovisionedbyreservationplanischeaperthan
thatprovisionedbyon-demandplan,sincecloudconsumerhastopaytoproviderinadvance.Withthereservationplan,theconsumer
canreducethetotalresourceprovisioningcost.However,thebestadvancereservationofresourcesisdifficulttobeachieveddueto
uncertaintyofconsumer’sfuturedemandandproviders’resourceprices.Toaddressthisproblem,anoptimalcloudresource
provisioning(OCRP)algorithmisproposedbyformulatingastochasticprogrammingmodel.TheOCRPalgorithmcanprovision
computingresourcesforbeingusedinmultipleprovisioningstagesaswellasalong-termplan,e.g.,fourstagesinaquarterplanand
twelvestagesinayearlyplan.ThedemandandpriceuncertaintyisconsideredinOCRP.Inthispaper,differentapproachestoobtain
thesolutionoftheOCRPalgorithmareconsideredincludingdeterministicequivalentformulation,sample-averageapproximation,and
Bendersdecomposition.NumericalstudiesareextensivelyperformedinwhichtheresultsclearlyshowthatwiththeOCRPalgorithm,
cloudconsumercansuccessfullyminimizetotalcostofresourceprovisioningincloudcomputingenvironments.
IndexTerms—Cloudcomputing,resourceprovisioning,virtualization,virtualmachineplacement,stochasticprogramming.
Ç
1 INTRODUCTION
CLOUDcomputing is a large-scale distributed computing instances, cloud providers which offer IaaS services with
paradigm in which a pool of computing resources is both plans. In general, pricing in on-demand plan is
available to users (called cloud consumers) via the Internet charged by pay-per-use basis (e.g., 1 day). Therefore,
[1]. Computing resources, e.g., processing power, storage, purchasing this on-demand plan, the consumers can
software,andnetworkbandwidth,arerepresentedtocloud dynamically provision resources at the moment when the
consumers as the accessible public utility services. Infra- resourcesareneededtofitthefluctuatedandunpredictable
structure-as-a-Service (IaaS) is a computational service demands.Forreservationplan,pricingischargedbyaone-
|       |        |         |        |                 |     |           |     | time | fee (e.g., | 1   | year) | typically | before | the computing |     |
| ----- | ------ | ------- | ------ | --------------- | --- | --------- | --- | ---- | ---------- | --- | ----- | --------- | ------ | ------------- | --- |
| model | widely | applied | in the | cloud computing |     | paradigm. |     |      |            |     |       |           |        |               |     |
In this model, virtualization technologies can be used to resource will be utilized by cloud consumer. With the
provide resources to cloud consumers. The consumers can reservation plan, the price to utilize resources is cheaper
thanthatoftheon-demandplan.Inthisway,theconsumer
| specify           | the required | software | stack,  | e.g., | operating |          | systems |            |     |          |              |     |          |              |     |
| ----------------- | ------------ | -------- | ------- | ----- | --------- | -------- | ------- | ---------- | --- | -------- | ------------ | --- | -------- | ------------ | --- |
|                   |              |          |         |       |           |          |         | can reduce |     | the cost | of computing |     | resource | provisioning | by  |
| and applications; |              | then     | package | them  | all       | together | into    |            |     |          |              |     |          |              |     |
virtual machines (VMs). The hardware requirement of using the reservation plan. For example, the reservation
VMs can also be adjusted by the consumers. Finally, those plan offered by Amazon EC2 can reduce the total
|     |     |     |     |     |     |     |     | provisioning |     | cost | up to | 49 percent | when | the | reserved |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---- | ----- | ---------- | ---- | --- | -------- |
VMswillbeoutsourcedtohostincomputingenvironments
operated by third-party sites owned by cloud providers. A resource is fully utilized (i.e, steady-state usage) [4].
cloud provider is responsible for guaranteeing the Quality With the reservation plan, the cloud consumers a priori
|     |     |     |     |     |     |     |     | reserve | the | resources | in  | advance. | As a result, | the | under- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --------- | --- | -------- | ------------ | --- | ------ |
ofServices(QoS)forrunningtheVMs.Sincethecomputing
|           |                |     |        |           |     |       |         | provisioning |     | problem | can occur | when | the reserved |     | resources |
| --------- | -------------- | --- | ------ | --------- | --- | ----- | ------- | ------------ | --- | ------- | --------- | ---- | ------------ | --- | --------- |
| resources | are maintained |     | by the | provider, | the | total | cost of |              |     |         |           |      |              |     |           |
ownership to the consumers can be reduced. areunabletofullymeetthedemandduetoitsuncertainty.
Althoughthisproblemcanbesolvedbyprovisioningmore
Incloudcomputing,aresourceprovisioningmechanism
resourceswithon-demandplantofittheextrademand,the
| is required | to supply |     | cloud consumers |     | a set | of computing |     |      |           |             |     |        |                |     |          |
| ----------- | --------- | --- | --------------- | --- | ----- | ------------ | --- | ---- | --------- | ----------- | --- | ------ | -------------- | --- | -------- |
|             |           |     |                 |     |       |              |     | high | cost will | be incurred |     | due to | more expensive |     | price of |
resourcesforprocessingthejobsandstoringthedata.Cloud
|           |     |             |           |     |              |     |        | resource | provisioning         |     | with | on-demand | plan.     | On     | the other |
| --------- | --- | ----------- | --------- | --- | ------------ | --- | ------ | -------- | -------------------- | --- | ---- | --------- | --------- | ------ | --------- |
| providers | can | offer cloud | consumers |     | two resource |     | provi- |          |                      |     |      |           |           |        |           |
|           |     |             |           |     |              |     |        | hand,    | the overprovisioning |     |      | problem   | can occur | if the | reserved  |
sioningplans,namelyshort-termon-demandandlong-term
resourcesaremorethantheactualdemandinwhichpartof
| reservation | plans. | Amazon | EC2 | [2] and | GoGrid | [3] | are, for |     |     |     |     |     |     |     |     |
| ----------- | ------ | ------ | --- | ------- | ------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
aresourcepoolwillbeunderutilized.Itisimportantforthe
|     |     |     |     |     |     |     |     | cloud | consumer | to  | minimize |     | the total cost | of  | resource |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | --- | -------- | --- | -------------- | --- | -------- |
. The authors are with the School of Computer Engineering, Nanyang provisioning by reducing the on-demand cost and over-
TechnologicalUniversity(NTU),NanyangAvenue,Singapore639798. subscribed cost of underprovisioning and overprovisioning.
E-mail:{siva0020,ebslee,dniyato}@ntu.edu.sg. To achieve this goal, the optimal computing resource
Manuscriptreceived3Apr.2010;revised6Sept.2010;accepted28Jan.2011; management is the critical issue.
publishedonline7Feb.2011.
|                 |     |           |          |                  |        |      |            | In               | this paper, | minimizing |          | both  | underprovisioning |     | and       |
| --------------- | --- | --------- | -------- | ---------------- | ------ | ---- | ---------- | ---------------- | ----------- | ---------- | -------- | ----- | ----------------- | --- | --------- |
| For information | on  | obtaining | reprints | of this article, | please | send | e-mail to: |                  |             |            |          |       |                   |     |           |
|                 |     |           |          |                  |        |      |            | overprovisioning |             |            | problems | under | the demand        |     | and price |
tsc@computer.organdreferenceIEEECSLogNumberTSCSI-2010-04-0030.
|     |     |     |     |     |     |     |     | uncertainty |     | in cloud | computing |     | environments |     | is our |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | --------- | --- | ------------ | --- | ------ |
DigitalObjectIdentifierno.10.1109/TSC.2011.7.
|     |     |     |     | 1939-1374/12/$31.00(cid:2)2012IEEE |     |     |     | PublishedbytheIEEEComputerSociety |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |

CHAISIRIETAL.: OPTIMIZATIONOFRESOURCEPROVISIONINGCOSTINCLOUDCOMPUTING 165
motivation to explore a resource provisioning strategy for proposed in which extra demanded resources can be more
cloud consumers. In particular, an optimal cloud resource efficiently provisioned. In [11], the concept of resource slot
provisioning(OCRP)algorithmisproposedtominimizethe was proposed. The objective is to address uncertainty of
totalcostforprovisioningresourcesinacertaintimeperiod. resources availability. In [12], a binary integer program to
Tomakeanoptimaldecision,thedemanduncertaintyfrom maximize revenues and utilization of resource providers
cloud consumer side and price uncertainty from cloud was formulated. However, [9], [10], [11], [12] did not
providers are taken into account to adjust the tradeoff consider uncertainty of future consumer demands. In [13],
betweenon-demandandoversubscribedcosts.Thisoptimal an optimization framework for resource provisioning was
developed.This frameworkconsidered multiple clientQoS
decisionisobtainedbyformulatingandsolvingastochastic
classes under uncertainty of workloads (e.g., demands of
integerprogrammingproblemwithmultistagerecourse[5].
computing resources). The arrival pattern of workloads is
Bendersdecomposition[6]andsample-averageapproxima-
estimated by using online forecasting techniques. In [14],
tion [7] are also discussed as the possible techniques to
heuristic method for service reservation was proposed.
solvetheOCRPalgorithm.Extensivenumericalstudiesand
Prediction of demand was performed to define reservation
simulationsareperformed,andtheresultsshowthatOCRP
prices. In [15], K-nearest-neighbors algorithm was applied
can minimize the total cost under uncertainty.
to predict the demand of resources. In contrast, our work
The major contributions of this paper lie in the
specifies that demands are given as probability distribu-
mathematicalanalysiswhichcanbesummarizedasfollows:
tions. In addition, the price difference between reservation
. The optimal cloud resource provisioning algorithm and on-demand plans was not taken into account in all
is proposed for the virtual machine management. works in the literature.
Asvirtualizationisacoretechnologyofcloudcomputing,
The optimization formulation of stochastic integer
the problem of virtual machine placement (VM placement)
programming is proposed to obtain the decision
becomescrucial[16],[17],[18],[19],[20].In[16],thebroker-
of the OCRP algorithm as such the total cost of
based architecture and algorithm for assigning VMs to
resource provisioning in cloud computing environ-
physicalserversweredeveloped.In[17],aresourcemanage-
ments is minimized. The formulation considers
mentconsistingofresourceprovisioningandVMplacement
multipleprovisioningstageswithdemandandprice
was proposed. In [18], techniques of VM placement and
uncertainties.
consolidation which leverage min-max and shares features
. ThesolutionmethodsbasedonBendersdecomposi-
providedbyhypervisorswereexplored.In[19],adynamic
tion and sample-average approximation algorithms
consolidationmechanismbasedonconstraintprogramming
are used to solve the optimization formulation in
was developed. This consolidation mechanism was origin-
an efficient way.
ally designed for homogeneous clusters. However, hetero-
. Theperformanceevaluationisperformedwhichcan
geneity which is common in a multiple cloud provider
reveal the importance of optimal computing re-
environment was ignored. Moreover, [16], [17], [18], [19]
source provisioning. The performance comparison
didnotconsideruncertaintyoffuturedemandsandprices.
among the OCRP algorithm and the other ap-
In[20],adynamicVMplacementwasproposed.However,
proaches is also presented.
the placement in [20] is heuristic-based which cannot
Theproposedmathematicalanalysiswillbeusefultothe
guaranteetheoptimalsolution.
cloud consumers (e.g., organization and company) for the Stochastic programming has been developed to solve
management of virtual machines in cloud computing resource planning under uncertainty [5] in various fields,
environment. The proposed OCRP algorithm will facilitate e.g., production planning, financial management, and
the adoption of cloud computing of the users as it can capacityplanning.Forexample,in[21],theauthorsapplied
reduce the cost of using computing resource significantly. the stochastic programming approach for planning of
The rest of this paper is organized as follows: Related electricalpowergenerationandtransmissionlineexpansion
works are reviewed in Section 2. The system model and whilesomeuncertaintiesaffectingtotheplanningaretaken
assumptionofcloudcomputingenvironmentaredescribed intoaccount.Itisshownthatstochasticprogrammingisthe
in Section 3. In Section 4, the stochastic programming promising mathematical tool which is able to address the
formulation of the OCRP algorithm is presented. Section 5 optimal decision making in the stochastic environment.
presents the Benders decomposition algorithm. Section 6 However, to the best of our knowledge, the application of
presents the sampling-average approximation approach. stochastic programming to computing resource provision-
Experiments and simulations to evaluate the performance ing has never been exclusively studied.
of the OCRP algorithm are presented in Section 7. Finally, The optimal virtual machine placement (OVMP) algorithm
conclusions are stated in Section 8. was proposed [22]. This OVMP algorithm can yield the
optimal solution for both resource provisioning and VM
placement in two provisioning stages. Motivated by this
2 RELATED WORK
previous work, we introduce the OCRP algorithm in this
Available resource provisioning options were discussed in paper which achieves many improvements. First, the
[8]. The resource provisioning strategies in distributed problemisgeneralized intothemultiple stageformulation.
systemswereaddressedin[9],[10],[11],[12],[13],[14],[15]. Second, the different approaches to obtain the solution of
In[9],anarchitecturaldesignofon-demandserviceforgrid computing resource provisioning are considered. Finally,
computingwasproposed.In[10],aprofile-basedapproach theperformanceevaluationisextendedtoconsidervarious
to capture expert’s knowledge of scaling applications was realistic scenarios.

166 IEEETRANSACTIONSONSERVICESCOMPUTING, VOL.5, NO.2, APRIL-JUNE2012
loadbalancer,tosupporttheconsumer’shostingVM.Note
thatthekeynotationsusedinthepaperarelistedinTable1.
3.2 Provisioning Plans
A cloud provider can offer the consumer two provisioning
plans, i.e., reservation and/or on-demand plans. For
planning, the cloud broker considers the reservation plan
asmedium-tolong-termplanning,sincetheplanhastobe
subscribed in advance (e.g., 1 or 3 years [2]) and the plan
can significantly reduce the total provisioning cost [4]. In
contrast,thebrokerconsiderstheon-demandplanasshort-
termplanning,sincetheon-demandplancanbepurchased
Fig.1.Systemmodelofcloudcomputingenvironment. anytime for short period of time (e.g., one week) when the
resources reserved by the reservation-plan are insufficient
3 SYSTEM MODELAND ASSUMPTION (e.g., during peak load).
3.1 Cloud Computing Environment 3.3 Provisioning Phases
As shown in Fig. 1, the system model of cloud computing The cloud broker considers both reservation and on-
environment consists of four main components, namely demand plans for provisioning resources. These resources
cloud consumer, virtual machine (VM) repository, cloud are used in different time intervals, also called provisioning
providers, and cloud broker. The cloud consumer has phases. There are three provisioning phases: reservation,
demand to execute jobs. Before the jobs are executed, expending, and on-demand phases. As shown in Fig. 2, these
computing resources has to be provisioned from cloud phaseswiththeiractionsperformindifferentpointsoftime
providers. To obtain such resources, the consumer firstly (orevents)asfollows.Firstinthereservationphase,without
creates VMs integrated with software required by the knowing the consumer’s actual demand, the cloud broker
jobs. The created VMs are stored in the VM repository. provisions resources with reservation plan in advance. In
Then, the VMs can be hosted on cloud providers’ the expending phase, the price and demand are realized,
infrastructures whose resources can be utilized by the and the reserved resources can be utilized. As a result, the
VMs. In Fig. 1, the cloud broker is located in the cloud reserved resources could be observed to be either over-
consumer’s site and is responsible on behalf of the cloud provisioned or underprovisioned. If the demand exceeds
consumer for provision resources for hosting the VMs. In the amount of reserved resources (i.e., underprovisioned),
addition, the broker can allocate the VMs originally stored thebrokercanpayforadditionalresourceswithon-demand
in the VM repository to appropriate cloud providers. The plan,andthenthe on-demandphasestarts.
broker implements the OCRP algorithm to make an
3.4 Provisioning Stages
optimal decision of resource provisioning.
A provisioning stage is the time epoch when the cloud
In OCRP, there are multiple VM classes used to classify
brokermakesadecisiontoprovisionresourcesbypurchas-
different types of VM. Let I (cid:2)IN 1 1 denote the set of VM
ingreservationand/oron-demandplans,andalsoallocates
classes.ItisassumedthatoneVMclassrepresentsadistinct
VMs to cloud providers for utilizing the provisioned
typeofjobs(e.g.,oneclassforwebapplicationandtheother
resources. Therefore, each provisioning stage can consist
for database application). A certain amount of resources is
of one or more provisioning phases. The number of
required for running the VM, and this required amount of
provisioning stages is based on the number of planning
resources canbedifferent forVM in different classes.With
epoches considered by the cloud broker, e.g., a yearly plan
this resource requirement, the cloud broker can reserve
consistsof12provisioningstages(i.e.,12months).LetT (cid:2)
computingresourcesfromcloudproviderstobeusedinthe IN 1 denote the set of all provisioning stages where jTj(cid:3)2.
futureaccordingtotheactualdemand.Thisdemandcanbe For resource provisioning under uncertainty, the broker is
determinedasthenumberofcreatedVMs.Inthiscase,itis assumed to be able to reserve the resources in the first
possible that additional resources can be provisioned provisioning stage. Also, the broker obtains a solution,
instantly from cloud providers if the reserved resources is called recourse action [5], for provisioning resources against
not enough to accommodate the actual demand. uncertainty parameters (i.e., demand and price) in every
LetJ (cid:2)IN 1denotethesetofcloudproviders.Eachcloud stage. These uncertainty parameters in each stage will be
provider supplies a pool of resources to the consumer. Let observed by the broker after the resource reservation has
R denote the set of resource types which can be provided beenmade.Theobserveduncertaintyparametersarecalled
by cloud providers. Resource types can be computing realization (e.g., the actual number of created VMs after the
power (in unit of CPU-hours), storage (in unit of GBs/ jobsaresubmittedbytheconsumers).Then,thebrokerwill
month), and network bandwidth for Internet data transfer take the recourse action according to the realization, e.g.,
(inunitofGBs/month).EachVMclassspecifiestheamount utilizing the reserved resource and/or provisioning more
ofresourcesineachresourcetype.Letb ir betheamountof resource with on-demand plan.
resource type r required by the VM in class i2I. It is Fig. 3 shows the relationship between provisioning
assumed that every cloud provider prepares facilities, e.g., phases and provisioning stages, where a yearly plan with
virtualization management software, network facility, and 12 provisioning stages, namely T ¼fT 1 ;T 2 ;...;T 12 g, is
considered. Fig. 3a shows the example of all three
1.IN1¼f1;2;3;...g. provisioning phases existing in each stage. In Fig. 3b, each

CHAISIRIETAL.: OPTIMIZATIONOFRESOURCEPROVISIONINGCOSTINCLOUDCOMPUTING 167
TABLE1
|     |     |     |     |     |     | Listof KeyNotations |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
stage may not consist of all provisioning phases. For reservation contract refers to the advance reservation of
example, the reservation phase is performed in T and the resources with the specific time duration of usage. For
1
number of resources are reserved. From T 1-T 3, the expend- example, the reservation plan offered by Amazon EC2 has
tworeservationcontracts[2],namely1-yearcontractand3-
| ing phase | starts | in some | points | of time | when | some |     |     |     |     |     |     |     |     |
| --------- | ------ | ------- | ------ | ------- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
resources reserved in T 1 are utilized. Then, the on-demand yearcontract.Thecertainamountofresourcesarereserved
phasestartsinT duetotheinsufficientreservedresources, for1yearintheone-yearcontractand3yearsinthethree-year
3
contractstartingfromthetimewhentheyareprovisioned.
| andsomeresourcesareprovisioned |             |       |        | withon-demand |        | plan. |                |         |          |            |        |             |           |     |
| ------------------------------ | ----------- | ----- | ------ | ------------- | ------ | ----- | -------------- | ------- | -------- | ---------- | ------ | ----------- | --------- | --- |
|                                |             |       |        |               |        |       | Let K(cid:2)IN |         | denote   | the set    | of all | reservation | contracts |     |
| In T 4, the                    | reservation | phase | starts | again and     | so on. |       |                | 1       |          |            |        |             |           |     |
|                                |             |       |        |               |        |       | which are      | offered | by cloud | providers. |        | Let         | L denote  | the |
k
| 3.5 Reservation |     | Contracts |     |     |     |     |               |     |          |                 |     |         |           |     |
| --------------- | --- | --------- | --- | --- | --- | --- | ------------- | --- | -------- | --------------- | --- | ------- | --------- | --- |
|                 |     |           |     |     |     |     | time duration |     | (in unit | of provisioning |     | stages) | specified | in  |
A cloud provider can offer the consumer multiple reserva- reservationcontractk2K.LetT kdenotethesetofstagesat
tion plans with different reservation contracts. Each whichthecloudbrokercanprovisionresourcesbycontract
|     |     |     |     |     |     |     | k. Let F | be  | the set of | stages | at  | which | some resources |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | ------ | --- | ----- | -------------- | --- |
kt
|     |     |     |     |     |     |     |                     |             | k                     |                           |             |      |          | t2T.     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | ----------- | --------------------- | ------------------------- | ----------- | ---- | -------- | -------- |
|     |     |     |     |     |     |     | reserved            | by contract |                       | could                     | be utilized |      | at stage |          |
|     |     |     |     |     |     |     | Given the           | total       | number                | of stages                 | jTj,        | both | T k and  | F kt are |
|     |     |     |     |     |     |     | expressed           | as follows: |                       |                           |             |      |          |          |
|     |     |     |     |     |     |     |                     |             | T ¼f1;...;jTj(cid:4)L |                           |             | þ1g; |          | ð1Þ      |
|     |     |     |     |     |     |     |                     |             | k                     |                           |             | k    |          |          |
|     |     |     |     |     |     |     | F ¼fmaxð1;t(cid:4)L |             |                       | þ1Þ;...;minðt;jTj(cid:4)L |             |      | þ1Þg:    | ð2Þ      |
|     |     |     |     |     |     |     | kt                  |             | k                     |                           |             |      | k        |          |
Fig.2.Transitionofprovisioningphases.
|     |     |     |     |     |     |     | In Fig.                 | 4, the | example | of             | advance | reservation |               | for the |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | ------ | ------- | -------------- | ------- | ----------- | ------------- | ------- |
|     |     |     |     |     |     |     | yearlyplanwith3-month(K |        |         | 1)and6-month(K |         |             | 2)reservation |         |
Fig. 3. Relationship between provisioning phases and provisioning Fig.4.Exampleofadvancereservationswith3-month(K 1)and6-month
| stages. |     |     |     |     |     |     | (K 2)contracts. |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |

168 IEEETRANSACTIONSONSERVICESCOMPUTING, VOL.5, NO.2, APRIL-JUNE2012
c a o b n o t v r e ac t t h s e is ti s m h e o l w in n e ( r i e .e p ., re L se K n 1 t ¼ th 3 e an ti d me L K c 2 o ¼ ve 6 ra ). ge Th o e f b s o o x m e e s a p n ro d v c id ðeÞ ed ð!Þ b , y de c f l i o n u e d dw p i r t o h v t i h d e er sim j, il r a e r sp w e a c y tiv a e s ly (4 . ), L d e e t no cð i t j r e k Þ t t ð h ! e Þ
ijkt
reserved contracts. As shown in (1), T K1 ¼fT 1 ;T 2 ;...;T 10 g reservation and expending costs for provisioning every
and T K2 ¼fT 1 ;T 2 ;...;T 7 g are the sets of stages at which resource type, respectively.
resources can be provisioned by K 1 and K 2, respectively. In on-demand phase, let cð j o rt Þð!Þ denote the unit price of
Contract K 1 is subscribed three times (e.g., T 7-T 9), while resource type r provided by cloud provider j in provision-
contract K 2 is subscribed twice (e.g., T 5-T 10). Fig. 4 also ingstagetgivenscenario!.Also,thepricecanbechanged
shows that some stages can be covered by two (or more) by cloud providers (i.e., uncertain to consumer when the
subscribedcontracts,e.g.,T 1-T
3
arecoveredbycontractsK
1 resource is reserved). Let
cðoÞð!Þ,
defined with the similar
ijt
and K 2. In Fig. 4, any set F kt in (2) can be obtained, e.g., way as (4), denote the on-demand cost for provisioning
F
K1T4
¼fT
2
;T
3
;T
4
g,F
K1T11
¼fT
9
;T
10
g,andF
K2T12
¼fT
7
g.
every resource type. Given VM class i, cloud provider j,
3.6 Uncertainty of Parameters provisioning stage t, and scenario !, the expending cost of
anyreservationcontractkisassumedtobecheaperthanthe
The optimal solution used by the cloud broker is obtained
on-demand cost (i.e.,
cðeÞ ð!Þ<cðoÞð!Þ).
from the OCRP algorithm based on stochastic integer ijkt ijt
programming [5]. Stochastic programming takes a set of From the system model and assumption, the optimal
uncertainty parameters (called scenarios), described by a cloud resource provisioning algorithm is developed to
probabilitydistributionintoaccount.Let(cid:2)denotethesetof minimize the total provisioning costs under the price and
all scenarios in every provisioning stage and (cid:2) t denote the demanduncertainty inmultiple provisioning stages.In the
set of all scenarios in provisioning stage t. Set (cid:2) is defined nextsection,thestochasticprogrammingformulationofthe
as the Cartesian product of all (cid:2), namely OCRP algorithm is presented.
t
Y
(cid:2)¼ (cid:2)
t
¼(cid:2)
1
(cid:5)(cid:2)
2
(cid:5)(cid:6)(cid:6)(cid:6)(cid:5)(cid:2)
jTj
: ð3Þ
4 STOCHASTIC PROGRAMMING MODEL
t2T
Inthissection,thestochasticprogrammingwithmultistage
Itisassumedthattheprobabilitydistributionof(cid:2)hasfinite
recourse [5] is presented as the core formulation of the
support, i.e., set (cid:2) has a finite number of scenarios with
OCRP algorithm. First, the original form of stochastic
respective probabilities pð!Þ2½0;1(cid:7) where ! is a composite
integer programming formulation is derived. Then, the
variable defined as !¼ð! 1 ;...;! jTj Þ2(cid:2). In this paper, formulationistransformedintothedeterministicequivalent
demand and price are considered as scenarios in (cid:2) whose
formulation (DEF) which can be solved by traditional
probability distribution is assumed to be available. The
optimization solver software.
actualscenarioofuncertaintyparameterafteritisobserved
by the broker is called realization. 4.1 Stochastic Integer Programming for OCRP
Minimize:
3.7 Provisioning Costs
With three aforementioned provisioning phases, there are z¼ XXX cðRÞxðRÞþIE (cid:2) Q (cid:3) xðRÞ;! (cid:4)(cid:5) ; ð5Þ
ijk ijk (cid:2) ijk
three corresponding provisioning costs incurred in these
i2I j2J k2K
phases, namely reservation, expending, and on-demand
subject to:
costs. The main objective of the OCRP algorithm is to
minimizeallofthesecostswhiletheconsumer’sdemandis
xðRÞ 2IN ; 8i2I;8j2J;8k2K: ð6Þ
met, given the uncertainty of demand and price. ijk 0
Forcloudprovider,thepriceisdefinedindollars($)per
The general form of stochastic integer program of the
resourceunit.LetcðRÞ
denotetheunitprice(i.e.,coststothe
jkr OCRP algorithm is formulated in (5) and (6). The objective
consumer) of resource type r subscribed to reservation
function (5) is to minimize the cloud consumer’s total
contract k provided by cloud provider j in reservation
provisioning cost. Decision variable
xðRÞ
denotes the
phase of the first provisioning stage. It is assumed that the ijk
numberofVMsprovisionedin thefirstprovisioningstage.
price of reservation plan in the first stage is charged by a
fixed one-time fee. The reservation cost
cðRÞ
is the cost for
Inotherwords,thisnumberreferstoasthetotalamountof
ijk reserved resources. The expected cost under the uncer-
provisioning every resource type defined as follows:
tainty (cid:2) is defined as IE (cid:2) ½Qðxð ij R k Þ;!Þ(cid:7) where Qðxð ij R k Þ;!Þ is
cðRÞ ¼ X b cðRÞ: ð4Þ expressed as follows:
ijk ir jkr
r2R
Q (cid:3) xðRÞ;! (cid:4) ¼ min CðYÞ; Y 2(cid:3) (cid:3) xðRÞ;! (cid:4) : ð7Þ
The prices in reservation and expending phases could be ijk Y¼ðxðrÞð!Þ;xðeÞð!Þ;xðoÞð!ÞÞ ijk
ijkt ijkt ijt
adjusted by cloud providers without informing the con-
sumerinadvance,exceptthepriceofthereservationplanin In (7), the objective of
Qðxð
ij
R
k
Þ;!Þ
is to minimize the cost
thefirstprovisioningstage.Forinstance,thecostofelectric under uncertainty given scenario ! and xð ij R k Þ . Such cost is
power to supply a cloud provider’s data center could be represented by Cð(cid:6)Þ and defined in (9). Composite variable
increased bypowerplantsinthe next fewmonths,andthe Y representing the solution of QðxðRÞ;!Þ consists of
ijk
cloud provider will be able to increase the costs of variables, namely xðrÞ ð!Þ, xðeÞ ð!Þ, and xðoÞð!Þ, which
ijkt ijkt ijt
computing resources in the future as well. For the prices denote the numbers of VMs provisioned in reservation,
inprovisioningstagetgivenscenario!inbothreservation expending, and on-demand phases, respectively. Set
and expending phases, cðrÞ ð!Þ and cðeÞ ð!Þ denote the unit (cid:3)ðxðRÞ;!Þ controls the relationship among the variables by
jkrt jkrt ijk
prices of resource type r with reservation contract k constraints as expressed in (8)-(15). The constraint in (10)

CHAISIRIETAL.: OPTIMIZATIONOFRESOURCEPROVISIONINGCOSTINCLOUDCOMPUTING 169
maintains the amount of resources utilized in expending subject to: (6)
phase to be less than or equal to the number of reserved
resourcesasstatedin(2).In(11),theconstraintimpliesthat xð ij e k Þ t ð!Þ(cid:8) X xð ij r k Þ t^ ð!Þ; 8i2I;8j2J;8k2K;8t2T;8!2(cid:2); ð17Þ
the reservation in the first stage can be performed without t^2Fkt
any uncertainty. The constraint in (12) ensures that the
consumer’s demand for VM class i2I in stage t2T is xðRÞ ¼xðrÞ ð!Þ; t¼1;8i2I;8j2J;8k2K;8!2(cid:2); ð18Þ
ijk ijkt
met. The constraint in (13) states that the allocation of
resources for VMsmust notexceed the maximum resource
!
capacity offered by a cloud provider. Constraints (14) and X X xðeÞ ð!ÞþxðoÞð!Þ (cid:3)d ð!Þ; 8i2I;8t2T;8!2(cid:2); ð19Þ
(15) indicate that variables take the values from a set of ijkt ijt it
j2J k2K
nonnegative integer numbers (i.e., IN 0).
!
Q (cid:3) xð ij R k Þ;! (cid:4) ¼minCðYÞ; ð8Þ X b ir X xð ij e k Þ t ð!Þþxð ij o t Þð!Þ (cid:8)a jrt ð!Þ; 8j2J;8r2R;8t2T;8!2(cid:2);
i2I k2K
where
ð20Þ
CðYÞ¼ XXXX cðrÞ ð!ÞxðrÞ ð!Þ
ijkt ijkt
i2I j2J k2Kt2T k !ð9Þ xð ij r k Þ t ð!Þ2IN 0 ; 8i2I;8j2J;8k2K;8t2T k ;8!2(cid:2); ð21Þ
þ XXX X cðeÞ ð!ÞxðeÞ ð!ÞþcðoÞð!ÞxðoÞð!Þ ;
ijkt ijkt ijt ijt
i2I j2J t2T k2K xð ij e k Þ t ð!Þ2IN 0 ; 8i2I;8j2J;8k2K;8t2T;8!2(cid:2); ð22Þ
subject to:
xðeÞ ð!Þ(cid:8) X xðrÞ ð!Þ; 8i2I;8j2J;8k2K;8t2T; ð10Þ
xð
ij
o
t
Þð!Þ2IN
0
; 8i2I;8j2J;8t2T;8!2(cid:2): ð23Þ
ijkt ijkt^
t^2Fkt
5 BENDERS DECOMPOSITION
xðRÞ ¼xðrÞ ð!Þ; t¼1;8i2I;8j2J;8k2K; ð11Þ In this section, the Benders decomposition algorithm [6] is
ijk ijkt
applied to solve the stochastic programming problem
formulated in Section 4. The goal of this algorithm is to
!
X X xðeÞ ð!ÞþxðoÞð!Þ (cid:3)d ð!Þ; 8i2I;8t2T; ð12Þ breakdowntheoptimizationproblemintomultiplesmaller
ijkt ijt it problems which can be solved independently and paral-
j2J k2K
lelly.Asaresult,thetimetoobtainthesolutionoftheOCRP
algorithm can be reduced. The Benders decomposition
!
X b X xðeÞð!ÞþxðoÞð!Þ (cid:8)a ð!Þ; 8j2J;8r2R;8t2T; ð13Þ algorithm can decompose integer programming problems
ir ijkt ijt jrt with complicating variables into two major problems:
i2I k2K master problem and subproblem.
Property 1. The DEF derived in (16)-(23) is the problem whose
xðrÞ ð!Þ2IN ; 8i2I;8j2J;8k2K;8t2T ; ð14Þ
ijkt 0 k structure has multiple complicating variables.
Proof. Variables xðeÞ ð!Þ from the DEF defined in (16)-(23)
ijkt
x i ð j e k Þ t ð!Þ2IN 0 ;xð ij o t Þð!Þ2IN 0 ; 8i2I;8j2J;8k2K;8t2T: ð15Þ are considered as complicating variables [6]. Since
variables xðeÞ ð!Þ exist in constraints (17), (19), and (20),
ijkt
4.2 Deterministic Equivalent Formulation
the variables prevent the decomposability of the DEF. If
Given a probability distribution of all scenarios in set (cid:2), variables xðeÞ ð!Þ are given the fixed values are denoted
ijkt
the formulation in (5)-(15) can be transformed into the byxðfixÞð!Þ,theDEFcanbedecomposedintotwotypesof
ijkt
deterministic integer programming called deterministic independent optimization subproblems, namely S 1 and
equivalent formulation as expressed in (16)-(23). To solve S 2 ð!Þ presented as follows:
this DEF, probability distributions of both price and ½S 1 (cid:7) Minimize:
demand must be available, i.e., pð!Þ in (16). Then, the
DEFcan besolved byusingtraditional optimization solver zðrÞ¼ XXX cðRÞxðRÞ
(cid:2) ijk ijk
software. For example, the formulation is implemented i2Ij2Jk2K
ð24Þ
using MathProg script, and then the script is solved by þ XXXXX pð!ÞcðrÞ ð!ÞxðrÞ ð!Þ;
GNU Linear Programming Kit (GLPK) [23]. ijkt ijkt
!2(cid:2)i2Ij2Jk2Kt2Tk
Minimize:
subject to: (6), (17), (18), (21)
z^ (cid:2) ¼ XXX cð ij R k Þxð ij R k Þþ XXXXX pð!Þcð ij r k Þ t ð!Þxð ij r k Þ t ð!Þ xðeÞ ð!Þ¼xðfixÞð!Þ; 8i2I;8j2J;8k2K;8t2T;8!2(cid:2); ð25Þ
i2Ij2Jk2K !2(cid:2)i2Ij2Jk2Kt2Tk ijkt ijkt
!
þ XXXX pð!Þ X cðeÞ ð!ÞxðeÞ ð!ÞþcðoÞð!ÞxðoÞð!Þ ; ½S 2 ð!Þ(cid:7) Minimize:
ijkt ijkt ijt ijt
!2(cid:2)i2Ij2Jt2T k2K zðoÞð!Þ¼ XXX pð!ÞcðoÞð!ÞxðoÞð!Þ; ð26Þ
(cid:2) ijt ijt
ð16Þ i2I j2J t2T

170 IEEETRANSACTIONSONSERVICESCOMPUTING, VOL.5, NO.2, APRIL-JUNE2012
Theobjectivefunction(28)isdirectlyderivedfromthatin
(16). xðeÞ ð!Þ represents variable xðeÞ ð!Þ in iteration (cid:2) of
ijkt(cid:2) ijkt
master problem, while variable (cid:3) (cid:2) provides the minimum
costgivenreservationandon-demandcosts.This(cid:3) (cid:2) willbe
improvedinconsequentiterations.Initially,(cid:3) (cid:2) canbefixed
byconstant(cid:3)ðlbÞasshowninconstraint(29).This(cid:3)ðlbÞcanbe
estimated from an economical analysis orhistorical data of
priorsolutions[6].Constraints(30)-(32)definetheboundary
ofxðeÞ ð!Þ.Aftersolvingthemasterproblem,thealgorithm
ijkt(cid:2)
proceedstothe Step-1.
Step-1: Subproblem solution. In Step-1, multiple subpro-
blems are formulated and solved. Lets assign solution
xðeÞ ð!Þ obtained from the master problem to variables
ijkt(cid:2)
xðfixÞð!Þ:
ijkt
Given the fixed solution
xðfixÞð!Þ,
two aforementioned
Fig.5.FlowchartofBendersdecompositionalgorithm. ijkt
subproblems, namely, S 1 and S 2 ð!Þ can be solved
concurrently.
subject to: (19), (20), (23)
ThesubproblemS 1 ispresentedin(24)-(25)inwhichthe
xðeÞ ð!Þ¼xðfixÞð!Þ; 8i2I;8j2J;8k2K;8t2T: ð27Þ objective function is to minimize the reservation cost. Let
ijkt ijkt variable (cid:4)ðrÞ ð!Þ denote the optimal solution of the dual
ijkt(cid:2)
From this decomposition, we conclude that the DEF has problemof S 1 in iteration (cid:2) associatedwith constraint (25).
the structure with multiple complicating variables. tu The solution of (cid:4)ðrÞ ð!Þ will be used in Step-3.
ijkt(cid:2)
From Property 1, the problem can be solved by Benders The subproblem S 2 ð!Þ is presented in (26)-(27) in which
the objective function is to minimize the on-demand cost
decomposition algorithm. The algorithm consists of steps
whichareperformediteratively.Ateachiteration,themaster when the realization is set to !. S 2 ð!Þ associates with the
number of scenarios j(cid:2)j, and hence j(cid:2)j subproblems are
problem constituted by the complicating variables and
generated. Note that j(cid:2)j is the Cardinality of set (cid:2). Let
subproblems constituted by the other decision variables variable (cid:4)ðoÞ ð!Þ denote the optimal value of the dual
aresolved,thenlowerandupperboundsarecalculated.The ijkt(cid:2)
problem of S 2 ð!Þ in iteration (cid:2) associated with constraint
algorithm stops when optimal solution converges, i.e., the (27).Thesolutionof(cid:4)ðoÞ ð!ÞwillbeusedinStep-3.
ijkt(cid:2)
lowerandupperboundsaresatisfactorilyclosetoeachother. Step-2:Convergencechecking.InStep-2,theconvergenceof
In Fig. 5, the flowchart of Benders decompostion
lower and upper bounds of the solutions obtained from
algorithm is shown. The algorithm for solving OCRP is master problem and subproblems is checked. Both bounds
presented in four steps (i.e., Step-0 to Step-3) as follows. areadjustedineachiteration.Thelowerboundiniteration
Step-0: Initialization of the master problem. In Step-0, the (cid:2) denoted as zðlbÞ can be obtained from the objective
(cid:2)
step is the initialization of the master problem. This Step-0 function of the master problem, i.e., zðlbÞ ¼z(cid:9)ðeÞ. The upper
(cid:2) (cid:2)
is performed only once, while Step-1 to Step-3 are bound in iteration (cid:2) denoted by zðubÞ can be obtained from
(cid:2)
repeatable in the algorithm. Let (cid:2) denote the iteration
counter and initially set (cid:2)¼1. The master problem as zðubÞ ¼z(cid:9)ðeÞ(cid:4)(cid:3) þz(cid:9)ðrÞþ X z(cid:9)ðoÞð!Þ: ð33Þ
(cid:2) (cid:2) (cid:2) (cid:2) (cid:2)
expressed in (28)-(32) is an alternative form of the
!2(cid:2)
formulation DEF shown in (16)-(23).
Let (cid:5) denote a small tolerance value to verify the
Minimize:
convergenceofbothlowerandupperbounds.TheBenders
zðeÞ ¼ XXXXX pð!ÞcðeÞ ð!ÞxðeÞ ð!Þþ(cid:3) ; ð28Þ decompositionalgorithmstopswhenzð (cid:2) ubÞ(cid:4)zð (cid:2) lbÞ <(cid:5),which
(cid:2) ijkt ijkt(cid:2) (cid:2) means both bounds are acceptably close to each other and
!2(cid:2) i2I j2J t2T k2K
theoptimalsolutioncanbefoundiniteration(cid:2).Otherwise,
subject to: thealgorithmproceedstothenextiterationinwhichStep-3
will perform.
(cid:3) (cid:2) (cid:3)(cid:3)ðlbÞ; ð29Þ Step-3: Master problem solution.
X x i ð j e k Þ t(cid:2) ð!Þ(cid:8)d it ð!Þ; 8i2I;8t2T;8!2(cid:2); ð30Þ (cid:3) (cid:2) (cid:3) XXXXX(cid:3)(cid:3) (cid:4)ð ij r k Þ t(cid:2) ð!Þþ(cid:4)ð ij o k Þ t(cid:2) ð!Þ (cid:4)
j2J !2(cid:2) i2I j2J k2Kt2T
(cid:3) xðeÞ ð!Þ(cid:4)xðeÞ ð!Þ (cid:4)(cid:4) ð34Þ
XX b ir xð ij e k Þ t ð!Þ(cid:8)a jrt ð!Þ; 8j2J;8r2R;8t2T;8!2(cid:2);ð31Þ þ i z jk (cid:9) t ð (cid:2) rÞþ X z ij (cid:9) k ð t o (cid:2) Þð!Þ; (cid:2) 2f1;...;(cid:2)(cid:4)1g:
i2I k2K (cid:2) (cid:2)
!2(cid:2)
xðeÞ ð!Þ2IN ; 8i2I;8j2J;8k2K;8t2T;8!2(cid:2); ð32Þ Let the iteration counter be increased by (cid:2) (cid:2)þ1.
ijkt(cid:2) 0
Then,themasterproblemin(28)-(32)canbefurtherrelaxed

CHAISIRIETAL.: OPTIMIZATIONOFRESOURCEPROVISIONINGCOSTINCLOUDCOMPUTING 171
byadditionalconstraintscalledBenderscuts[6].Inaddition, xð ij r k Þ t ð! n Þ2IN 0 ; 8i2I;8j2J;8k2K;8t2T k ;8n2N; ð40Þ
the solution of the master problem will adjust the cost (cid:3) (cid:2)
a
x
n
ðe
d
Þ ð
a
!
l
Þ
s
.
o
As
th
s
e
ho
e
w
x
n
pe
i
n
n
d
(
i
3
n
4
g
),t
c
h
o
e
st
Be
a
n
c
d
c
e
o
r
r
s
d
c
in
u
g
tsa
to
rec
so
o
l
n
u
s
t
t
i
r
o
u
n
cte
o
d
f xð
ij
e
k
Þ
t
ð!
n
Þ;xð
ij
o
t
Þð!
n
Þ2IN
0
; 8i2I;8j2J;8k2K;8t2T;8n2N:ð41Þ
ijkt(cid:2)
from the optimal costs obtained from master problem and
subproblems in the prior iterations. After solving this Q^(cid:3) xðRÞ;N (cid:4) ¼ 1 X N Q (cid:3) xðRÞ;! (cid:4) : ð42Þ
master problem, Step-1 is repeated and the same iterative ijk N ijk n
n¼1
process continues.
Letz(cid:9) andx(cid:9) denotetheoptimalobjectivefunctionvalue
andoptimalsolutionoftheoriginalformulation(definedin
6 SAMPLE-AVERAGE APPROXIMATION
(5)and(6)),respectively.Letz^(cid:9) andx^(cid:9) denotetheoptimal
N N
In the case that the number of scenarios is numerous, it objective function value and optimal solution of the AP
may not be efficient to obtain the solution of the OCRP formulation, respectively. Note that although z^(cid:9) becomes
N
algorithm by solving the stochastic programming formula- closer to z(cid:9) when N is large, value z^(cid:9) naturally varies
N
tion defined in (16)-(23) directly if all scenarios in the according to set of samples (cid:2) . Therefore, an estimation
N
problem are considered. To address this complexity issue, method is required to achieve the SAA lower and upper
the sample-average approximation (SAA) approach is bounds of the optimal solution. Obviously, z^(cid:9) forms the
N
applied [7]. This approach selects a set of scenarios, e.g., SAA upper bound of z(cid:9) as follows:
N scenarios, where N is smaller than the total number of
scenarios j(cid:2)j. Then, these N scenarios can be solved in a z(cid:9) (cid:8)z^(cid:9) : ð43Þ
N
deterministic equivalent formulation. The optimal solution
Inaddition,theSAAlowerboundofz(cid:9) isformedbythe
can be obtained if N is large enough which can beverified
following unbiased property
numerically.
In this section, the SAA approach is applied to IE½z^(cid:9) (cid:7)(cid:8)z(cid:9): ð44Þ
N
approximate the expected cost in every considered provi-
sioning stage, i.e., QðxðRÞ;!Þ in (7). A sampling method For the properties in (43) and (44), bounding method is
ijk
required to obtain the estimates of both SAA upper and
(e.g.,MonteCarlo[24]andLatinhypercube[25]),isusedto
generatescenarios(cid:2) N ¼f! 1 ;...;! N g,whereN denotesthe lower bounds on z(cid:9) with a certain confidence interval. The
next two following sections present the estimation of the
sample size. Let N ¼f1;...;Ng be the set of indices of
SAA bounds by applying the similar method to that in [7],
samples. Then, the expected cost can be redefined as
[21], [24].
shown in (42).
The function
Q^ðxð
ij
R
k
Þ;NÞ
is the SAA to the objective 6.1 SAA Lower Bound Estimates
functionin(5).Then,theproblemcanbetransformedintoa
The expected value IE½z^(cid:9) (cid:7) can be estimated by generating
deterministic equivalent formulation, as called approxima- N
M independent batches,2 each of size N, denoted as
tion problem (AP) formulation, as expressed in (35)-(41).
! 1;m ;...; ! N;m where m2f1;...;Mg, then solving the AP
Minimize:
formulation. Let z^(cid:9) denote the solution given batch m.
N;m
z^ ¼ XXX cðRÞxðRÞþ 1 XXXXX cðrÞ ð! ÞxðrÞ ð! Þ Next, the SAA lower bound can be obtained from
N ijk ijk N ijkt n ijkt n
i2Ij2Jk2K n2Ni2Ij2Jk2Kt2Tk 1 X M
! L ¼ z^(cid:9) : ð45Þ
þ
N
1XXXX X cð
ij
e
k
Þð!
n
Þxð
ij
e
k
Þ
t
ð!
n
Þþcð
ij
o
t
Þð!
n
Þxð
ij
o
t
Þð!
n
Þ N;M M m¼1 N;m
n2Ni2Ij2Jt2T k2K Dueto(44),thisL N;M isanunbiasedestimatorofthemean
ð35Þ IE½z^(cid:9) (cid:7) which forms a statistical lower bound for z(cid:9). When
N
the generated M batches are independent and identically
subject to: (6)
distributed (i.i.d.) by the Central Limit Theorem, the
xðeÞ ð! Þ(cid:8) X xðrÞ ; 8i2I;8j2J;8k2K;8t2T;8n2N; ð36Þ distribution of SAA lower bound estimate converges to a
ijkt n
t^2Fkt
ijkt^
normal distribution Nð0;(cid:6)2 L Þ,3 namely
p
xðRÞ¼xðrÞ ð! Þ; t¼1;8i2I;8j2J;8k2K;8n2N; ð37Þ ffi M ffiffiffiffi ðL N;M (cid:4)IE½z^(cid:9) N (cid:7)Þ! D Nð0;(cid:6)2 L Þ; as M !1; ð46Þ
ijk ijkt n
where (cid:6)2 ¼Var½z^(cid:9) (cid:7)4 which can be approximated by the
L N
! sample variance estimator s2ðMÞ as follows:
L
X X xðeÞ ð! ÞþxðoÞð! Þ (cid:3)d ð! Þ; 8i2I;8t2T;8n2N;
j2J k2K ijkt n ijt n it n s2ðMÞ¼ 1 X M ðz^(cid:9) (cid:4)L Þ2: ð47Þ
L M(cid:4)1 N;m N;M
ð38Þ m¼1
Finally, the ð1(cid:4)(cid:3)Þ-confidence interval of the SAA lower
!
X b X xðeÞ ð! ÞþxðoÞð! Þ (cid:8)a ð! Þ; bound can be defined as
ir ijkt n ijt n jrt n ð39Þ
i2I k2K
2.Abatchisasetofsamplesgeneratedbyasamplingtechnique.
8j2J;8r2R;8t2T;8n2N; 3.Nð0;(cid:6)2Þdenotesthenormaldistributionwithmean0andvariance(cid:6)2.
L L
4.Var½z^(cid:9)(cid:7)denotesthevarianceofsamples.
N

172 IEEETRANSACTIONSONSERVICESCOMPUTING, VOL.5, NO.2, APRIL-JUNE2012
(cid:7) z s ðMÞ z s ðMÞ(cid:8)
L (cid:4) (cid:3)=2 p L ;L þ (cid:3)=2 p L ; ð48Þ 7 PERFORMANCE EVALUATION
N;M ffiffiffiffiffi N;M ffiffiffiffiffi
M M
Inthissection,theperformanceevaluationoftheproposed
wherez (cid:3)satisfiesProbfNð0;1Þ(cid:8)z (cid:3) g¼1(cid:4)(cid:3).Notethatthe OCRP algorithm is presented. Two case studies are
valuez fromtheZ-distributioncanbereplacedbycritical considered in this evaluation, namely two provisioning stage
(cid:3)=2
valuet fromtheStudent’st-distributionifMissmall. problem (2-PSP) and 12 provisioning stage problem (12-PSP).
(cid:3)=2;M(cid:4)1
The former, 2-PSP, has only two provisioning stages. We
6.2 SAA Upper Bound Estimates assume that the cloud broker is making a decision for
Asshownin(43),z^(cid:9) formstheSAAupperboundofz(cid:9).By provisioning resources at the end of year. Under price and
N
selectingasolutionx^(cid:9) obtainedbysolvingtheAPformula- demand uncertainty, the cloud broker performs the
N
tion, the SAA upper bound can be estimated by using the advance reservation of resources in the first stage for
unbiasedestimatorofz^(cid:9) .Toachievethisestimator,wecan being used in the next whole year which is the second
N
generateM~ independentbatches,eachofsizeN~ ,denotedas stage. Therefore, the 1-year reservation contract is suffi-
! 1;m ;...;! N~;m where m2f1;...;M~g. Since solution x^(cid:9) N is ciently required by the broker since the contract can cover
already fixed to the SAA problem, i.e., z^ N ðx^(cid:9) N Þ, given N~ the time duration. At the second stage, the price and
demand are observed. Then, the number of reserved
samplesofeachgeneratedbatch,theobjectivefunction(35)
can be decomposed into
N~
independent subproblems in
resources are utilized and some additional amount of
resources can be provisioned in an on-demand fashion.
which each of them can be solved independently and in
For 12-PSP, we consider 12 months in a year and hence
parallel. Thus, these subproblems can be solved more
efficiently than the original AP formulation. After all the stage is defined as T ¼fT 1 ;T 2 ;...;T 12 g. In each stage,
the cloud broker can perform an advance reservation of
subproblems are solved, each batch yields the solution
resources for being used in the next incoming months
denoted as z^ N~;m ðx^(cid:9) N Þ. Then, the SAA upper bound can be withinthese12months.Moreover,additionalresourcescan
estimatedfrom
be provisioned by purchasing on-demand plans if the
1 X
M~ reservedresourcescannotmeettheactualdemand.Forboth
U N~;M~ ðx^(cid:9) N Þ¼ M~ z^ N~;m ðx^(cid:9) N Þ: ð49Þ case studies, the optimal solution obtained from the OCRP
m¼1 algorithm is the amount of reserved resources in different
provisioning stages (or the first stage for 2-PSP). Since the
Again, the distribution of SAA upper bound estimate
converges to a normal distribution Nð0;(cid:6)2ðx^(cid:9) ÞÞ given amountofresourcesisreservedforthenumberofVMs,this
U N optimalsolution canbeconsidered to thenumberofreserved
solution x^(cid:9) , namely
N VMs in other words.
pffi M ffi ~ ffiffiffi(cid:3) U N~;M~ ðx^(cid:9) N Þ(cid:4)z^ N ðx^(cid:9) N Þ (cid:4) ! D N (cid:3) 0;(cid:6)2 U ðx^(cid:9) N Þ (cid:4) ; as M~!1; ð50Þ 7.1 Experiment Setup
where (cid:6)2 U ðx^(cid:9) N Þ¼Var½z^ N ðx^(cid:9) N Þ(cid:7) which can be approximated 7.1.1 Setting of Cloud Computing Environment
by the sample variance estimator s2ðM~;x^(cid:9) Þ as follows: Wefirstpresenttheparametersettingofacloudcomputing
U N
environment used in this performance evaluation. The
s2 U ðM~;x^(cid:9) N Þ¼ M~ 1 (cid:4)1 X
M~
ðz^ N~;m ðx^(cid:9) N Þ(cid:4)U N~;M~ ðx^(cid:9) N ÞÞ2: ð51Þ e o n rg v a ir n o i n za m ti e o n n t )w co h n o s i i s st r s en o t f in o g n c l o y m o p n u e tin c g lo r u e d sou c r o c n e s s u o m ff e e r red (i. b e y .,
m¼1
cloud providers. The consumer has two different types of
Finally, the ð1(cid:4)(cid:3)Þ-confidence interval of the SAA upper applications representing two distinct VM classes, namely
bound can be obtained from I ¼fI 1 ;I 2 g.Forinstance,I 1 isadatabaseserverandI 2 isa
web server. Each VM class requires different amount of
" U N~;M~ ðx^(cid:9) N Þ(cid:4) z (cid:3)=2 s p U ð ffi M M ffi ~ ffi ~ ffiffi ;x^(cid:9) N Þ ;U N~;M~ ðx^(cid:9) N Þþ z (cid:3)=2 s p U ð ffi M M ffi ~ ffi ~ ffiffi ;x^(cid:9) N Þ # :ð52Þ r I e 1 so a u n r d ces I . 2 Pr a o r c e es 8 si , n 74 g 8 tim an e d un 6 it , s 57 re 0 qu C ir P e U d - b h y o a ur V s M p i e n r cl y as e s a e r s ,
respectively. Permanent storage capacities required by a
6.3 Monte Carlo Sampling VM in classes I 1 and I 2 are 1,920 and 1,200 GBs per year,
The Monte Carlo sampling technique can be applied to respectively.Networkbandwidthregardingoutbounddata-
generate scenarios (cid:2) N. Each scenario is from (cid:2) as follows. transferrequiredbyaVMinclassesI 1andI 2are24,000and
First, the random number is uniformly selected from ½0;1(cid:7). 30,000GBsperyear,respectively.Thecostofinbounddata
Then,thescenarioisderivedbytheinversetransformation transfer is assumed to be free of charge. Furthermore, a
method given the random number and cumulative prob- softwarepackageis neededto beinstalled in aVM of each
ability distribution of (cid:2). The same process is iteratively VMclass.Asoftwarepackageconsistsofoperatingsystem,
performed until the N scenarios are completely chosen. database software (for class I 1 only), web application
software (for class I 2 only), and other utility software. The
6.4 Obtaining the Optimal Solution softwarecostisadditionallychargedtotheconsumerasthe
The optimal solution based on the SAA approach can be license cost per a running VM. The license software costs
obtained when N is sufficiently large. However, we can corresponding to a VM in classes I 1 and I 2 are $500 and
select an optimal solution by solving different SAA $1,200, respectively. The consumer is assumed to purchase
problems with different size of N. Until the same solution thesesoftwarelicensesfromsoftwarevendorswhenVMsare
is found in these problems, we can choose the solution as runninginexpendingandon-demandphases.
the desired solution. The detail and result of this solution The environment consists of four cloud providers,
method is presented in the next section. namely J ¼fJ 1 ;J 2 ;J 3 ;J 4 g. J 1 represents the private cloud

CHAISIRIETAL.: OPTIMIZATIONOFRESOURCEPROVISIONINGCOSTINCLOUDCOMPUTING 173
TABLE2
|     |     |     |     | Pricing | DefinedbyEach |     | Cloud | Provider |     |     |     |
| --- | --- | --- | --- | ------- | ------------- | --- | ----- | -------- | --- | --- | --- |
andtheotherrepresentthethreepublicclouds.Theprivate phase of all resource types can be doubly increased, with
cloudJ
1isthedatacenterbelongingtothecloudconsumer. probability 0.1, from the price defined in Table 2. With
This data center has housed only 10 physical servers. Each probability 0.9, the price in the on-demand phase remains
server is assumed to offer 100 percent uptime system unchanged. For the demand uncertainty, the actual re-
24(cid:5)365¼8;760
availability, i.e., CPU-hours per year. quired number of VMs in the second provisioning stage of
Therefore, for the whole data center, J 1 can offer 87,600 VMclass(i.e.,I 1 andI 2)variesfrom1to50.Thedemandof
CPU-hoursasthemaximumprocessingcapacity.Theother one VM class is assumed to be the same as the other class.
resource typesin J isassumedtobeabundantto serveall Three distributions of demand are considered in the
1
VMs run by the consumer. The total cost to utilize the experiment, namely discrete normal distribution, uniform
serversinJ 1isonlyconsideredfromtheannualenergycost. distribution,anddistributionfromtestdata.Meansofboth
This annual cost is assumed to be the average energy cost normal and uniform distributions are set to 25.50. The
takenbyDellPowerEdgeM600bladeserveraspresentedin variance of normal distribution is set to 6, while the
[26]. The cost is calculated as 454:39=1;000 kilowatts variance of uniform distribution is 208.25. The last
(average power consumption per server5) (cid:5)$0:0897 (elec- distribution is generated from the logged data obtained
|     | watt-hour)(cid:5)24 |     |     |     | (cid:5)365 |     |     |     |     |     |     |
| --- | ------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
tric charge per (hours per day) (days from Institute of High Performance Computing (IHPC) in
per year) (cid:10)$357 per server per year. For only J 1, this cost Singapore. The data are collected from the actual usage of
($357) is considered as the reservation cost to reserve sharedcomputingresourceslocatedinthecomputercluster
|     |     |     |     |     |     |     | maintained | by IHPC. | The probability | distribution | (with |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --------------- | ------------ | ----- |
resourcesforaVM,whiletheexpendingcostofprocessing
time and storage capacity are omitted. Only the cost of mean = 21.64 and variance = 389.93) of the resource usage
networkbandwidthischargedto$0.10perGBpermonthof representing the number of required VMs is derived as
outbound data transfer. Furthermore, the on-demand plan shown in Fig. 6.
| for provisioning |              | resources | is unavailable | in       | J 1 .    |         |          |            |              |               |     |
| ---------------- | ------------ | --------- | -------------- | -------- | -------- | ------- | -------- | ---------- | ------------ | ------------- | --- |
|                  |              |           |                |          |          |         | 7.2 Case | Study: Two | Provisioning | Stage Problem |     |
| The              | public cloud | providers | (J 2,          | J 3, and | J 4) are | assumed |          |            |              |               |     |
to offer unlimited capacity of all resource types, so the 7.2.1 Cost Structure
constraintin(13)isomitted.Pricingofresourcesinprovider
First,thecoststructuretoprovisionresourcesisstudied.To
J 2 is based on the prices defined by Amazon EC2 (in ease the illustration, this study considers only single VM
February2010),andthepriceofprocessingtimeisbasedon class I and single cloud provider J 2. The number of
1
| that of | the Small | Instance | type [2]. | However, | pricing | in  |     |     |     |     |     |
| ------- | --------- | -------- | --------- | -------- | ------- | --- | --- | --- | --- | --- | --- |
requiredVMs(i.e.,demand)isvariedfollowingthenormal
J J
providers 3 and 4 is artificially and reasonably defined. distribution. In Fig. 7, given different number of reserved
Providers J 2 and J 3 offer customers both reservation and VMs, cost in the first stage called first stage cost (which is
| on-demand | plans, | while | J has only | an on-demand |     | plan. |     |     |     |     |     |
| --------- | ------ | ----- | ---------- | ------------ | --- | ----- | --- | --- | --- | --- | --- |
4 actually reservation cost), cost in the second stage called
| Providers | J and | J   | offer customers |     | three | different |                                                     |     |     |     |     |
| --------- | ----- | --- | --------------- | --- | ----- | --------- | --------------------------------------------------- | --- | --- | --- | --- |
|           | 2     | 3   |                 |     |       |           | secondstagecostincludingexpendingandon-demandcosts, |     |     |     |     |
reservation contracts, namely 3-month (3M), 6-month and total cost, are presented. As expected, the first stage
| (6M), and | 1-year | (1Y)      | contracts. | Pricing    | of resource | in       |                 |        |                    |     |            |
| --------- | ------ | --------- | ---------- | ---------- | ----------- | -------- | --------------- | ------ | ------------------ | --- | ---------- |
|           |        |           |            |            |             |          | cost increases, | as the | number of reserved | VMs | increases. |
| expending | and    | on-demand | phases     | is charged | as          | the pay- |                 |        |                    |     |            |
However,thesecondstagecostdecreasesafterthedemand
| per-use | basis based | on  | the actual | usage per | resource | unit. |     |     |     |     |     |
| ------- | ----------- | --- | ---------- | --------- | -------- | ----- | --- | --- | --- | --- | --- |
isrealized,sincethecloudconsumerneedssmallernumber
The resource unit of processing time is CPU-hour, while of VMs provisioned by on-demand plan. In this case, the
| one of storage | capacity |     | and network | bandwidth | is  | GBs per |     |     |     |     |     |
| -------------- | -------- | --- | ----------- | --------- | --- | ------- | --- | --- | --- | --- | --- |
month.Forthenetworkbandwidth,onlytheoutbounddata
transferischarged,whiletheinboundoneisfreeofcharge
provider.6
| in every          | cloud     |            | Pricing | defined | by every | cloud |     |     |     |     |     |
| ----------------- | --------- | ---------- | ------- | ------- | -------- | ----- | --- | --- | --- | --- | --- |
| provider          | is listed | in Table   | 2.      |         |          |       |     |     |     |     |     |
| 7.1.2 Uncertainty |           | Parameters |         |         |          |       |     |     |     |     |     |
Inthispart,twomainuncertaintyparametersincludingthe
priceofresourceandthedemandasthenumberofrequired
VMsperVMclass,aredefined.Thepriceintheon-demand
5.Weomitthepowerconsumptionofcoolingsystemasitisthefixed
costofprivatecloudintheorganization.
6.ThechargeofinbounddatatransferofferedbyAmazonEC2hasbeen
freethroughJune30,2010. Fig.6.Theprobabilitydistributionoftherealdata.

174 IEEETRANSACTIONSONSERVICESCOMPUTING, VOL.5, NO.2, APRIL-JUNE2012
Fig.8.Comparisonbetweentotalcostsofresourceprovisionwithand
Fig.7.Theoptimalsolutioninasimplecloudcomputingenvironment. withoutreservation.
provisioned in the first stage is presented. Also, the
optimal number of reserved VMs can be determined to be
expected second stage costs incurred due to different
30reservedVMsasshowninFig.7,whichisthepointthat
probability distributions are shown. The costs include the
thetotalcostisminimum.Clearly,eveninthissmallsetting
reservation cost (R.C.), expending cost (E.C.), on-demand
(oneVMclassandoneprovider),theoptimalsolutionisnot
cost(O.C.),oversubscribedcost(O.S.C.),andtotalcost.The
trivial to obtain due to the demand uncertainty. Therefore,
probability distributions include normal distribution
the OCRP algorithm would be required to guarantee the
(Norm), uniform distribution (Uniform), and distribution
minimum cost to the consumer.
from test data. Furthermore, three variances of the normal
Given the optimal reservation of 30 VMs as shown in
distributionareconsidered,namelyvariance=4(Normv4),
Fig. 7, the comparison between resource provisioning with
6 (Norm v6), and 8 (Norm v8).
and without reservation can be made as illustrated in
In Table 3, we observe that as the variance increases the
Fig. 8. Without reservation, the number of VMs is to
number of VMs also needs to be increased. Therefore, the
dynamically provision resources in the second stage by
number of reserved VMs in the test data is highest, while
only purchasing resources in the on-demand plan. Given
that in Norm v4 is lowest. Larger variance increases the
different demands (or realization of required number of
chance that the demand will be smaller or larger than the
VMs) from 1 to 50, the cost in resource provision with
mean. Consequently, Norm v8 incurs more total cost and
reservation becomes cheaper than that without reservation
reserves more VMs than those in Norm v4 and Norm v6.
due to the discounted price of processing time. However,
Again, the increment of number of reserved VMs can
the cost with reservation may not always be the cheapest.
ensure that the on-demand cost can be minimized.
As shown in Fig. 8, the total cost in the resource provision
without reservation is lower than the other one until the 7.2.3 Comparison with Other Provisioning Algorithms
demand is 15 in which the effective reservation begins.
Next, the comparison between provisioning algorithms is
This fact indicates that even if the solution is optimal, it
performed. The algorithms include the proposed OCRP,
cannot guarantee the best solution in all realizations of
expected-value of uncertainty provisioning (EVU), max-
observed parameters.Therefore, the effective way to tackle
imum advance reservation provisioning (MaxRes), and
the uncertainty is not to search for the best solution for
nonreservationprovisioning(NoRes)algorithms.EVUuses
every possible situation happening in the future, but to
the average values of uncertainty parameters and solves
obtain the solution which is able to minimize the tradeoff
them by a traditional deterministic program. MaxRes
between advance reservation and on-demand provision
reserves the maximum number of available VMs, while
while the uncertainty is carefully considered.
NoRes does not reserve any resources. Both MaxRes and
7.2.2 Impact of Probability Distributions NoRes also apply the traditional deterministic program for
For the next experiments, all parameters of the cloud allocating VMs to cloud providers. All algorithms with the
computing environment are applied. The deterministic defined input parameters are coded and solved by GLPK.
equivalent formulation derived in Section 4.2 is implemen- Thegivendistributionsareappliedtothepossiblescenarios
ted and solved by GLPK. of demand and price, respectively. The solution obtained
The stochastic effect of demand under different prob- from each solved algorithm yields the number of reserved
ability distributions is investigated. In Table 3, the number VMs(N.R.)andtheallocationofVMstoproviders.Then,a
of reserved VMs (indicated as label N.R. in Table 3) simulationprogramisdevelopedtoevaluatethesolutionof
TABLE3
Number ofReservedVMsand CostsGiven Different ProbabilityDistributions

CHAISIRIETAL.: OPTIMIZATIONOFRESOURCEPROVISIONINGCOSTINCLOUDCOMPUTING 175
TABLE4
Number ofReserved VMsandAverageCosts GivenDifferent Resource ProvisioningAlgorithms
each algorithm. The simulation contains 1,000iterations. In However, solving the master problem requires substantial
each iteration, the random number is uniformly selected amountoftimesincemoreBenderscutshavetobeadded.
| from ½0;1(cid:7). | Next, | the    | scenario |     | is derived | by  | the    | inverse |          |        |        |              |     |       |     |
| ----------------- | ----- | ------ | -------- | --- | ---------- | --- | ------ | ------- | -------- | ------ | ------ | ------------ | --- | ----- | --- |
|                   |       |        |          |     |            |     |        |         | 7.3 Case | Study: | Twelve | Provisioning |     | Stage |     |
| transformation    |       | method | given    |     | the random |     | number | and     |          |        |        |              |     |       |     |
Problem
| cumulative | probability |     | distributions |     | of  | the scenarios. |     | The |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | ------------- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
provisioningcostsincurredbypurchasingtheprovisioning TheSAAapproachpresentedinSection6isstudied.Inthis
plansgivenbythesolutionofeachalgorithmarerecorded. 12-PSP, only provider J and J are considered. It is
|                 |     |          |            |     |                |     |            |     |         |          |          | 2     | 3         |         |        |
| --------------- | --- | -------- | ---------- | --- | -------------- | --- | ---------- | --- | ------- | -------- | -------- | ----- | --------- | ------- | ------ |
|                 |     |          |            |     |                |     |            |     | assumed | that the | resource | price | is stable | and the | demand |
| After finishing |     | the last | iteration, |     | the simulation |     | calculates |     |         |          |          |       |           |         |        |
512
theaveragecostsaspresentedinTable4.Thecostsinclude varies within set f10;20;30;40;50g (i.e., ¼244;140;625
reservation cost (R.C.), expending cost (E.C.), on-demand scenariosforthe12stages).Forsamplingdata,foursample
|     |     |     |     |     |     |     |     |     |     |     |     |     | N   | 2f200;500;600;750g. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- |
cost (O.C.), oversubscribed cost (OS.C.), and total cost. sizes are determined, namely
InTable4,theproposedOCRPachievesthelowesttotal Then, the Monte Carlo sampling technique generates
cost, while NoRes yields the highest total cost due to the demand realizations for five batches per each size, i.e.,
| highest   | on-demand  |      | cost.  | The       | OCRP   | algorithm | reserves       |          |            |           |         |           |          |                  |            |
| --------- | ---------- | ---- | ------ | --------- | ------ | --------- | -------------- | -------- | ---------- | --------- | ------- | --------- | -------- | ---------------- | ---------- |
|           |            |      |        |           |        |           |                |          | M ¼5.      | Lower     | bound   | estimate  | of       | each sample      | size is    |
| 59 VMs    | (including |      | both   | classes   | I      | and       | I 2). Although |          |            |           |         |           |          |                  |            |
|           |            |      |        |           | 1      |           |                |          | calculated | by        | solving | five SAA  | problems | with             | respective |
| MaxRes    | reserves   | 100  | VMs    | (50       | per VM | class)    | to             | entirely |            |           |         |           |          |                  |            |
|           |            |      |        |           |        |           |                |          | batches.   | For upper | bound   | estimate, |          | the solution     | obtained   |
| avoid the | higher     | cost | in the | on-demand |        | plan,     | it still       | incurs   |            |           |         |           |          |                  |            |
|           |            |      |        |           |        |           |                |          | from each  | solved    | SAA     | problem   | is       | fixed to another | new        |
muchhighercostthanthatofOCRP.Additionally,MaxRes
|            |         |                |     |     |      |       |              |     | SAA problem |     | whose sample |     | size is | 750, i.e., N~ | ¼750. Ten |
| ---------- | ------- | -------------- | --- | --- | ---- | ----- | ------------ | --- | ----------- | --- | ------------ | --- | ------- | ------------- | --------- |
| incurs the | highest | oversubscribed |     |     | cost | since | the reserved |     |             |     |              |     |         |               |           |
resources are unnecessarily overprovisioned. EVU incurs batches of the new SAA problem are constructed and
|           |      |       |      |       |     |        |     |       | solved, | i.e., M~ | ¼10. Then, | the | solutions | obtained | from the |
| --------- | ---- | ----- | ---- | ----- | --- | ------ | --- | ----- | ------- | -------- | ---------- | --- | --------- | -------- | -------- |
| the total | cost | lower | than | those | of  | MaxRes | and | NoRes |         |          |            |     |           |          |          |
algorithms. Although the oversubscribed cost of OCRP is ten batches can be calculated as the upper bound estimate.
higher than that of EVU, the on-demand cost of the OCRP InTable5,theestimatesofSAAlowerandupperbounds
algorithm is much lower. Again, it is possible that the on- are presented. The optimal solution is found in the sample
demandcostcanincreaseduetothepriceuncertainty.Asa size of 750. From this optimal solution, advance reserva-
result, the diminution of the on-demand cost is more tionswithonlythe6-monthreservationcontractareusedin
important. The result of this experiment shows the balance onlyT andT 7.Thatis,10VMswillbereservedtoprovider
1
| between      | the    | number        | of      | provisioning |        | resources |       | to be |                |     |                     |       |         |                |     |
| ------------ | ------ | ------------- | ------- | ------------ | ------ | --------- | ----- | ----- | -------------- | --- | ------------------- | ----- | ------- | -------------- | --- |
|              |        |               |         |              |        |           |       |       | J 2 in stagesT | 1   | andT 7 eachand30    |       | VMswill | bereservedto   |     |
| acquired     | in the | first         | and     | second       | stages | in        | which | OCRP  |                |     |                     |       |         |                |     |
| can provide  | the    | most          | optimal | tradeoff.    |        |           |       |       |                |     |                     |       |         |                |     |
|              |        |               |         |              |        |           |       |       |                |     |                     | TABLE | 5       |                |     |
| 7.2.4 Bender |        | Decomposition |         |              |        |           |       |       |                |     |                     |       |         |                |     |
|              |        |               |         |              |        |           |       |       | Estimation     | of  | LowerandUpperBounds |       |         | ofProvisioning |     |
Fig. 9 shows the bound convergence obtained by solving Costsin the12 ProvisioningStageProblem
| Bender              | decomposition |             | algorithm.    |               | The       | adjustment           | of          | lower  |     |     |     |     |     |     |     |
| ------------------- | ------------- | ----------- | ------------- | ------------- | --------- | -------------------- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| and upper           | bounds        |             | is performed  |               | in        | each                 | iteration.  | At     |     |     |     |     |     |     |     |
| iteration           | (cid:2) ¼42,  | algorithm   |               | converges.The |           | optimalsolution      |             |        |     |     |     |     |     |     |     |
| obtained            | from          | the         | decomposition |               | is        | the                  | same        | as one |     |     |     |     |     |     |     |
| obtained            | by            | solving     | DEF           | without       |           | decomposition.       |             | We     |     |     |     |     |     |     |     |
| observe             | that the      | subproblems |               | can           | be solved | efficiently          |             | due    |     |     |     |     |     |     |     |
| to their            | smaller       | number      |               | of variables  |           | and parallelization. |             |        |     |     |     |     |     |     |     |
| Fig. 9. Convergence |               | of          | the upper     | and           | lower     | bounds               | by applying | the    |     |     |     |     |     |     |     |
Bendersdecomposition.

176 IEEETRANSACTIONSONSERVICESCOMPUTING, VOL.5, NO.2, APRIL-JUNE2012
provider J 3 in stages T 1 and T 7 each. We conclude that 40 with deterministic equivalent formulation directly.
reservedVMsareonlyneededinstagesT 1andT 7each.This In contrast, the approximation algorithm with
solutioncanavoidthehigheron-demandcost,sinceonly10 estimation of SAA lower and upper bounds can
more VMs could be provisioned with on-demand plan in yield tolerably solutions while the problems can be
any provisioning stages. practically solved in timely manner.
4. Limitation of stochastic programming. Stochastic pro-
7.4 Discussion
gramming does not address the method to obtain
7.4.1 Experimental Results appropriate probability distributions describing un-
certainty (i.e., distributions of scenarios (cid:2)). How-
1. Balance of costs. We observe that the cloud broker ever, this limitation can be alleviated by applying
with OCRP will minimize on-demand cost rather variance reduction techniques (e.g., importance
than the oversubscribed cost. Since resource pricing
sampling [27]) to increase the precision of the
in the on-demand plan is higher and possibly
estimates of uncertainty.
increased by cloud providers, the reservation plan
is more attractive by the cloud broker. However, 7.4.3 Future Research Direction
reserving too many VMs may not be optimal (e.g.,
Forthefuturework,scenarioreductiontechniques[28]will
as that of MaxRes from Table 4). Therefore, the
be applied to reduce the number of scenarios. In addition,
tradeoff between on-demand and oversubscribed
the optimal pricing scheme for cloud providers with
costs needs to be adjusted in which OCRP can
the consideration of competition in the market will be
optimally perform.
investigated.
2. Virtual machine outsourcing. As presented in Sec-
tion7.2,theVMoutsourcingfromaprivatecloudto
a public cloud provider (or public cloud) shows 8 CONCLUSION
interesting result. In the experiment, the private
Inthispaper,wehaveproposedanoptimalcloudresource
cloud fully utilizes its own resources. Then, extra
provisioning (OCRP) algorithm to provision resources
VMscanbespilledovertopublicclouds.Purchasing
offered by multiple cloud providers. The optimal solution
anddeployingnewhardwaretoaprivatecloudmay
obtained from OCRP is obtained by formulating and
not be an optimal solution, since the total cost of
solving stochastic integer programming with multistage
ownership(TCO)mustbeconsidered.Toreducethis
recourse. We have also applied Benders decomposition
TCO, workload outsourcing is the attractive choice
approach to divide an OCRP problem into subproblems
which is shown from our evaluation.
which can be solved parallelly. Furthermore, we have
7.4.2 Implementation Issues applied the SAA approach for solving the OCRP problem
with a large set of scenarios. The SAA approach can
1. Multiple provisioning stages planning issue. As shown effectively achieve an estimated optimal solution even the
inSection7.3,theOCRPalgorithmcanbeappliedto problem size is greatly large. The performance evaluation
multipleprovisioningstagesrepresenting long-term of the OCRP algorithm has been performed by numerical
planning. Since the optimal solution of the first studiesandsimulations.Fromtheresults,thealgorithmcan
provisioning stage depends on multiple probability
optimally adjust the tradeoff between reservation of
distributionsdescribingtheuncertaintyoccurringin
resources and allocation of on-demand resources. The
consequenttimeepochs,multiplestagesplanningis
OCRP algorithm can be used as a resource provisioning
needed. For example, the workload of some online
toolfortheemergingcloudcomputingmarketinwhichthe
souvenir shopping websites could be dramatically
tool can effectively save the total cost.
increasedinthehigh-seasonconsistingofmanytime
periods in a year (e.g., Christmas Day, Valentine’s
Day,etc.).Asaresult,thewebsitesshouldprovision ACKNOWLEDGMENTS
resources by considering multiple time epochs (i.e.,
This work was done in the Parallel and Distributed
provisioning stages) in advance, while reservation
Computing Centre (PDCC) of the School of Computer
contracts offered by cloud providers can be taken
Engineering,NanyangTechnologicalUniversity,Singapore.
into account to reduce the provisioning cost.
Thisworkwassupportedbytheprojects“UserandDomain
2. Use of decomposition method. The use of decomposi-
DrivenDataAnalytics”and“DesignandAnalysisofCloud
tion method for OCRP has to be carefully consid-
Computing for Data Value Chain: Operation Research
ered,sincetheformulationoftheOCRPalgorithmis
Approach,” granted by the A*STAR Thematic Strategic
a pure integer program which is the NP-hard
Research Programme.
problem [5]. Although the subproblems can be
solved in parallel, the master problem with the
additional Benders cuts requires considerable com- REFERENCES
putational time. The performance improvement of
[1] I. Foster, Y. Zhao, and S. Lu, “Cloud Computing and Grid
the decomposition algorithm will be considered in Computing 360-Degree Compared,” Proc. Grid Computing Envir-
the future work. onmentsWorkshop(GCE’08),2008.
3. BenefitofSAA.Sample-averageapproximationmeth- [2] AmazonEC2,http://aws.amazon.com/ec2,2012.
[3] GoGrid,http://www.gogrid.com,2012.
od can overcome the provisioning problems with a [4] Amazon EC2 Reserved Instances, http://aws.amazon.com/ec2/
large set of scenarios which are impossible to solve reserved-instances,2012.

CHAISIRIETAL.: OPTIMIZATIONOFRESOURCEPROVISIONINGCOSTINCLOUDCOMPUTING 177
[5] F.V. Louveaux, “Stochastic Integer Programming,” Handbooks in Sivadon Chaisiri received the MEng degree
fromKasetsartUniversity,Bangkok,Thailand,in
OR&MS,vol.10,pp.213-266,2003.
[6] A.J.Conejo,E.Castillo,andR.Garc´ıa-Bertrand,“LinearProgram- 2005. He is currently working toward the PhD
ming: Complicating Variables,” Decomposition Techniques in degree at Nanyang Technological University,
MathematicalProgramming,chapter3,pp.107-139,Springer, 2006. Singapore. His current research interests in-
[7] J.Linderoth,A.Shapiro,andS.Wright,“TheEmpiricalBehavior cludecloudcomputinganddistributedsystems.
HeisastudentmemberoftheIEEE.
| of Sampling |     | Methods | for Stochastic | Programming,” |     |     | Ann. Opera- |     |     |     |     |     |     |     |
| ----------- | --- | ------- | -------------- | ------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
tionalResearch,vol.142,no.1,pp.215-241,2006.
[8]
| G. Juve | and | E. Deelman, |     | “Resource | Provisioning |     | Options |     |     |     |     |     |     |     |
| ------- | --- | ----------- | --- | --------- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
forLarge-ScaleScientificWorkflows,”Proc.IEEEFourthInt’lConf.
e-Science,2008.
| [9] Z. Huang, |     | C. He, and | J. Wu,               | “On-Demand |       | Service | in Grid:    |     |     |         |     |          |         |             |
| ------------- | --- | ---------- | -------------------- | ---------- | ----- | ------- | ----------- | --- | --- | ------- | --- | -------- | ------- | ----------- |
|               |     |            |                      |            |       |         |             |     |     | Bu-Sung | Lee | received | the BSc | (Hons.) and |
| Architecture  |     | Design,    | and Implementation,” |            | Proc. | 11th    | Int’l Conf. |     |     |         |     |          |         |             |
PhDdegreesfromtheElectricalandElectronics
ParallelandDistributedSystems(ICPADS’05),2005.
| [10] |     |     |     |     |     |     |     |     |     | Department, | Loughborough |     | University | of Tech- |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | ---------- | -------- |
Y.Jie,Q.Jie,andL.Ying,“AProfile-BasedApproachtoJust-in-
Time Scalability for Cloud Applications,” Proc. IEEE Int’l Conf. nology, United Kingdom, in 1982 and 1987,
CloudComputing(CLOUD’09),2009. respectively. He is currently an associate pro-
fessorwiththeSchoolofComputerEngineering,
[11] Y.KeeandC.Kesselman,“GridResourceAbstraction,Virtualiza-
|     |     |     |     |     |     |     |     |     |     | Nanyang | Technological |     | University, | Singapore. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | ----------- | ---------- |
tion,andProvisioningforTime-TargetApplications,”Proc.IEEE
|     |     |     |     |     |     |     |     |     |     | He was | elected | the | inaugural | president of |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- | --- | --------- | ------------ |
Int’lSymp.ClusterComputingandtheGrid,2008.
|                 |      |        |        |           |           |     |           |     |     | Singapore | Research | and | Education | Networks |
| --------------- | ---- | ------ | ------ | --------- | --------- | --- | --------- | --- | --- | --------- | -------- | --- | --------- | -------- |
| [12] A. Filali, | A.S. | Hafid, | and M. | Gendreau, | “Adaptive |     | Resources |     |     |           |          |     |           |          |
ProvisioningforGridApplicationsandServices,”Proc.IEEEInt’l (SingAREN), 2003-2007, and has been an
|     |     |     |     |     |     |     |     | active member | of  | several national | standards | organizations, |     | such as a |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---------------- | --------- | -------------- | --- | --------- |
Conf.Comm.,2008.
boardmemberofAsiaPacificAdvancedNetworks(APAN)Ltd.In2010,
| [13] D. Kusic | and | N. Kandasamy, |     | “Risk-Aware | Limited |     | Lookahead |     |     |     |     |     |     |     |
| ------------- | --- | ------------- | --- | ----------- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
heheldajointappointmentasdirector,ServicePlatformLab,HPLabs
| Control | for | Dynamic | Resource | Provisioning | in  | Enterprise | Com- |     |     |     |     |     |     |     |
| ------- | --- | ------- | -------- | ------------ | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
Singapore.Hisresearchinterestsincludecomputernetworksprotocols,
putingSystems,”Proc.IEEEInt’lConf.AutonomicComputing,2006.
distributedcomputing,networkmanagement,andgrid/cloudcomputing.
[14] K. Miyashita, K. Masuda, and F. Higashitani, “Coordinating HeisamemberoftheIEEE.
| Service | Allocation | through |     | Flexible | Reservation,” | IEEE | Trans. |     |     |     |     |     |     |     |
| ------- | ---------- | ------- | --- | -------- | ------------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
ServicesComputing,vol.1,no.2,pp.117-128,Apr.-June2008.
DusitNiyatoreceivedtheBEdegreefromKing
[15] J.Chen,G.Soundararajan,andC.Amza,“AutonomicProvision-
|     |     |     |     |     |     |     |     |     |     | Mongkut’s | Institute | of Technology |     | Ladkrabang, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------------- | --- | ----------- |
ingofBackendDatabasesinDynamicContentWebServers,”Proc.
Bangkok,Thailand,in1999andthePhDdegree
IEEEInt’lConf.AutonomicComputing,2006.
inelectricalandcomputerengineeringfromthe
[16] L.Grit,D.Irwin,A.Yumerefendi,andJ.Chase,“VirtualMachine University of Manitoba, Winnipeg, Canada, in
Hosting for Networked Clusters: Building the Foundations for 2008. He is currently an assistant professor in
AutonomicOrchestration,”Proc.IEEEInt’lWorkshopVirtualization
|     |     |     |     |     |     |     |     |     |     | the Division |     | of Computer | Communications, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----------- | --------------- | --- |
TechnologyinDistributedComputing,2006.
|     |     |     |     |     |     |     |     |     |     | School | of Computer |     | Engineering, | Nanyang |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | --- | ------------ | ------- |
[17] H.N. Van, F.D. Tran, and J.-M. Menaud, “SLA-Aware Virtual TechnologicalUniversity,Singapore.Hiscurrent
Resource Management for Cloud Infrastructures,” Proc. IEEE research interests include the design, analysis,
NinthInt’lConf.ComputerandInformationTechnology,2009. andoptimizationofwirelesscommunication,smartgridsystems,green
[18] M.Cardosa, M.R.Korupolu,andA. Singh,“SharesandUtilities radiocommunications,andmobilecloudcomputing.Heisamemberof
BasedPowerConsolidationinVirtualizedServerEnvironments,”
theIEEE.
| Proc. | IFIP/IEEE | 11th Int’l | Conf. | Symp. | Integrated | Network | Manage- |     |     |     |     |     |     |     |
| ----- | --------- | ---------- | ----- | ----- | ---------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
ment(IM’09),2009.
| [19] F. Hermenier, |     | X. Lorca, |     | and J.-M.  | Menaud, | “Entropy: |          | A   |     |     |     |     |     |     |
| ------------------ | --- | --------- | --- | ---------- | ------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| Consolidation      |     | Manager   | for | Clusters,” | Proc.   | ACM       | SIGPLAN/ |     |     |     |     |     |     |     |
SIGOPSInt’lConf.VirtualExecutionEnvironments(VEE’09),2009.
| [20] N. Bobroff, |     | A. Kochut, | and | K. Beaty, | “Dynamic | Placement |     | of  |     |     |     |     |     |     |
| ---------------- | --- | ---------- | --- | --------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
VirtualMachinesforManagingSLAViolations,”Proc.IFIP/IEEE
| Int’l | Symp. | Integrated | Network | Management | (IM | ’07), pp. | 119-128, |     |     |     |     |     |     |     |
| ----- | ----- | ---------- | ------- | ---------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
May2007.
[21] P.JirutitijaroenandC.Singh,“ReliabilityConstrainedMulti-Area
AdequacyPlanningUsingStochasticProgrammingwithSample-
| Average | Approximations,” |     | IEEE | Trans. | Power | Systems, | vol. 23, |     |     |     |     |     |     |     |
| ------- | ---------------- | --- | ---- | ------ | ----- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
no.2,pp.504-513,May2008.
| [22] S. Chaisiri, |     | B.S. Lee,       | and D. | Niyato,     | “Optimal | Virtual | Machine    |     |     |     |     |     |     |     |
| ----------------- | --- | --------------- | ------ | ----------- | -------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| Placement         |     | across Multiple | Cloud  | Providers,” |          | Proc.   | IEEE Asia- |     |     |     |     |     |     |     |
PacificServicesComputingConf.(APSCC),2009.
| [23] GNU | Linear | Programming |     | Kit (GLPK), | http://www.gnu.org/ |     |     |     |     |     |     |     |     |     |
| -------- | ------ | ----------- | --- | ----------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
software/glpk,2012.
[24] W.-K.Mak,D.P.Morton,andR.K.Wood,“MonteCarloBounding
| Techniques |     | for Determining |     | Solution | Quality | in  | Stochastic |     |     |     |     |     |     |     |
| ---------- | --- | --------------- | --- | -------- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Programs,”OperationsResearchLetter,vol.24,pp.47-56,1999.
[25] M.D.McKay,R.J.Beckman,andW.J.Conover,“AComparisonof
| Three    | Methods | for Selecting |      | Values     | of Input | Variables      | in the |     |     |     |     |     |     |     |
| -------- | ------- | ------------- | ---- | ---------- | -------- | -------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| Analysis | of      | Output        | from | a Computer | Code,”   | Technometrics, |        |     |     |     |     |     |     |     |
vol.21,no.2,pp.239-245,1979.
| [26] R. Chheda, |     | D. Shookowsky, |     | S. Stefanovich, |     | and | J. Toscano, |     |     |     |     |     |     |     |
| --------------- | --- | -------------- | --- | --------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
“ProfilingEnergyUsageforEfficientConsumption,”Architecture
J.,no.18,2008.
| [27] G.B. | Dantzig    | and G.         | Infangerm, | “Large-Scale   |         | Stochastic      | Linear |     |     |     |     |     |     |     |
| --------- | ---------- | -------------- | ---------- | -------------- | ------- | --------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| Programs: | Importance |                | Sampling   | and            | Benders | Decomposition,” |        |     |     |     |     |     |     |     |
| Proc.     | IMACS      | World Congress |            | on Computation |         | and Applied     | Math., |     |     |     |     |     |     |     |
1991.
| [28] H.Heitschand |     | W. Ro¨misch,  |     | “Scenario        | ReductionAlgorithmsin |              |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------------- | --- | ---------------- | --------------------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| Stochastic        |     | Programming,” |     | J. Computational |                       | Optimization | and |     |     |     |     |     |     |     |
Applications,vol.24,pp.187-206,2003.