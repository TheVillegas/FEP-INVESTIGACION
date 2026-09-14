Accepted Manuscript


A comprehensive framework for cloud computing migration using
Meta-synthesis approach

Hamid reza Bazi , Alireza Hasanzadeh , Ali Moeini

PII:                   S0164-1212(17)30045-6
DOI:                   10.1016/j.jss.2017.02.049
Reference:             JSS 9932


To appear in:          The Journal of Systems & Software

Received date:         31 August 2016
Revised date:          29 January 2017
Accepted date:         24 February 2017

Please cite this article as: Hamid reza Bazi , Alireza Hasanzadeh , Ali Moeini , A comprehensive
framework for cloud computing migration using Meta-synthesis approach, The Journal of Systems &
Software (2017), doi: 10.1016/j.jss.2017.02.049




This is a PDF file of an unedited manuscript that has been accepted for publication. As a service
to our customers we are providing this early version of the manuscript. The manuscript will undergo
copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please
note that during the production process errors may be discovered which could affect the content, and
all legal disclaimers that apply to the journal pertain.
                                ACCEPTED MANUSCRIPT


Highlights
        Presenting a comprehensive cloud migration framework.
        Extracting concepts from previous researches and classify them to categories
        Proposing a maturity model to improve migration process




                                                                   T
                                                                 IP
                                                               CR
                                             US
                                           AN
                                     M
                          ED
                  PT
         CE
AC




1|
                                     ACCEPTED MANUSCRIPT


                     A comprehensive framework for cloud computing migration using

                                           Meta-synthesis approach



                        Hamid reza Bazi1, Alireza Hasanzadeh2*, Ali Moeini3


Abstract

Migration to the cloud computing environment is a strategic organizational decision. Using a reliable framework
for migration ensures managers to mitigate risks in the cloud computing technology. Therefore, organizations




                                                                              T
always search for cloud migration frameworks with dynamic nature as well as integrity beside their simplicity.
In previous studies, these important features have received less attention and have not been achieved in an




                                                                            IP
integrated and comprehensive way. The aim of this study is to use a meta-synthesis method for the first time for
analysis and synthesis of previous published studies and suggests a comprehensive cloud migration framework.
We review more than 657 papers from relevant journals and conference proceedings. The concepts which are




                                                                          CR
extracted from these papers are classified to related sub-categories and categories. Then, our proposed
framework based on these concepts and categories is developed. It includes seven main phases (categories) and
fifteen sub-categories. To improve the migration process a maturity model called ―ClM3‖ is introduced. Finally,
proposed framework and maturity model is evaluated by forming different focus group meetings and taking

                                                     US
advantages of the cloud experts’ opinion. The results of this research can help managers have a safe and
effective migration to cloud computing environment.
                                                   AN
Keywords: Cloud Computing, Migration Framework, Meta-Synthesis, Process Maturity Model.
                                           M


1. Introduction

    Cloud computing denotes hosted online services (Markovic et al., 2013). According to American National
Institute of Standards and Technology (NIST) definition, ―cloud computing is a model for enabling ubiquitous,
                              ED




convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks,
servers, storage, applications, and services) that can be rapidly provisioned and released with minimal
management effort or service provider interaction‖ (Mell and Grance, 2011). Cloud computing provides new
                    PT




capabilities in line with organizational requirements without the need to invest in infrastructure, new human
resources and licenses (SIclovan, 2012). Cloud computing is a new technology that helps organizations to
develop and create competitive advantage with inherent characteristics such as agility, flexibility, scalability,
           CE




simple and secure accessibility from anywhere, increasing reliability, enhancing fault tolerance and economic
efficiency. NIST and International Organization for Standardization ( ISO/IEC 17788), have described items
such as on-demand self-service, broad network access, resource pooling, rapid elasticity, measured services and
multi-tenancy as the main characteristics of cloud computing (Alsaeed and Saleh, 2015). Service models which
AC




are offered by cloud computing include, software as a system (SaaS), platform as a service (PaaS) and
infrastructure as a service (IaaS) (Mell and Grance, 2011; Rimal et al., 2009; Sharma and Banga, 2013; Tayal,
2011). To deploy cloud computing, organizations can choose one of the deployment models such as private



1
  Department of Information Technology Management ,Tarbiat Modares University , Tehran, Iran. Email:
hr.bazi@modares.ac.ir
2
  ( *Corresponding author), Department of Information Technology Management, Tarbiat Modares University
(TMU),Jalale Alahmad Avenue, P.O. Box 14155-111, Tehran, Iran. Fax: +98-21-82883637. Email:
ar_hassanzadeh@modares.ac.ir.
3
  Department of Information Technology Management, Tehran University, Tehran, Iran. Email:
A.moeini@ut.ac.ir


2|
                                        ACCEPTED MANUSCRIPT


cloud, community cloud, public cloud and hybrid cloud (as shown in Fig.1) (Adrees et al., 2015; Yaghmaei and
Binesh, 2015).
                                                          Hybrid

                                Private / Community                        Public




                              On Premises/Internal                   Off Premises/External
                                         Fig.1. Cloud computing deployment models.




                                                                                         T
   To gain the advantages of cloud computing technology, it is necessary for organizations to migrate their
legacy applications and services to cloud environment (Babar and Chauhan, 2011). Migration to cloud is an




                                                                                       IP
organizational strategic decision. The aim of various research performed in this field, is to enable organizations
to migrate effectively and efficiently from their existing services to cloud solutions. Different organizations
should invest in new technologies such as cloud computing to focus on the core business activities and their




                                                                                     CR
improvement. An important point in cloud adoption and migration is the mentality of organizations; they must
focus on the services instead of infrastructure ownership (Rewatkar and Lanjewar, 2010).
   Regarding to the diversity of cloud offerings with various options (such as location, sales model,
reproducibility, etc.) for usage, it is difficult to select the most appropriate configuration for infrastructure, best


                                                         US
service, and provider (García-Galán et al., 2016). So a framework is required to help the decision makers and
perform successful migration. In most studies, Decision Support System (DSS) are designed for migration to the
cloud which mostly focused on selecting a cloud service provider. In fact, they considered the cost as a major
factor but they ignored comprehensive researching to find the key factors involved in the migration. In addition
                                                       AN
to choose a provider, organizations need to increase their knowledge and be aware of capabilities, principles and
rules of the cloud technology, (Alkhalil et al., 2014). As Jamshidi et al. (2013) stated research in cloud
migration, is in the early stages of maturity and further research is required in this area. A systematic literature
search deals with identifying, categorizing and synthesizing the previous published studies and enabling
knowledge sharing in the research community. This research provides a comprehensive framework for
                                               M


migration to the cloud by the meta-synthesis approach and systematic literature search of the published studies.
   The remainder of this paper is structured as follows: Section 2 contains a description of the background. A
general review of related research works and some critics of the previous published studies are given in this
                               ED




section. Section 3 describes research method that is adopted to conduct the current research. In this section, a
systematic literature search, selecting appropriate research articles, synthesize qualitative findings and validation
of research are explained. Section 4 describes our proposal. At first, we present preliminary framework, then we
improve it and propose a comprehensive framework for cloud computing migration and cloud migration
maturity model (ClM3). In Section 5, we describe research limitations and threats to validity. Finally, Section 6
                     PT




concludes this paper.

2. Background and Related Work
          CE




   This section discusses prior research in cloud computing migration. Khan and Al-Yasiri (2016) show that the
lack of knowledge about cloud computing is one of the main obstacles in adoption and migration to the cloud.
Alabadi (2011) investigates one of the main decision makers’ concerns which is how to prioritize and select the
AC




appropriate cloud services to migrate toward cloud environment. He classifies activities of an organization from
the perspective of sensitivity of the mission. Accordingly, Kundra (2011) offers ―value‖ and ―readiness‖ table to
select applications and services for transmission. Based on Turban decision-making process, Alkhalil, eT al.
(2014) considered the design phase and business intelligence components. They present the knowledge-based
decision support system (KBDSS), helping organizations in seamless migration to the cloud. Alkhalil’s models,
not only pay attention to the cost like others but also create a knowledge-based decision-making system.
Andrikopoulos, Strauch, and Leymann (2013), Andrikopoulos, Song, and Leymann (2013) pose decision
support systems too. In a similar way, Khajeh-Hosseini et al. (2011), Greenwood et al. (2010) also pose decision
support tools.
   In a different way, some authors such as Alonso et al. (2013), Menzel and Ranjan (2012), Johnson and Qu
(2012), Pfitzmann and Joukov (2011), Hajjat et al. (2011), Lewis et al. (2005), Jermyn et al. (2014) formulate




3|
                                               ACCEPTED MANUSCRIPT


the cloud migration problem using an objective function including cost, revenue, net present value, rate of
investment, etc. and they finally solve it to find its optimal solution.
   Some of research focused on the selection of best cloud service provider, suitable solution and best cloud
platform. García-Galán et al.(2016) present ―automated analysis of feature models‖ (AAFM) to analyze and
select the infrastructure. Garg et al. (2013) develop a framework based on Service measurement index (SMI).
This framework uses the analytic hierarchy process (AHP) method to help customers to find the most
appropriate cloud provider. Also, Omerovic et al. (2013), Chan and Chieu (2010), Li et al. (2010) have done
more research on cloud service provider selection.
   Phaphoom et al. (2015) and Surendro and Fardani (2012) have considered the factors that affect cloud
computing adoption and migration. Rockmann et al. (2014) define three dimensions of required IT capabilities
including technological, human, organizational capabilities to implement cloud computing technology in an
organization.




                                                                                                  T
   Gholami et al. (2016) have investigated the cloud migration process and proposed an evaluation framework




                                                                                                IP
to classify approaches applicable to cloud migration. Hwang et al. (2016) present cloud migration orchestrator
(CMO) which includes four engines includes discovery, analytics, configuration and migration. This framework
automates and coordinates the cloud migration based on the IBM business process management (BPM)




                                                                                              CR
technology. With systematic literature review of migration to the cloud in 23 papers by Jamshidi et al. (2013),
they propose a migration model including processes of migration planning, migration execution and migration
evaluation. In their proposed model, cross-cutting concerns also cover main processes in an umbrella form.
Andrikopolos et al. (2013) define four types of migration and introduce related adaption activities according to

                                                                  US
each type in different layers (i.e. data layer, business layer and the presentation layer). Guillén et al. (2013) for
developing cloud applications propose a service-oriented framework that allowed application construct from
combination of software components and migrate freely between cloud platforms. Menychtas et al. (2013) based
                                                                AN
on ARTIST4 methodology, present a new approach for modernization and adaptation of legacy application to
cloud environment, with taking into account the technical and economical aspects.
   As Gholami et al. (2016) state lack of a unified process model of the cloud migration is one of the main open
challenges. Appendix A, Table A1 presents more information about reviewed papers. In Table 1, the migration
                                                       M


steps from different published studies are shown.
Table 1
Migration steps from different published studies.
                                      ED




                 Authors                                                              Migration steps

    Khan and Al-Yasiri (2016)               Cloud requirement stage (CRS) - cloud preparation stage (CPS) - cloud migration stage (CMS)

    Yaghmaei and Binesh (2015)              Developing the knowledge base about cloud - evaluating the present stage of IT (university) -
                              PT




                                            experiment the cloud computing solutions - choosing the cloud computing solutions -
                                            implementation and management of the cloud computing solutions.
    Rai et al. (2015)                       Feasibility study- requirements analysis and migration planning-migration execution- testing and
                                            migration validation- monitoring and maintenance.
              CE




    Wielki (2015)                           Preliminary assessment- migration’s plan creation- implementation and maintenance.
    Pardeshi (2014)                         Preparation- analysis- migration to cloud platform- concluding the cloud migration- maintenance
                                            and vendor management.
    Kiadehi (2014)                          Decision making- preparation- establishment- delivery and monitoring.
AC




    Abderrahim and Choukair (2014)          Baseline architecture- target architecture- migration decision- migration strategy- integration
                                            concerns.
    Okai et al. (2014)                      Planning- choosing the right deployment model- choosing the most suitable service delivery
                                            model- vendor selection- negotiating the SLA(service level agreement) - migration
    Jamshidi, et al. (2013)                 Migration planning- migration execution- migration evaluation.
    Chauhan and Babar (2012)                Identification of requirements- identification of potential cloud hosting environments- analyzing
                                            application compatibility with potential cloud environments-identification of potential
                                            architecture solutions- evaluation of cloud platforms- evaluation of potential architecture
                                            solutions-implementation and system refactoring.



4
    Advanced software-based service provisioning and migration of legacy software




4|
                                      ACCEPTED MANUSCRIPT


    With the holistic view, cloud computing migration consists of three stages called pre-migration, migration,
and post-migration. Reviewing organizational failures in the implementation of applications and IT-based
technologies reflects the fact that most life cycle models suffer from lack of a transparent stage of post-
migration, while this stage is the longest phase of life cycle (Jasperson, Carter, & Zmud, 2005). Therefore,
complete review of the migration and post-migration processes are vital in cloud-related models because the
success of its implementation is based on the acceptance, routinization and infusion (i.e., maximum usage of
potential) of the technology (Saga and Zmud, 1993).
    By reviewing the resources in the field of cloud computing, it is clear that a great deal of knowledge has been
created related to the adoption of informational systems and cloud computing technology by many researchers,
such as Davis (1989), Venkatesh et al. (2000;2003;2012), Tornatzky et al. (1990), El-Gazzar et al. (2016), Sabi
et al. (2016), Gangwar et al. (2015), Safari et al. (2015), Prasad et al. (2014), Premkumar (2003). But a few
researchers comprehensively have studied behaviors of post-adoption (migration) and post-migration.




                                                                                T
According to the selected studies in this research, some critics of the previous research are as follows:
   A few usage of theoretical foundation




                                                                              IP
           As Gholami et al. (2016) in their survey research state, in more than 65% identified papers (28 papers
           from 43 papers), theoretical foundation is not applied. In retained papers, model-driven development,




                                                                            CR
           optimization techniques, usable techniques in software development (such as software product line,
           software pattern), etc. are mentioned as theoretical foundation. With reviewing the selected papers, we
           understand unlike the previous studies in the field of cloud computing adoption, a small number of
           published studies supported their research by a theory in the field of migration and implementation of

                                                      US
           cloud. Technical view is rather dominant on research; along with shortage of theoretical framework.
   A few comprehensive qualitative research
        According to the selected studies in this research, the most studies emphasize quantitative approaches
                                                    AN
        while the shortage of comprehensive qualitative research such as qualitative meta-synthesis method
        (focuses on the comprehensive review and synthesis of findings) is tangible. This fact is reported in other
        published studies such as Gholami et al. (2016) who state in a few researches, semi-structured interview
        is applied as a qualitative research method and only fewer than 14% identified papers, defined their
                                            M


        research process.
   Lack of holistic view
        Most of previous studies lack a systematic review and presentation of holistic view. Majority of Proposed
                              ED




        approaches incorporated with heterogeneous technical-centric concept. By rely only on the earlier studies,
        managers don't find the comprehensive framework of cloud computing migration, in which all cases are
        defined.
   Static consideration of migration and implementation processes
                    PT




        Most studies consider the migration as static processes. They have not considered maturing stages of
        cloud computing in implementation and migration.
In the next Sections a new framework is proposed to overcome to the above mentioned problems.
         CE




3. Research method

   The model of the research process that was provided by Oates (2006) is a suitable reference for the present
AC




research method. According to the aforementioned model, firstly, researchers must define the component that
make up the research process including strategy (e.g., survey, design and creation, experiment, case study,
action research, ethnography), data generation methods (e.g., interview, observation, questionnaires, documents)
and data analysis methods (quantitative or qualitative). In the present research, ―Design and Creation‖ is taken
into account as the research strategy. The data generation method is ―documents‖ and records of the previous
resources. In this study, qualitative meta-synthesis is used to analyze data and combine results from a variety of
published studies.
   ―Design and creation‖ strategy consists of five stages which are called awareness, suggestion, development,
evaluation and conclusion(Oates, 2006). In the awareness stage, the problem of cloud computing migration is
described by systematic literature search, also new areas and dimensions are defined. In suggestion and
development stages, meta-synthesis approach is applied to identify concepts, related sub-categories and related
categories and ultimately provide a comprehensive framework. In the evaluation stage, validation of the



5|
                                        ACCEPTED MANUSCRIPT


proposed framework is performed by the opinion of experts (seven experts have been purposefully selected by
using the snowball technique in the form of a focus group). A conclusion also constitutes the final stage. In this
stage the acquired knowledge along with design process explanation is documented.
    In fact, to provide a framework for cloud computing migration, it is needed to determine main components
by reviewing the previous published studies. For this reason, we use the meta-synthesis method that is one of the
qualitative methods and it is consistent with interpretive paradigm assumptions. The meta-synthesis method has
not been used in cloud computing migration studies yet. By providing a systematic approach for researchers,
meta-synthesis method explores new and essential concepts through synthesizing qualitative research. Meta-
synthesis method creates a comprehensive and wide spread view toward the problems in addition to promote the
current knowledge. It also is a method of reinterpreting and reshaping existing qualitative findings (McClean
and Shaw, 2005). A qualitative meta-synthesis is a technique that combines results from a variety of studies with
a common theme. Per se, ―The sample for a meta-synthesis, then, is made up of individual qualitative studies




                                                                                       T
selected on the basis of their relevance to a specific research question posed by the synthesist‖ (Zimmer, 2006).




                                                                                     IP
    In carrying out a qualitative meta-synthesis method, there are three specific objectives: theory building,
theory explication and theory development(Douglas et al., 2008). The objective of this research is to explicate
the theory, which a more holistic view of the phenomenal results from the synthesis of qualitative findings from




                                                                                   CR
previous studies.
    There are various meta-synthesis Methods. Perhaps the first planned synthesis of qualitative findings is done
by Glaser and Strauss(Zimmer, 2006). Noblit and Hare offer a seven-step method based on qualitative
ethnography(Zimmer, 2006). Sandelowski and Barroso (2007) also propose a seven-step method that has more

                                                            US
generality and it is the selected method of this research. These steps include: formulate the review questions,
conduct a systematic literature search, screen and select appropriate research articles, extract the results, analyze
and synthesize qualitative findings, maintain quality control and present findings. According to all
                                                          AN
aforementioned explanations, the process used in this research is summarized in Fig. 2 (these steps will be
explained later in different sub-sections).
    As shown in Fig.2, we have defined a feedback process. As it will be explained later in Section 3.4, we used
experts’ peer review to validate the proposed framework. In addition, to optimize the validity of qualitative
                                                M


research process, we used two independent reviewers who should answer to predefined questions in different
steps of our research process. As a result, the comments received from the focus group members (i.e., the
experts) and two independent reviewers can affect on each step of the research process and modify it. Therefore,
                               ED




if the experts and reviewers recognize that one of the steps of the research process has not been done in a right
way; this step must be done again.

                                      Formulate the review questions
                     PT




                                        Systematic literature search
         CE




                                    Select appropriate research articles


                                            Extract the results
AC




                                Analyze and synthesize qualitative findings


                                  Present findings (proposal framework)

                                                                                   Feedback
                           Validation (expert peer review/ independent reviewer)
                                        Fig.2. The research process.



3.1.Formulate the Review Questions (RQs)

   With the holistic view and systematic search of previous published studies, this research looks to eliminate
the mentioned deficiencies (as explained in previous section), and find categories and concepts related to cloud



6|
                                                           ACCEPTED MANUSCRIPT


computing migration in the previous published studies. The research answers the following questions and
provides the comprehensive and dynamic framework of cloud computing migration using meta-synthesis
method.

              RQ1. What are the existing processes or phases of cloud migration?
              RQ2. How do these processes or phases form migration framework?
              RQ3. Based on our research, what can we conclude about the appropriate cloud migration framework?




                                                                                                                    T
3.2. Systematic Literature search and Selecting Appropriate Research Articles




                                                                                                                  IP
   All articles from relevant journals and conferences from 2000 (the obtained results from our primary search
indicated that the published studies before the year 2000 can be negligible) to the first half of 2016 in different
databases and search engines such as Elsevier, Scopus, Springer, IEEE Xplore and Google Scholar are statistical




                                                                                                                CR
population of this study. Keywords of cloud computing, migration, migrate, acceptance, usage, and
implementation are applied for searching. The Criteria considering articles as part of the research are shown in
Table 2.

Table 2
Criteria for considering as part of the research.
Criteria
 No.
  C1
                          Parameters
                       Paper’s language
                                                                                  US
                                                                                  inclusion criteria
                                                                          Studies written in English
                                                                                                                                      exclusion criteria
                                                                                                                            Studies not written in English
                                                                                AN
                                                                    Papers published from 2000 to the first
  C2                     Time of presenting papers                                                                         Studies published prior to 2000
                                                                                 half of 2016
                                                                        Migration to cloud computing
  C3                         Research subject                                                                          Cases different from the mentioned subject
                                                                                 environment
                                                                      Papers published in peer reviewed
                                                                                                                       Book reviews, non-peer reviewed journals,
                                                                    M


  C4                          Type of study                           journal and international relevant
                                                                                                                                 personal comments
                                                                                 conferences
                                                                    Papers with clear research process and             Papers with unclear research process and
  C5               Status of research information
                                                                              research findings                                   research findings
                                                   ED




   In early search, based on keywords we found 657 related articles. After investigating the title it is determined
that most of them are related to other research fields of cloud computing and 145 articles are selected for
reviewing abstract. After studying the abstracts, 63 articles are chosen for full content review. After a full
                                    PT




review of content, 11 articles are rejected and finally 52 articles are obtained for analysis of content (see
Appendix A, Table A1). The number of selected papers with separate years of publishing, relevant databases
and search engines and also the process of searching and selecting appropriate articles are shown in Fig. 3, Fig.4
and Fig. 5 respectively.
               CE




                 The number of selected papers by year of publication                          The number of selected papers by search databases and
 12                                                                                                                search engine
                                                    11     11
                                                                                         25                                                 23
AC




 10
                              9
                                                                    8                    20
  8
                                                                                                                14
                                                                                         15
  6

                   4                   4                                    4
                                                                                         10        7                                                       7
  4
                                                                                          5
  2
                                                                                                                               1
           1
                                                                                          0
  0                                                                                             Elsevier      Scopus       Springer     IEEE Xplore- Google Scholar
       2005       2010       2011    2012          2013   2014     2015    2016                                                            Scopus
                                            year                                                                                         (common)

Fig.3. The number of selected papers by year of publishing.                         Fig.4. The number of selected papers by search databases and engines.




7|
                                                   ACCEPTED MANUSCRIPT


  The number of papers founded based on key words N =657
                                                                               The number of rejected papers based on ―Title‖
                                                                               N =512; considering exclusion criteria (C1, C2, C3)
  The number of abstracts review N =145
                                                                               The number of rejected papers based on ―Abstract‖ N =82;
                                                                               considering exclusion criteria (C1, C2, C3, C4)
  The number of full contents review N =63
                                                                               The number of rejected papers based on ―Content‖,
                                                                               ―Bibliography information‖, and ―Quality‖ N =11
  The number of papers obtained for analysis of content N =52                  ; considering exclusion criteria (C1, C2, C3, C4, C5)


                                          Fig. 5. The process of searching and selecting appropriate articles.




                                                                                                       T
                                                                                                     IP
3.3. Extract The Results, Analyze and Synthesize Qualitative Findings




                                                                                                   CR
   For extracting the concepts from the text of the research questions, two following questions have been
simultaneously taken into account.

            RQ1. What are the existing processes or phases of cloud migration?
      

                                                                       US
             RQ2. How do these processes or phases form migration framework?

   In many papers in the literature review, the concepts have been directly mentioned. We extract these
concepts from the literature review and write them with their references in Appendix B, Table B1. Then, we
                                                                     AN
gather the similar concepts together based on the meaning of each concept and after that we extract the related
sub-categories. This procedure is repeated in creating categories which have been derived from similar sub-
categories. Concepts, sub-categories and categories are validated by the experts’ review. Finally, the main
phases of the initial framework are determined based on created categories. By comprehensively studying the
                                                           M


resources, 91concepts are extracted and accordingly, 13 sub-categories and 6 main categories are grouped (see
Appendix B, Table B1).
   As an example of extracted concepts, sub-categories and categories; we show a category titled ―Initiation
                                          ED




phase‖, its sub-categories and related concepts in table 3. This category is composed of twelve various extracted
concepts and two related sub-categories. Concepts are taken out from various papers and considering to their
similarity in meaning we classify them in two sub-categories.
Table 3
                               PT




Example of concepts and sub-categories as well as their extraction resources related to initiation phase.
                                                                                                                         Sub-
 No                            Concepts                                             References                                                          Category
                                                                                                                      categories
                                                                (Khan and Al-Yasiri, 2016), (Yaghmaei and
             CE




                                                                                                                        Expanding the knowledge about




 1        Developing and expanding the knowledge                Binesh, 2015), (Pardeshi, 2014), (Alkhalil et al.,
                                                                                                                         and their basic requirements




          about cloud computing.                                2014)
                                                                (Kiadehi, 2014), (Rewatkar and Lanjewar, 2010),
                                                                                                                               cloud computing




 2        Changing the mentality.
                                                                (Kundra, 2011)
          Understanding the legal requirement and
 3                                                              (Alsufyani et al., 2015)
AC




          implication related to the cloud.
          Should become fully aware of the cloud
 4                                                              (Alkhalil et al., 2014)
          computing principles.
                                                                                                                                                           Initiation phase




 5        Reviewing the standards related to the cloud.         (Khan and Al-Yasiri, 2016), (Kiadehi, 2014)
          Become fully aware of the cloud contract
 6        terms.                                                (Khan and Al-Yasiri, 2016)

          Identifying the services and business                 (Yaghmaei and Binesh, 2015), (Rockmann et al.,
 7
          processes.                                            2014)
                                                                                                                        opportunities and




 8        Identifying the cloud environment.                    (Alkhalil et al., 2014)
                                                                                                                        Identification of




 9        Identifying opportunities.                            (Alkhalil et al., 2014)
                                                                                                                            threats




                                                                (Khan and Al-Yasiri, 2016), (Alkhalil et al.,
 10       Identifying limitations (constraints).
                                                                2014), (Alsufyani et al., 2015)
                                                                (Khan and Al-Yasiri, 2016), (Omerovic et al.,
 11       Identifying risks.                                    2013), (Alkhalil et al., 2014), (Kiadehi, 2014),
                                                                (Khajeh-Hosseini et al., 2010b)
 12       Developing knowledge base.                            (Andrikopoulos et al., 2013b), (Alkhalil et al.,



8|
                                      ACCEPTED MANUSCRIPT


                                                2014)



3.4.Validation of Research

    The consensus of most researchers is that the output of meta-synthesis method can be validated by one of the
following methods:
     • Experts peer review in the approval of research outputs (Sandelowski and Barroso, 2007)
     • Providing a comprehensive result of using new case studies (Thorne, 2009)

    In this research, Experts’ peer reviews in the acknowledgement of research achievements are used to validate
the proposed framework. Therefore, seven experts (independent people of the research team who do related
research or have an activity in the industry and related fields) associated with cloud computing in Iran, are




                                                                                T
selected by purposive and snowball technique, then we have arranged some focus group meetings. Finally the




                                                                              IP
proposed framework is finalized and confirmed.
    The experts of this research have evaluated and validated our proposed cloud computing migration
framework. It is very important to state that the selected experts in focus group must be knowledgeable in the




                                                                            CR
field of cloud computing technology. Accordingly, we categorized the experts’ experiences in two main groups.
The members of first group have academic activities related to cloud computing technology and have published
relevant research papers. The second group, work in cloud computing industry as cloud service providers. The
first group’s members focus on the proposed framework from academic point of view while the second group

                                                      US
mainly considers the technical aspects. These groups have a close collaboration in our focus group.
    A key mechanism for optimizing the validity of study is audit trail - consist of documents tracking search-
(Sandelowski & Barroso, 2007). We maintain of an audit trail. The research documents are delivered to
                                                    AN
reviewers and focus group members. It is worthy to note the focus group consists of research team and seven
experts.
    For optimizing the validity of qualitative research synthesis studies, according to Sandelowski and Barroso
(2007) procedures; research team meet together weekly (for 5 months and 2 meeting with 8 hours per week) to
                                            M


discuss and formulate outcomes and refine study appraisal strategies. All procedures are documented (audit
trail) and delivered to two independent reviewers (different from the focus group), who have great rich
experiences in qualitative research, to appraise each report and evaluate research process. In different situation,
                              ED




they should answer to predefined questions:
      - Are meta-synthesis research processes done in a right way (by research team)?
      - Paper selected for research, are related and suitable? If papers selection process is done in a right
          manner or not?
                    PT




      - Whether the selected papers cover the research topic or not?
      - Are the independent reviewers’ opinions about rejected papers close to research team’s opinion?
          (independent reviewers randomly appraise some rejected papers and response to this question)
         CE




      - If the independent reviewers’ opinion about extracted concepts, sub categories and categories are close
          to research team’s opinion or not? (independent reviewers randomly appraise some papers and extract
          concepts then compare their result to research team result)
AC




4. Results (Proposed framework) and Discussion

   In this section, we first propose a primary framework. This primary framework is constructed directly based
on the extracted concepts, sub-categories and categories (i.e., the result of qualitative Meta-synthesize research
methodology as shown in Appendix B, Table B1). It should be noted that to avoid probable misguiding, it seems
better that the readers should first consider this primary framework. Then, we improve the primary framework
based on complementary findings and add new phases (categories) to it as well as proposing the final migration
framework. Finally, we clarify our proposed cloud migration maturity model for improving migration processes.

4.1. Preliminary framework




9|
                                                ACCEPTED MANUSCRIPT


   According to the concepts, sub-categories and categories of Table3 which are the results of qualitative
analysis and synthesis of research source's findings, the following preliminary framework (Fig. 6) is
recommended for stepwise migration to cloud computing environment. The mentioned framework consists of
six main phases (categories) including initiation, adoption, decision-making and selection, migration,
adaptation and control, routinization and maintenance stages and thirteen sub-phases.

Initiation phase:
       In the initial phase as Cooper and Zmud (1990) explained, organizational need or technological
   innovation or both of them increase the pressure for change. Organizations deal with proactive investigation
   of problems, opportunities and adoption of cloud solutions related to them. One of the main obstacles in the
   way of organizations’ migration to cloud computing environment is the lack of awareness of top managers
   and decision-makers from cloud computing. For a successful start, organizations must effectively extend




                                                                                                  T
   their cloud knowledge (Khan and Al-Yasiri, 2016; Yaghmaei and Binesh, 2015; Pardeshi, 2014; Alkhalil, et




                                                                                                IP
   al., 2014). In addition, it is necessary for organizations to modify their mentality from infrastructure
   ownership toward the providing services. Organizations should understand legal considerations, verify
   standards and develop knowledge database (Alkhalil et al., 2014; Alsufyani et al., 2015; Kiadehi, 2014).




                                                                                              CR
   They should identify the cloud environment, opportunities, risks and threats (Alkhalil et al., 2014; Khajeh-
   Hosseini et al., 2010a; Omerovic et al., 2013; Rockmann et al., 2014). The more accuracy in the process of
   acquiring knowledge leads to more effective analysis process at later phases.

                    Feedback
                                                                   US                           Adaptation and      Routinization and
                                                                 AN
                                                                                                   control            Maintenace
                                                       Decision             Migration
                                                      making and                                                    • Support and
                                  Adoption                                                    • Migration process     maintenance
                                                       selection
       Initiation                                                      • Develop the            control and         • Continual
                                                • Goal setting           migration strategy     evaluation            monitoring
                                                        M


                          • Identification of   • Analyze the detail   • Pilot test and       • Adaptation
 • Expanding the            detail requirements requirements and         migration
   cloud knowledge          and solutions         solutions
 • Identification of      • Preliminary         • Choosing the
                                       ED




   opportunities and        strategic analysis    solutions                                                          Effective& Efficient
   threats
                                                                                                                      Cloud Migration
                          PT




                               Fig. 6. Preliminary stepwise migration framework to cloud computing environment.

Adoption phase:
           CE




      In the adoption phase, according to the opinion of Cooper and Zmud (1990) and Kwon and Zmud (1987)
  a logical and political bargaining in the organization leads to organizational support to implement IT
  applications. At this phase, the organization incline to cloud computing migration, and the decision is made
  to invest in the required resources. For reasonable bargaining in the organizations, separate needs and
AC




  requirements should be firstly identified fully-detailed. In addition to fully understanding of applications
  (Menychtas et al., 2013), the requirements of stakeholders, compatibility, security (Subramanian and
  Seshasaayee, 2014), the potential cloud hosting environments and the proposed solutions are needed to be
  accurately and completely identified (Chauhan and Babar, 2012). After the identification step, preliminary
  strategic analysis is required to be conducted. In this step the value of cloud computing is analyzed (Kundra,
  2011). After enterprise readiness identification (Khan and Al-Yasiri, 2016; Kiadehi, 2014), organizational
  strengths and weaknesses, opportunities and threats, in the previous step, the market landscape(Kiadehi,
  2014), business strategy (Alkhalil et al., 2014), technology vision, IT governance status (Khan and Al-Yasiri,
  2016) and specification of governmental service should be evaluated.
Decision-making and selection phase:




10 |
                                      ACCEPTED MANUSCRIPT


      At this phase, after the preliminary strategic analysis and evaluating the positivity of organization’s
  opinion toward cloud computing migration, migration goals must be set. Then, deployment model, service
  model, bench points, and architecture of target should be determined (Menychtas et al., 2013; Omerovic et
  al., 2013; Pardeshi, 2014). It is notable that being align with the organizational goals and strategies should
  always be considered in setting the goals by IT managers. After goal setting, stakeholder requirements,
  required IT capabilities (technical, human and organizational) and outsourcing capabilities (ITO) should be
  analyzed (Rockmann et al., 2014). Technical and economical feasibility analysis is should be done (Alonso
  et al., 2013; Jamshidi et al., 2013; Johnson and Qu, 2012; Khan and Al-Yasiri, 2016; Pfitzmann and Joukov,
  2011), also suitability of cloud-based services should be evaluated with the potential cloud environment
  (Alkhalil et al., 2014; Chauhan and Babar, 2012; Garg et al., 2013). By developing the knowledge-based
  decision support system from the analysis, which is done in the previous step, organizations can rank
  services and service providers based on various criteria, including the user's previous experience and




                                                                                T
  performance of the service. Organizations can choose a suitable provider for migration by selecting the




                                                                              IP
  appropriate platform (Garg et al., 2013; Menzel and Ranjan, 2012).
Migration phase:
      The most important action on the migration phase is developing the migration strategy. Then, to apply the




                                                                            CR
  developed strategy, it is better to choose a pilot project and proceed to migrate after the initial test. In this
  phase, it is needed to make policy and plan for cloud migration, and doing the categorization and assignment
  of responsibilities according to that.
  Services, applications and data should be classified along with ones which should migrate must be selected

                                                      US
  according to various criteria (such as: high updating, high maintenance costs, low utilization rates, high cost
  per user and innovation of delivered service). Then, decision makers should classify selected application and
  services based on sensitivity of the mission (Alabbadi, 2011). We suggest applying traditional system for
                                                    AN
  highly sensitive application with critical missions (not to be migrated). If organizations want to use cloud
  solutions for mentioned services and application, it is better for them to use private cloud deployment model.
  Public cloud is Suitable for low sensitive applications and services.
    For effective migration, interoperability strategy (Abderrahim & Choukair, 2014), multi-tenancy and
                                            M


  elasticity strategy (Andrikopoulos et al., 2013c), outsourcing strategy (Pardeshi, 2014), exit strategy and
  transmission schedule (Kiadehi, 2014) should be developed along with determination of immigrant services.
  After migration strategy development, modernization and adaptation of the legacy applications are done
                              ED




  (Menychtas et al., 2013) and effective contract (Khan and Al-Yasiri, 2016) is presented. To perform
  migration process, it is better to select a pilot project at first, and employ systems’ testing, retrieval and
  adaptation of the architecture (Jamshidi et al., 2013) and performing extraction and migration of data,
  services and applications as a seamless and integrated migration (Alkhalil et al., 2014).
                    PT




Adaptation and Control phase:
     The purposes of this phase are control, monitor and evaluate important issues during migration, and then
         CE




  adapting the various factors to reach the desired results. By controlling the application for its security,
  availability and performance throughout the migration process, this phase looks to ensure continuity of the
  application and integration of the new system with the older system(Abderrahim and Choukair, 2014;
  Jamshidi et al., 2013; Menychtas et al., 2013). In order to realization of technical and economical goals
AC




  which are set in the adoption phase, it should be evaluated and verified during and after the migration. For
  improvement, adaptation activities should also be done during and after the migration, such as the
  acquisition of new skills depending on the needs (Kundra, 2011), review of the existing IT governance
  model and creation of a governance model related to organizational strategies; also all relevant policies are
  reviewed for ensuring effective support (Kiadehi, 2014). As Cooper and Zmud (1990) also express, in
  adaptation phase, organizational procedures are reviewed and developed, besides organization’s members
  are trained toward new procedures and IT applications(Cooper and Zmud, 1990).

Routinization and Maintenance phase:
      At this phase, in addition to the creation of guidelines, activities related to support, update and vendor
  management are conducted. The routine budget is considered for migration. Cooper and Zmud (1990) and
  Kwon and Zmud (1987) define routinization phase in such a way that usage of systems and IT application



11 |
                                      ACCEPTED MANUSCRIPT


   are part of individual’s routine behavior, normal activities and governance systems of organizations have
   been adjusted to respond to IT application. At this phase, in order to respond to organization’s governance
   systems, evaluation of service delivery and vendor’ models (Kundra, 2011) are periodically and continuously
   done as well as routine monitoring of quality of service (QoS) (Kundra, 2011; Pardeshi, 2014) and the way
   of meeting service level agreement (SLA) (Garg et al., 2014).


4.2. Improving the preliminary framework and propose comprehensive cloud migration framework

    Apart from knowing how the innovative technology are acquired by the organization (created internally or
purchased commercially), they should be incorporated since their benefits are fully flourished (Hazen et al.,
2012). In fact, there is a gap between the adoption of innovative technology and its incorporation in the
organization so that it must be filled with acceptance, routinization and infusion (or, alternatively, assimilation)




                                                                                T
stages (Hazen et al., 2012).




                                                                              IP
     In order to better understanding of adoption, acceptance, routinization and infusion (or, alternatively,
assimilation ) stages, it is better to refer to the six-step model of IT implementation presented by Cooper and
Zmud (1990) and Kwon and Zmud (1987). They have introduced a six-stage model of IT implementation




                                                                            CR
includes Initiation (organizational needs and innovation will lead to increase in pressure to change), Adoption (a
logical and political bargaining in the organization will lead to decide for investing in IT application adoption),
Adaption (IT application is developed, installed and maintained; also organizational procedures are reviewed
and developed), Acceptance (reflects users’ commitment for the use of new system), routinization (using system

                                                      US
and IT application are parts of individual’s routine behavior and normal activity), infusion (it mentions
incorporation and the maximum usage of application’s potential in a deep, broad and comprehensive way in the
organizational or individual work system).
                                                    AN
    So, to effectively use of cloud computing migration framework, it is better to entirely consider IT
implementation model. The primary framework covers the first five stages of IT implementation model include
initiation, adoption, adaptation, acceptance and routinization but there are not any phases about infusion stage
(as shown in Fig. 6). Indeed, infusion stage means the incorporation and the maximum usage of technology’s
                                             M


potential in a deep, broad and comprehensive way in the organizational or individual work system. Accordingly,
to improve the preliminary framework, it is necessary to add a new phase (including infusion stage). Thus, it is
suggested to add ―optimizing and Infusion‖ phase to the previous framework (as shown in Fig.7) and define a
                               ED




new model for the maturity of cloud computing migration processes.
    The optimization and infusion phase points to the dynamics of migration process and its perfection trend. In
the optimization and infusion phase, the migration processes are optimized in line with organizational strategic
objectives. As Cooper and Zmud (1990) stated, the infusion phase points out deep, widespread and
                    PT




comprehensive implementation and incorporation of any technology such cloud computing technology in the
organization. Also, technology is used to its utmost potential in the organization. Then, with applying this new
added phase, organizations ensure that the usage of cloud computing technology reaches to the maximum
         CE




possible value in terms of related volume and diversity of organizational processes, and depth of usage.
AC




12 |
                                             ACCEPTED MANUSCRIPT


                                                       Feedback



                                                                                                                      Optimizing
                                                                                Adaptation and   Routinization        and infusion
                                                                  Migration        control       &Maintenance
                                           Decision
                                          making and
                                           selection                                                                 • Optimizing
                          Adoption                           • Develop the       • Migration
                                                                                   process       • Support and       • Infusion
       Initiation                                              migration
                                          • Goal setting                                           maintenance
                                                               strategy            control and
                                          • Analyze the                                          • Continual
                       • Identification                      • Pilot test and      evaluation
                                            detail                                                 monitoring
  • Expanding the        of detail                             migration         • Adaptation
                                            requirements




                                                                                              T
    cloud                requirements       and solutions
    knowledge            and solutions    • Choosing the
  • Identification




                                                                                            IP
                       • Preliminary        solutions
    of opportunities     strategic
    and threats          analysis                                                                                Effective and efficient
                                                                                                                    cloud migration




                                                                                          CR
4.3.Cloud Migration Maturity Model (ClM3)
                                                               US
                                           Fig. 7. Comprehensive cloud migration framework.
                                                             AN
    If the proposed framework is considered with process approach, its phases consist of migration processes and
sub-processes which the migration maturity model can be defined for improve them. Using maturity model
guide the organization to a level of perfection in the migration process by going through different levels of it. To
define the cloud migration maturity model, we review different maturity model such as CMMI, OPM3, BPMM,
                                                     M


etc. Finally, inspired by representation approaches (staged representation and continuous representation)
introduced in CMMI for Services ver. 1.3 (Team, 2011); we construct our proposed ―Cloud Migration Maturity
Model‖ (ClM3). In this maturity model, organizational processes scope only contains cloud migration processes
                                          ED




(as shown in proposed migration framework (Fig. 7)). Our main reason for selecting CMMI is its application in
organizations from various industries (Zubrow, 2003).
    Cloud migration maturity model (ClM3) helps organizations find out the right chose for migration to cloud
computing environment by building capability in their cloud migration processes. To validate this maturity
                         PT




model, we used new focus group meetings with previous members who review, evaluate and finalize it for us.
ClM3 contains the following model components:
  • Migration process areas: ClM3 is a collection of defined seven migration process areas and fifteen related
            CE




       processes that presented in proposed framework (Table 4). According to ClM3, a migration process area is
       satisfied when it covers all of the generic and specific goals and practices for that process area.
  • Generic goals and generic practices: they are general categories of goals that may fulfill certain needs. They
AC




       are part of every migration process area (Appendix C, Table C1).
  • Specific goals and specific practices: they are specific to a migration process area (Appendix D, Table D1).

   The ClM3 is structured as two representation approaches in which just one of them must be selected. Note
that, both ClM3 representations contain above mentioned model components.
     -    Continuous representation (capability levels): this approach allows an organization to choose one or
          more specific cloud migration process areas and improve relative to these. It uses capability levels
          (level 0 to level 3) to distinguish improvement relative to an individual process area. Attribute of each
          capability level, required generic goals and generic practices is shown in Table5.
     -    Staged representation (maturity levels): it is an approach that uses sets of migration process areas to
          define an improvement path for an organizational cloud migration. This improvement path is described




13 |
                                               ACCEPTED MANUSCRIPT


          by five maturity level. Description of each maturity level in ClM3 staged representation is shown in
          Table 6.
   In fact, if organizations want to use ClM3, they should select one of the two representation approaches in
the first step. A representation approach allows an organization to follow different improvement objectives.
Note that in continuous representation approach, organizations can select one or more migration process and
improve their capabilities by covering all generic goals and their related specific goals (see Table5). But, Staged
representation approach uses sets of migration process areas to define an improvement path for an
organizational cloud migration. This improvement path is described by five maturity level with their required
generic and specific goals that should be covered (see Table 6 and Table 5).

Table 4
Migration processes in ClM3.




                                                                                                    T
  No      Abb.                                 Core processes                                           Process area
 1      ECK          Expanding the cloud knowledge                                       Initiation




                                                                                                  IP
 2      IOT          Identification of opportunities and threats                         Initiation
 3      IDR          Identification of detail requirements and solutions                 Adoption
 4      PSA          Preliminary strategic analysis                                      Adoption




                                                                                                CR
 5      GSE          Goal setting                                                        Decision making and selection
 6      ADR          Analyze the detail requirements and solutions                       Decision making and selection
 7      CSO          Choosing the solutions                                              Decision making and selection
 8      DMS          Develop the migration strategy                                      Migration
 9      PTM          Pilot test and migration                                            Migration



                                                                    US
 10     MPC          Migration process control and evaluation                            Adaptation and control
 11     ADA          Adaptation                                                          Adaptation and control
 12     SAM          Support and maintenance                                             Routinization and maintenance
 13     CMO          Continual monitoring                                                Routinization and maintenance
 14     OPT          Optimizing                                                          Optimizing and infusion
                                                                  AN
 15     INF          Infusion                                                            Optimizing and infusion
                                                        M


Table 5
Capability levels within CLM3 contiguous representation.
  Capability             Attributes                    Status                 Generic goals                  Generic practices
                                       ED



    levels
CL0               - Ad hoc process          - Failure to reach CL1         Process is either not performed or only partially performed
(Incomplete)                                                               in that one or more of the specific goals for a process area at
                                                                           level 1 are not satisfied.
CL1              - A process that              - All specific goals of     GG1: Achieve            GP 1.1: Perform Specific Practices.
(Performed)                                                                Specific Goals
                         PT




                   accomplishes the work        the process area are
                   necessary to satisfy the     satisfied
                   specific goals.
CL2              - A performed process         - All specific goals of     GG2:                  GP 2.1: Establish an organizational
(Managed)          that is planned and           the process area are      Institutionalize a    policy
            CE




                   executed in accordance        satisfied                 Managed Process       GP 2.2: Plan the process
                   with policy                                                                   GP 2.3: Provide resources
                                               - Institutionalize a
                                                                                                 GP 2.4: Assign responsibility
                 - Employs skilled people        Managed Process
                                                                                                 GP 2.5: Train people
                 - Is monitored                                                                  GP 2.6: Manage configurations
AC




                 - Involves Stakeholders                                                         GP 2.7: Identify and involve relevant
                                                                                                 stakeholders
                                                                                                 GP 2.8: Monitor and control the
                                                                                                 process
                                                                                                 GP 2.9: Objectively evaluate
                                                                                                 adherence
                                                                                                 GP 2.10:Review status with higher
                                                                                                 level management
CL3              - A managed process           - All specific goals of     GG3:                  GP 3.1: Establish a defined process
(Defined)          that is tailored from the     the process area are      Institutionalize a    GP 3.2: Collect improvement
                   organization’s set of         satisfied                 defined process       information
                   standard processes.         - Institutionalize a
                 - has a maintained              managed process
                   process description         - Institutionalize a
                 - contributes process           defined process
                   related experiences to




14 |
                                              ACCEPTED MANUSCRIPT


 Capability             Attributes                     Status                 Generic goals                   Generic practices
   levels
                  organizational
                  Process assets.
Note that in continuous representation, organization can select one or more migration process and improve their
capabilities by covering all generic goals and their related specific goals.

Table 6
Description of each maturity level in CLM3 staged representation.
  Maturity                               Description                                            Core processes                Processes
     levels                                                                                                                   capability
                                                                                                                                  level
       ML1    • Migration processes are unpredictable, poorly controlled and                           -                        -
                reactive.
              • The migration process performance may not be stable and may




                                                                                                  T
                not meet specific objectives such as quality, cost, and schedule,
                but useful work can be done.
              • Migration processes are planned, documented, performed,




                                                                                                IP
       ML2                                                                              All migration processes               CL2
                  monitored, and controlled at the project level (often reactive).      (initiation phase to adaptation     (managed
              • The managed migration process comes closer to achieving the             phase) are managed process.        processes) *
                  specific objectives such as quality, cost, and schedule.




                                                                                              CR
       ML3    Migration processes, standards, procedures, tools, etc. are defined      All processes (initiation phase       CL3
              at the organizational level. Project or local tailoring is allowed,       to adaptation phase) are            (defined
              however it must be based on the organization’s set of standard            defined processes.                 processes)*
              processes and defined per the organization’s tailoring guidelines.
       ML4    Migration process is measured and controlled


                                                                  US             
                                                                                       All processes (initiation phase
                                                                                        to adaptation phase) are
                                                                                        defined processes.
                                                                                        Routinization and maintenance
                                                                                        processes are defined
                                                                                                                               CL3
                                                                                                                             (defined
                                                                                                                            processes)
                                                                AN
                                                                                        processes.
       ML5    Focus is on continuous quantitative improvement                          All processes (initiation phase        CL3
                                                                                        to Routinization phase) are          (defined
                                                                                        defined process.                    processes)
                                                                                       Optimization and Infusion
                                                                                        processes are defined
                                                      M


                                                                                        processes.
* Managed processes and defined process are defined in Table5.

Comparison between two defined representations in ClM3 is shown in Table7.
                                     ED




Table 7
Comparison of maturity levels and capability levels in CLM3.
     Level        Staged representation (maturity         Continuous representation
                         PT




                            levels titles)                 (capability levels titles)
    Level 0                        -                             Incomplete
    Level 1                     Initial                          Performed
    Level 2                   Managed                             Managed
    Level 3                    Defined                             Defined
             CE




    Level 4           Quantitatively Managed                           -
    Level 5                  Optimizing                                -
AC




5. Research limitations

There are some limitations in this research (threat to validity) which are explained to clarify research process:
    - Publication bias
         A threat to the validity of integration studies like this research is including only published papers
         (Sandelowski & Barroso, 2002) and studies are written in English. This may lead to publication bias
         (Johansson, Fenwick, & Premberg, 2015)
    - Bias in selecting appropriate research articles
         This research focused on studies that reviewed the cloud computing migration. For controlling the
         mentioned bias and reducing missing relevant papers, we extend the research keywords (defined in
         Section 3.2). Furthermore, we search in primary selected papers references to find related papers which
         not necessarily use our defined keywords. Additionally, such as description in section 3.4, we consult



15 |
                                             ACCEPTED MANUSCRIPT


           two independent reviewers to evaluate paper selection process. Finally, based on research
           methodology, 52 research papers selected (as shown in Appendix A, Table A1).
       -   Researcher bias
           Every researcher has some kind of bias. The bias could be simply promoting one theory over other or
           neglecting to interview some kinds of disagreements. To control this bias and reduce threat to validity,
           research team use weekly discussion meeting. In this meeting, researchers freely discussed about
           defined topics. Additionally, we consult two independent reviewers to realize research team activities
           such as research method, paper selection, concepts extraction, result presentation, etc. Furthermore,
           extracted data with their references (as shown in Appendix B, Table B1) delivered to seven experts,
           and in a focus group meeting they are evaluated and finalized.

6. Conclusions and future work




                                                                                          T
   New technologies such as cloud computing play an important role in organizations flexibility and




                                                                                        IP
productivity and allow them to take proper steps in developing and creating competitive advantage by accessing
the capabilities of additional value. In order to take advantages of cloud computing infrastructure and services,




                                                                                      CR
organizations need to migrate to the cloud environment. Migration to the cloud is a strategic organizational
decision with complex and dynamic nature. The benefit of this research is that, for the first time, has used the
qualitative meta-synthesis method to analyze and synthesize the result of previous studies whose main objective
was to recommend a framework or model for cloud migration. This research has founded the concepts, sub-


                                                               US
categories and categories affecting cloud computing migration and provided a comprehensive cloud computing
migration framework containing initial stages of pre-migration, migration and post-migration.
  As RQ1 is concerned, research team uses systematic literature search on cloud migration related papers.
According to research process (as shown in section 3) we search in related database and select 52 relevant
                                                             AN
papers to analyze and identify the cloud migration processes and phases. In regarding RQ2, to realize how these
processes or phases form migration framework, we deeply review the selected papers and extract relevant
concepts. To ensure doing right manner to extract appropriate concepts, we request two independent reviewers
who are expert in qualitative research, comment on these processes. After several discussion meetings among
                                                     M


research team, concepts validated and finalized.
In regarding to RQ3, we synthesize previous research findings and pose a suitable migration framework based
on the finalized extracted concepts, sub categories and categories. For validating defined categories and pose
                                    ED




preliminary framework, we use expert peer review method. Considering the all experts comments and finalizing
the sub categories and categories (as shown in Appendix B, Table B1), preliminary framework is proposed. This
preliminary migration framework has been constructed directly based on synthesizes of reviewed papers
                        PT




findings. If reviewers pursue the defined research process, without difficulty they validate this framework.
Inspired by the IT implementation model introduced in (Cooper & Zmud,1990; Kwon & Zmud,1987) and
according to complementary study done by research team, the preliminary framework improved and final cloud
migration framework (Comprehensive cloud migration framework) presented (as shown in Fig. 7).
           CE




Additionally, we propose maturity model which is named ―ClM3‖ for ensuring dynamism and improving in
cloud migration processes. Our proposed framework and maturity model helps managers to gain a
comprehensive overview of migration and they can perform strategic planning for its effective management. In
AC




connection with the future activities, it is suggested to use mixed method research and case studies to validate
the proposed framework.

Acknowledgements

   We would like to show our gratitude to the software development research group of ICT research institute
and IT-department of the Niroo Research Institute (NRI) for sharing their pearls of wisdom with us during the
course of this research. The authors also wish to thank ―anonymous‖ reviewers for their so-called insights.

Appendix A

Table A1
Purpose and proposed output of selected research papers.
References                                                 Purpose of research and proposed output




16 |
                                              ACCEPTED MANUSCRIPT


References                                                     Purpose of research and proposed output
(Khan and Al-Yasiri,       The proposed stepwise framework consists of cloud requirement, cloud preparation and cloud migration. They
2016)                      focus on preparation of organizations by informing them about risks. Studies show that the lack of expertise's
                           knowledge about cloud computing is one of the main obstacles in the way of adoption and migration to the cloud.
(Hwang et al., 2016)       Presented Cloud Migration Orchestrator (CMO), includes four engines (parts) of discovery, analytics,
                           configuration and migration. This framework automates and coordinates the cloud migration based on the IBM
                           business process management (BPM) technology with pre-migration analytics.
(García-Galán et al.,      The authors present automated analysis of feature models (AAFM) to analyze and select the infrastructure.
2016)                      Considering the infrastructure’s requirements and costs, this model simplifies the configuration process and
                           especially selecting model.
(Gholami, et al., 2016)     They survey the cloud migration process and propose an evaluation framework to classify approaches applicable
                           to cloud migration.
(Kumar et al., 2015)       To reduce business data recovery time in disasters (man-made or natural) and minimize downtime for business
                           process, they improve disaster recovery planning (DRP) based on the prioritization of data by using topsis
                           technique, in order to storage data in IaaS.
(Tashkandi and Al-         They Suggest improvement in network and internet infrastructure for providing services at reasonable and




                                                                                                 T
Jabri, 2015)               affordable costs. These are prerequisites for the acceptance and implementation of cloud computing and the
                           privacy should be ensured.
(Alsufyani et al., 2015)   They propose, before migrating to the cloud several factors like, a deployment model (private or public), security




                                                                                               IP
                           (what type of data should go to the cloud) should be determined as well as customizable capabilities, legal
                           considerations, and implications.
(Yaghmaei and Binesh,      According to their opinion, the implementation and usage stages of cloud computing in higher education




                                                                                             CR
2015)                      institutions are formed with stages of Developing the Knowledge base about Cloud; evaluating the current stage
                           of IT, experiment the cloud computing solutions, choosing the cloud computing solutions besides its
                           implementation and management.
(Alsaffar et al., 2015)    For cloud screen-migration, they provide the internet protocol television (IPTV) service framework, based on
                           secure authentication mechanism and lightweight content encryption method. The proposed framework prevents



                                                                  US
                           cyber-attacks and reduces vulnerability.
(Phaphoom et al.,          The research is based on the logistic regression method on security and technical obstacles which prevent
2015)                      adoption of cloud computing services. Accordingly, data privacy, security and mobility are detected important.
(Rai et al., 2015)         In systematic literature review from 2009 to 2014, factors affecting on cloud migration and migration challenges
                           are identified. Their study focuses on the necessity of creating a secure and comprehensive migration model to
                                                                AN
                           the cloud. The authors offer five-stage model for migration, includes feasibility analysis, requirements analysis
                           and migration planning, migration execution, testing and migration validation, and monitoring and maintenance.
(Wielki, 2015)             He states that that 17.9% of young organizations and 10.2% of mature organizations (more than 5 years
                           operation) don’t have an optimized cloud strategy. So he provides a proposed three-stage model (preliminary
                           assessment, migration’s plan creation, implementation and maintenance) for the strategy of using cloud
                           computing and migration to it.
                                                      M


(Subramanian and           They Suggest that required non-software components for setting up a cloud infrastructure consist of connectivity
Seshasaayee, 2014)         and bandwidth, land for data centers, security. They offer that several important factors should be considered and
                           analyzed when migrating to the cloud.
(Alkhalil et al., 2014)    The model of decision-making process for cloud migration is provided based on Knowledge Base Decision
                                     ED



                           Support System (KBDSS), which comprises Six main steps: business strategy, cloud environment, service
                           suitability, risk assessment, vendor evaluation, and implementation.
(Jermyn et al., 2014)      They focus on the migration from the data center to cloud and propose a method that automatically computes
                           optimized target resources and identifies required configurations. In this method, the relationships between
                           servers are examined in the source environment. Then this method identifies potential resource consolidations
                           and configuration. This information is applied to design a placement strategy for the target cloud architecture.
                           PT




                           This method reduces service's cost down to 60.1%.
(Pardeshi, 2014)           In order to migrate to system based cloud computing, a five-phase strategy, including preparation, analysis, and
                           migration, concluding the cloud migration, maintenance and vendor management is presented.
(Kiadehi, 2014)            He offers a four-stage framework by reviewing the requirements and cloud computing strategies of the federal
            CE




                           government, Department of Defense (DoD), Federal Aviation Administration (FAA) and the Government of
                           Australia. Steps include decision-making, preparation, establishment, delivery and monitoring.
(Rockmann et al.,          To implement cloud computing technology in an organization, three dimensions of required IT capabilities
2014)                      including technological, human, organizational capabilities are defined.
(Abderrahim and            They develop Cloud Computing Adaptive Migration (CCAM) model By using Jamshidi’s Cloud Reference
AC




Choukair, 2014)            migration model (RMM) and Enterprise Architecture Framework (EA). This model comprises five phases:
                           baseline architecture, target architecture, migration decision, migration strategy and integration concerns. It is
                           suggested divide baseline architecture into four domains of business, applications, data and infrastructure. They
                           defin different scenarios of these four parts in order to migrate to the cloud. Reference Model (RM) or Reference
                           Architecture (RA) should be determined before making a decision. Also during and after migration, activities
                           continuity and interoperability of migrated elements with current elements in the organization and other providers
                           should be ensured.
(Botto et al., 2014)       By reviewing papers from 2006 to 2013, 48 papers are selected to review migration of service oriented
                           architecture (SOA) applications to cloud computing environments. Resources categorized in the areas of
                           migration strategies (Conventional or model-driven), migration approach (re-host, re-factor, revise and re-build),
                           migration type (replace a component, partially migrate, migrate the whole software stack and cloudify) and
                           considered qualitative aspects.
(Mateescu et al., 2014)    They present a brief introduction of web-based tool to audit cloud computing migration which is called
                           ―Migration Assessment Tool (MAT)‖. This tool asks questions about the complexity of the implementation
                           (challenges of migration to the cloud), risk and compliance, infrastructure, performance, etc. Then the MTA
                           scores and computes the impact of the cloud adoption and suggests the suitable cloud service providers.
(Okai et al., 2014)        They identify security, privacy and reliability as the main challenges of adopting cloud computing and they set




17 |
                                              ACCEPTED MANUSCRIPT


References                                                     Purpose of research and proposed output
                          some guidelines for their proposed model in order to remove them. Also they provide a roadmap for migration,
                          including planning stages, choosing the right deployment model, selecting the most suitable Service delivery
                          model, vendor selection, negotiating the SLA and migration. The mentioned road map has been tested in the Asia
                          Pacific University of Technology and Innovation [APU].
(Sefraoui et al., 2014)   They explain cloud type, deployment model, rationalization of resources and migration limitation for each type of
                          organization.
(Garg et al., 2013)       They develop a framework (SMI Cloud) based on SMI (service measurement index). This framework helps
                          customers to find the most appropriate cloud provider. The framework includes a service selection based on
                          quality of service (QoS) requirements, service ranking based on the user's previous experience and performance
                          of the service.
(Guillén, et al., 2013)   They proposed a service-oriented framework for developing cloud applications that allowed application construct
                          from combination of software components and migrate freely between cloud platforms.
(Omerovic et al., 2013)   They provide a Decision Support Method (DSM) to select suitable cloud services and provider in multi-cloud
                          environments, it that considers several aspects of cost, risk and quality. The DSM process consists of three main
                          steps: establish context and model the target assess and verification of cost, risk, quality, and treatment and




                                                                                                  T
                          decision-making.
(Menychtas et al.,        Based on ARTIST (advanced software-based service provisioning and migration of legacy software)
2013)                     methodology, a new approach is presented for modernization and migrate legacy application to the cloud




                                                                                                IP
                          environment, with taking into account the technical and economical aspects. ARTIST methodology includes pre-
                          migration (technical and economic feasibility assessment, and application understanding), migration (using
                          reverse engineering and forward engineering techniques), post- migration (verification of pre-defined goals), and




                                                                                              CR
                          evolution and reuse of migration’s artifacts (maintenance and support activities of post-migration).
(Alonso et al., 2013)     By using ARTIST methodology, they present an approach consisting three main steps, the characterization of the
                          legacy application from technical and business points of view, the technical feasibility analysis and economic
                          feasibility analysis in order to decide migration to the cloud.
(Jamshidi et al., 2013)   With a systematic literature review of the migration, from 23 papers selected from the 2010 to 2013, they



                                                                  US
                          eventually offer Cloud-RMM (Cloud - Reference Migration Model). This model includes the processes of
                          migration planning, migration execution, and migration evaluation; that the cross-cutting concerns cover these
                          three processes in an umbrella form.
(Andrikopoulos et al.,    They define four types of migration (replacement, partially migrate, migrate the whole software stack and
2013a)                    cloudify) as well as defining the adoption activities according to each type at different layers (data layer, business
                                                                AN
                          layer and the presentation layer).
(Andrikopoulos et al.,    They review challenges of migrating to cloud such as distribution of applications, multi-tenancy, QoS, cost of
2013c)                    migration &operation, security and confidentiality of data, etc. finally they provide a decision support system.
(Andrikopoulos et al.,    With the aim of selecting an appropriate service provider for migration of existing applications based on least
2013b)                    cost, they define a migration decision support system (MDSS) by analytical hierarchy process (AHP) that
                          consists of three layers (user interface, offerings matcher and cost calculator).
                                                      M


(Chang et al., 2013)      They introduce a cloud computing business framework (CCBF) which consists of four main parts (classification,
                          organizational sustainability modeling (OSM), service portability and linkage. This framework helps
                          organizations in designing, deploying and migrating of cloud computing.
(Srirama et al., 2013)    They propose scientific computational experiments be done directly in the cloud and design a desktop to cloud
                          migration (D2CM) tool to support direct migration of applications to the cloud. This tool supports life-cycle
                                     ED




                          management for applications to be hosted on compatible infrastructure such as Amazon’s EC2 or Eucalyptus.
(Menzel and Ranjan,       They divide the process of an IT system migration to a cloud infrastructure service into five steps and introduce a
2012)                     framework called cloud genius that offers a multi-criteria approach for deciding about the cloud IaaS service
                          provider. The five steps are cloud infrastructure-service selection, selection of cloud VM image, cloud VM image
                          customization, definition of migration strategy, and applying migration strategy.
                          PT




(Johnson and Qu,          In order to decide cloud migration, they offer a holistic model of calculating income and cost of migration.
2012)
(Surendro and Fardani,    With the help of cloud computing reference model, they study the preparation of Indonesian companies related to
             CE




2012)                     the implementation of cloud computing. They said that most of companies tend to use public cloud and SaaS.
                          There is not a problem about human resources, financial and infrastructure issues. The main problems are lack of
                          managers’ adequate training and lack of rules.
(Chauhan and Babar,       They propose a process framework to support migration that includes identification of requirements,
2012)                     identification of potential cloud hosting environments, analyzing application compatibility with potential cloud
AC




                          environments, identification of potential architecture solutions, and evaluation of cloud platforms, evaluation of
                          potential architecture solutions, and implementation and system refactoring.
(Pfitzmann and            In order to migrate to cloud in multi- image environments, they use a method that considers the analysis of return
Joukov, 2011)             on investment (ROI) rate.
(Mircea and               They introduce processes of choosing and migrating to the cloud by using several tables: data identification, data
Andreescu, 2011)          classification, data evaluation and activity evaluation, and etc.
(Misra and Mondal,        They descript four key characteristics of the company's IT resources that should be considered during the
2011)                     migration. These are size, the utilization pattern, sensitivity of the data and criticality of work.
(Hajjat et al., 2011)     They contribute making decision for having a beneficial migration of applications to the cloud by modeling
                          various factors such as: policy constraints, benefits, internet costs and increasing transaction delays.
(Khajeh-Hosseini et       In their study, two tools for cloud migration decisions are offered and besides usage of infrastructure as a service
al., 2011)                (IaaS). The first tool is applied for estimating the cost of using and the latter is a spreadsheet that classifies and
                          evaluates the advantages and risks of using IaaS.
(Alabbadi, 2011)          For cloud formation, he introduces the cloud computing formation (C3F) model that belongs to the Jericho
                          forum. Then he describes its dimensions such as physical location and management, ownership, and the
                          architectural mindset. Next, they mapped IT activities of an educational organization to C3F model based on
                          sensitivity and mission sensitivity matrix.




18 |
                                           ACCEPTED MANUSCRIPT


References                                                  Purpose of research and proposed output
(Kundra, 2011)         He offers the decision framework of the federal government’s cloud computing strategy in order to migrate
                       services and applications to the cloud including: selection, preparation and management stages. He also offers
                       ―value‖ and ―readiness‖ table to select applications and services for transmission.
(Garg et al., 2011)    They describes service measurement index (presented by the consortium of the cloud measurement index) for
                       reviewing the quality of service level by AHP method and selection of appropriate services.
(Babar and Chauhan,    They describe their experiences of migrating an open source application called Hackystat to the cloud which is
2011)                  included the initial architecture of the application, and modified architecture according to the cloud requirements
                       and decision plan.
(Greenwood et al.,     They present, cloud adoption toolkit that addresses the challenges of cloud adoption with risk analysis and cost
2010)                  calculations.
(Li et al., 2010)      Public cloud providers are compared based on defined indexes in their study.
(Chan and Chieu,       They rank and map apps to cloud computing services by choosing the best cloud service provider.
2010)
(Khajeh-Hosseini et    They investigate the advantages and risks of the migration of an Oil and Gas Company data center to Amazon
al., 2010b)            EC2 and they show the cost of the infrastructure system within 5 years would be decreased 37% and support




                                                                                             T
                       activities would be also decreased 21%.
(Lewis et al., 2005)   They study a smart technique that is a service-oriented migration and reuse technique in the field of migration.
                       This technique helps organizations analyze their existing systems, whether their function can appear as a service




                                                                                           IP
                       in a service-oriented architecture.




                                                                                         CR
                                                              US
                                                            AN
                                                   M
                                  ED
                       PT
            CE
AC




19 |
                                                ACCEPTED MANUSCRIPT


Appendix B

Table B1
Concepts, sub-categories and categories as well as their extraction resources




                                                                                                                              category

                                                                                                                                                                                            Category
                                                                                                                                Sub-
No                                Concept                                               References




                                                                                                                        Expanding the knowledge about cloud
1                                                                   (Khan & Al-Yasiri, 2016),(Yaghmaei & Binesh,
     Developing and expanding the knowledge about cloud
                                                                    2015),(Pardeshi, 2014),(Alkhalil, et al., 2014)
     computing




                                                                                                                             computing and their basic
2                                                                   (Kiadehi, 2014),(Rewatkar & Lanjewar,
     Changing the mentality
                                                                    2010),(Kundra, 2011)




                                                                                                                                   requirements
3    Understanding the legal requirement and implication related to
                                                                    (Alsufyani, et al., 2015)
     the cloud.




                                                                                                    T
4
     Become fully aware of the cloud computing principles           (Alkhalil, et al., 2014)




                                                                                                  IP
5
     Reviewing the standards related to the cloud.                  (Khan & Al-Yasiri, 2016),(Kiadehi, 2014)




                                                                                                                                                                                            Initiation phase
6




                                                                                                CR
     Become fully aware of the cloud contract terms                 (Khan & Al-Yasiri, 2016)
7                                                                   (Yaghmaei & Binesh, 2015),(Rockmann, et al.,
     Identifying the services and business processes.
                                                                    2014)




                                                                                                                              Identification of opportunities
8
     Identifying the cloud environment.                             (Alkhalil, et al., 2014)
9
     Identifying opportunities.
                                                                   US
                                                                    (Alkhalil, et al., 2014)




                                                                                                                                        and threats
10                                                                  (Khan & Al-Yasiri, 2016),(Alkhalil, et al.,
     Identifying limitations (constraints).
                                                                    2014),(Alsufyani, et al., 2015)
                                                                 AN
                                                                    (Khan & Al-Yasiri, 2016),(Omerovic, et al.,
11                                                                  2013),(Alkhalil, et al., 2014),(Kiadehi,
     Identifying risks.
                                                                    2014),(Khajeh-Hosseini, Greenwood, &
                                                                    Sommerville, 2010)
12                                                                  (Andrikopoulos, Song, et al., 2013),(Alkhalil, et
     Developing the knowledge base about cloud computing
                                                        M


                                                                    al., 2014)
13
                                                                                                                                      Identification of detail requirements and solutions
                                                                    (Menychtas, et al., 2013),(Khan & Al-Yasiri,
     Understanding the applications.
                                                                    2016),(Rai, Sahoo, & Mehfuz, 2015)
14
                                         ED



     Identifying the IT requirements.                               (Yaghmaei & Binesh, 2015)

15                                                                  (Khan & Al-Yasiri, 2016),(Pardeshi,
     Identifying the stakeholder requirement.                       2014),(Kiadehi, 2014),(Alkhalil, et al.,
                                                                    2014),(Chauhan & Babar, 2012)
16
                           PT




     Identifying security requirements.                             (Subramanian & Seshasaayee, 2014)
17
     Identifying compatibility requirements.                        (Subramanian & Seshasaayee, 2014)
18
             CE




     Identifying the potential cloud hosting environment            (Chauhan & Babar, 2012)
                                                                                                                                                                                            Adoption phase




19
     Identifying potential solutions.                               (Chauhan & Babar, 2012),(Alkhalil, et al., 2014)
20
     Finding the optimized target resource.                         (Jermyn, et al., 2014)
AC




21 Analyzing the cloud computing values (agility, efficiency,
                                                                    (Kiadehi, 2014),(Kundra, 2011)
   innovation, cost saving, availability)
                                                                                                                                      Preliminary Strategic analysis




22
   Evaluating enterprise readiness.                                 (Khan & Al-Yasiri, 2016),(Kiadehi, 2014)
23
     Evaluating governmental service specification                  (Kiadehi, 2014)
24
     Evaluating the market landscape.                               (Kiadehi, 2014)
25
     Analyzing the business strategy.                               (Kiadehi, 2014)
26
     Evaluating the technology vision.                              (Kiadehi, 2014)
27 Risk assessment and ranking these risks (dependent on
                                                                    (Khan & Al-Yasiri, 2016)
   probability, affect, etc.)




20 |
                                                   ACCEPTED MANUSCRIPT




                                                                                                                            category

                                                                                                                                                                                 Category
                                                                                                                              Sub-
No                                 Concept                                                    References


28
     Reviewing the IT governance.                                      (Khan & Al-Yasiri, 2016)
29                                                                     (Yaghmaei & Binesh, 2015),(Rai, Sahoo, &
     Evaluating the current stage of enterprise IT.
                                                                       Mehfuz, 2015)
30
     SWOT analysis                                                     (Pardeshi, 2014)

31 Setting goals and target attribute (deployment, service and
                                                                       (Omerovic, et al., 2013),(Menychtas, et al., 2013)
   ownership models)
32




                                                                                                                                 Goal setting
   Tuning the bench point for legal compatibility and security.        (Pardeshi, 2014)




                                                                                                       T
33
     Specify the architecture of the target.                           (Omerovic, et al., 2013)




                                                                                                     IP
34                                                                     (Khan & Al-Yasiri, 2016)
     Characterizing the objectives aligned with enterprise strategy.




                                                                                                   CR
35
     Analyzing stakeholder requirements.                               (Jamshidi, et al., 2013),(Pardeshi, 2014)
36 Analyzing software and hardware requirements the cloud point
                                                                (Pardeshi, 2014),(Khan & Al-Yasiri, 2016)
   of view.




                                                                                                                                 Analyze the detail requirements and solutions
37




39
   Analyzing transparency, certificates and audits.
38 Analyzing required it capabilities (technical, human,
   organizational).                                                 US
                                                                (Subramanian & Seshasaayee, 2014)

                                                                       (Rockmann, et al., 2014)
                                                                       (Pardeshi, 2014),(Khan & Al-Yasiri,
                                                                  AN
     Managerial and technical feasibility analysis.                    2016),(Jamshidi, et al., 2013),(Alonso, et al.,




                                                                                                                                                                                 Decision making and selection
                                                                       2013),(Menychtas, et al., 2013),(Kiadehi, 2014)
40
     Analyzing IT outsourcing capability.                              (Rockmann, et al., 2014)
41
     Analyzing organizational attributes                               (Rockmann, et al., 2014)
                                                        M


                                                                       (Pardeshi, 2014),(Khan & Al-Yasiri,
42                                                                     2016),(Jamshidi, et al., 2013),(Alonso, et al.,
     Economical feasibility analysis                                   2013),(Menychtas, et al., 2013),(Johnson & Qu,
                                                                       2012),(Pfitzmann & Joukov, 2011),(Khajeh-
                                        ED




                                                                       Hosseini, Greenwood, & Sommerville, 2010)
43
     Analyzing infrastructure flexibility.                             (Rockmann, et al., 2014)
44 Analyzing application compatibility with potential cloud
                                                              (Kiadehi, 2014),(Chauhan & Babar, 2012)
   environment.
                           PT




45
   Developing a cloud knowledge based decision support system (Alkhalil, et al., 2014)
46
     Choosing the suitable implementation platform.                    (Kiadehi, 2014)
             CE




                                                                                                                                 Choosing the solutions




47 Evaluating the suitability of cloud-based services and cloud-       (Alkhalil, et al., 2014),(Garg, et al.,
                                                                       2013),(Chauhan & Babar, 2012),(Yaghmaei &
   based solutions.
                                                                       Binesh, 2015)
48 Ranking the services based on user experiences and service
                                                                       (Garg, et al., 2013)
AC




   performance.
49                                                                     (Garg, et al., 2013),(Menzel & Ranjan,
     Choosing appropriate service and solution.                        2012),(Yaghmaei & Binesh, 2015),(Omerovic, et
                                                                       al., 2013)
50                                                                     (Khan & Al-Yasiri, 2016),(Alkhalil, et al.,
     Choosing an appropriate cloud service provider.                   2014),(Andrikopoulos, Strauch, et al.,
                                                                       2013),(Kiadehi, 2014),(Jamshidi, et al., 2013)
51
                                                                                                                            Develop the Migration




     Policy making and planning for cloud migration.                   (Kiadehi, 2014)
52                                                                     (Khan & Al-Yasiri, 2016),(Menzel & Ranjan,
                                                                                                                                                                                 Migration
                                                                                                                                  strategy




     Categorizing the current services and data.
                                                                       2012),(Jamshidi, et al., 2013)
53                                                                     (Jamshidi, et al., 2013),(Pardeshi, 2014),(Kundra,
     Choosing the immigrant services.
                                                                       2011)
54
     Assigning responsibilities.                                       (Khan & Al-Yasiri, 2016),(Pardeshi, 2014)




21 |
                                                 ACCEPTED MANUSCRIPT




                                                                                                                    category

                                                                                                                                                       Category
                                                                                                                      Sub-
No                                 Concept                                            References


55
     Preparing the interoperability strategy.                     (Abderrahim & Choukair, 2014)
56 Ensuring the convergence between enterprise architecture and
                                                                (Abderrahim & Choukair, 2014)
   cloud computing
57
   Preparing the elastic strategy.                              (Andrikopoulos, Strauch, et al., 2013)




                                                                                                                    Develop the Migration strategy
58
     Preparing the multi tenancy requirements.                    (Andrikopoulos, Strauch, et al., 2013)




                                                                                                                             (Continued)
59 Modernization and adaptation of legacy application in the
                                                                  (Menychtas, et al., 2013)
   cloud environment




                                                                                                  T
60
   Preparing the outsourcing strategy.                            (Pardeshi, 2014)




                                                                                                                                                       Migration (Continued)
                                                                                                IP
61
     Developing a transfer schedule.                              (Kundra, 2011),(Kiadehi, 2014)
62
     Considering the required turn over.                          (Khan & Al-Yasiri, 2016)




                                                                                              CR
63                                                                (Khan & Al-Yasiri, 2016),(Kundra,
     Effective contracting.
                                                                  2011),(Kiadehi, 2014),(Pardeshi, 2014)
64
     Preparing an exit strategy.                                  (Kiadehi, 2014)
65
     Appling the migrating strategy.
                                                                    US
                                                                  (Chauhan & Babar, 2012),(Menzel & Ranjan,
                                                                  2012)




                                                                                                                            Pilot test and migration
66
     Choosing the pilot project.                                  (Pardeshi, 2014)
                                                                  AN
67                                                                (Khan & Al-Yasiri, 2016), (Jamshidi, et al.,
     Test the systems.
                                                                  2013),(Rai, Sahoo, & Mehfuz, 2015)
68                                                                (Jamshidi, et al., 2013),(Pardeshi, 2014),(Rai,
     Extracting and migrating the data.
                                                                  Sahoo, & Mehfuz, 2015)
69
                                                        M


     Seamlessly migrate to cloud computing services.              (Alkhalil, et al., 2014)

70 Monitoring the application for its availability & performance
   throughout the migration process.
                                                                 (Khan & Al-Yasiri, 2016)                           Migration process control and
                                                                 (Abderrahim & Choukair, 2014),(Kiadehi,
                                        ED



71
   Ensuring integration between new systems and older systems. 2014),(Kundra, 2011),(Pardeshi, 2014),(Jermyn,
                                                                                                                             evaluation

                                                                 et al., 2014)
72 Ensuring the service continuity management throughout the
                                                                 (Abderrahim & Choukair, 2014)
                                                                                                                                                       Adaptation and control

   migration process.
73
                           PT




   Monitoring and controlling the migration process.             (Pardeshi, 2014)
74                                                                (Menychtas, et al., 2013),(Garg, et al.,
     Technical and commercial goals verification
                                                                  2013),(Jamshidi, et al., 2013)
75                                                                (Kiadehi, 2014),(Kundra, 2011),(Rockmann, et
            CE




     Creating a new set of it skills depending on the needs.
                                                                  al., 2014)
                                                                                                                            Adaptation




76
     Applying an agile approach to innovation in services.        (Kiadehi, 2014)
77
     IT governance alignment to organizational strategy           (Kiadehi, 2014)
AC




78
     Architecture recovery and adaptation.                        (Jamshidi, et al., 2013)

79 Implementing a security structure in order to defend against
                                                                  (Kiadehi, 2014)
                                                                                                                                                       Routinization and maintenance




   cyber threats.
                                                                                                                            Support and Maintenance




80                                                                (Kiadehi, 2014),(Pardeshi, 2014),(Omerovic, et
   Developing guidelines to guide migration.
                                                                  al., 2013)
81
     Vendor management.                                           (Yaghmaei & Binesh, 2015),(Pardeshi, 2014)
82                                                                (Khan & Al-Yasiri, 2016),(Menychtas, et al.,
     Updating and maintenance.
                                                                  2013),(Rai, Sahoo, & Mehfuz, 2015)
83
     Support.                                                     (Menychtas, et al., 2013)
84 Reviewing all related policies to ensure support for cloud
                                                                  (Kiadehi, 2014)
   computing services.




22 |
                                                ACCEPTED MANUSCRIPT




                                                                                                                     category

                                                                                                                                                      Category
                                                                                                                       Sub-
No                               Concept                                                References


85
      Assigning a routine budget.                                    (Pardeshi, 2014)




                                                                                                                                              Routinization and maintenance
86                                                                   (Kundra, 2011),(Garg, Toosi, Gopalaiyengar, &
      Monitoring the SLA.
                                                                     Buyya, 2014),(Kiadehi, 2014)
87




                                                                                                                       Continual monitoring
      Evaluating user quality of experiences.                        (Pardeshi, 2014)




                                                                                                                                                       (Continued)
88
      Monitoring quality of services.                                (Pardeshi, 2014),(Khan & Al-Yasiri, 2016)

89
      Ensuring the transparency, maintenance and updating.           (Khan & Al-Yasiri, 2016)




                                                                                                  T
90
      Evaluating periodical service models.                          (Kundra, 2011),(Kiadehi, 2014)




                                                                                                IP
91
      Evaluating periodical vendors.                                 (Kundra, 2011),(Kiadehi, 2014)




                                                                                              CR
Appendix C

Table C1
Generic goals and practices of cloud migration process areas.
No.
 1
 2
         Abb.
         GG1
         GG2
                   Achieve specific goals
                   Institutionalize a managed
                   process
                             objective

                                                                    US        General practices
                                                  GP 1.1: Perform Specific Practices.
                                                  GP 2.1: Establish an organizational policy
                                                  GP 2.2: Plan the process
                                                                  AN
                                                  GP 2.3: Provide resources
                                                  GP 2.4: Assign responsibility
                                                  GP 2.5: Train people
                                                  GP 2.6: Manage configurations
                                                  GP 2.7: Identify and involve relevant stakeholders
                                                  GP 2.8: Monitor and control the process
                                                        M


                                                  GP 2.9: Objectively evaluate adherence
                                                  GP 2.10:Review status with higher level management
 3       GG3       Institutionalize a defined     GP 3.1: Establish a defined process
                   process                        GP 3.2: Collect improvement information
                                        ED




Appendix D

Table D1
                            PT




Specific goals of cloud migration process areas.
No.         Process                                                          Specific goals
1
                          Developing and expanding the knowledge about cloud computing
             CE




2
                          Changing the mentality
3
                          Understanding the legal requirement and implication related to the cloud.
        Expanding the
AC




4      cloud knowledge
                          Become fully aware of the cloud computing principles
5
                          Reviewing the standards related to the cloud.
6
                          Become fully aware of the cloud contract terms
7
                          Identifying the services and business processes.
8
        Identification of Identifying the cloud environment.
       opportunities and
9
            threats       Identifying opportunities
10
                          Identifying limitations




23 |
                                                 ACCEPTED MANUSCRIPT


No.        Process                                                            Specific goals
11
                          Identifying risks.

12
                          Developing the knowledge base about cloud computing

13
                          Understanding the applications.
14
                          Identifying the IT requirements.
15
                          Identifying the stakeholder’s requirement.
16
    Identification of Identifying security requirements.
   detail requirements




                                                                                                   T
17
      and solutions Identifying compatibility requirements.




                                                                                                 IP
18
                          Identifying the potential cloud hosting environment
19
                          Identifying potential solutions.




                                                                                               CR
20
                          Finding the optimized target resource.
21
                          Analyzing the cloud computing values (agility, efficiency, innovation, cost saving, availability)
22

24

25
                          Evaluating enterprise readiness.

                          Evaluating the market landscape.            US
                                                                    AN
                          Analyzing the business strategy.
26        Preliminary
                          Evaluating the technology vision.
       strategic analysis
27
                          Risk assessment and ranking these risks (dependent on probability, affect, etc.)
                                                         M


28
                          Reviewing the IT governance.
29
                          Evaluating the current stage of enterprise IT.
                                        ED




30
                          SWOT analysis
31
                          Setting goals (technical and financial) and target attribute (deployment, service & ownership models)
                          PT




32
                          Tuning the bench point for legal compatibility and security.
         Goal setting
33
                          Specify the architecture of the target.
             CE




34
                          Characterizing the objectives aligned with enterprise strategy.
35
                          Analyzing stakeholder requirements.
36
AC




                          Analyzing software and hardware requirements the cloud point of view.
37
                          Analyzing transparency, certificates and audits.
38     Analyze the detail
       requirements and Analyzing required it capabilities (technical, human, organizational).
           solutions
39
                          Managerial & technical feasibility analysis.
40
                          Analyzing IT outsourcing capability.
41
                          Analyzing organizational attributes




24 |
                                                     ACCEPTED MANUSCRIPT


No.         Process                                                            Specific goals


42
                            Economical feasibility analysis


43
                            Analyzing infrastructure flexibility.
44
                            Analyzing application compatibility with potential cloud environment.
45
                            Developing a cloud knowledge based decision support system
46
                            Choosing the suitable implementation platform.
47




                                                                                                     T
                            Evaluating the suitability of cloud-based services and cloud-based solutions.
         Choosing the
48        solutions




                                                                                                   IP
                            Ranking the services based on user experiences and service performance.
49
                            Choosing appropriate service and solution.




                                                                                                 CR
50
                            Choosing an appropriate cloud service provider.

51
                            Policy making and planning for cloud migration.
52

53
                            Categorizing the current services & data.

                            Choosing the immigrant services.
                                                                         US
                                                                       AN
54
                            Assigning responsibilities.
55
                            Preparing the interoperability strategy.
56
                            Ensuring the convergence between enterprise architecture and cloud computing
                                                              M


57
                            Preparing the elastic strategy.
         Develop the
58     migration strategy
                            Preparing the multi tenancy requirements.
                                          ED




59
                            Modernization and adaptation of legacy application in the cloud environment
60
                            Preparing the outsourcing strategy.
                            PT




61
                            Developing a transfer schedule.
62
                            Considering the required turn over.
             CE




63
                            Effective contracting.
64
                            Preparing an exit strategy.
65
AC




                            Appling the migrating strategy.
66
                            Choosing the pilot project.
67       Pilot test and
                            Test the systems.
          migration
68
                            Extracting and migrating the data.
69
                            Seamlessly migrate to cloud computing services.
70
       Migration process Monitoring the application for its availability & performance throughout the migration process.
         control and
71
          evaluation     Ensuring integration between new systems and older systems.




25 |
                                             ACCEPTED MANUSCRIPT


No.        Process                                                          Specific goals
72
                       Ensuring the service continuity management throughout the migration process.
73
                       Monitoring and controlling the migration process.
74
                       Technical and commercial goals verification
75
                       Creating a new set of IT skills depending on the needs.
76
                       Applying an agile approach to innovation in services.
         Adaptation
77
                       IT governance alignment to organizational strategy
78




                                                                                                 T
                       Architecture recovery and adaptation.
79




                                                                                               IP
                       Implementing a security structure in order to defend against cyber threats.
80
                       Developing guidelines to guide migration.




                                                                                             CR
81
                       Vendor management
82       Support and
                       Updating and maintenance
         maintenance
83

84

85
                       Support

                                                                   US
                       Reviewing all related policies to ensure support for cloud computing services.
                                                                 AN
                       Assigning a routine budget.
86
                       Monitoring the SLA.
87
                       Evaluating user quality of experiences.
                                                     M


88
                       Monitoring quality of services.
         Continual
89       monitoring
                       Ensuring the transparency, maintenance and updating.
                                    ED




90
                       Evaluating periodical service models.
91
                       Evaluating periodical vendors.
92
                       PT




                       Establish and maintain process-performance models for the migration processes.
93
                       The migration process is quantitatively managed
94                     Improvements are proactively identified, evaluated using statistical and other quantitative techniques.
            CE




      Optimizing
95                     Measurable improvements to the organization’s processes and technologies are deployed and evaluated using
                       statistical and other quantitative techniques.
96                     Systematically determining the root causes of outcomes.
AC




97 Infusion
                       Systematically addressing the root causes of outcomes.
98                     Ensuring the maximum usage of application’s potential in a deep, broad and comprehensive way in the
                       organizational or individual work system.




26 |
                                               ACCEPTED MANUSCRIPT


7. References
Abderrahim, W., Choukair, Z., 2014. A framework architecture based model for cloud computing adaptive migration, 2014 Global
       Information Infrastructure and Networking Symposium, GIIS 2014, pp. 1 - 6.
Adrees, S.M., Omer, K.a.M., Sheta, E.O., 2015. cloud computing architecture for higher education in the third world countries (republic of
       the sudan as model). International Journal of Database Management Systems 7, 13-24.
Alabbadi, M.M., 2011. Cloud computing for education and learning: Education and learning as a service (ELaaS), Interactive Collaborative
       Learning (ICL), 2011 14th International Conference on. IEEE, pp. 589-594.
Alkhalil, A., Sahandi, R., John, D., 2014. Migration to Cloud Computing: A Decision Process Model, Central European Conference on
       Information and Intelligent Systems. Faculty of Organization and Informatics Varazdin, pp. 154-163.
Alonso, J.M., Orue-Echevarria, L., Escalante, M., Gorroñogoitia, J., Presenza, D., 2013. Cloud modernization assessment framework:
       Analyzing the impact of a potential migration to Cloud, Maintenance and Evolution of Service-Oriented and Cloud-Based Systems
       (MESOCA), 2013 IEEE 7th International Symposium on the. IEEE, pp. 64-73.
Alsaeed, N., Saleh, M., 2015. Towards Cloud Computing Services for Higher Educational Institutions: Concepts & Literature Review,
       Cloud Computing (ICCC), 2015 International Conference on. IEEE, pp. 1-7.




                                                                                                   T
Alsaffar, A.A., Shin, Y.R., Huh, E.N., 2015. IPTV Service Framework Based on Secure Authentication and Lightweight Content Encryption
       for Screen-Migration in Cloud Computing. Advances in Multimedia 2015, 9-22.




                                                                                                 IP
Alsufyani, R., Safdari, F., Chang, V., 2015. Migration of cloud services and deliveries to higher education, Proceedings of ESaaSA 2015-
       2nd International Workshop on Emerging Software as a Service and Analytics, In conjuction with the 5th International Conference on
       Cloud Computing and Services Science-CLOSER 2015, pp. 86-94.




                                                                                               CR
Andrikopoulos, V., Binz, T., Leymann, F., Strauch, S., 2013a. How to adapt applications for the Cloud environment. Computing 95, 493-
       535.
Andrikopoulos, V., Song, Z., Leymann, F., 2013b. Supporting the migration of applications to the cloud through a decision support system,
       2013 IEEE Sixth International Conference on Cloud Computing. IEEE, pp. 565-572.



                                                                   US
Andrikopoulos, V., Strauch, S., Leymann, F., 2013c. Decision Support for Application Migration to the Cloud:Challenges and Vision
       Proceedings of CLOSER’13, 149-155.
Babar, M.A., Chauhan, M.A., 2011. A tale of migration to cloud computing for sharing experiences and observations, Proceedings -
       International Conference on Software Engineering, Hawaii, USA, pp. 50-56.
Botto, M., González-Huerta, J., Insfran, E., 2014. Are model-driven techniques used as a means to migrate SOA applications to cloud
                                                                 AN
       computing? WEBIST 2014 - Proceedings of the 10th International Conference on Web Information Systems and Technologies 1,
       208-213.
Chan, H., Chieu, T., 2010. Ranking and mapping of applications to cloud computing services by SVD, Network Operations and
       Management Symposium Workshops (NOMS Wksps), 2010 IEEE/IFIP. IEEE, pp. 362-369.
Chang, V., Walters, R.J., Wills, G., 2013. The development that leads to the Cloud Computing Business Framework. International Journal of
                                                       M


       Information Management 33, 524-538.
Chauhan, M.A., Babar, M.A., 2012. Towards process support for migrating applications to cloud computing, Cloud and Service Computing
       (CSC), 2012 International Conference on. IEEE, pp. 80-87.
Cooper, R.B., Zmud, R.W., 1990. Information technology implementation research: a technological diffusion approach. Management
                                      ED




       science 36, 123-139.
Davis, F.D., 1989. Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS quarterly, 319-
       340.Douglas, A.C., Mills, J.E., Niang, M., Stepchenkova, S., Byun, S., Ruffini, C., Lee, S.K., Loutfi, J., Lee, J.-K., Atallah, M., 2008.
       Internet addiction: Meta-synthesis of qualitative research for the decade 1996–2006. Computers in Human Behavior 24, 3027-3044.
                          PT




El-Gazzar, R., Hustad, E., Olsen, D.H., 2016. Understanding cloud computing adoption issues: A Delphi study approach. Journal of Systems
       and Software 118, 64-84.
Gangwar, H., Date, H., Ramaswamy, R., 2015. Developing a Cloud-Computing Adoption Framework. Global Business Review 16, 632-
       651.García-Galán, J., Trinidad, P., Rana, O.F., Ruiz-Cortés, A., 2016. Automated configuration support for infrastructure migration to
            CE




       the cloud. Future Generation Computer Systems 55, 200-212.
Garg, S.K., Toosi, A.N., Gopalaiyengar, S.K., Buyya, R., 2014. SLA-based virtual machine management for heterogeneous workloads in a
       cloud datacenter. Journal of Network and Computer Applications 45, 108-120.
Garg, S.K., Versteeg, S., Buyya, R., 2011. Smicloud: A framework for comparing and ranking cloud services, Utility and Cloud Computing
       (UCC), 2011 Fourth IEEE International Conference on. IEEE, Melbourne, Australia, pp. 210-218.
AC




Garg, S.K., Versteeg, S., Buyya, R., 2013. A framework for ranking of cloud computing services. Future Generation Computer Systems 29,
       1012-1023.
Gholami, M.F., Daneshgar, F., Low, G., Beydoun, G., 2016. Cloud migration process—A survey, evaluation framework, and open
       challenges. Journal of Systems and Software 120, 31-69.
Greenwood, D., Khajeh-Hosseini, A., Smith, J., Sommerville, I., 2010. The cloud adoption toolkit: Addressing the challenges of cloud
       adoption in enterprise. Arxiv preprint.
Guillén, J., Miranda, J., Murillo, J.M., Canal, C., 2013. A service-oriented framework for developing cross cloud migratable software.
       Journal of Systems and Software 86, 2294-2308.
Hajjat, M., Sun, X., Sung, Y.-W.E., Maltz, D., Rao, S., Sripanidkulchai, K., Tawarmalani, M., 2011. Cloudward bound: planning for
       beneficial migration of enterprise applications to the cloud. ACM SIGCOMM Computer Communication Review 41, 243-254.
Hazen, B.T., Overstreet, R.E., Cegielski, C.G., 2012. Supply chain innovation diffusion: going beyond adoption. The International Journal
       of Logistics Management 23, 119-134.
Hwang, J., Bai, K., Tacci, M., Vukovic, M., Anerousis, N., 2016. Automation and orchestration framework for large-scale enterprise cloud
       migration. IBM Journal of Research and Development 60, 1: 1-1: 12.




27 |
                                              ACCEPTED MANUSCRIPT


Jamshidi, P., Ahmad, A., Pahl, C., 2013. Cloud migration research: a systematic review. Cloud Computing, IEEE Transactions on 1, 142-
       157.
Jasperson, J.S., Carter, P.E., Zmud, R.W., 2005. A comprehensive conceptualization of post-adoptive behaviors associated with information
       technology enabled work systems. Mis Quarterly 29, 525-557.Jermyn, J., Hwang, J., Bai, K., Vukovic, M., Anerousis, N., Stolfo, S.,
       2014. Improving readiness for enterprise migration to the cloud, Proceedings of the Middleware Industry Track. ACM, NY, USA,
       2014, pp. 51-57.
Johnson, B., Qu, Y., 2012. A holistic model for making cloud migration decision: A consideration of security, architecture and business
       economics, Parallel and Distributed Processing with Applications (ISPA), 2012 IEEE 10th International Symposium on. IEEE, pp.
       435-441.
Khajeh-Hosseini, A., Greenwood, D., Smith, J.W., Sommerville, I., 2010a. The cloud adoption toolkit: Addressing the challenges of cloud
       adoption in enterprise. arXiv preprint arXiv:1003.3866.
Khajeh-Hosseini, A., Greenwood, D., Sommerville, I., 2010b. Cloud migration: a case study of migrating an enterprise IT system to IaaS,
       Cloud Computing (CLOUD), 2010 IEEE 3rd International Conference on. IEEE, Miami, 2010, pp. 450-457.
Khajeh-Hosseini, A., Sommerville, I., Bogaerts, J., Teregowda, P., 2011. Decision support tools for cloud migration in the enterprise, Cloud
       Computing (CLOUD), 2011 IEEE International Conference on. IEEE, pp. 541-548.




                                                                                                T
Khan, N., Al-Yasiri, A., 2016. Framework for cloud computing adoption: A road map for Smes to cloud migration. International Journal on
       Cloud Computing: Services and Architecture (IJCCSA) 5, 1-15.




                                                                                              IP
Kiadehi, E.M., S, 2014. Cloud Computing Technology in Iran: Opportunities,Threats. International Journal of Electronics Communication
       and Computer Engineering 5, 166-172.
Kumar, A., Mishra, S., Mishra, A., 2015. Priority with adoptive data migration in case of disaster using cloud computing use style,




                                                                                            CR
       Proceedings - 2015 International Conference on Communication, Information and Computing Technology, ICCICT 2015, Mumbai,
       India, pp. 1-6.
Kundra, V., 2011. Federal cloud computing strategy. Washington D.C: The White House.
Kwon, T.H., Zmud, R.W., 1987. Unifying the fragmented models of information systems implementation, Critical issues in information



                                                                 US
       systems research. John Wiley & Sons, Inc., Chichester, UK, 1987, pp. 227-251.Lewis, G., Morris, E., Smith, D., 2005. Service-
       oriented migration and reuse technique (smart), Software Technology and Engineering Practice, 2005. 13th IEEE International
       Workshop on. IEEE, pp. 15-23.
Li, A., Yang, X., Kandula, S., Zhang, M., 2010. CloudCmp: comparing public cloud providers, Proceedings of the 10th ACM SIGCOMM
       conference on Internet measurement. ACM, Melbourne, Australia, pp. 1-14.
                                                               AN
Markovic, D.S., Zivkovic, D., Branovic, I., Popovic, R., Cvetkovic, D., 2013. Smart power grid and cloud computing. Renewable and
       Sustainable Energy Reviews 24, 566-577.
Mateescu, G., Vladescu, M., Sgarciu, V., 2014. Auditing cloud computing migration, SACI 2014 - 9th IEEE International Symposium on
       Applied Computational Intelligence and Informatics, Proceedings, Timisoara, pp. 263-268.
McClean, S., Shaw, A., 2005. From schism to continuum? The problematic relationship between expert and lay knowledge—an exploratory
                                                      M


       conceptual synthesis of two qualitative studies. Qualitative Health Research 15, 729-749.
Mell, P., Grance, T., 2011. The NIST definition of cloud computing. National Institute of Standards and Technology. Special Publication
       800-145.
Menychtas, A., Santzaridou, C., Kousiouris, G., Varvarigou, T., Orue-Echevarria, L., Alonso, J.M., Gorronogoitia, J., Bruneliere, H.,
                                     ED




       Strauss, O., Senkova, T., 2013. ARTIST Methodology and Framework: A novel approach for the migration of legacy software on the
       Cloud, Symbolic and Numeric Algorithms for Scientific Computing (SYNASC), 2013 15th International Symposium on. IEEE, pp.
       424-431.
Menzel, M., Ranjan, R., 2012. CloudGenius: decision support for web server cloud migration, Proceedings of the 21st international
                         PT




       conference on World Wide Web. ACM, Lyon, France, pp. 979-988.
Mircea, M., Andreescu, A.I., 2011. Using cloud computing in higher education: A strategy to improve agility in the current financial crisis.
       Communications of the IBIMA 2011, 1-15.
Misra, S.C., Mondal, A., 2011. Identification of a company’s suitability for the adoption of cloud computing and modelling its
           CE




       corresponding Return on Investment. Mathematical and Computer Modelling 53, 504-521.
Oates, B.J., 2006. Researching information systems and computing, 1 ed. Sage Publications, London.
Okai, S., Uddin, M., Arshad, A., Alsaqour, R., Shah, A., 2014. Cloud computing adoption model for universities to increase ICT
       proficiency. SAGE Open 4, 1-10.
Omerovic, A., Muntés-Mulero, V., Matthews, P., Gunka, A., 2013. Towards a method for decision support in multi-cloud environments.
AC




       CLOUD COMPUTING 2013, 244-250.
Pardeshi, V.H., 2014. Cloud Computing for Higher Education Institutes: Architecture, Strategy and Recommendations for Effective
       Adaptation. Procedia Economics and Finance 11, 589-599.
Pfitzmann, B., Joukov, N., 2011. Migration to multi-image cloud templates, Services Computing (SCC), 2011 IEEE International
       Conference on. IEEE, pp. 80-87.
Phaphoom, N., Wang, X., Samuel, S., Helmer, S., Abrahamsson, P., 2015. A survey study on major technical barriers affecting the decision
       to adopt cloud services. Journal of Systems and Software 103, 167-181.
Prasad, A., Green, P., Heales, J., Finau, G., 2014. On cloud computing service considerations for the small and medium enterprises,
       Twentieth Americas Conference on Information Systems.
Premkumar, G., 2003. A meta-analysis of research on information technology implementation in small business. Journal of organizational
       computing and electronic commerce 13, 91-121.
Rai, R., Sahoo, G., Mehfuz, S., 2015. Exploring the factors influencing the cloud computing adoption: a systematic study on cloud
       migration. SpringerPlus 4, 1-12.
Rewatkar, L.R., Lanjewar, U., 2010. Implementation of cloud computing on web application. International Journal of Computer
       Applications 2, 28-32.



28 |
                                              ACCEPTED MANUSCRIPT


Rimal, B.P., Choi, E., Lumb, I., 2009. A taxonomy and survey of cloud computing systems, INC, IMS and IDC, 2009. NCM'09. Fifth
        International Joint Conference on. Ieee, pp. 44-51.
Rockmann, R., Weeger, A., Gewald, H., 2014. Identifying Organizational Capabilities for the Enterprise-Wide Usage of Cloud Computing,
        PACIS, p. 355.
Sabi, H.M., Uzoka, F.M.E., Langmia, K., Njeh, F.N., 2016. Conceptualizing a model for adoption of cloud computing in education.
        International Journal of Information Management 36, 183-191.
Safari, F., Safari, N., Hasanzadeh, A., 2015a. The adoption of software-as-a-service (SaaS): ranking the determinants. Journal of Enterprise
        Information Management 28, 400-422.
Safari, N., Safari, F., Kazemi, M., Ahmadi, S., Hasanzadeh, A., 2015b. Prioritisation of cloud computing acceptance indicators using fuzzy
        AHP. International Journal of Business Information Systems 19, 488-504.Saga, V.L., Zmud, R.W., 1993. The nature and
        determinants of IT acceptance, routinization, and infusion, Proceedings of the IFIP TC8 working conference on diffusion, transfer and
        implementation of information technology. Elsevier Science Inc., pp. 67-86.
Sandelowski, M., Barroso, J., 2007. Handbook for synthesizing qualitative research. Springer Publishing Company, New York.
Sefraoui, O., Aissaoui, M., Eleuldj, M., 2014. Cloud computing migration and IT resources rationalization, International Conference on
        Multimedia Computing and Systems -Proceedings, pp. 1164-1168.




                                                                                                 T
Sharma, T., Banga, V.K., 2013. Efficient and Enhanced Algorithm in Cloud Computing. International Journal of Soft Computing and
        Engineering 13, 2231-2307.




                                                                                               IP
SIclovan, A., 2012. The Future of Cloud Computing. BRAND. Broad Research in Accounting, Negotiation, and Distribution 3, pp. 36-39.
Srirama, S.N., Ivanistsev, V., Jakovits, P., Willmore, C., 2013. Direct migration of scientific computing experiments to the cloud,
        Proceedings of the 2013 International Conference on High Performance Computing and Simulation, HPCS 2013, pp. 27-34.




                                                                                             CR
Subramanian, S., Seshasaayee, A., 2014. Review & Proposal for a Cloud based Framework for Indian Higher Education. International
        Journal Of Engineering And Computer Science 3.
Surendro, K., Fardani, A., 2012. Identification of SME readiness to implement cloud computing, loud Computing and Social Networking
        (ICCCSN), pp. 1-4.



                                                                  US
Tashkandi, A., Al-Jabri, I., 2015. Cloud Computing Adoption by Higher Education Institutions in Saudi Arabia: Analysis Based on TOE,
        2015 International Conference on Cloud Computing, ICCC 2015, Riyadh, pp. 1-8.
Tayal, S., 2011. Tasks scheduling optimization for the cloud computing systems. International Journal of Advanced Engineering Sciences
        And Technologies (IJAEST) 5, 111-115.
Team, C.P., 2011. CMMI for Services Version 1.3. Carnegie Mellon University publication.
                                                                AN
, Pittsburgh, Pennsylvania.Thorne, S., 2009. The role of qualitative research within an evidence-based context: can metasynthesis be the
        answer? International journal of nursing studies 46, 569-575.
Tornatzky, L., Fleischer, M., 1990. The Processes of Technological Innovation. Lexington, MA: Lexington Books.
Torrecilla-Salinas, C., Sedeño, J., Escalona, M., Mejías, M., 2016. Agile, Web Engineering and Capability Maturity Model Integration: A
        systematic literature review. Information and Software Technology 71, 92-107.
                                                      M


Venkatesh, V., Davis, F.D., 2000. A theoretical extension of the technology acceptance model: Four longitudinal field studies. Management
        science 46, 186-204.
Venkatesh, V., Morris, M.G., Davis, G.B., Davis, F.D., 2003. User acceptance of information technology: Toward a unified view. MIS
        quarterly, 425-478.
                                     ED




Venkatesh, V., Thong, J.Y., Xu, X., 2012. Consumer acceptance and use of information technology: extending the unified theory of
        acceptance and use of technology. MIS quarterly 36, 157-178.
Wielki, J., 2015. An analysis of the opportunities and challenges connected with utilization of the cloud computing model and the most
        important aspects of the migration strategy, Proceedings of the 2015 Federated Conference on Computer Science and Information
                         PT




        Systems, FedCSIS 2015, pp. 1569-1574.
Yaghmaei, O., Binesh, F., 2015. Impact of Applying Cloud Computing On Universities Expenses. IOSR Journal of Business and
        Management 17, 42-47.
Zimmer, L., 2006. Qualitative meta‐synthesis: a question of dialoguing with texts. Journal of advanced nursing 53, 311-318.
           CE




Zubrow, D., 2003. Current trends in adoption of the CMMI® Product Suite, Computer Software and Applications Conference, 2003.
        COMPSAC 2003. Proceedings. 27th Annual International. IEEE, Dallas,TX, USA, pp. 126-129.
AC




29 |
                                    ACCEPTED MANUSCRIPT


Hamid reza Bazi is currently the Ph.D. candidate in information technology management at the Tarbiat
Modares University. His major research interests focus on cloud computing and migration models.



Alireza Hasanzadeh is an academic who graduated from the University of Tehran with a Ph.D. in systems
management. He is an associate Professor & Head of Information Technology Management Department at the
Tarbiat Modares University. He has published many works in IT-IS subjects in international journal of
information management, Knowledge-Based Systems, Computers & Education, Expert Systems with
Applications. He has a research interest in analysis and design and implementation of integrated management
information systems, intelligent information systems, cloud computing, and service oriented architecture.




                                                                            T
Ali Moeini received his Ph.D. in Nonlinear Systems at the University of Sussex, UK, in 1997. He is an




                                                                          IP
Associate Professor of Electrical & Computer Engineering at Faculty of Engineering Science, School of
Engineering, the University of Tehran, and ad joint Professor at Department of Information Technology
Management, Faculty of Management, the University of Tehran in Iran. His research interests include Formal




                                                                        CR
Methods in Knowledge and Software Engineering and Knowledge Management, Soft computing Methods,
Randomized Algorithms, Approximation Algorithms, and Bioinformatics. He has published many papers in
Journals and Conferences on the above mentioned topics.



                                                   US
                                                 AN
                                          M
                             ED
                   PT
         CE
AC




30 |
