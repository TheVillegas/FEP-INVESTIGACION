302 IEEETRANSACTIONSONSERVICESCOMPUTING, VOL.10, NO.2, MARCH/APRIL2017
| Resource |     |     |     | Accounting |              |     |     | of Shared |        |     | IT  | Resources |     |     |     |
| -------- | --- | --- | --- | ---------- | ------------ | --- | --- | --------- | ------ | --- | --- | --------- | --- | --- | --- |
|          |     |     |     | in         | Multi-Tenant |     |     |           | Clouds |     |     |           |     |     |     |
ByungChulTak,YoungjinKwon,andBhuvanUrgaonkar,SeniorMember,IEEE
Abstract—Intoday’sITplatforms,thecapabilitytoaccuratelyaccountoverallresourceusageamongapplicationsiscrucialfor
varietyofmanagementactions(e.g.,capacityplanning,dynamicresourcereallocationand/orloadbalancing).However,inthe
environmentswheresmallnumberofsharedservicescatertoalargenumberofdistinctentities’requests,resourceaccounting
becomessignificantlychallenging.First,theoverallresourceconsumptionatthesharedserviceistheaggregateoftheresource
consumptionformultipleremoteentitieswhoseidentitiesarenotvisibletothesharedservice.Second,evenifsuchinformation
becomesavailable,commonmonitoringtools(e.g.,top,iostat)areunabletodeliveraccuratebreak-downofresourceconsumption
sincesharingoccursatsub-instancelevel(i.e.,serviceinstancesarenotexclusive).Westudyinherentchallengesofperforming
resourceaccountingofsharedresource.Wecomparetwononintrusiveapproacheshavingdifferentbalancebetweenlocalmonitoring
andcollectiveinference-(i)LRthatuseseasily-availabletoolswhichprovideaggregatemeasurementandapplyingwell-knownlinear
regressionasinference,and(ii)Rameterthatputsmoreemphasisongatheringfine-grainedper-threadinformationfromwithinthe
hypervisorandapplyinglightinferenceonthedata.EvaluationshowsthatRameterofferslessthan1%errorinaccountingwhereas
LR’serrorfluctuatesbetween5-150%.
IndexTerms—Cloudcomputing,distributedsystem,andresourcemanagement
Ç
1 INTRODUCTION
ACHIEVING operational excellence on modern IT (Infor- management scenarios. For one thing, it can be crucial for
mation Technology) platforms continues to become performancemanagement.Suboptimaloruntimelyreaction
ever more challenging. The complexity of IT platforms to the current resource sharing state may adversely impact
keeps growing with emergent paradigms such as SDN businessoperations.Forinstance,aloadimbalancetowards
(Software Defined Network). Furthermore, recent “Big oneofthereplicasinashareddatabaseVMmayimpactneg-
Data”trendsarenecessitatingincreaseofplatformscalesto ativelytheend-to-enddelayofalltheservicesthatrelyonit.
unprecedented degrees. Today’s management capabilities Manyindustrydatasupportthatrevenueishighlysensitive
struggle to keep up with the increase of such complexity toevensub-secondincreaseofdelays[5].Suchunderstand-
|           |      |              |         |     |                 |     |       | ing also | helps | administrators |     | get answers | to  | questions | that |
| --------- | ---- | ------------ | ------- | --- | --------------- | --- | ----- | -------- | ----- | -------------- | --- | ----------- | --- | --------- | ---- |
| and scale | [1], | [2]. A large | portion | of  | this complexity |     | stems |          |       |                |     |             |     |           |      |
fromthesharingandconsolidationofcomputingresources. aredifficulttoaddressotherwise.E.g.,whichapp’srequest
Increasingly, IT platforms consolidate multiple S/W appli- is triggering suddenburst of CPUsaturationsin one of the
key-valuestorageserversdeepdownintheservicepipeline?
| cations          | on a shared | set              | of hardware |            | equipment | for  | reasons    |          |         |        |            |     |                |     |         |
| ---------------- | ----------- | ---------------- | ----------- | ---------- | --------- | ---- | ---------- | -------- | ------- | ------ | ---------- | --- | -------------- | --- | ------- |
|                  |             |                  |             |            |           |      |            | To which | replica | should | I redirect |     | such workloads |     | so that |
| of cost-efficacy |             | ororganizational |             | necessity. |           | Such | consolida- |          |         |        |            |     |                |     |         |
tion and sharing occur in a wide variety of platforms such overall resource utilization stays within a safe range? Is it
as public clouds, private clouds, and even medium/small- also possible to apply resource capping so that fairness is
|            |         |     |          |                |     |         |         | maintained | for | the end | users, | and | on what | basis | can we |
| ---------- | ------- | --- | -------- | -------------- | --- | ------- | ------- | ---------- | --- | ------- | ------ | --- | ------- | ----- | ------ |
| scale data | centers | or  | clusters | in enterprises |     | or labs | running |            |     |         |        |     |         |       |        |
chargetheuserfortheresourceusageofthetargetserver?
| multiple | applications. |     | Popular | cloud-based |     | shared | services |     |     |     |     |     |     |     |     |
| -------- | ------------- | --- | ------- | ----------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
such as key-value stores (e.g., Amazon SimpleDB [3]) and Proactivelytakingactionsforresourceusageadjustment
orresourceusagepolicyenforcementrequireaccuratemeas-
| relational  | databaseservices(e.g., |        |                | SQLAzure[4])exemplify |           |         |         |          |       |             |          |               |     |          |          |
| ----------- | ---------------------- | ------ | -------------- | --------------------- | --------- | ------- | ------- | -------- | ----- | ----------- | -------- | ------------- | --- | -------- | -------- |
|             |                        |        |                |                       |           |         |         | urements | of    | them.       | However, | ascertainment |     | of       | accurate |
| this trend. | Considering            |        | a              | broader               | context,  | sharing | also    |          |       |             |          |               |     |          |          |
|             |                        |        |                |                       |           |         |         | resource | usage | information |          | (the activity |     | we refer | to as    |
| occurs      | for S/W,               | non-IT | infrastructure |                       | resources |         | such as |          |       |             |          |               |     |          |          |
coolingandpower,andevenpersonnel. resource accounting in this paper) is challenging within sys-
|     |     |     |     |     |     |     |     | tems consisting |     | of multiple |     | servers | running | heterogeneous |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------- | --- | ------- | ------- | ------------- | --- |
Clearunderstandingofhowsharinghappensforvarious
|           |     |         |             |            |     |     |          | distributed      | applications. |       | First,  | in many  | cases      | there     | are no  |
| --------- | --- | ------- | ----------- | ---------- | --- | --- | -------- | ---------------- | ------------- | ----- | ------- | -------- | ---------- | --------- | ------- |
| resources | can | provide | significant | advantages |     | in  | numerous |                  |               |       |         |          |            |           |         |
|           |     |         |             |            |     |     |          | clear indicators |               | that  | tell us | to which | remote     | component | or      |
|           |     |         |             |            |     |     |          | entity the       | resource      | usage | should  | be       | attributed | at        | a given |
(cid:1)
B.C.TakiswiththeIBMT.J.WatsonResearchCenter. time.Forinstance,atthedatabasenodeofa multi-tiere-com-
(cid:1) Y.KwoniswiththeComputerScienceDepartment,UniversityofTexasat
Austin,Austin,TX. merceapplicationthatissharedbyseveralunrelatedgroup
(cid:1) B. Urgaonkar is with the Department of CSE, The Pennsylvania State of end-users, there is no explicit information about whose
University,PA. initialrequeststriggeredforgivencurrentlyissueddatabase
Manuscriptreceived30Jan.2015;revised8June2015;accepted1July2015. queriesareunlesstheS/Wstacksateachtierismodifiedto
Dateofpublication8July2015;dateofcurrentversion7Apr.2017.
carryrequestidentifiers.Suchconditionposesdifficultiesin
| For information | on  | obtaining | reprints | of this | article, please | send | e-mail to: |     |     |     |     |     |     |     |     |
| --------------- | --- | --------- | -------- | ------- | --------------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
managingtheresourceutilizationofthedatabaseserverby
reprints@ieee.org,andreferencetheDigitalObjectIdentifierbelow.
|     |     |     |     |     |     |     |     | means | of admission |     | control | at the | user-facing | component. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | --- | ------- | ------ | ----------- | ---------- | --- |
DigitalObjectIdentifierno.10.1109/TSC.2015.2453980
1939-1374(cid:1)2015IEEE.Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttp://www.ieee.org/publications_standards/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore.  Restrictions apply.

TAKETAL.:RESOURCEACCOUNTINGOFSHAREDITRESOURCESINMULTI-TENANTCLOUDS 303
Another difficulty is that, even with such knowledge,
resourceattributionisnon-trivialduetothefollowings.Sim-
ple utilization information of processes or threads (such as
top, iostat) may be insufficient because those numbers
are the aggregate resource utilization caused by multiple
remote entities. This is due to the granularity of resource
principals being as fine as threads and even the bindings
between the remote resource consuming entities and such
resource principals could change dynamically over time.
Thisimpliesthatwe needto furtherbreakdownthe moni-
tored values using inference techniques. Other example is
the write activity of diskI/O in which OSkernel combines
multiple writes and issues them much later in time non-
deterministically.Thesechallengesareintensifiedespecially
intoday’scomplexservicearchitecturesinwhichmanyserv-
icesarebuiltontopofotherheterogeneousservicesviainter- Fig.1.Problemmodel.CE(ChargeableEntity)isdefinedtobeanyentity
orgroupofentitiesthatsendsrequestsdirectlyorindirectly.
facesuchasRESTAPIs(RepresentationalStateTransfer).
Basedonourstudy,webelievethatcurrentstate-of-the-art
needs to be improved to deliver aforementioned resource data collection and inferencing during the overall resource
accounting capabilities for improving cloud operations and accounting.Onecentralconcerninourdesignistoachieve
management.Towardthisend,wehavedesignedandimple- generality by avoiding application modification. Specifi-
mented the resource accounting technique, called Rameter. cally, we make the following key contributions. First, we
Rameter consists of two modules—(i) distributed request formulate the problem of resource accounting for shared
(message) causality tracking module running within the serversrunningdistributedapplications,andintroducethe
hypervisor, and (ii) resource usage accounting module that design of Rameter, capable of providing accurate resource
gathersthreadscheduling,spawningandI/Oactivities.Our usage information of shared services. To the best of our
distributedrequesttrackingtechniqueallowsustofirstdeter- knowledge, our design goes beyond the state-of-the-art by
minetheownershipofrequestmessagesatanyVMorserver being the accounting solution that is both: (i) implemented
nodes without the need to modify the application codes. withinprivilegedcode(VMMinourcase)withnoneedfor
Oncetheownership isdetermined,the resourceaccounting applicationmodification, and(ii) capableof accounting the
module observes fine-grained thread level events from the usage of shared services. Second, using a mix of synthetic
hypervisortofurtherbreakdowntheCPUandI/Ousages. andreal-world sharedservices,wepresentthecomparison
Compared to our Rameter, some of the existing techni- of two approaches—LR that uses easily-available system
quesrelyonmodifying(allorpartof)theOSormiddleware utilities which provide aggregate measurement data and
stacks to enrich the collected data [6], [7]. Often, they spe- applying well-known linear regression as inference, and
cialize on one specific component and implement the (ii) Rameter that puts more emphasis on gathering fine-
accounting and/or controlling functions by modifying grainedinformationfromwithinthehypervisorandapply-
source code [8], [9]. However, such instrumentation-based ing light inference on the data. Third, we demonstrate the
approaches are viable only to the organization who builds usefulness of Rameter’s resource accounting information by
theirownS/Wstacksortotherelativelysmallenvironment applyingittoonlineresourcecontrol(specificallyviathrot-
such as embedded systems. And, even with some instru- tling)usingthescenarioofenforcingtheSLArequirements
mentation, gathered monitoring data may not contain forRUBiSapplicationunderheavyworkloads.Suchcapabil-
enough information for the purpose of accurate resource ityofonlineresourcecontrolforsharedservicesisachievable
accounting. In response to such limitations, we pursue the onlywhenfine-grainedthread-levelinformationisavailable,
goal of building effective resource accounting technique whichaggregatemonitoringdatacannotprovide.
that is (i) focusing on obtaining fine-grained per-thread The rest of this paper is organized as follows. Section 2
resource usage information, (ii) generally applicable to provides some background knowledge and explains what
existing environments, (iii) accurate enough for any type makes the resource accounting problem challenging. In
of resources, including both IT and non-IT resources, and Section 3, we define our problem. In Section 4, we identify
(iv) flexible enough to accommodate a wide-range of key design requirements. Descriptions of our solution are
resource management policies. As an initial step, we focus given in Section 5, and it is followed by implementation
on IT resource such as CPU, I/O and network in a virtual- detailsinSection6.InSection7,wepresentourexperimen-
izedenvironment.Notethatourstudyisnotaboutpropos- tal evaluation. Then, we provide related work in Section 8.
ingtheadoptionofmoredetailed billinginformationtothe Finally,inSection9,wepresentconcludingremarks.
cloudusers.Weaddresstheresourcemanagementproblem
from the perspective of cloud service providers with the
2 BACKGROUNDANDCHALLENGES
goalofimprovingthecloudmanagementoperations.
We study the resource accounting problem and investi- 2.1 ProblemModel,TerminologyandScope
gatesolutionsthataddressesallchallengesidentifiedabove. WeuseFig.1thatshowsarepresentativeplatformthatwe
Towards finding the right solution we build and compare usetodriveourdiscussion.Itillustratesvariouskeyentities
twoapproachesthatdifferinwheretheyfocusmoreamong andtherelationshipsbetweenthem.Werefertoaplatform
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore. Restrictions apply.

304 IEEETRANSACTIONSONSERVICESCOMPUTING, VOL.10, NO.2, MARCH/APRIL2017
user or their application whose resource usage must be In resource management, fairness can be defined in sev-
separately tracked and accounted as a chargeable entity eral ways. They could be either strictly in terms of the
(CE). The concept of CE is not limited to subscribers of amountof resource usage, orin relation to how much user
software services. We define it in a broader sense to rec- iswillingtopayfortheservicequality.Inanycase,accurate
ognize groups of computing equipment as CEs as well. resource accounting is the basis for the enforcement of the
Fig. 1 shows several types of such CEs—Group 1, 2, User fairness.Thescopeinthisworkistobuildsupportingmech-
1, 2, and 3. However, if necessary, any other entities such anismtoenabletheenforcementofvariousfairnesspolicies.
as “Business Logic VM” or individual VMs in Group 2 Extending Rameter to enforce the fairness in terms of the
canbetreatedasseparateCEs.Weassumethevirtualized servicequalityandpaymentisourfutureplan.
environment in which CEs’ software components run
withinvirtualmachines(VM).
2.2 Real-WorldExamplesofSharedServices
Also shown in the figure are example shared services
It is not hard to find the shared services in both the public
thattheplatformofferstoitsCEs—adatabaseserviceanda
clouds(especiallyinPaaS)and/ornon-cloudenvironments
configuration management service. These shared services
that conform well to our model. Valid example should
themselveshavemultiplecomponentsthatspanacrosssev-
exhibitthebehaviorinwhichtheresourcesharingoccursat
eralVMsorphysicalservers.Internallythedatabaseservice
theinstance-level(i.e.,process).IfseparateinstanceofVMs
maintains functionally separategroupof VMs for load bal-
or processes serves different CEs, then managing the
ancing. Whereas its front-end tier communicates directly
resource usage becomes significantly easier. However,
with the chargeable entities, its back-end components are
instance-levelsharingisbecomingmorecommonbecauseit
exercisedindirectly,i.e.,viarequestsmadetothefront-end
provides better scalability and resource efficiency. Real-
tier.Thearrowfromtheconfigurationmanagementservice
world examples of shared services that conform to our
tothedatabaseservicerepresentsthefactthatservicesmay
modelarelistedbelow.
build on top of other services. Note that each CE does not
SQL Azure. The first example of a shared service is the
exclusivelyownitsdatabaseprocess.Onedatabaseinstance
Microsoft SQL Azure [4], the multi-tenant SaaS database
(inourexample,twofront-endsandthreequeryprocessing
service. In SQL Azure,tenants see onlytheir own database
VMsforoneinstance)maybesharedbyanunrelatedgroup
of tenants.1 Shared services in our model are frequently spaces, but they physically share the underlying
database server instance with other tenants [4]. Windows
foundinPlatform-as-a-Service(Paas)typecloudwherecus-
Azure also offers three different types of shared storage
tomers pay for the usage of services rather than owning
services—Blob, Table, and Queue—intended for different
exclusiveserviceinstances.
purpose. Tenants are given separate database spaces, but
Unlike for ‘Web Server VM’ or ‘Business Logic VM’
thedatabaseinstancesareshared[4].
where an accounting-capable VMM (e.g., using an exist-
Force.com. It is a (Platform-as-a-Service version of the
ing accounting solution such as resource containers [10])
Salesforce.com, which is a SaaS cloud service specializing in
could associate the VMs with appropriate CEs, existing
providinganonlineCRM(CustomerRelationshipManage-
solutions cannot be directly adapted for accounting
ment) solution. By design, Force.com adopts an architecture
within servers that belong to shared services where the
in which all the users share a single software instance and
VMM-visibleresourceprincipalsdonothaveafixedasso-
thesetofH/W.[16].Thisarchitectureischosentoincrease
ciation with any CE. Additionally, since the back-end tier
themanageability.
of the database service is only exercised by the CEs indi-
SimpleDB. An example of the shared service can also be
rectly, i.e., via work generated during processing of
found in AWS (Amazon Web Services) cloud. Amazon
requeststhataremadebyCEstothefront-end,additional
offers non-relational key-value data store service, called
thought is needed to identify what portion of its resource
SimpleDB[3].Subscribersarechargedbythemachineutili-
usage should be attributed to which CE. Consequently, a
zation, datatransfer size incurred by user requests and the
resource may be used by a CE either directly (e.g., resour-
totalstoragespaceused.Especially,SimpleDBmeasuresthe
ces on server VMs exclusively assigned for the software
owned by them) or indirectly via a shared service (e.g., CPUutilizationattheindividualrequestlevel.CPUutiliza-
resources on servers hosting the database-as-a-service, tionconsumptionisestimatedbasedontheamountofdata
within the SaaS (Software-as-a-Service) database, the size. Although system architecture is not publically avail-
sharednetwork,ortheSAN). able,itcanbeinferred thatSimpleDB adoptssomeform of
Recently a number of data center resource management resourceaccountingmechanism.
solutions (e.g., DCOS [11], [12], [13], fos [14], and Open- Bigtable. Bigtable [17] is Google’s proprietary database
Stack [15]) have emerged all of which require solutions for built with massive scalability in mind. Bigtable service
keepingtrackofandaccountingtheoverallusageofshared builds on top of two other services—Chubby [18] and GFS
resources,typicallyatthegranularityofacontainerorVM. (GoogleFileSystem)[19].Chubbyis adistributed lockser-
We view our work as highly complementary to these solu- vicemanagerthatprovidescoarse-grainedsynchronization
tionsinthatourtechniquecanbeusedinthesesolutionsfor onshared resources. BigtableusesChubbyfor maintaining
evenfinertaskgranularityaccounting. a master Bigtable server and for storing the metadata for
datalocations.GFSisusedbytheBigtabletostorelogsand
data files. Bigtable internally serves the needs of multiple
1.Theterm,tenant,istheequivalentoftheCEindatabaseterminol-
groupsinGoogle.Eachgroupisgivenisolatedtablespace,
ogy.However,ittypicallyreferstothedirectsubscribersofthedata-
baseserviceitself,notoftheentireplatformashowCEisdefined. buttheysharetheBigtableinstancesimilartoSQLAzure.
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore. Restrictions apply.

TAKETAL.:RESOURCEACCOUNTINGOFSHAREDITRESOURCESINMULTI-TENANTCLOUDS 305
| 2.3 Challenges |     |     |     |     |     |     |     |     |     |     |     | TABLE1 |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
SummaryofSymbols
2.3.1 LackofDirectIndicators
AkeydifficultyarisesduetolackofdirectindicatorsofCEs Symbol Description
| responsible | for | the currently |     | in-progress |     | resource | activities |     |     |     |                     |     |     |     |     |
| ----------- | --- | ------------- | --- | ----------- | --- | -------- | ---------- | --- | --- | --- | ------------------- | --- | --- | --- | --- |
|             |     |               |     |             |     |          |            | c   |     |     | Chargeableentity,CE |     |     |     |     |
attheservers,especiallyinsharedservices.Unlikeapplica-
|            |           |     |          |         |     |          |              | C   |     |     | TotalsetofCE |     |     |     |     |
| ---------- | --------- | --- | -------- | ------- | --- | -------- | ------------ | --- | --- | --- | ------------ | --- | --- | --- | --- |
| tion-owned | software, |     | a shared | service |     | may only | be exercised |     |     |     |              |     |     |     |     |
|            |           |     |          |         |     |          |              | s   |     |     | Server       |     |     |     |     |
by a CE indirectly, making it more difficult to ascertain this S Groupofserverscomprisingasharedservice
relationship.InFig.1,thequeryprocessingVMsofthedata- r Resourcetype(e.g.CPU,DiskI/Oand/or
baseservice(SharedService1)ismerelyinvokedindirectly NetworkI/O)
|        |             |     |                 |     |           |     |           | n          |     |     | Numberofresourcetypesweconsider |     |     |     |     |
| ------ | ----------- | --- | --------------- | --- | --------- | --- | --------- | ---------- | --- | --- | ------------------------------- | --- | --- | --- | --- |
| by the | CEs through |     | the front-ends, |     | oblivious |     | of who it | is Ur;sðtÞ |     |     |                                 |     |     |     |     |
Resourceutilizationtime-seriesoftyperats
| w o r k i n g | f or . L | ik e w i | s e fo r th | e f ro    | n t -e n ds | , t h ey a | r e o n ly a b     | le Ur | ;sðtÞ |     |               |                                          |     |     |     |
| ------------- | -------- | -------- | ----------- | --------- | ----------- | ---------- | ------------------ | ----- | ----- | --- | ------------- | ---------------------------------------- | --- | --- | --- |
|               |          |          |             |           |             |            |                    |       |       |     | R e s o u r   | c e u ti l iz ationtime-seriesoftyperats |     |     |     |
| to i d e n t  | if y w h | e th e r | t h e r eq  | u es t is | f r o m     | G r o u p  | 1 ,2 , B u sin e s | s     | c     |     |               |                                          |     |     |     |
|               |          |          |             |           |             |            |                    |       |       |     | at tr i b u t | a b le t o c                             |     |     |     |
Vr;sðtÞ
LogicVMsortheConfig.collector.But,itishardtoidentify Unaccountableresourceutilizationtime-series
further whether the requests coming from the Business oftyperats
Wr;sðtÞ
LogicVMsarefromUser1,2or3.Oneapproachforinfer- Resourceidletime-seriesoftyperats
| ring such | relationship |              | maybeto |     | instrument | the       | messaging  |     |     |     |     |     |     |     |     |
| --------- | ------------ | ------------ | ------- | --- | ---------- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| S/W to    | inject       | identifiers, | which   | is  | not        | generally | applicable |     |     |     |     |     |     |     |     |
producentime-series,oneperresourcetyperatameasure-
andmaybeprohibitive.
mentgranularityD.WedenoteasUr;sðtÞtheutilizationmea-
Howaccuratelythelocalmonitoringonservercaniden-
surementforresourceratserversduringthetthtimeslot.
tifysuchindirectusagedependsonitsaccuracyinrecogniz-
|         |            |     |           |        |      |            |         | Its | range | is 0(cid:3)Ur;sðtÞ(cid:3)1 |     | to indicate | proportions. |     | Table 1 |
| ------- | ---------- | --- | --------- | ------ | ---- | ---------- | ------- | --- | ----- | -------------------------- | --- | ----------- | ------------ | --- | ------- |
| ing the | underlying |     | causation | (i.e., | some | activities | of a CE |     |       |                            |     |             |              |     |         |
caused certain activities of a component which consumed summarizesthesymbolsandtheirmeanings.
Thegoalofresourceaccountingistoinfer,foreachCEcat
| some resources). |     | When | a CE     | is only | “one      | hop           | away” from |                                         |     |     |     |     |     |                   |     |
| ---------------- | --- | ---- | -------- | ------- | --------- | ------------- | ---------- | --------------------------------------- | --- | --- | --- | --- | --- | ----------------- | --- |
|                  |     |      |          |         |           |               |            | s,thecontributionofctotheutilization,Ur |     |     |     |     |     | ;sðtÞ.Inaddition, |     |
| the component,   |     | the  | presence |         | of direct | communication |            |                                         |     |     |     |     |     | c                 |     |
between them can yield this causation information. How- we are interested in finding out the proportion that is not
attributabletoanyc,denotedasVr;sðtÞ.Thatis,wewantto
| ever,identifyingcausation |     |     |     | becomestrickier |     | whenthecom- |     |     |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
findUr ;sðtÞandVr;sðtÞsuchthat
| ponent | is “more | than | one | hop away” | from | the | CE. Solving |     | c   |     |     |     |     |     |     |
| ------ | -------- | ---- | --- | --------- | ---- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
this problem, in general, requires some form of statistical X
inferencebasedonprobabilisticmodelstocapturethiscau- Ur ;sðtÞþVr;sðtÞ¼Ur;sðtÞ: (1)
c
| sation, | and closely |     | related | examples | can | be seen | in some |     |     |     |     |     |     |     |     |
| ------- | ----------- | --- | ------- | -------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
c2C
work[6],[20].
Wr;sðtÞ
|     |     |     |     |     |     |     |     |     | As a | corollary, | if we | let | be the | proportion | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---------- | ----- | --- | ------ | ---------- | --- |
unused(i.e.,iPdle)resourceattimetatservers,itwouldfol-
2.3.2 MismatchofResourcePrincipalsandCEs
|     |     |     |     |     |     |     |     | Plow | thPat |     | Ur ;sðtÞþVr;sðtÞþWr;sðtÞ¼1. |     |     |     | Similarly, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----- | --- | --------------------------- | --- | --- | --- | ---------- |
|     |     |     |     |     |     |     |     |      |       |     | c2C c                       |     |     |     |            |
I f ap p li c a t io n -o w n e d S /W c o m p o n e n t s a r e c o n t a in e d Ur ;sðtÞ
|            |           |           |          |          |           |             |                    |      | ti(cid:3)t(cid:3)tj | s2S | c would    | represent | the           | usage of | resource |
| ---------- | --------- | --------- | -------- | -------- | --------- | ----------- | ------------------ | ---- | ------------------- | --- | ---------- | --------- | ------------- | -------- | -------- |
| w ith in r | e s o u r | ce p r in | c ipa ls | that a r | e li k el | y t o b e e | as il y i d e n ti | -    |                     |     |            |           |               |          |          |
|            |           |           |          |          |           |             |                    |      | r                   | c   |            |           |               | S        |          |
|            |           |           |          |          |           |             |                    | type | by                  | in  | the entire | shared    | service group | during   | the      |
fiable by underlying resource management software (e.g., timeperiodoft (cid:3)t(cid:3)t
|             |         |     |          |          |     |      |            |     |     |     | i   | j.  |     |     |     |
| ----------- | ------- | --- | -------- | -------- | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| the virtual | machine |     | monitors | (VMMs)), |     | this | implies an |     |     |     |     |     |     |     |     |
existinglocalaccountingsolutionsuchasresourcecontain-
4 DESIGNPRINCIPLES
erscanbeeasilyusedbythismanagementsoftwaretoasso-
ciatetheseresourceprincipalswiththecorrespondingCE.2
|     |     |     |     |     |     |     |     | Any | accounting |     | solution | that forms | the basis | for | the deci- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | ---------- | --------- | --- | --------- |
Ontheotherhand,thesharedservice’ssoftwaredesignand sion of resource controlling actions must have two ele-
| configuration |     | may not | be  | amenable | to easy | adaption | of such |        |     |           |            |     |                 |            |     |
| ------------- | --- | ------- | --- | -------- | ------- | -------- | ------- | ------ | --- | --------- | ---------- | --- | --------------- | ---------- | --- |
|               |     |         |     |          |         |          |         | ments: |     | (i) local | monitoring | and | (ii) collective | inference. | We  |
existing solutions for local accounting. For example, the data use the phrase “local monitoring” to refer to facilities
store component in Fig. 1 multiplexes the resources within each server that record events and statistics per-
assignedtoitsinternalschedulableentities(e.g.,threads)in
|     |     |     |     |     |     |     |     | taining |     | to the | resource | usage of | (or on behalf | of) | each CE. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------ | -------- | -------- | ------------- | --- | -------- |
highly application-specific (and possibly unknown) ways E.g., in resource containers, local monitoring is carried
amongtheactivitiesitcarriesoutonbehalfofCEs,render- out by the server operating system that is modified to
ingasolutionsuchasresourcecontainersdifficulttoadapt. identifyresource allocation/schedulingevents(e.g.,when
|     |     |     |     |     |     |     |     | threads |     | are | scheduled/descheduled |     | on  | the CPU) | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --------------------- | --- | --- | -------- | --- |
3 PROBLEMDEFINITION using this information to charge their usage to appropri-
|               |     |                |     |        |     |       |        | ate | containers |     | [10]. | The phrase | “collective | inference” |     |
| ------------- | --- | -------------- | --- | ------ | --- | ----- | ------ | --- | ---------- | --- | ----- | ---------- | ----------- | ---------- | --- |
|               |     |                |     |        |     | c2C   | C      |     |            |     |       |            |             |            |     |
| Let us denote |     | the chargeable |     | entity | by  | where | is the |     |            |     |       |            |             |            |     |
referstothefunctionalityneededtocombinethepiecesof
setofallCEs,andaserverbys.Serversisoneoftheservers
informationofferedbylocalmonitoringtocreateacorrect
| in a shared | service |     | group | S for | which | we are | interested |         |     |         |                |     |                |            |     |
| ----------- | ------- | --- | ----- | ----- | ----- | ------ | ---------- | ------- | --- | ------- | -------------- | --- | -------------- | ---------- | --- |
|             |         |     |       |       |       |        |            | overall |     | picture | of accounting. |     | Since resource | containers |     |
s
in performing the resource accounting. For server we are only concerned with a single server, collective
|     |     |     |     |     |     |     |     | inference |     | is trivially |     | realized | from the | monitored | data. |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------ | --- | -------- | -------- | --------- | ----- |
2.Infact,thisistheessentialideabehinddistributedresourcecon- Distributed resource containers must address a more
tainers [21]: individual servers use resource containers for local complicated version of collective inference, and it does
accountingandthenetworkstackswithinserveroperatingsystemsare
modified to embed tokens within messages sent to/by components this by augmenting the locally monitored data within
thatuniquelyidentifytheirCEs. each server with the identity of the distributed container
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore.  Restrictions apply.

306 IEEETRANSACTIONSONSERVICESCOMPUTING, VOL.10, NO.2, MARCH/APRIL2017
| (carried | within messages |     | exchanged |     | between | container |     |     |     |     |     |     |     |     |
| -------- | --------------- | --- | --------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
components)thattheycorrespondto[21].
AsarguedinSection3,bothlocalmonitoringandcollec-
| tive inference   | need       | to be      | reconsidered |              | for servers |               | running |     |     |     |     |     |     |     |
| ---------------- | ---------- | ---------- | ------------ | ------------ | ----------- | ------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| shared services. | There      |            | exist a      | large number |             | of techniques |         |     |     |     |     |     |     |     |
| and tools        | for local  | monitoring |              | that one     | could       | choose        | from.   |     |     |     |     |     |     |     |
| These existing   | techniques |            | span         | a wide       | spectrum    |               | of the  |     |     |     |     |     |     |     |
“levelofdetail”theyofferatthecostofgenerality,applica-
tionintrusiveness,andoverheadsposed.Atoneendofthis
| spectrum | are techniques |     | that | can instrument |     | user-space |     |     |     |     |     |     |     |     |
| -------- | -------------- | --- | ---- | -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
and OS/VMM code to create a very detailed record of a Fig.2.Illustrationofsolutionconceptusinganend-to-endflowofoneof
incomingrequests.
| shared service’s |     | resource | usage | that | contains | sufficient |     |     |     |     |     |     |     |     |
| ---------------- | --- | -------- | ----- | ---- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
informationforcollectiveinference[22].Attheotherendof
|              |     |              |     |          |       |           |     | Section    | 2.3, that | real challenges  |     | in answering |     | this question     |
| ------------ | --- | ------------ | --- | -------- | ----- | --------- | --- | ---------- | --------- | ---------------- | --- | ------------ | --- | ----------------- |
| the spectrum | are | CE-oblivious |     | resource | usage | reporting |     |            |           |                  |     |              |     |                   |
|              |     |              |     |          |       |           |     | arise when | CE        | c uses resources |     | on server    | s   | indirectly, i.e., |
tools that rely on information available within the server’s whenasharedservicerunningonsconsumesresourceson
OSandVMM.E.g.,top,andiostat.
behalfofc.
AswewillempiricallyshowinSection7,collectiveinfer-
encethatreliesondataofferedbythesetoolscanhavesig-
|     |     |     |     |     |     |     |     | 5.1.1 | IdentifyingtheCausationandInterval |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------------------------------- | --- | --- | --- | --- | --- |
nificantinaccuraciesinaccounting.Furthermore,aswewill
c
find, such inference can be extremely sensitive to a variety To recognize a CE that is more than one hop away, we
of system properties and environmental conditions, an have devised a technique that could track the causal rela-
undesirable feature. Although our analysis of inference tionship between incoming and outgoing messages in a
using existing tools will be based on a specific inference component. Let us use Fig. 2 to explain its key idea. The
technique,wearguethattherootcauseoftheseinaccuracies figure illustrates an example end-to-end flow of a user
is the inadequacy of information contained in the monitor- request across distributed components. Although it shows
ing information offered by these tools, and even more the message flow of a single request across components, it
sophisticatedinferencetechniquesrelyingonsuchinforma- shouldbenotedthatmultiplerequestsarebeingprocessed
tionwouldfalter. concurrently.Startingfromthefirstrecvsystemcallbythe
Generally speaking, collective inference is a statistical Threadx,theinitialrequestoriginatedfromaCEproducesa
learning problem that must derive models that can mean- flow of causally related system call events until a reply is
ingfully tie together the data provided by local monitors, sentbacktotheCE.Betweentheserecvandsend,wecan
possibly filling in any gaps or discrepancies within these trackthesequenceofsystemcalleventsacrosscomponents
data.Theefficacyofsuchinferencecruciallydependsupon using the following rules. First, within the component, the
the resource usage phenomena collected by local monitor- causality is carried by the thread. Second, when the thread
ingelements.Existingmonitoringtoolsthatarenotapplica- sends a message to other components, the causality moves
tion-intrusivehavebeendesignedforinformationcollection to a thread in the receiving component. In order to apply
at the granularity of OS/VMM-relevant abstractions (e.g., these rules, we collect the system call events related to the
threads, TCP connections) that may not coincide with the network activities. Additionally, it records the thread IDs
needs of our accounting. Consequently we identify the fol- and socket tuple information (i.e., IP and port number of
lowingdesignprinciplethatunderliesouraccountingsolu- sender and receiver components) for each events. Thread
tion: our local monitoring must explicitly capture information ID enables us to connect the activities that belong to the
pertaining to resource usage on behalf of CEs to allow accurate same threads, and the socket tuple allows us to connect
sendandrecvpairsacrosscomponents.
accountingbyourcollectiveinference.
|     |     |     |     |     |     |     |     | However, | resource | accounting |     | requires |     | detecting more |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ---------- | --- | -------- | --- | -------------- |
5 RAMETER:RESOURCEACCOUNTING events than only those related to network activities. First,
FRAMEWORK creation of new threads must be tracked. Processing one
|     |     |     |     |     |     |     |     | request | may involve | spawning |     | of multiple |     | threads or pro- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | -------- | --- | ----------- | --- | --------------- |
Guidedbythedesignprinciplesstated inSection4regard- cessesandeachmayconsumesystemresourcesinadiffer-
ing the consequence of choosing the local monitoring tech- ent way. Component2 of Fig. 2 illustrates such example.
niqueandthecollectiveinferencealgorithms,wedevelopa
|          |            |            |     |        |          |      |      | Suppose | that   | Thread1    | spawns    | two | threads   | via fork (or |
| -------- | ---------- | ---------- | --- | ------ | -------- | ---- | ---- | ------- | ------ | ---------- | --------- | --- | --------- | ------------ |
| resource | accounting | technique, |     | called | Rameter, | that | pos- |         |        |            |           |     |           |              |
|          |            |            |     |        |          |      |      | clone)  | system | calls upon | receiving |     | a request | message.     |
sessesfollowingcharacteristics. First,oursolution doesnot Thread2 incurs multiple disk I/Os, whereas Thread3 inter-
| require modifications |     | to  | applications |     | and/or | middleware. |     |           |         |            |     |         |          |             |
| --------------------- | --- | --- | ------------ | --- | ------ | ----------- | --- | --------- | ------- | ---------- | --- | ------- | -------- | ----------- |
|                       |     |     |              |     |        |             |     | acts with | another | component. |     | In this | example, | the correct |
Second,thegranularityofdatacollectedfromthelocalmon-
|     |     |     |     |     |     |     |     | CPU consumption |     | for | processing | of  | the request | message |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | ---------- | --- | ----------- | ------- |
itoringisatthethread-level.Inthissectionwedescribethe given to the Component2 is the sum of CPU cycles con-
generalideasunderlyingRameter. sumedbyallthreethreads.Second,thereturnvalueofsys-
temcallsareneeded.Returnvaluesofsystemcallsindicate
5.1 LocalMonitoring the amount of data handled by the system call. In order to
Thekeyaspectoflocalmonitoringthatweneedtoperform determine the size of I/Os performed, we need to extract
is identifying and recording information about resource thosereturnvalues.Anotherrequirementforthecapability
principals and scheduling events of interest. Recall from of resource control is the online causality tracking within
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore.  Restrictions apply.

TAKETAL.:RESOURCEACCOUNTINGOFSHAREDITRESOURCESINMULTI-TENANTCLOUDS 307
thehypervisor.Weprovideimplementationdetailsspecific We observe the occurrences and return values of system
|     |     |     |     |     |     |     |     | recv, |     | send, | recvfrom, |     | sendto,3 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --------- | --- | -------- | --- |
to our environment in Section 6 and discuss other techni- calls such as and and
quesfordifferentenvironments. accumulate their return values to come up with network
|     |     |     |     |     |     |     | bandwidth | usage. | Note | that | this quantity | does | not | include |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ---- | ---- | ------------- | ---- | --- | ------- |
5.1.2 ThreadSchedulingEvents
|     |     |     |     |     |     |     | the bandwidth |     | consumption |     | due to | protocol-specific |     | over- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | --- | ------ | ----------------- | --- | ----- |
Thisaspectoflocalmonitoringisconcernedwithdetecting heads such as retransmissions and various header/trailer
portionsaddedacrosstheprotocolstacks.
| the exact | moment | of  | thread | context | switch | and collecting |      |                |     |     |                |     |        |         |
| --------- | ------ | --- | ------ | ------- | ------ | -------------- | ---- | -------------- | --- | --- | -------------- | --- | ------ | ------- |
|           |        |     |        |         |        |                | Disk | I/O accounting |     | is  | done similarly |     | as the | network |
informationaboutwhenthethreadbeginstousearesource
read
on behalf of which CE as well as when it stops doing so. I/O (i.e., by tracking the return values of and
The local monitoring must record such information solely writesystemcalls).However,theresourceusagewecol-
|          |      |     |            |     |             |           | lect is different |     | from | the actual | disk | bandwidth | consump- |     |
| -------- | ---- | --- | ---------- | --- | ----------- | --------- | ----------------- | --- | ---- | ---------- | ---- | --------- | -------- | --- |
| based on | what | the | hypervisor |     | can observe | about the |                   |     |      |            |      |           |          |     |
resource principals on that server, and the events corre- tion observed by the storage device. This is due to
spondingtotheirscheduling. nondeterminism introduced by the page cache and block
|       |        | s          |     |      | c       |                | I/O optimization |     | mechanisms |     | by  | the kernel. |     | If exact |
| ----- | ------ | ---------- | --- | ---- | ------- | -------------- | ---------------- | --- | ---------- | --- | --- | ----------- | --- | -------- |
| For a | server | indirectly |     | used | by a CE | (i.e., running | a                |     |            |     |     |             |     |          |
|       |        |            |     | s    |         | c),            |                  |     |            |     |     |             |     |          |
shared service component exercised by we need to accountingofphysicaldiskbandwidthisrequired,appro-
identifyCPU(de-)schedulingeventswithinthesoftwareofs priate inference technique must be employed on top of
thatcorrespondtodurationsforwhichswasusingtheCPU theaccountinginformationweprovide.
c.
| on behalf | of  | Identification |     | of any | I/O activities | initiated |     |     |     |     |     |     |     |     |
| --------- | --- | -------------- | --- | ------ | -------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
duringthesesameperiodsallowsforaccountingI/Oband- 5.3 Limitations
| width usage | by  | s on | behalf | of c. | For example, | Thread1 of |     |     |     |     |     |     |     |     |
| ----------- | --- | ---- | ------ | ----- | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
WedescribesomeofknownlimitationsofcurrentRameter.
Component2 in Fig. 2 may experience three different types First, Rameter is currently not able to account memory
ofschedulingeventsbetweenrecvandsend-VM,process
|     |     |     |     |     |     |     | usage due | to  | overhead | in  | tracking | individual |     | memory |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------- | --- | -------- | ---------- | --- | ------ |
andthread(de-)schedulingevents.Specificimplementation
|     |     |     |     |     |     |     | accesses. | Detecting | the | memory | access | by  | inducing | page |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | ------ | ------ | --- | -------- | ---- |
details we have employed to achieve these areprovided in faultsisoneoption,buthighperformanceimpactrendersit
Section6. impractical. Second, there are some gaps between reported
|     |     |     |     |     |     |     | Rameter’s | I/O | accounting | results |     | and the | actual | ‘physical’ |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------- | ------- | --- | ------- | ------ | ---------- |
5.2 CollectiveInference
|     |     |     |     |     |     |     | resource | usage | as pointed | out | in previous |     | subsection. | This |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ---------- | --- | ----------- | --- | ----------- | ---- |
Given the extensive information that our local monitoring is because some of the I/Os detected by Rameter may not
gathers, collective inference for accounting CPU, network translatetoactualphysicalI/Osduetocaching.Locksheld
anddiskI/Obandwidthessentiallyboilsdowntoaggrega- by shared resources may also cause Rameter to produce
tion of the resource usage information collected by various misleading results. Resources consumed by a thread while
local monitoring units. Depending on the type and owner- busy-waitingonlocksarecountedasresourceconsumption
shipofresources,differentmethodsshouldbeemployed. byRameterwhenthereisnoactualprogressofworkbeing
Definition. We use the term, segment, as referring to the made.Third,Rameterdoesnottrytoaccountfortheeffects
duration of time starting from the arrival of arequest mes- of interleaved workloads from multiple CEs. For example,
sage by recv until sending of another message by send CE c1 may end up issuing more disk I/O requests because
withinacomponent.Interactingcomponentsofthoserecv
theworkloadfromconcurrentlyrunningc2flushesc1’sdata
andsendarenotnecessarilythesame.
|     |     |     |     |     |     |     | from the   | internal  | cache. | However, |           | Rameter | still focuses | on       |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ------ | -------- | --------- | ------- | ------------- | -------- |
|     |     |     |     |     |     |     | faithfully | reporting | what   | has      | happened, | rather  |               | than who |
5.2.1 CPU caused it. Such analysis requires additional inferences and
itisleftasafuturework.
| Basicidea | of CPU | accountingisto |     |     | measure | thetime differ- |     |     |     |     |     |     |     |     |
| --------- | ------ | -------------- | --- | --- | ------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
encebetweenrecvandsendeventsofeachrequestmessage
(i.e.,segment),andtoaddthedifferencetothecorresponding 6 IMPLEMENTATION
CE’svariablethatholdstheaccumulatedCPUusage.Inaddi-
|     |     |     |     |     |     |     | In this section, |     | we describe |     | implementation |     | details | specific |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------- | --- | -------------- | --- | ------- | -------- |
tion,wesubtractthetimewhenthethreadwasdescheduled
|     |     |     |     |     |     |     | to our | environment. |     | Our | virtualization |     | environment | is  |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | --- | --- | -------------- | --- | ----------- | --- |
usingtheinformationaboutschedulingeventscollectedasa
|               |             |     |     |      |             |          | based on      | Xen | 3.1.4,     | 32-bit | para-virtualization. |           |            | Required |
| ------------- | ----------- | --- | --- | ---- | ----------- | -------- | ------------- | --- | ---------- | ------ | -------------------- | --------- | ---------- | -------- |
| part of local | monitoring. |     | The | time | is measured | by RDTSC |               |     |            |        |                      |           |            |          |
|               |             |     |     |      |             |          | modifications |     | are mostly | for    | enabling             | the local | monitoring |          |
instruction,whichcontainsthenumberofcyclecountssince
|     |     |     |     |     |     |     | techniques | as  | described | in Section |     | 5.1. Collective |     | inference |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | ---------- | --- | --------------- | --- | --------- |
boot.Sometimeswecanencounterasegmentofthreadexe-
isindependentofenvironmentspecificssinceitisaprocess-
| cutionthatdoes |     | notstart | withrecv. |     | These | CPUconsump- |     |     |     |     |     |     |     |     |
| -------------- | --- | -------- | --------- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
ingofdatagatheredfromthelocalmonitoringstep.Inorder
tionscanbeduetobackground(periodic)activitiesofOSor
|     |     |     |     |     |     |     | to realize | the | local monitoring |     | of  | Section | 5.1, we | need to |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------------- | --- | --- | ------- | ------- | ------- |
daemons.Thesesegmentsthatcannotbelabeledwithappro-
implementthreecapabilities—systemcallinterception,cap-
priateCEistreatedas‘unaccountable’(SeeFigs.7band13a
|     |     |     |     |     |     |     | turingof | systemcall |     | return | values,anddetection |     |     | ofsched- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | ------ | ------------------- | --- | --- | -------- |
forexample).The‘unaccountable’quantitiestellusthepossi-
ulingevents.Techniquesdescribedbelowaredependenton
blerangeoferrorsinCPUaccounting.Itisourfuturegoalto
ourplatform’sspecifications,anddifferentsetoftechniques
extendaccountingstothemandreduceerrors.
mayneedtobeimplementedtoachievesimilarcapabilities
inotherenvironment.
5.2.2 NetworkandDiskI/O
All the network related activities within the segment is 3.The read and write syscalls are used for both network and
| accounted | to the | CE  | currently | associated | with | the thread. | diskI/Os. |     |     |     |     |     |     |     |
| --------- | ------ | --- | --------- | ---------- | ---- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore.  Restrictions apply.

308 IEEETRANSACTIONSONSERVICESCOMPUTING, VOL.10, NO.2, MARCH/APRIL2017
6.1 SystemCallInterception
Forinterceptingtheentrypointofthesystemcallsinvoked
| by user    | applications |               | in guest | VMs, | we     | modify           | the Xen |     |     |     |     |     |     |     |     |
| ---------- | ------------ | ------------- | -------- | ---- | ------ | ---------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| hypervisor | in           | the following |          | way. | In our | para-virtualized |         |     |     |     |     |     |     |     |     |
Xenenvironment,systemcallsuseINT80hmechanism.To
| intercept | the system | calls, | we  | first | add an | system | call han- |     |     |     |     |     |     |     |     |
| --------- | ---------- | ------ | --- | ----- | ------ | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
dlerentryintheexceptiontable.Then,weregisterasystem
gateforinterrupt80htotheIDT(interruptdescriptortable).
WheneveraguestVMfiresasystemcall,thesoftwareinter- Fig.3.Hypervisor-basedCPUresourcecontrolmechanismbymanipula-
rupt 80 h is triggered. CPU, then, looks up the IDT and tionofVM-boundtimerinterrupts.
jumpstothesystemgateweinstalled.Withinit,theaddress
32-bitXenpara-virtualizationenvironment,wheneverstack
of the custom handler is searched from the exception table (do_
|     |     |     |     |     |     |     |     | switching | happens, | it  | traps | to the | Xen | hypervisor |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | ----- | ------ | --- | ---------- | --- |
and,finally,thecontrolcomestothecustomhandler.
|      |        |        |      |           |     |              |     | stack_switch |     | function  | in     | mm.c).     | We  | have added | here  |
| ---- | ------ | ------ | ---- | --------- | --- | ------------ | --- | ------------ | --- | --------- | ------ | ---------- | --- | ---------- | ----- |
| More | common | system | call | mechanism |     | is SYSENTER/ |     |              |     |           |        |            |     |            |       |
|      |        |        |      |           |     |              |     | the codes    | for | recording | thread | scheduling |     | events     | using |
SYSEXIT.INT80hismainlyusedinthepara-virtualization
Xen-providedTRACEmacro.
sinceSYSENTER/SYSEXITishardwiredintheprocessorto
assumethatthekernelresidesinring0,whereasinpara-vir-
tualization,theguestVM’skernelisinring1.Infull-virtual- 6.4 CPUResourceControlfromHypervisor
ization, SYSENTER mechanism is being used because the In order to demonstrate the effectiveness of Rameter in
guestkernelrunsinring0.Althoughwedidn’tneedtohan- the evaluation, we employ a hypervisor-based CPU
dle this, system call based on SYSENTER can still be inter- resource control mechanism to a reactive resource control
ceptedusingtechniquesdescribedinEther[23].
|     |     |     |     |     |     |     |     | scenario   | (see    | Section | 7.3.1).     | It takes | Rameter’s |     | resource    |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ------- | ----------- | -------- | --------- | --- | ----------- |
|     |     |     |     |     |     |     |     | accounting | results | as      | its input   | and      | performs  |     | targeted    |
|     |     |     |     |     |     |     |     | throttling | of the  | CPU     | consumption |          | caused    | by  | the CE that |
6.2 CapturingSystemCallReturnValues
|             |             |                   |            |      |           |                |           | is overusing |     | the CPU      | at        | the shared          |          | server.   | This is    |
| ----------- | ----------- | ----------------- | ---------- | ---- | --------- | -------------- | --------- | ------------ | --- | ------------ | --------- | ------------------- | -------- | --------- | ---------- |
| At the      | entry point | of                | the system |      | calls, we | have           | access to |              |     |              |           |                     |          |           |            |
|             |             |                   |            |      |           |                |           | achieved     | by  | manipulating |           | VM-bound            |          | timer     | interrupts |
| information | such        | as filedescriptor |            |      | number,   | bufferaddress, |           |              |     |              |           |                     |          |           |            |
|             |             |                   |            |      |           |                |           | from within  | the | hypervisor.  |           | It is non-intrusive |          |           | and trans- |
| buffer      | size and    | buffer            | contents.  |      | However,  | the            | return    |              |     |              |           |                     |          |           |            |
|             |             |                   |            |      |           |                |           | parent to    | the | guest VMs.   | Currently |                     | this     | technique | is lim-    |
| value is    | available   | only              | at the     | exit | point of  | the system     | call.     |              |     |              |           |                     |          |           |            |
|             |             |                   |            |      |           |                |           | ited to the  | CPU | resource     | only.     | We                  | describe | key       | principles |
Thereareseveraltechniquesforinterceptingtheexitpoint.
andimplementationdetailsinthissubsection.
OnewayistoleveragetheIREThypercallhandlerbuiltinto
Rameterlogicinthehypervisormaintainscurrentstatus
| the Xen   | hypervisor. | In  | 64-bit | Xen,  | they are      | invoked | trans- |           |     |          |             |     |     |     |            |
| --------- | ----------- | --- | ------ | ----- | ------------- | ------- | ------ | --------- | --- | -------- | ----------- | --- | --- | --- | ---------- |
|           |             |     |        |       |               |         |        | of per-CE | CPU | resource | consumption |     | of  | the | target VM. |
| parently, | whereas     | in  | 32-bit | mode, | it is enabled | only    | when   |           |     |          |             |     |     |     |            |
WhenitdetectsthatoneoftheCEstartstoexceedtheCPU
| VM86 mode |        | is set, which |      | is the       | backward | compatibility |        |             |            |       |              |     |              |     |               |
| --------- | ------ | ------------- | ---- | ------------ | -------- | ------------- | ------ | ----------- | ---------- | ----- | ------------ | --- | ------------ | --- | ------------- |
|           |        |               |      |              |          |               |        | consumption | defined    |       | by a policy, |     | it initiates | the | resource      |
| mode that | allows | real          | mode | instructions |          | to execute    | in the |             |            |       |              |     |              |     |               |
|           |        |               |      |              |          |               |        | control     | technique, | whose | principle    |     | is described |     | in Fig. 3. It |
protectedmode.For32-bitXen,weneedtomodifyonejnz
jmpin arch/i386/kernel/entry-xen.S shows an example thread scheduling sequence at a CPU
| instruction                   | to       |            |     |         |                       |     |            |         |              |     |            |        |        |         |          |
| ----------------------------- | -------- | ---------- | --- | ------- | --------------------- | --- | ---------- | ------- | ------------ | --- | ---------- | ------ | ------ | ------- | -------- |
|                               |          |            |     |         |                       |     |            | that is | assigned     | to  | the target | VM,    | where  | two     | threads, |
| to force                      | the IRET | hypercall. |     | Another | method                | is  | to use the |         |              |     |            |        |        |         |          |
|                               |          |            |     |         |                       |     |            | thread1 | and thread2, |     | alternate. | Let us | assume | Rameter | has      |
| pageprotectionmechanism.Atthe |          |            |     |         | systemcallentrypoint, |     |            |         |              |     |            |        |        |         |          |
weperformtwotasks.First,weturnoffthePAGE_PRESENT already determined that thread1 and thread2 are bound to
CE1andCE2,respectively.RameteraimstoreducetheCPU
| bit of the | page         | table | entry  | that holds | the         | use stack | page       |                |          |            |         |        |                |         |            |
| ---------- | ------------ | ----- | ------ | ---------- | ----------- | --------- | ---------- | -------------- | -------- | ---------- | ------- | ------ | -------------- | ------- | ---------- |
|            |              |       |        |            |             |           |            | usage of       | CE2,     | and, thus, | thread2 | is     | the subject    | of      | throttling |
| address.   | Second,      | we    | record | the        | address     | of kernel | stack      |                |          |            |         |        |                |         |            |
|            |              |       |        |            |             |           |            | in this case.  | Whenever |            | Rameter | in     | the hypervisor |         | detects    |
| which      | is available | in    | one    | of the     | Xen-defined |           | variables. |                |          |            |         |        |                |         |            |
|            |              |       |        |            |             |           |            | the scheduling |          | event      | of the  | VM, it | checks         | if next | thread is  |
Whenthesystemcallexits,itwillattempttowritethereturn
|     |     |     |     |     |     |     |     | thread2. | If so, | Rameter | increases | the | frequency |     | of timer |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------- | --------- | --- | --------- | --- | -------- |
valuefromEAXtotheuserstack.Thiswilltrapand,when
|     |     |     |     |     |     |     |     | interrupts | from | 100/s | to 200/s | until | next | scheduling | event |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ----- | -------- | ----- | ---- | ---------- | ----- |
theXenhypervisorgainsthecontrol,theEAXvaluecanbe
fires.SinceVM’snotionoftimeisbasedonthetimerinter-
| read from      | the       | kernel   | stack. | We have         | tested   | these       | mecha-     |             |      |             |         |          |             |          |            |
| -------------- | --------- | -------- | ------ | --------------- | -------- | ----------- | ---------- | ----------- | ---- | ----------- | ------- | -------- | ----------- | -------- | ---------- |
|                |           |          |        |                 |          |             |            | rupts from  | the  | hypervisor, |         | faster   | timer       | causes   | the next   |
| nisms and      | confirmed |          | that   | they were       | able     | to retrieve | the        |             |      |             |         |          |             |          |            |
|                |           |          |        |                 |          |             |            | scheduling  | to   | happen      | sooner. | In       | the figure, |          | thread2 is |
| return values. |           | However, | for    | the convenience |          | in the      | experi-    |             |      |             |         |          |             |          |            |
|                |           |          |        |                 |          |             |            | descheduled | only | after       | 5 ms,   | although |             | VM’s     | OS kernels |
| ment, we       | have      | inserted | custom | hypercalls      |          | to the      | exit point |             |      |             |         |          |             |          |            |
|                |           |          |        |                 |          |             |            | thinks 10   | ms   | has passed. |         | Timer    | rate is     | restored | when       |
| of the guest   | kernel    | system   |        | calls and       | directly | delivered   | the        |             |      |             |         |          |             |          |            |
thread2isdescheduled.
returnvaluestothehypervisor.
|                                 |     |     |     |     |     |     |     | VM             | scheduling | events            | are     | captured | by     | Rameter   | when        |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---------- | ----------------- | ------- | -------- | ------ | --------- | ----------- |
|                                 |     |     |     |     |     |     |     | thread context |            | switch            | occurs. | In Xen   | 3.1.4, | all       | the context |
| 6.3 DetectionofSchedulingEvents |     |     |     |     |     |     |     |                |            | do_stack_switch() |         |          |        | xen/arch/ |             |
|                                 |     |     |     |     |     |     |     | switching      | traps      | at                |         |          |        | in        |             |
There are three types of scheduling events we need to x86/x86_32/mm.c. Within that function we identify the
detect—VM scheduling, process scheduling and thread thread by observingthe kernel stack address given by esp
scheduling. Detection of VM scheduling events is trivial parameter.Ifitmatchesthestackoftargetthread,wechange
since it is done by the hypervisor. For other scheduling the timer rate by assigning new rate as this: current-
events, the scheduling object in Linux is the light weight >periodic_period=MILLISECS(1). Later when this
threadisdescheduled,weswitchbacktoMILLISECS(10)
| process, | equivalent | to  | the thread. |     | Thus, detection |     | of thread |     |     |     |     |     |     |     |     |
| -------- | ---------- | --- | ----------- | --- | --------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
scheduling event covers the process scheduling. In our torestorethenormalrate.
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore.  Restrictions apply.

TAKETAL.:RESOURCEACCOUNTINGOFSHAREDITRESOURCESINMULTI-TENANTCLOUDS 309
Fig.4.Set-upofoursyntheticsharedserviceandtheCEsexercisingit,
whereeachserverhereisaseparateVM.
|     |     |     |     |     |     |     |     | Fig. 5. Impact | of workload |     | burstiness | on the | accuracy | by Rameter |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | --- | ---------- | ------ | -------- | ---------- | --- |
The principles of resource control described here can be versus LR at S1 in our synthetic shared service, and CPU utilization.
readilyappliedtocontainerenvironmentsaswell.Monitor- WeshowerrorpercentagesforthreeCEs(C1,C2,C3)withLR,andlabel
ing and/or changing scheduling behavior in containers is their average as “LR Average.” In all cases, Rameter offers less than
1percenterror.
| generally     | easier | than    | from the | native | hypervisors. |        | Threads  |     |     |     |     |     |     |     |     |
| ------------- | ------ | ------- | -------- | ------ | ------------ | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| in containers | are    | visible | from     | the    | host         | in the | same way | it  |     |     |     |     |     |     |     |
sees any other threads. It is also straightforward to change non-existence of multi-collinearity among x, constant vari-
the scheduling quantum of targeted threads which is the ance of errors holds. As will be shown, various system
basisofourresourcecontrol.Notethattimermanipulation propertiescanviolatesuchpre-conditionsandleadtounde-
isnolongerneededforcontainersbecauseofthat. sirableresults.Wesolveitusingtheleastsquaresmethodto
|              |     |     |     |     |     |     |     | obtainthecoefficientsða |            |     | ;a ...a          | Þforeachintervalt.Since |                |      |      |
| ------------ | --- | --- | --- | --- | --- | --- | --- | ----------------------- | ---------- | --- | ---------------- | ----------------------- | -------------- | ---- | ---- |
|              |     |     |     |     |     |     |     |                         |            |     | 0 1              | n                       |                |      |      |
| 7 EVALUATION |     |     |     |     |     |     |     |                         |            |     |                  |                         |                | x    | ðtÞ  |
|              |     |     |     |     |     |     |     | each coefficient        | represents |     | the contribution |                         | of             | each | i to |
|              |     |     |     |     |     |     |     | the resource            | usage,     | we  | treated          | them                    | as proportions |      | to   |
InthissectionweevaluatetheefficacyofRameterandcom-
|                 |            |            |           |         |           |            |          | divide    | the resource | utilization |         | yðtÞ, giving | us     | the   | break- |
| --------------- | ---------- | ---------- | --------- | ------- | --------- | ---------- | -------- | --------- | ------------ | ----------- | ------- | ------------ | ------ | ----- | ------ |
| pare it against |            | a baseline | technique |         | that      | uses       | commonly |           |              |             |         |              |        |       |        |
|                 |            |            |           |         |           |            |          | down by   | each CE      | at Si       | at time | t. Since     | we     | wrote | server |
| available       | statistics | combined   |           | with    | linear    | regression |          | as an     |              |             |         |              |        |       |        |
|                 |            |            |           |         |           |            |          | codes, we | were able    | to          | measure | the exact    | amount | of    | CPU    |
| inference       | method.    | First,     | we        | explore | Rameter’s |            | accuracy |           |              |             |         |              |        |       |        |
resourcesconsumedbyeachCE,whichenabledustocalcu-
| using CEs | and | a shared | service |     | that are | based | on home- |     |     |     |     |     |     |     |     |
| --------- | --- | -------- | ------- | --- | -------- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
latetheaccuracyofLR-basedtechnique.
grownprogramsforwhichthe“groundtruth”canbefound
| with confidence. |        | Next,     | we employ    |     | Rameter | for | accounting |                                            |     |     |     |     |     |     |     |
| ---------------- | ------ | --------- | ------------ | --- | ------- | --- | ---------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|                  |        |           |              |     |         |     |            | 7.2 AccountingAccuracyforaSyntheticService |     |     |     |     |     |     |     |
| the usage        | of two | real-life | applications |     | used    | as  | shared     | serv-                                      |     |     |     |     |     |     |     |
ices—a clustered MySQL database server and an HBase 7.2.1 ExperimentalSetup
| key-value | store. | Throughout, |     | we  | compare | Rameter | against |              |     |        |                   |     |     |             |     |
| --------- | ------ | ----------- | --- | --- | ------- | ------- | ------- | ------------ | --- | ------ | ----------------- | --- | --- | ----------- | --- |
|           |        |             |     |     |         |         |         | Fig. 4 shows | the | design | and configuration |     | of  | a synthetic |     |
abaselineaccountingtechniquecalledLR(describedbelow) shared service we employ. We use a two-tiered design for
that relies upon readily available resource usage informa- the shared service with the front-end acting as a caching
tionavailableintoday’sservers.
|     |     |     |     |     |     |     |     | tier. This    | is a simple | data | store      | service | in which | the      | front- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | ---- | ---------- | ------- | -------- | -------- | ------ |
|     |     |     |     |     |     |     |     | end simulates | the         | data | processing | and     | the      | back-end | the    |
7.1 BaselineAccountingTechnique
|     |     |     |     |     |     |     |     | data storage. | The | front-end | is  | configured | to  | maintain | a   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | --- | ---------- | --- | -------- | --- |
Our baseline is based on the linear regression model. LR- cache size of 300 KB. A user request specifies the data
| based modeling |       | technique |        | is popular  |                  | in modeling |     | the     |         |           |         |        |      |              |     |
| -------------- | ----- | --------- | ------ | ----------- | ---------------- | ----------- | --- | ------- | ------- | --------- | ------- | ------ | ---- | ------------ | --- |
|                |       |           |        |             |                  |             |     | address | and the | data size | in unit | of KB. | Each | user request |     |
| resource       | usage | due       | to its | simplicity, | interpretability |             |     | and     |         |           |         |        |      |              |     |
incursCPUconsumptiontomimicthedataprocessingover-
good conformance to linearity for many cases. Gupta head.Cachemissesatthefront-tierresultinworkgenerated
etal.[24]haveappliedLRtopredictingtheCPUusageofa
attheback-end.Multipleclientssendrequeststothefront-
VMusingtheincomingnetworktrafficvolumeastheinput
endduringlong-lastingsessionsandcorrespondtooursyn-
andhavefoundthatitperformedwell.LRisalsoshownto thetic CEs. Statistics collector gathers CPU, network, and
be effective in modeling and predicting the resource diskI/OutilizationsforLR.LRequationisformedusingxi
| requirements |     | due to | virtualization |     | overhead |     | by  | Wood     |        |        |         |             |     |            |     |
| ------------ | --- | ------ | -------------- | --- | -------- | --- | --- | -------- | ------ | ------ | ------- | ----------- | --- | ---------- | --- |
|              |     |        |                |     |          |     |     | and y as | marked | in the | figure. | Separately, | Xen | hypervisor |     |
etal.[25].Powerresourceusagemodelingisanotheractive
|     |     |     |     |     |     |     |     | runs its | own local | monitoring. | The | reason | we  | use the | syn- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ----------- | --- | ------ | --- | ------- | ---- |
domain of LR’s application [26], [27]. All of the existing thetic benchmark is because, having the source code, it
applicationLRtriestomodeltheresourceusageatthegran-
allowsustoengineertheexactamountoftrueresourcecon-
ularityofVMorindividualserver.Ourkeypointofstudyis
|     |     |     |     |     |     |     |     | sumption | we want | for determining |     | the | error | of each | tech- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --------------- | --- | --- | ----- | ------- | ----- |
whether LR is still effective when modeling the resource niqueweapply.
usageofsharedservicesbyvariousCEs.
| Our LR          | model | relates      | the | resource | usage   | yðtÞ    | of Si | (e.g.   |                                        |     |     |     |     |     |     |
| --------------- | ----- | ------------ | --- | -------- | ------- | ------- | ----- | ------- | -------------------------------------- | --- | --- | --- | --- | --- | --- |
|                 |       |              |     |          |         |         |       | 7.2.2   | EffectofBurstyversusNon-BurstyWorkload |     |     |     |     |     |     |
| CPU utilization |       | time-series) |     | to the   | inbound | network |       | traffic |                                        |     |     |     |     |     |     |
x ðtÞ Fig.5compares the effect of burstiness/variance in work-
| volume | i from | each | Ci. | That is, | we  | form the | following |         |              |     |                |     |     |               |     |
| ------ | ------ | ---- | --- | -------- | --- | -------- | --------- | ------- | ------------ | --- | -------------- | --- | --- | ------------- | --- |
|        |        |      |     |          |     |          |           | load on | the accuracy | of  | CPU accounting |     | at  | S1. Different |     |
equationforeachintervalt:
|     |     |     |     |     |     |     |     | values | of the average |     | request | rate are | imposed | on  | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------------- | --- | ------- | -------- | ------- | --- | --- |
a 0 þa 1 (cid:4)x 1 ðtÞþa 2 (cid:4)x 2 ðtÞþ(cid:4)(cid:4)(cid:4)þa n (cid:4)x n ðtÞ¼yðtÞ: (2) shared service by a group of three chargeable entities C1,
|     |     |     |     |     |     |     |     | C2, C3, | (which create | different |     | CPU | utilization | levels | at  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --------- | --- | --- | ----------- | ------ | --- |
In applying this model, we assume that conditions the server S1). Eight levels of request rates are chosen for
|     |     |     |     |     |     |     | x   | y,  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
for linear regression such as linearity between and each CE ranging from 15 to 120 req/s at an increment of
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore.  Restrictions apply.

310 IEEETRANSACTIONSONSERVICESCOMPUTING, VOL.10, NO.2, MARCH/APRIL2017
15. We pick a “non-bursty” scenario where the requests relevant phenomena accurately, Rameter is robust to
are uniformly spaced in time, and a “bursty” scenario such effects, and offers high-accuracy accounting infor-
where the request inter-arrival times follow lognormal mation across a wide range of operating conditions.
| (0,1.0) distribution. |      |     | We find | that | the efficacy | of     | LR varies |                                      |     |     |     |     |     |     |     |
| --------------------- | ---- | --- | ------- | ---- | ------------ | ------ | --------- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|                       |      |     |         |      |              |        |           | 7.3 EvaluationWithReal-WorldServices |     |     |     |     |     |     |     |
| depending             | upon | the | extent  | of   | variation    | within | the       |                                      |     |     |     |     |     |     |     |
imposed workload. This is in line with results known in In this section, we report on the results of accounting the
existing work that finds non-stationarity in workloads CPU and network bandwidth usage of two real-world
useful for certain kinds of prediction and modeling [28]. applications—MySQLClusterandHBase.Theyarebothset
|              |        |          |     |             |      |        |       | up to be | shared | by multiple |     | Chargeable | Entities. |     | MySQL |
| ------------ | ------ | -------- | --- | ----------- | ---- | ------ | ----- | -------- | ------ | ----------- | --- | ---------- | --------- | --- | ----- |
| Intuitively, | better | accuracy |     | is achieved | with | bursty | work- |          |        |             |     |            |           |     |       |
loads because the higher variety/dynamism in the input Cluster represents the class of relational database services,
data supplies more information to LR; we expect this and the HBase the class of key-value store services, both
|               |     |          |     |                 |     |           |       | commonly | found | in  | modern | cloud | services. | We compare |     |
| ------------- | --- | -------- | --- | --------------- | --- | --------- | ----- | -------- | ----- | --- | ------ | ----- | --------- | ---------- | --- |
| basic insight |     | to apply | to  | any statistical |     | inference | tech- |          |       |     |        |       |           |            |     |
nique for accounting. For a less bursty workload, a large theresourceaccountingcapabilitiesofLRwithourRameter
part of the input data may be redundant and not offer techniqueandpresentthecasewhereLRmakesanincorrect
conclusionwhereasRameterremainsrobust.Ingeneral,we
| new information |     | to  | an inference |     | technique. | On  | the other |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | ------------ | --- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
hand,byvirtue ofitsdirectmeasurementof relevant phe- cannotexpecttodetermineareal-worldapplication’sactual
nomena, Rameter is able to achieve accurate accounting resource usage on behalf of different chargeable entities
thatisrobusttochangesinsuchworkloadconditions. without resorting to extensive application and OS instru-
|     |     |     |     |     |     |     |     | mentation. | Consequently, |     | unlike | for | our synthetic |     | shared |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | ------ | --- | ------------- | --- | ------ |
7.2.3 EffectofOtherFactors service, we cannot obtain/present a direct comparison of
|     |     |     |     |     |     |     |     | the efficacy | of  | our techniques, |     | i.e., distance |     | of the account- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------------- | --- | -------------- | --- | --------------- | --- |
Wehavealsostudiedtheeffectofcachingandbufferingas
|     |     |     |     |     |     |     |     | ing information |     | offered | by Rameter |     | versus | that offered | by  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------- | ---------- | --- | ------ | ------------ | --- |
wellasvaryingnumberofchargeableentities.Wefindthat
LRfromthe“groundtruth.”Thereforethefocusofthissec-
cachingandbuffering—bothvaluableandprevalentperfor-
|       |             |     |                   |     |     |              |     | tion is | not on       | the accuracy | of        | the accounting |             | results | from |
| ----- | ----------- | --- | ----------------- | --- | --- | ------------ | --- | ------- | ------------ | ------------ | --------- | -------------- | ----------- | ------- | ---- |
| mance | enhancement |     | techniques—affect |     |     | the accuracy | of  |         |              |              |           |                |             |         |      |
|       |             |     |                   |     |     |              |     | both LR | and Rameter. |              | In actual | systems        | management, |         | this |
accountingofatechniquelikeLR.Asiswell-knowningen- rank order can be more important than the accuracy of
eral,acachewithinorinfrontofaservicecandestroy/dis-
|     |     |     |     |     |     |     |     | resource | accounting |     | since management |     | algorithms |     | often |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | ---------------- | --- | ---------- | --- | ----- |
tortcorrelationsbetweenitsincomingrequest/trafficevents
|     |     |     |     |     |     |     |     | need to | pick the | victim | to enforce | actions | to. | If a resource |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------ | ---------- | ------- | --- | ------------- | --- |
andtheworkloadimposedonitsunderlyingserverincom-
|     |     |     |     |     |     |     |     | accounting | technique |     | tells you | the | resource | consumption |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | --------- | --- | -------- | ----------- | --- |
plexways.Bufferingofrequests/trafficcanalsohaveasim-
|     |     |     |     |     |     |     |     | quantity | with | certain | level of | error | (although | it  | may be |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ------- | -------- | ----- | --------- | --- | ------ |
ilareffectbymodifyingthetimelagbetweenanevent(e.g.,
unknown),itcanbelessproblematicthanthecaseinwhich
theissuanceofarequest)anditscause(e.g.,theactualser-
|     |     |     |     |     |     |     |     | it picks | the wrong | entity | as  | the largest | consumer |     | of the |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ------ | --- | ----------- | -------- | --- | ------ |
vicing) in complicated ways. We have carried out experi- resource.Wedemonstrateinthissectionthatsuchcasesdo
| ments where |     | we vary | several | factors | affecting |     | the degree |             |     |         |       |         |         |     |         |
| ----------- | --- | ------- | ------- | ------- | --------- | --- | ---------- | ----------- | --- | ------- | ----- | ------- | ------- | --- | ------- |
|             |     |         |         |         |           |     |            | exist under | LR  | in both | MySQL | Cluster | setting |     | and the |
andnatureofcachingwithinthefront-tierofoursharedser-
|             |      |             |                |        |              |               |     | HBase setting. |          | We also | show         | that Rameter |              | does not | suffer |
| ----------- | ---- | ----------- | -------------- | ------ | ------------ | ------------- | --- | -------------- | -------- | ------- | ------------ | ------------ | ------------ | -------- | ------ |
| vice (see   | Fig. | 4): request | size           | (fixed | or varying), | read/write    |     |                |          |         |              |              |              |          |        |
|             |      |             |                |        |              |               |     | from such      | problem. |         | In MySQL     | Cluster      | experiments, |          | we     |
| ratio (from | 10:1 | to          | 1:1), temporal |        | locality     | (non-existent | to  |                |          |         |              |              |              |          |        |
|             |      |             |                |        |              |               |     | mainly         | focus    | on the  | CPU resource |              | accounting.  | We       | show   |
veryhigh),andtheextentofcommon/overlappingcontent
resultsfortheaccountingofthemostbottleneckedresource
| requested | by      | the chargeable |     | entities. | Although   | graphs | are     |         |        |          |       |         |       |            |     |
| --------- | ------- | -------------- | --- | --------- | ---------- | ------ | ------- | ------- | ------ | -------- | ----- | ------- | ----- | ---------- | --- |
|           |         |                |     |           |            |        |         | for the | shared | service, | which | we find | to be | CPU cycles | for |
| omitted   | for the | interest       | of  | space,    | we observe | that   | caching |         |        |          |       |         |       |            |     |
MySQLandnetworkbandwidthforHBase.Oneinteresting
factorsdescribedabovealsohavevariousdegreeofimpacts
|                 |     |             |     |           |             |     |          | power    | of Rameter       | is  | the capability | to  | control       | the resource |        |
| --------------- | --- | ----------- | --- | --------- | ----------- | --- | -------- | -------- | ---------------- | --- | -------------- | --- | ------------- | ------------ | ------ |
| to the accuracy |     | LR results. |     | The error | of LR-based |     | resource |          |                  |     |                |     |               |              |        |
|                 |     |             |     |           |             |     |          | usage at | the thread-level |     | in real-time,  |     | transparently |              | to the |
accountingrangedfrom10to60percentwithhighvariance guest VMs. We demonstrate our early implementation of
| whereas | Rameter | exhibited |     | less than | 1 percent | error | for all |     |     |     |     |     |     |     |     |
| ------- | ------- | --------- | --- | --------- | --------- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
thisfunctionalitybyshowinghowitcanbeusedinsystems
cases.Accuracygainsfromtheburstinessoftheworkloads
|               |     |           |             |     |         |           |      | management |     | tasks. In      | HBase | experiments, |     | we put     | more |
| ------------- | --- | --------- | ----------- | --- | ------- | --------- | ---- | ---------- | --- | -------------- | ----- | ------------ | --- | ---------- | ---- |
| can be easily |     | offset if | application |     | happens | to employ | some |            |     |                |       |              |     |            |      |
|               |     |           |             |     |         |           |      | emphasis   | on  | the accounting |       | of network   | I/O | bandwidth. |      |
formofcachingstructureinternally.
|     |     |     |     |     |     |     |     | Also, in   | order    | to provide | the        | proof of | Rameter’s | capability |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ---------- | ---------- | -------- | --------- | ---------- | --- |
|     |     |     |     |     |     |     |     | to perform | resource |            | accounting | at       | any node  | within     | the |
7.2.4 SummaryofKeyFindings shared service infrastructure, we present the accounting
resultsofnon-front-endnodeofHBasesettings.
| To summarize, |         | we find | that | the efficacy |     | of LR relies | upon      |     |     |     |     |     |     |     |     |
| ------------- | ------- | ------- | ---- | ------------ | --- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| both the      | quality | of      | data | it gathers   | as  | well as      | the pres- |     |     |     |     |     |     |     |     |
ence/extent of correlation between its inputs and out- 7.3.1 ClusteredMySQLastheSharedService
puts. Even when accurate data can be obtained (as with Experimental setup. Fig. 6 shows the set-up of our MySQL
our implementation of LR), several factors including (i) clusterthatisusedasasharedservicebythreeCEs.Twoof
inherent workload properties (e.g., variance, temporal theseCEsusetheTPC-Wbenchmark[29]togeneratework-
locality, intensity), (ii) system mechanisms and algo- load for the database, while the third CE uses RUBiS [30].
rithms (e.g., caching or buffering), and (iii) environmental The cluster consists of a front-end SQL node that interacts
conditions (e.g., degree of resource interference from with the CEs, three data nodes, and a management node;
other S/W) might affect such correlation and affect the each node is hosted within its dedicated server. One inter-
accuracy of the accounting technique. We find empirical esting aspect of the cluster’s operation is that even in the
evidence that, owing to its ability to directly measure absence of any workload imposed by the CEs, a large
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore.  Restrictions apply.

TAKETAL.:RESOURCEACCOUNTINGOFSHAREDITRESOURCESINMULTI-TENANTCLOUDS 311
Fig.6.SharedMySQLclustersetting.ThreeCEslabeledC1,C2,andC3
sharethisdatabaseservice.
numberofsmallmessagesareexchangedbetweenallpairs
| of nodes                       | within | the | cluster | for liveness |        | check. | The CEs  |     |     |     |     |     |     |     |     |
| ------------------------------ | ------ | --- | ------- | ------------ | ------ | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| house separate/non-overlapping |        |     |         | data         | within | the    | database |     |     |     |     |     |     |     |     |
whichisspreadacrossthethreedatanodes,andthecluster
hasareplicationdegreeof1.
| Experiment |     | design and | key        | findings. | Given        | exact | accuracy |     |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | ---------- | --------- | ------------ | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| numbers    | are | elusive,   | we compare |           | the efficacy | of    | Rameter  |     |     |     |     |     |     |     |     |
andLRinthefollowingonlineresourcecontrolsituation:we Fig. 7.ComparisonofCPU accounting results.CPU usageofMySQL
ClusterSQLnodeisbeingaccounted.Bycomparingtheareasofequiv-
| wish to | ensurethat | when | the | aggregateworkloadimposed |     |     |     |     |     |     |     |     |     |     |     |
| ------- | ---------- | ---- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
alentcolorweseetherankorderdeterminedbyeachtechniqueaswell
upontheMySQLclustercausesitsserverCPUstosaturate,
asaccuracies.
| we identify |     | the contribution |     | of  | various | CEs | to this |     |     |     |     |     |     |     |     |
| ----------- | --- | ---------------- | --- | --- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
“overload,”andthenenforcetargetedCPUthrottlingonlyto LRandRameteratoneoftheMySQLservers,SN,andhow
theCEcausingtheoverload.WeimplementaCPUthrottling itevolvesduringphases1-3(resultsforCPUaccountingof
mechanismwithintheXenhypervisorsoftheMySQLcluster othernodesarequalitativelysimilarandwedonotpresent
serverswhichmanipulatestherateatwhichtimerinterrupts themintheinterestofspace).
aredeliveredtotheguestVMonlywhenthethreadserving Figs.7a,7bshowCPUaccountingfortheSQLnode(SN)
theCEcausingtheoverloadistobescheduled. as carried out by LR and Rameter, respectively. We use a
We configure CEs to impose a dynamically changing “stacked” representation, where the area under the curve
workload (consisting of three phases) on MySQL as correspondingtoaCErepresentstheCPUusagechargedto
described in Table 2. In phase 1, all CEs generate a low- it. During phase 1, both LR and Rameter produce correct
intensity workload, whose aggregate does not saturate the rank orders of CEs, although LR slightly overestimates the
MySQL servers. During phase 2, starting at t = 400 s, C2 CPU consumption for C2. However, during phase 2, LR
starts to issue CPU-intensiverequests. Weareinterested in starts to report incorrect rank order: it determines C3 to be
observinghowLRandRameterhandlethissuddenchange the cause of the increased CPU usage. Upon investigating
of behavior. Finally, in phase 3, starting at t = 600 s, C2 the reason for this mistake by LR, we find the following.
issuescontinuallyincreasingworkloadsthatcausetheCPU WhileC2issuesCPU-heavyrequestsandwaitsforMySQL’s
to saturate. Here we are interested in observing how our response, the CPU utilization stays at high level. During
simple resource throttling performs based on the account- this, C3 continues to issue requests at a relatively high rate
inginformationofferedbyLRandRameter. that are not CPU-heavy. However, the higher rate of
Since we do not have precise knowledge (i.e., ground requests coming from C3 causes LR to infer spurious posi-
truth) about true resource consumption, we engineer the tivecorrelationbetweenC3’srequestsandSN’sCPUusage.
workloads so that the CPU consumption imposed by the Infact,LRisunabletocorrectthisthroughoutphase2.
CEsissignificantlydifferentfromeachother,allowingusto As we show in Fig. 7b, besides correctly identifying the
rank their contributions without ambiguity. For example, correct rank order in its accounting, Rameter also reports
we make the CPU consumption of C2 much larger than whatportionoftheCPUusageofSN’sserveritfindsunac-
othersstartingatt=400ssothatotherCEscannotbemis- countable. This amount indicates that Rameter’s algorithm
taken as heavy CPU consumers. We begin by taking an in- was unable to charge the given thread’s resource usage to
depth look at the CPU accounting information offered by any of the chargeable entities because no direct association
|     |     |     |     |     |     |     |     | was found. | This | can happened |     | if some | thread | is spawned |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ------------ | --- | ------- | ------ | ---------- | --- |
TABLE2 independently of input requests from the chargeable enti-
WorkloadPlaybackScenario ties and performs maintenance jobs. Or, it could be due to
thenatureofthethreadthatiscreatedtoserviceotherrun-
| Phase | TimeWindow |     |     | Workload |     |     | TopUser |               |     |           |         |     |          |               |     |
| ----- | ---------- | --- | --- | -------- | --- | --- | ------- | ------------- | --- | --------- | ------- | --- | -------- | ------------- | --- |
|       |            |     |     |          |     |     |         | ning threads. | In  | any case, | Rameter |     | provides | this resource |     |
Phase1 0-400s All3CEsgenerate C2 usagetotheuseranditisuptotheusertodivideupamong
lightloads chargeableentities. Themostreasonabledivisionwouldbe
Phase2 400-600s C2startstoissue C2 to divide the ‘unaccountable’ portion according to the pro-
CPU-heavyrequests
|     |     |     |     |              |     |     |     | portion         | of resource | usage | by each | chargeable |     | entity | within |
| --- | --- | --- | --- | ------------ | --- | --- | --- | --------------- | ----------- | ----- | ------- | ---------- | --- | ------ | ------ |
|     |     |     |     | C2’sworkload |     |     |     | thattimewindow. |             |       |         |            |     |        |        |
overwhelms Fig. 9 quantifies the accuracy of accounting results of
| Phase3 | 600-1,200s |     |     | CPU,loadincreases |     |     | C2  |     |     |     |     |     |     |     |     |
| ------ | ---------- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.7.Inordertogetthegroundtruth,weperformseparate
every100s
|     |     |     |     |     |     |     |     | individual | runs | and | use the | CPU | measurements |     | as  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | --- | ------- | --- | ------------ | --- | --- |
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore.  Restrictions apply.

312 IEEETRANSACTIONSONSERVICESCOMPUTING, VOL.10, NO.2, MARCH/APRIL2017
Fig.10.Set-upofHBaseasasharedservice.WehavetwoCEslabels
Fig.8.ResponsetimedevelopmentofRUBiSfortwocases—throttledby
asYCSB1andYCSB2runningYCSBworkloadgenerator.
LR,andcontrolledbyRameter.LRincorrectlypicksC3 asaculpritfor
performancedegradation.ThrottlingtherequestrateofC3hasnoeffect. servers”andtheHBase“master”thatmanagestheseregion
However,RameterisabletopreventSLAviolation. servers.Theregionserversactasin-memorycachesforthe
contents of the data nodes. HBase stores its data in a
estimationsoftrueconsumption(labeledas‘separateruns’). Hadoopcluster,andthisisagreatexampleofasharedser-
Comparing the SUM columns, we observe that combined vice(HBase)relyinguponanothersharedservice(Hadoop)
workloadgenerateslessCPUconsumptionthanthesumof to cater to the needs of CEs using it. Due to space con-
individual runs in our application. Therefore, we use the straints, we only discuss accounting of HBase servers. A
percentage of totals as the basis for comparison. Fig. 9b regionserveremploysanHDFSclienttocommunicatewith
showstheaveragedifferenceofthepercentageoftotalsfor the Hadoop cluster that stores data persistently. HBase
Rameter and LR when compared to the ‘Separate Runs’. employsZookeeperforcoordinatingdistributedoperations
Rameter consistently differs by 4.3 5.3 percent whereas LR andlocatingregionservers.WeconfigureourHBasewitha
deviates by larger amount as workload intensifies from single region server. HBase operation involves significant
phase1tophase3. data transfer from the data nodes to the region server,
Duringphase3,startingatt¼600s,C2 startstosaturate whereastheCPUloadimposedbymostrequestsissmallas
the CPU by drastically increasing the workload it imposes most requests are for simple data retrieval or inversions.
as described in Table 2. As portions of Figs. 7a and 7b for Sincethenetworkbandwidthavailabletotheregionserver
thisphaseshow,LRcontinuestoperformincorrectaccount- becomes the bottleneck resource well before the CPU, we
ing.ThishasadetrimentaleffectonourCPUpolicingbased highlight accounting results for network bandwidth. Our
resource control. Fig. 8 shows the change of response time HBase caters to requests from two CEs derived from the
for C3 whose RUBiS application is accessing the shared YCSBworkloadgenerator[31](CAandCB).
MySQLClusterservice.Startingfromtime600,theresponse Experimentdesignandkeyfindings.Fig.10istheconfigura-
time increases. We have set the response time of 300ms as tionofourHBaseinstallationusedinthisexperiments.We
the initial warning level and 600 ms as the SLA violation run an experiment lasting 500 seconds, during which the
level. The CPU saturation caused by C2 continues to loadsofferedbyCAandCBarevariedasfollows:(i)duringt
degradetheresponsetimeofRUBiSandeventuallyitviola- = 0 to t = 100 s, both CA and CB generates identical work-
tes the SLA. Since LR determines that C3, not C2, is the loads which contains 5 percent update requests, (ii) at t =
source of overload (see Fig. 7a), C2 is not marked for any 100s,CB changestoaread-intensivemodewithgoodtem-
counter actions. However, Rameter is able to identify true poral locality, which incurs high hits in the region server
cause of the overload and, starting at time 730, it initiates causing its CPU usage to increase proportionally with the
the CPU throttling for C2. Fig. 8 indicates that the moving networktrafficsenttoCB,(iii)att=200s,CA startstoissue
average of response time under the control of Rameter is CPU-intensiveinsert-typerequeststhatcausetheCPUusage
abletocontaintheresponsetimebelowtheSLAlimit.This at the region server to increase. Fig. 11 shows the network
demonstratesonepromisingcapabilityof Rameter(i.e.,the trafficsizeinboundtotheregionserverfromthetwoCEs.
thread-levelmonitoringtechnique)incriticalresourceman- Fig. 12a and 12b shows the result of accounting the net-
agementsofsuchsharedresources. workbandwidthbyLRandRameterattheregionserverof
HBase.TheinputstotheLRaretwotimeseriesofinbound
7.3.2 HBaseastheSharedService network traffic from two chargeable entities as shown in
Experimental setup. Our second real-world shared service is Fig.11.WehaveconfiguredLRtouse100second-longdata
HBase, akey-value storage systemoffering an open-source asaninputlengthinthisHBase’sresourceaccounting,pro-
implementation of Google’s Bigtable, that has significantly ducingnoaccountingresultsforthefirst100secondsofthe
different resource usage characteristics from a database
such as MySQL. An HBase cluster consists of “region
Fig.11.Evolutionofincomingnetworktraffictotheregionserverfrom
twoCEs.BothCAandCBsendssimilarrequeststoHBaseduringt=0
tot=100sconsumingequalnetworkbandwidth.CAchangesitsbehav-
Fig.9.Comparisonofaccountingaccuracy. ioratt=100s,andCBchangesitsbehavioratt=200s.
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore. Restrictions apply.

TAKETAL.:RESOURCEACCOUNTINGOFSHAREDITRESOURCESINMULTI-TENANTCLOUDS 313
TABLE3
OverheadofSystemcallInterceptionandInformationRecording
System TypicalAvg Systemcall Systemcall
callname Turn-aroundtime Interception Intcpt&Record
read 72.0microsec .38% .59%
recv 39.6microsec .71% 1.07%
write 26.4microsec 1.07% 1.60%
send 134.3microsec .21% .31%
open 41.9microsec .67% 1.01%
accept 14.6microsec 1.93% 2.89%
connect 148.0microsec 0.19% 0.29%
pread 54.0microsec 0.52% 0.78%
(orange color). It includes CPU cycles consumed for com-
municatingwiththeZookeeper,HBasemasterandHadoop
Fig.12.ComparisonofaccountingresultsbetweenLRandRameteron Namenodes.Especially,wehavenoticedtwohighpeaksat
theout-boundnetworktrafficfromdatanodetotheregionserver. around80and470sec.Bystudyingthe HBasedocumenta-
tions, we have concluded that these would most likely be
run. The accounting results from Rameter are presented in duetotheI/Ocompactionattheregionserver.
Fig.12b.Inbothofthestackedgraphs,theupperareacorre-
sponds to the portion of network bandwidth used by CB 7.4 Overhead
and the lower one, the portion used by CA. The network
TheoverheadofRameterexistsatboththelocalmonitoring
bandwidth usage of CA drops at t = 200, thus making CB
andthecollectiveinferencesteps.Duringthelocalmonitor-
the heavierconsumer ofnetwork bandwidth.LRcontinues
ing step, the control of the intercepted system call is deliv-
to report CA as the dominant consumer of network band-
ered to the hypervisor and several information including
width. In contrast, Rameter correctly reflects this resource
system call parameters, time stamps and thread identifiers
usagebyCEs.(SeeFig.12baftert=200s).Themisjudgment
are recorded. Since these tasks must be completed before
by LR can be explained in terms of caching effects. After
returning the control back to the system call handler of
t = 200, the traffic from CB to the region server doubles by
VM’sguestkernel,thedelayheredirectlyaffectstheperfor-
theendoftherun(SeeFig.11)whereasthetrafficfromdata
mance. Therefore, our overhead measurement closely
nodesincreasesbyonly20percent.Webelievethisisdueto
focusesonthisaspect.However,weconsidertheoverhead
cachingwithintheregionserverandHBasedocumentation
ofcollectiveinferencetobenegligible.Fortheofflinemode,
supportsthisconjecture.
theoverheadofinferenceisoutofthecriticalpathsinceitis
We also present some of the selected accounting results
performed at separate server node. For the online mode
using Rameter. Fig. 13a shows the CPU accounting at the
needed by the resource control, the hypervisor manages
region server for CA and CB. According to our preplanned
small number of variables corresponding to the CEs and
workloadscenario,CB shouldconsumemoreCPUthanCA
carries out simple arithmetic. Thus, we present the over-
after time 200 sec. The accounting result indicates this
headofthelocalmonitoringstepbelow.
behavior. Notice the significant portion of unaccountable
In order to better explain the overhead of Rameter’s
CPU usage at the bottom region of the stacked graph
local monitoring step, we provide our measurement data
in Table 3. It shows the performance impact of two core
mechanisms to various system calls. The first mechanism
is the system call interception alone within the hypervi-
sor. The second mechanism is the system call interception
and data recording (via TRACE_xD macro of xen). We
first measured pure time overhead of these two opera-
tions per individual system calls through repeated meas-
urements of a dummy system call that had empty logic
inside the function. System call interception alone turns
out to add 282 nanosec of overhead to each system call.
When data recording step is combined, total of 422 nano-
sec is incurred per each system call. The second column
of Table 3 provides our measurements of typical system
call turn-around times. Compared to those turn-around
times, the overhead of system call interception and data
recording is only about 1-2 percent and the worst case is
Fig. 13. Results by Rameter at various nodes of HBase. (b) shows less than 3 percent. Therefore, the data gathering during
Rameter’scapabilitytoaccountresourceatmultiplehopsawayfromthe
the local monitoring step incurs small overhead to the
front-endofthesharedservice.NotethatdatanodeofHBasedoesnot
haveadirectcontactwithCEs. runningapplicationswithintheguestVM.
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore. Restrictions apply.

314 IEEETRANSACTIONSONSERVICESCOMPUTING, VOL.10, NO.2, MARCH/APRIL2017
8 RELATEDWORK logs as well as network usage of distributed applications.
|         |       |          |        |      |           |     |          | Rameter | can | be benefit | from | such | monitoring | tools | by  |
| ------- | ----- | -------- | ------ | ---- | --------- | --- | -------- | ------- | --- | ---------- | ---- | ---- | ---------- | ----- | --- |
| Earlier | works | by Banga | et al. | have | addressed | the | issue of |         |     |            |      |      |            |       |     |
extendingittoleveragetheinformationprovidedbythem.
| resource | accounting | within | a   | single | host [10]. | They | intro- |     |     |     |     |     |     |     |     |
| -------- | ---------- | ------ | --- | ------ | ---------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Intheevaluationwehavedemonstratedauseofresource
ducednewabstraction,calledresourcecontainers,tobeused
|     |     |     |     |     |     |     |     | accounting | in  | preventing | SLA | violation | via | our resource |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | --- | --------- | --- | ------------ | --- |
asanewresourceprincipalwithinthekernel.Realizationof
controltechnique.Theproblemofresourcecontrolhasbeen
theresourcecontainerrequiredmodificationsofthekernelas
investigatedinseveralstudiesandvariouseffectivetechni-
| well as | applications. | Distributed |     | resource |     | container | [21], |           |      |           |     |             |             |        |     |
| ------- | ------------- | ----------- | --- | -------- | --- | --------- | ----- | --------- | ---- | --------- | --- | ----------- | ----------- | ------ | --- |
|         |               |             |     |          |     |           |       | ques have | been | developed |     | [37], [38], | [39], [40], | [41].. | One |
andPowerContainer[32]areextensionsofittothedistrib-
|                  |          |               |     |                |             |            |          | main difference |     | of our     | resource | control  | problem  | is    | that we |
| ---------------- | -------- | ------------- | --- | -------------- | ----------- | ---------- | -------- | --------------- | --- | ---------- | -------- | -------- | -------- | ----- | ------- |
| uted environment |          | in which      |     | local resource |             | containers | are      |                 |     |            |          |          |          |       |         |
|                  |          |               |     |                |             |            |          | are required    |     | to control | the      | resource | usage at | finer | thread  |
| bound            | together | by exchanging |     | global         | identifiers |            | via IPv6 |                 |     |            |          |          |          |       |         |
granularitywithinasharedinstance,whereasthesestudies
optionalfieldinordertocoordinatetheresourceconsump-
tion across hosts. The goal is to throttle the energy con- aim to better-schedule separate VM instances. However,
controltheoretictechniquessuchastheoneinQ-clouds[40]
| sumption | per | applications. | The | use | of resource |     | container |                |     |        |                 |     |          |     |       |
| -------- | --- | ------------- | --- | --- | ----------- | --- | --------- | -------------- | --- | ------ | --------------- | --- | -------- | --- | ----- |
|          |     |               |     |     |             |     |           | canbeappliedto |     | oursto | achieveaccurate |     | CPUusage |     | ratio |
reliesonthehelpfromtheapplicationforcorrectandtimely
amongCEs.
| binding   | of resource | principals |     | to the           | container, |        | although |     |     |     |     |     |     |     |     |
| --------- | ----------- | ---------- | --- | ---------------- | ---------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| they also | describe    | heuristics |     | to automatically |            | detect | the      |     |     |     |     |     |     |     |     |
bindings. The OS has to be modified to support the neces- 9 CONCLUSION
sarydatastructureforrepresentingtheresourcecontainers
(and the propagation of it to other hosts in case of the dis- In this paper we have presented our study on the problem
|     |     |     |     |     |     |     |     | of resource | accounting |     | within | an  | IT platform | that | offers |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | ------ | --- | ----------- | ---- | ------ |
tributedresourcecontainer).
The resource accounting problem has been studied by a shared services. In order to understand the nature of the
number of researchers. Reumann et al. [7] have recognized problem and find effective solution we have explored two
theproblemandproposedamechanism,StatefulDistributed differentaccountingtechniquesbuiltwithdifferentbalance
Interposition,forsharingtheapplicationcontextinformation of emphasis - LR-based technique and Rameter. Our main
across multi-tiered servers to support actions such as contributionistheresourceaccountingframework,Rameter,
enforcingresourcequota.Theydefinedthecontextabstrac- thatoperatesatthe hypervisor. Itcombines the monitoring
tionthatincludedtheidentityoftheclientandachievedthe unit that collects fine-grained thread-level data and the
creation of the contexts and propagation of them across inference unit that applies light-weight inference. Compar-
server via modification of OS and applications. Users are ing with LR-based approach, our analysis revealed that
requiredtorecompiletheapplicationafterinstrumentingit. there could be cases where more fine-grained monitoring
Fonseca et al. [8] described an architecture, Quanto, for informationdoesnotonlyprovidebetteraccuracy,butalso
tracking the energy consumption of embedded devices. To impact critical management decisions. Rameter also incurs
achieve the goal of energy tracking, they have developed a only about 1-2% of the turn-around time overhead to the
framework for resource accounting of distributed devices. systemcallsthatareintercepted.
| Since their                                      | target | environment |     | is embedded |     | systems,   | they |            |        |              |     |     |                           |     |     |
| ------------------------------------------------ | ------ | ----------- | --- | ----------- | --- | ---------- | ---- | ---------- | ------ | ------------ | --- | --- | ------------------------- | --- | --- |
| wereabletosupportthescenarioinwhichtheymakemodi- |        |             |     |             |     |            |      | REFERENCES |        |              |     |     |                           |     |     |
| fications                                        | to the | OS kernel   | and | require     | the | developers | to   |            |        |              |     |     |                           |     |     |
|                                                  |        |             |     |             |     |            |      | [1] E. M.  | Haber, | E. Kandogan, |     | and | P. Maglio, “Collaboration |     | in  |
writeapplicationsthatnotifytheOSoftheownerofvarious system administration,” Queue, vol. 8, no. 12, pp. 10:10–10:20,
activities. In one of the most recent work by Narasayya Dec.2010.
et al. [9], the resource accounting problem has been [2] E.Kotsovinos,“Virtualization:Blessingorcurse?”Queue,vol.8,
addressed in the context of mitigating the performance pp.40:40–40:46,2010.
|     |     |     |     |     |     |     |     | [3] Amazon | SimpleDB. |     | [Online]. | Available: | http://aws.amazon. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | --------- | ---------- | ------------------ | --- | --- |
interferences due to resource sharing within SQL Azure com/simpledb/,2015.
RDBMS. Their accounting mechanism relies on modifying [4] SQLAzureWhitepaper.[Online].Available:http://social.technet.
theinternalsoftheSQLAzuredatabase. microsoft.com/wiki/contents/articles/1695.inside-windows-
azure-sql-database.aspx,2010.
Thereareplentyofworksrelatedtomonitoringofdistrib-
|     |     |     |     |     |     |     |     | [5] Latency | is  | everywhere | and | it costs | you sales-how | to  | crush it. |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---------- | --- | -------- | ------------- | --- | --------- |
uted systems that are relevant to the resource accounting [Online]. Available: http://highscalability.com/blog/2009/7/
althoughtheydonotexplicitlytargettheresourceaccounting 25/latency-is-everywhere-and-it-costs-you\\-sales-how-to-crush-
problem we address in this work. Ganglia [33] is a distrib- it.html,2009.
|     |     |     |     |     |     |     |     | [6] S.Agarwala,F.Alegre,K.Schwan,andJ.Mehalingham,“E2eprof: |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
utedmonitoringsystemwithscalabilityinmind.Thegoalis Automated end-to-end performance management for enterprise
to provide statistics related to various resource types per systems,”inProc.37thAnnu.IEEE/IFIPInt.Conf.DependableSyst.
server in clusters. Itdoes notsupportfine-grained resource Netw.,2007,pp.749–758.
usagemonitoringperchargeableentities.Chopstix[34]pro- [7] J. Reumann and K. G. Shin, “Stateful distributed interposition,”
ACMTrans.Comput.Syst.,vol.22,no.1,pp.1–48,Feb.2004.
vides detailed monitoring information about low-level OS [8] R. Fonseca, P. Dutta, P. Levis, and I. Stoica, “Quanto: Tracking
events.Itaddsadatastructure,sketches,tothekernelinorder energy in networked embedded systems,” in Proc. 8th USENIX
to monitor page allocation, mutex/semaphore locking, and Conf.OperatingSyst.Des.Implementation,Berkeley,CA,USA,2008,
CPU utilization. They focus on building a sampling-based pp.323–338.
|     |     |     |     |     |     |     |     | [9] V. | R. Narasayya, |     | S. Das, | M. Syamala, | B. Chandramouli, |     | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------- | --- | ------- | ----------- | ---------------- | --- | --- |
system thatmonitors events of interest as a highresolution S.Chaudhuri,“Sqlvm:PerformanceisolationinMulti-tenantrela-
with low overhead. OProfile [35] is capable of delivering tionalDatabase-as-a-service,”inProc.CIDR,2013,pp.1–9.
detailedsystem-wideprofileinformation.Itprovidesconve- [10] G.Banga,P.Druschel,andJ.C.Mogul,“Resourcecontainers:A
newfacilityforresourcemanagementinserversystems,”inProc.
nient access to the performance counters. Nagios [36] is an 3rdSymp.OperatingSyst.Des.Implementation.Berkeley,CA,USA,
open source monitoring system that monitors CPU, disk, 1999,pp.45–58.
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore.  Restrictions apply.

TAKETAL.:RESOURCEACCOUNTINGOFSHAREDITRESOURCESINMULTI-TENANTCLOUDS 315
[11] B.Hindman,A.Konwinski,M.Zaharia,A.Ghodsi,A.D.Joseph, [35] John Levon. Oprofile. [Online]. Available: http://oprofile.
R. Katz, S. Shenker, and I. Stoica, “Mesos: A platform for Fine- sourceforge.net/credits/,2014.
grainedresourcesharinginthedatacenter,”inProc.8thUSENIX [36] Introducing the Windows Azure Paltform. [Online]. Available:
Conf. Netw. Syst. Des. Implementation, Berkeley, CA, USA, 2011, http://go.microsoft.com/?linkid=9752185,2011.
pp.295–308. [37] F.Checconi,G.Anastasi,andL.Abeni,“Respectingtemporalcon-
[12] Mesosphere.[Online].Available:https://mesosphere.com/,2015. straints in virtualised services,” in Proc. 2nd IEEE Int. Workshop
[13] Stratoscale. [Online]. Available: http://www.stratoscale.com/, Real-TimeServ.-OrientedArchit.Appl.,2009,pp.73–78.
2015. [38] F.Checconi,T.Cucinotta,D.Faggioli,andG.Lipari,“Hierarchical
[14] D.WentzlaffandA.Agarwal,“Factoredoperatingsystems(FOS): multiprocessorcpureservationsforthelinuxkernel,”inProc.5th
Thecaseforascalableoperatingsystemformulticores,”SIGOPS Int. Workshop Operating Syst. Platforms EmbeddedReal-Time Appl.,
Oper.Syst.Rev.,vol.43,no.2,pp.76–85,Apr.2009. 2009,pp.15–22.
[15] Openstack. [Online]. Available: http://www.openstack.org/, [39] J.Lee,S.Xi,S.Chen,L.T.X.Phan,C.Gill,I.Lee,C.Lu,andO.
2015. Sokolsky, “Realizing compositional scheduling through
[16] (2008). The Force.com Multitenant Architecture: Understanding virtualization,” in Proc. IEEE 18th Real Time Embedded Technol.
theDesignofSalesforce.com’sInternetApplicationDevelopment Appl.Symp., Washington,DC,USA,2012,pp.13–22.
Platform. [Online]. Available: in Force.com Whitepaper http://wiki. [40] R.Nathuji,A.Kansal, andA.Ghaffarkhah,“Q-clouds: Manag-
developerforce.com/index.php/Multi_Tenant_Architecture ing performance interference effects for qos-aware clouds,” in
[17] F.Chang,J.Dean,S.Ghemawat,W.C.Hsieh,D.A.Wallach,M. Proc. 5th Eur. Conf. Comput. Syst., New York, NY, USA, 2010,
Burrows,T.Chandra,A.Fikes,andR.E.Gruber,“Bigtable:Adis- pp.237–250.
tributedstoragesystemforstructureddata,”inProc.7thUSENIX [41] S. Xi, J. Wilson, C. Lu, and C. Gill, “Rt-xen: Towards Real-time
Symp. Operating Syst. Des. Implementation, Berkeley, CA, USA, hypervisorschedulinginxen,”inProc.9thACMInt.Conf.Embed-
2006. dedSoftw.,NewYork,NY,USA,2011,pp.39–48.
[18] M.Burrows,“Thechubbylockserviceforloosely-coupleddistrib-
utedsystems,”inProc.7thSymp.OperatingSyst.Des.Implementa- ByungChulTakisaresearchstaffmemberat
tion,Berkeley,CA,USA,2006,pp.335–350. IBM T.J. Watson Research Center, Yorktown
[19] S.Ghemawat,H.Gobioff,andS.-T.Leung,“Thegooglefilesys- Height,NY.HereceivedhisPhDincomputersci-
tem,” in Proc. 19th ACM Symp. Operating Syst. Principles, New encein2012fromPennsylvaniaStateUniversity.
York,NY,USA,2003,pp.29–43. HereceivedhisMSdegreeincomputerscience
[20] M.Y.Chen,A.Accardi,E.Kiciman,J.Lloyd,D.Patterson,A.Fox, from Korea Advanced Institute of Science and
andE.Brewer,“Path-basedfaliureandevolutionmanagement,” Technology (KAIST) in 2003, and his BS from
in Proc. 1st Conf. Netw. Syst Des Implementation, Berkeley, CA, YonseiUniversity,Koreain2000.Prior tojoining
USA,2004,pp.23–23. Pennsylvania State University, he worked as a
[21] A.WeisselandF.Bellosa,“Dynamicthermalmanagementfordis- researcher in the Electronics and Telecommuni-
tributed systems,”in Proc. 1st Workshop Temperature-Aware Com- cations Research Institute (ETRI), Daejeon,
put.Syst.,Munich,Germany,Jun.2004,pp.1–11. Korea. His research interest includes virtualization, operating systems
[22] P.Barham,A.Donnelly,R.Isaacs,andR.Mortier,“Usingmagpie andcloudcomputing.
forrequestextractionandworkloadmodelling,”inProc.6thConf.
Symp. Opearting Syst. Des. Implementation, Berkeley, CA, USA,
2004,pp.18–18. YoungjinKwonisaPhDcandidateatcomputer
[23] A. Dinaburg, P. Royal, M. Sharif, and W. Lee, “Ether: Malware science department, the University of Texas at
analysis via hardware virtualization extensions,” in Proc. 15th Austin. He received his BS degree in computer
ACMConf.Comput.Commun.Security,NewYork,NY,USA,2008, sciencefromSogangUniversityin2007,andhis
pp.51–62. MS degree in computer science from Korea
[24] D.Gupta,L.Cherkasova,R.Gardner,andA.Vahdat,“Enforcing Advanced Institute of Science and Technology
performance isolation across virtual machines in xen,” in Proc. (KAIST)in2009.HestartedhisPhDprogramin
ACM/IFIP/USENIXInt.Conf.Middleware,2006,pp.342–362. Sep,2012. Hiscurrent research interestsare in
[25] T.Wood,L.Cherkasova,K.Ozonat,andP.Shenoy,“Profilingand virtualization technology, improving operating
modelingresourceusageofvirtualizedapplications,”inProc.9th system,andsystemsecurity.
ACM/IFIP/USENIXInt.Conf.Middleware,2008,pp.366–387.
[26] A. Kansal, F. Zhao, J. Liu, N. Kothari, and A. A. Bhattacharya,
“Virtualmachinepowermeteringandprovisioning,”inProc.1st
ACMSymp.CloudComput.,NewYork,NY,USA,2010,pp.39–50. BhuvanUrgaonkarisanassociateprofessorin
[27] J. C. McCullough, Y. Agarwal, J. Chandrashekar, S. Kuppusw- the department of computer science and engi-
amy,A. C.Snoeren,andR. K.Gupta,“Evaluating theeffective- neeringatthePennsylvaniaStateUniversity.He
ness of Model-based power characterization,” in Proc USENIX receivedhisMS(2002)andPhD(2005)degrees
Conf.USENIXAnnu.Tech.Conf.,Berkeley,CA,USA,2011,p.12. incomputerscienceattheUniversityofMassa-
[28] C.Stewart,T.Kelly,andA.Zhang,“Exploitingnonstationarityfor chusetts,andhisBTech(1999)incomputersci-
performanceprediction,”inProc.2ndACMSIGOPS/EuroSysEur. ence and engineering at IIT Kharagpur. He is a
Conf.Comput.Syst.,2007,pp.31–44. recipient of the NSF CAREER Award, research
[29] W. Smith. TPC-W: Benchmarking An Ecommerce Solution. awards from HP Labs and Cisco, and has co-
[Online]. Availabole: http://www.tpc.org/information/other/ authoredbeststudentpapersatIEEEMASCOTS
techarticles.asp,2010. 2008andICAC2005conferences. Hisresearch
[30] RUBiS.[Online].Availabole:http://rubis.objectweb.org/,2008. involves applying ideas from distributed computing,resource manage-
[31] B.F.Cooper,A.Silberstein,E.Tam,R.Ramakrishnan,andR.Sears, ment, scheduling, performance evaluation, and analytical modeling to
“Benchmarking cloud serving systems with ycsb,” in Proc. 1st thedesignandevaluationofdatacenters,networkedsystems,operating
ACMSymp.CloudComput.,NewYork,NY,USA,2010,pp.143–154. systems, virtualization techniques, and storage systems. His current
[32] K. Shen, A. Shriraman, S. Dwarkadas, X. Zhang, and Z. Chen, researchfocusisincloudcomputing,powermanagementofdatacen-
“Power containers: An os facility for fine-grained power and ters,andstoragesystems.UrgaonkarisaseniormemberofIEEEand
energymanagementonmulticoreservers,”inProc.18thInt.Conf. seniormemberofACM.
Archit.SupportProgram.Lang.OperatingSyst.,2013,pp.65–76.
[33] M.L.Massie,B.N.Chun,andD.E.Culler,“Thegangliadistrib-
uted monitoring system: Design, implementation and experi-
ence,”ParallelComput.,vol.30,pp.817–840,2003.
[34] S. Bhatia, A. Kumar, M. E. Fiuczynski, and L. Peterson,
“Lightweight, High-resolution monitoring for troubleshooting
production systems,” in Proc. 8th USENIX Conf. Operating Syst.
Des.Implementation,Berkeley,CA,USA,2008,pp.103–116.
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore. Restrictions apply.