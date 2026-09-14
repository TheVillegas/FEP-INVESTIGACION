                                               Mathematical and Computer Modelling 53 (2011) 504–521



                                                    Contents lists available at ScienceDirect


                                   Mathematical and Computer Modelling
                                             journal homepage: www.elsevier.com/locate/mcm




Identification of a company’s suitability for the adoption of cloud
computing and modelling its corresponding Return on Investment
Subhas Chandra Misra ∗ , Arka Mondal 1
Department of Industrial and Management Engineering, Indian Institute of Technology, Kanpur, India



article              info                           abstract
Article history:                                    Internet has become pervasive in our daily life and cloud computing is the newest offering
Received 1 November 2009                            as service over the ubiquitous Web. Cloud computing has been considered as a much hyped
Received in revised form 15 March 2010              phenomenon in the IT and business world promising to deliver a host of benefits. Compa-
Accepted 16 March 2010
                                                    nies need to look beyond this hype and seriously consider the real value of incorporating
                                                    the Cloud in their own businesses. This paper is aimed at helping companies analyze several
Keywords:
                                                    characteristics of their own business as well as pre-existing IT resources to identify their fa-
Cloud computing
Return on Investment (ROI)
                                                    vorability in the migration to the Cloud Architecture. A general Return on Investment (ROI)
Benefits of cloud computing                         model has also been developed here taking into consideration various intangible impacts
Cost of cloud computing                             of Cloud Computing, apart from the cost. The analysis presented herein provides a much
                                                    broader perspective and insight into Cloud Computing to its prospective adopters.
                                                                                                         © 2010 Elsevier Ltd. All rights reserved.


1. Introduction

    Cloud computing (CC) [1] is a paradigm shift in computing with the potential of changing the whole perspective with
which we look at computing today. Currently, desktops, laptops and numerous such devices have penetrated into our daily
lives and have become indispensable [2]. It will not be too long from now that all we will need to know is that there is
one huge computer at a remote location (without even knowing where it is) which has the potential to provide all the
computational power and resources that we ever really need.
    CC can be defined as collection disembodied services accessible from anywhere using any mobile device with an Internet
connection, provided by a type of parallel and distributed system of virtualized computers that are interconnected and
that can be dynamically provisioned and presented as one or more unified computing resources based on Service-Level
Agreements (SLAs) established between the service provider and the user [3–5].
    In this paper, we analyze some of the economic aspects of migration to cloud architecture. Specifically, we attempt to
model ROI in using CC in organizations. Studies of the economic aspects, in general, and ROI, in particular, are important
organizational considerations in the adoption of any new technology. In the context of Grid Computing [6,7], for example,
works (e.g., [8–16]) relating to these aspects exist. As CC is an important technological trend, it is also important to study
these economic aspects of CC.
    There are different cloud delivery models (e.g., [3,17,18]) based on pay-per-use models, viz., Software-as-a-Service (SaaS),
Platform-as-a-Service (PaaS) and Infrastructure-as-a-Service (IaaS). Software-as-a-Service (SaaS) may be described as a
process by which different software applications are provided by the Application Service Provider (ASP) as a rental over
the Internet leveraging cloud infrastructure. This eliminates the necessity for installing and running the application on
the customer’s own computer. It also diminishes the tremendous load of software maintenance, ongoing operation and


 ∗ Corresponding author.
   E-mail address: s_c_misra@yahoo.com (S.C. Misra).
 1 Current Address: Motilal Nehru National Institute of Technology, Allahabad, Uttar Pradesh, India.

0895-7177/$ – see front matter © 2010 Elsevier Ltd. All rights reserved.
doi:10.1016/j.mcm.2010.03.037
                                     S.C. Misra, A. Mondal / Mathematical and Computer Modelling 53 (2011) 504–521                  505


support [3]. Platform-as-a-Service (PaaS) is an entire virtualized platform. It includes one or more servers, operating systems,
specific applications and development platforms provided as a service over the Internet for developers to build applications
on Infrastructure-as-a-Service (IaaS) is the delivery of computer infrastructure as a service. Infrastructure includes servers,
processing power and storage. This helps in the elimination of upfront capital cost and is of immense benefit to companies
who want to start small [17,18] and also relieves them of their need to forecast their demands of the future and provision
accordingly.
    There is no doubt about the paramount potential of CC, but it is yet to cross its stage of infancy, with only a limited
number of takers currently, owing to some of the challenges of its widespread adoption such as security, trust, and cost-
effectiveness [19,2]. It is estimated that 71% of companies believe that cloud computing is a real technology option. 70% hold
that it would make their business flexible. 62% think that it would help them react quickly to market conditions and 65% fee, it
would help increase focus on core business [20]. However, in reality, there are only very few companies which are actually
using CC. It is because of the lack of proper understanding of the cloud architecture, its pricing model and its suitability
to the different requirements and scenarios of different companies with different business environments. These form the
motivation behind the work presented in this paper.
    The rest of the paper is organized as follows: In Section 2, we provide the background and motivation of this work.
Section 3 gives the guidelines that identify the suitability of a company for the adoption of the CC, while in Section 4, we
derive our ROI model. Finally, we conclude the paper in Section 5.

2. Background and motivation

    Considering the way adoption of CC can revolutionize the business scenario as it has revolutionized the research scenario,
some work has been done in this field. In [3], Pyke has supported the potential of CC in business and explained how it is
a paradigm shift from what we have known traditional computing to be, and how to tell if the application is in the cloud
or not. He also dealt with the technicalities for the implementation of CC and its delivery to customers. The various layers
in the cloud infrastructure and some delivery models have been exhaustively covered in [4]. The authors have also dealt
with market-oriented2 resource allocation of Clouds by leveraging the third generation Aneka enterprise Grid technology.
Some works (such as [24,25]) have perceived the likelihood of CC becoming the fifth utility after electricity, water, gas and
telephony.
    Comparisons of CC to other forms of computing such as grid computing (desktop grids) and volunteer computing have
been made in [26]. The benefits of CC, the challenges faced in the implementation of the cloud architecture, the opportunities
in their solution and the various risks that users might have to undertake for migration to the cloud have been explained
in [17]. The authors also proposed a tradeoff equation which indicates which technology can give more profit.
    Different cloud services provided by the different service providers along with their costs and characteristics have been
compared in [27,28].
    Reports and inferences drawn from various global surveys carried out for CC have been mentioned in [20,29,18,30]. Also,
various types of cost–benefit analysis of cloud have been reported in [31–34], giving direct figures of costs that are included.
Currently, there also exists debates in various blog sites between primarily two groups divided on the opinion of profitability
of the cloud. One group finds the cloud to be cost saving, while the other finds it to be more expensive. ROI of implementing
CC has also been calculated in a few cases (viz., [27]), but pertaining only to specific companies. Even cost analysis of whether
e-mail servers should be moved to the cloud is given in [34]. But none of these sources are fundamentally similar in context
and scope of this paper which neither measures the suitability, nor gives a generic model for the calculation of ROI. Dargha’s
work [35] is based on the principle that this paper has followed for finding the suitability index. But the present work
provides a much deeper insight. It defines a number of factors to be considered prior to adopting CC. In this paper, we have
more criteria over and above the major criteria. This makes analysis more meaningful. The present work also provides both
objective and subjective tools for the present analysis as well as for decision making.
    Some previous researchers (e.g., [24,25]) have also studied the cost–benefit analysis of CC, but their works pertain to the
data of single companies. Only direct costs have been included in their discussions, but as such a generic model containing
variables [24,25] which should be applicable to any and all companies—big or small, well established or start-ups, has not
been explored.
    A contemporary survey has found out that the current pricing pattern and other factors of the cloud make it highly
suitable for small and medium enterprises [18]. Currently, CC may not be very suitable for big enterprises. However, no
criteria have been set forth to consider the factors which make a company big, medium or small. It is yet to be decided
whether the criteria should be based only on their annual revenue or some other factors as well.
    The ROI model has been limited only to the accounting of costs of the cloud, the savings made from it or the extra amount
to be spent on it. No valuation has been given to the intangible benefits of CC (e.g. [24,25]). Intangible benefits have been
limited only to its mention in certain sources.
    CC has so far been viewed primarily from the perspective of cost. This paper tries to broaden that outlook with a model
that helps not just identify the suitability of a company for the cloud by clearly spelling out all the factors that need to be
considered for the same, but also tries to give a certain profitability valuation of the benefits associated with CC.

 2 It is worth noting that similar works in the context of Grid Computing also exist in the literature. Examples include [21–23].
506                             S.C. Misra, A. Mondal / Mathematical and Computer Modelling 53 (2011) 504–521


    The CC architecture consists of three main players—Cloud Providers, Cloud Users or Customers and Cloud Vendors [36].
In this paper we would be primarily looking from the cloud user point of view. Two types of business models can be drawn
for the enterprises (cloud users) willing to adopt CC services. They are:
 i. Business model for companies with existing IT infrastructure.
ii. Business model for startup companies.
    Startup companies are the most eligible candidates for the adoption of CC [18] because of the starkly visible benefits that
CC offers in the form of no upfront capital investment in having to buy servers, buildings and floor space to build datacenters,
no electricity, cooling costs, no purchase of software licenses, etc. thus there are no barriers to entry. These companies can
start small and can invest in the increase of hardware resources as their business flourishes or only when there is an increase
in their needs [17].
    The challenge comes when making a decision for companies with an already existing and working datacenter (IT
infrastructure) on whether CC would be appropriate for the organization and they should embark on the cloud or they
should stick to their own in-house infrastructure and invest in their expansion and consolidation [37]. It is expected that
this present paper will find use in this regard.

3. Identification of a company’s suitability for the adoption of CC

    Some of the key characteristics of the resources possessed by a company to be considered before hopping onto the cloud
‘‘bandwagon’’ are:
  I. Size of the IT resources.
 II. The utilization pattern of the resources.
III. Sensitivity of the data they are handling.
IV. Criticality of work done by the company.

3.1. Size of IT resources

    Largeness of the resources already present in a company plays a very vital role in the cost factor. The larger the volume
of the resources, the lesser is the per capita cost of operating these resources, owing to the economics of scale [17,38–40].
This economics of scale causes TCO of datacenters to reduce their size increases. It then becomes much cheaper and more
beneficial in the long run than using the cloud services. Thus, it may not be economically viable, or for that matter profitable,
for companies with sufficiently large datacenters to drop their own infrastructure and head towards the cloud. Considering
all relevant factors, however, cloud computing has been found to be more suitable for small and medium size business
enterprises [18].
    Some of the factors that are taken into account, while determining the size of the IT resources of a company are:
1. The number of servers the company maintains in its datacenters.
2. The size of the customer base of the company.
3. The annual revenue from IT.
4. The number of countries across which the company is spread over [35].

3.1.1. Number of servers
a. Less than 100 servers . . . (small).
b. From 101 to 2000 servers . . . (medium).
c. From 2001 to 10,000 servers . . . (large).
d. 10,001 to 50,000 servers . . . (very large).
e. 50,001 to 100,000 servers . . . (super large).
 f. Above 100,000 servers . . . (IT giants).
    Categories ‘e’ and ‘f’ do not count. Category ‘e’ belongs to companies like Akamai Technologies, 1&1 Internet,
Rackspace [20], etc. which maintain or rather host huge ‘server farms’.
    It may so happen that in their servers a large part of the Internet resides. If it is so, it would not be meaningful for them to
go for the clouds because they make their money by maintaining servers for other companies. Category ‘f’ belongs to huge
hulking IT giants such as Google, Amazon, and IBM [41]. They too do not count because they themselves are as such some
of the key players providing CC services.

3.1.2. Size of customer base
    The size of the customer base or the number of users of the services offered by a company is a very good yardstick in
estimating the size of the internal resources maintained by an organization for its smooth functioning and service delivery.
It also gives a picture of the utilization pattern of the in-house datacenter resources. A wide geographical distribution of the
customer base of a company would give a more or less constant workload pattern [35].
                                S.C. Misra, A. Mondal / Mathematical and Computer Modelling 53 (2011) 504–521                507




                                            Fig. 1. Moderately variable workload with no surges.


3.1.3. Annual revenue from IT offerings
   The amount of revenue generated from the IT resources of a company goes a long way in deciding whether it should still
maintain the expensive yet convenient datacenters or should it adopt seamless switch over to the cloud.
a. Less than $ 100 million . . . (small).
b. Between $ (100–500) million . . . (medium).
c. Above $ 500 million . . . (large).

3.1.4. Number of countries IT is spread across
    The greater the number of countries [35] a company and its datacenters are spread in, the greater the pool of its internal
resources facilitating larger benefit from economies of scale and thus reducing its operational cost. Also, if the company has
its presence felt in a number of countries, then its workload can be assumed to be quite constant which might reduce its
suitability for the adoption of cloud services [17,35].
    Some categories we can break them up into:
a. One country.
b. More than one but less than four countries.
c. Less than or equal to six countries.
d. Less than ten countries.
e. Above 10 countries.

3.2. Utilization pattern of the resources

    Merely having large or small resources does not make it beneficial for a company to respectively abstain from or embark
on the cloud services. Profitability also depends on the amount of utilization of the existing resources. A large number of very
underutilized (too much over provisioning) server resources leads to a large amount of wastage and hence makes it suitable
for using cloud services, whereas small yet perennially well utilized servers would not be economical if taken to the clouds.
McKinsey report states that the global average server usage tops at 5%–10% only. This happens as a result of provisioning
for the peaks, the sudden spikes & surges. It is a very daunting task to accurately forecast workload requirements. This task
gets even more aggravated in businesses which depends on web applications and whose workload varies a lot more than
traditional business applications [18]. CC is beneficial for companies especially if there are highly variable spikes in resource
demand [17].
    We can determine the utilization pattern by:
a. Average usage.
     i. The type of services offered by the company.
    ii. The number of users using the services, i.e., same as customer base.
   iii. The number of projects undertaken.
b. Peak usage.
    i. The duration of peak usage/year.
   ii. The number of times the peak value is of the average value.
c. Amount of data handling/transactions done.
Average and peak usage patterns.
  Let us look into some of the normal workload variability patterns found in enterprise installations:
• Profile 1: Moderately variable workload with no surges [42] (Fig. 1).
• Profile 2: Highly variable workload with spikes [42] (Fig. 2).
• Profile 3: No variability constant workload (Fig. 3).
• Profile 4: Moderately variable workload with occasional surges (Fig. 4).
508                            S.C. Misra, A. Mondal / Mathematical and Computer Modelling 53 (2011) 504–521




                                               Fig. 2. Highly variable workload with spikes.




                                                 Fig. 3. No variability constant workload.




                                       Fig. 4. Moderately variable workload with occasional surges.




                                              Fig. 5. Variable workload with long averages.


• Profile 5: Constant workload but workload pattern varies at different times of the year owing to different types of project
      undertaken (Fig. 5).
      Type of services offered by a company.
      Table 1 shows some examples of types of services offered by a company.
Type of projects undertaken
   In this work, the type of a project refers to the degree of computationally intensive processes required to complete a task.
This criterion may not be applicable for all organizations especially for those enterprises which provide web applications
or internet services. These are meant for those enterprises which are involved in the various computationally intensive
jobs, e.g., research laboratories involved in nuclear research, drug design, weather forecasting, etc. or companies involved in
                                     S.C. Misra, A. Mondal / Mathematical and Computer Modelling 53 (2011) 504–521                                   509


Table 1
Some of the different types of online services offered by companies.
 Service offered                      Workload profile             Surges in workload and their duration

 Social networking                    3                            –
 Search engines                       3                            –
 Online book store                    4                            New book releases. Lasts for a few days only.
 E-mail                               1                            –
 Gaming portals/arcades               3                            –
 Marriage sites                       2                            During marriage season. Usually lasts for 1 or 2 months in a year.
 Banking/finance                      3                            –
 Newsrooms                            4                            During sudden break of big events, disasters. Lasts from a few hours to a few weeks.
 Software providers                   2                            New software releases. Lasts for a few weeks.
 Video/music sites                    3                            –
 Downloadable sites                   –
 Jobs site                            1                            –
 Pornography sites                    3                            –
 Online ticketing                     4                            During holiday seasons, festivals, disasters. Lasts for a few weeks.
 Stock brokerage                      4                            Sudden fall or rise of SENSEX. Lasts for a few hours.
 Photo sharing sites                  2                            After holiday season. Lasts for a few weeks.
 Online shopping/auction              2                            During lottery. Lasts for a few minutes only.


developing high-end animation and special effect movies and games or companies which are involved in the development
of various softwares and applications. Thus, type of project also plays a crucial role in determining the average workload
pattern of any organization.
Peak usage
   Peak usage is the maximum utilization of the computational resources present in an organization. Peak value is reached
when the demand suddenly increases and reaches its maximum value. Hence, they are often known as surges or spikes. But
they may be very discrete, intermittent and sporadic. If the organization resources are provisioned for these peaks, then it
leads to large wastage of idling resources. Highly variable workloads are more suitable for the clouds than constant ones [17,
18]. Peak usage can be measured in terms of:
 i. Duration of peaks. If the peaks are quite frequent, then the aggregate duration of the peaks may become worthwhile for
    provisioning in the organization’s own datacenter. But if this duration does not accumulate to a substantial amount, then
    provisioning for these peaks would tantamount to large wastage of resources [42] and hence opting for CC would be a
    viable option.
       Aggregate duration of these peaks in a year has been categorized into:
    • Few hours.
    • Few days.
    • Few weeks (less than or equal to 3).
    • Few months (less than or equal to 3).
ii. Peak by average value.
       Provisioning for workload patterns with the value of peak a few multiples of the average value would draw large
    wastage of precious resources. If not provisioned, it would result in a large number of unsatisfied customers or delay
    in product delivery. Highly scalable and dynamically allocated resources of the cloud would be the best option in these
    scenarios.
       Peak by average value has been categorized [17,43] into:
    • Less than twice . . . (least wastage).
    • Less than five times.
    • Less than ten times.
    • Above ten times . . . (huge wastage).
Amount of data handling
   Amount of data handled, acted upon or generated in a day also should play a significant role in a company’s decision to
move for the CC services [17]. Huge amount of data acted upon would require a large bandwidth concerning data processing
and storage in the cloud environment [44,45]. This would cause substantial amount of money to be spent on bandwidth
charges alone, which would be detrimental for the adoption of CC in the long run. For example, CERN, the European
Organization for Nuclear Research, generates terabytes of data each day from its nuclear research in its laboratories. If all
these data were to be sent to the clouds for processing as well as storage and also recalled regularly for analysis, firstly it
would take a huge amount of time for transfer. Also, the bandwidth charges alone would be a significant portion from their
budget, apart from the charges of storage of such huge amount of data in the clouds.
   In this case, the categories have been sub-divided into:
a. Above 100 terabytes/month.
b. 1–100 terabytes/month.
510                                 S.C. Misra, A. Mondal / Mathematical and Computer Modelling 53 (2011) 504–521


Table 2
Categorizing sensitivity of data.
  Category                                      Data

                                                Information and data of government federal and intelligence agencies like CIA, FBI.
  Extremely sensitive                           Blue prints and information regarding weapon systems, artillery, aircrafts, etc. of the defense forces.
                                                Matters concerning national security [21].
                                                Bank related data like bank accounts, passwords, pin, transactions and balances, etc.
                                                Financial data of companies, quotations for various tenders, etc.
                                                Company databases.
  Very sensitive
                                                Ongoing confidential research. Trade secrets, drug formulas, early research findings [21].
                                                Source codes.
                                                E-mail accounts.
                                                Personal information such as name, contact details, e-mail-ids, profiles.
  Sensitive
                                                Patient records, health records [21].
                                                Pictures, videos in social networking websites.
  Less sensitive                                Click stream data.
                                                Service usage details.
                                                Free software, music, videos, pictures, games, news, articles.
  Not sensitive                                 Views & comments in blogs.
                                                Anything downloadable which is authorized.


c. 500 gigabytes–1 terabytes/month.
d. 100–500 gigabytes/month.
e. Below 100 gigabytes.

3.3. Sensitivity of data handled

   One of the major apparent shortcomings of CC, which prevents it from being a runaway success is the concern for the
security of data governance [46] in the cloud environment. Though there has been huge advancement in security and there
are no fundamental difficulties as such in making the cloud a high security density zone with well understood encryptions,
data firewalls, and packet filters [17], but it is yet to be tested exhaustively in the real life. Data security becomes more of
an issue as the sensitivity of the data handled by a company increases. Concerns of data lock-in in case of outages and data
availability in the long run in case a cloud provider goes out of business aggravates the problem. Data needs to be protected
from unauthorized disclosure, fraud, waste or abuse at all costs [47,19].
Sensitivity of data has been categorized as in Table 2:

3.4. Criticality of work done by the company

   Highly critical work requires the most stringent of resources, platforms, applications and security. The more critical the
work gets, the more demanding gets the requirements. Thus very critical work may not find suitability to the cloud as it
would require very stringent Service-Level Agreements (SLAs) [35] with the cloud provider. If the company is not very big,
then the cloud service providers may not be very willing to provide the highly customized Service-Oriented-Architecture
(SOA) and Application Programming Interfaces (APIs). They may not even be able to deliver the Quality-of-Service (QoS) [4,
19,48–51] in processes requiring very low latencies [17,35] owing to constraints of the system or lack of profitability and
feasibility on their part.
   Criticality of services can be categorized into:
   Highly critical . . . (may not be suitable for the cloud).
   Critical . . . (may be suitable if company is large).
   Less critical . . . (suitable).
   Standard . . . (easily suitable).
Tabulation sheet
    All the factors have been assigned various credits (weights) according to their relative importance in the factor which
constitutes them. The credits that have been already assigned may work for certain companies, but certainly not for all
companies. The credits may be customized by the companies, depending on the importance of the characteristics for them
or their business. Table 3 acts as an initial guide in arriving at the decision of whether or not CC is suitable for an organization
and should not be considered as the definitive and the only tool for the same.3 In-depth analysis should be carried out and
various other factors at the company level should be considered before taking a final leap in embarking to the clouds.


  3 Owing to change in market conditions the outcome of this study may differ. An in-depth (subjective as well as objective) analysis is strongly
recommended and will be required when applying for personalized businesses as other factors may also arise.
                             S.C. Misra, A. Mondal / Mathematical and Computer Modelling 53 (2011) 504–521             511




Table 3
Tabulation sheet.
                    Characteristics                                                                          Credits

                    Size of IT resources                                                                     7
                    Number of servers                                                                        8
                      Less than 100 servers                                                                  4
                      From 101 to 2000 servers                                                               3
                      From 1001 to 10,000 servers                                                            2
                      10,001 to 50,000 servers                                                               1
                    Number of countries it is spread across                                                  4
                      One country                                                                            5
                      More than one but less than four countries                                             4
                      More than equal to four but less than equal to six countries                           3
                      More than six but less than ten countries                                              2
                      Above 10 countries                                                                     1
                    Annual revenue from IT offerings                                                         4
                      Less than $ 100 million                                                                3
                      Between $ (100–500) million                                                            2
                      Above $ 500 million                                                                    1
                    Workload variability                                                                     8
                    Peak usage                                                                               6
                    Duration of peak usage/year                                                              6
                      Few hours                                                                              4
                      Few days                                                                               3
                      Few weeks (less than equal 3)                                                          2
                      Few months (less than equal 3)                                                         1
                    Peak by average                                                                          9
                      Less than twice                                                                        1
                      Less than five times                                                                   2
                      Less than ten times                                                                    3
                      Above ten times                                                                        4
                    Average usage                                                                            8
                    Type of services                                                                         5
                      Profile 1                                                                              2
                      Profile 2                                                                              4
                      Profile 3                                                                              1
                      Profile 4                                                                              3
                    Type of projects undertaken                                                              5
                      Profile 1                                                                              2
                      Profile 3                                                                              1
                      Profile 5                                                                              3
                    Size of user/customer base                                                               7
                      Above 10 million                                                                       1
                      100,000 to 10 million                                                                  2
                      Below 100,000                                                                          3
                    Amount of data handling                                                                  5
                      Above 100 terabytes/month                                                              1
                      1–100 terabytes/month                                                                  2
                      500 gigabytes–1 terabytes/month                                                        3
                      100–500 gigabytes/month                                                                4
                      Below 100 gigabytes.                                                                   5
                    Sensitivity of data                                                                      6
                      Extremely sensitive                                                                    1
                      Very sensitive                                                                         2
                      Sensitive                                                                              3
                      Less sensitive                                                                         4
                      Not sensitive                                                                          5
                    Criticality of work done                                                                 4
                      Highly critical                                                                        1
                      Critical                                                                               2
                      Less critical                                                                          3
                      Standard                                                                               4
512                              S.C. Misra, A. Mondal / Mathematical and Computer Modelling 53 (2011) 504–521


Calculations
Various calculations can be carried out using the following formulae:

         Largeness value (L) = NoS × CNoS + NoC × CNoC + AR × CAR .
         Average Usage value (AU) = ToS × CToS         (or)    ToP × CToP + (4 − SCB) × CSCB .
         Peak Usage value (PU) = DoP × CDoP + PbA × CPbA .
         Value of Workload Variability (WV) = PU × CPU + AU × CAU + ADH × CADH .
         Value of Data Sensitivity (DS) = SoD.
         Value of Criticality (C ) = CWD.

      Finally,

         Suitability index = L × CL + WV × CWV + DS × CDS × ADH + C × CC × (65 − L).

      Here,

 NoS = Number of Servers
 CNoS = Credit of Number of Servers
 NoC = Number of Countries it is Spread Across
 CNoC = Credit of Number of Countries it is Spread Across
 AR = Annual Revenue
 CAR = Credit of Annual Revenue
 SCB = Size of Customer Base
 CSCB = Credit of Size of Customer Base
 ToS = Type of Service
 CToS = Credit of Type of Service
 ToP = Type of Project
 CToP = Credit of Type of Project
 DoP = Duration of Peak
 CDoP = Credit of Duration of Peak
 PbA = Peak by Average
 CPbA = Credit of Peak by Average
 CPU = Credit of Peak Usage
 CAU = Credit of Average Usage
 ADH = Amount of Data Handling
 CADH = Credit of Amount of Data Handling
 CWV = Credit of Work Variability
 CC = Credit of Criticality.

For calculation of the upper limit we consider values on the higher side from the table.

 NoS = 3, NoC = 4 and AR = 2.5.
 As provided in the table CNoS = 8, CNoC = 4 and CAR = 4.
 Now, L = NoS × CNoS + NoC × CNoC + AR × CAR .
 Using these values we get, L = 3 × 8 + 4 × 4 + 2.5 × 4 = 50.
 Then, ToS = 3, SCB = 2.5.
 As given in the table CToS = 5, CSCB = 7.
 Now, (AU) = ToS × CToS (or) ToP × CToP + (4 − SCB) × CSCB .
 Using these values we get, AU = 3 × 5 + (4 − 2.5) × 7 = 25.5.
 Please note that decimal or fractional values can also be obtained from the table by breaking them into smaller groups.
 Similarly, DoP = 3, PbA = 3. From chart CDoP = 6 and CPbA = 9.
 We know, (PU) = DoP × CDoP + PbA × CPbA .
 Therefore, PU = 3 × 6 + 3 × 9 = 45.
 Now, WV = PU × CPU + AU × CAU + ADH × CADH . Here ADH = 4 and CADH = 5, CPU = 6 & CAU = 8.
 Therefore WV = 45 × 6 + 25.5 × 8 + 4 × 5 = 494.
 DS = 4, C = 3;
 Now, Suitability index = L × CL + WV × CWV + DS × CDS × ADH + C × CC × (65 − L), where CL = 7, CWV = 8,
 CDS = 6 & CC = 4.
 Therefore, Suitability index = 50 × 7 + 494 × 8 + 4 × 6 × 4 + 3 × 4 × (65 − 50) = 4578.
 Leaving some margin we get the value to be around 4600.
                                    S.C. Misra, A. Mondal / Mathematical and Computer Modelling 53 (2011) 504–521             513




                                                Fig. 6. Suitability of a company for adoption of cloud.


Similarly, for calculation of the lower limit we consider values on the lower side from the table.
 NoS = 2, NoC = 2 and AR = 1.5.
 As provided in the table CNoS = 8, CNoC = 4 & CAR = 4.
 Now, L = NoS × CNoS + NoC × CNoC + AR × CAR .
 Using these values we get, L = 2 × 8 + 2 × 4 + 1.5 × 4 = 30.
 Then, ToS = 2, SCB = 1.5. As given in the table CToS = 5, CSCB = 7.
 Now, (AU) = ToS × CToS (or) ToP × CToP + (4 − SCB) × CSCB .
 Using these values we get, AU = 2 × 5 + 2.5 × 7 = 27.5.
 Please note that decimal or fractional values can also be obtained from the table by breaking them into smaller groups.
 Similarly, DoP = 2, PbA = 2. From chart CDoP = 6 & CPbA = 9.
 We know, (PU) = DoP × CDoP + PbA × CPbA .
 Therefore, PU = 2 × 6 + 2 × 9 = 30.
 Now, WV = PU × CPU + AU × CAU + ADH × CADH . Here ADH = 2 and CADH = 5, CPU = 6 & CAU = 8.
 Therefore WV = 30 × 6 + 27.5 × 8 + 2 × 5 = 410.
 DS = 2, C = 2;
 Now, Suitability index = L × CL + WV × CWV + DS × CDS × ADH + C × CC × (65 − L) where CL = 7, CWV = 8,
 CDS = 6 & CC = 4.
 Therefore, Suitability index = 30 × 7 + 410 × 8 + 2 × 6 × 2 + 2 × 4 × (65 − 30) = 3794.
 Leaving some margin we get the value to be around 3760.

Interpretation of results
    On doing the calculations a numerical value would be obtained. If the numerical value obtained for a particular
organization is below 3760 then it would not be recommended to be suitable to adopt CC.
    A result obtained between 3760 and 46004 is considered moderate i.e. it may or may not be beneficial for them to go for
the cloud. Further investigation would be required and other factors at the company level should be taken into consideration
in order to arrive at the decision whether the cloud services would be viable in the long run. A company could look at other
options in these cases such as partial adoption of cloud services or adoption of virtualization techniques in its already existing
datacenters.
    A score above 4600 would indicate that the company needs to adopt CC in order to enjoy large cost savings and other
benefits that come along with CC.
    The above is shown pictorially in Fig. 6.
    It is important to note that the cut-off scores given here are suitable for the credits given to the factors in the table and
would only apply to those companies which keep the same weightage to the various factors. Customizing the credits of
the various factors to suit certain needs would cause the cut-off scores to change accordingly. The lower and upper cut-off
scores are obtained by taking the lower average and the upper average of the factors respectively.
    It should also be noted that owing to change in market conditions the outcome of this study may differ. An in-depth
(subjective as well as objective) analysis is strongly recommended and will be required when applying for personalized
businesses as other factors may come into the picture.

4. ROI

    The discussions presented in Section 3 serves as a pointer in determining whether CC is advisable for an organization or
not. A lot of time and resources are spent in calculating ROI by taking into consideration a large number of factors involved
in a business. The indication given by the marker would give an image of how the ROI would look like and the pain and effort


 4 These scores are obtained by taking the lower and upper averages of the factors respectively.
514                            S.C. Misra, A. Mondal / Mathematical and Computer Modelling 53 (2011) 504–521




                                               Fig. 7. Schematic diagram of traditional ROI.




                                     Fig. 8. Schematic diagram of costs for partial migration to cloud.


spent in calculating the ROI would be worth it. In other words, it would give an assurance that the ROI would be positive if
a positive indication is given by the marker. If a negative indication is given by the table, the ROI calculated could certainly
come out to be a negative one and the effort that would be spent in calculating the ROI may not pay off.
Calculating ROI
   ROI is a tool for measuring the efficiency of any investment. For calculating ROI, as shown in Fig. 7, we need the initial
cost of project, the investment made, the cost savings done owing to the new investment [52].

              (Initial cost − Final cost) − Investment          Costs saved − Investment
      ROI =                                                 =                                    .                            (1)
                             Investment                                  Investment
It thus turns out that for calculating the ROI of CC, we need to understand what these cost savings, the initial costs and the
investments mean in the cloud model.
    No initial investment is required for migration to the clouds, i.e., there is no upfront capital cost. Embarking on the cloud
can be as easy as browsing through a catalogue of IT services, adding them to a shopping cart and submitting the order. As
soon as the order is approved by an administrator, the rest of the things are done by cloud [53] The cost of using the cloud
services is completely operational in nature. Hence, in this case the investment is on a monthly or yearly basis using the
pay-per-use cost of the cloud services. The initial project cost is the total cost of ownership (TCO) of maintaining one’s own
datacenter before using cloud services. Cost saved would be the entire elimination of datacenter cost (in case of complete
migration) or the reduction in datacenter cost (in case of partial migration). Fig. 8 shows the schematic diagram of costs for
partial migration to cloud.
    However, the economics of CC does not end here. Associated benefits of CC such as massive scalability, flexibility of
service, elasticity of resources, and latest technology offering add to the profitability of the enterprise cloud user. Therefore,
as shown in Fig. 9,

                        Increase in profit + Reduction in cost − Cloud costs
      ROI for cloud =                                                                     .                                   (2)
                                                 Cloud costs
Here, the time frame can be per month or per year.
ROI model
   Let us consider a case of a moderate value on the tabulation sheet in Section 3. For such an enterprise, the best way of
using the cloud services would be to simultaneously maintain its own datacenter as well as use the cloud services for the
extra resources which cannot be provisioned in its own datacenter [4,42].
   Considering their average workload, they can maintain 30% above this average value in their in-house datacenter and
outsource the rest of the computational needs to the cloud. Only when 80% of the in-house server capacity has exceeded,
                                      S.C. Misra, A. Mondal / Mathematical and Computer Modelling 53 (2011) 504–521        515




                                                                  Fig. 9. View of profits.




                                                          Fig. 10. Partial cloud migration model.



the excess capacity would be drawn from the cloud.
                                         ∫ T                                      
                                                                110
      Cost of cloud per year =                       W (t ) −         × average · dt
                                             0                  100
                                         × cloud cost + (storage in clouds) × (cost/month) × 12
                                         + bandwidth cost + cost of using applications.                                     (3)
      Bandwidth cost = (incoming data + outgoing data) per year × bandwidth charges.                                        (4)
                                             −   j
      Cost of using applications =                   Tn × An                                                                (5)
                                             n =1

where,

   Tn = time (in hours) of usage of nth application/platform.
   An = cost of application per hour of usage as provided by the ASP.
            T 
The integral 0 W (t ) − 110
                                                     
                          100
                              × average · dt takes into consideration only the positive value, i.e., the part shown in Fig. 10.
   Aggregate workload can be calculated by using the formula given by Chari in [42]. Aggregate workload can be found out
by calculating the area under the workload curve.
   Hence,
                    ∫ T
      aggregate =            W (t ) · dt .                                                                                  (6)
                     0

The average workload can be calculated as
                   aggregate
      average =                   ,
                         T
where T is time frame in which it is calculated in hours.

      Traditional cost before cloud adoption = number of servers × cost behind each server.                                 (7)
      Cost behind each server or TCO = costs of (electricity + cooling + maintenance
                                       + manpower + software + backup power).                                               (8)

In-depth calculation of TCO can be done following the approach presented in [55].
516                                          S.C. Misra, A. Mondal / Mathematical and Computer Modelling 53 (2011) 504–521


Cost savings
   Since the in-house capacity is provisioned only for 30% above the average usage, and not for the peak, there is a significant
reduction in the number of servers that the company has to maintain in its own datacenter. The extra servers can be
decommissioned or sold. Therefore,

         Cost saved = (initial no. of servers − present no. of servers) × TCO of each server.                                 (9)

Valuation of intangible benefits leading to increased profits:
Agility/flexibility
   CC gives a company the ability to explore, experiment and innovate with better means such as better platforms, and
application tools in a quick and cost-effective way to come up with better services and solutions. This would give a great
boost to their business. Flexibility from CC adds value to an enterprise, but its value decreases with the increase in size of
the enterprise, i.e., this potential to be flexible may not add so much profitability to a large organization as it may do to a
small organization. Let profitability from flexibility be denoted by F.
   Then,

              constant (B)
                                                   
                                               B
         F=                     =                       .                                                                    (10)
                  f ( L)                 65 − L
The constant B can be the original annual profit which the company had before the adoption of cloud services.
   f (L) is a function of largeness. Value of L5 found from table should be substituted. This results in about 2% to 5% increase
in profit.
Scalability
   As such, scalability can be quantified by the amount of usage of extra resources which are automatically commissioned
with the increase in demand and charged on a pay-per-consumption basis. But the actual importance of scalability lies in
the fact that resources are made available in minutes, which otherwise would have taken weeks or even months. Scalability
also prevents dissatisfied customers as it scales the resources automatically when demand increases. Also, it leads to faster
time to market.
   Thus,

         Scalability = f (time value, customer satisfaction, faster time to market).                                         (11)

No separate formula is given for scalability, as the benefits of scalability have been quantified separately.
Faster time to market
   Apart from saving time in the faster provisioning of resources, companies using the technique of batch processing can
complete a work much faster than what their datacenter resources permit, e.g., using 1000 EC2 machines a work can be
done in one hour, which one machine would take 1000 h to complete and that too at essentially the same cost by leveraging
the concept of pay-per-use [17]. Faster time to market has many advantages such as one gets to have the entire market
share and thus s/he can charge a premium, as there is no other competitor in the market. Thus, one gets a lot of extra sales
and for extended period of time getting the opportunity to capture the loyalties of customers earlier. It also improves the
company’s technological and innovative image [54].
   The financial implications of faster time to market [54] can be represented graphically as shown in Fig. 11:
   Let us consider the relation function to be an approximate sine curve.
   We represent flow of money M (t ) = −A · sin(t ), where A is the estimated break-even cost.
                                ∫ t1                        ∫ t1
         Traditional cost =                  M (t )dt =               −A · sin(t ) · dt                                      (12)
                                    0                        0
                                    ∫ t2                     ∫ t2
         Traditional profit =                 M (t )dt =                −A · sin(t ) · dt                                    (13)
                                        t1                       t1

where,
      t1 = original time taken to market.
      t2 = time for which product stays in market.
      Let the time saved be 1t.

         Now, the reference line becomes y = −A · sin(t1 − 1t (Fig. 12)).                                                    (14)

Therefore,
                       ∫ t1−1t                                   ∫ t1′
         New cost =              (y − M (t ))dt =                        (−A · sin(t1 − 1t ) + A · sin(t ))dt .              (15)
                           1t                                      1t
                                      S.C. Misra, A. Mondal / Mathematical and Computer Modelling 53 (2011) 504–521                          517




                                                    Fig. 11. Relation of cost, revenue with time [54].




                                          Fig. 12. Relation of new cost, revenue with early time to market [54].


Here, the time taken from 1t does not necessarily imply costs being considered from time 1t after start of project. It is just
a representation for measuring costs.
    Also,
                         ∫ t2′                        ∫ t2′
       New profit =                (M (t ) − y)dt =           (−A · sin(t ) + A · sin(t1 − 1t ))dt                                          (16)
                           t1−1t                        t1′

where,
   t1′ = new time taken to market.
   t2′ = new time for which product stays in market.
   t2′ may be considered equal to t2.
Therefore,
       Value of faster time to market (FTM) = (traditional cost − new cost) + (new profit − traditional profit).                            (17)
Customer satisfaction
   Customer satisfaction is of high priority in any business. Transition to the cloud certainly add to the customer satisfaction
level. Quantification of benefits of CC calls for not the level of customer satisfaction achieved, but rather the increase of it.
   The increase of customer satisfaction6 can be measured by any of the general traditional methods of survey.
   Assuming a logarithmic7 curve,
                                                                                  
                                                                        1
       Percentage increase in profit8 = B × loge                                                                                            (18)
                                                                  1 − % increase
                                                                         100

where, % increase = (final% − initial%) of customer satisfaction.
   B is a constant whose value (varying from 8 to 15) depends upon the type of the services provided by the company and
also directly proportional to L (largeness value).
   The graph obtained by plotting various increase in customer satisfaction to increase in profit percentage is shown in
Fig. 13.
Time value
   Making IT resources available to end users becomes very time-intensive for the companies that employ traditional
datacenter management practices. It includes steps, such as purchasing hardware, building floor space, adequate power
supplies and cooling systems installing operating systems, middleware and software to be run in the servers, provisioning


 5 The value of L that we get from table is actually value of smallness. To get largeness we deduct it from (1 + max value), which is 65.
 6 Difference in percentage of customer satisfaction after and before adoption of cloud.
 7 This logarithmic function of customer satisfaction closely follows profitability when plotted.
 8 This is only a suggested formula and has no scientific backing behind it.
518                                  S.C. Misra, A. Mondal / Mathematical and Computer Modelling 53 (2011) 504–521




                                           Fig. 13. Increase in profit versus increase in customer satisfaction.


the network and the securing back up power. This process may take more than 2–3 months, depending to different
factors. IT organizations also take several weeks to re-provision existing hardware resources. CC dramatically alleviates this
problem through automation, business workflows and resource abstraction reducing the lead time required from months
to minutes [53]. This time saved in the cloud, which otherwise would have been spent provisioning for resources in the
datacenter can be quantified as the expenditure of the enterprise during that time of provisioning without any profits.
   Thus,

       Time value = (time taken to provision in weeks) × (weekly expenditure).                                                                      (19)

Focus on core competencies
    With no need to worry about the underlying infrastructure, their maintenance, their proper provisioning before the start
of any project, more attention and care can be given towards the development and the improvement of quality of services
and products of a company. Thus, better focus leads to improvement in productivity and its business propositions. Another
great advantage of CC is ubiquitous access or mobility, which allows employees to be productive from wherever they are
rather than confining them to their desks at the company [56].
    Improvement in productivity can be quantified in terms of decrease in marginal cost (Mc) and increase in marginal
benefits (Mb).
    Thus,

       Focus = (Mc + Mb) × number of products or services delivered/year.                                                                           (20)

Disaster recovery
   Disaster recovery is a very important aspect of enterprise computing. As devices, systems, and networks get increasingly
complex, there are many other things that can go wrong. Disaster may occur due to several causes including natural and
man-made ones. Natural sources include earthquakes, fires and anthropogenic sources that include viruses, power failure,
and intrusion.
   It is estimated that most large companies spend between 2%–4% of their budget and small and medium enterprises (SMEs)
spend up to 25% of their IT budget on disaster recovery planning, with the aim of avoiding larger losses in the event that
the business cannot continue to function due to loss of IT infrastructure and data. Of companies that had a major loss of
business data, 43% never reopen, 51% close within two years, and only 6% survive long-term [57]. Hence, disaster recovery
and business continuity planning are becoming increasingly important for every business organization.
   Disaster recovery planning is done by replicating resources in a number of places. This fear is very much reduced in the
cloud as data in the cloud is replicated thrice and stored in servers which are geographically scattered.

       Thus, savings from DR = (% budget9 invested in DR × annual budget)
                                        − bandwidth cost of storing new data daily to cloud − storage charges.10                                    (21)

Green IT
    An enterprise gets a ‘‘Green IT’’ tag when it helps save valuable natural resources. Green tag does improve the image
of a company and makes them more likely to be favored by people at the time of energy crisis. A recent survey has
found that the ‘green’ tag of companies alone were able to master a 17% increase in customer acquisition, 31% increase
in customer retention and a 69% raise in customer satisfaction. They have stated that the ‘Green route’ has helped improve


 9 This percentage is quite less than the original percentage which the company used to invest in DR as this is a model of partial migration to the cloud.
For entire migration it would be whole of it.
10 Bandwidth and storage charges are recurring but should not be taken into account here as it is already being paid as cost of usage of cloud.
                                    S.C. Misra, A. Mondal / Mathematical and Computer Modelling 53 (2011) 504–521          519


their customer loyalty [58]. Going by the modest of values that would lead to about 5% increases11 in annual profit. There
are also government incentives for companies trying to ‘go green’.
Risks
Outage of service
   This is one of the worst nightmares of CC, and this has happened a few times in the past [17]. But since this would be
an overlapping model with the cloud services being used, when datacenter capacity is exceeded, it may not adversely affect
the enterprise.

5. Conclusion

    This paper provides an in-depth analysis of the financial perspective of CC in a very lucid and simple manner. The
discussed model provides both the objective as well as the subjective decision making tool to find the suitability of a company
for adopting CC. With the suitability index presented in this paper, companies need not first waste their resources and time
in the calculation of ROI which is both time and effort consuming, and which may not yield a desirable result at the end. With
the suitability index customized to their needs, they can easily get a pointer as to where their company stands with respect
to its favorability to the adoption or migration to the cloud environment. Also depending on the score they get, they have a
number of options to choose from as to which model would suit their needs better. It is then that they can start calculating
ROI with the very simple yet generic model presented here which can again be customized to their specifications. Various
intangible benefits have been included in the model which gives a much broader picture of CC to its potential adopters.
Prospective adopters would really find it useful as it would save both their time and cost.
Managerial implications
    It is highly important for a company to remain competitive in today’s business scenario. To remain competitive in the
market they need to embrace the latest technologies, methodologies, processes, applications, etc. to come up with the best
services and products. For this managers in such organizations need to be very dynamic taking the best decisions which
would accelerate changes in business processes. These changes may vary from minor adjustments in ongoing processes,
to revolutionizing the entire business, systems and processes. They need tools which would assist them with proper
decision making. This model is one such tool that helps them understand the different models of CC, and the potential
outcomes/benefits of implementation of such models.
    Management of information systems is progressively becoming more difficult. As a result senior management including
CIOs and CFOs are being required to justify projects financially based on their return. Information systems have always
been difficult to quantify in profitability terms because most of the derived benefits are intangible by nature, e.g. improved
customer service. This paper attempts to incorporate various intangibles into traditional cost–benefit analysis and ROI. The
paper also reviews the suitability of the company to CC taking into consideration various parameters. This goes a long way
in assisting decision-making at the managerial level.
Performance analysis and scope for further work
    We have taken up the partial migration model for showing the costs and quantifying the benefits, because with this
model one can clearly showcase in good light all the various models of CC that can be adopted by companies along with
their cost and how they affect the ROI calculation.
    Companies which want to completely migrate to the cloud infrastructure would not have to incur any additional cost at
their own datacenter, other than only operational costs of the cloud. They would be saving the entire cost of running their
datacenter and whatever cost they incur from the cloud would be included as investment.
    Other cases include situations when a company opts for virtualization of the IT resources in its datacenter, i.e., creating
private cloud. Then, in that case, cost of virtualization that includes cost of VM middleware software license, its regular
updates would be added to the TCO of the servers maintained in its own datacenter.
    The expenditure of using the cloud services is completely operational in nature and that too on a pay-per-use basis. There
are absolutely no up-front costs or capital expenditure at the time of adoption or migration to the cloud services. But the
profits generated from the benefits of CC may not be of the same time frame as the cloud cost. The increased profits may
trickle in the later. In that case, considering the operational cost of the cloud as the investment and the time frame in which
increased profit is expected, Net Present Value (NPV) and Internal Rate of Return (IRR) can be calculated along with ROI.
    The profits from the benefits of CC shown here may not be applicable for all companies. So companies should customize
with scenarios that let them fit their model and incorporate only those costs and benefits in the calculation of their ROI.
    The model presented in this paper has been developed taking into consideration a large number of factors acting in the
IT industry and, hence, should work for a wide range of cases. But this model needs to be exhaustively tested with real
industry data, conditions and situations. Real company data would be able to ascertain the robustness of this model. Even
simulation data obtained by replicating the industry conditions on various software can be used to assess the practicality of
model analyzed by us. Thus, scope for future work includes rigorous testing of this model with real and simulated data.


11 Putting 69% in the customer satisfaction formula.
520                                    S.C. Misra, A. Mondal / Mathematical and Computer Modelling 53 (2011) 504–521


References

 [1] A. Weiss, Computing in the clouds, NetWorker 11 (4) (2007) 16–25.
 [2] A. Chien, B. Calder, S. Elhert, K. Bhatia, Entropia: architecture and performance of an enterprise desktop grid system, Journal of Parallel and Distributed
     Computing 63 (5) (2003) 597–610.
 [3] J. Pyke, Now is the time to take the cloud seriously. http://www.cordys.com/cordyscms_sites/objects/bb1a0bd7f47b1c91ddf36ba7db88241d/time_
     to_take_the_cloud_seroiusly_online_1_.pdf.
 [4] R. Buyya, C.S. Yeo, S. Venugopal, Market-oriented cloud computing: vision, hype, and reality for delivering IT services as computing utilities, in:
     Proceedings of the 2009 9th IEEE/ACM International Symposium on Cluster Computing and the Grid, vol. 00, 2009.
 [5] J. Broberg, S. Venugopal, R. Buyya, Market-oriented grids and utility computing: the start-of-the-art and future directions, Journal of Grid Computing
     6 (3) (2008) 255–276.
 [6] I. Foster, C. Kesselman (Eds.), The Grid: Blueprint for a Future Computing Infrastructure, Morgan Kaufmann, San Francisco, USA, 1999.
 [7] M. Chetty, R. Buyya, Weaving computational grids: how analogous are they with electrical grids? Computing in Science and Engineering 4 (4) (2002)
     61–71.
 [8] Alek Opitz, Hartmut König, Sebastian Szamlewsk, What does grid computing cost? Journal of Grid Computing 6 (4) (2008) 385–397.
 [9] Enis Afgan, Purushotham Bangalore, Computation cost in grid computing environments, in: 29th International Conference on Software Engineering
     Workshops, ICSEW’07, 2007, p. 9. ISBN 0-7695-2955-0.
[10] Zhengyou Liang, Ling Zhang, Shoubin Dong, Wenguo Wei, Charging and accounting for grid computing system, grid and co-operative computing,
     in: Lecture Notes in Computer Science, vol. 3003, ISBN: 978-3-540-21993-4, 2004, pp. 644–651.
[11] Roman Beck, Michael Schwind, Oliver Hinz, Grid economics in departmentalized enterprises, Journal of Grid Computing 6 (3) (2008) 277–290.
[12] Michael Schwind, Oliver Hinz, Roman Beck, A cost-based multi-unit resource auction for service-oriented grid computing, in: Proceedings of the 8th
     IEEE/ACM International Conference on Grid Computing, 2007, pp. 137–144. ISBN: 978-1-4244-1559-5.
[13] Dirk Neumann, Jochen Stößer, Christof Weinhardt, Jens Nimis, A framework for commercial grids-economic and technical challenges, Journal of Grid
     Computing 6 (3) (2008) 325–347.
[14] Daniel J. Veit, Wolfgang Gentzsch, Grid economics and business models, Journal of Grid Computing 6 (3) (2008) 215–217.
[15] James Broberg, Srikumar Venugopal, Rajkumar Buyya, Market-oriented grids and utility computing: the state-of-the-art and future directions, Journal
     of Grid Computing 6 (3) (2008) 255–276.
[16] Ramayya Krishnan, Grid economics: a selective discussion of two research problems, Journal of Grid Computing 6 (3) (2008) 219–224.
[17] M. Armbrust, A. Fox, R. Griffith, Anthony D. Joseph, R.H. Katz, A. Konwinski, G. Lee, D.A. Patterson, A. Rabkin, I. Stoica, M. Zaharia, Above the clouds: a
     berkeley view of cloud computing, February 10, 2009. http://www.eecs.berkeley.edu/Pubs/TechRpts/2009/EECS-2009-28.html.
[18] Mckinsey report, clearing the air on cloud computing. http://images.cxotoday.com/cxoimages/storyimages/matter101157.pdf.
[19] E. Burke, Categorizing data sensitivity for computer security, No. 222, March 4, 2001. http://datacenter.cit.nih.gov/interface/interface222/security.
     html.
[20] Avanade, 2009 global survey of cloud computing, February 2009. http://www.avanade.com/_uploaded/pdf/thoughtleadership/
     cloudsurveyexecsummary810844.pdf.
[21] Werner Streitberger, Sebastian Hudert, Torsten Eymann, Bjoern Schnizler, Floriano Zini, Michele Catalano, On the simulation of grid market
     coordination approaches, Journal of Grid Computing 6 (3) (2008) 349–366.
[22] G. Stuer, K. Vanmechelena, J. Broeckhovea, A commodity market algorithm for pricing substitutable grid resources, Future Generation Computer
     Systems 23 (5) (2007) 688–701.
[23] K. Lai, L. Rasmusson, E. Adar, L. Zhang, B.A. Huberman, Tycoon: an implementation of a distributed, market-based resource allocation system,
     Multiagent and Grid Systems 1 (3) (2005) 169–182.
[24] R. Buyya, C.S. Yeo, S. Venugopal, Market-oriented cloud computing: vision, hype, and reality for delivering computing as the 5th utility, December
     2008.
[25] R. Buyya, C.S. Yeo, S. Venugopal, J. Broberg, I. Brandic, Cloud computing and emerging IT platforms: vision, hype, and reality for delivering computing
     as the 5th utility, Future Generation Computer Systems 25 (2009) 599–616.
[26] M. Maheswaran, Cloud computing, Seminar Report, Cochin University of Science and Technology, India, November 2008.
[27] A. Edlund, Cloud computing, pay-as-you-go computing explained.
[28] D. Chappell, Chappell and Associates, Cloud platforms today: a perspective, April 18, 2009.
[29] Survey: cloud computing ‘no hype’, but fear of security and control slowing adoption. http://www.circleid.com/posts/20090226_cloud_computing_
     hype_security.
[30] B. Matthews, D. Chapman, Alsbridge cloud computing survey—summary of findings, 21st April 2009.
[31] ROI Case Study, Nucleus Research.com, Document I117, January 2009. http://www.google.com/apps/intl/en/business/case_studies/tvr.pdf.
[32] D. Hinchcliffe, What does cloud computing actually cost? An analysis of the top vendors, ebiz: the Insider’s Guide to Business and IT Agility.
     http://www.ebizq.net/blogs/enterprise/2009/08/what_does_cloud_computing_actu.php.
[33] Financial implications of the cloud, Infosys Microsoft Alliance and Solutions Blog. http://www.infosysblogs.com/microsoft/2008/12/financial_
     implications_of_the_1.html.
[34] D. Rosenberg, The cost of cloud adoption. http://news.cnet.com/8301-13846_3-10140303-62.html.
[35] T. Schadler, Should your email live in the cloud? A comparative cost analysis, January 5, 2009.
[36] R. Dargha, Cloud computing: key considerations for adoption, Infosys Technologies, April 2009. http://www.infosys.com/cloud-computing/white-
     papers/cloud-computing.pdf.
[37] Cloud computing. http://en.wikipedia.org/wiki/Cloud_computing.
[38] W. Vogels, Beyond server consolidation, ACM Queue 6 (1) (2008) 20–26.
[39] P.R. Krugman, Maurice Obstfeld, International Economics: Theory and Policy, sixth ed., Economies of Scale, Imperfect Competition & International
     Trade, 2003 (Chapter 6).
[40] D. Abramson, R. Buyya, J. Giddy, A Computional economy for grid computing and its implementation in the Nimrod-G resource broker, Future
     Generation Computer Systems 18 (8) (2002) 1061–1074.
[41] R. Buyya, D. Abramson, S. Venugopal, The grid economy, Proceedings of the IEEE 93 (3) (2005) 698–714.
[42] Rich     Miller,     Who      has     the     most     web     servers?    May    2009.    http://www.datacenterknowledge.com/archives/2009/05/14/
     whos-got-the-most-web-servers/.
[43] S. Chari, Confronting the data center crisis: a cost–benefit analysis of the IBM computing on demand (CoD) cloud offering, March 2009.
[44] The high volume web sites team, ‘‘Knowing your workload’’, Best Practices for High-Volume Web Sites, IBM RedBooks, 2002.
[45] J. Broberg, Z. Tari, MetaCDN: harnessing storage clouds for high performance content delivery, in: Proc. Sixth Intl. Conference on Service-Oriented
     Computing, ICSOC 2008, Sydney, Australia, 2008.
[46] S. Mansfield-Devine, Danger in the clouds, Network Security (12) (2008) 9–11.
[47] K.M. Cullagh, Data sensitivity: resolving the conundrum 1. http://www.bileta.ac.uk/Document%20Library/1/Data%20Sensitivity%20-%20resolving%
     20the%20conundrum.pdf.
[48] K. Keahey, I. Foster, T. Freeman, X. Zhang, Virtual workspaces: achieving quality of service and quality of life in the grid, Scientific Programming 13
     (4) (2005) 265–275.
[49] S. Venugopal, R. Buyya, L. Winton, A grid service broker for scheduling E-science applications on global data grids, Concurrency and Computation:
     Practice and Experience 18 (6) (2006) 685–699.
                                     S.C. Misra, A. Mondal / Mathematical and Computer Modelling 53 (2011) 504–521                                    521


[50] I. Brandic, S. Pllana, S. Benker, Specification planning, and execution of QoS-aware grid workflows within the amadeus environment, Concurrency and
     Computation: Practice and Experience 20 (4) (2008) 331–345.
[51] B. Maggs, Global internet continent delivery, in: Proc. 1st IEEE/ACM Intl. Symposium on Cluster Computing and the Grid, CCGrid 2001, Brisbane,
     Australia, May 2001.
[52] K. El Emam, The ROI From Software Quality, Auerbach Publications, 2005.
[53] IBM, Seeding the clouds: key infrastructure elements for cloud computing, February 2009.
[54] K.S. Pawar, U. Menon, J.C.K.H. Riedel, Time to market, Integrated Manufacturing Systems 5 (1) (1994) 14–22.
     http://cloudslam09.com/content/confronting-data-center-crisis-cost-benefit-analysis-ibm-computing-demand-cod-cloud-offering.
[55] J. Koomey, K. Brill, P. Turner, B. Taylor, J. Stanley, A simple model for determining true total cost of ownership for datacenters, Uptime Institute.
     http://www.missioncriticalmagazine.com/MC/Home/Files/PDFs/(TUI3011B)SimpleModelDetermingTrueTCO.pdf.
[56] http://web2.sys-con.com/node/640237.
[57] J. Hoffer, Backing up business—industry trend or event, Health Management Technology. http://www.accessmylibrary.com/coms2/summary_0286-
     10537060_ITMJanuary2001.
[58] Nathesh, Green technology—aberdeen report reveals advantages of green retail initiatives, August 14, 2008. http://green.tmcnet.com/
     topics/green/articles/37018-aberdeen-report-reveals-advantages-green-retail-initiatives.htm and http://www-935.ibm.com/services/uk/cio/pdf/
     oiw03022usen.pdf.
