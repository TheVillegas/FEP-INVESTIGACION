MathematicalandComputerModelling53(2011)504–521
ContentslistsavailableatScienceDirect
Mathematical and Computer Modelling
journalhomepage:www.elsevier.com/locate/mcm
Identification of a company’s suitability for the adoption of cloud
computing and modelling its corresponding Return on Investment
SubhasChandraMisra ∗ ,ArkaMondal1
DepartmentofIndustrialandManagementEngineering,IndianInstituteofTechnology,Kanpur,India
a r t i c l e i n f o a b s t r a c t
Articlehistory: Internethasbecomepervasiveinourdailylifeandcloudcomputingisthenewestoffering
Received1November2009 asserviceovertheubiquitousWeb.Cloudcomputinghasbeenconsideredasamuchhyped
Receivedinrevisedform15March2010 phenomenonintheITandbusinessworldpromisingtodeliverahostofbenefits.Compa-
Accepted16March2010
niesneedtolookbeyondthishypeandseriouslyconsidertherealvalueofincorporating
theCloudintheirownbusinesses.Thispaperisaimedathelpingcompaniesanalyzeseveral
Keywords:
characteristicsoftheirownbusinessaswellaspre-existingITresourcestoidentifytheirfa-
Cloudcomputing
vorabilityinthemigrationtotheCloudArchitecture.AgeneralReturnonInvestment(ROI)
ReturnonInvestment(ROI)
modelhasalsobeendevelopedheretakingintoconsiderationvariousintangibleimpacts
Benefitsofcloudcomputing
Costofcloudcomputing ofCloudComputing,apartfromthecost.Theanalysispresentedhereinprovidesamuch
broaderperspectiveandinsightintoCloudComputingtoitsprospectiveadopters.
©2010ElsevierLtd.Allrightsreserved.
1. Introduction
Cloudcomputing(CC)[1]isaparadigmshiftincomputingwiththepotentialofchangingthewholeperspectivewith
whichwelookatcomputingtoday.Currently,desktops,laptopsandnumeroussuchdeviceshavepenetratedintoourdaily
livesandhavebecomeindispensable[2].Itwillnotbetoolongfromnowthatallwewillneedtoknowisthatthereis
onehugecomputerataremotelocation(withoutevenknowingwhereitis)whichhasthepotentialtoprovideallthe
computationalpowerandresourcesthatweeverreallyneed.
CCcanbedefinedascollectiondisembodiedservicesaccessiblefromanywhereusinganymobiledevicewithanInternet
connection, provided by a type of parallel and distributed system of virtualized computers that are interconnected and
thatcanbedynamicallyprovisionedandpresentedasoneormoreunifiedcomputingresourcesbasedonService-Level
Agreements(SLAs)establishedbetweentheserviceproviderandtheuser[3–5].
Inthispaper,weanalyzesomeoftheeconomicaspectsofmigrationtocloudarchitecture.Specifically,weattemptto
modelROIinusingCCinorganizations.Studiesoftheeconomicaspects,ingeneral,andROI,inparticular,areimportant
organizationalconsiderationsintheadoptionofanynewtechnology.InthecontextofGridComputing[6,7],forexample,
works(e.g.,[8–16])relatingtotheseaspectsexist.AsCCisanimportanttechnologicaltrend,itisalsoimportanttostudy
theseeconomicaspectsofCC.
Therearedifferentclouddeliverymodels(e.g.,[3,17,18])basedonpay-per-usemodels,viz.,Software-as-a-Service(SaaS),
Platform-as-a-Service (PaaS) and Infrastructure-as-a-Service (IaaS). Software-as-a-Service (SaaS) may be described as a
processbywhichdifferentsoftwareapplicationsareprovidedbytheApplicationServiceProvider(ASP)asarentalover
the Internet leveraging cloud infrastructure. This eliminates the necessity for installing and running the application on
thecustomer’sowncomputer.Italsodiminishesthetremendousloadofsoftwaremaintenance,ongoingoperationand
∗
Correspondingauthor.
E-mailaddress:s_c_misra@yahoo.com(S.C.Misra).
1 CurrentAddress:MotilalNehruNationalInstituteofTechnology,Allahabad,UttarPradesh,India.
0895-7177/$–seefrontmatter©2010ElsevierLtd.Allrightsreserved.
doi:10.1016/j.mcm.2010.03.037

S.C.Misra,A.Mondal/MathematicalandComputerModelling53(2011)504–521 505
support[3].Platform-as-a-Service(PaaS)isanentirevirtualizedplatform.Itincludesoneormoreservers,operatingsystems,
specificapplicationsanddevelopmentplatformsprovidedasaserviceovertheInternetfordeveloperstobuildapplications
onInfrastructure-as-a-Service(IaaS)isthedeliveryofcomputerinfrastructureasaservice.Infrastructureincludesservers,
processingpowerandstorage.Thishelpsintheeliminationofupfrontcapitalcostandisofimmensebenefittocompanies
whowanttostartsmall[17,18]andalsorelievesthemoftheirneedtoforecasttheirdemandsofthefutureandprovision
accordingly.
ThereisnodoubtabouttheparamountpotentialofCC,butitisyettocrossitsstageofinfancy,withonlyalimited
numberoftakerscurrently,owingtosomeofthechallengesofitswidespreadadoptionsuchassecurity,trust,andcost-
effectiveness[19,2].Itisestimatedthat71%ofcompaniesbelievethatcloudcomputingisarealtechnologyoption.70%hold
thatitwouldmaketheirbusinessflexible.62%thinkthatitwouldhelpthemreactquicklytomarketconditionsand65%fee,it
wouldhelpincreasefocusoncorebusiness[20].However,inreality,thereareonlyveryfewcompanieswhichareactually
usingCC.Itisbecauseofthelackofproperunderstandingofthecloudarchitecture,itspricingmodelanditssuitability
tothedifferentrequirementsandscenariosofdifferentcompanieswithdifferentbusinessenvironments.Theseformthe
motivationbehindtheworkpresentedinthispaper.
The rest of the paper is organized as follows: In Section 2, we provide the background and motivation of this work.
Section3givestheguidelinesthatidentifythesuitabilityofacompanyfortheadoptionoftheCC,whileinSection4,we
deriveourROImodel.Finally,weconcludethepaperinSection5.
2. Backgroundandmotivation
ConsideringthewayadoptionofCCcanrevolutionizethebusinessscenarioasithasrevolutionizedtheresearchscenario,
someworkhasbeendoneinthisfield.In[3],PykehassupportedthepotentialofCCinbusinessandexplainedhowitis
aparadigmshiftfromwhatwehaveknowntraditionalcomputingtobe,andhowtotelliftheapplicationisinthecloud
ornot.HealsodealtwiththetechnicalitiesfortheimplementationofCCanditsdeliverytocustomers.Thevariouslayers
inthecloudinfrastructureandsomedeliverymodelshavebeenexhaustivelycoveredin[4].Theauthorshavealsodealt
withmarket-oriented2resourceallocationofCloudsbyleveragingthethirdgenerationAnekaenterpriseGridtechnology.
Someworks(suchas[24,25])haveperceivedthelikelihoodofCCbecomingthefifthutilityafterelectricity,water,gasand
telephony.
ComparisonsofCCtootherformsofcomputingsuchasgridcomputing(desktopgrids)andvolunteercomputinghave
beenmadein[26].ThebenefitsofCC,thechallengesfacedintheimplementationofthecloudarchitecture,theopportunities
intheirsolutionandthevariousrisksthatusersmighthavetoundertakeformigrationtothecloudhavebeenexplained
in[17].Theauthorsalsoproposedatradeoffequationwhichindicateswhichtechnologycangivemoreprofit.
Differentcloudservicesprovidedbythedifferentserviceprovidersalongwiththeircostsandcharacteristicshavebeen
comparedin[27,28].
ReportsandinferencesdrawnfromvariousglobalsurveyscarriedoutforCChavebeenmentionedin[20,29,18,30].Also,
varioustypesofcost–benefitanalysisofcloudhavebeenreportedin[31–34],givingdirectfiguresofcoststhatareincluded.
Currently,therealsoexistsdebatesinvariousblogsitesbetweenprimarilytwogroupsdividedontheopinionofprofitability
ofthecloud.Onegroupfindsthecloudtobecostsaving,whiletheotherfindsittobemoreexpensive.ROIofimplementing
CChasalsobeencalculatedinafewcases(viz.,[27]),butpertainingonlytospecificcompanies.Evencostanalysisofwhether
e-mailserversshouldbemovedtothecloudisgivenin[34].Butnoneofthesesourcesarefundamentallysimilarincontext
andscopeofthispaperwhichneithermeasuresthesuitability,norgivesagenericmodelforthecalculationofROI.Dargha’s
work [35] is based on the principle that this paper has followed for finding the suitability index. But the present work
providesamuchdeeperinsight.ItdefinesanumberoffactorstobeconsideredpriortoadoptingCC.Inthispaper,wehave
morecriteriaoverandabovethemajorcriteria.Thismakesanalysismoremeaningful.Thepresentworkalsoprovidesboth
objectiveandsubjectivetoolsforthepresentanalysisaswellasfordecisionmaking.
Somepreviousresearchers(e.g.,[24,25])havealsostudiedthecost–benefitanalysisofCC,buttheirworkspertaintothe
dataofsinglecompanies.Onlydirectcostshavebeenincludedintheirdiscussions,butassuchagenericmodelcontaining
variables[24,25]whichshouldbeapplicabletoanyandallcompanies—bigorsmall,wellestablishedorstart-ups,hasnot
beenexplored.
A contemporary survey has found out that the current pricing pattern and other factors of the cloud make it highly
suitableforsmallandmediumenterprises[18].Currently,CCmaynotbeverysuitableforbigenterprises.However,no
criteriahavebeensetforthtoconsiderthefactorswhichmakeacompanybig,mediumorsmall.Itisyettobedecided
whetherthecriteriashouldbebasedonlyontheirannualrevenueorsomeotherfactorsaswell.
TheROImodelhasbeenlimitedonlytotheaccountingofcostsofthecloud,thesavingsmadefromitortheextraamount
tobespentonit.NovaluationhasbeengiventotheintangiblebenefitsofCC(e.g.[24,25]).Intangiblebenefitshavebeen
limitedonlytoitsmentionincertainsources.
CChassofarbeenviewedprimarilyfromtheperspectiveofcost.Thispapertriestobroadenthatoutlookwithamodel
thathelpsnotjustidentifythesuitabilityofacompanyforthecloudbyclearlyspellingoutallthefactorsthatneedtobe
consideredforthesame,butalsotriestogiveacertainprofitabilityvaluationofthebenefitsassociatedwithCC.
2 ItisworthnotingthatsimilarworksinthecontextofGridComputingalsoexistintheliterature.Examplesinclude[21–23].

506 S.C.Misra,A.Mondal/MathematicalandComputerModelling53(2011)504–521
TheCCarchitectureconsistsofthreemainplayers—CloudProviders,CloudUsersorCustomersandCloudVendors[36].
Inthispaperwewouldbeprimarilylookingfromtheclouduserpointofview.Twotypesofbusinessmodelscanbedrawn
fortheenterprises(cloudusers)willingtoadoptCCservices.Theyare:
i. BusinessmodelforcompanieswithexistingITinfrastructure.
ii. Businessmodelforstartupcompanies.
StartupcompaniesarethemosteligiblecandidatesfortheadoptionofCC[18]becauseofthestarklyvisiblebenefitsthat
CCoffersintheformofnoupfrontcapitalinvestmentinhavingtobuyservers,buildingsandfloorspacetobuilddatacenters,
noelectricity,coolingcosts,nopurchaseofsoftwarelicenses,etc.thustherearenobarrierstoentry.Thesecompaniescan
startsmallandcaninvestintheincreaseofhardwareresourcesastheirbusinessflourishesoronlywhenthereisanincrease
intheirneeds[17].
The challenge comes when making a decision for companies with an already existing and working datacenter (IT
infrastructure)onwhetherCCwouldbeappropriatefortheorganizationandtheyshouldembarkonthecloudorthey
shouldsticktotheirownin-houseinfrastructureandinvestintheirexpansionandconsolidation[37].Itisexpectedthat
thispresentpaperwillfinduseinthisregard.
3. Identificationofacompany’ssuitabilityfortheadoptionofCC
Someofthekeycharacteristicsoftheresourcespossessedbyacompanytobeconsideredbeforehoppingontothecloud
‘‘bandwagon’’are:
I. SizeoftheITresources.
II. Theutilizationpatternoftheresources.
III. Sensitivityofthedatatheyarehandling.
IV. Criticalityofworkdonebythecompany.
3.1. SizeofITresources
Largenessoftheresourcesalreadypresentinacompanyplaysaveryvitalroleinthecostfactor.Thelargerthevolume
oftheresources,thelesseristhepercapitacostofoperatingtheseresources,owingtotheeconomicsofscale[17,38–40].
ThiseconomicsofscalecausesTCOofdatacenterstoreducetheirsizeincreases.Itthenbecomesmuchcheaperandmore
beneficialinthelongrunthanusingthecloudservices.Thus,itmaynotbeeconomicallyviable,orforthatmatterprofitable,
forcompanieswithsufficientlylargedatacenterstodroptheirowninfrastructureandheadtowardsthecloud.Considering
allrelevantfactors,however,cloudcomputinghasbeenfoundtobemoresuitableforsmallandmediumsizebusiness
enterprises[18].
Someofthefactorsthataretakenintoaccount,whiledeterminingthesizeoftheITresourcesofacompanyare:
1. Thenumberofserversthecompanymaintainsinitsdatacenters.
2. Thesizeofthecustomerbaseofthecompany.
3. TheannualrevenuefromIT.
4. Thenumberofcountriesacrosswhichthecompanyisspreadover[35].
3.1.1. Numberofservers
a. Lessthan100servers...(small).
b. From101to2000servers...(medium).
c. From2001to10,000servers...(large).
d. 10,001to50,000servers...(verylarge).
e. 50,001to100,000servers...(superlarge).
f. Above100,000servers...(ITgiants).
Categories ‘e’ and ‘f’ do not count. Category ‘e’ belongs to companies like Akamai Technologies, 1&1 Internet,
Rackspace[20],etc.whichmaintainorratherhosthuge‘serverfarms’.
ItmaysohappenthatintheirserversalargepartoftheInternetresides.Ifitisso,itwouldnotbemeaningfulforthemto
goforthecloudsbecausetheymaketheirmoneybymaintainingserversforothercompanies.Category‘f’belongstohuge
hulkingITgiantssuchasGoogle,Amazon,andIBM[41].Theytoodonotcountbecausetheythemselvesareassuchsome
ofthekeyplayersprovidingCCservices.
3.1.2. Sizeofcustomerbase
Thesizeofthecustomerbaseorthenumberofusersoftheservicesofferedbyacompanyisaverygoodyardstickin
estimatingthesizeoftheinternalresourcesmaintainedbyanorganizationforitssmoothfunctioningandservicedelivery.
Italsogivesapictureoftheutilizationpatternofthein-housedatacenterresources.Awidegeographicaldistributionofthe
customerbaseofacompanywouldgiveamoreorlessconstantworkloadpattern[35].

S.C.Misra,A.Mondal/MathematicalandComputerModelling53(2011)504–521 507
Fig.1. Moderatelyvariableworkloadwithnosurges.
3.1.3. AnnualrevenuefromITofferings
TheamountofrevenuegeneratedfromtheITresourcesofacompanygoesalongwayindecidingwhetheritshouldstill
maintaintheexpensiveyetconvenientdatacentersorshoulditadoptseamlessswitchovertothecloud.
a. Lessthan$100million...(small).
b. Between$(100–500)million...(medium).
c. Above$500million...(large).
3.1.4. NumberofcountriesITisspreadacross
Thegreaterthenumberofcountries[35]acompanyanditsdatacentersarespreadin,thegreaterthepoolofitsinternal
resourcesfacilitatinglargerbenefitfromeconomiesofscaleandthusreducingitsoperationalcost.Also,ifthecompanyhas
itspresencefeltinanumberofcountries,thenitsworkloadcanbeassumedtobequiteconstantwhichmightreduceits
suitabilityfortheadoptionofcloudservices[17,35].
Somecategorieswecanbreakthemupinto:
a. Onecountry.
b. Morethanonebutlessthanfourcountries.
c. Lessthanorequaltosixcountries.
d. Lessthantencountries.
e. Above10countries.
3.2. Utilizationpatternoftheresources
Merelyhavinglargeorsmallresourcesdoesnotmakeitbeneficialforacompanytorespectivelyabstainfromorembark
onthecloudservices.Profitabilityalsodependsontheamountofutilizationoftheexistingresources.Alargenumberofvery
underutilized(toomuchoverprovisioning)serverresourcesleadstoalargeamountofwastageandhencemakesitsuitable
forusingcloudservices,whereassmallyetperenniallywellutilizedserverswouldnotbeeconomicaliftakentotheclouds.
McKinseyreportstatesthattheglobalaverageserverusagetopsat5%–10%only.Thishappensasaresultofprovisioning
forthepeaks,thesuddenspikes&surges.Itisaverydauntingtasktoaccuratelyforecastworkloadrequirements.Thistask
getsevenmoreaggravatedinbusinesseswhichdependsonwebapplicationsandwhoseworkloadvariesalotmorethan
traditionalbusinessapplications[18].CCisbeneficialforcompaniesespeciallyiftherearehighlyvariablespikesinresource
demand[17].
Wecandeterminetheutilizationpatternby:
a. Averageusage.
i. Thetypeofservicesofferedbythecompany.
ii. Thenumberofusersusingtheservices,i.e.,sameascustomerbase.
iii. Thenumberofprojectsundertaken.
b. Peakusage.
i. Thedurationofpeakusage/year.
ii. Thenumberoftimesthepeakvalueisoftheaveragevalue.
c. Amountofdatahandling/transactionsdone.
Averageandpeakusagepatterns.
Letuslookintosomeofthenormalworkloadvariabilitypatternsfoundinenterpriseinstallations:
• Profile1:Moderatelyvariableworkloadwithnosurges[42](Fig.1).
• Profile2:Highlyvariableworkloadwithspikes[42](Fig.2).
• Profile3:Novariabilityconstantworkload(Fig.3).
• Profile4:Moderatelyvariableworkloadwithoccasionalsurges(Fig.4).

508 S.C.Misra,A.Mondal/MathematicalandComputerModelling53(2011)504–521
Fig.2. Highlyvariableworkloadwithspikes.
Fig.3. Novariabilityconstantworkload.
Fig.4. Moderatelyvariableworkloadwithoccasionalsurges.
Fig.5. Variableworkloadwithlongaverages.
• Profile5:Constantworkloadbutworkloadpatternvariesatdifferenttimesoftheyearowingtodifferenttypesofproject
undertaken(Fig.5).
Typeofservicesofferedbyacompany.
Table1showssomeexamplesoftypesofservicesofferedbyacompany.
Typeofprojectsundertaken
Inthiswork,thetypeofaprojectreferstothedegreeofcomputationallyintensiveprocessesrequiredtocompleteatask.
Thiscriterionmaynotbeapplicableforallorganizationsespeciallyforthoseenterpriseswhichprovidewebapplications
orinternetservices.Thesearemeantforthoseenterpriseswhichareinvolvedinthevariouscomputationallyintensive
jobs,e.g.,researchlaboratoriesinvolvedinnuclearresearch,drugdesign,weatherforecasting,etc.orcompaniesinvolvedin

S.C.Misra,A.Mondal/MathematicalandComputerModelling53(2011)504–521 509
Table1
Someofthedifferenttypesofonlineservicesofferedbycompanies.
Serviceoffered Workloadprofile Surgesinworkloadandtheirduration
| Socialnetworking      | 3   | –                                     |
| --------------------- | --- | ------------------------------------- |
| Searchengines         | 3   | –                                     |
| Onlinebookstore       | 4   | Newbookreleases.Lastsforafewdaysonly. |
| E-mail                | 1   | –                                     |
| Gamingportals/arcades | 3   | –                                     |
Marriagesites 2 Duringmarriageseason.Usuallylastsfor1or2monthsinayear.
| Banking/finance | 3   | –   |
| --------------- | --- | --- |
Newsrooms 4 Duringsuddenbreakofbigevents,disasters.Lastsfromafewhourstoafewweeks.
| Softwareproviders | 2   | Newsoftwarereleases.Lastsforafewweeks. |
| ----------------- | --- | -------------------------------------- |
| Video/musicsites  | 3   | –                                      |
| Downloadablesites | –   |                                        |
| Jobssite          | 1   | –                                      |
| Pornographysites  | 3   | –                                      |
Onlineticketing 4 Duringholidayseasons,festivals,disasters.Lastsforafewweeks.
| Stockbrokerage    | 4   | SuddenfallorriseofSENSEX.Lastsforafewhours. |
| ----------------- | --- | ------------------------------------------- |
| Photosharingsites | 2   | Afterholidayseason.Lastsforafewweeks.       |
Onlineshopping/auction 2 Duringlottery.Lastsforafewminutesonly.
developinghigh-endanimationandspecialeffectmoviesandgamesorcompanieswhichareinvolvedinthedevelopment
ofvarioussoftwaresandapplications.Thus,typeofprojectalsoplaysacrucialroleindeterminingtheaverageworkload
patternofanyorganization.
Peakusage
Peakusageisthemaximumutilizationofthecomputationalresourcespresentinanorganization.Peakvalueisreached
whenthedemandsuddenlyincreasesandreachesitsmaximumvalue.Hence,theyareoftenknownassurgesorspikes.But
theymaybeverydiscrete,intermittentandsporadic.Iftheorganizationresourcesareprovisionedforthesepeaks,thenit
leadstolargewastageofidlingresources.Highlyvariableworkloadsaremoresuitableforthecloudsthanconstantones[17,
18].Peakusagecanbemeasuredintermsof:
i. Durationofpeaks.Ifthepeaksarequitefrequent,thentheaggregatedurationofthepeaksmaybecomeworthwhilefor
provisioningintheorganization’sowndatacenter.Butifthisdurationdoesnotaccumulatetoasubstantialamount,then
provisioningforthesepeakswouldtantamounttolargewastageofresources[42]andhenceoptingforCCwouldbea
viableoption.
Aggregatedurationofthesepeaksinayearhasbeencategorizedinto:
• Fewhours.
•
Fewdays.
•
Fewweeks(lessthanorequalto3).
•
Fewmonths(lessthanorequalto3).
ii. Peakbyaveragevalue.
Provisioningforworkloadpatternswiththevalueofpeakafewmultiplesoftheaveragevaluewoulddrawlarge
wastageofpreciousresources.Ifnotprovisioned,itwouldresultinalargenumberofunsatisfiedcustomersordelay
inproductdelivery.Highlyscalableanddynamicallyallocatedresourcesofthecloudwouldbethebestoptioninthese
scenarios.
Peakbyaveragevaluehasbeencategorized[17,43]into:
• Lessthantwice...(leastwastage).
• Lessthanfivetimes.
• Lessthantentimes.
• Abovetentimes...(hugewastage).
Amountofdatahandling
Amountofdatahandled,acteduponorgeneratedinadayalsoshouldplayasignificantroleinacompany’sdecisionto
movefortheCCservices[17].Hugeamountofdataacteduponwouldrequirealargebandwidthconcerningdataprocessing
andstorageinthecloudenvironment[44,45].Thiswouldcausesubstantialamountofmoneytobespentonbandwidth
charges alone, which would be detrimental for the adoption of CC in the long run. For example, CERN, the European
OrganizationforNuclearResearch,generatesterabytesofdataeachdayfromitsnuclearresearchinitslaboratories.Ifall
thesedataweretobesenttothecloudsforprocessingaswellasstorageandalsorecalledregularlyforanalysis,firstlyit
wouldtakeahugeamountoftimefortransfer.Also,thebandwidthchargesalonewouldbeasignificantportionfromtheir
budget,apartfromthechargesofstorageofsuchhugeamountofdataintheclouds.
Inthiscase,thecategorieshavebeensub-dividedinto:
a. Above100terabytes/month.
b. 1–100terabytes/month.

510 S.C.Misra,A.Mondal/MathematicalandComputerModelling53(2011)504–521
Table2
Categorizingsensitivityofdata.
Category Data
InformationanddataofgovernmentfederalandintelligenceagencieslikeCIA,FBI.
Extremelysensitive Blueprintsandinformationregardingweaponsystems,artillery,aircrafts,etc.ofthedefenseforces.
Mattersconcerningnationalsecurity[21].
Bankrelateddatalikebankaccounts,passwords,pin,transactionsandbalances,etc.
Financialdataofcompanies,quotationsforvarioustenders,etc.
Companydatabases.
Verysensitive
Ongoingconfidentialresearch.Tradesecrets,drugformulas,earlyresearchfindings[21].
Sourcecodes.
E-mailaccounts.
Personalinformationsuchasname,contactdetails,e-mail-ids,profiles.
Sensitive
Patientrecords,healthrecords[21].
Pictures,videosinsocialnetworkingwebsites.
Lesssensitive Clickstreamdata.
Serviceusagedetails.
Freesoftware,music,videos,pictures,games,news,articles.
Notsensitive Views&commentsinblogs.
Anythingdownloadablewhichisauthorized.
c. 500gigabytes–1terabytes/month.
d. 100–500gigabytes/month.
e. Below100gigabytes.
3.3. Sensitivityofdatahandled
OneofthemajorapparentshortcomingsofCC,whichpreventsitfrombeingarunawaysuccessistheconcernforthe
securityofdatagovernance[46]inthecloudenvironment.Thoughtherehasbeenhugeadvancementinsecurityandthere
arenofundamentaldifficultiesassuchinmakingthecloudahighsecuritydensityzonewithwellunderstoodencryptions,
datafirewalls,andpacketfilters[17],butitisyettobetestedexhaustivelyinthereallife.Datasecuritybecomesmoreof
anissueasthesensitivityofthedatahandledbyacompanyincreases.Concernsofdatalock-inincaseofoutagesanddata
availabilityinthelongrunincaseacloudprovidergoesoutofbusinessaggravatestheproblem.Dataneedstobeprotected
fromunauthorizeddisclosure,fraud,wasteorabuseatallcosts[47,19].
SensitivityofdatahasbeencategorizedasinTable2:
3.4. Criticalityofworkdonebythecompany
Highlycriticalworkrequiresthemoststringentofresources,platforms,applicationsandsecurity.Themorecriticalthe
workgets,themoredemandinggetstherequirements.Thusverycriticalworkmaynotfindsuitabilitytothecloudasit
wouldrequireverystringentService-LevelAgreements(SLAs)[35]withthecloudprovider.Ifthecompanyisnotverybig,
thenthecloudserviceprovidersmaynotbeverywillingtoprovidethehighlycustomizedService-Oriented-Architecture
(SOA)andApplicationProgrammingInterfaces(APIs).TheymaynotevenbeabletodelivertheQuality-of-Service(QoS)[4,
19,48–51]inprocessesrequiringverylowlatencies[17,35]owingtoconstraintsofthesystemorlackofprofitabilityand
feasibilityontheirpart.
Criticalityofservicescanbecategorizedinto:
Highlycritical...(maynotbesuitableforthecloud).
Critical...(maybesuitableifcompanyislarge).
Lesscritical...(suitable).
Standard...(easilysuitable).
Tabulationsheet
Allthefactorshavebeenassignedvariouscredits(weights)accordingtotheirrelativeimportanceinthefactorwhich
constitutesthem.Thecreditsthathavebeenalreadyassignedmayworkforcertaincompanies,butcertainlynotforall
companies.Thecreditsmaybecustomizedbythecompanies,dependingontheimportanceofthecharacteristicsforthem
ortheirbusiness.Table3actsasaninitialguideinarrivingatthedecisionofwhetherornotCCissuitableforanorganization
andshouldnotbeconsideredasthedefinitiveandtheonlytoolforthesame.3In-depthanalysisshouldbecarriedoutand
variousotherfactorsatthecompanylevelshouldbeconsideredbeforetakingafinalleapinembarkingtotheclouds.
3 Owingtochangeinmarketconditionstheoutcomeofthisstudymaydiffer.Anin-depth(subjectiveaswellasobjective)analysisisstrongly
recommendedandwillberequiredwhenapplyingforpersonalizedbusinessesasotherfactorsmayalsoarise.

S.C.Misra,A.Mondal/MathematicalandComputerModelling53(2011)504–521 511
Table3
Tabulationsheet.
Characteristics Credits
SizeofITresources 7
Numberofservers 8
Lessthan100servers 4
From101to2000servers 3
From1001to10,000servers 2
10,001to50,000servers 1
Numberofcountriesitisspreadacross 4
Onecountry 5
Morethanonebutlessthanfourcountries 4
Morethanequaltofourbutlessthanequaltosixcountries 3
Morethansixbutlessthantencountries 2
Above10countries 1
AnnualrevenuefromITofferings 4
Lessthan$100million 3
Between$(100–500)million 2
Above$500million 1
Workloadvariability 8
Peakusage 6
Durationofpeakusage/year 6
Fewhours 4
Fewdays 3
Fewweeks(lessthanequal3) 2
Fewmonths(lessthanequal3) 1
Peakbyaverage 9
Lessthantwice 1
Lessthanfivetimes 2
Lessthantentimes 3
Abovetentimes 4
Averageusage 8
Typeofservices 5
Profile1 2
Profile2 4
Profile3 1
Profile4 3
Typeofprojectsundertaken 5
Profile1 2
Profile3 1
Profile5 3
Sizeofuser/customerbase 7
Above10million 1
100,000to10million 2
Below100,000 3
Amountofdatahandling 5
Above100terabytes/month 1
1–100terabytes/month 2
500gigabytes–1terabytes/month 3
100–500gigabytes/month 4
Below100gigabytes. 5
Sensitivityofdata 6
Extremelysensitive 1
Verysensitive 2
Sensitive 3
Lesssensitive 4
Notsensitive 5
Criticalityofworkdone 4
Highlycritical 1
Critical 2
Lesscritical 3
Standard 4

512 S.C.Misra,A.Mondal/MathematicalandComputerModelling53(2011)504–521
Calculations
Variouscalculationscanbecarriedoutusingthefollowingformulae:
|                            |     | ( )=NoS×C |              |       | +NoC×C | +AR×C      | .      |           |     |     |     |     |     |
| -------------------------- | --- | --------- | ------------ | ----- | ------ | ---------- | ------ | --------- | --- | --- | --- | --- | --- |
| Largenessvalue             |     | L         |              | NoS   |        | NoC        | AR     |           |     |     |     |     |     |
| AverageUsagevalue          |     |           | ( AU )=ToS×C |       |        | (or) ToP×C | +(     | 4−SCB )×C |     | .   |     |     |     |
|                            |     |           |              |       | ToS    |            | ToP    |           | SCB |     |     |     |     |
|                            |     | (         | )=DoP×C      |       | +PbA×C |            | .      |           |     |     |     |     |     |
| PeakUsagevalue             |     | PU        |              |       |        |            |        |           |     |     |     |     |     |
|                            |     |           |              | DoP   |        | PbA        |        |           |     |     |     |     |     |
|                            |     |           |              | (     | )=PU×C | +AU×C      | +ADH×C |           | .   |     |     |     |     |
| ValueofWorkloadVariability |     |           |              | WV    |        | PU         | AU     |           | ADH |     |     |     |     |
| ValueofDataSensitivity     |     |           | ( DS         | )=SoD | .      |            |        |           |     |     |     |     |     |
|                            |     | (         | )=CWD        | .     |        |            |        |           |     |     |     |     |     |
| ValueofCriticality         |     |           | C            |       |        |            |        |           |     |     |     |     |     |
Finally,
| Suitabilityindex=L×C |     |     | +WV×C |     | +DS×C |     | ×ADH+C×C | ×(  | 65−L | ).  |     |     |     |
| -------------------- | --- | --- | ----- | --- | ----- | --- | -------- | --- | ---- | --- | --- | --- | --- |
|                      |     |     | L     |     | WV    |     | DS       | C   |      |     |     |     |     |
Here,
NoS=NumberofServers
C =CreditofNumberofServers
NoS
NoC=NumberofCountriesitisSpreadAcross
C = CreditofNumberofCountriesitisSpreadAcross
NoC
AR=AnnualRevenue
=CreditofAnnualRevenue
C AR
SCB=SizeofCustomerBase
=CreditofSizeofCustomerBase
C SCB
ToS=TypeofService
C =CreditofTypeofService
ToS
ToP=TypeofProject
C =CreditofTypeofProject
ToP
DoP=DurationofPeak
C =CreditofDurationofPeak
DoP
PbA=PeakbyAverage
=CreditofPeakbyAverage
C PbA
=CreditofPeakUsage
C PU
=CreditofAverageUsage
C AU
ADH=AmountofDataHandling
=CreditofAmountofDataHandling
C
ADH
C =CreditofWorkVariability
WV
C =CreditofCriticality.
C
Forcalculationoftheupperlimitweconsidervaluesonthehighersidefromthetable.
| NoS=3 , | NoC=4andAR=2 |     | .   |     |     |     |     |     |     |     |     |     |     |
| ------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5.
|                                   |         |        | =8  | ,     | =4andC | =4.       |     |     |     |     |     |     |     |
| --------------------------------- | ------- | ------ | --- | ----- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
| AsprovidedinthetableC             |         |        | NoS | C NoC |        | AR        |     |     |     |     |     |     |     |
| Now,L=NoS×C                       |         | +NoC×C |     | +AR×C |        |           |     |     |     |     |     |     |     |
|                                   |         | NoS    |     | NoC   |        | AR .      |     |     |     |     |     |     |     |
| Usingthesevaluesweget,L=3×8+4×4+2 |         |        |     |       |        | . 5×4=50. |     |     |     |     |     |     |     |
| Then,ToS=3                        | , SCB=2 | .      |     |       |        |           |     |     |     |     |     |     |     |
5.
,
| AsgiveninthetableC             |         |     | =5 C      | =7. |       |            |      |     |     |     |     |     |     |
| ------------------------------ | ------- | --- | --------- | --- | ----- | ---------- | ---- | --- | --- | --- | --- | --- | --- |
| (                              | )=ToS×C | ToS |           | SCB | +(    | )×C        |      |     |     |     |     |     |     |
| Now, AU                        |         |     | (or)ToP×C |     | 4−SCB |            | .    |     |     |     |     |     |     |
|                                |         | ToS |           | ToP |       |            | SCB  |     |     |     |     |     |     |
| Usingthesevaluesweget,AU=3×5+( |         |     |           |     | 4−2   | . 5 )×7=25 | . 5. |     |     |     |     |     |     |
Pleasenotethatdecimalorfractionalvaluescanalsobeobtainedfromthetablebybreakingthemintosmallergroups.
| Similarly,DoP=3 |              | , PbA=3.FromchartC |        |     |     | =6andC | =9. |     |     |     |     |     |     |
| --------------- | ------------ | ------------------ | ------ | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
|                 |              |                    |        |     | DoP |        | PbA |     |     |     |     |     |     |
| Weknow,         | ( PU )=DoP×C |                    | +PbA×C |     | .   |        |     |     |     |     |     |     |     |
|                 |              |                    | DoP    |     | PbA |        |     |     |     |     |     |     |     |
Therefore,PU=3×6+3×9=45.
| Now,WV=PU×C         |     | +AU×C |                | +ADH×C |     | .HereADH=4andC |     |     | =5 , | =6&C | =8. |     |     |
| ------------------- | --- | ----- | -------------- | ------ | --- | -------------- | --- | --- | ---- | ---- | --- | --- | --- |
|                     |     | PU    |                | AU     |     | ADH            |     | ADH | C PU |      | AU  |     |     |
| ThereforeWV=45×6+25 |     |       | . 5×8+4×5=494. |        |     |                |     |     |      |      |     |     |     |
| DS=4 ,              | =3; |       |                |        |     |                |     |     |      |      |     |     |     |
C
|                      |     | =L×C |     | +WV×C |     | +DS×C | ×ADH+C×C |     | ×( 65−L | )       |     | =7 , | =8 , |
| -------------------- | --- | ---- | --- | ----- | --- | ----- | -------- | --- | ------- | ------- | --- | ---- | ---- |
| Now,Suitabilityindex |     |      |     |       |     |       |          |     |         | ,whereC |     | C    |      |
|                      |     |      |     | L     | WV  |       | DS       | C   |         |         | L   | WV   |      |
| C =6&C               | =4. |      |     |       |     |       |          |     |         |         |     |      |      |
| DS                   | C   |      |     |       |     |       |          |     |         |         |     |      |      |
Therefore,Suitabilityindex =50×7+494×8+4×6×4+3×4×( 65−50 )=4578.
Leavingsomemarginwegetthevaluetobearound4600.

S.C.Misra,A.Mondal/MathematicalandComputerModelling53(2011)504–521 513
|     |     |     |     | Fig.6. Suitabilityofacompanyforadoptionofcloud. |     |     |     |     |     |
| --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- |
Similarly,forcalculationofthelowerlimitweconsidervaluesonthelowersidefromthetable.
| NoS=2 , NoC=2andAR=1 |     |     | .   |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5.
|                       |     |        | =8 , | =4&C  | =4. |     |     |     |     |
| --------------------- | --- | ------ | ---- | ----- | --- | --- | --- | --- | --- |
| AsprovidedinthetableC |     | NoS    | C    | NoC   | AR  |     |     |     |     |
| Now,L=NoS×C           |     | +NoC×C |      | +AR×C |     |     |     |     |     |
.
|                                   |       | NoS                  | NoC |          | AR .    |          |     |     |     |
| --------------------------------- | ----- | -------------------- | --- | -------- | ------- | -------- | --- | --- | --- |
| Usingthesevaluesweget,L=2×8+2×4+1 |       |                      |     |          | 5×4=30. |          |     |     |     |
|                                   | ,     | .                    |     |          |         | ,        |     |     |     |
| Then,ToS=2                        | SCB=1 | 5.AsgiveninthetableC |     |          |         | =5 C =7. |     |     |     |
|                                   |       |                      |     |          | ToS     | SCB      |     |     |     |
| Now, ( AU )=ToS×C                 |       | (or)ToP×C            |     | +( 4−SCB | )×C     | .        |     |     |     |
|                                   |       | ToS                  |     | ToP      |         | SCB      |     |     |     |
| Usingthesevaluesweget,AU=2×5+2    |       |                      |     | . 5×7=27 |         | . 5.     |     |     |     |
Pleasenotethatdecimalorfractionalvaluescanalsobeobtainedfromthetablebybreakingthemintosmallergroups.
| Similarly,DoP=2 |           | , PbA=2.FromchartC |        |       | =6&C | =9. |     |     |     |
| --------------- | --------- | ------------------ | ------ | ----- | ---- | --- | --- | --- | --- |
|                 |           |                    |        | DoP   |      | PbA |     |     |     |
|                 | ( )=DoP×C |                    | +PbA×C |       |      |     |     |     |     |
| Weknow,         | PU        |                    | DoP    | PbA . |      |     |     |     |     |
Therefore,PU=2×6+2×9=30.
| Now,WV=PU×C         |     | +AU×C | +ADH×C         |     | .HereADH=2andC |     | =5 , =6&C | =8. |     |
| ------------------- | --- | ----- | -------------- | --- | -------------- | --- | --------- | --- | --- |
|                     |     | PU    | AU             |     | ADH            |     | ADH C PU  | AU  |     |
| ThereforeWV=30×6+27 |     |       | . 5×8+2×5=410. |     |                |     |           |     |     |
| DS=2 ,              | =2; |       |                |     |                |     |           |     |     |
C
|     |     |     |     |     |     |     | ×( ) |     | , , |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
Now,Suitabilityindex =L×C +WV×C +DS×C ×ADH+C×C 65−L whereCL=7 C =8
|        |     |     | L   | WV  |     | DS  | C   |     | WV  |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C =6&C | =4. |     |     |     |     |     |     |     |     |
| DS     | C   |     |     |     |     |     |     |     |     |
Therefore,Suitabilityindex =30×7+410×8+2×6×2+2×4×( 65−30 )=3794.
Leavingsomemarginwegetthevaluetobearound3760.
Interpretationofresults
On doing the calculations a numerical value would be obtained. If the numerical value obtained for a particular
organizationisbelow3760thenitwouldnotberecommendedtobesuitabletoadoptCC.
Aresultobtainedbetween3760and46004isconsideredmoderatei.e.itmayormaynotbebeneficialforthemtogofor
thecloud.Furtherinvestigationwouldberequiredandotherfactorsatthecompanylevelshouldbetakenintoconsideration
inordertoarriveatthedecisionwhetherthecloudserviceswouldbeviableinthelongrun.Acompanycouldlookatother
optionsinthesecasessuchaspartialadoptionofcloudservicesoradoptionofvirtualizationtechniquesinitsalreadyexisting
datacenters.
Ascoreabove4600wouldindicatethatthecompanyneedstoadoptCCinordertoenjoylargecostsavingsandother
benefitsthatcomealongwithCC.
TheaboveisshownpictoriallyinFig.6.
Itisimportanttonotethatthecut-offscoresgivenherearesuitableforthecreditsgiventothefactorsinthetableand
wouldonlyapplytothosecompanieswhichkeepthesameweightagetothevariousfactors.Customizingthecreditsof
thevariousfactorstosuitcertainneedswouldcausethecut-offscorestochangeaccordingly.Theloweranduppercut-off
scoresareobtainedbytakingtheloweraverageandtheupperaverageofthefactorsrespectively.
Itshouldalsobenotedthatowingtochangeinmarketconditionstheoutcomeofthisstudymaydiffer.Anin-depth
(subjectiveaswellasobjective)analysisisstronglyrecommendedandwillberequiredwhenapplyingforpersonalized
businessesasotherfactorsmaycomeintothepicture.
4. ROI
ThediscussionspresentedinSection3servesasapointerindeterminingwhetherCCisadvisableforanorganizationor
not.AlotoftimeandresourcesarespentincalculatingROIbytakingintoconsiderationalargenumberoffactorsinvolved
inabusiness.TheindicationgivenbythemarkerwouldgiveanimageofhowtheROIwouldlooklikeandthepainandeffort
4
Thesescoresareobtainedbytakingthelowerandupperaveragesofthefactorsrespectively.

514 S.C.Misra,A.Mondal/MathematicalandComputerModelling53(2011)504–521
Fig.7. SchematicdiagramoftraditionalROI.
Fig.8. Schematicdiagramofcostsforpartialmigrationtocloud.
spentincalculatingtheROIwouldbeworthit.Inotherwords,itwouldgiveanassurancethattheROIwouldbepositiveif
apositiveindicationisgivenbythemarker.Ifanegativeindicationisgivenbythetable,theROIcalculatedcouldcertainly
comeouttobeanegativeoneandtheeffortthatwouldbespentincalculatingtheROImaynotpayoff.
CalculatingROI
ROIisatoolformeasuringtheefficiencyofanyinvestment.ForcalculatingROI,asshowninFig.7,weneedtheinitial
costofproject,theinvestmentmade,thecostsavingsdoneowingtothenewinvestment[52].
( Initialcost−Finalcost )−Investment Costssaved−Investment
ROI= = . (1)
Investment Investment
ItthusturnsoutthatforcalculatingtheROIofCC,weneedtounderstandwhatthesecostsavings,theinitialcostsandthe
investmentsmeaninthecloudmodel.
Noinitialinvestmentisrequiredformigrationtotheclouds,i.e.,thereisnoupfrontcapitalcost.Embarkingonthecloud
canbeaseasyasbrowsingthroughacatalogueofITservices,addingthemtoashoppingcartandsubmittingtheorder.As
soonastheorderisapprovedbyanadministrator,therestofthethingsaredonebycloud[53]Thecostofusingthecloud
servicesiscompletelyoperationalinnature.Hence,inthiscasetheinvestmentisonamonthlyoryearlybasisusingthe
pay-per-usecostofthecloudservices.Theinitialprojectcostisthetotalcostofownership(TCO)ofmaintainingone’sown
datacenterbeforeusingcloudservices.Costsavedwouldbetheentireeliminationofdatacentercost(incaseofcomplete
migration)orthereductionindatacentercost(incaseofpartialmigration).Fig.8showstheschematicdiagramofcostsfor
partialmigrationtocloud.
However,theeconomicsofCCdoesnotendhere.AssociatedbenefitsofCCsuchasmassivescalability,flexibilityof
service,elasticityofresources,andlatesttechnologyofferingaddtotheprofitabilityoftheenterpriseclouduser.Therefore,
asshowninFig.9,
Increaseinprofit+ Reductionincost − Cloudcosts
ROIforcloud = . (2)
Cloudcosts
Here,thetimeframecanbepermonthorperyear.
ROImodel
LetusconsideracaseofamoderatevalueonthetabulationsheetinSection3.Forsuchanenterprise,thebestwayof
usingthecloudserviceswouldbetosimultaneouslymaintainitsowndatacenteraswellasusethecloudservicesforthe
extraresourceswhichcannotbeprovisionedinitsowndatacenter[4,42].
Consideringtheiraverageworkload,theycanmaintain30%abovethisaveragevalueintheirin-housedatacenterand
outsourcetherestofthecomputationalneedstothecloud.Onlywhen80%ofthein-houseservercapacityhasexceeded,

S.C.Misra,A.Mondal/MathematicalandComputerModelling53(2011)504–521 515
Fig.9. Viewofprofits.
Fig.10. Partialcloudmigrationmodel.
theexcesscapacitywouldbedrawnfromthecloud.
|     |     | ∫ T |   |     |     |
| --- | --- | ----- | --- | --- | --- |
110
| Costofcloudperyear |     | = W ( t )− ×average | ·dt |     |     |
| ------------------ | --- | ------------------- | --- | --- | --- |
100
|     |     | ×cloudcost+(storageinclouds)×( 0 | /   | )×12 |     |
| --- | --- | -------------------------------- | --- | ---- | --- |
cost month
|     |     | +bandwidthcost+costofusingapplications. |     |     | (3) |
| --- | --- | --------------------------------------- | --- | --- | --- |
Bandwidthcost=( incomingdata+outgoingdata ) peryear×bandwidthcharges. (4)
j
−
| Costofusingapplications= |     | T ×A |     |     | (5) |
| ------------------------ | --- | ---- | --- | --- | --- |
n n
n=1
where,
=time(inhours)ofusageofnthapplication/platform.
T
n
A =costofapplicationperhourofusageasprovidedbytheASP.
n
T ( )− ·dttakesintoconsiderationonlythepositivevalue,i.e.,thepartshowninFig.10.
| Theintegral | W t 110 | × average |     |     |     |
| ----------- | ------- | --------- | --- | --- | --- |
0 100
AggregateworkloadcanbecalculatedbyusingtheformulagivenbyChariin[42].Aggregateworkloadcanbefoundout
bycalculatingtheareaundertheworkloadcurve.
Hence,
∫ T
| aggregate= | (   | )·dt . |     |     |     |
| ---------- | --- | ------ | --- | --- | --- |
|            | W   | t      |     |     | (6) |
0
Theaverageworkloadcanbecalculatedas
|     | aggregate | ,   |     |     |     |
| --- | --------- | --- | --- | --- | --- |
average=
T
whereT istimeframeinwhichitiscalculatedinhours.
Traditionalcostbeforecloudadoption=numberofservers×costbehindeachserver. (7)
(
CostbehindeachserverorTCO = costsof electricity+cooling+maintenance
|     |     | +manpower+software+backuppower |     | ).  | (8) |
| --- | --- | ------------------------------ | --- | --- | --- |
In-depthcalculationofTCOcanbedonefollowingtheapproachpresentedin[55].

516 S.C.Misra,A.Mondal/MathematicalandComputerModelling53(2011)504–521
Costsavings
Sincethein-housecapacityisprovisionedonlyfor30%abovetheaverageusage,andnotforthepeak,thereisasignificant
reduction in the number of servers that the company has to maintain in its own datacenter. The extra servers can be
decommissionedorsold.Therefore,
Costsaved=( initialno.ofservers−presentno.ofservers )×TCOofeachserver .
(9)
Valuationofintangiblebenefitsleadingtoincreasedprofits:
Agility/flexibility
CCgivesacompanytheabilitytoexplore,experimentandinnovatewithbettermeanssuchasbetterplatforms,and
applicationtoolsinaquickandcost-effectivewaytocomeupwithbetterservicesandsolutions.Thiswouldgiveagreat
boosttotheirbusiness.FlexibilityfromCCaddsvaluetoanenterprise,butitsvaluedecreaseswiththeincreaseinsizeof
theenterprise,i.e.,thispotentialtobeflexiblemaynotaddsomuchprofitabilitytoalargeorganizationasitmaydotoa
smallorganization.LetprofitabilityfromflexibilitybedenotedbyF.
Then,
|          |        |    |     |     |     |      |
| -------- | ------- | --- | --- | --- | --- | ---- |
| constant | ( B ) B |     |     |     |     |      |
| F=       | =       | .   |     |     |     |      |
| ( )      |         |     |     |     |     | (10) |
| f L      | 65−L    |     |     |     |     |      |
TheconstantBcanbetheoriginalannualprofitwhichthecompanyhadbeforetheadoptionofcloudservices.
f ( L ) isafunctionoflargeness.ValueofL5foundfromtableshouldbesubstituted.Thisresultsinabout2%to5%increase
inprofit.
Scalability
Assuch,scalabilitycanbequantifiedbytheamountofusageofextraresourceswhichareautomaticallycommissioned
withtheincreaseindemandandchargedonapay-per-consumptionbasis.Buttheactualimportanceofscalabilityliesin
thefactthatresourcesaremadeavailableinminutes,whichotherwisewouldhavetakenweeksorevenmonths.Scalability
alsopreventsdissatisfiedcustomersasitscalestheresourcesautomaticallywhendemandincreases.Also,itleadstofaster
timetomarket.
Thus,
Scalability=f ( timevalue,customersatisfaction,fastertimetomarket ). (11)
Noseparateformulaisgivenforscalability,asthebenefitsofscalabilityhavebeenquantifiedseparately.
Fastertimetomarket
Apartfromsavingtimeinthefasterprovisioningofresources,companiesusingthetechniqueofbatchprocessingcan
completeaworkmuchfasterthanwhattheirdatacenterresourcespermit,e.g.,using1000EC2machinesaworkcanbe
doneinonehour,whichonemachinewouldtake1000htocompleteandthattooatessentiallythesamecostbyleveraging
theconceptofpay-per-use[17].Fastertimetomarkethasmanyadvantagessuchasonegetstohavetheentiremarket
shareandthuss/hecanchargeapremium,asthereisnoothercompetitorinthemarket.Thus,onegetsalotofextrasales
andforextendedperiodoftimegettingtheopportunitytocapturetheloyaltiesofcustomersearlier.Italsoimprovesthe
company’stechnologicalandinnovativeimage[54].
Thefinancialimplicationsoffastertimetomarket[54]canberepresentedgraphicallyasshowninFig.11:
Letusconsidertherelationfunctiontobeanapproximatesinecurve.
|     |     | ( )=−A·sin | ( ) |     |     |     |
| --- | --- | ---------- | --- | --- | --- | --- |
WerepresentflowofmoneyM t t ,whereAistheestimatedbreak-evencost.
|                    | ∫ t1 | ∫ t1         |        |     |     |      |
| ------------------ | ---- | ------------ | ------ | --- | --- | ---- |
| Traditionalcost=   | (    | ) = −A·sin   | ( )·dt |     |     |      |
|                    | M t  | dt           | t      |     |     | (12) |
|                    | 0    | 0            |        |     |     |      |
|                    | ∫ t2 | ∫ t2         |        |     |     |      |
| Traditionalprofit= |      | ( ) = −A·sin | ( )·dt |     |     |      |
|                    | M    | t dt         | t      |     |     | (13) |
|                    | t1   | t1           |        |     |     |      |
where,
t1=originaltimetakentomarket.
| t2=timeforwhichproductstaysinmarket |     |     | .   |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- |
Letthetimesavedbe(cid:49)t.
Now,thereferencelinebecomesy=−A·sin ( t1−(cid:49)t ( Fig.12 )). (14)
Therefore,
| ∫        | t1−(cid:49)t | ∫ t1 ′    |                        |         |        |      |
| -------- | ------------ | --------- | ---------------------- | ------- | ------ | ---- |
|          | (            | ( ))      | (−A·sin ( t1−(cid:49)t | )+A·sin | ( )) . |      |
| Newcost= | y−M          | t dt =    |                        |         | t dt   | (15) |
|          | (cid:49)t    | (cid:49)t |                        |         |        |      |

S.C.Misra,A.Mondal/MathematicalandComputerModelling53(2011)504–521 517
Fig.11. Relationofcost,revenuewithtime[54].
Fig.12. Relationofnewcost,revenuewithearlytimetomarket[54].
Here,thetimetakenfrom(cid:49)tdoesnotnecessarilyimplycostsbeingconsideredfromtime(cid:49)tafterstartofproject.Itisjust
arepresentationformeasuringcosts.
Also,
∫ t2 ′ ∫ t2 ′
Newprofit= ( M ( t )−y ) dt = (−A·sin ( t )+A·sin ( t1−(cid:49)t )) dt (16)
t1−(cid:49)t t1′
where,
t1 ′ =newtimetakentomarket.
t2 ′ =newtimeforwhichproductstaysinmarket.
′
t2maybeconsideredequaltot2.
Therefore,
Valueoffastertimetomarket(FTM) =( traditionalcost−newcost )+( newprofit−traditionalprofit ). (17)
Customersatisfaction
Customersatisfactionisofhighpriorityinanybusiness.Transitiontothecloudcertainlyaddtothecustomersatisfaction
level.QuantificationofbenefitsofCCcallsfornotthelevelofcustomersatisfactionachieved,butrathertheincreaseofit.
Theincreaseofcustomersatisfaction6canbemeasuredbyanyofthegeneraltraditionalmethodsofsurvey.
Assumingalogarithmic7curve,
 
1
Percentageincreaseinprofit8 =B×log (18)
e 1− %increase
100
where,%increase=(final%−initial%)ofcustomersatisfaction.
Bisaconstantwhosevalue(varyingfrom8to15)dependsuponthetypeoftheservicesprovidedbythecompanyand
alsodirectlyproportionaltoL(largenessvalue).
Thegraphobtainedbyplottingvariousincreaseincustomersatisfactiontoincreaseinprofitpercentageisshownin
Fig.13.
Timevalue
Making IT resources available to end users becomes very time-intensive for the companies that employ traditional
datacentermanagementpractices.Itincludessteps,suchaspurchasinghardware,buildingfloorspace,adequatepower
suppliesandcoolingsystemsinstallingoperatingsystems,middlewareandsoftwaretoberunintheservers,provisioning
5 ThevalueofLthatwegetfromtableisactuallyvalueofsmallness.Togetlargenesswedeductitfrom(1+maxvalue),whichis65.
6 Differenceinpercentageofcustomersatisfactionafterandbeforeadoptionofcloud.
7 Thislogarithmicfunctionofcustomersatisfactioncloselyfollowsprofitabilitywhenplotted.
8 Thisisonlyasuggestedformulaandhasnoscientificbackingbehindit.

518 S.C.Misra,A.Mondal/MathematicalandComputerModelling53(2011)504–521
Fig.13. Increaseinprofitversusincreaseincustomersatisfaction.
the network and the securing back up power. This process may take more than 2–3 months, depending to different
factors.ITorganizationsalsotakeseveralweekstore-provisionexistinghardwareresources.CCdramaticallyalleviatesthis
problemthroughautomation,businessworkflowsandresourceabstractionreducingtheleadtimerequiredfrommonths
tominutes[53].Thistimesavedinthecloud,whichotherwisewouldhavebeenspentprovisioningforresourcesinthe
datacentercanbequantifiedastheexpenditureoftheenterpriseduringthattimeofprovisioningwithoutanyprofits.
Thus,
Timevalue=(
timetakentoprovisioninweeks
)×(
weeklyexpenditure
).
(19)
Focusoncorecompetencies
Withnoneedtoworryabouttheunderlyinginfrastructure,theirmaintenance,theirproperprovisioningbeforethestart
ofanyproject,moreattentionandcarecanbegiventowardsthedevelopmentandtheimprovementofqualityofservices
andproductsofacompany.Thus,betterfocusleadstoimprovementinproductivityanditsbusinesspropositions.Another
greatadvantageofCCisubiquitousaccessormobility,whichallowsemployeestobeproductivefromwherevertheyare
ratherthanconfiningthemtotheirdesksatthecompany[56].
Improvement in productivity can be quantified in terms of decrease in marginal cost (Mc) and increase in marginal
benefits(Mb).
Thus,
Focus=( Mc+Mb )×numberofproductsorservicesdelivered/year . (20)
Disasterrecovery
Disasterrecoveryisaveryimportantaspectofenterprisecomputing.Asdevices,systems,andnetworksgetincreasingly
complex,therearemanyotherthingsthatcangowrong.Disastermayoccurduetoseveralcausesincludingnaturaland
man-madeones.Naturalsourcesincludeearthquakes,firesandanthropogenicsourcesthatincludeviruses,powerfailure,
andintrusion.
Itisestimatedthatmostlargecompaniesspendbetween2%–4%oftheirbudgetandsmallandmediumenterprises(SMEs)
spendupto25%oftheirITbudgetondisasterrecoveryplanning,withtheaimofavoidinglargerlossesintheeventthat
thebusinesscannotcontinuetofunctionduetolossofITinfrastructureanddata.Ofcompaniesthathadamajorlossof
businessdata,43%neverreopen,51%closewithintwoyears,andonly6%survivelong-term[57].Hence,disasterrecovery
andbusinesscontinuityplanningarebecomingincreasinglyimportantforeverybusinessorganization.
Disasterrecoveryplanningisdonebyreplicatingresourcesinanumberofplaces.Thisfearisverymuchreducedinthe
cloudasdatainthecloudisreplicatedthriceandstoredinserverswhicharegeographicallyscattered.
Thus,savingsfromDR = ( %budget9investedinDR× annualbudget )
− bandwidthcostofstoringnewdatadailytocloud−storagecharges.10 (21)
GreenIT
Anenterprisegetsa‘‘GreenIT’’tagwhenithelpssavevaluablenaturalresources.Greentagdoesimprovetheimage
of a company and makes them more likely to be favored by people at the time of energy crisis. A recent survey has
foundthatthe‘green’tagofcompaniesalonewereabletomastera17%increaseincustomeracquisition,31%increase
incustomerretentionanda69%raiseincustomersatisfaction.Theyhavestatedthatthe‘Greenroute’hashelpedimprove
9 ThispercentageisquitelessthantheoriginalpercentagewhichthecompanyusedtoinvestinDRasthisisamodelofpartialmigrationtothecloud.
Forentiremigrationitwouldbewholeofit.
10 Bandwidthandstoragechargesarerecurringbutshouldnotbetakenintoaccounthereasitisalreadybeingpaidascostofusageofcloud.

S.C.Misra,A.Mondal/MathematicalandComputerModelling53(2011)504–521 519
theircustomerloyalty[58].Goingbythemodestofvaluesthatwouldleadtoabout5%increases11inannualprofit.There
arealsogovernmentincentivesforcompaniestryingto‘gogreen’.
Risks
Outageofservice
ThisisoneoftheworstnightmaresofCC,andthishashappenedafewtimesinthepast[17].Butsincethiswouldbe
anoverlappingmodelwiththecloudservicesbeingused,whendatacentercapacityisexceeded,itmaynotadverselyaffect
theenterprise.
5. Conclusion
This paper provides an in-depth analysis of the financial perspective of CC in a very lucid and simple manner. The
discussedmodelprovidesboththeobjectiveaswellasthesubjectivedecisionmakingtooltofindthesuitabilityofacompany
foradoptingCC.Withthesuitabilityindexpresentedinthispaper,companiesneednotfirstwastetheirresourcesandtime
inthecalculationofROIwhichisbothtimeandeffortconsuming,andwhichmaynotyieldadesirableresultattheend.With
thesuitabilityindexcustomizedtotheirneeds,theycaneasilygetapointerastowheretheircompanystandswithrespect
toitsfavorabilitytotheadoptionormigrationtothecloudenvironment.Alsodependingonthescoretheyget,theyhavea
numberofoptionstochoosefromastowhichmodelwouldsuittheirneedsbetter.Itisthenthattheycanstartcalculating
ROIwiththeverysimpleyetgenericmodelpresentedherewhichcanagainbecustomizedtotheirspecifications.Various
intangiblebenefitshavebeenincludedinthemodelwhichgivesamuchbroaderpictureofCCtoitspotentialadopters.
Prospectiveadopterswouldreallyfinditusefulasitwouldsaveboththeirtimeandcost.
Managerialimplications
Itishighlyimportantforacompanytoremaincompetitiveintoday’sbusinessscenario.Toremaincompetitiveinthe
markettheyneedtoembracethelatesttechnologies,methodologies,processes,applications,etc.tocomeupwiththebest
servicesandproducts.Forthismanagersinsuchorganizationsneedtobeverydynamictakingthebestdecisionswhich
wouldacceleratechangesinbusinessprocesses.Thesechangesmayvaryfromminoradjustmentsinongoingprocesses,
to revolutionizing the entire business, systems and processes. They need tools which would assist them with proper
decision making. This model is one such tool that helps them understand the different models of CC, and the potential
outcomes/benefitsofimplementationofsuchmodels.
Managementofinformationsystemsisprogressivelybecomingmoredifficult.Asaresultseniormanagementincluding
CIOsandCFOsarebeingrequiredtojustifyprojectsfinanciallybasedontheirreturn.Informationsystemshavealways
beendifficulttoquantifyinprofitabilitytermsbecausemostofthederivedbenefitsareintangiblebynature,e.g.improved
customerservice.Thispaperattemptstoincorporatevariousintangiblesintotraditionalcost–benefitanalysisandROI.The
paperalsoreviewsthesuitabilityofthecompanytoCCtakingintoconsiderationvariousparameters.Thisgoesalongway
inassistingdecision-makingatthemanageriallevel.
Performanceanalysisandscopeforfurtherwork
Wehavetakenupthepartialmigrationmodelforshowingthecostsandquantifyingthebenefits,becausewiththis
modelonecanclearlyshowcaseingoodlightallthevariousmodelsofCCthatcanbeadoptedbycompaniesalongwith
theircostandhowtheyaffecttheROIcalculation.
Companieswhichwanttocompletelymigratetothecloudinfrastructurewouldnothavetoincuranyadditionalcostat
theirowndatacenter,otherthanonlyoperationalcostsofthecloud.Theywouldbesavingtheentirecostofrunningtheir
datacenterandwhatevercosttheyincurfromthecloudwouldbeincludedasinvestment.
OthercasesincludesituationswhenacompanyoptsforvirtualizationoftheITresourcesinitsdatacenter,i.e.,creating
privatecloud.Then,inthatcase,costofvirtualizationthatincludescostofVMmiddlewaresoftwarelicense,itsregular
updateswouldbeaddedtotheTCOoftheserversmaintainedinitsowndatacenter.
Theexpenditureofusingthecloudservicesiscompletelyoperationalinnatureandthattooonapay-per-usebasis.There
areabsolutelynoup-frontcostsorcapitalexpenditureatthetimeofadoptionormigrationtothecloudservices.Butthe
profitsgeneratedfromthebenefitsofCCmaynotbeofthesametimeframeasthecloudcost.Theincreasedprofitsmay
trickleinthelater.Inthatcase,consideringtheoperationalcostofthecloudastheinvestmentandthetimeframeinwhich
increasedprofitisexpected,NetPresentValue(NPV)andInternalRateofReturn(IRR)canbecalculatedalongwithROI.
TheprofitsfromthebenefitsofCCshownheremaynotbeapplicableforallcompanies.Socompaniesshouldcustomize
withscenariosthatletthemfittheirmodelandincorporateonlythosecostsandbenefitsinthecalculationoftheirROI.
Themodelpresentedinthispaperhasbeendevelopedtakingintoconsiderationalargenumberoffactorsactinginthe
ITindustryand,hence,shouldworkforawiderangeofcases.Butthismodelneedstobeexhaustivelytestedwithreal
industrydata,conditionsandsituations.Realcompanydatawouldbeabletoascertaintherobustnessofthismodel.Even
simulationdataobtainedbyreplicatingtheindustryconditionsonvarioussoftwarecanbeusedtoassessthepracticalityof
modelanalyzedbyus.Thus,scopeforfutureworkincludesrigoroustestingofthismodelwithrealandsimulateddata.
11 Putting69%inthecustomersatisfactionformula.

520 S.C.Misra,A.Mondal/MathematicalandComputerModelling53(2011)504–521
References
[1] A.Weiss,Computingintheclouds,NetWorker11(4)(2007)16–25.
[2] A.Chien,B.Calder,S.Elhert,K.Bhatia,Entropia:architectureandperformanceofanenterprisedesktopgridsystem,JournalofParallelandDistributed
Computing63(5)(2003)597–610.
[3] J.Pyke,Nowisthetimetotakethecloudseriously.http://www.cordys.com/cordyscms_sites/objects/bb1a0bd7f47b1c91ddf36ba7db88241d/time_
to_take_the_cloud_seroiusly_online_1_.pdf.
[4] R.Buyya,C.S.Yeo,S.Venugopal,Market-orientedcloudcomputing:vision,hype,andrealityfordeliveringITservicesascomputingutilities,in:
Proceedingsofthe20099thIEEE/ACMInternationalSymposiumonClusterComputingandtheGrid,vol.00,2009.
[5] J.Broberg,S.Venugopal,R.Buyya,Market-orientedgridsandutilitycomputing:thestart-of-the-artandfuturedirections,JournalofGridComputing
6(3)(2008)255–276.
[6] I.Foster,C.Kesselman(Eds.),TheGrid:BlueprintforaFutureComputingInfrastructure,MorganKaufmann,SanFrancisco,USA,1999.
[7] M.Chetty,R.Buyya,Weavingcomputationalgrids:howanalogousaretheywithelectricalgrids?ComputinginScienceandEngineering4(4)(2002)
61–71.
[8] AlekOpitz,HartmutKönig,SebastianSzamlewsk,Whatdoesgridcomputingcost?JournalofGridComputing6(4)(2008)385–397.
[9] EnisAfgan,PurushothamBangalore,Computationcostingridcomputingenvironments,in:29thInternationalConferenceonSoftwareEngineering
Workshops,ICSEW’07,2007,p.9.ISBN0-7695-2955-0.
[10] ZhengyouLiang,LingZhang,ShoubinDong,WenguoWei,Chargingandaccountingforgridcomputingsystem,gridandco-operativecomputing,
in:LectureNotesinComputerScience,vol.3003,ISBN:978-3-540-21993-4,2004,pp.644–651.
[11] RomanBeck,MichaelSchwind,OliverHinz,Grideconomicsindepartmentalizedenterprises,JournalofGridComputing6(3)(2008)277–290.
[12] MichaelSchwind,OliverHinz,RomanBeck,Acost-basedmulti-unitresourceauctionforservice-orientedgridcomputing,in:Proceedingsofthe8th
IEEE/ACMInternationalConferenceonGridComputing,2007,pp.137–144.ISBN:978-1-4244-1559-5.
[13] DirkNeumann,JochenStößer,ChristofWeinhardt,JensNimis,Aframeworkforcommercialgrids-economicandtechnicalchallenges,JournalofGrid
Computing6(3)(2008)325–347.
[14] DanielJ.Veit,WolfgangGentzsch,Grideconomicsandbusinessmodels,JournalofGridComputing6(3)(2008)215–217.
[15] JamesBroberg,SrikumarVenugopal,RajkumarBuyya,Market-orientedgridsandutilitycomputing:thestate-of-the-artandfuturedirections,Journal
ofGridComputing6(3)(2008)255–276.
[16] RamayyaKrishnan,Grideconomics:aselectivediscussionoftworesearchproblems,JournalofGridComputing6(3)(2008)219–224.
[17] M.Armbrust,A.Fox,R.Griffith,AnthonyD.Joseph,R.H.Katz,A.Konwinski,G.Lee,D.A.Patterson,A.Rabkin,I.Stoica,M.Zaharia,Abovetheclouds:a
berkeleyviewofcloudcomputing,February10,2009.http://www.eecs.berkeley.edu/Pubs/TechRpts/2009/EECS-2009-28.html.
[18] Mckinseyreport,clearingtheaironcloudcomputing.http://images.cxotoday.com/cxoimages/storyimages/matter101157.pdf.
[19] E.Burke,Categorizingdatasensitivityforcomputersecurity,No.222,March4,2001.http://datacenter.cit.nih.gov/interface/interface222/security.
html.
[20] Avanade, 2009 global survey of cloud computing, February 2009. http://www.avanade.com/_uploaded/pdf/thoughtleadership/
cloudsurveyexecsummary810844.pdf.
[21] Werner Streitberger, Sebastian Hudert, Torsten Eymann, Bjoern Schnizler, Floriano Zini, Michele Catalano, On the simulation of grid market
coordinationapproaches,JournalofGridComputing6(3)(2008)349–366.
[22] G.Stuer,K.Vanmechelena,J.Broeckhovea,Acommoditymarketalgorithmforpricingsubstitutablegridresources,FutureGenerationComputer
Systems23(5)(2007)688–701.
[23] K.Lai,L.Rasmusson,E.Adar,L.Zhang,B.A.Huberman,Tycoon:animplementationofadistributed,market-basedresourceallocationsystem,
MultiagentandGridSystems1(3)(2005)169–182.
[24] R.Buyya,C.S.Yeo,S.Venugopal,Market-orientedcloudcomputing:vision,hype,andrealityfordeliveringcomputingasthe5thutility,December
2008.
[25] R.Buyya,C.S.Yeo,S.Venugopal,J.Broberg,I.Brandic,CloudcomputingandemergingITplatforms:vision,hype,andrealityfordeliveringcomputing
asthe5thutility,FutureGenerationComputerSystems25(2009)599–616.
[26] M.Maheswaran,Cloudcomputing,SeminarReport,CochinUniversityofScienceandTechnology,India,November2008.
[27] A.Edlund,Cloudcomputing,pay-as-you-gocomputingexplained.
[28] D.Chappell,ChappellandAssociates,Cloudplatformstoday:aperspective,April18,2009.
[29] Survey:cloudcomputing‘nohype’,butfearofsecurityandcontrolslowingadoption.http://www.circleid.com/posts/20090226_cloud_computing_
hype_security.
[30] B.Matthews,D.Chapman,Alsbridgecloudcomputingsurvey—summaryoffindings,21stApril2009.
[31] ROICaseStudy,NucleusResearch.com,DocumentI117,January2009.http://www.google.com/apps/intl/en/business/case_studies/tvr.pdf.
[32] D.Hinchcliffe,Whatdoescloudcomputingactuallycost?Ananalysisofthetopvendors,ebiz:theInsider’sGuidetoBusinessandITAgility.
http://www.ebizq.net/blogs/enterprise/2009/08/what_does_cloud_computing_actu.php.
[33] Financial implications of the cloud, Infosys Microsoft Alliance and Solutions Blog. http://www.infosysblogs.com/microsoft/2008/12/financial_
implications_of_the_1.html.
[34] D.Rosenberg,Thecostofcloudadoption.http://news.cnet.com/8301-13846_3-10140303-62.html.
[35] T.Schadler,Shouldyouremailliveinthecloud?Acomparativecostanalysis,January5,2009.
[36] R.Dargha,Cloudcomputing:keyconsiderationsforadoption,InfosysTechnologies,April2009.http://www.infosys.com/cloud-computing/white-
papers/cloud-computing.pdf.
[37] Cloudcomputing.http://en.wikipedia.org/wiki/Cloud_computing.
[38] W.Vogels,Beyondserverconsolidation,ACMQueue6(1)(2008)20–26.
[39] P.R.Krugman,MauriceObstfeld,InternationalEconomics:TheoryandPolicy,sixthed.,EconomiesofScale,ImperfectCompetition&International
Trade,2003(Chapter6).
[40] D.Abramson,R.Buyya,J.Giddy,AComputionaleconomyforgridcomputinganditsimplementationintheNimrod-Gresourcebroker,Future
GenerationComputerSystems18(8)(2002)1061–1074.
[41] R.Buyya,D.Abramson,S.Venugopal,Thegrideconomy,ProceedingsoftheIEEE93(3)(2005)698–714.
[42] Rich Miller, Who has the most web servers? May 2009. http://www.datacenterknowledge.com/archives/2009/05/14/
whos-got-the-most-web-servers/.
[43] S.Chari,Confrontingthedatacentercrisis:acost–benefitanalysisoftheIBMcomputingondemand(CoD)cloudoffering,March2009.
[44] Thehighvolumewebsitesteam,‘‘Knowingyourworkload’’,BestPracticesforHigh-VolumeWebSites,IBMRedBooks,2002.
[45] J.Broberg,Z.Tari,MetaCDN:harnessingstoragecloudsforhighperformancecontentdelivery,in:Proc.SixthIntl.ConferenceonService-Oriented
Computing,ICSOC2008,Sydney,Australia,2008.
[46] S.Mansfield-Devine,Dangerintheclouds,NetworkSecurity(12)(2008)9–11.
[47] K.M.Cullagh,Datasensitivity:resolvingtheconundrum1.http://www.bileta.ac.uk/Document%20Library/1/Data%20Sensitivity%20-%20resolving%
20the%20conundrum.pdf.
[48] K.Keahey,I.Foster,T.Freeman,X.Zhang,Virtualworkspaces:achievingqualityofserviceandqualityoflifeinthegrid,ScientificProgramming13
(4)(2005)265–275.
[49] S.Venugopal,R.Buyya,L.Winton,AgridservicebrokerforschedulingE-scienceapplicationsonglobaldatagrids,ConcurrencyandComputation:
PracticeandExperience18(6)(2006)685–699.

S.C.Misra,A.Mondal/MathematicalandComputerModelling53(2011)504–521 521
[50] I.Brandic,S.Pllana,S.Benker,Specificationplanning,andexecutionofQoS-awaregridworkflowswithintheamadeusenvironment,Concurrencyand
Computation:PracticeandExperience20(4)(2008)331–345.
[51] B.Maggs,Globalinternetcontinentdelivery,in:Proc.1stIEEE/ACMIntl.SymposiumonClusterComputingandtheGrid,CCGrid2001,Brisbane,
Australia,May2001.
[52] K.ElEmam,TheROIFromSoftwareQuality,AuerbachPublications,2005.
[53] IBM,Seedingtheclouds:keyinfrastructureelementsforcloudcomputing,February2009.
[54] K.S.Pawar,U.Menon,J.C.K.H.Riedel,Timetomarket,IntegratedManufacturingSystems5(1)(1994)14–22.
http://cloudslam09.com/content/confronting-data-center-crisis-cost-benefit-analysis-ibm-computing-demand-cod-cloud-offering.
[55] J.Koomey,K.Brill,P.Turner,B.Taylor,J.Stanley,Asimplemodelfordeterminingtruetotalcostofownershipfordatacenters,UptimeInstitute.
http://www.missioncriticalmagazine.com/MC/Home/Files/PDFs/(TUI3011B)SimpleModelDetermingTrueTCO.pdf.
[56] http://web2.sys-con.com/node/640237.
[57] J.Hoffer,Backingupbusiness—industrytrendorevent,HealthManagementTechnology.http://www.accessmylibrary.com/coms2/summary_0286-
10537060_ITMJanuary2001.
[58] Nathesh, Green technology—aberdeen report reveals advantages of green retail initiatives, August 14, 2008. http://green.tmcnet.com/
topics/green/articles/37018-aberdeen-report-reveals-advantages-green-retail-initiatives.htm and http://www-935.ibm.com/services/uk/cio/pdf/
oiw03022usen.pdf.