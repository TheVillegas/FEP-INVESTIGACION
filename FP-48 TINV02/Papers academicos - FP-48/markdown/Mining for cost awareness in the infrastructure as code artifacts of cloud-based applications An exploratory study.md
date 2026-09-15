TheJournalofSystemsandSoftware215(2024)112112
ContentslistsavailableatScienceDirect
TheJournalofSystems&Software
journalhomepage:www.elsevier.com/locate/jss
Miningforcostawarenessintheinfrastructureascodeartifactsof
✩
cloud-basedapplications:Anexploratorystudy
DanielFeitosa∗,Matei-TudorPenca,MassimilianoBerardi,Rares-DorianBoza,
VasiliosAndrikopoulos
BernoulliInstituteforMathematics,ComputerScienceandArtificialIntelligence,UniversityofGroningen,TheNetherlands
A R T I C L E I N F O A B S T R A C T
Keywords: Context:Cloud computing’s rise as the primary platform for software development and delivery is largely
Cloudcomputing drivenbythepotentialcostsavings.However,itissurprisingthatnoempiricalevidencehasbeencollected
Costawareness todeterminewhethercostawarenesspermeatesthedevelopmentprocessandhowitmanifestsinpractice.
Miningsoftwarerepositories Objective:This study aims to provide empirical evidence of cost awareness by mining open source repos-
Cloudorchestration
itories of cloud-based applications. The focus is on Infrastructure-as-Code artifacts that automate software
(re)deploymentonthecloud.
Methods:Asystematicexaminationof152735repositoriesyielded2010relevanthits.Wethenanalyzed538
relevantcommitsand208relevantissuesusinginductiveanddeductivecodingandcorroboratedfindingswith
discussionsfromStackOverflow.
Results:The findings indicate that developers are not only concerned with the cost of their application
deployments but also take actions to reduce these costs beyond selecting cheaper cloud services. We also
identifyresearchareasforfutureconsideration.
Conclusion:AlthoughwefocusonaparticularInfrastructure-as-Codetechnology(Terraform),thefindingscan
beapplicabletocloud-basedapplicationdevelopmentingeneral.Theprovidedempiricalgroundingcanserve
developers seeking to reduce costs through service selection, resource allocation, deployment optimization,
andothertechniques.
1. Introduction Amazon Web Services, Microsoft Azure, and Google Cloud Platform,
collectivelyknownashyperscalersduetotheirabilitytoenablescaling
Cost reduction is one of the main drivers of cloud adoption (An- to virtually infinite levels of demand, allow these providers to offer
drikopoulosetal.,2013).Costsavingsforthecloudconsumersaccrue access to these resources for almost (always) declining prices (Harms
due to two phenomena. First, access to any kind of computational andYamartino,2010).Thismakescloudcomputingveryattractiveto
resources (both hardware and software) is on-demand and is being allkindsandsizesoforganizationsandenterprises.
billedutilities-style(Melletal.,2011).Thismeansthatscalingupand Further testimony to the importance of cost for adopters of cloud
downtheamountoftheseresourcestomeettheneedsofthecurrent computingistheamountofrelatedworkonareasinvestigatinghowto
loadleadstohigherefficiencyincomparisonwithafixedinfrastructure minimizeand/ormanagethiscost.Thiscanbeachieved,forexample,
such as e.g. in a traditional data center. Compounding this, there is
fromtheperspectiveofcloudconsumersthroughoptimalcloudservice
also no need for upfront capital expenses for the acquisition of these
provider selection (Tricomi et al., 2020; Hosseinzadeh et al., 2020),
resources, e.g. to cope with unforeseen demand. This means a nearly
andfromtheperspectiveoftheprovidersbymeansofoptimizedtask
completetransferofthefocusfromthemanagementofcapitalexpenses
scheduling (Arunarani et al., 2019) or other profit optimization tech-
tooperationalones,alsoknownastheCAPEX-to-OPEXshift(Armbrust
niquessuchasenergyconsumptionminimization(Congetal.,2020).
etal.,2010).Second,andontopofthat,theeconomiesofscalerealized
Whatsmore,everycloudserviceprovideroffersinoneformoranother
by the cloud service providers, and especially by the ones such as
✩
Editor:ShaneMcIntosh.
∗ Correspondingauthor.
E-mailaddresses: d.feitosa@rug.nl(D.Feitosa),matei.penca1@gmail.com(M.-T.Penca),massimiliano.berardi93@gmail.com(M.Berardi),
raresboza@gmail.com(R.-D.Boza),v.andrikopoulos@rug.nl(V.Andrikopoulos).
URLs: https://feitosa-daniel.github.io(D.Feitosa),https://vandriko.github.io(V.Andrikopoulos).
https://doi.org/10.1016/j.jss.2024.112112
Received18December2023;Receivedinrevisedform10April2024;Accepted22May2024
Availableonline24May2024
0164-1212/©2024TheAuthors.PublishedbyElsevierInc.ThisisanopenaccessarticleundertheCCBYlicense(http://creativecommons.org/licenses/by/4.0/).

D.Feitosaetal.
TheJournalofSystems&Software215(2024)112112
costcalculatortools,allowingtheiruserstogetaquoteontheirservice identified related topics are discussed on a popular developer forum,
consumptionbasedontheirforeseencomputational,storage,network StackOverflow,1 inrelationtothesametypeofartifacts.Theanalysis
etc. needs. Consulting on cloud cost management has developed into oftheinvolvedpostsconfirmsthefitnessofourresulttopurpose.The
itsownlineofbusiness,withevencloudserviceprovidersthemselves contributionsofthisworkcanthereforebesummarizedasfollows:
offeringsuchservicestotheirusers.Inallcases,costisreferringtothe
• wecollectandpresentempiricalevidenceoftheexistenceofcost-
monetaryexpensesofhostingandrunningsoftwareinoneofthecloud relatedinformationpertinenttoTerraformartifactsasitappears
deploymentmodelsasdefinedbyNIST(Melletal.,2011). in(open)sourcecoderepositories;
| However,andtotheextentofourknowledge,noempiricalevidence |     |     |     |     |     |     |     | •   |     |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
wetriangulateandaugmentthisinformationextractionbyiden-
| exists on | whether      | and in | what form | the cost | of cloud-based |       | software |         |       |          |       |       |           |             |      |
| --------- | ------------ | ------ | --------- | -------- | -------------- | ----- | -------- | ------- | ----- | -------- | ----- | ----- | --------- | ----------- | ---- |
|           |              |        |           |          |                |       |          | tifying | Stack | Overflow | posts | where | pertinent | discussions | take |
| projects  | is discussed | among  | the       | involved | developers.    | While | on the   |         |       |          |       |       |           |             |      |
place;
| surface such | concerns | appear | to  | be outside | of the | remit | of software | •   |               |     |           |           |         |     |               |
| ------------ | -------- | ------ | --- | ---------- | ------ | ----- | ----------- | --- | ------------- | --- | --------- | --------- | ------- | --- | ------------- |
|              |          |        |     |            |        |       |             | we  | make publicly |     | available | a curated | dataset | of  | the artifacts |
developmentperse,thesituationinpracticeisquitedifferent.Thefact,
identifiedthroughthisevidence-collectionprocessandthescripts
| for example, | that | the DevOps | paradigm | became | popular |     | and widely |     |     |     |     |     |     |     |     |
| ------------ | ---- | ---------- | -------- | ------ | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
weusedduringthedatacollection,seeFeitosaetal.(2024);
| adopted almost | in  | the same | timeframe | as  | cloud computing |     | hints that |      |          |        |            |       |            |          |         |
| -------------- | --- | -------- | --------- | --- | --------------- | --- | ---------- | ---- | -------- | ------ | ---------- | ----- | ---------- | -------- | ------- |
|                |     |          |           |     |                 |     |            | • we | define a | set of | actionable | items | for future | research | on cost |
softwaredeveloperscannoteasilyignoretheoperationalaspectsofthe
awarenessbasedonourpreliminaryanalysisofthisdataset.
codetheyproduce,includingitscost.Furthermore,theaforementioned
Therestofthispaperisstructuredasfollows.Somerelatedworks
| utilities-like | billing | of cloud | services | means | that developers |     | are now |     |     |     |     |     |     |     |     |
| -------------- | ------- | -------- | -------- | ----- | --------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
arepresentedinSectionSection2.Section3discussesthestudydesign,
| in a position | to  | be held | effectively | accountable |     | for the | generated |     |     |     |     |     |     |     |     |
| ------------- | --- | ------- | ----------- | ----------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
includingthedefinitionofresearchquestionstoinvestigate.Section4
revenueofthesoftwarethattheyproduced,deployed,andranonthe
presentsourfindings,andSection5discussesourefforttotriangulate
| cloud infrastructure. |           | As such, | and    | further  | bolstered  | by the | amount of   |              |             |     |              |     |          |        |           |
| --------------------- | --------- | -------- | ------ | -------- | ---------- | ------ | ----------- | ------------ | ----------- | --- | ------------ | --- | -------- | ------ | --------- |
|                       |           |          |        |          |            |        |             | them through | developers’ |     | interactions | on  | a public | forum. | Section 6 |
| anecdotal             | evidence, | we do    | expect | software | developers | to     | be actively |              |             |     |              |     |          |        |           |
offersadiscussionontheimplicationsofthesefindingsforpractitioners
awareandconcernedaboutthecostoftheirsoftware,andwesetout
|     |     |     |     |     |     |     |     | and researchers, |     | including | the | formulation | of a | research | agenda for |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --------- | --- | ----------- | ---- | -------- | ---------- |
tocollectevidenceofthis.
futurework.Finally,Sections7and8closethispaperwithareflection
| The objective |     | of this | study is | therefore | clear: | to examine | to what |                |     |          |         |        |       |         |             |
| ------------- | --- | ------- | -------- | --------- | ------ | ---------- | ------- | -------------- | --- | -------- | ------- | ------ | ----- | ------- | ----------- |
|               |     |         |          |           |        |            |         | on the threats | to  | validity | to this | study, | and a | summary | of its main |
extentsoftwaredevelopersareawareofthecostofdeployingandoperating
findings,respectively.
cloud-basedsoftware,andwhatkindofconcernsandactioninitiativesthey
| are having | about | it. We choose |     | MSR (Mining | Software | Repositories) |     |     |     |     |     |     |     |     |     |
| ---------- | ----- | ------------- | --- | ----------- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2. Relatedwork
| as the means | to  | answer | this question | empirically. |     | Among | its other |     |     |     |     |     |     |     |     |
| ------------ | --- | ------ | ------------- | ------------ | --- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
uses,MSRallowstoempiricallystudyotherwisesubjectiveorexternal Asmentionedintheprevioussection,andtothebestofourknowl-
phenomena in combination with (or through) large-scale systematic edge,thereisnoexistingstudygatheringempiricalevidenceabouthow
mining of development artifacts. Fields such as green software engi- developers deal with the cost of deploying cloud-based or otherwise
neering(Hindle,2013;Pereiraetal.,2021),riskassessment(Choetkier- software,anddefinitelynonecollectedthroughrepositorymining.The
tikul et al., 2015; da Costa et al., 2017; Choetkiertikul et al., 2018), closest works in spirit in this direction are instead studies on mining
and software classification (Howard et al., 2013; LeClair et al., 2018; energy consumption awareness on the developer’s side such as the
Sas and Capiluppi, 2022) have advanced noticeably due to MSR. In workbyMouraetal.(2015)andBaoetal.(2016).Otherworkssuch
a similar fashion to these works, we hypothesize that the amount as the one by Pinto et al. (2014) on the same topic, or Das et al.
and diversity of costs-related information in cloud-based software project (2016) analyzing documented performance-related issues can be also
repositoriesissufficienttoproducemeaningfulinsights. consideredsomewhatrelatedtoours.
Cloud-basedapplicationdevelopment,however,coversaverywide
|     |     |     |     |     |     |     |     | However, | that | is not | to say | that there | are no | research | efforts for |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ------ | ------ | ---------- | ------ | -------- | ----------- |
rangeofapplicationtypesanddevelopmentactivities,andthiscreates supporting the management of cost in such systems. In fact, that is
aquestionofscopeinthisstudy.Selectingforaspecificprogramming a flourishing line of research approached from different perspectives.
language or ecosystem as in other MSR studies does not produce Despite being recognized early on as a major concern when migrat-
meaningful results here since these are orthogonal concerns to the ing existing systems to the cloud (Andrikopoulos et al., 2013), for
useofcloudinfrastructures.Instead,wescopeoursearchforevidence example, and being a crucial component in many migration support
to cloud orchestrator artifacts included in open source projects. Cloud approaches (Jamshidi et al., 2013), estimating the cost of deploying
orchestrators are Infrastructure as Code (IaC) solutions that provide and running software in the cloud remains an open research chal-
an abstraction layer over the self-service management APIs of the lenge(Shuaibetal.,2019).Costofdeploymentandoperationoftarget
various cloud service providers, with the intention of flattening out applications is one of the common factors taken into consideration
thedifferencesbetweenthem(deCarvalhoanddeAraujo,2020).This in works researching mechanisms for efficient decision making on
isusuallyachievedbymeansofdescriptorfiles,i.e.,configurationfiles which cloud service provider(s) to use (Hosseinzadeh et al., 2020).
thatwheninterpretedbytheorchestratorensurethatboththeunder- Thisalsoappearstobethecasefortherelatedproblemofoptimizing
theselectionofservicesfrompotentiallyacrossserviceproviders,com-
| lying infrastructure |     | is made | available, | and | the tasks | required | for the |             |     |               |     |             |        |     |              |
| -------------------- | --- | ------- | ---------- | --- | --------- | -------- | ------- | ----------- | --- | ------------- | --- | ----------- | ------ | --- | ------------ |
|                      |     |         |            |     |           |          |         | monly known | as  | cloud service |     | composition | (Amato | and | Venticinque, |
(re)deploymentofsoftwareonthisinfrastructureisexecutedcorrectly.
|            |           |         |                 |     |           |     |            | 2016; Vakili | and | Navimipour, | 2017). | Managing |     | the cost | (and energy |
| ---------- | --------- | ------- | --------------- | --- | --------- | --- | ---------- | ------------ | --- | ----------- | ------ | -------- | --- | -------- | ----------- |
| Descriptor | files are | usually | semi-structured |     | documents | in  | a machine- |              |     |             |        |          |     |          |             |
consumption)isalsoidentifiedasoneofthefocuspointsofarchitecting
| readable | format | that is easy | to  | process such | as YAML | or  | JSON, and |             |          |     |           |        |        |            |        |
| -------- | ------ | ------------ | --- | ------------ | ------- | --- | --------- | ----------- | -------- | --- | --------- | ------ | ------ | ---------- | ------ |
|          |        |              |     |              |         |     |           | cloud-based | software | as  | discussed | in the | survey | of Chauhan | et al. |
likeanyotherconfigurationfilestheyareaddedtocoderepositoriesto
(2017)onthetopic.
bemanagedbytherespectiveversioncontrolsystem.Orchestratorsare
either(cloudservice)provider-specific,suchasAmazonWebServices
3. Studydesign
| CloudFormation, |     | or provider-agnostic, |     | such | as Terraform, |     | Cloudify, |     |     |     |     |     |     |     |     |
| --------------- | --- | --------------------- | --- | ---- | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
ApacheHeat,andothersasdiscussedforexampleinTomarchioetal.
|             |         |      |         |           |            |       |           | In this       | section,  | we elaborate |            | on the methods |             | employed | to achieve  |
| ----------- | ------- | ---- | ------- | --------- | ---------- | ----- | --------- | ------------- | --------- | ------------ | ---------- | -------------- | ----------- | -------- | ----------- |
| (2020). For | reasons | that | will be | discussed | in Section | 3, we | focus our |               |           |              |            |                |             |          |             |
|             |         |      |         |           |            |       |           | the objective | presented |              | in Section | 1. In          | particular, | we       | discuss the |
workspecificallyonTerraformartifacts.
|     |     |     |     |     |     |     |     | derived research |     | questions, | the | required | data and | its collection, | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------- | --- | -------- | -------- | --------------- | --- |
In summary, this paper aims to report on the first work that at- howthedataisanalyzedtoprovidethenecessaryanswers.
| tempts to    | perform  | cost awareness |     | mining     | for cloud-based |     | application |     |     |     |     |     |     |     |     |
| ------------ | -------- | -------------- | --- | ---------- | --------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| development, | starting | with           | IaC | artifacts. | In addition,    | we  | fortify the |     |     |     |     |     |     |     |     |
findingsoftheminingprocessbyalsoinvestigatingtowhatextentthe 1 https://stackoverflow.com/
2

D.Feitosaetal.
TheJournalofSystems&Software215(2024)112112
3.1. Researchquestions We clarify that there are other viable options, Cloudify3 being
|     |     |     |     |     |     |     | a well known | one, | marginally | behind | Terraform | in terms | of  | perfor- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ---------- | ------ | --------- | -------- | --- | ------- |
To explore developers’ cost awareness and how it manifests in mance(KovácsandKacsuk,2017).Hyperscalersarealsoofferingtheir
projectrepositories,wedefinethreemainquestions: own IaC solutions, with AWS’ CloudFormation being a particularly
popularone.Inprinciple,therefore,wecouldexecutethisstudywith
RQ 1 Whatkindofrelevantinformationcanweextractfromcommits artifactsofmultiplecloudorchestratorstakenintoaccount.However,
onIaCartifacts? thecomplexityofanalyzingmultipleplatformswasdeemedprohibitive
sincethiskindofstudyisaresource-demandingendeavoras-is.More-
RQ 2 How can we augment this information further based on issues over,wefoundthenumberofprojectsonGitHubmentioningCloudify
raisedintherespectiverepositories? (876 repositories with around 79K commits) to be significantly fewer
|        |                 |                  |     |           |      |        | than that | of projects | mentioning | Terraform |     | (171K with | around | 1M  |
| ------ | --------------- | ---------------- | --- | --------- | ---- | ------ | --------- | ----------- | ---------- | --------- | --- | ---------- | ------ | --- |
| RQ How | can we organize | this information |     | so we can | gain | deeper |           |             |            |           |     |            |        |     |
3 commits). Cloudify has some of its features locked behind a pay-
insightsfromit? wall(KovácsandKacsuk,2017),potentiallyturningawaymanysmall
timeandopen-sourcedevelopers,whichmightexplainthisdifference
Inabsenceofanypriorstudyestablishingalinkbetweenactivities in numbers. Furthermore, provider-specific cloud orchestrators would
in repositories and cost awareness, we define these questions on a need a deeper understanding on our part of the cloud services being
purelyexploratorybase.Westrivetofindinformationrelatedtoactions used which would detract from the focus of the study. Nevertheless,
takenoncloud-basedsoftwareprojectsonthebasisofimpactingtheir
weacknowledgetherelevanceofinvestigatingotherplatformsinfuture
| deployment | cost. In an initial | exploration, | we  | seek stronger | evidence |     |     |     |     |     |     |     |     |     |
| ---------- | ------------------- | ------------ | --- | ------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
work(seeSection6).
| of such actions | and, thus, | focus on changes |     | to code connected |     | with |     |     |     |     |     |     |     |     |
| --------------- | ---------- | ---------------- | --- | ----------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Insummary,thecasesunderconsiderationforthisstudycomprise
| acknowledged | impact to         | cost by means | of commit   | messages |     | (RQ ). |                                                                   |     |         |                 |     |                     |     |        |
| ------------ | ----------------- | ------------- | ----------- | -------- | --- | ------ | ----------------------------------------------------------------- | --- | ------- | --------------- | --- | ------------------- | --- | ------ |
|              |                   |               |             |          |     | 1      | GitHubprojectsthatuseTerraformastheircloudorchestrator,andaddress |     |         |                 |     |                     |     |        |
| Next, we     | expand the search | scope for     | discussions | that may | not | incur  |                                                                   |     |         |                 |     |                     |     |        |
|              |                   |               |             |          |     |        | matters related                                                   | to  | cost in | commit messages | and | issues discussions. |     | In the |
in changes but that are relevant nevertheless (RQ 2 ). In the case of followingwedescribehowweactuallyapplythelattercriterion.
| this study, | we explore entries | in the | issue trackers | of  | projects | that |     |     |     |     |     |     |     |     |
| ----------- | ------------------ | ------ | -------------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
were identified in the previous research question. At this phase, it 3.3. Datacollectionandanalysis
| is also relevant | to understand | how | the topics | of discussion |     | differ |     |     |     |     |     |     |     |     |
| ---------------- | ------------- | --- | ---------- | ------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
(if at all) compared to the information on commit messages. This Following best practices in evidence-based software engineering
information can guide future research and development efforts (see (Wohlin et al., 2012), we characterize the population of this study in
Section6). termsofunitofanalysis.Theunitsofthisstudyarecommitsorissues
| The information | collected | in the previous |     | RQs can | inform | future |     |     |     |     |     |     |     |     |
| --------------- | --------- | --------------- | --- | ------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
inrepositoriesthatcontainevidenceofcloudcostawareness.Foreach
research and practitioner decisions. However, this ‘rawer’ format of validunit,weextractthetriplet<unit-id;unit-content;label>,
the data may often require examining the dataset in more depth to where:(a)unit-idreferstotherepositoryandcommithashorissue
unit-content
make connections between the identified core concepts and more in- id, (b) is the commit message or issue text, and (c)
formeddecisions.Thus,itisinstrumentaltounderstandhowtheknowl- label is a descriptor highlighting the main theme(s) derived from
edgeevolvingfromtheinformationextractedinthepreviousresearch unit-content.
questionscanbestructuredforthispurpose(RQ ). TheprocesstoextractandanalyzetheunitsissummarizedinFig.1.
3
|     |     |     |     |     |     |     | Locating | Terraform | descriptor | files is relatively |     | straightforward |     | since |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ---------- | ------------------- | --- | --------------- | --- | ----- |
3.2. Caseselection they are by default written in the HashiCorp Configuration Language
|     |     |     |     |     |     |     | (HCL), a | language | that | is indexed by | GitHub, | and carry | the | .tf or |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ---- | ------------- | ------- | --------- | --- | ------ |
Aswithpreviousstudiesonminingsoftwarerepositories,wedirect .tf.json extension as per the Terraform documentation.4 Further-
|     |     |     |     |     |     |     | more, Terraform’s |     | first release | was in | 2014, allowing | us  | to constrain |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------------- | ------ | -------------- | --- | ------------ | --- |
oureffortstoopensourcerepositories.Thereasoninghereisthatusing
suchanopencollectionofrepositoriesminimizestheselectionbiason our search further for repositories after this date. To automate the
PyGitHub.5
oursideandthereforeincreasestherobustnessofourpossiblefindings. interaction with GitHub’s API, we use Therefore we set
Among other qualities, we seek a source that can provide a sizable PyGitHubtosearch,onaday-to-daybasis,6 untiltheendofMay2022
anddiversepopulation.Also,fromapopulationthatmeetsthequality (whenthedatacollectionforthisstudytookplace),forrepositoriesthat
criteria, we must find the breadth and depth of the data that one can contain HCL files created after 2014. The search returns a candidate
derive. As a source of repositories, we choose GitHub mainly due to setof156585repositorylinks.Removingrepositoriesfromthissetthat
the volume and diversity of software projects that are available in it. do not include .tf or .tf.json files reduces this set to 152735
Moreover, we aim at maximizing the data pool while maintaining a repositoriesforfurtherconsideration.
systematic and repeatable approach and, therefore, GitHub’s search We then use a list of keyword stems to match against commit
|     |     |     |     |     |     |     | messages | and further | search | in this set | for cost-awareness. |     | However, |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ------ | ----------- | ------------------- | --- | -------- | --- |
featuresandAPIareinstrumental.
itisworthnoticingthatsincetherearenopreviousworksonthesame
| We also | already put forward | in the | introductory | section | our | par- |     |     |     |     |     |     |     |     |
| ------- | ------------------- | ------ | ------------ | ------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
topicwecannotreusetheirkeywordslistandwehavetocomeupwith
| ticular interest | in investigating | projects | that | use cloud | orchestrators. |     |     |     |     |     |     |     |     |     |
| ---------------- | ---------------- | -------- | ---- | --------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Sinceweseektoidentifyevidenceofdevelopers’discussionsovercloud our own. After some piloting, and considering the research questions
stems,7
infrastructurematters(inthiscase,cost),itisnaturaltonarrowdown we aim to answer, we decide on the following keyword (in
our search scope to projects that use IaC. The commit messages and alphabeticalorder):
issuesinvolvingdescriptorfileshavethepotentialtobringupconcerns
bill,cheap,cost,efficient,expens,andpay.
weareinterestedin.Forthepurposesofthisstudy,wechoosetowork
| with Terraform2                                            | as it is one | of the most | notable | and widely | adopted |     |     |     |     |     |     |     |     |     |
| ---------------------------------------------------------- | ------------ | ----------- | ------- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| orchestrators(deCarvalhoanddeAraujo,2020).Terraformisknown |              |             |         |            |         |     | 3   |     |     |     |     |     |     |     |
https://cloudify.co/
for providing an open-source version, cloud services compatibility, 4 https://www.terraform.io/language/files
interface accessibility and mature API (de Carvalho and de Araujo, 5 https://pygithub.readthedocs.io/
2020). 6 This was done to avoid the limitations in the amount of results by the
GitHubAPIperrequest.
|     |     |     |     |     |     |     | 7 Treating | them | as stems | means that | expens | for example | will | match |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | -------- | ---------- | ------ | ----------- | ---- | ----- |
2 https://www.terraform.io/ againstexpenseexpenses,inexpensive,andinexpensively.
3

D.Feitosaetal. TheJournalofSystems&Software215(2024)112112
Fig.1. Stepsofdatacollectionandanalysis.
Fig.2. RQ repositorydemographics(90thpercentile).
1
Usingthislist,weinstructPyDriller(Spadinietal.,2018)toprocess In Fig. 2, we characterize the repositories in terms of IaC ar-
all commit messages in the candidate repositories for the presence of tifacts’ size (iac-sloc, max. 89K), source code size (sloc, max.
oneormorethesekeywordsandweoutputtherepositoryname,com- 1210K), number of commits (#commits, max. 17K), contributors
mithashandmessage.PyDrillerisaPythonlibraryusedforanalyzing (#contributors, max. 596), number of Terraform modules
Git repositories. We chose this tool for its easy-to-use API and broad (#tfmodules, max. 1.4K), resources (#tfresources, max. 2.5K),
adoptionbytheMSRcommunity,whichweinterpretasanadditional variables (#tfvariables, max. 5K), subnets-related definitions
signofquality. (#tfsubnets, max. 32), instances-related definitions
After this step, a much more manageable set of 2010 repositories (#tfinstances,max.36),andnumberofTerraformclusters-related
containing 6116 potentially related commits is identified as a result. definitions(#tfclusters,max.21).Themaxvaluesarenotvisible
Thissetofcommitsandtheirrespectiverepositoriesserveasinputto inFig.2sinceweneededtotrimthetop10%valuesofeachvariableto
collectthedataandperformtheanalysisforeachresearchquestion. bettervisualizetheplot.Wealsonotethat65%(284)ofthepopulation
comprise repositories that contain (and manage) IaC artifacts only
3.3.1. RQ (i.e., they do not contain source code). These characteristics suggest
1
To answer the first research question, we must identify what kind that the population is varied with a tendency for repositories main-
ofinformationrelatedtocloudcostmanagementcanbeextractedfrom tained by few contributors and concentrated in repositories of more
the commits. Out of this set of 6116 commits, 377 are from forked Terraform and other IaC files than source code. This is possibly an
repositories already in the set. After filtering out these commits and indicationofdeveloperstakingovera‘‘Terraformexpert’’roleinteams
those that do not modify any Terraform files, we are left with 1162 that become responsible also with dealing with the operational cost
repositoriesand2045relatedcommits.Theselectedcommitsarethen aspectofeachproject.
inspected manually to decide their actual relevance. For that, each We then proceed to collect what kind of information related to
commit message is checked by two researchers and validated by a cloud cost management can be extracted from these commits. This
third one. Any conflicts are resolved by the entire team in consolida- is primarily a manual task, to be performed using open coding, a
tion meetings. The output of this process results in the identification form of inductive coding (Corbin and Strauss, 2014). For this task,
of 538 relevant commits. The selected units come from 434 distinct each data point (for this RQ, commit message) is labeled first by
repositories. two researchers and validated by a third. The labels refer to central
4

D.Feitosaetal.
TheJournalofSystems&Software215(2024)112112
ideas in the discussion and their characteristics. Any conflicts (incl. core concepts. This process is done in two steps, starting with topic
disagreements) are resolved by all five researchers in a consolidation modeling(Blei,2010)andfollowedbyasecondcodingactivity,culmi-
meeting. In this meeting, we verify the rationale for the codes and natinginthecreationofaknowledgegraphwhichcombinestheresults
analyzedtheevidenceagain(i.e.,thecompletecommitmessage),and oftheprevioussteps.Wedescribethesestepsinthefollowing.
arguedtoaconsensus.Wedidnothavecaseswhereaconsensuswas Topic modeling is a statistical learning tool that is well-suited
notmetafterthisprocess. for abstracting connections between words (into topics) from a cor-
As it will be discussed further in Section 4, all collected units are pus of documents (Blei, 2010). We apply Latent Dirichlet Allocation
analyzedtoidentifyrelevantcharacteristicssuchastheprevalenceof (LDA) (Blei, 2010), a popular topic-modeling technique used in a
thevariouslabelsanddistributionoftheunitsamongrepositories.In number of MSR studies e.g. Zimmerle et al. (2022), Al Alamin et al.
addition,meta-informationsuchastheunit-idisusedtoanalyzethe (2021),Chenetal.(2012),Hindleetal.(2011).
repositories,e.g.,regardingthenumberofsourcelinesofcode(SLOC) Before applying LDA, a number of steps must be undertaken for
andnumberofcontributors. cleaningandpreparingthecorpus.GitHubcontentcontainsamixture
|     |     |     |     |     |     |     |     | of Markdown | and | HTML | code scattered |     | throughout | the | text that we |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---- | -------------- | --- | ---------- | --- | ------------ |
mined.Thus,wefirstconvertanymarkdownsyntaxtoHTML,remove
3.3.2. RQ 2
|     |     |     |     |     |     |     |     | the content | in pre, | code | and blockquote |     | elements, | and | remove the |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ---- | -------------- | --- | --------- | --- | ---------- |
Forthesecondresearchquestion,wewishtoexplorewhatkindof
additionalinformationrelatedtocloudcostawarenesscanbeextracted markupandURLs.Wenotethatweremovecodesnippetsbecausewe
fromentriesinissuetrackersthataddstothatextractedfromcommit are interested in developers’ discussions and the code may bias the
messages.AsshowninFig.1,westartfromthelistof1339repositories LDA to find irrelevant topics. Next, we prepare each document using
obtained from the first filtering of commits based on keyword. We Stanza’s(Qietal.,2020)neuralnetworkNLPpipeline.8 Inparticular,
use this list because discussion may take place before actual changes wetokenizeitintosentencescontaininglistsoftokens,extractpart-of-
speech(PoS)tagsofeachtoken,andlemmatizethem.Thelatterstepis
| happen (as | demonstrated |     | by modification |     | to Terraform | files), | and we |     |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | --------------- | --- | ------------ | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
especiallyrelevanttoimprovethevalidityofthebagofwordsusedfor
wouldliketocapturethemtoo.Also,thissetofrepositoriesallowsus
topicmodeling.Fromthepreparedtokens,wefilterthePoStagsthat
| to narrow | down | the population |     | to an amount | of  | issues | that we can |     |     |     |     |     |     |     |     |
| --------- | ---- | -------------- | --- | ------------ | --- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
maycontainrelevantwords,i.e.,nouns,adjectives,adverbsandverbs.
feasiblyextractfromGitHubsincetheyalreadycontainsomeevidence
Wealsoremovetokensaccordingtoastop-wordlistthatwebuiltby
thatcostmaybeaconcernfortheproject.
To extract the issues, we provide GrimoreLab’s Perceval (Dueñas mergingtheGensim’s(ŘehůřekandSojka,2010)listforEnglishwith
etal.,2018)withtherepositoryownerusername,therepositoryname, terms deemed irrelevant for our analysis. We perform the same steps
andaGitHubAPItoken.PercevalisaPython-basedtoolthatcancollect forbothcommits’andissues’text.
|     |     |     |     |     |     |     |     | With | the prepared | corpus, | we  | use Gensim | to  | convert | it into a bag |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------ | ------- | --- | ---------- | --- | ------- | ------------- |
datafromvarioussources,includingissuetrackers.WechosePerceval
ofwords,buildaTF-IDF(termfrequency–inversedocumentfrequency)
foritsversatilityandvalidationwithintheMSRcommunity.Thetool
modelandusethetwotocreateLDAmodels.TobuildanLDAmodel,
| then returns | us a | list of issue | objects | that | contain | every | single detail |     |     |     |     |     |     |     |     |
| ------------ | ---- | ------------- | ------- | ---- | ------- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
wemustfindasuitablenumberoftopics(𝐾),asitimpactsthegran-
| pertaining  | the issue. | We      | then extract | the    | issue  | objects | that contain |            |             |             |     |         |           |         |            |
| ----------- | ---------- | ------- | ------------ | ------ | ------ | ------- | ------------ | ---------- | ----------- | ----------- | --- | ------- | --------- | ------- | ---------- |
|             |            |         |              |        |        |         |              | ularity of | the results | (Abdellatif |     | et al., | 2020; Han | et al., | 2020). The |
| one or more | of the     | defined | keywords     | in the | title, | body or | any of the   |            |             |             |     |         |           |         |            |
qualityofthemodelisalsoaffectedbyotherhyperparameters,suchas
comments;thisresultsinaninitialsetof862entries.
𝛼(referringtodocument-topicdensity)and𝛽9(referringtotopic-word
| Next, | we apply | a process | similar | to  | that described |     | for RQ to |     |     |     |     |     |     |     |     |
| ----- | -------- | --------- | ------- | --- | -------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
1
filter for relevant issues and then label them. Since issues may con- density)aresomeofthemostrelevant(Campbelletal.,2015;Treude
tain long discussions, the coding is focused on the context, i.e., the and Wagner, 2019). Following the related literature (Reboucas et al.,
2016;AlAlaminetal.,2021;Zimmerleetal.,2022),weexperimented
sentencewherethekeywordappearsandthesurroundingones(when
|                    |             |           |          |        |          |               |          | with the       | ranges 𝐾                                         | = {5,6,…,34,35}, |          | 𝛼         | = 𝛽 =       | {50∕𝐾,0.01}. | We also        |
| ------------------ | ----------- | --------- | -------- | ------ | -------- | ------------- | -------- | -------------- | ------------------------------------------------ | ---------------- | -------- | --------- | ----------- | ------------ | -------------- |
| needed).           | If multiple | keywords  | appear   | on     | the same | issue         | and they |                |                                                  |                  |          |           |             |              |                |
|                    |             |           |          |        |          |               |          | varied the     | chuncksize                                       | (number          | of       | documents | for         | each         | training mini- |
| refer to different |             | contexts, | multiple | checks | are      | performed.    | We note  |                |                                                  |                  |          |           |             |              |                |
|                    |             |           |          |        |          |               |          | batch)10 𝑆     | ={1,2,4,8,…,1024}asitcanyieldpositiveimpactonthe |                  |          |           |             |              |                |
| that the labels    | are         | applied   | to whole | issues | based    | on evidence   | found    |                |                                                  |                  |          |           |             |              |                |
|                    |             |           |          |        |          |               |          | model (Hoffman |                                                  | et al., 2010).   | Although |           | the quality | of           | the model is   |
| in any of          | the content | elements  | (i.e.,   | title, | body     | or comments). | This     |                |                                                  |                  |          |           |             |              |                |
ultimatelyassessedbyus,wereliedonthecoherence(Abdellatifetal.,
processculminatesintheselectionof208unitsbelongingto89distinct
|               |                                                   |     |     |     |     |     |     | 2020; Al       | Alamin | et al., 2021) | and     | perplexity |        | (Treude | and Wagner,   |
| ------------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- | ------ | ------------- | ------- | ---------- | ------ | ------- | ------------- |
| repositories. | InFig.3,wecharacterizetherepositoriesintermsofthe |     |     |     |     |     |     |                |        |               |         |            |        |         |               |
|               |                                                   |     |     |     |     |     |     | 2019; Zimmerle |        | et al., 2022) | metrics | to         | narrow | down    | the number of |
samemetricsasinFig.2:iac-sloc(max.43K),sloc(max.1486K),
#commits (max. 6K), #contributors, (max. 156), #tfmodules candidate models to be manually inspected. Finally, we train models
#tfresources #tfvariables using 100 iterations for hyperparameter exploration, and use 1000
| (max. 373K), |     |     | (max. | 646K), |     |     | (max. |     |     |     |     |     |     |     |     |
| ------------ | --- | --- | ----- | ------ | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
#tfsubnets, #tfinstances iterationstotrainthemodelsselectedformanualinspection.Afterthis
| 3.5K), |     | (max. | 39), |     |     | (max. | 34), and |     |     |     |     |     |     |     |     |
| ------ | --- | ----- | ---- | --- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
#tfclusters, process, we settled with 𝐾 = 12, 𝛼 = 50∕𝐾, 𝛽 = 0.01, and 𝑆 = 32 for
|     |     | max. 27). | We again | trimmed | the | top 10% | values of |                                            |     |     |     |     |     |     |             |
| --- | --- | --------- | -------- | ------- | --- | ------- | --------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | ----------- |
|     |     |           |          |         |     |         |           | themodelbasedonthecommitsdatasetmodel;and𝐾 |     |     |     |     |     |     | =5,𝛼 =0.01, |
eachvariabletobettervisualizetheplot.Thispopulationofrepositories
𝛽=50∕𝐾,and𝑆=2forthemodelbasedontheissuesdataset.
| is considerably | smaller | than     | that         | collected | for RQ  | , and     | contains a |       |        |          |             |     |       |           |          |
| --------------- | ------- | -------- | ------------ | --------- | ------- | --------- | ---------- | ----- | ------ | -------- | ----------- | --- | ----- | --------- | -------- |
|                 |         |          |              |           |         | 1         |            | Next, | we aim | to build | a knowledge |     | graph | by making | informed |
| lower amount    | of      | projects | that contain | (and      | manage) | Terraform | files      |       |        |          |             |     |       |           |          |
connectionsbetweenrelevantwords.Thesetwordscomefromboththe
| (only 44%). | Nevertheless, |     | the descriptive |     | statistics | summarized | by  |                      |     |     |       |                                 |     |     |     |
| ----------- | ------------- | --- | --------------- | --- | ---------- | ---------- | --- | -------------------- | --- | --- | ----- | ------------------------------- | --- | --- | --- |
|             |               |     |                 |     |            |            |     | codingperformedforRQ |     |     | andRQ | aswellasfromtheinterpretationof |     |     |     |
Fig. 3 suggest a fair distribution of data points, with higher averages 1 2
thetopicsofbothmodels.Tointerpretthetopics,weusedtheopencard
(byapprox.afactoroftwo).
|         |       |                   |     |           |          |             |       | sorting technique |     | (Abdellatif | et al., | 2020; | Zimmerle | et  | al., 2022) and |
| ------- | ----- | ----------------- | --- | --------- | -------- | ----------- | ----- | ----------------- | --- | ----------- | ------- | ----- | -------- | --- | -------------- |
| Similar | to RQ | 1 , the collected |     | units are | analyzed | to identify | rele- |                   |     |             |         |       |          |     |                |
analyzedthetopwordsofatopicviaarandomsampleofdocuments
| vant characteristics |     | such | as the prevalence |     | of the | various | labels and |           |       |        |                  |     |        |     |             |
| -------------------- | --- | ---- | ----------------- | --- | ------ | ------- | ---------- | --------- | ----- | ------ | ---------------- | --- | ------ | --- | ----------- |
|                      |     |      |                   |     |        |         |            | dominated | by it | (Ahmed | and Bagherzadeh, |     | 2018). | The | sample size |
distributionoftheunitsamongrepositories.Moreover,theresultsare
|          |          |          |      |         |         |        |             | varied from | 10 to | 20 documents |     | per topic, | depending | on  | the number |
| -------- | -------- | -------- | ---- | ------- | ------- | ------ | ----------- | ----------- | ----- | ------------ | --- | ---------- | --------- | --- | ---------- |
| compared | to those | obtained | from | RQ , to | reflect | on the | value added |             |       |              |     |            |           |     |            |
1 of documents connected to a given topic (we aimed for 5%–10% of
byexploringissues.Bothoftheseissuesaretobediscussedfurtherin
|     |     |     |     |     |     |     |     | the number | of documents |     | connected | to  | the topic). | Three | researchers |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | --- | --------- | --- | ----------- | ----- | ----------- |
Section4.
3.3.3. RQ 3 8 https://stanfordnlp.github.io/stanza/pipeline.html
In the final research question, we want to examine the dataset in 9 InGensim,theparameter‘eta’refersto𝛽.
more depth and make contextual connections between the identified 10 https://radimrehurek.com/gensim/models/ldamodel.html
5

D.Feitosaetal.
TheJournalofSystems&Software215(2024)112112
|     |     |     |     |     | Fig.3. | RQ repositorydemographics(90thpercentile). |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2
Removedthedefaultuseofdetailedmonitoring.
(#17)*ReducesCloudWatchcostsformetricsby
80%
|     |     |     |     |     |     |     | blinkist/terraform-aws-airship-ecs-cluster |     |     |     |     |     | (commit | hash: |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | ------- | ----- | --- |
d7aa6599)
Thisexampleshowcasesthefactthatmonitoringsolutionsprovided
bythecloudserviceprovidersmightofferdeepinsightsintothebilling
oftheirservices,butarealsoincurringexpensesfortheirusage,aswith
|     |     |     |     |     |     |     | any other           | cloud     | service. | This         | being the | most common     |         | label indicates |          |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --------- | -------- | ------------ | --------- | --------------- | ------- | --------------- | -------- |
|     |     |     |     |     |     |     | not only            | awareness | on       | behalf       | of the    | developers,     | but     | also            | specific |
|     |     |     |     |     |     |     | cost reducing       |           | actions  | as an effect | of        | this awareness. |         | As a matter     | of       |
|     |     |     |     |     |     |     | fact, approximately |           | 70%      | of all       | commits   | as shown        | in Fig. | 4 document      |          |
concreteactionstosavecost.Characterizingthetypesofactionstaken
Fig.4. Codingdemographicsofcommits.
|     |     |     |     |     |     |     | is outside | of  | the scope | of this | work, | but can | be easily | achieved | by  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | ------- | ----- | ------- | --------- | -------- | --- |
furtherprocessingthecommitsinthedataset.
Thenextmostpopularlabelisawareness,whichdoesalsoimply
action,e.g.:
applied the technique, with the other two researchers validating the natgatewayisverry[sic]expensive
resultsandresolvingdisagreements.Finally,therelationshipbetween stealthHat/k8s-terraform(hash:681a3f8b)
wordsisdefinedbyapplyingaxialcodingandselectivecoding(Corbin
| and Strauss, | 2014) | on the        | preexisting | labels | (from       | RQ and RQ )  |                                                          |     |     |     |     |     |     |     |     |
| ------------ | ----- | ------------- | ----------- | ------ | ----------- | ------------ | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|              |       |               |             |        |             | 1 2          | ThisparticularexampleidentifiesawellknownissuewithAmazon |     |     |     |     |     |     |     |     |
| and words    | from  | topics. Axial | coding      | is a   | combination | of inductive |                                                          |     |     |     |     |     |     |     |     |
WebServices’NATGatewayservicewithrespecttocostaccruingeasily
| and deductive | coding | with | the goal | of relating | codes | (e.g., finding |     |     |     |     |     |     |     |     |     |
| ------------- | ------ | ---- | -------- | ----------- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
outofcontrolthatiseventhesubjectofonlinememesandfrequently
emergingcategories).Selectivecodingisasimilarprocess,buttofind
recurringTwitterthreads.11
thecoresetofcodesandcategories.Groupcategoriesandrelationship
Finally,thelabelinstanceunderstandablyfiguresamongthetop
| between labels | can | be identified | from | a topic | (if a word | can describe |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ------------- | ---- | ------- | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
recurringlabels.Anexamplefromthedatasetis:
| the topic well) | and | from manual | inspection |     | of labels | and their linked |                                          |     |     |     |     |     |     |     |     |
| --------------- | --- | ----------- | ---------- | --- | --------- | ---------------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| documents.      |     |             |            |     |           |                  | Movefromm4.largetom5.large.Thenewgenhave |     |     |     |     |     |     |     |     |
moreCPUandarecheaper
4. Results
alphagov/govuk-aws(hash:6cfda6ad)
| The presentation |     | of the | results | follows | the | RQs defined in |     |               |      |       |        |         |          |         |     |
| ---------------- | --- | ------ | ------- | ------- | --- | -------------- | --- | ------------- | ---- | ----- | ------ | ------- | -------- | ------- | --- |
|                  |     |        |         |         |     |                | In  | this respect, | this | label | can be | located | anywhere | between | the |
Section3.
previoustwoones:itcanidentifyawarenessandintentionofactionat
thesametime.Onarelatednote,itisworthpointingoutthat,although
| 4.1. CostAwarenessinCommits(RQ |     |     |     | )   |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1 lessprevalent,wealsoidentifiedinformationexplicitlydiscussingcost
increasesduetoapriorchange(inroughly2%oftheunits).
As a result of the coding process, we obtain a set of 14 distinct Altogether, we notice developers’ consciousness of consequences
labelsrelatedtothe538commits.Eachcommithasbetweenoneand of decisions in deployment. Moreover, labels such as instance and
| fivelabelsassignedtoitbasedonthemessagecontent.Fig.4liststhe |     |     |     |     |     |     | storage |       |             |         |     |                |     |          |        |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------- | ----- | ----------- | ------- | --- | -------------- | --- | -------- | ------ |
|                                                              |     |     |     |     |     |     |         | point | to specific | aspects | of  | the deployment |     | that are | or can |
collectedlabels,andshowstheirrecurrenceamongunits(i.e.,commits)
|     |     |     |     |     |     |     | be tuned | to  | manage cost. | From | Fig. | 4, we cannot | infer | or speculate |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------ | ---- | ---- | ------------ | ----- | ------------ | --- |
anddistinctrepositories,andnumberofdistinctcontributorsassociated
overwhichofsuchaspectsaremoreoftentreatedthisway.However,
| with them. | We provide | a   | description | of each | label | in Table 1 and |             |     |                   |     |         |         |              |     |         |
| ---------- | ---------- | --- | ----------- | ------- | ----- | -------------- | ----------- | --- | ----------------- | --- | ------- | ------- | ------------ | --- | ------- |
|            |            |     |             |         |       |                | considering |     | the configuration |     | options | offered | by platforms |     | such as |
elaborateonthemostrecurrentonesinthefollowing.
saving.
| The most | popular | label | by all | metrics | is  | A notorious |     |     |     |     |     |     |     |     |     |
| -------- | ------- | ----- | ------ | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
examplefromthedatasetis: 11 Seee.g.https://twitter.com/quinnypig/status/1440301033314349062
6

D.Feitosaetal.
TheJournalofSystems&Software215(2024)112112
Table1
Labeldescriptions.
|     | Label |     |     |     | Description |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
alert textexpressingconcernsrelatedtobillingalarmsenforcinganupperthresholdoncosts.
area textexpressingconcernsrelatedtoserverorinstancegeographicallocation.
awareness textsimplymentioningconcernswithcost(withoutnecessarilyimplyingaction).
billing_mode textexpressingconcernsrelatedtothetypeofbillingplanbeingused(e.g.,on-demandfor
developmentornormalplanforproduction).
|     | cluster |     |     |     | textexpressingconcernsrelatedtoclusterconfiguration.           |     |     |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | domain  |     |     |     | textexpressingconcernsrelatedtodomainnamesystemandIPaddresses. |     |     |     |     |     |     |     |     |     |
feature textexpressingconcernsrelatedtovariousfeaturessuchaslogging,loadbalancersorusageofthird
partylibraries.
|     | increase |     |     |     | textexpressingconcernsrelatedtoincreaseincostduetoachange. |     |     |     |     |     |     |     |     |     |
| --- | -------- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
instance textexpressingconcernsrelatedtocomputationalinstances(e.g.,AmazonAWSt2.micro)usedinthe
deployment.
|     | networking |     |     |     | textexpressingconcernsrelatedtonetworkingconfiguration. |     |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
policy textexpressingconcernsrelatedtotheimplementationofgeneralrulestopreventexcessivecharges.
provider textexpressingconcernsrelatedtochoosingaserviceproviders(e.g.,Amazon,Azure,Google).
|     | saving |     |     |     | denotesmentionedchangesmadetosavecosts. |     |     |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
storage textexpressingconcernsrelatedtostoragesolutions(e.g.,Amazongp2)usedinthedeployment.
Terraform,thedatasuggestabroadunderstandingoftheseoptions.At
thesametime,thenumberofrepositoriesinourdatasetcomparedto
thetotalamountofprojectsusingTerraformmayalsosuggestthatonly
| a small percentage |     | of developers |     | are interested |     | or aware | of the | cost- |     |     |     |     |     |     |
| ------------------ | --- | ------------- | --- | -------------- | --- | -------- | ------ | ----- | --- | --- | --- | --- | --- | --- |
savingpossibilitiesinIaCconfiguration.Wenotethatthisobservation
isalsospeculativeasitrequiresfurtherinvestigationtoe.g.discardtest
| or template | projects. | Further   | insights            | can | be gained | by    | analyzing       | the |     |     |     |     |     |     |
| ----------- | --------- | --------- | ------------------- | --- | --------- | ----- | --------------- | --- | --- | --- | --- | --- | --- | --- |
| dataset in  | more      | depth for | e.g. characterizing |     | the       | types | of repositories |     |     |     |     |     |     |     |
withrespecttothelabelsusedintheircommits,identifyingtherelation
| between        | labels and | contributors |            | and so | on. This | kind  | of analysis | is  |     |     |     |     |     |     |
| -------------- | ---------- | ------------ | ---------- | ------ | -------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| left as future | work       | and          | as part of | a call | to the   | wider | community,  | as  |     |     |     |     |     |     |
discussedbelowinSection6.
| 4.2. CostAwarenessinIssues(RQ |     |        | 2          | )        |                |     |        |     |     |     |                                    |     |     |     |
| ----------------------------- | --- | ------ | ---------- | -------- | -------------- | --- | ------ | --- | --- | --- | ---------------------------------- | --- | --- | --- |
|                               |     |        |            |          |                |     |        |     |     |     | Fig.5. Codingdemographicsofissues. |     |     |     |
| The coding                    |     | of the | 208 issues | resulted | in recognizing |     | labels | we  |     |     |                                    |     |     |     |
identifiedinthecommit-unitsofanalysis,withoutaddingnewones.We
notethatonelabel,namelypolicy,wasnotidentifiedamongissues. ButtheLBs(HTTP(s)andTCP)donotworkbecause
Each issue discussion has between one and four labels assigned to it they only have the default/main worker pool as
basedonthetextinthetitle,bodyandcomments.Fig.5describethe targetpool,andinmysetupitssizeis0.SoIam
labelsintermsoftheirrecurrenceamongunits(i.e.,issues)anddistinct kindapayingforGlobalFWrulesthathavenouse
|     |     |     |     |     |     |     |     |     | and | I cannot | delete | them | because | they will get |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ---- | ------- | ------------- |
repositories,andnumberofdistinctcreatorsandcommenters.
createdagaininthenext‘terraformapply‘.
Atafirstglance,wenoticeconsiderablesimilaritybetweenFigs.4
label:networking
and 5. We explored this observation further by inspecting the con- poseidon/typhoon(issue:#558)
| tent of a | random      | sample | of units | from     | both datasets | that | are    | tagged  |     |     |     |     |     |     |
| --------- | ----------- | ------ | -------- | -------- | ------------- | ---- | ------ | ------- | --- | --- | --- | --- | --- | --- |
| with the  | same label. | For    | that, we | selected | 50 commits    |      | and 20 | issues, |     |     |     |     |     |     |
Thus,whilecommitmessagesarecommonlymorecompactandmay
i.e. aiming for a representativeness of 10%. In general, we notice report cost-changing actions, issues may shed light on the decision-
that issues contain more information around the cost-related matter makingprocessthatdevelopersundergobeforeapplyingacost-affecting
athand,whichisexpectedsincetheyessentiallyprovideadiscussion change.Anexampleofthiscontrastcanbeseeninthefollowingunits
forum. More importantly, we found the extra amount of information bothlabeledasinstance:
| to be often | related | to decision-making |     | around | the | cost | matter. | Actors |     |     |     |     |     |     |
| ----------- | ------- | ------------------ | --- | ------ | --- | ---- | ------- | ------ | --- | --- | --- | --- | --- | --- |
may present hints on the current configuration of the deployment, Change code to use the cheaper r4.xlarge
instancestype.
| the alternatives |     | for change, | the | rationale | and even | potential |     | feature |     |     |     |     |     |     |
| ---------------- | --- | ----------- | --- | --------- | -------- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- |
cisagov/cyhy_amis(hash:4e67a501)
| requests.  | For example, |     | see the  | following   | two  | samples | from           | differ- |     |     |     |     |     |     |
| ---------- | ------------ | --- | -------- | ----------- | ---- | ------- | -------------- | ------- | --- | --- | --- | --- | --- | --- |
| ent issues | showing      | the | depth of | information | that | can     | be potentially |         |     |     |     |     |     |     |
extracted:
|     |     |     |     |     |     |     |     |     | It  | would | be really | great | if the | new ‘t4g‘ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --------- | ----- | ------ | --------- |
By having a personal deployment, we are instance, which are even cheaper than
free to experiment and research without any ‘t3.nano‘,wouldbesupportedaswell
limitation. The drawback is that it implies a Guimove/terraform-aws-bastion(issue:#124)
| cost | for   | the cloud | provider. |                    | Alternatively, |     |     |     |     |     |     |     |     |     |
| ---- | ----- | --------- | --------- | ------------------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| we   | could | imagine   | a         | ‘sandbox.qhub.dev‘ |                |     |     | or  |     |     |     |     |     |     |
Whilethecommitmessagecommunicatesthechangeforacheaper
‘alpha.qhub.dev‘orwhatever
label:provider instance, the issue hints on the current configuration and expresses
Quansight/qhub(issues:#924)
|     |     |     |     |     |     |     |     |     | the wish  | for a new    | feature | (i.e., support | of a different | instance). We    |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | ------- | -------------- | -------------- | ---------------- |
|     |     |     |     |     |     |     |     |     | note that | this example | regards | different      | repositories.  | We tried to find |
7

D.Feitosaetal.
TheJournalofSystems&Software215(2024)112112
|     |     |     |     |     |     | now take    | a step  | back to collect |              | more relevant |            | labels and | establish |
| --- | --- | --- | --- | --- | --- | ----------- | ------- | --------------- | ------------ | ------------- | ---------- | ---------- | --------- |
|     |     |     |     |     |     | connections | between | them.           | As described |               | in Section | 3.3.3, we  | started   |
bymodelingtopicsfromourdataset,andthenproceedtoperformaxial
andselectivecodingbasedonthetopicsandthelabelsidentifiedinour
dataset.
|     |     |     |     |     |     | DuringtheinvestigationofRQ |     |     |     | ,weestablishedthatthetextinboth |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | ------------------------------- | --- | --- | --- |
2
|     |     |     |     |     |     | commit messages |     | and issues’ | content | is varied | but | complementary | in  |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ----------- | ------- | --------- | --- | ------------- | --- |
nature.Soweaimedtocreateonemodelpersetofunitstoavoidthe
|     |     |     |     |     |     | risk of not | identifying | relevant | topics. | As  | a result | of our topic | mod- |
| --- | --- | --- | --- | --- | --- | ----------- | ----------- | -------- | ------- | --- | -------- | ------------ | ---- |
eling,weidentified12topicsfromcommitunitsandfivetopicsfrom
issueunits.Theusedhyperparameterconfigurations(seeSection3.3.3)
yieldedthemostpromisingresults,butnotalltopicswereusefulforour
purposes.
|     |     |     |     |     |     | In particular, |     | only one | topic derived | from | issues | was considered. |     |
| --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | ------------- | ---- | ------ | --------------- | --- |
Fig.6. Codingdemographicsofthecombineddataset. Therelevanttopicsmentioncost-relatedterms(e.g.,‘cheap’,‘expen-
sive’,‘budget’,‘waste’)andactions(e.g.,‘change’,‘move’,‘add’,‘test’,
‘upgrade’)associatedwithvariouspropertiesofthedeployment,both
connections between commits and issues but our dataset does not general (e.g., ‘VM’, ‘storage’, ‘disk’, ‘machine’) and specific (e.g., ‘dy-
| contain any | direct links to | issue in commit | messages. | An alternative |     |     |     |     |     |     |     |     |     |
| ----------- | --------------- | --------------- | --------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
namodb’,‘CPU’,‘NAT’,‘EC2’,‘RAM’).Someoftheconnectionsrevealed
toexplorethisavenueistostudypullrequests,whichisoutsideofour
|     |     |     |     |     |     | through | the topics | are already | observable |     | in our | coding for | RQ 1 and |
| --- | --- | --- | --- | --- | --- | ------- | ---------- | ----------- | ---------- | --- | ------ | ---------- | -------- |
scopebutmentionedinourresearchagenda(seeSection6).
|     |     |     |     |     |     | RQ ,intheformofco-occurringlabelsassummarizedbyFig.7.The |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
2
Continuingwiththeanalysis,wenoticesomechangesintheorder figurepresentstheseco-occurrencerelationshipsasanUpSetplot(Lex
ofthelabelsintermsofrecurrence.Fig.6showsacomparisonofthe et al., 2014). The labels (with their frequencies) are shown as rows
twosetsofunitsandhelpstovisualizetheirdifferences.awareness
onthebottompart,andthefrequencyofthevariouscombinationsof
ismorerecurrentthansavingamongissues,whichmightberelated
labelsarerepresentedascolumnsonthetoppartanddescribedthrough
| to our observation | that issues | can be a more | prominent | platform | for |     |     |     |     |     |     |     |     |
| ------------------ | ----------- | ------------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theconnecteddotsonthebottompart.
decision-making.Onasimilarnote,unitslabeledwithincreaseare
Wethenappliedaxialandselectivecodingtoaggregateterms(from
| also more | recurrent among | issues (compared | to commit | units). | This |     |     |     |     |     |     |     |     |
| --------- | --------------- | ---------------- | --------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
topicsandlabels)andinspecttherelationshipsintheunits.Attheend
mightalsobeinlinewiththenatureofissues,inthiscase,reporting
|     |     |     |     |     |     | of this process, |     | we created | the knowledge |     | graph | depicted | in Fig. 8. |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------- | ------------- | --- | ----- | -------- | ---------- |
oracknowledgingcostincrease.Theexamplebelowdepictsasituation
ofaseeminglyunintentionalincrease. The graph compiles three main levels of information: effects on cost,
actionsrelatedtoaneffect,andthepropertiesofthedeploymentthat
Pods for some core services have migrated over are considered for the action. The edges reflect the most significant
to high-memory nodes, which have a much higher connectionswefoundandsubsequentlyconfirmedinthedataset.
costthatthegeneralnodes.Itriedkillingthe Themostrecurrentrelationshipsidentifiedduringtheopencoding
podhopingitwouldrestartonadifferentnode,
|     |     |     |     |     |     | (for RQ 1 | and RQ | 2 ) are also | represented | in  | the graph. | Moreover, | new |
| --- | --- | --- | --- | --- | --- | --------- | ------ | ------------ | ----------- | --- | ---------- | --------- | --- |
butusuallyitjustrestartsonthesamenode.
linksbetweenpreexistinglabelswerefoundbasedontopics(e.g.,be-
Quansight/qhub(issue:#321) tween increase and alert) and new, more specific, terms ap-
peared(e.g.,‘CPU’).Wehighlightthat,althoughseeingspecificterms
|           |                    |               |     |              |     | in one context |     | is what led | us to | add the | associated | general | label |
| --------- | ------------------ | ------------- | --- | ------------ | --- | -------------- | --- | ----------- | ----- | ------- | ---------- | ------- | ----- |
| From Fig. | 6, we also observe | that, despite | the | lower number | of  |                |     |             |       |         |            |         |       |
(e.g.,instancefor‘CPU’),thefactthatthespecifictermappearsin
| repositories | among issue-units | of analysis, | the majority | (54 | out of 89, |     |     |     |     |     |     |     |     |
| ------------ | ----------------- | ------------ | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
and an average of 85% per label) are unique to them. In conclu- atopicisastrongindicativethatitisprominent.Suchparticularcases
sion,despitethesimilaritiesoftheassignedlabels,theresultssuggest promptedustoincludethespecifictermtographandconnectittothe
that the information extracted from issues can complement that from relatedtermsandthemoregeneralone.
commits. In particular, issues can provide more knowledge about the After identifying their relationships, some of the topics identified
| decision-making | surrounding | cost management | in  | the deployment | of  |     |     |     |     |     |     |     |     |
| --------------- | ----------- | --------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
forthepreviousquestioncanbeinterpretedasspecificpainpointsthat
cloudsystemsconfiguredwithIaC.
|     |     |     |     |     |     | developers    | are clearly | concerned | about:     | choices |                | concerning | network- |
| --- | --- | --- | --- | --- | --- | ------------- | ----------- | --------- | ---------- | ------- | -------------- | ---------- | -------- |
|     |     |     |     |     |     | ing, instance | and         | provider  | selection, | and     | the applicable | billing    | mode     |
4.3. KnowledgeOrganization(RQ 3 ) (property levelinFig.8).Othertopicssignifyspecificactionstakento
addresstheseconcerns,orawarenessthattheseactionscould/shouldbe
From the initial coding performed for RQ 1 and RQ 2 , we obtained takentoavoidunnecessarycosts:settingorremovingalerts,testingfor
| a set of 14 | labels. Moreover, | as we delved | in the | units’ content | to  |     |     |     |     |     |     |     |     |
| ----------- | ----------------- | ------------ | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
oneormoreoftheseconcerns(e.g.theuseofVPN),orchangingsome-
furtherunderstandwhatkindofinformationcanbeextracted,wefound
thingintheTerraformfiletowardsdirectlydealingwiththeseconcerns
evidenceofconnectionsandadditionalrelevantthemes.Forexample,
|     |     |     |     |     |     | (action level | in Fig. | 8). All | these actions, |     | both affected | and | intended |
| --- | --- | --- | --- | --- | --- | ------------- | ------- | ------- | -------------- | --- | ------------- | --- | -------- |
intheunitregardingalphagov/govuk-aws(hash:6cfda6ad)presentedin
|     |     |     |     |     |     | to be affected | can | be characterized |     | based | on their | desired | outcome: |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ---------------- | --- | ----- | -------- | ------- | -------- |
Section4.1,wenoticeaclearlinkbetweeninstanceandsaving,as
increasingawareness,dealingwithincreasingcosts,orproducesavings
wellasindicationofwhatmotivatesthechange(i.e.,moreCPU).This
|     |     |     |     |     |     | (effect levelinFig.8). |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
particularunithadalreadybeentaggedwithbothlabels,butourlabels
arenotfine-grainedtothepointofprovidinglowerlevelsofdetail. Inconclusion,theinformationaggregatedintheknowledgegraph
Wenotethatonemainreasonfornotusingfiner-grainedlabelsdur- servesasasummaryofrelevantcost-relatedconcernsandactionswhen
ingcodingwastoavoidexplosionoflabelsthat,althoughmeaningful, deployingcloud-basedapplicationsusingTerraform.Italsointroduces
|           |                      |          |            |           |         | the subjects | one      | may expect  | to find | in our | dataset  | in terms   | of both |
| --------- | -------------------- | -------- | ---------- | --------- | ------- | ------------ | -------- | ----------- | ------- | ------ | -------- | ---------- | ------- |
| might not | have been ultimately | relevant | (i.e., not | recurrent | enough) |              |          |             |         |        |          |            |         |
|           |                      |          |            |           |         | content and  | context. | Altogether, | it      | opens  | the door | to extract | deeper  |
andcouldriskthequalityoftheprocedure.Ourgoalistoguidefuture
researchandpractitioners’decisionsbyprovidingamoregeneralizable insights and inform research and deployment decisions, as discussed
| and actionable | knowledge based | on developers’ | experience. |     | Thus, we | below. |     |     |     |     |     |     |     |
| -------------- | --------------- | -------------- | ----------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
8

D.Feitosaetal.
TheJournalofSystems&Software215(2024)112112
Fig.7. UpSetplotshowingtheoccurrencesandco-occurrencesoftopiclabelsincommitmessagesandissuesdiscussionsaslabelintersectionsresultingfromtheopencodingin
RQ 1 andRQ 2 .
|     |     |     |     |     |     |     |     | 2023datadump,namely,posts,13 |     |     | comments14 | andchangehistories,15 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | ---------- | --------------------- | --- | --- |
totaling57.3GiB.Asthegoalofthisprocessistotriangulatetheresults
ofthestudyonGitHubrepositories,wespecificallytargeteddiscussions
|     |     |     |     |     |     |     |     | about Terraform, | rooted        | in questions | containing |         | tags with the | string |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------------- | ------------ | ---------- | ------- | ------------- | ------ |
|     |     |     |     |     |     |     |     | ‘terraform’      | in the post’s | metadata.    | Thus, we   | started | by filtering  | ques-  |
|     |     |     |     |     |     |     |     | tions fitting    | the mentioned | criteria,    | which      | led to  | a dataset of  | 19139  |
questionsstoredasJSONfiles.
Wegatheredthecommentsandposthistoriesassociatedwitheach
questionandupdatedtherespectiveJSONfiletoincludethem.Wethen
extractedtheanswerslinkedtoeachquestion,identifiedthroughtheir
|     |     |     |     |     |     |     |     | parentpost        | IDs,andadded | thecommentsand |                 | posthistories |           | similarly |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ------------ | -------------- | --------------- | ------------- | --------- | --------- |
|     |     |     |     |     |     |     |     | to the questions. | The answers  |                | (and associated | data)         | were then | added     |
tothequestionfiles,creatingthefinalversionofthedatasetof19139
questionsandtheirassociatedanswers,completewiththeirrespective
commentsandposthistories.
| Fig. 8. Knowledge                       | graph | resulting | from the | axial and | selecting | coding; label | save |                   |              |       |                  |     |            |         |
| --------------------------------------- | ----- | --------- | -------- | --------- | --------- | ------------- | ---- | ----------------- | ------------ | ----- | ---------------- | --- | ---------- | ------- |
| replacesthelabelsavingusedinopencoding. |       |           |          |           |           |               |      | 5.2. Dataanalysis |              |       |                  |     |            |         |
|                                         |       |           |          |           |           |               |      | In the            | analysis, we | aimed | at investigating |     | whether or | not the |
5. Resultstriangulation concepts depicted in Fig. 8 are also present and prominent in SO
|     |     |     |     |     |     |     |     | discussions. | For that, we | started | with filtering | cost-related | questions |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | ------- | -------------- | ------------ | --------- | --- |
Toverifyandstrengthenourfindings,wesoughttoinvestigatethe by searching the body, title, comments and history of all questions
andassociatedanswer(s)forthesamekeywordstemsusedforfiltering
extenttowhichtheidentifiedrelatedtopicsarealsodiscussedamong
commitmessages(seeSection3.3):bill,cheap,cost,efficient,
| developers | outside | GitHub. | In particular, | in  | this section, | we  | analyze |     |     |     |     |     |     |     |
| ---------- | ------- | ------- | -------------- | --- | ------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
expens,andpay.
| the discussions | of  | developers | in Stack | Overflow12 | (SO) | and | aim at |     |     |     |     |     |     |     |
| --------------- | --- | ---------- | -------- | ---------- | ---- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
thetriangulatingtheobservationsfromthisempiricalworkwiththose Next,wesearchedthesamefieldsmentionedaboveofeachfiltered
presented in Section 4.3. We start by presenting the data collection question for the properties documented in our knowledge graph (see
procedure, followed by the performed analysis, and concluding with Fig.8).Inthisprocess,weaugmentedeachquestionJSONfilewitha
theresultsandcomparisonagainstourpreviousobservations. listoffilteredsentencesthatcontainoneormoreoftheseproperties.
Finally,twooftheauthorsmanuallyinspectedarepresentativesample
5.1. Datacollection
|          |            |          |                |     |             |             |     | 13 https://archive.org/download/stack-exchange-data-dump-2023-09- |     |     |     |     |     |     |
| -------- | ---------- | -------- | -------------- | --- | ----------- | ----------- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| The data | collection | entailed | the extraction |     | of relevant | discussions |     |                                                                   |     |     |     |     |     |     |
12/stackoverflow.com-Posts.7z
| from SO. | For that, | we used | key datasets | from | the | September | 12, |                                                                   |     |     |     |     |     |     |
| -------- | --------- | ------- | ------------ | ---- | --- | --------- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|          |           |         |              |      |     |           |     | 14 https://archive.org/download/stack-exchange-data-dump-2023-09- |     |     |     |     |     |     |
12/stackoverflow.com-Comments.7z
|     |     |     |     |     |     |     |     | 15 https://archive.org/download/stack-exchange-data-dump-2023-09- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
12 https://stackoverflow.com/ 12/stackoverflow.com-PostHistory.7z
9

D.Feitosaetal.
TheJournalofSystems&Software215(2024)112112
|     |     |     |     |     |     |     | I am           | trying  | to       | reduce  | the cost        | of    | my AWS |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | -------- | ------- | --------------- | ----- | ------ |
|     |     |     |     |     |     |     | infrastructure |         | deployed |         | using Terraform |       | for    |
|     |     |     |     |     |     |     | a Django       | app.    | I        | have 2  | public subnets  |       | and 2  |
|     |     |     |     |     |     |     | private        | subnets |          | and in  | the subnets     | I     | deploy |
|     |     |     |     |     |     |     | NAT gateways   |         | and      | elastic | ips. all        | works | but is |
expensive.
|     |     |     |     |     |     |     | postid:#74422443 |     |     |     |     | label:nat |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --------- | --- |
Developersevenidentifycost-relatedfeaturesrequestedtobeadded
toTerraformasananswertoexistingproblems:
|     |     |     |     |     |     |     | Also | savings | plans | have | largely | replaced |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------- | ----- | ---- | ------- | -------- | --- |
reservedinstancesfornowsoIhadbetracking
|     |     |     |     |     |     |     | this                      | issue | https://github.com/hashicorp/terraform- |           |                 |         |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | ----- | --------------------------------------- | --------- | --------------- | ------- | --- |
|     |     |     |     |     |     |     | provider-aws/issues/10785 |       |                                         | if you    | are interesting |         | in  |
|     |     |     |     |     |     |     | support                   | for   | using                                   | Terraform | to manage       | savings |     |
plans.
label:provider
postid:#48751593
Fig.9. Co-occurrencesofactionandpropertyconceptsfromtheknowledgegraphof
Fig.8inStackOverflowquestionsandtheirassociatedanswers. Addingsentenceswheretheinitialkeywords(i.e.cost,bill,etc.)are
mentionedprovidesadditionalinsights:
|     |     |     |     |     |     |     | Since | licensing | of  | SQL Server | is  | expensive, | I   |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------- | --- | ---------- | --- | ---------- | --- |
wanttoswitchitoffatleastforthenight.
| of the questions | where | properties | were found | with | the goal | of estab- |                  |     |     |     |     |               |     |
| ---------------- | ----- | ---------- | ---------- | ---- | -------- | --------- | ---------------- | --- | --- | --- | --- | ------------- | --- |
|                  |       |            |            |      |          |           | postid:#76474230 |     |     |     |     | label:expense |     |
lishingtheaccuracyofthisprocess.Wenotethatthegenerateddataset
andusedscriptsarepubliclyavailable(Feitosaetal.,2024).
|     |     |     |     |     |     |     | I have | multiple |     | databases | running | in  | each |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --- | --------- | ------- | --- | ---- |
5.3. Resultsanddiscussion
|     |     |     |     |     |     |     | environment |        | which | are charging |              | me a | lot of |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ----- | ------------ | ------------ | ---- | ------ |
|     |     |     |     |     |     |     | cost each   | month, |       | so i wanted  | to downscale |      | the    |
Theinitialfiltering(usingkeywordsstems)returnedatotalof491 DTUs to some lower count during non-working
questions,i.e.,approx.2.6%ofallquestionsonSOwith‘terraform’in hours, again during working hours DTUs to be
any of the tags. Although the sample size may seem small compared upscale back to actual DTUs count, it should
happenautomaticallyaspertimesettingsevery
| to the entire | population | of  | Terraform-related | questions, | we  | note that |     |     |     |     |     |     |     |
| ------------- | ---------- | --- | ----------------- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
singleday.
thisisdoublethesamplesizecomparedtothatofGitHubrepositories
|     |     |     |     |     |     |     | postid:#74538381 |     |     |     |     | label:cost |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | ---------- | --- |
containingcost-relatedcommits(1.3%,2010outof152735containing
| Terraform artifacts; |     | see Section | 3.3). This | proportional | increase | may |     |     |     |     |     |     |     |
| -------------------- | --- | ----------- | ---------- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
befurtherindicativeofdevelopers’involvementwithandattentionto Someofthesediscussionspointtowardstheneedforarchitectural
cost-relateddecisions. refactoringasawayofaddressingcost-relatedconcerns:
Uponinspectingthesequestionsandtheiranswersforactionsand
|                 |     |           |           |         |          |          | If you | need | zero cost | during | idle | time, | should |
| --------------- | --- | --------- | --------- | ------- | -------- | -------- | ------ | ---- | --------- | ------ | ---- | ----- | ------ |
| properties from | our | knowledge | graph, we | learned | that 451 | (approx. |        |      |           |        |      |       |        |
yougowithserverlesswithnewdesign?
92%)ofthemmentiononeormoreoftheseconcepts.Inthediagonalof
Fig.9,weshowtheexactnumberofquestionsandassociatedanswers postid:#56530721 label:cost
| where each     | concept | was present | as a             | term. While | properties  | such |          |       |             |            |              |     |             |
| -------------- | ------- | ----------- | ---------------- | ----------- | ----------- | ---- | -------- | ----- | ----------- | ---------- | ------------ | --- | ----------- |
| as area appear | only    | once,       | other properties | such        | as provider | and  |          |       |             |            |              |     |             |
|                |         |             |                  |             |             |      | Aided by | these | highlighted | sentences, | we proceeded |     | to manually |
instance
(189 and 138 occurrences, respectively) but also actions inspectarepresentativesampleof37questions,16 consideringthatwe
| change |     |     | test |     |     |     |     |     |     |     |     |     |     |
| ------ | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
such as (199) and (154) are very popular. The same selected2.6%ofapopulationof19139questionswithTerraformtags.
questionanditsassociatedanswersmightcontainareferencetomore During the inspection, we aimed to verify whether: (1) the question
than one such concept. From these questions’ JSON file, we then indeedcontainedacost-relateddiscussion(eitherasthemainproblem
extracted3934sentencescontainingoneormoreoftheseconcepts. or as the element of a description or argument), and (2) one of the
Extractedsentencesshowcasedeveloperssharingtheirexperiences properties is an essential element of the identified cost-related text.
Asaresult,wefoundthatallinspectedquestionsweretruepositives.
indealingwithinsidiouscost-inducingtechnicalitiesinusingexisting
|     |     |     |     |     |     |     | These combined | observations |     | show that | the knowledge |     | graph cannot |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------ | --- | --------- | ------------- | --- | ------------ |
servicesoraskingforadviceinthisdirection:
onlybeusedtoidentifyactualpainpointsfacedbycloudapplication
Azure by itself discusses the challenge you developers,butitalsopointstothemostrecurrentones.
are addressing and recommends using ""data Basedontheco-occurrencesidentifiedinFig.9,weproceededtoin-
lifecycle"" for reducing the storage costs. vestigateifandhowtheknowledgegraphcouldbeaugmented.Wenote
[...] After you enable blob versioning for a thatthefrequencyoftheobservedco-occurrencesvariesgreatlywhile
storage account, every write operation to a also being positively skewed, i.e., many low co-occurrences (min.: 1,
blobinthataccountresultsinthecreationof Q1:2,Q2:5,Q3:12,max.:98).Followingourgoalofrepresentingthe
anewversion.
label:storage
postid:#72881767
|     |     |     |     |     |     |     | 16 https://www.calculator.net/sample-size-calculator.html?type=1&cl=95& |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
ci=5&pp=2.6&ps=491&x=Calculate
10

D.Feitosaetal.
TheJournalofSystems&Software215(2024)112112
Fig.10. Knowledgegraphupdatedbasedontheco-occurrencesofconceptsintheStackOverflowposts.
mostmeaningfulinformationintheknowledgegraph,weprocessedthe help practitioners avoid common mistakes and pitfalls in managing
co-occurrencefrequenciesasfollows: theiroperationalexpensesinthecloud.
Withrespecttotheresearchercommunity,ourfindingsdemonstrate
1. markpreexistinggraphedgesthatwerenotobservedasabsent;
|     |     |     |     |         |     |     | that there is | indeed | empirical | evidence | of software | developers |     | being |
| --- | --- | --- | --- | ------- | --- | --- | ------------- | ------ | --------- | -------- | ----------- | ---------- | --- | ----- |
|     |     |     |     | present |     | ≤   |               |        |           |          |             |            |     |       |
2. classify the observed co-occurrences into (𝑓 2), aware of the cost of their choices with respect to deploying their
| recurrent |     | ≤   | frequent |     | ≤   |     |     |     |     |     |     |     |     |     |
| --------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(2 < 𝑓 4), (4 < 𝑓 12) and softwareinthecloud.Thisevidenceiscorroboratedbythenumberof
predominant(12<𝑓)accordingtothefourquartiles; postsonStackOverflowdiscussingthetopicsweidentifiedasimportant
3. markpreexistinggraphedgesobservedinthedataaccordingto forcostawareness.Whilethisconclusionistheproductofprocessing
theirfrequencyclass(establishedinthepreviousstep);and only a specific type of artifacts in open source repositories and user
4. addnewgraphedgesforpredominantco-occurrencesthatwere forums,thereisnoreasontomakeusbelievethatthereisnofurther
notpresentinthepreviousversion. evidence to be uncovered when other types of artifacts, or even the
|     |     |     |     |     |     |     | software source | code | in the identified |     | repositories | in  | the dataset | is  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ---- | ----------------- | --- | ------------ | --- | ----------- | --- |
TheresultingknowledgegraphisdepictedinFig.10.Wenotethat examined. The findings of this study are therefore a call for further
the markings explained in the figure legend are aimed at helping the studiesoncostawarenessduringsoftwaredevelopment.
reader visualize the process. The augmented graph comprise all pre- More specifically, the following research items can be pursued by
existing edges with the addition of the new edges for predominant startingwithourexistingdataset:
co-occurrences.Lookingatthedifferencesandco-occurrencesfrequen-
|                  |               |         |              |                  |               |        | ➥ Provide | a finer-grain | analysis     | of     | the collected  | evidence    | looking   |        |
| ---------------- | ------------- | ------- | ------------ | ---------------- | ------------- | ------ | --------- | ------------- | ------------ | ------ | -------------- | ----------- | --------- | ------ |
| cies, while many | relationships | between | concepts     | are              | also observed | in     |           |               |              |        |                |             |           |        |
|                  |               |         |              |                  |               |        | at e.g.   | the commit    | contributors |        | and type       | of projects | involved. |        |
| this dataset,    | we learn two  | main    | lessons: (a) | the cost-related |               | topics |           |               |              |        |                |             |           |        |
|                  |               |         |              |                  |               |        | Combined, | for           | example,     | with a | practitioner’s | survey      | or        | inter- |
revolve mainly around the ability to try out different configurations views,itcanshedlightonhowdifferentdevelopmentteamsand
| test) |     |     |     | change), |     |     |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(i.e., andupdatingconfiguration (i.e., also meaning organizationsdealwithcost-relatedissues.
| thatcreatingsystemalertsisnotfrequentlydiscussed;and(b)discus- |     |     |     |     |     |     | ➥       |               |      |           |          |      |          |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | ------------- | ---- | --------- | -------- | ---- | -------- | --- |
|                                                                |     |     |     |     |     |     | Collect | and correlate | cost | awareness | evidence | from | the pull | re- |
sionsaremoreconcreteinthesensethattheygetmorespecificabout
|     |     |     |     |     |     |     | quests | (PRs) of | the identified | repositories. |     | PRs | can provide | the |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | -------------- | ------------- | --- | --- | ----------- | --- |
deploymentmatterssuchasfeaturesandbenefitsofproviders,e.g.,ap-
|                     |     |           |                   |     |           |      | missing | link between | commits | and | issues | and offer | further | in- |
| ------------------- | --- | --------- | ----------------- | --- | --------- | ---- | ------- | ------------ | ------- | --- | ------ | --------- | ------- | --- |
| propriate instances | and | policies. | The latter point, | in  | turn, led | to a |         |              |         |     |        |           |         |     |
sightsintothecostmanagementpractices.
| numberofnewrelationsbeingidentifiedbetween‘‘lowlevel’’concepts |     |     |     |     |     |     | ➥   |     |     |     |     |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Extendtheevidencesearchtoothercloudorchestratorsolutions,
inthegraph,e.g.,betweeninstanceandpolicyorcluster.
|     |     |     |     |     |     |     | both provider-agnostic |     | (e.g. | TOSCA17) | and | -specific | ones | (AWS |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | ----- | -------- | --- | --------- | ---- | ---- |
CloudFormation18),andcomparethefindings.Especiallyforthe
6. Implications&futurework latter, GitHub might not necessarily be the best data source for
|     |     |     |     |     |     |     | this purpose, |     | with the repositories |     | of (large) | organizations |     | and |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------------------- | --- | ---------- | ------------- | --- | --- |
Thepresentedfindingshaveimplicationsforbothpractitionersand enterpriseswithmaturecloudpresenceovertheyearsbeingmuch
moreattractivesourcesofdata.
academicresearchers.Withrespecttotheformer,itbecomesclearthat
|     |     |     |     |     |     |     | ➥ Apply | natural | language processing |     | and other | machine | learning |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------------------- | --- | --------- | ------- | -------- | --- |
costawarenessshouldactuallybepresent,ifitisnotalready,through-
|     |     |     |     |     |     |     | techniques | such | as sentiment | analysis | to  | gain | further insights |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ------------ | -------- | --- | ---- | ---------------- | --- |
outthedevelopmentofcloud-basedapplications.Ourdatasetcontains
|                   |               |     |                  |       |            |     | into the | reasoning | of the | developers. | Sentiment |          | analysis | in par- |
| ----------------- | ------------- | --- | ---------------- | ----- | ---------- | --- | -------- | --------- | ------ | ----------- | --------- | -------- | -------- | ------- |
| multiple examples | of developers |     | rushing to adapt | their | deployment |     |          |           |        |             |           |          |          |         |
|                   |               |     |                  |       |            |     | ticular  | has been  | shown  | to be       | a mixed   | bag when | software | is      |
configurationstodealwithprohibitivecosts,orintentionallydesigning
concerned(Linetal.,2022),butwiththetrainingoftheanalyzer
theirdeploymentwiththeclearintentionofavoidingthem,particularly
focusedoncloudorchestratorartifactsandtheirassociatedcom-
whenspecificcloudservicesareinvolved.Moreimportantly,thereare
|               |            |         |                   |     |          |       | mit messages |     | and issue discussions, |     | it might | be  | possible | to get |
| ------------- | ---------- | ------- | ----------------- | --- | -------- | ----- | ------------ | --- | ---------------------- | --- | -------- | --- | -------- | ------ |
| specific pain | points and | actions | that can be taken | for | reducing | costs |              |     |                        |     |          |     |          |        |
betterresultsthroughthetighterscope.
inthesecasesandlessonslearnedbyotherdeveloperstobeextracted
byinvestigatingourcurateddataset.Lookingatthequestionspostedon
StackOverflowonthetopic,andthecorrespondinganswers,itbecomes 17 https://docs.oasis-open.org/tosca/TOSCA/v1.0/TOSCA-v1.0.html
clear that having such knowledge in advance at their disposal would 18 https://aws.amazon.com/cloudformation/
11

D.Feitosaetal. TheJournalofSystems&Software215(2024)112112
➥ Lookforsimilarevidenceinothertypesofartifacts,forexample 8. Conclusions
other configuration files, and/or in closed source repositories,
e.g. of large software-intensive organizations and enterprises. Managing the operational expenses of deploying software in the
This search can go beyond cloud-based software, or at least cloudisamajorchallengefororganizations.However,howpractition-
public cloud deployments, and incorporate also the wealth of ersapproachthistopichassofarbeentreatedbytheliteratureinan
DevOpstoolsavailableforautomatingsoftwaredeploymentand anecdotalandthereforenonsystematicmanner.Consequently,andasa
management. firststep,inthisworkweinvestigatedwhetherthereis(empirical)ev-
➥ Lookalsointhesourcecodeofrepositories,startingwiththeones idenceofsoftwaredevelopersbeingawareoftheoperationalexpenses
alreadycontainingcost-awareorchestrationartifactsaseasierto ofdeployinganddeliveringsoftwareinthecloud,andifyes,thenwhat
reach targets. This is an obvious extension of the current work, kindofinformationcanbeextractedfromthisevidenceandhowthis
but will need a wide experience with multiple programming
informationcanbeorganizedforfurtherstudy.
languagesandplatformsonbehalfoftheresearchers.
Given the wide scope and previously unexamined nature of these
➥ UsetheextractedpostsfromStackOverflowtoextendthelistof
questions,atleastfromanMSRperspective,westartedtacklingthem
topicsrelatedtocostawareness,andupdatetheknowledgegraph
by focusing on cloud orchestrator descriptor files. We chose reposi-
ofFig.8accordingly.
tory mining as our methodology, and designed and executed the first
➥ Organizethecollectedinformationintoreusableknowledgecon-
suchstudysearchingforevidenceinopensourcecoderepositorieson
cerningthebestpracticesofmanagingtheoperationalexpenses
GitHub that contain Terraform orchestration artifacts, a very popular
ofcloud-basedsoftware.Inasense,thiswouldbetheoutcomeof
provider-agnosticIaCtool.
thisresearchagendawiththemostimpacttothewidercommu-
Oursearchwasshowntobesuccessful,insofarasitactuallyallowed
nity.
ustoretrieveandorganizeinadatasetnotonlyevidenceofcostaware-
Westronglybelievethatthisisonlythefirststudyofmanytocome ness by software developers, but also of specific actions being taken
onthisparticulartopic. as a result. More specifically, with respect to extracting information
fromcommitmessagesintheselectedrepositories(RQ ),ourfindings
1
7. Threatstovalidity showthatthemostpopulartopicsdominatingthedeveloperdiscourse
isnotlimitedtobeingawareofthepotentialoractualcostofdeploying
Likeanyotherempiricalstudyinsoftwareengineering,thiswork’s
and operating the system in the cloud. Developers seem also to not
validityisalsothreatened(andthesethreatsmitigated)inseveralways.
onlybetakingconcreteactionstominimizethiscost,butalsotoavoid
Themainthreatstothisworkarediscussedinthefollowing.
excessive charging to occur when e.g. using specific cloud services
External Validity: Regarding external validity, the population in
and/or offerings within them. Processing cost-related issues from the
our data sets (from GitHub and Stack Overflow) may not represent
same repositories (RQ ) did not reveal any additional information in
allpossiblecost-relateddiscussionsincloudprojects.Theinclusionof 2
terms of identified topics of discussion. It did however offer further
repositorieshostedinother(closed-source)platforms,orthatuseother
insights into the decision-making process entailed in managing cloud
cloud orchestrators, or that use no cloud orchestrators, could lead to
coststhatcanbepursuedfurtherinfuturework.
theidentificationofnewdiscussions.Theinclusionofdiscussionforums
otherthanStackOverflowcouldalsoleadtonewdiscussions.However, Enriching and organizing the extracted information from the pre-
ourdecisionswerecarefullyconsideredwiththeaimofensuringdata vious steps into a knowledge graph (RQ 3 ) helped us identify both
quality, diversity and quantity while keeping the execution feasible higher-level, recurring concepts such as awareness, and specific pain
for the available human resources. Furthermore, our goal was not to points such CPU and RAM (sizes) in the deployment and operation
collect all possible evidence, to begin with, but rather to see if there of cloud-based software that dominate the developers’ discussions.
isanyevidenceavailable.Thatsaid,theresultstriangulation(between Thefollow-uptriangulationwithStackOverflowTerraformdiscussions
GitHub- and Stack Overflow-based discussions) helps mitigate threats that address cost concerns corroborates these pain points and their
toexternalvalidity. prevalenceinthespectrumofdiscussiontopics.
ConstructValidity:Theselectioncriteria,andmostnoticeablythe Finally,basedonthatevidenceandthelimitationsofthisworkwe
defined keywords may threat the construct validity of our work. We developedalistoffutureresearchitemswhichbothprovidesuswith
mitigatedthisthreatbypilotingandtestingourselectioncriteria,and a clear roadmap for future work, and offers to the wider community
considering the knowledge of both academic and industrial domain an opportunity to develop a new research topic at the intersection of
experts. Furthermore, the coding activity is naturally open to sub- miningsoftwarerepositoriesandcloudcomputing.
jectivity and inconsistencies. To mitigate this threat, we followed a
well-establishedprocess,andintroducedanextrafinalsteptoconsol- CRediTauthorshipcontributionstatement
idate the knowledge and systematically discuss the labels. Also, the
topicsderivedfromapplyingLDAmaynotfullyrepresenttheircontent.
Daniel Feitosa: Writing – original draft, Validation, Supervision,
We mitigate this threat by manually inspecting the units of analysis
Software, Methodology, Formal analysis, Data Curation, Conceptual-
during the investigation of RQ , which was part of the axial coding
3 ization. Matei-Tudor Penca: Software, Formal analysis, Data cura-
andselectivecoding.Thisthreatisalsomitigatedbythetriangulation
tion.MassimilianoBerardi:Software,Formalanalysis,Datacuration.
presented in Section 5. That said, we acknowledge that the Stack
Rares-Dorian Boza: Software, Formal analysis, Data curation. Vasil-
Overflowstudyitselfsuffersfromitsownthreatstoconstructvalidity,
ios Andrikopoulos: Writing – original draft, Validation, Supervision,
mainlyrelatedtoselectionofappropriatedatapoints,i.e.,pertainingto
Methodology,Conceptualization.
cost-relateddiscussionofTerraform-baseddeployments.Themitigation
strategiesinthiscaseentailtheuseofTerraform-relatedtagsthathave
Declarationofcompetinginterest
beenassignedbyusers,ontopofusingpreviously-validatedkeywords
forsearchingcost-relatedentrieswithinthefilteredposts.
Reliability: Finally, to mitigate threats to the reliability of the The authors declare that they have no known competing finan-
study,wehavedescribedthedataacquisitionprocessinasmuchdetail cial interests or personal relationships that could have appeared to
aspossible.Moreimportantly,thedatasetcuratedthroughourefforts influencetheworkreportedinthispaper.
is publicly available (Feitosa et al., 2024) together with the scripts
to aid the replication the data collection and topic modeling tasks. Dataavailability
Thispackagealsoincludesthedatasetandscriptsusedfortheresults
triangulationwithStackOverflowquestions. Wehavesharedthelinktomydataandcodeinthemanuscript.
12

D.Feitosaetal.
TheJournalofSystems&Software215(2024)112112
Acknowledgments Hindle, A., 2013. Green mining: A methodology of relating software change and
|     |     |     |     |     |     |     | configuration | to  | power consumption. |     | Empir. Softw. | Eng. | 20 (2), | 374–409. http: |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------------ | --- | ------------- | ---- | ------- | -------------- |
TheauthorswouldliketothankDiomidisSpinellisforprovidingthe //dx.doi.org/10.1007/s10664-013-9276-6.
inspirationforthiswork. Hindle,A.,Ernst,N.A.,Godfrey,M.W.,Mylopoulos,J.,2011.Automatedtopicnaming
tosupportcross-projectanalysisofsoftwaremaintenanceactivities.In:Proceedings
|     |     |     |     |     |     |     | of the | 8th Working | Conference | on  | Mining Software |     | Repositories. | MSR, ACM, |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | ---------- | --- | --------------- | --- | ------------- | --------- |
References
|     |     |     |     |     |     |     | Waikiki, | Honolulu, | HI, USA, | pp. 163–172. | http://dx.doi.org/10.1145/1985441. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | -------- | ------------ | ---------------------------------- | --- | --- | --- |
1985466.
| Abdellatif, A., | Costa, D., | Badran, K., | Abdalkareem, | R., Shihab, | E., 2020. Challenges |     |     |     |     |     |     |     |     |     |
| --------------- | ---------- | ----------- | ------------ | ----------- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Hoffman,M.,Bach,F.,Blei,D.,2010.OnlinelearningforlatentDirichletallocation.
in chatbot development: A study of stack overflow posts. In: Proceedings of the In: Lafferty, J., Williams, C., Shawe-Taylor, J., Zemel, R., Culotta, A. (Eds.), In:
17thInternationalConferenceonMiningSoftwareRepositories.MSR,ACM,Seoul, Advances in Neural Information Processing Systems, vol. 23, Curran Associates,
| RepublicofKorea,pp.174–185.http://dx.doi.org/10.1145/3379597.3387472. |     |     |     |     |     |     | Inc.. |     |     |     |     |     |     |     |
| --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
Ahmed, S., Bagherzadeh, M., 2018. What do concurrency developers ask about? A Hosseinzadeh,M.,Hama,H.K.,Ghafour,M.Y.,Masdari,M.,Ahmed,O.H.,Khezri,H.,
| large-scale | study using | stack overflow. | In: Proceedings | of  | the 12th ACM/IEEE |     |               |           |       |                |          |         |     |               |
| ----------- | ----------- | --------------- | --------------- | --- | ----------------- | --- | ------------- | --------- | ----- | -------------- | -------- | ------- | --- | ------------- |
|             |             |                 |                 |     |                   |     | 2020. Service | selection | using | multi-criteria | decision | making: | A   | comprehensive |
International Symposium on Empirical Software Engineering and Measurement. overview.J.Netw.Syst.Manage.28(4),1639–1693.
ACM,Oulu,Finland,http://dx.doi.org/10.1145/3239235.3239524. Howard, M.J., Gupta, S., Pollock, L., Vijay-Shanker, K., 2013. Automatically mining
Al Alamin, M.A., Malakar, S., Uddin, G., Afroz, S., Haider, T.B., Iqbal, A., 2021. software-based,semantically-similarwordsfromcomment-codemappings.In:Pro-
| An empirical | study of | developer | discussions on | low-code software | development |     |     |     |     |     |     |     |     |     |
| ------------ | -------- | --------- | -------------- | ----------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ceedingsofthe10thWorkingConferenceonMiningSoftwareRepositories.IEEE,
| challenges.In:2021IEEE/ACM18thInternationalConferenceonMiningSoftware |     |     |     |     |     |     | pp.377–386. |     |     |     |     |     |     |     |
| --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Repositories.MSR,pp.46–57.http://dx.doi.org/10.1109/MSR52588.2021.00018. Jamshidi,P.,Ahmad,A.,Pahl,C.,2013.Cloudmigrationresearch:Asystematicreview.
Amato, A., Venticinque, S., 2016. Multiobjective optimization for brokering of IEEETrans.CloudComput.1(2),142–157.
multicloudservicecomposition.ACMTrans.InternetTechnol.(TOIT)16(2),1–20.
|     |     |     |     |     |     |     | Kovács, J., | Kacsuk, | P., 2017. Occopus: |     | A multi-cloud | orchestrator |     | to deploy and |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ------------------ | --- | ------------- | ------------ | --- | ------------- |
Andrikopoulos,V.,Binz,T.,Leymann,F.,Strauch,S.,2013.Howtoadaptapplications
|     |     |     |     |     |     |     | manage | complex | scientific infrastructures. |     | J. Grid | Comput. | 16 (1), | 19–37. http: |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | --------------------------- | --- | ------- | ------- | ------- | ------------ |
forthecloudenvironment.Computing95(6),493–535.http://dx.doi.org/10.1007/ //dx.doi.org/10.1007/s10723-017-9421-3.
s00607-012-0248-2. LeClair, A., Eberhart, Z., McMillan, C., 2018. Adapting neural text classification for
| Armbrust, M., | Fox, A., Griffith, | R., Joseph, | A.D., Katz,       | R., Konwinski, | A.,                 | Lee, G., |          |             |                 |            |           |                                  |     |               |
| ------------- | ------------------ | ----------- | ----------------- | -------------- | ------------------- | -------- | -------- | ----------- | --------------- | ---------- | --------- | -------------------------------- | --- | ------------- |
|               |                    |             |                   |                |                     |          | improved | software    | categorization. | In:        | 2018 IEEE | International                    |     | Conference on |
| Patterson,    | D., Rabkin,        | A., Stoica, | I., et al., 2010. | A view         | of cloud computing. |          |          |             |                 |            |           |                                  |     |               |
|               |                    |             |                   |                |                     |          | Software | Maintenance | and             | Evolution. | ICSME,    | IEEE, http://dx.doi.org/10.1109/ |     |               |
Commun.ACM53(4),50–58.
icsme.2018.00056.
Arunarani,A.,Manjula,D.,Sugumaran,V.,2019.Taskschedulingtechniquesincloud Lex,A.,Gehlenborg,N.,Strobelt,H.,Vuillemot,R.,Pfister,H.,2014.UpSet:Visualiza-
computing:Aliteraturesurvey.FutureGener.Comput.Syst.91,407–415.
tionofintersectingsets.IEEETrans.Visual.Comput.Graph.20(12),1983–1992.
Bao,L.,Lo,D.,Xia,X.,Wang,X.,Tian,C.,2016.Howandroidappdevelopersmanage
http://dx.doi.org/10.1109/tvcg.2014.2346248.
| power consumption? |     | In: Proceedings | of the 13th | International | Conference | on  |     |     |     |     |     |     |     |     |
| ------------------ | --- | --------------- | ----------- | ------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Lin,B.,Cassee,N.,Serebrenik,A.,Bavota,G.,Novielli,N.,Lanza,M.,2022.Opinion
MiningSoftwareRepositories.ACM,http://dx.doi.org/10.1145/2901739.2901748. miningforsoftwaredevelopment:Asystematicliteraturereview.ACMTrans.Softw.
Blei,D.M.,2010.Probabilistictopicmodels.IEEESignalProcess.Mag.27,55–65. Eng.Methodol.31(3),http://dx.doi.org/10.1145/3490388.
| Campbell, J.C., | Hindle, A., | Stroulia, E., | 2015. Latent | Dirichlet | allocation: | Extracting |     |     |     |     |     |     |     |     |
| --------------- | ----------- | ------------- | ------------ | --------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Mell,P.,Grance,T.,etal.,2011.TheNISTdefinitionofcloudcomputing.NISTSpecial
topicsfromsoftwareengineeringdata.In:TheArtandScienceofAnalyzingSoft-
Publication800-145.
| ware Data. | Elsevier, pp. | 139–159. | http://dx.doi.org/10.1016/b978-0-12-411519- |     |     |     |                   |     |                    |     |              |              |     |              |
| ---------- | ------------- | -------- | ------------------------------------------- | --- | --- | --- | ----------------- | --- | ------------------ | --- | ------------ | ------------ | --- | ------------ |
|            |               |          |                                             |     |     |     | Moura, I., Pinto, | G., | Ebert, F., Castor, | F., | 2015. Mining | energy-aware |     | commits. In: |
4.00006-9. 2015IEEE/ACM12thWorkingConferenceonMiningSoftwareRepositories.IEEE,
Chauhan,M.A.,Babar,M.A.,Benatallah,B.,2017.Architectingcloud-enabledsystems:
http://dx.doi.org/10.1109/msr.2015.13.
| A systematic | survey | of challenges | and solutions. | Softw. - | Pract. Exp. | 47 (4), |     |     |     |     |     |     |     |     |
| ------------ | ------ | ------------- | -------------- | -------- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Pereira,R.,Matalonga,H.,Couto,M.,Castor,F.,Cabral,B.,Carvalho,P.,deSousa,S.M.,
599–644.
|                      |       |           |             |             |            |          | Fernandes, | J.P., | 2021. GreenHub: | A   | large-scale | collaborative | dataset | to battery |
| -------------------- | ----- | --------- | ----------- | ----------- | ---------- | -------- | ---------- | ----- | --------------- | --- | ----------- | ------------- | ------- | ---------- |
| Chen, T.-H., Thomas, | S.W., | Nagappan, | M., Hassan, | A.E., 2012. | Explaining | software |            |       |                 |     |             |               |         |            |
defects using topic models. In: Proceedings of the 9th IEEE Working Conference consumption analysis of android devices. Empir. Softw. Eng. 26 (3), http://dx.
doi.org/10.1007/s10664-020-09925-5.
| on Mining | Software Repositories. |     | MSR, pp. 189–198. | http://dx.doi.org/10.1109/ |     |     |                    |     |            |              |           |       |          |             |
| --------- | ---------------------- | --- | ----------------- | -------------------------- | --- | --- | ------------------ | --- | ---------- | ------------ | --------- | ----- | -------- | ----------- |
|           |                        |     |                   |                            |     |     | Pinto, G., Castor, | F., | Liu, Y.D., | 2014. Mining | questions | about | software | energy con- |
MSR.2012.6224280.
|     |     |     |     |     |     |     | sumption. | In: Proceedings | of  | the 11th | Working | Conference | on Mining | Software |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------------- | --- | -------- | ------- | ---------- | --------- | -------- |
Choetkiertikul,M.,Dam,H.K.,Tran,T.,Ghose,A.,2015.Characterizationandpredic-
tionofissue-relatedrisksinsoftwareprojects.In:Proceedingsofthe12thWorking Repositories.pp.22–31.
ConferenceonMiningSoftwareRepositories.IEEE,pp.280–291. Qi,P.,Zhang,Y.,Zhang,Y.,Bolton,J.,Manning,C.D.,2020.Stanza:APythonnatural
|     |     |     |     |     |     |     | language | processing | toolkit | for many | human | languages. | In: Proceedings | of the |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ------- | -------- | ----- | ---------- | --------------- | ------ |
Choetkiertikul,M.,Dam,H.K.,Tran,T.,Ghose,A.,Grundy,J.,2018.Predictingdelivery
|                                                     |              |                       |      |        |             |         | 58th Annual     | Meeting | of the | Association | for | Computational | Linguistics: | System |
| --------------------------------------------------- | ------------ | --------------------- | ---- | ------ | ----------- | ------- | --------------- | ------- | ------ | ----------- | --- | ------------- | ------------ | ------ |
| capability                                          | in iterative | software development. | IEEE | Trans. | Softw. Eng. | 44 (6), |                 |         |        |             |     |               |              |        |
| 551–573.http://dx.doi.org/10.1109/tse.2017.2693989. |              |                       |      |        |             |         | Demonstrations. |         |        |             |     |               |              |        |
Cong,P.,Xu,G.,Wei,T.,Li,K.,2020.Asurveyofprofitoptimizationtechniquesfor Reboucas, M., Pinto, G., Ebert, F., Torres, W., Serebrenik, A., Castor, F., 2016. An
empiricalstudyontheusageoftheSwiftprogramminglanguage.In:Proceedings
cloudproviders.ACMComput.Surv.(CSUR)53(2),1–35.
|     |     |     |     |     |     |     | of the IEEE | 23rd | International | Conference | on  | Software | Analysis, | Evolution, and |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ------------- | ---------- | --- | -------- | --------- | -------------- |
Corbin,J.,Strauss,A.,2014.BasicsofQualitativeResearch:TechniquesandProcedures
Reengineering.SANER,IEEE,http://dx.doi.org/10.1109/saner.2016.66.
forDevelopingGroundedTheory.SAGEPublications.
daCosta,D.A.,McIntosh,S.,Treude,C.,Kulesza,U.,Hassan,A.E.,2017.Theimpact Sas,C.,Capiluppi,A.,2022.Antipatternsinsoftwareclassificationtaxonomies.J.Syst.
ofrapidreleasecyclesontheintegrationdelayoffixedissues.Empir.Softw.Eng. Softw.190,111343.http://dx.doi.org/10.1016/j.jss.2022.111343.
|     |     |     |     |     |     |     | Shuaib, M., | Samad, | A., Alam, S., | Siddiqui, | S.T., 2019. | Why | adopting | cloud is still a |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ------------- | --------- | ----------- | --- | -------- | ---------------- |
23(2),835–904.http://dx.doi.org/10.1007/s10664-017-9548-7.
challenge?—Areviewonissuesandchallengesforcloudmigrationinorganizations.
Das,T.,DiPenta,M.,Malavolta,I.,2016.Aquantitativeandqualitativeinvestigation
of performance-related commits in android apps. In: 2016 IEEE International In:AmbientCommunicationsandComputerSystems.Springer,pp.387–399.
ConferenceonSoftwareMaintenanceandEvolution.ICSME,IEEE,pp.443–447. Spadini,D.,Aniche,M.,Bacchelli,A.,2018.PyDriller:Pythonframeworkformining
de Carvalho, L.R., de Araujo, A.P.F., 2020. Performance comparison of terraform software repositories. In: Proceedings of the 2018 26th ACM Joint Meeting on
|              |               |                |          |               |               |     | European | Software | Engineering | Conference | and | Symposium | on the | Foundations |
| ------------ | ------------- | -------------- | -------- | ------------- | ------------- | --- | -------- | -------- | ----------- | ---------- | --- | --------- | ------ | ----------- |
| and cloudify | as multicloud | orchestrators. | In: 2020 | 20th IEEE/ACM | International |     |          |          |             |            |     |           |        |             |
Symposium on Cluster, Cloud and Internet Computing. CCGRID, IEEE, http://dx. of Software Engineering. ESEC/FSE 2018, ACM, New York, New York, USA, pp.
doi.org/10.1109/ccgrid49817.2020.00-55. 908–911. http://dx.doi.org/10.1145/3236024.3264598, URL: https://github.com/
Dueñas,S.,Cosentino,V.,Robles,G.,Gonzalez-Barahona,J.M.,2018.Perceval:Software ishepard/pydriller.
|     |     |     |     |     |     |     | Tomarchio, | O., Calcaterra, | D., Modica, | G.D., | 2020. | Cloud | resource orchestration | in  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | ----------- | ----- | ----- | ----- | ---------------------- | --- |
projectdataatyourwill.In:Proceedingsofthe40thInternationalConferenceon
SoftwareEngineering:CompanionProceedings.ICSE-C,ACM,Gothenburg,Sweden, the multi-cloud landscape: A systematic review of existing frameworks. J. Cloud
pp. 1–4. http://dx.doi.org/10.1145/3183440.3183475, URL: https://github.com/ Comput.9(1),1–24.
chaoss/grimoirelab-perceval. Treude, C., Wagner, M., 2019. Predicting good configurations for GitHub and stack
Feitosa, D., Penca, M.-T., Berardi, M., Boza, R.-D., Andrikopoulos, V., 2024. Supple- overflowtopicmodels.In:ProceedingsoftheIEEE/ACM16thInternationalCon-
mentarymaterialforminingcostawarenessintheinfrastructureascodeartifacts ference on Mining Software Repositories. MSR, IEEE, http://dx.doi.org/10.1109/
| ofcloud-basedapplications.http://dx.doi.org/10.5281/zenodo.11312689. |     |     |     |     |     |     | msr.2019.00022. |     |     |     |     |     |     |     |
| -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
Han, J., Shihab, E., Wan, Z., Deng, S., Xia, X., 2020. What do programmers discuss Tricomi,G.,Merlino,G.,Panarello,A.,Puliafito,A.,2020.Optimalselectiontechniques
about deep learning frameworks. Empir. Softw. Eng. 25 (4), 2694–2747. http: forcloudserviceproviders.IEEEAccess8,203591–203618.
//dx.doi.org/10.1007/s10664-020-09819-6. Vakili,A.,Navimipour,N.J.,2017.Comprehensiveandsystematicreviewoftheservice
Harms, R., Yamartino, M., 2010. The economics of the cloud. Microsoft whitepaper, composition mechanisms in the cloud environments. J. Netw. Comput. Appl. 81,
| MicrosoftCorporation. |     |     |     |     |     |     | 24–36. |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
13

D.Feitosaetal.
TheJournalofSystems&Software215(2024)112112
Řehůřek, R., Sojka, P., 2010. Software framework for topic modelling with large specificallyinLLMagents,informationretrievalanddataminingwithinthelifesciences
corpora.In:ProceedingsoftheLREC2010WorkshoponNewChallengesforNLP domain.Mateiiscommittedtointegratingthelatestresearchtechnologiesforoptimized
Frameworks.ELRA,Valletta,Malta,pp.45–50. data-drivenapplications.
| Wohlin, C.,     | Runeson, P., Höst, | M., Ohlsson, M.,          | Regnell, B., | Wesslén, A., 2012. |     |     |     |     |     |     |
| --------------- | ------------------ | ------------------------- | ------------ | ------------------ | --- | --- | --- | --- | --- | --- |
| Experimentation | in Software        | Engineering. In: Computer | Science,     | Springer Berlin,   |     |     |     |     |     |     |
Heidelberg. MassimilianoBerardiisarecentgraduateofComputingSciencefromtheUniversityof
Groningen,wherehealsocontributedasateachingassistantforvariouscourses.Heis
Zimmerle,C.,Gama,K.,Castor,F.,Filho,J.M.M.,2022.Miningtheusageofreactive
currentlyworkingasaSoftwareEngineeratSyntho,astartupspecializinginsynthetic
| programming | APIs: A study | on GitHub and | stack overflow. | In: Proceedings |                  |     |              |                     |                           |     |
| ----------- | ------------- | ------------- | --------------- | --------------- | ---------------- | --- | ------------ | ------------------- | ------------------------- | --- |
|             |               |               |                 |                 | data generation. | His | expertise in | database management | and software architecture | is  |
of the 19th International Conference on Mining Software Repositories. MSR, employedinimprovingtheirproductandgrowingasacompany.
ACM,Pittsburgh,Pennsylvania,pp.203–214.http://dx.doi.org/10.1145/3524842.
3527966.
|     |     |     |     |     | Rareş-Dorian | Boza   | is pursuing an    | M.Sc. in Computer | Science at Delft University | of         |
| --- | --- | --- | --- | --- | ------------ | ------ | ----------------- | ----------------- | --------------------------- | ---------- |
|     |     |     |     |     | Technology,  | having | previously earned | his B.Sc. from    | the University of           | Groningen, |
Daniel Feitosa is an assistant professor at the University of Groningen, where he alongsidethecompletionoftheHonoursCollegeprogramme.Currently,heisdelving
|                |                          |                         |               |                      | into natural            | language | processing | solutions, software | architecture, and information |           |
| -------------- | ------------------------ | ----------------------- | ------------- | -------------------- | ----------------------- | -------- | ---------- | ------------------- | ----------------------------- | --------- |
| contributes to | the Software Engineering | and Architecture        | group         | within the Bernoulli |                         |          |            |                     |                               |           |
|                |                          |                         |               |                      | retrieval, specifically |          | in the use | case of recommender | systems. Alongside            | academia, |
| Institute for  | Mathematics, Computer    | Science, and Artificial | Intelligence. | Earning his          |                         |          |            |                     |                               |           |
RareşisengagedasasoftwaretoolinginternforIntel’sdepartmentinEindhoven.
| Ph.D. from | the same university, | Daniel’s research | interests are | rooted in software |     |     |     |     |     |     |
| ---------- | -------------------- | ----------------- | ------------- | ------------------ | --- | --- | --- | --- | --- | --- |
quality,miningsoftwarerepositories,anddeveloperexperience,especiallyappliedto
technicaldebtmanagement,andenergyefficiency.HehasparticipatedinEU-funded
VasiliosAndrikopoulosisassociateprofessorattheUniversityofGroningen,anda
project, such as SDK4ED, and is an active member of various software engineering memberoftheSoftwareEngineeringandArchitecturegroupintheBernoulliInstitute
| communities, | having served as a | program committee | member | in several conferences |                  |          |         |                              |             |           |
| ------------ | ------------------ | ----------------- | ------ | ---------------------- | ---------------- | -------- | ------- | ---------------------------- | ----------- | --------- |
|              |                    |                   |        |                        | for Mathematics, | Computer | Science | and Artificial Intelligence. | He received | his Ph.D. |
andrefereeformultiplejournals.
|     |     |     |     |     | from Tilburg | University, | the Netherlands, | and he has | worked as a post-doc | for both |
| --- | --- | --- | --- | --- | ------------ | ----------- | ---------------- | ---------- | -------------------- | -------- |
TilburgUniversityandtheUniversityofStuttgart,Germany.Hisresearchinterestsarein
softwarearchitecturesforcloud-basedsystems,withanemphasisontheirsustainability
| Matei Tudor | Penca is a Data Scientist | at Elsevier, | a scientific | publisher and data |            |                 |        |                   |                     |           |
| ----------- | ------------------------- | ------------ | ------------ | ------------------ | ---------- | --------------- | ------ | ----------------- | ------------------- | --------- |
|             |                           |              |              |                    | across all | its dimensions. | He has | participated in a | number of EU-funded | projects, |
analyticscompany,wherehecontributestotheDataScienceLifeSciencesdepartment
oftheAmsterdamteam.HeholdsaMaster’sdegreeinInformationStudies:DataScience including the Network of Excellence S-Cube, and is reviewing for a multitude of
journals.
| from the University | of Amsterdam. | His expertise lies | in natural | language processing, |     |     |     |     |     |     |
| ------------------- | ------------- | ------------------ | ---------- | -------------------- | --- | --- | --- | --- | --- | --- |
14