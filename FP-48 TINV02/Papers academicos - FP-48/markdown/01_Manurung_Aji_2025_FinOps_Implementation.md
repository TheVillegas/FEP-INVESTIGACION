Scientific Journal of Informatics
Vol. 12, No. 4, November 2025
p-ISSN 2407-7658 https://journal.unnes.ac.id/journals/sji/index e-ISSN 2460-0040
Evaluating the Implementation of the FinOps Framework for Cloud
Infrastructure Cost Management: A Case Study of Technology
Companies in Indonesia
Hierony Manurung1*, Rizal Fathoni Aji2
1,2Faculty of Computer Science, Universitas Indonesia, Indonesia
Abstract.
Purpose: The management of cloud infrastructure costs has become increasingly relevant in light of the rapid rate of
cloud service adoption, especially in Indonesia's technology space, where there is tremendous economic pressure.
Cloud infrastructure cost management solutions such as the FinOps Framework are clearly intended to provide a greater
degree of accountability for financial governance and to enable cloud spending optimization when implemented
holistically. However, a critical empirical gap exists regarding the technical-cultural dissonance in emerging markets,
where the adoption of advanced cloud tools often outpaces the development of necessary financial accountability
structures. In this research, we want to evaluate how FinOps adoption maturity is in several technology companies, and
to find the gap between FinOps Framework principles and their real-world implementation.
Methods: A mixed-methods case study was employed using a sequential explanatory design. The qualitative phase
involved semi-structured interviews with six FinOps practitioners, followed by thematic analysis to identify adoption
patterns. Subsequently, in the quantitative phase, these qualitative findings were mapped to a three-point maturity
scoring matrix derived from the FinOps Framework (Crawl, Walk, Run) to calculate and benchmark the specific
maturity levels of each participating organization.
Result: From the interviews, there was an emphasis on key processes, such as cost ownership, budgeting, and
governance, which were quite centralized, reactive, and somewhat informal, although everyone was using technical
optimization approaches such as rightsizing. Our quantitative analysis corroborated this, with a cohort average maturity
score of only 1.53 out of 3. This indicates a general maturity score in the "Crawl" or first stage, indicating shortcomings
related to the process element of the basic practices not being integrated in a systematic way.
Novelty: This research provides meaningful and helpful insights into the real challenges of tech companies in Indonesia
implementing FinOps. Our research provides a clear baseline for companies working locally by measuring maturity
levels and making recommendations at the end. More importantly, beyond technical optimization, it clearly identifies
the need to formalize policies and to improve cooperation across functional areas. These findings suggest that future
maturity assessment frameworks should decouple technical tooling scores from cultural readiness to diagnose the
adoption patterns typical of emerging markets accurately. This mixed methods approach should be extended to other
research by increasing sample size and allowing for a deeper exploration of the cultural context.
Keywords: Cloud computing, FinOps framework, Cost optimization
Received November 2025 / Revised December 2025 / Accepted December 2025
This work is licensed under a Creative Commons Attribution 4.0 International License.
INTRODUCTION
The surging demand for dependable computing is creating a major transition to IT infrastructure. As a
result, many organizations are shifting from physical servers to cloud computing [1], [2], [3], and [4]. The
primary motive for this change is the pay-as-you-go billing model, which can spare an organization the
high upfront capital expenditures associated with housing their own infrastructure. This is a significant
advantage because reaching a level of service quality provided by the large public cloud providers would
require significant time and capital investment [5], [6], [7]. Therefore, the pay-as-you-go model has an
opportunity to greatly reduce capital expenditures and aid in operational efficiency. Unfortunately, in the
absence of disciplined governance, there are inefficiencies such as waste, poor visibility, and poor
forecasting that can limit these advantages [8]. As the adoption of the cloud grows, these issues of
governance become especially problematic and important, especially when world cloud spending is
increasing at a rapid rate. Statista has forecasted that worldwide cloud spending is expected to be greater
than $1.4 trillion in 2027 [9], up from just $675 billion in 2024, as illustrated in Figure 1. Gartner predicts
*Corresponding author.
Email addresses: hierony.manurung@ui.ac.id (Manurung), rizal@cs.ui.ac.id (Aji)
DOI: 10.15294/sji.v12i4.36226
Scientific Journal of Informatics, Vol. 12, No. 4, November 2025 | 709

that cloud spending will top off at $723 billion in 2025 [10]. More robust cloud cost governance is much
needed, and there are some indications that leading experts are recommending organizations implement
best practices and governance regarding cloud cost management.
Figure 1. Usage of public cloud worldwide from 2021 - 2027 (USD) [10]
This trend highlights the urgent need for a new model of financial accountability enabled by digital
solutions, particularly in Indonesia, where a drastic shift from hyper-growth to survival creates a unique
context. The Indonesian technology sector is currently navigating a “'tech winter” of distinct intensity; after
77,965 layoffs in the tech sector from January to December 2024 [11], the sector is under immense pressure
to prioritize immediate business sustainability over previous goal-based growth models [12]. Furthermore,
the Indonesian context is critical to study due to a specific crisis of trust in financial governance. Recent
corporate scandals in major local technology companies have highlighted systemic issues in accountability.
For instance, trust has been eroded by allegations of financial mismanagement at Investree and by disputes
over exaggerated growth metrics at Efishery [13]. These incidents demonstrate that for Indonesian
technology companies, disciplined cloud cost governance is not merely an optimization tactic, but a
necessary strategy to restore investor confidence and enforce the financial transparency that the market now
demands.
FinOps is a framework and a cultural practice that allows organizations to maximize their value out of
technology and cloud. FinOps allows for cross-functional collaboration between engineering, finance, and
business teams, enables financial accountability, and paves the way to timely and data-driven decisions
[14]. The term “FinOps” was first coined at the Cloud Economic Summit in early 2019. The term “FinOps”
has become increasingly popular as a keyword over the last four years, according to Google Trends data
for the terms “FinOps” and “Cloud FinOps,” as illustrated in Figure 2. This suggests cost optimization
solutions related to cloud infrastructure are becoming more popular.
Figure 2. Searches for the term 'FinOps' from 2022 - [15].
710 | Scientific Journal of Informatics, Vol. 12, No. 4, November 2025

Though comprehensive frameworks, including IT Financial Management (ITFM) and Technology
Business Management (TBM), do exist for aligning technology expenses with business value, these
frameworks are generally intended for use in stable, on-premises systems or for managing comprehensive
IT budgets [16]. FinOps, on the other hand, is the most applicable framework for cloud expenses because
it targets the high-velocity, variable nature of OpEx models while, at the same time, also addressing the
cultural divides that prevent accountability between the engineering and finance sides of local businesses
[17]. The FinOps Framework details the theoretical benefits of improving financial management,
eliminating waste, and increasing visibility of expenses [14], [17], [18], [19], but it appears that the current
state of the industry is stuck on the surface level of expense management.
While the FinOps Framework had been widely researched among developed markets, where it is widely
indicated that 27% of cloud budget is wasted annually [20]. Literature focusing on the Indonesian
environment specifically, though minimal, is essential, especially when Indonesia experiences the speedy
development of the digital infrastructure environment, where technology firms are typified by their fiercely
cloudy adoptive strategy with high economic fluctuation [12]. Differing from the markets of the North
American environment, where the financial management of the environment is well documented,
technology firms of the Indonesian markets are presently undergoing a new “efficiency shift” phase without
local standards. It is indicated that the digital economy of the Southeast Asian nation has made a new shift,
forsaking the “growth-at-all-costs” paradigm for the pursuit of profitability [21].
Despite the heavy economic pressure on cutting costs, up until now, there is still no empirical study on
benchmarking the implementation of cloud financial governance practices among Indonesian companies.
This study will fill the gap of knowledge by examining the FinOps level of Indonesian tech companies,
specifically benchmarking their practices with the “Crawl, Walk, Run” model. This study will add new
knowledge to the existing literature in the following ways: first, it will offer the first empirical
benchmarking on the cloud financial governance practices of Indonesian markets, and it will also offer a
critical validation of the TC dissonance phenomenon, showing that emerging markets will, on average,
achieve the optimal level of technology but not the accountability needed.
METHODS
To achieve a rich and contextual understanding of FinOps adoption, we employed a mixed-methods case
study design. This approach was warranted in order to study a complex, real-world phenomenon. With this
approach, we developed a quantitative benchmark of practitioners' FinOps maturity level, and we gleaned
insightful qualitative evidence from their experiences [22].
The researchers conducted semi-structured interviews to gather data, which contributed to a multi-faceted
and contextual grasp of participants' practices, experiences, and perspectives. This well-known qualitative
method allows researchers to explore opinions while utilizing newly revealed data during the semi-
structured interview [23]. Semi-structured interviews allow the researcher to follow a procedure and still
assist the process of analyzing themes that emerge through the conversation, including problems that may
not have been previously recognized. This provides an avenue for obtaining further specific and appropriate
information relevant to the study.
Participants were selected via purposive sampling methods; we intentionally chose six practitioners from a
range of technology companies based in Indonesia and who were all selected for predetermined criteria in
line with the objectives of the study. Purposive sampling is a common method for selecting participants
used in qualitative research to ensure that the participants have relevant knowledge or experiences that
enable the achievement of the study's aims [24]. The selected respondents were Cloud Infrastructure
Architects with direct experience controlling costs of cloud infrastructure from a business perspective (e.g.,
data-driven decisions and budget allocation) and from a technical perspective (e.g., optimizing resources
and monitoring billing). Utilizing this approach helps ensure that the information obtained is relevant,
contextual, meaningful, and valuable contributions to address the research problem aligned with the aims
of the study. The participant demographics are shown in Table 1.
Scientific Journal of Informatics, Vol. 12, No. 4, November 2025 | 711

Table 1. Participants demographics
Participant Code Industry Annual Cloud Spend ($) Years of Experience
P1 Software as a Service (SaaS) 4,000,000 5 Years
P2 Fintech - Payment Gateway 10,000,000 12 Years
P3 Online Travel Platform 12,500,000 10 Years
P4 IT Consulting 3,200,000 10 Years
P5 E-Groceries 1,000,000 10 Years
P6 Fintech - Digital Banking 8,000,000 9 Years
The FinOps Framework and relevant research on cloud cost optimization and FinOps practices were
consulted in the development of the interview questions. Evidence from earlier research on workload-aware
optimization in cloud-native/serverless contexts, including commitments, benchmarking, and estimation
[25], cross-functional decision-making and cost visibility [26], spend-leakage detection and anomaly
analysis [27], and ML-assisted demand forecasting and high-performance computer cost control [28]. In
actuality, the questions look at how businesses accomplish visibility, allocation, and reporting in the Inform
phase; how they pursue commitment-based discounts and rightsizing during optimization; and how
operationalization, governance, and automation support operations in the Operate phase. To maintain
uniform coverage while enabling more in-depth examination of context-specific concerns, a semi-
structured format was selected. The list of interview questions is shown in Table 2.
Table 2. Interview questions
No Question
FinOps Phase 1: Inform (Visibility, Allocation, and Reporting)
1. Who on your team is ultimately in charge of monitoring cloud spending? Could you also explain to me how you actually
assign those expenses to the particular divisions or goods that make use of them? [26]
2. Describe an instance where you experienced an unforeseen increase in expenses. What was the procedure for taking
action, and how did your team initially identify it? [27]
3. Describe an instance where you experienced an unforeseen increase in expenses. What was the procedure for taking
action, and how did your team initially identify it? [27]
FinOps Phase 2: Optimize (Optimization and Efficiency)
4. Discuss "rightsizing" with me. To ensure that you're not overprovisioning, how often does your infrastructure team check
the sizes of resources like servers or databases? [28]
5. Do you currently use commitment-based discounts to reduce your expenses, such as Savings Plans or Reserved
Instances? [25], [27]
6. What are the primary tactics your team employs on a daily basis to maximize or minimize cloud spending, aside from
RIs and rightsizing? [27], [26]
FinOps Phase 3: Operate (Operationalization and Automation)
7. How can you make your engineers consider cost? If so, how does that awareness fit into their regular, day-to-day
operations? [26]
8. Does the governance have a formal policy? What guidelines must a team adhere to, for instance, before launching a new
cloud resource? [27]
9. Do you use any tools or platforms to track and control cloud expenses? [28]
Impact, Challenges, and Future Development
10. What has been your greatest success or "win" from your cost management work? [26]
11. Can that be quantified? Specifically, how much money have you saved or the total cost avoidance you have accomplished
since implementing these practices? [29]
12. What is the hardest thing you are dealing with today? What is the largest problem or challenge right now?[25]
13. What are your company's plans for FinOps in the future? What do you want to happen, perhaps in the next year or two,
to current practice? [28]
To examine the data, a sequential explanatory analysis approach was used. The qualitative data, extracted
from the interview transcriptions, was analyzed through the use of thematic analysis. To allow efficient
coding and the representation of these codes on thematical maps, the transcriptions were imported into the
qualitative data analysis software, NVivo. To promote the trustworthiness and validity of the coding
approach, the peer-debriefing technique was used. The initial coding and thematical grouping of the data
was carried out by the primary researcher using the NVivo software, with the secondary author acting as
the strategic auditor, critically assessing the identified themes and the code-book structure, to check
assumptions and reduce the perspective of the researcher. This dual assessment approach allowed for the
logical integrity of the results. Having completed the qualitative analysis, the data was extracted through
the use of the researcher-administrated scoring tool, on the transcriptions and supportive documentation,
rather than the use of survey questionnaires. This involved the mapping of the participant's data on a defined
rubric, on the Maturity Stages of FinOps Framework: “Crawl” for reactive/ad-hoc practices (1 point),
712 | Scientific Journal of Informatics, Vol. 12, No. 4, November 2025

“Walk” for defined & proactive practices (2 points), and “Run” for automated & data-driven practices (3
points). For reliability purposes, the data was assessed independently by the researchers over the seven
domains of FinOps, with any defined conflicts addressed through the use of consensus. Analysis of the data
used the descriptive statistical method, where the average score for the arithmetic mean calculation of the
data for each participant was used, deriving the individual FinOps Maturity score, on which the group
average score was used on subsequent calculation, for the determination of the FinOps Maturity level of
the group. The approach is illustrated in Figure 3.
Figure 3. Methodology flowchart
RESULT AND DISCUSSION
In the following chapter, results will be reported and discussed. Results consist of the identified themes
through thematic analysis, as well as the gap analysis on observed practices and the FinOps Framework.
The chapter ends with a summary of the findings as well as implications.
Thematic analysis theme
Based on the thematic analysis result of interview transcripts from six Cloud Infrastructure Architects, we
found several key themes. These themes reflect organizational practices and challenges in FinOps adoption.
This result was shown in Table 3, which summarizes each theme, along with supporting keywords and
representative participant quotations. This substantiates the findings and provides empirical context for
interpreting the results.
Table 3. Thematic analysis themes
Theme Supporting Words Quote from Participants
Responsibility DevOps, Special "Each product's DevOps team is responsible for managing cloud costs." (P1)
for Cloud Cost Workgroup, Head of
Management Engineering, Lead "We have a special workgroup that monitors and manages cloud spending."
Site Reliability (P2)
Engineer
"At present, accountability lies solely with the Head of Engineering and the
Lead Site Reliability Engineer. A cost allocation process on a per-
department basis has not yet been implemented." (P3)
“Our organization recently hired a FinOps Lead who acts as a gatekeeper for
cloud costs. However, clear cost ownership is still missing for example,
showback or chargeback mechanisms for stakeholders have not yet been
implemented.” (P6)
Budgeting and Rarely, reactive, not "Budgeting comes from the CTO’s direction. Forecasting is based on
Forecasting yet historical cost trends." (P2)
Challenges
"Budgeting is rarely done; previously, it was reactive, but now it's
improving." (P3)
"A formal budgeting process is not yet in place; we only make estimations
regarding the cost impact of new service releases. As for forecasting, we
currently rely solely on the native forecast feature within AWS Cost
Explorer." (P5)
Scientific Journal of Informatics, Vol. 12, No. 4, November 2025 | 713

| Theme  | Supporting Words  |     | Quote from Participants  |     |     |
| ------ | ----------------- | --- | ------------------------ | --- | --- |

Cost  Enterprise  contracts,  "We use enterprise contracts, spot instances, and shift to self-hosted tools."
| Optimization  | spot                   | instances,  (P1)                                                   |     |     |     |
| ------------- | ---------------------- | ------------------------------------------------------------------ | --- | --- | --- |
| Strategies    | reserved               | instances,                                                         |     |     |     |
|               | rightsize, unused VM,  | "We rightsize daily and use reserved instances for savings." (P2)  |     |     |     |
|               | start/stop             | non-                                                               |     |     |     |

production
|     |     | "Low-hanging  | fruit  like  turning  | off  unused  VMs  | or  scaling  down  |
| --- | --- | ------------- | --------------------- | ----------------- | ------------------ |
environments are our focus." (P3)

"Utilization of discounts such as Savings Plans and Spot Instances." (P4)

"Implementing start/stop schedulers for non-production environments." (P5)

“We used EDP (Enterprise Discount Program), Commitment used discount,
and spot instances.” (P6)

Lack  of  Cost  Still limited, no clear  "Unfortunately, it's still limited to the Infra and management teams." (P1)
| Awareness  | awareness,  | not    |     |     |     |
| ---------- | ----------- | ------ | --- | --- | --- |
integrated  "There's no clear awareness. Most engineers don’t see cost as their concern."
(P2)

"We’re trying to integrate cost visibility into daily workflows, but it’s still in
progress.” (P3)"

"Since cloud infrastructure costs are currently managed exclusively by the
Head of Engineering and the Lead SRE, cost-awareness practices have not
yet been integrated into the engineering team's workflow." (P5)

Cost visibility is still limited. We have a dashboard that calculates spend for
each GCP project, but it has not yet been distributed to other stakeholders
through showback or chargeback.” (P6)
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
Limited  No  formal  policy,  "Any team intending to use new cloud resources must first obtain approval
| Governance   | approval              | of  the  from the infrastructure team." (P2)  |     |     |     |
| ------------ | --------------------- | --------------------------------------------- | --- | --- | --- |
| and  Policy  | infrastructure team,  |                                               |     |     |     |
Enforcement  "No formal policy, only estimates and mutual understanding." (P3)

"All changes to the cloud environment require prior approval from the Head
of Engineering or the Lead SRE." (P5)
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
Tools for Cost  In-house  app,  "We built an in-house app combined with Metabase for cost visualization."
| Monitoring  | Metabase, AWS Cost   | (P1)                                                      |     |     |     |
| ----------- | -------------------- | --------------------------------------------------------- | --- | --- | --- |
|             | Explorer,            | Cast.ai,                                                  |     |     |     |
|             | Infracost, Optscale  | "We use AWS Cost Explorer, cast.ai, and infracost." (P2)  |     |     |     |

"The tools we use are the billing pages provided by each cloud provider. We
also use another tool, Optscale, but it is not yet fully utilized." (P4)
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
Future  Increase  cost  "Increase cost awareness among engineers and stop overestimating capacity
| Expectations  | awareness,       | stop  and cloud resource specifications." (P1)  |     |     |     |
| ------------- | ---------------- | ----------------------------------------------- | --- | --- | --- |
| for  FinOps   | overestimating,  | real-                                           |     |     |     |
Integration and  time dashboard  "FinOps practices should continue to be improved and become a non-
Collaboration  functional requirement for all engineering teams." (P2)

"Rising awareness of cloud resource costs so that developers can take this
into account when building applications." (P3)

"There should be tools that make FinOps implementation easier, and if the
tools are paid, the cost should still be reasonable." (P4)

"There should be a real-time dashboard that can used as a single source of
truth for tracking cloud infrastructure cost trends." (P5)

Several recurring themes were identified from the thematic analysis of the interview transcripts. These
themes were classified and calculated based on frequency, and then these themes were mapped to the
FinOps Framework's core capability domains to offer a more solid, quantitative interpretation of these
findings. The findings were presented in Table 4. The findings show that even though all of the
714 | Scientific Journal of Informatics, Vol. 12, No. 4, November 2025

organizations  adopt  technical  optimization  capabilities, most  of  them have not  established  cultural
capabilities such as ownership and governance.

Table 4. Frequency of FinOps capability gaps based on thematic analysis (N=6)
| FinOps  |                       |     |     | Identified Theme (Based on  |              |     |     | Frequency  |             |
| ------- | --------------------- | --- | --- | --------------------------- | ------------ | --- | --- | ---------- | ----------- |
|         | Framework Capability  |     |     |                             |              |     |     |            | Percentage  |
| Domain  |                       |     |     |                             | Interviews)  |     |     | (N = 6)    |             |
Understand  Allocation  [Gap] Cost ownership is centralized,  6  100 %
| Usage & Cost  |                 |     |     | no showback/chargeback.               |     |     |     |     |      |
| ------------- | --------------- | --- | --- | ------------------------------------- | --- | --- | --- | --- | ---- |
|               |                 |     |     |                                       |     |     |     |     |      |
|               |                 |     |     | [Gap] Process is reactive, informal,  |     |     |     |     |      |
|               | Budgeting and   |     |     | or rarely done.                       |     |     |     | 5   | 83%  |
|               | Forecasting     |     |     |                                       |     |     |     |     |      |
|               |                 |     |     |                                       |     |     |     |     |      |
| Quantify      |                 |     |     | [Gap] No formal process to link       |     |     |     |     |      |
Business Value  Unit Economics  cloud cost to business value.  6  100%
|                 |     |     |     |             |           |        |       |     |     |
| --------------- | --- | --- | --- | ----------- | --------- | ------ | ----- | --- | --- |
| Optimize Usage  |     |     |     |             |           |        |       |     |     |
| & Cost          |     |     |     | [Positive]  | Actively  | using  | RIs,  |     |     |
  Rate Optimization  Savings Plans, or Spot Instances   4  67%
|                  |                        |            |     |                                       |           |                      |     |     |       |
| ---------------- | ---------------------- | ---------- | --- | ------------------------------------- | --------- | -------------------- | --- | --- | ----- |
|                  |                        |            |     | [Positive] Using "low-hanging fruit"  |           |                      |     |     |       |
|                  | Workload Optimization  |            |     | (rightsizing, start/stop).            |           |                      |     | 5   | 83%   |
| Manage           | the                    |            |     |                                       |           |                      |     |     |       |
| FinOps Practice  |                        |            |     |                                       |           |                      |     |     |       |
|                  | Policy & Governance    |            |     | [Gap] No formal policies currently    |           |                      |     |     |       |
|                  |                        |            |     | applied,                              | resource  | approval             | is  | 4   | 67%   |
|                  |                        |            |     | informal.                             |           |                      |     |     |       |
|                  |                        |            |     |                                       |           |                      |     |     |       |
|                  | FinOps Tools           |            |     | [Gap] Tooling is fragmented, still    |           |                      |     |     |       |
|                  |                        |            |     | manual, and underutilized.            |           |                      |     | 5   | 83%   |
|                  |                        |            |     |                                       |           |                      |     |     |       |
|                  | FinOps                 | Education  | &   | [Gap]                                 | Lack      | of  cost  awareness  |     |     |       |
|                  | Enablement             |            |     | among engineers.                      |           |                      |     | 5   | 83%   |
|                  |                        |            |     |                                       |           |                      |     |     |       |
|                  | Cross-functional       |            |     | [Gap] Teams are siloed; no shared     |           |                      |     |     |       |
|                  | Collaboration          |            |     | accountability.                       |           |                      |     | 6   | 100%  |

FinOps maturity score
To find the maturity level of each participant, we developed a 3-point scale that defined the maturity for
each subject. We refer to this model from the FinOps maturity model, which is "crawl", "walk", "run".
Based on the interview and supporting documentation that we got, we scored their practice remarks against
the primary FinOps competencies. Our 3-point scale was defined as follows:
●
1 - Crawl: The method is manual, reactive, ad hoc, or highly centralized. We used this score for
responses such as "no formal policy," "budgeting rarely done," or "accountability lies solely with the
Head of Engineering".
●  2 - Walk: The practice is proactive, well-defined, and supported by fundamental techniques. We used
this score for responses such as "rightsizing daily," "using RIs/Savings Plans," and "implementing
start/stop schedulers."
●  3 - Run: The practice and procedure are data-driven, fully automated, and completely integrated
throughout the company.

The participant's score for each domain is described in Table 5.

Table 5. FinOps maturity scoring matrix
Final
|          |      | (2)   | (3)    | (4) Rate   |     |      |      |              |        |
| -------- | ---- | ----- | ------ | ---------- | --- | ---- | ---- | ------------ | ------ |
| Particip | (1)  |       |        |            |     | (5)  | (6)  |              | Score  |
|          |      | Budge | Rights | Optimizati |     |      |      | (7) Tooling  |        |
ant  Allocation  ting  izing  on  Awareness  Governance  (Average
)
| P1  | 2   | 2   | 2   | 2   |     | 1   | 2   | 2   | 1.86  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
| P2  | 2   | 2   | 2   | 2   |     | 2   | 2   | 2   | 2     |
| P3  | 1   | 1   | 2   | 2   |     | 1   | 1   | 1   | 1.29  |
| P4  | 1   | 1   | 2   | 2   |     | 1   | 1   | 1   | 1.29  |
| P5  | 1   | 1   | 2   | 2   |     | 1   | 2   | 1   | 1.43  |
| P6  | 1   | 1   | 2   | 2   |     | 1   | 1   | 1   | 1.29  |
Cohort
|     |     |     |     |     |     |     |     |     | 1.53  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
Average:
Scientific Journal of Informatics, Vol. 12, No. 4, November 2025 | 715

Each individual's final score is derived from the mean of the seven key skill areas (Allocation, Budgeting,
Rightsizing, Rate Optimization, Awareness, Governance, and Tooling). Refer to Figure 4 for the details.
The average score for the cohort of six participants is 1.53 out of 3.00; these results quantitatively suggest
that the entire cohort is operating between the "Crawl" and "Walk" maturity models. Only participant 2
(P2) functions that walk the maturity model with a score of 2.00 out of 3.00.
Figure 4. FinOps maturity score
Discussion and implications
The quantitative result of the study will show that the FinOps Maturity Score for Indonesian technology
businesses is averaged at 1.53 out of a possible 3.0, indicating that the group of technology businesses is
firmly positioned within the "Crawl" and "Walk" phases of the FinOps Framework Maturity Model [14].
Despite the fact that participants possessed aptitude for the tech-related FinOps tasks of rightsizing,
Reserved Instances, and so forth, they show several vulnerabilities, especially regarding cultural and
process-related aspects, specifically the Governance and Cost Allocation aspects. This disequality between
the tech-related FinOps aptitude and other FinOps-related aspects of Indonesian technology businesses
reveals that FinOps initiatives are currently seen by Indonesian technology organizations merely for their
practical, tech-related, hence budget-cutting, purposes. This specific data fits existing literature that
distinguishes IT Financial Management (ITFM) services, which tend to handle budgeting statically, from
sound Cloud Financial Management practices, which demand cloud budgeting processes performed on a
real-time, engineering accountability level [5]. The data regarding the centralization of FinOps technology
ownership, indicated that 83% of participants believed that ownership of FinOps technology services stayed
exclusively within the management of the current Head of Engineering and not with the existing distributed
DevOps, suggests that Indonesian technology businesses actually face a bottleneck situation. This situation,
where FinOps ownership and responsibilities for Indonesian technology businesses are handled, analyzed,
and organized "silo-style," clashes with one of the FinOps Key Takeaways that "everyone takes ownership
for their technology use." This situation hinders Indonesian technology businesses' FinOps processes from
progressing onwards from the current "Crawl, Walk, Run." FinOps Maturity Stages, where the matter of
technology-related expenses will actually have decentralized, data-driven approaches.
In comparison with developed markets, the Indonesian market poses interesting challenges. According to
the State of FinOps reports, nearly 20% of businesses have attained the “Run” level, thanks to advanced
automation and the implementation of "unit economics" processes [14]. Our own group of organizations,
on the other hand, practices reactive budgeting and optimizations for the 'low-hanging fruits' (for example,
shutting down unused virtual machines), commensurate with the "OpEx shock" of accelerated cloud
adoption prevalent in the Indonesian market [5]. Indonesian businesses are undergoing a phase where they
employ the use of cloud technology (for example, AWS Cost Explorer, Cast.ai) but have not adjusted their
business structure for managing the variability of expenses. This paper offers two important additions to
the existing knowledge base on cloud financial management. Firstly, it applies the FinOps model to the
emerging markets, addressing the existing gap that previous studies carried out in the regional arena have
overlooked, including the general financial management, which was explored, for instance, by McCoy &
Pahlavani [12]. Secondly, it verifies the use of the "Crawl, Walk, Run" model of the FinOps Framework
716 | Scientific Journal of Informatics, Vol. 12, No. 4, November 2025

Analysis. According to the findings, there exists a particular growth path of FinOps for the emerging
markets, that is, the rate optimization, which offers the initial level of growth. However, the training and
the governance, on the other hand, are deemed the lagging indicators that need substantial transformation
of the involved organizations and, accordingly, cannot be realized until that happens.
The persistence of the "technical-cultural dissonance" identified in this study, where technical optimization
scores (2.00) significantly outpace governance scores (1.29–1.53), can be attributed to three specific
constraints inherent to the Southeast Asian technology landscape. First, there are organizational restrictions.
Most of Indonesia’s technology companies are still suffering from growing structural inertia from the
previous decade of “growth-at-all-costs'' strategies. This region, as was mentioned in the first section, was
operating in a “tech winter.” But, because of the “tech winter,” this region is no longer in hyper-growth
mode and is focusing on being profitable. However, the organizational structures are still skewed towards
speed of delivery rather than cost efficiency. This situation encourages the engineering teams to deliver
features as quickly as possible and avoid cost management except as retrospective accounting. Second,
from the cultural side, there are constraints in the form of hierarchical silos. The lack of alternatives fosters
a culture of stringent centralized control decision that shaped a corporate structure in which 83% of the
participants consider there to be only one “gatekeeper” (Head of Engineering or Lead SRE) to the
possession of the cloud costs. Within the framework of Indonesian corporate culture, this constitutes a rigid
functional silo, within which the financial responsibility is perceived as the exclusive purview of the the
upper layer of management, obtrusively flattening the gradation of responsibility in the management of the
corporate data which becomes the obstacle for the democratization of data required for dispersed financing
models like showback. Regarding the lack of data and or data gaps, this is directly a function of the disparity
between the process and the tooling. Although advanced cloud platforms (i.e, AWS Cost Explorer, Cast.ai)
are readily available, there still exists a gap as there is a low friction procurement of a tool, but then, for the
governance restrictions required to implement a tool to be high friction organizational change. Therefore,
every effort is made to utilize the available tools for solving the reactive and low problem maturation “fire
drill” governance within the Operate phase. The lack of structural support for the technical adoption and
the culture change required are represented in the diagram as shown in Figure 5.
Figure 5. Conceptual framework
The present study also provides practical insight into how to handle the current tech winter and associated
pressure for profitability [21]. First, the management needs to transition from the centralized "gatekeeper"
model wherein only the Head of Engineering or CTO currently tracks the expenses to a distributed model
of ownership. On a practical level, this means building "Showback" mechanisms that provide daily cloud
cost visibility to engineering teams so that a culture of accountability can be developed. Secondly,
organizations should move beyond the reactive nature of current practices wherein budgeting is usually
informal or done rarely. While such informality might work during growth times, survival under the current
economic pressures requires an organization to formalize tagging strategies and procurement policies so
Scientific Journal of Informatics, Vol. 12, No. 4, November 2025 | 717

that spend leakage can be avoided before it actually happens [27]. Lastly, the gap in governance should be
filled with automation. Because tooling maturity scored reasonably well relative to other domains, for
example, 1.86 for P1 and 2.0 for P2, leaders need to leverage these existing platforms towards automating
governance tasks, like budget alerts, instead of relying on manual, retroactive monthly reviews.
Path toward the run stage
It requires a strategic pivot from a simple cost-control mindset to a holistic cost-optimization approach to
move from the base Crawl stage to the advanced Run stage. This evolution can only be achieved by first
establishing distributed accountability through Showback mechanisms that move beyond mere centralized
gatekeeping and expose real-time cost data, granular to the project or feature, that the organization can then
use to foster a cost-aware culture necessary for maturity. Meanwhile, to address reactive governance,
organizations should move toward formal, policy-driven automation, often called "Policy as Code." That
means replacing manual monthly reviews with automated protocols consisting of budget alerts and flagging
non-compliant resources, such as restricting the launch of untagged instances. Finally, the Run stage
requires the fundamental change in performance metrics from total cloud spend to "Unit Economics" such
as cost per transaction or user. Only this fine-grained perspective lets an organization tell good spend-
driving business growth-apart from bad spend-waste-and thus make scaling decisions based on data that is
aligned directly with business value.
Limitations and generalizability
The researchers realize that the sample size of six participants reduces the statistical generalization of
quantitative maturity scores to the whole Indonesian technology industry. In this study, however, analytical
generalization is used, meaning a goal of generalizing and extending theories-such as the FinOps "Crawl,
Walk, Run" model-rather than describing how many people or things in a population have certain
characteristics. The sample consisted of participants selected through purposive sampling, a strategy which
ensured that each respondent was at a high level of technical capability as a Cloud Infrastructure Architect
with direct responsibility for significant cloud budgets. In fact, the annual budgets ranged between $1M
and $12.5M. Therefore, although the specific maturity rating, 1.53, should be seen as indicative rather than
definitive for the whole nation, thematic patterns, such as "technical-cultural gap" and centralization of
ownership, were highly consistent across cohorts, suggesting that findings are transferable to comparable
contexts, namely technology-driven organizations in emerging markets transitioning from rapid growth to
cost efficiency.
CONCLUSION
This research investigated the adoption of the FinOps Framework in Indonesian technology organizations
and result in the average maturity score 1.53 (out of 3.00). This puts the sector in the basic "Crawl" phase.
The results reveal a clear “two-speed” adoption pattern: despite the fact that organizations are highly
skilled in technical optimization (rightsizing, rate optimization, etc.), they are severely lacking in cultural
governance characterized by centralized gatekeeping and budgetary reactive processes. In terms of theory,
the study contributes to cloud financial management literature by identifying the technological-cultural gap
in the context of emerging markets. In contrast to research in developed economies, where the process is
often linear, our research substantiates that in the context of Indonesia, the utilization of sophisticated cloud
tools happens before the establishment of sufficient financial accountability mechanisms. In addition, it
validates the applicability of the “Crawl, Walk, Run” maturity model as an appropriate diagnostic
instrument in the case of Southeast Asian markets and identifies “Rate Optimisation” as the core entry point
for local adoption.
In practice, the results are a guide to the current "tech winter" facing technology leaders. Moving from
"Crawl" to "Run" requires organizations to urgently move from the centralized gatekeeper model to
distributed ownership. This will involve rapidly putting in place "Showback" mechanisms that democratize
cost data, so governance policies can be formalized rather than relying on ad-hoc, reactive interventions.
Also, leaders are in a better position to exploit their tooling maturity to automate governance-for example,
budget alerts-rather than relying on manual oversight. The key limitation is that only six participants are
included in this study; hence, statistical generalization of the quantitative scores to the larger Indonesian
industry is limited. However, the research achieves analytical generalization through the consistency of
thematic patterns identified. The evident next step for this research is to overcome this limitation by
deploying large-scale quantitative surveys to test these maturity baselines across a stratified sample of
718 | Scientific Journal of Informatics, Vol. 12, No. 4, November 2025

industries. It would also be interesting to document, through longitudinal studies, how these levels of
maturity evolve as regional economic pressure for profitability increases.
Recommendations for future research
For future research, there are still areas that require further investigation. To add more holistic FinOps
adoption findings, future studies could involve a larger sample size involving separate businesses with a
greater depth of industry and cloud maturity adoption. In addition, applying the mixed-methods approach
used in this study extends this quantitative maturity model to a larger sample, which adds empirical
foundation to the findings.
REFERENCES
[1] F. Nwanganga, M. Saebi, G. Madey, and N. Chawla, “A Minimum-Cost Flow Model for Workload
Optimization on Cloud Infrastructure,” in IEEE International Conference on Cloud Computing,
CLOUD, IEEE Computer Society, Sep. 2017, pp. 480–487. doi: 10.1109/CLOUD.2017.68.
[2] K. M. Varma and G. B. Se, “Efficient Scalable Migrations in the Cloud,” in Proceedings - 2022
IEEE/ACIS 7th International Conference on Big Data, Cloud Computing, and Data Science, BCD
2022, Institute of Electrical and Electronics Engineers Inc., 2022, pp. 3–6. doi:
10.1109/BCD54882.2022.9900725.
[3] P. Faria, T. Simões, and Y. Qianmin, “Automation on Cloud Migrations,” in 2024 47th ICT and
Electronics Convention, MIPRO 2024 - Proceedings, Institute of Electrical and Electronics
Engineers Inc., 2024, pp. 1949–1953. doi: 10.1109/MIPRO60963.2024.10569673.
[4] C. S. Ranganathan and R. Sampathrajan, “Cloud Migration Meets Targeted Deadlines,” in 2023
4th International Conference on Electronics and Sustainable Communication Systems, ICESC
2023 - Proceedings, Institute of Electrical and Electronics Engineers Inc., 2023, pp. 672–676. doi:
10.1109/ICESC57686.2023.10193104.
[5] R. Donatello Sannino, “The impact of Cloud adoption on ICT Financial Management: how to
address emerging challenges TESI DI LAUREA MAGISTRALE IN MANAGEMENT
ENGINEERING INGEGNERIA GESTIONALE,” 2021.
[6] M. Gaianu, “On Premise Data Center vs CLOUD,” in Proceedings - 2023 International Conference
on Computational Science and Computational Intelligence, CSCI 2023, Institute of Electrical and
Electronics Engineers Inc., 2023, pp. 1068–1071. doi: 10.1109/CSCI62032.2023.00176.
[7] V. V. Sen, S. Hussein, M. R. Sumaru, S. Ali, and F. Ali, “Cloud-Based Service versus On-Premise
Services: A Comparative Study at a Local Organization in Fiji,” in Proceedings of the 2023 IEEE
Asia-Pacific Conference on Computer Science and Data Engineering, CSDE 2023, Institute of
Electrical and Electronics Engineers Inc., 2023. doi: 10.1109/CSDE59766.2023.10487723.
[8] F. Li, G. Wu, J. Lu, M. Jin, H. An, and J. Lin, “SmartCMP: A Cloud Cost Optimization Governance
Practice of Smart Cloud Management Platform,” in Proceedings - 2022 IEEE 7th International
Conference on Smart Cloud, SmartCloud 2022, Institute of Electrical and Electronics Engineers
Inc., 2022, pp. 171–176. doi: 10.1109/SmartCloud55982.2022.00034.
[9] PWC, “Technology-enabled CFO: The FinOps transformation journey,” 2025. [Online]. Available:
https://www.finops.org/framework/maturity-model/
[10] Gartner, “Gartner Forecasts Worldwide Public Cloud End-User Spending to Total $723 Billion in
2025.” Accessed: Dec. 09, 2025. [Online]. Available:
https://www.gartner.com/en/newsroom/press-releases/2024-11-19-gartner-forecasts-worldwide-
public-cloud-end-user-spending-to-total-723-billion-dollars-in-2025
[11] Kemnaker, “Satudata Kemnaker - Tenaga Kerja ter-PHK Tahun 2024.” Accessed: Dec. 09, 2025.
[Online]. Available: https://satudata.kemnaker.go.id/data/kumpulan-data/2342a
[12] A. Kautsar et al., “Technology Companies in Indonesia: How is the Financial Performance?,” in
2023 International Conference on Sustainable Islamic Business and Finance, SIBF 2023, Institute
of Electrical and Electronics Engineers Inc., 2023, pp. 154–158. doi:
10.1109/SIBF60067.2023.10379890.
[13] Bloomberg, “How Indonesian Startup Efishery’s Ex-CEO Gibran Huzaifah Faked the Numbers.”
Accessed: Dec. 09, 2025. [Online]. Available: https://www.bloomberg.com/news/features/2025-
04-15/how-indonesian-startup-efishery-s-ex-ceo-gibran-huzaifah-faked-the-numbers
[14] FinOps Foundation, “FinOps Framework Overview.” Accessed: Dec. 09, 2025. [Online].
Available: https://www.finops.org/framework/
[15] Google, “Google Trends: ‘FinOps’, ‘Cloud Cost Management’, and ‘Cloud Financial
Management’, worldwide.” Accessed: Dec. 09, 2025. [Online]. Available:
Scientific Journal of Informatics, Vol. 12, No. 4, November 2025 | 719

https://trends.google.com/trends/explore?date=2022-01-01%202025-06-
01&q=FinOps,Cloud%20Cost%20Management,Cloud%20Financial%20management&hl=en
[16] R. Katekeetta, “Optimizing IT Financial Management: Analysis of Cost Categorization and Report-
ing Practices.”
[17] N. P. A. Vo, M. Kesarwani, R. Mahindru, and C. Narayanaswami, “FinOps Agent -- A Use-Case
for IT Infrastructure and Cost Optimization,” Oct. 2025, [Online]. Available:
http://arxiv.org/abs/2510.25914
[18] B. H. Nguyen, N. Nao, and Y. Hitoshi, “Multi-Cloud Cost Management Platform with FOCUS,”
in Proceedings - 19th IEEE International Conference on Service-Oriented System Engineering,
SOSE 2025, Institute of Electrical and Electronics Engineers Inc., 2025, pp. 118–122. doi:
10.1109/SOSE67019.2025.00018.
[19] A. P. Agrawal, A. Mittal, S. Srivastava, M. Brevard, V. Moskovich, and M. Chowdhury, “INFA-
FinOps for Cloud Data Integration,” in 2024 IEEE International Conference on Big Data
(BigData), IEEE, Dec. 2024, pp. 2214–2223. doi: 10.1109/BigData62323.2024.10825704.
[20] Flexera, “2024 State of the Cloud Report.” Accessed: Dec. 09, 2025. [Online]. Available:
https://www.flexera.com/blog/finops/cloud-computing-trends-flexera-2024-state-of-the-cloud-
report/
[21] Google, Temasek, and Bahn&Company, “e-Conomy SEA 2024: Profitability on the Rise,” 2024.
[22] P. Baxter and S. Jack, “Qualitative Case Study Methodology: Study Design and Implementation
for Novice Researchers,” The Qualitative Report, Jan. 2015, doi: 10.46743/2160-3715/2008.1573.
[23] H. Kallio, A. M. Pietilä, M. Johnson, and M. Kangasniemi, “Systematic methodological review:
developing a framework for a qualitative semi-structured interview guide,” Dec. 01, 2016,
Blackwell Publishing Ltd. doi: 10.1111/jan.13031.
[24] I. Etikan, “Comparison of Convenience Sampling and Purposive Sampling,” American Journal of
Theoretical and Applied Statistics, vol. 5, no. 1, p. 1, 2016, doi: 10.11648/j.ajtas.20160501.11.
[25] D. Mileski and M. Gusev, “FinOps in Cloud-Native Near Real-Time Serverless Streaming
Solutions,” in 2023 31st Telecommunications Forum, TELFOR 2023 - Proceedings, Institute of
Electrical and Electronics Engineers Inc., 2023. doi: 10.1109/TELFOR59449.2023.10372626.
[26] V. K. Sikha and D. Siramgari, “International Journal on Recent and Innovation Trends in
Computing and Communication Finops Practice Accelerating Innovation on Public Cloud,” Finops
Practice Accelerating Innovation on Public Cloud Article in International Journal on Recent and
Innovation Trends in Computing and Communication, 2023, doi: 10.5281/zenodo.14435853.
[27] U. C. Bhookya, K. Jethuri, S. R. Ravuru, Priyadarshi, and M. Natu, “Addressing Spend Leakage
and Optimization of Cloud Costs,” in Proceedings - 2024 IEEE International Conference on Big
Data, BigData 2024, Institute of Electrical and Electronics Engineers Inc., 2024, pp. 2288–2293.
doi: 10.1109/BigData62323.2024.10825120.
[28] P. Nawrocki and M. Smendowski, “FinOps-driven optimization of cloud resource usage for high-
performance computing using machine learning,” J Comput Sci, vol. 79, Jul. 2024, doi:
10.1016/j.jocs.2024.102292.
[29] M. Kothapalli, “Cost Optimization Strategies for Cloud Infrastructure,” vol. 2, no. 1, p. 2023, 2023,
doi: 10.47363/JAICC/2023(2)329.
720 | Scientific Journal of Informatics, Vol. 12, No. 4, November 2025