# Mining for cost awareness in the infrastructure as code artifacts of cloud-based applications: An exploratory study

> **Pilar:** P2
> **Clasificación:** Declarada en la matriz
> **Evidencia de clasificación:** Fila académica del CSV titulada “Mining for cost awareness in the infrastructure as code artifacts of cloud-based applications: An exploratory study”, código P2.
> **Archivo fuente:** papers-pdf/Feitosa et al. - 2024 - Mining for cost awareness in the infrastructure as code artifacts of cloud-based applications An ex.pdf
> **Uso previsto:** Lectura personal y apoyo documental; requiere validación humana antes de incorporarse al informe.

## 1. Título

*Mining for cost awareness in the infrastructure as code artifacts of cloud-based applications: An exploratory study*.

## 2. Autor y fecha

- **Autores verificados en el PDF:** Daniel Feitosa, Matei-Tudor Penca, Massimiliano Berardi, Rares-Dorian Boza y Vasilios Andrikopoulos.
- **Fecha bibliográfica utilizada:** 2024, *Journal of Systems and Software*, 215, 112112; disponible en línea el 24 de mayo de 2024.

## 3. Problema que trata

Aunque el costo motiva la adopción cloud, faltaba evidencia empírica sistemática sobre cómo los desarrolladores manifiestan conciencia de costos durante el desarrollo y qué acciones quedan registradas en artefactos de infraestructura como código.

## 4. Qué quiere hacer

Buscar evidencia de conciencia de costos en repositorios abiertos con Terraform, identificar la información presente en commits e issues, organizarla para análisis posterior y triangular los hallazgos con discusiones de Stack Overflow.

## 5. Cómo lo hace

Examina sistemáticamente **152.735** repositorios con Terraform. Un filtrado por raíces de palabras relacionadas con costo produce 2.010 hits; los autores codifican 538 commits y 208 issues mediante codificación inductiva/deductiva, modelado de temas y construcción de un grafo de conocimiento. Luego filtran 19.139 preguntas Terraform de Stack Overflow, encuentran 491 relacionadas con costo y revisan una muestra manual (secciones 3–5).

## 6. Resultados

- En commits aparecen 14 etiquetas; “saving” es la más recurrente. Se observan acciones sobre instancias, almacenamiento, red, proveedores, políticas y alertas, no solo menciones abstractas (sección 4.1, tabla 1).
- Los 208 issues no agregan etiquetas, pero contienen más contexto sobre alternativas y razonamiento; 54 de los 89 repositorios con issues son exclusivos de ese conjunto (sección 4.2).
- El grafo organiza efectos —conciencia, aumento, ahorro—, acciones —cambiar, probar, alertar— y propiedades de despliegue (sección 4.3, figura 8).
- En Stack Overflow, 491 preguntas equivalen a aproximadamente 2,6 % de las preguntas Terraform; 451 (92 %) contienen conceptos del grafo. “change” aparece 199 veces, “provider” 189, “test” 154 e “instance” 138 (sección 5.3, figura 9).
- Los resultados son evidencia observada en artefactos seleccionados; no miden ahorro monetario ni prevalencia en todo el desarrollo cloud.

## 7. Discusión y trabajo futuro

Los autores proponen analizar contribuyentes y tipos de proyecto, correlacionar pull requests, incluir otros orquestadores y repositorios cerrados, aplicar NLP y revisar código fuente. Entre las amenazas: sesgo de GitHub/Stack Overflow, foco exclusivo en Terraform, palabras clave definidas por los investigadores, subjetividad de codificación y límites de LDA (secciones 6–7).

## 8. Conclusión del paper

Los autores concluyen que sí existe evidencia empírica de conciencia y acciones de costo en artefactos Terraform. Los commits muestran cambios concretos; los issues enriquecen el proceso de decisión; el grafo resume preocupaciones y acciones, y Stack Overflow corrobora varios puntos. Presentan el trabajo como inicio de una agenda, no como caracterización definitiva de toda la ingeniería cloud.

## Relación preliminar con INV-01

Puede apoyar la estimación temprana y el enfoque shift-left de 4.3 y 4.7, además de palancas en 3.7. Aporta evidencia de que decisiones de costo aparecen junto al IaC, pero no evalúa herramientas específicas ni demuestra causalidad o ahorro.

## Limitaciones de esta síntesis

Los porcentajes se refieren a los universos filtrados del estudio y no a todos los repositorios. El muestreo y las palabras clave condicionan lo encontrado. Esta síntesis no convierte ejemplos de desarrolladores en mejores prácticas; requiere lectura y validación humana.

## Texto extraído del PDF

> **Advertencia de conversión:** extracción textual automática de 14 páginas (114755 caracteres). Se conservaron títulos, párrafos, referencias y contenido textual por página. La disposición multicolumna, las figuras, las tablas y las ecuaciones pueden no mantener su alineación o representación visual; verifique esos elementos en el PDF original.

### Página PDF 1

The Journal of Systems and Software 215 (2024) 112112


                                                 Contents lists available at ScienceDirect

                    The Journal of Systems & Software


                                             journal homepage: www.elsevier.com/locate/jss


Mining for cost awareness in the infrastructure as code artifacts of
cloud-based applications: An exploratory study✩
Daniel Feitosa ∗, Matei-Tudor Penca, Massimiliano Berardi, Rares-Dorian Boza,
Vasilios Andrikopoulos

Bernoulli Institute for Mathematics, Computer Science and Artificial Intelligence, University of Groningen, The Netherlands


A R T I C L E   I N F O            A B S T R A C T


Keywords:                                      Context: Cloud computing’s rise as the primary platform for software development and delivery is largely
Cloud computing                                  driven by the potential cost savings. However, it is surprising that no empirical evidence has been collected
Cost awareness                                      to determine whether cost awareness permeates the development process and how it manifests in practice.
Mining software repositories                        Objective: This study aims to provide empirical evidence of cost awareness by mining open source repos-
Cloud orchestration
                                                          itories of cloud-based applications. The focus is on Infrastructure-as-Code artifacts that automate software
                                               (re)deployment on the cloud.
                                          Methods: A systematic examination of 152 735 repositories yielded 2 010 relevant hits. We then analyzed 538
                                                   relevant commits and 208 relevant issues using inductive and deductive coding and corroborated findings with
                                                   discussions from Stack Overflow.
                                                 Results: The findings indicate that developers are not only concerned with the cost of their application
                                             deployments but also take actions to reduce these costs beyond selecting cheaper cloud services. We also
                                                      identify research areas for future consideration.
                                             Conclusion: Although we focus on a particular Infrastructure-as-Code technology (Terraform), the findings can
                                            be applicable to cloud-based application development in general. The provided empirical grounding can serve
                                                developers seeking to reduce costs through service selection, resource allocation, deployment optimization,
                                          and other techniques.


1. Introduction                                            Amazon Web Services, Microsoft Azure, and Google Cloud Platform,
                                                                                collectively known as hyperscalers due to their ability to enable scaling
   Cost reduction is one of the main drivers of cloud adoption (An-     to virtually infinite levels of demand, allow these providers to offer
drikopoulos et al., 2013). Cost savings for the cloud consumers accrue     access to these resources for almost (always) declining prices (Harms
due to two phenomena. First, access to any kind of computational    and Yamartino, 2010). This makes cloud computing very attractive to
resources (both hardware and software) is on-demand and is being      all kinds and sizes of organizations and enterprises.
billed utilities-style (Mell et al., 2011). This means that scaling up and        Further testimony to the importance of cost for adopters of cloud
down the amount of these resources to meet the needs of the current    computing is the amount of related work on areas investigating how to
load leads to higher efficiency in comparison with a fixed infrastructure    minimize and/or manage this cost. This can be achieved, for example,
such as e.g. in a traditional data center. Compounding this, there is                                                                from the perspective of cloud consumers through optimal cloud service
also no need for upfront capital expenses for the acquisition of these                                                                        provider selection (Tricomi et al., 2020; Hosseinzadeh et al., 2020),
resources, e.g. to cope with unforeseen demand. This means a nearly                                                              and from the perspective of the providers by means of optimized task
complete transfer of the focus from the management of capital expenses
                                                                       scheduling (Arunarani et al., 2019) or other profit optimization tech-
to operational ones, also known as the CAPEX-to-OPEX shift (Armbrust
                                                                      niques such as energy consumption minimization (Cong et al., 2020).
et al., 2010). Second, and on top of that, the economies of scale realized
                                                             Whats more, every cloud service provider offers in one form or another
by the cloud service providers, and especially by the ones such as


 ✩Editor: Shane McIntosh.
  ∗Corresponding author.
     E-mail addresses:  d.feitosa@rug.nl (D. Feitosa), matei.penca1@gmail.com (M.-T. Penca), massimiliano.berardi93@gmail.com (M. Berardi),
raresboza@gmail.com (R.-D. Boza), v.andrikopoulos@rug.nl (V. Andrikopoulos).
    URLs:  https://feitosa-daniel.github.io (D. Feitosa), https://vandriko.github.io (V. Andrikopoulos).

https://doi.org/10.1016/j.jss.2024.112112
Received 18 December 2023; Received in revised form 10 April 2024; Accepted 22 May 2024
Available online 24 May 2024
0164-1212/© 2024 The Authors. Published by Elsevier Inc. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).

### Página PDF 2

D. Feitosa et al.                                                                                                   The Journal of Systems & Software 215 (2024) 112112

cost calculator tools, allowing their users to get a quote on their service     identified related topics are discussed on a popular developer forum,
consumption based on their foreseen computational, storage, network     Stack Overflow,1 in relation to the same type of artifacts. The analysis
etc. needs. Consulting on cloud cost management has developed into     of the involved posts confirms the fitness of our result to purpose. The
its own line of business, with even cloud service providers themselves     contributions of this work can therefore be summarized as follows:
offering such services to their users. In all cases, cost is referring to the
                                                                                                                      • we collect and present empirical evidence of the existence of cost-
monetary expenses of hosting and running software in one of the cloud
                                                                                  related information pertinent to Terraform artifacts as it appears
deployment models as defined by NIST (Mell et al., 2011).
                                                                                   in (open) source code repositories;
   However, and to the extent of our knowledge, no empirical evidence
                                                                                                                      • we triangulate and augment this information extraction by iden-
exists on whether and in what form the cost of cloud-based software
                                                                                        tifying Stack Overflow posts where pertinent discussions take
projects  is discussed among the involved developers. While on the                                                                                    place;
surface such concerns appear to be outside of the remit of software                                                                                                                      • we make publicly available a curated dataset  of the artifacts
development per se, the situation in practice is quite different. The fact,                                                                                     identified through this evidence-collection process and the scripts
for example, that the DevOps paradigm became popular and widely                                                         we used during the data collection, see Feitosa et al. (2024);
adopted almost in the same timeframe as cloud computing hints that                                                                                                                      • we define a set of actionable items for future research on cost
software developers cannot easily ignore the operational aspects of the                                                                             awareness based on our preliminary analysis of this dataset.
code they produce, including its cost. Furthermore, the aforementioned
utilities-like billing of cloud services means that developers are now       The rest of this paper is structured as follows. Some related works
in a position to be held effectively accountable for the generated     are presented in Section Section 2. Section 3 discusses the study design,
revenue of the software that they produced, deployed, and ran on the     including the definition of research questions to investigate. Section 4
cloud infrastructure. As such, and further bolstered by the amount of     presents our findings, and Section 5 discusses our effort to triangulate
anecdotal evidence, we do expect software developers to be actively    them through developers’ interactions on a public forum. Section 6
aware and concerned about the cost of their software, and we set out     offers a discussion on the implications of these findings for practitioners
                                                              and researchers, including the formulation of a research agenda forto collect evidence of this.
                                                                           future work. Finally, Sections 7 and 8 close this paper with a reflection   The objective of this study is therefore clear: to examine to what
                                                             on the threats to validity to this study, and a summary of its mainextent software developers are aware of the cost of deploying and operating
                                                                               findings, respectively.
cloud-based software, and what kind of concerns and action initiatives they
are having about  it. We choose MSR (Mining Software Repositories)
                                                                           2. Related work
as the means to answer this question empirically. Among its other
uses, MSR allows to empirically study otherwise subjective or external                                                                  As mentioned in the previous section, and to the best of our knowl-
phenomena in combination with (or through) large-scale systematic                                                                        edge, there is no existing study gathering empirical evidence about how
mining of development artifacts. Fields such as green software engi-     developers deal with the cost of deploying cloud-based or otherwise
neering (Hindle, 2013; Pereira et al., 2021), risk assessment (Choetkier-     software, and definitely none collected through repository mining. The
tikul et al., 2015; da Costa et al., 2017; Choetkiertikul et al., 2018),     closest works in spirit in this direction are instead studies on mining
and software classification (Howard et al., 2013; LeClair et al., 2018;     energy consumption awareness on the developer’s side such as the
Sas and Capiluppi, 2022) have advanced noticeably due to MSR. In    work by Moura et al. (2015) and Bao et al. (2016). Other works such
a similar fashion to these works, we hypothesize that the amount     as the one by Pinto et al. (2014) on the same topic, or Das et al.
and diversity of costs-related information in cloud-based software project    (2016) analyzing documented performance-related issues can be also
repositories is sufficient to produce meaningful insights.                      considered somewhat related to ours.
   Cloud-based application development, however, covers a very wide       However, that is not to say that there are no research efforts for
range of application types and development activities, and this creates     supporting the management of cost in such systems. In fact, that is
a question of scope in this study. Selecting for a specific programming    a flourishing line of research approached from different perspectives.
language or ecosystem as in other MSR studies does not produce     Despite being recognized early on as a major concern when migrat-
meaningful results here since these are orthogonal concerns to the     ing existing systems to the cloud (Andrikopoulos et  al., 2013), for
use of cloud infrastructures. Instead, we scope our search for evidence     example, and being a crucial component in many migration support
to cloud orchestrator artifacts included in open source projects. Cloud    approaches (Jamshidi et al., 2013), estimating the cost of deploying
orchestrators are Infrastructure as Code (IaC) solutions that provide    and running software in the cloud remains an open research chal-
an abstraction layer over the self-service management APIs of the     lenge (Shuaib et al., 2019). Cost of deployment and operation of target
various cloud service providers, with the intention of flattening out     applications is one of the common factors taken into consideration
the differences between them (de Carvalho and de Araujo, 2020). This     in works researching mechanisms for efficient decision making on
                                                               which cloud service provider(s) to use (Hosseinzadeh et al., 2020).is usually achieved by means of descriptor files, i.e., configuration files
                                                                        This also appears to be the case for the related problem of optimizingthat when interpreted by the orchestrator ensure that both the under-
                                                                        the selection of services from potentially across service providers, com-lying infrastructure is made available, and the tasks required for the
                                                             monly known as cloud service composition (Amato and Venticinque,(re)deployment of software on this infrastructure is executed correctly.
                                                                   2016; Vakili and Navimipour, 2017). Managing the cost (and energy
Descriptor files are usually semi-structured documents in a machine-
                                                                   consumption) is also identified as one of the focus points of architecting
readable format that is easy to process such as YAML or JSON, and
                                                                      cloud-based software as discussed in the survey of Chauhan et  al.
like any other configuration files they are added to code repositories to
                                                                   (2017) on the topic.
be managed by the respective version control system. Orchestrators are
either (cloud service) provider-specific, such as Amazon Web Services                                                                           3. Study design
CloudFormation, or provider-agnostic, such as Terraform, Cloudify,
Apache Heat, and others as discussed for example in Tomarchio et al.        In this section, we elaborate on the methods employed to achieve
(2020). For reasons that will be discussed in Section 3, we focus our     the objective presented in Section 1. In particular, we discuss the
work specifically on Terraform artifacts.                                 derived research questions, the required data and its collection, and
   In summary, this paper aims to report on the first work that at-    how the data is analyzed to provide the necessary answers.
tempts to perform cost awareness mining for cloud-based application
development, starting with IaC artifacts. In addition, we fortify the
findings of the mining process by also investigating to what extent the         1 https://stackoverflow.com/

                                                                        2

### Página PDF 3

D. Feitosa et al.                                                                                                   The Journal of Systems & Software 215 (2024) 112112

3.1. Research questions                                   We clarify that there are other viable options, Cloudify3 being
                                                                  a well known one, marginally behind Terraform in terms of perfor-
   To explore developers’ cost awareness and how  it manifests in    mance (Kovács and Kacsuk, 2017). Hyperscalers are also offering their
project repositories, we define three main questions:                own IaC solutions, with AWS’ CloudFormation being a particularly
                                                                     popular one. In principle, therefore, we could execute this study with
RQ1 What kind of relevant information can we extract from commits      artifacts of multiple cloud orchestrators taken into account. However,
      on IaC artifacts?                                                  the complexity of analyzing multiple platforms was deemed prohibitive
                                                                            since this kind of study is a resource-demanding endeavor as-is. More-
RQ2 How can we augment this information further based on issues     over, we found the number of projects on GitHub mentioning Cloudify
       raised in the respective repositories?                            (876 repositories with around 79K commits) to be significantly fewer
                                                                    than that of projects mentioning Terraform (171K with around 1M
RQ3 How can we organize this information so we can gain deeper     commits). Cloudify has some of  its features locked behind a pay-
       insights from it?                                                 wall (Kovács and Kacsuk, 2017), potentially turning away many small
                                                                    time and open-source developers, which might explain this difference
   In absence of any prior study establishing a link between activities     in numbers. Furthermore, provider-specific cloud orchestrators would
in repositories and cost awareness, we define these questions on a    need a deeper understanding on our part of the cloud services being
purely exploratory base. We strive to find information related to actions    used which would detract from the focus of the study. Nevertheless,
taken on cloud-based software projects on the basis of impacting their    we acknowledge the relevance of investigating other platforms in future
deployment cost. In an initial exploration, we seek stronger evidence    work (see Section 6).
of such actions and, thus, focus on changes to code connected with        In summary, the cases under consideration for this study comprise
acknowledged impact to cost by means of commit messages (RQ1).     GitHub projects that use Terraform as their cloud orchestrator, and address
Next, we expand the search scope for discussions that may not incur     matters related to cost in commit messages and issues discussions. In the
in changes but that are relevant nevertheless (RQ2). In the case of     following we describe how we actually apply the latter criterion.
this study, we explore entries in the issue trackers of projects that
were identified in the previous research question. At this phase,  it     3.3. Data collection and analysis
is also relevant to understand how the topics of discussion differ
(if at  all) compared to the information on commit messages. This        Following best practices in evidence-based software engineering
information can guide future research and development efforts (see    (Wohlin et al., 2012), we characterize the population of this study in
Section 6).                                                           terms of unit of analysis. The units of this study are commits or issues
   The information collected in the previous RQs can inform future     in repositories that contain evidence of cloud cost awareness. For each
research and practitioner decisions. However, this ‘rawer’ format of     valid unit, we extract the triplet <unit-id;unit-content;label>,
the data may often require examining the dataset in more depth to    where: (a) unit-id refers to the repository and commit hash or issue
make connections between the identified core concepts and more in-      id, (b) unit-content is the commit message or issue text, and (c)
formed decisions. Thus, it is instrumental to understand how the knowl-    label is a descriptor highlighting the main theme(s) derived from
edge evolving from the information extracted in the previous research    unit-content.
questions can be structured for this purpose (RQ3).                      The process to extract and analyze the units is summarized in Fig. 1.
                                                                       Locating Terraform descriptor files is relatively straightforward since
3.2. Case selection                                                     they are by default written in the HashiCorp Configuration Language
                                                                     (HCL), a language that is indexed by GitHub, and carry the .tf or
   As with previous studies on mining software repositories, we direct    .tf.json extension as per the Terraform documentation.4 Further-
our efforts to open source repositories. The reasoning here is that using    more, Terraform’s first release was in 2014, allowing us to constrain
such an open collection of repositories minimizes the selection bias on    our search further for repositories after this date. To automate the
our side and therefore increases the robustness of our possible findings.     interaction with GitHub’s API, we use PyGitHub.5 Therefore we set
Among other qualities, we seek a source that can provide a sizable    PyGitHub to search, on a day-to-day basis,6 until the end of May 2022
and diverse population. Also, from a population that meets the quality    (when the data collection for this study took place), for repositories that
criteria, we must find the breadth and depth of the data that one can     contain HCL files created after 2014. The search returns a candidate
derive. As a source of repositories, we choose GitHub mainly due to     set of 156 585 repository links. Removing repositories from this set that
the volume and diversity of software projects that are available in it.    do not include .tf or .tf.json files reduces this set to 152 735
Moreover, we aim at maximizing the data pool while maintaining a     repositories for further consideration.
systematic and repeatable approach and, therefore, GitHub’s search     We then use a  list of keyword stems to match against commit
features and API are instrumental.                                    messages and further search in this set for cost-awareness. However,
  We also already put forward in the introductory section our par-       it is worth noticing that since there are no previous works on the same
ticular interest in investigating projects that use cloud orchestrators.     topic we cannot reuse their keywords list and we have to come up with
Since we seek to identify evidence of developers’ discussions over cloud    our own. After some piloting, and considering the research questions
infrastructure matters (in this case, cost), it is natural to narrow down    we aim to answer, we decide on the following keyword stems,7 (in
our search scope to projects that use IaC. The commit messages and     alphabetical order):
issues involving descriptor files have the potential to bring up concerns
                                                              bill, cheap, cost, efficient, expens, and pay.
we are interested in. For the purposes of this study, we choose to work
with Terraform2 as it is one of the most notable and widely adopted
orchestrators (de Carvalho and de Araujo, 2020). Terraform is known         3                                                                                         https://cloudify.co/
for providing an open-source version, cloud services compatibility,         4                                                                                     https://www.terraform.io/language/files
interface accessibility and mature API (de Carvalho and de Araujo,         5 https://pygithub.readthedocs.io/
2020).                                                                                          6 This was done to avoid the limitations in the amount of results by the
                                                                      GitHub API per request.
                                                                                                   7 Treating them as stems means that expens for example will match
   2 https://www.terraform.io/                                                    against expense expenses, inexpensive, and inexpensively.

                                                                        3

### Página PDF 4

D. Feitosa et al.                                                                                                   The Journal of Systems & Software 215 (2024) 112112


                                                                     Fig. 1. Steps of data collection and analysis.


                                                                Fig. 2. RQ1 repository demographics (90th percentile).


   Using this list, we instruct PyDriller (Spadini et al., 2018) to process        In Fig. 2, we characterize the repositories in terms of IaC ar-
all commit messages in the candidate repositories for the presence of      tifacts’ size (iac-sloc, max. 89K), source code size (sloc, max.
one or more these keywords and we output the repository name, com-     1 210K), number of commits (#commits, max. 17K), contributors
mit hash and message. PyDriller is a Python library used for analyzing    (#contributors,  max.  596),  number  of  Terraform  modules
Git repositories. We chose this tool for its easy-to-use API and broad    (#tfmodules, max. 1.4K), resources (#tfresources, max. 2.5K),
adoption by the MSR community, which we interpret as an additional     variables (#tfvariables, max.  5K),  subnets-related  definitions
sign of quality.                                              (#tfsubnets,    max.     32),     instances-related     definitions
   After this step, a much more manageable set of 2 010 repositories    (#tfinstances, max. 36), and number of Terraform clusters-related
containing 6 116 potentially related commits is identified as a result.     definitions (#tfclusters, max. 21). The max values are not visible
This set of commits and their respective repositories serve as input to     in Fig. 2 since we needed to trim the top 10% values of each variable to
collect the data and perform the analysis for each research question.       better visualize the plot. We also note that 65% (284) of the population
                                                                   comprise repositories that contain (and manage) IaC artifacts only
3.3.1. RQ1                                                                                       (i.e., they do not contain source code). These characteristics suggest
   To answer the first research question, we must identify what kind     that the population is varied with a tendency for repositories main-
of information related to cloud cost management can be extracted from     tained by few contributors and concentrated in repositories of more
the commits. Out of this set of 6116 commits, 377 are from forked     Terraform and other IaC files than source code. This is possibly an
repositories already in the set. After filtering out these commits and     indication of developers taking over a ‘‘Terraform expert’’ role in teams
those that do not modify any Terraform files, we are left with 1162     that become responsible also with dealing with the operational cost
repositories and 2045 related commits. The selected commits are then     aspect of each project.
inspected manually to decide their actual relevance. For that, each     We then proceed to collect what kind of information related to
commit message is checked by two researchers and validated by a     cloud cost management can be extracted from these commits. This
third one. Any conflicts are resolved by the entire team in consolida-      is primarily a manual task, to be performed using open coding, a
tion meetings. The output of this process results in the identification    form of inductive coding (Corbin and Strauss, 2014). For this task,
of 538 relevant commits. The selected units come from 434 distinct    each data point (for this RQ, commit message)  is labeled  first by
repositories.                                                   two researchers and validated by a third. The labels refer to central

                                                                        4

### Página PDF 5

D. Feitosa et al.                                                                                                   The Journal of Systems & Software 215 (2024) 112112

ideas in the discussion and their characteristics. Any conflicts (incl.     core concepts. This process is done in two steps, starting with topic
disagreements) are resolved by all five researchers in a consolidation    modeling (Blei, 2010) and followed by a second coding activity, culmi-
meeting. In this meeting, we verify the rationale for the codes and     nating in the creation of a knowledge graph which combines the results
analyzed the evidence again (i.e., the complete commit message), and     of the previous steps. We describe these steps in the following.
argued to a consensus. We did not have cases where a consensus was        Topic modeling  is a  statistical learning tool that  is well-suited
not met after this process.                                                     for abstracting connections between words (into topics) from a cor-
   As it will be discussed further in Section 4, all collected units are    pus of documents (Blei, 2010). We apply Latent Dirichlet Allocation
analyzed to identify relevant characteristics such as the prevalence of    (LDA) (Blei, 2010), a popular topic-modeling technique used in a
the various labels and distribution of the units among repositories. In    number of MSR studies e.g. Zimmerle et al. (2022), Al Alamin et al.
addition, meta-information such as the unit-id is used to analyze the     (2021), Chen et al. (2012), Hindle et al. (2011).
repositories, e.g., regarding the number of source lines of code (SLOC)        Before applying LDA, a number of steps must be undertaken for
and number of contributors.                                             cleaning and preparing the corpus. GitHub content contains a mixture
                                                                              of Markdown and HTML code scattered throughout the text that we
3.3.2. RQ2                                                         mined. Thus, we first convert any markdown syntax to HTML, remove
   For the second research question, we wish to explore what kind of     the content in pre, code and blockquote elements, and remove the
additional information related to cloud cost awareness can be extracted    markup and URLs. We note that we remove code snippets because we
from entries in issue trackers that adds to that extracted from commit     are interested in developers’ discussions and the code may bias the
messages. As shown in Fig. 1, we start from the list of 1339 repositories    LDA to find irrelevant topics. Next, we prepare each document using
obtained from the first filtering of commits based on keyword. We     Stanza’s (Qi et al., 2020) neural network NLP pipeline.8 In particular,
use this list because discussion may take place before actual changes    we tokenize it into sentences containing lists of tokens, extract part-of-
happen (as demonstrated by modification to Terraform files), and we     speech (PoS) tags of each token, and lemmatize them. The latter step is
would like to capture them too. Also, this set of repositories allows us     especially relevant to improve the validity of the bag of words used for
to narrow down the population to an amount of issues that we can     topic modeling. From the prepared tokens, we filter the PoS tags that
feasibly extract from GitHub since they already contain some evidence    may contain relevant words, i.e., nouns, adjectives, adverbs and verbs.
that cost may be a concern for the project.                     We also remove tokens according to a stop-word list that we built by
                                                                 merging the Gensim’s (Řehůřek and Sojka, 2010) list for English with   To extract the issues, we provide GrimoreLab’s Perceval (Dueñas
                                                                    terms deemed irrelevant for our analysis. We perform the same stepset al., 2018) with the repository owner username, the repository name,
                                                                                for both commits’ and issues’ text.and a GitHub API token. Perceval is a Python-based tool that can collect
                                                                  With the prepared corpus, we use Gensim to convert it into a bagdata from various sources, including issue trackers. We chose Perceval
                                                                              of words, build a TF-IDF (term frequency–inverse document frequency)for its versatility and validation within the MSR community. The tool
                                                             model and use the two to create LDA models. To build an LDA model,then returns us a list of issue objects that contain every single detail
                                                     we must find a suitable number of topics (𝐾), as it impacts the gran-pertaining the issue. We then extract the issue objects that contain
                                                                                ularity of the results (Abdellatif et al., 2020; Han et al., 2020). Theone or more of the defined keywords in the title, body or any of the
                                                                            quality of the model is also affected by other hyperparameters, such ascomments; this results in an initial set of 862 entries.
                                                                         𝛼(referring to document-topic density) and 𝛽9 (referring to topic-word
   Next, we apply a process similar to that described for RQ1 to
                                                                            density) are some of the most relevant (Campbell et al., 2015; Treudefilter for relevant issues and then label them. Since issues may con-
                                                              and Wagner, 2019). Following the related literature (Reboucas et al.,tain long discussions, the coding is focused on the context, i.e., the
                                                                   2016; Al Alamin et al., 2021; Zimmerle et al., 2022), we experimented
sentence where the keyword appears and the surrounding ones (when
                                                                    with the ranges 𝐾= {5, 6, … , 34, 35}, 𝛼= 𝛽= {50∕𝐾, 0.01}. We also
needed).  If multiple keywords appear on the same issue and they
                                                                         varied the chuncksize (number of documents for each training mini-
refer to different contexts, multiple checks are performed. We note
                                                                             batch)10 𝑆= {1, 2, 4, 8, … , 1024} as it can yield positive impact on the
that the labels are applied to whole issues based on evidence found
                                                             model (Hoffman et al., 2010). Although the quality of the model is
in any of the content elements (i.e., title, body or comments). This
                                                                           ultimately assessed by us, we relied on the coherence (Abdellatif et al.,
process culminates in the selection of 208 units belonging to 89 distinct
                                                                   2020; Al Alamin et al., 2021) and perplexity (Treude and Wagner,
repositories. In Fig. 3, we characterize the repositories in terms of the
                                                                   2019; Zimmerle et al., 2022) metrics to narrow down the number of
same metrics as in Fig. 2: iac-sloc (max. 43K), sloc (max. 1 486K),
                                                                      candidate models to be manually inspected. Finally, we train models
#commits (max. 6K), #contributors, (max. 156), #tfmodules
                                                                       using 100 iterations for hyperparameter exploration, and use 1000
(max. 373K), #tfresources (max. 646K), #tfvariables (max.
                                                                                 iterations to train the models selected for manual inspection. After this
3.5K), #tfsubnets, (max.  39), #tfinstances (max.  34), and
                                                                             process, we settled with 𝐾= 12, 𝛼= 50∕𝐾, 𝛽= 0.01, and 𝑆= 32 for
#tfclusters, max. 27). We again trimmed the top 10% values of
                                                                        the model based on the commits dataset model; and 𝐾= 5, 𝛼= 0.01,
each variable to better visualize the plot. This population of repositories
                                            𝛽= 50∕𝐾, and 𝑆= 2 for the model based on the issues dataset.
is considerably smaller than that collected for RQ1, and contains a
                                                                           Next, we aim to build a knowledge graph by making informed
lower amount of projects that contain (and manage) Terraform files
                                                                       connections between relevant words. The set words come from both the
(only 44%). Nevertheless, the descriptive  statistics summarized by
                                                                    coding performed for RQ1 and RQ2 as well as from the interpretation ofFig. 3 suggest a fair distribution of data points, with higher averages
                                                                        the topics of both models. To interpret the topics, we used the open card
(by approx. a factor of two).
                                                                             sorting technique (Abdellatif et al., 2020; Zimmerle et al., 2022) and
   Similar to RQ1, the collected units are analyzed to identify rele-                                                                     analyzed the top words of a topic via a random sample of documents
vant characteristics such as the prevalence of the various labels and
                                                                dominated by  it (Ahmed and Bagherzadeh, 2018). The sample size
distribution of the units among repositories. Moreover, the results are
                                                                         varied from 10 to 20 documents per topic, depending on the number
compared to those obtained from RQ1, to reflect on the value added                                                                              of documents connected to a given topic (we aimed for 5%–10% of
by exploring issues. Both of these issues are to be discussed further in
                                                                        the number of documents connected to the topic). Three researchers
Section 4.

3.3.3. RQ3                                                                                     8 https://stanfordnlp.github.io/stanza/pipeline.html
   In the final research question, we want to examine the dataset in         9 In Gensim, the parameter ‘eta’ refers to 𝛽.
more depth and make contextual connections between the identified        10 https://radimrehurek.com/gensim/models/ldamodel.html

                                                                        5

### Página PDF 6

D. Feitosa et al.                                                                                                   The Journal of Systems & Software 215 (2024) 112112


                                                                Fig. 3. RQ2 repository demographics (90th percentile).


                                                        Removed the default use of detailed monitoring.
                                                        (#17) * Reduces CloudWatch costs for metrics by
                                                        80%
                                                                                        blinkist/terraform-aws-airship-ecs-cluster     (commit     hash:
                                                                   d7aa6599)


                                                                           This example showcases the fact that monitoring solutions provided
                                                              by the cloud service providers might offer deep insights into the billing
                                                                              of their services, but are also incurring expenses for their usage, as with
                                                               any other cloud service. This being the most common label indicates
                                                                      not only awareness on behalf of the developers, but also specific
                                                                             cost reducing actions as an effect of this awareness. As a matter of
                                                                                        fact, approximately 70% of all commits as shown in Fig. 4 document
                                                                        concrete actions to save cost. Characterizing the types of actions taken
                       Fig. 4. Coding demographics of commits.                             is outside of the scope of this work, but can be easily achieved by
                                                                             further processing the commits in the dataset.
                                                                The next most popular label is awareness, which does also imply
                                                                               action, e.g.:

applied the technique, with the other two researchers validating the       nat gateway is verry [sic] expensive
results and resolving disagreements. Finally, the relationship between          stealthHat/k8s-terraform (hash: 681a3f8b)
words is defined by applying axial coding and selective coding (Corbin
and Strauss, 2014) on the preexisting labels (from RQ1 and RQ2)
                                                                           This particular example identifies a well known issue with Amazon
and words from topics. Axial coding is a combination of inductive
                                                   Web Services’ NAT Gateway service with respect to cost accruing easily
and deductive coding with the goal of relating codes (e.g., finding
                                                                      out of control that is even the subject of online memes and frequently
emerging categories). Selective coding is a similar process, but to find
                                                                          recurring Twitter threads.11
the core set of codes and categories. Group categories and relationship
                                                                                     Finally, the label instance understandably figures among the top
between labels can be identified from a topic (if a word can describe
                                                                          recurring labels. An example from the dataset is:
the topic well) and from manual inspection of labels and their linked
documents.
                                                        Move from m4.large to m5.large. The new gen have
                                                        more CPU and are cheaper
4. Results                                                                           alphagov/govuk-aws (hash: 6cfda6ad)

   The  presentation  of  the  results  follows  the RQs  defined  in
                                                                               In this respect, this label can be located anywhere between the
Section 3.
                                                                       previous two ones: it can identify awareness and intention of action at
                                                                        the same time. On a related note, it is worth pointing out that, although
4.1. Cost Awareness in Commits (RQ1 )                                          less prevalent, we also identified information explicitly discussing cost
                                                                            increases due to a prior change (in roughly 2% of the units).
   As a result of the coding process, we obtain a set of 14 distinct        Altogether, we notice developers’ consciousness of consequences
labels related to the 538 commits. Each commit has between one and     of decisions in deployment. Moreover, labels such as instance and
five labels assigned to it based on the message content. Fig. 4 lists the    storage point to specific aspects of the deployment that are or can
collected labels, and shows their recurrence among units (i.e., commits)    be tuned to manage cost. From Fig. 4, we cannot infer or speculate
and distinct repositories, and number of distinct contributors associated     over which of such aspects are more often treated this way. However,
with them. We provide a description of each label in Table 1 and     considering the configuration options offered by platforms such as
elaborate on the most recurrent ones in the following.
   The most popular label by  all metrics  is saving. A notorious
example from the dataset is:                                                              11 See e.g. https://twitter.com/quinnypig/status/1440301033314349062

                                                                        6

### Página PDF 7

D. Feitosa et al.                                                                                                   The Journal of Systems & Software 215 (2024) 112112


                Table 1
                 Label descriptions.

                   Label                                Description

                      alert                                    text expressing concerns related to billing alarms enforcing an upper threshold on costs.
                   area                                    text expressing concerns related to server or instance geographical location.
                  awareness                              text simply mentioning concerns with cost (without necessarily implying action).
                   billing_mode                           text expressing concerns related to the type of billing plan being used (e.g., on-demand for
                                                  development or normal plan for production).
                     cluster                                 text expressing concerns related to cluster configuration.
                domain                                text expressing concerns related to domain name system and IP addresses.
                    feature                                 text expressing concerns related to various features such as logging, load balancers or usage of third
                                                       party libraries.
                    increase                                text expressing concerns related to increase in cost due to a change.
                   instance                                text expressing concerns related to computational instances (e.g., Amazon AWS t2.micro) used in the
                                                    deployment.
                  networking                            text expressing concerns related to networking configuration.
                    policy                                  text expressing concerns related to the implementation of general rules to prevent excessive charges.
                   provider                               text expressing concerns related to choosing a service providers (e.g., Amazon, Azure, Google).
                   saving                             denotes mentioned changes made to save costs.
                   storage                                 text expressing concerns related to storage solutions (e.g., Amazon gp2) used in the deployment.


Terraform, the data suggest a broad understanding of these options. At
the same time, the number of repositories in our dataset compared to
the total amount of projects using Terraform may also suggest that only
a small percentage of developers are interested or aware of the cost-
saving possibilities in IaC configuration. We note that this observation
is also speculative as it requires further investigation to e.g. discard test
or template projects. Further insights can be gained by analyzing the
dataset in more depth for e.g. characterizing the types of repositories
with respect to the labels used in their commits, identifying the relation
between labels and contributors and so on. This kind of analysis is
left as future work and as part of a call to the wider community, as
discussed below in Section 6.


4.2. Cost Awareness in Issues (RQ2 )
                                                                                                                        Fig. 5. Coding demographics of issues.

   The coding of the 208 issues resulted in recognizing labels we
identified in the commit-units of analysis, without adding new ones. We
note that one label, namely policy, was not identified among issues.       But the LBs (HTTP(s) and TCP) do not work because
Each issue discussion has between one and four labels assigned to it       they only have the default/main worker pool as
based on the text in the title, body and comments. Fig. 5 describe the       target pool, and in my setup its size is 0. So I am
labels in terms of their recurrence among units (i.e., issues) and distinct       kinda paying for Global FW rules that have no use
repositories, and number of distinct creators and commenters.            and I cannot delete them because they will get
   At a first glance, we notice considerable similarity between Figs. 4       created again in the next ‘terraform apply‘.
and 5. We explored this observation further by inspecting the con-         poseidon/typhoon (issue: #558)           label: networking
tent of a random sample of units from both datasets that are tagged
with the same label. For that, we selected 50 commits and 20 issues,        Thus, while commit messages are commonly more compact and may
i.e. aiming for a representativeness of 10%. In general, we notice     report cost-changing actions, issues may shed light on the decision-
that issues contain more information around the cost-related matter    making process that developers undergo before applying a cost-affecting
at hand, which is expected since they essentially provide a discussion     change. An example of this contrast can be seen in the following units
forum. More importantly, we found the extra amount of information    both labeled as instance:
to be often related to decision-making around the cost matter. Actors
may present hints on the current configuration of the deployment,       Change  code  to  use  the  cheaper  r4.xlarge
the alternatives for change, the rationale and even potential feature       instances type.
requests. For example, see the following two samples from differ-         cisagov/cyhy_amis (hash: 4e67a501)
ent issues showing the depth of information that can be potentially
extracted:
                                                        It would be really great if the new ‘t4g‘
   By  having  a  personal  deployment,  we  are          instance,  which  are  even  cheaper  than
   free to experiment and research without any          ‘t3.nano‘, would be supported as well
   limitation. The drawback is that it implies a             Guimove/terraform-aws-bastion (issue: #124)
   cost for the cloud provider. Alternatively,
   we  could  imagine  a  ‘sandbox.qhub.dev‘  or
                                                                    While the commit message communicates the change for a cheaper
   ‘alpha.qhub.dev‘ or whatever
                                                                             instance, the issue hints on the current configuration and expresses
    Quansight/qhub (issues: #924)              label: provider
                                                                        the wish for a new feature (i.e., support of a different instance). We
                                                                      note that this example regards different repositories. We tried to find

                                                                        7

### Página PDF 8

D. Feitosa et al.                                                                                                   The Journal of Systems & Software 215 (2024) 112112

                                                     now take a step back to collect more relevant labels and establish
                                                                       connections between them. As described in Section 3.3.3, we started
                                                              by modeling topics from our dataset, and then proceed to perform axial
                                                              and selective coding based on the topics and the labels identified in our
                                                                               dataset.
                                                                     During the investigation of RQ2, we established that the text in both
                                                            commit messages and issues’ content is varied but complementary in
                                                                           nature. So we aimed to create one model per set of units to avoid the
                                                                                   risk of not identifying relevant topics. As a result of our topic mod-
                                                                                  eling, we identified 12 topics from commit units and five topics from
                                                                              issue units. The used hyperparameter configurations (see Section 3.3.3)
                                                                         yielded the most promising results, but not all topics were useful for our
                                                                         purposes.
                                                                               In particular, only one topic derived from issues was considered.
                Fig. 6. Coding demographics of the combined dataset.              The relevant topics mention cost-related terms (e.g., ‘cheap’, ‘expen-
                                                                                          sive’, ‘budget’, ‘waste’) and actions (e.g., ‘change’, ‘move’, ‘add’, ‘test’,
                                                                           ‘upgrade’) associated with various properties of the deployment, both
connections between commits and issues but our dataset does not     general (e.g., ‘VM’, ‘storage’, ‘disk’, ‘machine’) and specific (e.g., ‘dy-
contain any direct links to issue in commit messages. An alternative    namodb’, ‘CPU’, ‘NAT’, ‘EC2’, ‘RAM’). Some of the connections revealed
to explore this avenue is to study pull requests, which is outside of our    through the topics are already observable in our coding for RQ1 and
scope but mentioned in our research agenda (see Section 6).            RQ2, in the form of co-occurring labels as summarized by Fig. 7. The
   Continuing with the analysis, we notice some changes in the order     figure presents these co-occurrence relationships as an UpSet plot (Lex
of the labels in terms of recurrence. Fig. 6 shows a comparison of the                                                                                 et al., 2014). The labels (with their frequencies) are shown as rows
two sets of units and helps to visualize their differences. awareness    on the bottom part, and the frequency of the various combinations of
is more recurrent than saving among issues, which might be related                                                                                labels are represented as columns on the top part and described through
to our observation that issues can be a more prominent platform for
                                                                        the connected dots on the bottom part.
decision-making. On a similar note, units labeled with increase are
                                                  We then applied axial and selective coding to aggregate terms (from
also more recurrent among issues (compared to commit units). This
                                                                              topics and labels) and inspect the relationships in the units. At the end
might also be in line with the nature of issues, in this case, reporting
                                                                              of this process, we created the knowledge graph depicted in Fig. 8.or acknowledging cost increase. The example below depicts a situation
                                                             The graph compiles three main levels of information: effects on cost,of a seemingly unintentional increase.
                                                                            actions related to an effect, and the properties of the deployment that
   Pods for some core services have migrated over         are considered for the action. The edges reflect the most significant
   to high-memory nodes, which have a much higher         connections we found and subsequently confirmed in the dataset.
   cost that the general nodes. I tried killing the          The most recurrent relationships identified during the open coding
   pod hoping it would restart on a different node,          (for RQ1 and RQ2) are also represented in the graph. Moreover, new
   but usually it just restarts on the same node.            links between preexisting labels were found based on topics (e.g., be-
    Quansight/qhub (issue: #321)                                   tween increase and alert) and new, more specific, terms ap-
                                                                   peared (e.g., ‘CPU’). We highlight that, although seeing specific terms
   From Fig. 6, we also observe that, despite the lower number of     in one context  is what led us to add the associated general label
repositories among issue-units of analysis, the majority (54 out of 89,      (e.g., instance for ‘CPU’), the fact that the specific term appears in
and an average of 85% per label) are unique to them. In conclu-    a topic is a strong indicative that it is prominent. Such particular cases
sion, despite the similarities of the assigned labels, the results suggest    prompted us to include the specific term to graph and connect it to the
that the information extracted from issues can complement that from     related terms and the more general one.
commits. In particular, issues can provide more knowledge about the        After identifying their relationships, some of the topics identified
decision-making surrounding cost management in the deployment of     for the previous question can be interpreted as specific pain points that
cloud systems configured with IaC.                                      developers are clearly concerned about: choices concerning network-
                                                                                 ing, instance and provider selection, and the applicable billing mode
4.3. Knowledge Organization (RQ3 )                                          (property level in Fig. 8). Other topics signify specific actions taken to
                                                                       address these concerns, or awareness that these actions could/should be
   From the initial coding performed for RQ1 and RQ2, we obtained     taken to avoid unnecessary costs: setting or removing alerts, testing for
a set of 14 labels. Moreover, as we delved in the units’ content to
                                                               one or more of these concerns (e.g. the use of VPN), or changing some-
further understand what kind of information can be extracted, we found
                                                                         thing in the Terraform file towards directly dealing with these concerns
evidence of connections and additional relevant themes. For example,
                                                                                 (action level in Fig. 8). All these actions, both affected and intended
in the unit regarding alphagov/govuk-aws (hash: 6cfda6ad) presented in
                                                                            to be affected can be characterized based on their desired outcome:
Section 4.1, we notice a clear link between instance and saving, as
                                                                           increasing awareness, dealing with increasing costs, or produce savings
well as indication of what motivates the change (i.e., more CPU). This
                                                                                          (effect level in Fig. 8).
particular unit had already been tagged with both labels, but our labels
are not fine-grained to the point of providing lower levels of detail.           In conclusion, the information aggregated in the knowledge graph
  We note that one main reason for not using finer-grained labels dur-     serves as a summary of relevant cost-related concerns and actions when
ing coding was to avoid explosion of labels that, although meaningful,     deploying cloud-based applications using Terraform. It also introduces
might not have been ultimately relevant (i.e., not recurrent enough)     the subjects one may expect to find in our dataset in terms of both
and could risk the quality of the procedure. Our goal is to guide future     content and context. Altogether, it opens the door to extract deeper
research and practitioners’ decisions by providing a more generalizable     insights and inform research and deployment decisions, as discussed
and actionable knowledge based on developers’ experience. Thus, we     below.

                                                                        8

### Página PDF 9

D. Feitosa et al.                                                                                                   The Journal of Systems & Software 215 (2024) 112112


Fig. 7. UpSet plot showing the occurrences and co-occurrences of topic labels in commit messages and issues discussions as label intersections resulting from the open coding in
RQ1 and RQ2.


                                                            2023 data dump, namely, posts,13 comments14 and change histories,15
                                                                               totaling 57.3 GiB. As the goal of this process is to triangulate the results
                                                                              of the study on GitHub repositories, we specifically targeted discussions
                                                                   about Terraform, rooted in questions containing tags with the string
                                                                               ‘terraform’ in the post’s metadata. Thus, we started by filtering ques-
                                                                              tions fitting the mentioned criteria, which led to a dataset of 19 139
                                                                         questions stored as JSON files.
                                                  We gathered the comments and post histories associated with each
                                                                        question and updated the respective JSON file to include them. We then
                                                                          extracted the answers linked to each question, identified through their
                                                                       parent post IDs, and added the comments and post histories similarly
                                                                            to the questions. The answers (and associated data) were then added
                                                                            to the question files, creating the final version of the dataset of 19 139
                                                                         questions and their associated answers, complete with their respective
                                                            comments and post histories.

Fig. 8. Knowledge graph resulting from the axial and selecting coding; label save
replaces the label saving used in open coding.                                      5.2. Data analysis


                                                                               In the analysis, we aimed at investigating whether or not the
5. Results triangulation                                               concepts depicted in Fig. 8 are also present and prominent in SO
                                                                              discussions. For that, we started with filtering cost-related questions
   To verify and strengthen our findings, we sought to investigate the    by searching the body, title, comments and history of all questions
extent to which the identified related topics are also discussed among    and associated answer(s) for the same keyword stems used for filtering
developers outside GitHub. In particular, in this section, we analyze    commit messages (see Section 3.3): bill, cheap, cost, efficient,
the discussions of developers in Stack Overflow12 (SO) and aim at    expens, and pay.
the triangulating the observations from this empirical work with those        Next, we searched the same fields mentioned above of each filtered
presented in Section 4.3. We start by presenting the data collection     question for the properties documented in our knowledge graph (see
procedure, followed by the performed analysis, and concluding with     Fig. 8). In this process, we augmented each question JSON file with a
the results and comparison against our previous observations.                  list of filtered sentences that contain one or more of these properties.
                                                                                 Finally, two of the authors manually inspected a representative sample

5.1. Data collection

                                                                                                  13 https://archive.org/download/stack-exchange-data-dump-2023-09-
   The data collection entailed the extraction of relevant discussions
                                                                              12/stackoverflow.com-Posts.7z
from SO. For that, we used key datasets from the September 12,        14                                                                                 https://archive.org/download/stack-exchange-data-dump-2023-09-
                                                                          12/stackoverflow.com-Comments.7z
                                                                                                  15 https://archive.org/download/stack-exchange-data-dump-2023-09-
  12 https://stackoverflow.com/                                                 12/stackoverflow.com-PostHistory.7z

                                                                        9

### Página PDF 10

D. Feitosa et al.                                                                                                   The Journal of Systems & Software 215 (2024) 112112


                                                        I am trying to reduce the cost of my AWS
                                                        infrastructure deployed using Terraform for
                                                        a Django app. I have 2 public subnets and 2
                                                        private subnets and in the subnets I deploy
                                                        NAT gateways and elastic ips. all works but is
                                                        expensive.
                                                                                      post id: #74422443                                label: nat


                                                                        Developers even identify cost-related features requested to be added
                                                                            to Terraform as an answer to existing problems:

                                                        Also  savings  plans  have  largely  replaced
                                                        reserved instances for now so I had be tracking
                                                        this   issue    https://github.com/hashicorp/terraform-
                                                                         provider-aws/issues/10785 if you are interesting in
                                                        support for using Terraform to manage savings
                                                        plans.
                                                                                      post id: #48751593                         label: provider

Fig. 9. Co-occurrences of action and property concepts from the knowledge graph of
Fig. 8 in Stack Overflow questions and their associated answers.                      Adding sentences where the initial keywords (i.e. cost, bill, etc.) are
                                                                mentioned provides additional insights:

                                                        Since licensing of SQL Server is expensive, I
                                                        want to switch it off at least for the night.
of the questions where properties were found with the goal of estab-                                                                                      post id: #76474230                          label: expense
lishing the accuracy of this process. We note that the generated dataset
and used scripts are publicly available (Feitosa et al., 2024).

                                                        I have multiple databases running in each
5.3. Results and discussion                                      environment which are charging me a lot of
                                                        cost each month, so i wanted to downscale the
   The initial filtering (using keywords stems) returned a total of 491       DTUs to some lower count during non-working
questions, i.e., approx. 2.6% of all questions on SO with ‘terraform’ in       hours, again during working hours DTUs to be
any of the tags. Although the sample size may seem small compared       upscale back to actual DTUs count, it should
to the entire population of Terraform-related questions, we note that       happen automatically as per time settings every
this is double the sample size compared to that of GitHub repositories       single day.
containing cost-related commits (1.3%, 2 010 out of 152 735 containing          post id: #74538381                               label: cost
Terraform artifacts; see Section 3.3). This proportional increase may
be further indicative of developers’ involvement with and attention to      Some of these discussions point towards the need for architectural
cost-related decisions.                                                      refactoring as a way of addressing cost-related concerns:
   Upon inspecting these questions and their answers for actions and
properties from our knowledge graph, we learned that 451 (approx.       If you need zero cost during idle time, should
92%) of them mention one or more of these concepts. In the diagonal of       you go with serverless with new design?
Fig. 9, we show the exact number of questions and associated answers          post id: #56530721                               label: cost
where each concept was present as a term. While properties such
as area appear only once, other properties such as provider and       Aided by these highlighted sentences, we proceeded to manually
instance (189 and 138 occurrences, respectively) but also actions     inspect a representative sample of 37 questions,16 considering that we
such as change (199) and test (154) are very popular. The same     selected 2.6% of a population of 19 139 questions with Terraform tags.
question and its associated answers might contain a reference to more    During the inspection, we aimed to verify whether: (1) the question
than one such concept. From these questions’ JSON  file, we then     indeed contained a cost-related discussion (either as the main problem
extracted 3 934 sentences containing one or more of these concepts.       or as the element of a description or argument), and (2) one of the
   Extracted sentences showcase developers sharing their experiences     properties is an essential element of the identified cost-related text.
in dealing with insidious cost-inducing technicalities in using existing    As a result, we found that all inspected questions were true positives.
services or asking for advice in this direction:                          These combined observations show that the knowledge graph cannot
                                                                      only be used to identify actual pain points faced by cloud application
   Azure by itself discusses the challenge you         developers, but it also points to the most recurrent ones.
   are addressing and recommends using  ""data           Based on the co-occurrences identified in Fig. 9, we proceeded to in-
   lifecycle"" for reducing the storage costs.          vestigate if and how the knowledge graph could be augmented. We note
   [...] After you enable blob versioning for a          that the frequency of the observed co-occurrences varies greatly while
   storage account, every write operation to a          also being positively skewed, i.e., many low co-occurrences (min.: 1,
   blob in that account results in the creation of        Q1: 2, Q2: 5, Q3: 12, max.: 98). Following our goal of representing the
   a new version.
     post id: #72881767                          label: storage              16                                                                                   https://www.calculator.net/sample-size-calculator.html?type=1&cl=95&
                                                                      ci=5&pp=2.6&ps=491&x=Calculate

                                                                        10

### Página PDF 11

D. Feitosa et al.                                                                                                   The Journal of Systems & Software 215 (2024) 112112


                                      Fig. 10. Knowledge graph updated based on the co-occurrences of concepts in the Stack Overflow posts.


most meaningful information in the knowledge graph, we processed the     help practitioners avoid common mistakes and pitfalls in managing
co-occurrence frequencies as follows:                                         their operational expenses in the cloud.
                                                                  With respect to the researcher community, our findings demonstrate
    1. mark preexisting graph edges that were not observed as absent;     that there is indeed empirical evidence of software developers being
    2. classify the observed co-occurrences into present (𝑓≤2),    aware of the cost of their choices with respect to deploying their
     recurrent (2 < 𝑓 ≤4), frequent (4 < 𝑓 ≤12) and     software in the cloud. This evidence is corroborated by the number of
     predominant (12 < 𝑓) according to the four quartiles;            posts on Stack Overflow discussing the topics we identified as important
    3. mark preexisting graph edges observed in the data according to     for cost awareness. While this conclusion is the product of processing
       their frequency class (established in the previous step); and        only a specific type of artifacts in open source repositories and user
    4. add new graph edges for predominant co-occurrences that were     forums, there is no reason to make us believe that there is no further
      not present in the previous version.                              evidence to be uncovered when other types of artifacts, or even the
                                                                       software source code in the identified repositories in the dataset is
   The resulting knowledge graph is depicted in Fig. 10. We note that    examined. The findings of this study are therefore a call for further
the markings explained in the figure legend are aimed at helping the     studies on cost awareness during software development.
reader visualize the process. The augmented graph comprise all pre-       More specifically, the following research items can be pursued by
existing edges with the addition of the new edges for predominant     starting with our existing dataset:
co-occurrences. Looking at the differences and co-occurrences frequen-
                                                          ➥Provide a finer-grain analysis of the collected evidence looking
cies, while many relationships between concepts are also observed in
                                                                                     at e.g. the commit contributors and type of projects involved.
this dataset, we learn two main lessons: (a) the cost-related topics
                                                                    Combined, for example, with a practitioner’s survey or inter-
revolve mainly around the ability to try out different configurations
                                                                              views, it can shed light on how different development teams and
(i.e., test) and updating configuration (i.e., change), also meaning          organizations deal with cost-related issues.
that creating system alerts is not frequently discussed; and (b) discus-      ➥Collect and correlate cost awareness evidence from the pull re-
sions are more concrete in the sense that they get more specific about                                                                               quests (PRs) of the identified repositories. PRs can provide the
deployment matters such as features and benefits of providers, e.g., ap-          missing link between commits and issues and offer further in-
propriate instances and policies. The latter point, in turn, led to a           sights into the cost management practices.
number of new relations being identified between ‘‘low level’’ concepts     ➥Extend the evidence search to other cloud orchestrator solutions,
in the graph, e.g., between instance and policy or cluster.             both provider-agnostic (e.g. TOSCA17) and -specific ones (AWS
                                                                            CloudFormation18), and compare the findings. Especially for the
6. Implications & future work                                                          latter, GitHub might not necessarily be the best data source for
                                                                                          this purpose, with the repositories of (large) organizations and
   The presented findings have implications for both practitioners and           enterprises with mature cloud presence over the years being much
                                                                more attractive sources of data.academic researchers. With respect to the former, it becomes clear that
                                                    ➥Apply natural language processing and other machine learningcost awareness should actually be present, if it is not already, through-
                                                                            techniques such as sentiment analysis to gain further insights
out the development of cloud-based applications. Our dataset contains
                                                                                   into the reasoning of the developers. Sentiment analysis in par-
multiple examples of developers rushing to adapt their deployment
                                                                                        ticular has been shown to be a mixed bag when software  is
configurations to deal with prohibitive costs, or intentionally designing
                                                                        concerned (Lin et al., 2022), but with the training of the analyzer
their deployment with the clear intention of avoiding them, particularly
                                                                            focused on cloud orchestrator artifacts and their associated com-
when specific cloud services are involved. More importantly, there are                                                                         mit messages and issue discussions, it might be possible to get
specific pain points and actions that can be taken for reducing costs                                                                                   better results through the tighter scope.
in these cases and lessons learned by other developers to be extracted
by investigating our curated dataset. Looking at the questions posted on
Stack Overflow on the topic, and the corresponding answers, it becomes        17 https://docs.oasis-open.org/tosca/TOSCA/v1.0/TOSCA-v1.0.html
clear that having such knowledge in advance at their disposal would        18 https://aws.amazon.com/cloudformation/

                                                                        11

### Página PDF 12

D. Feitosa et al.                                                                                                   The Journal of Systems & Software 215 (2024) 112112

 ➥Look for similar evidence in other types of artifacts, for example     8. Conclusions
     other configuration files, and/or in closed source repositories,
      e.g. of large software-intensive organizations and enterprises.       Managing the operational expenses of deploying software in the
     This search can go beyond cloud-based software, or at least     cloud is a major challenge for organizations. However, how practition-
     public cloud deployments, and incorporate also the wealth of     ers approach this topic has so far been treated by the literature in an
    DevOps tools available for automating software deployment and     anecdotal and therefore non systematic manner. Consequently, and as a
     management.                                                                        first step, in this work we investigated whether there is (empirical) ev-
 ➥Look also in the source code of repositories, starting with the ones     idence of software developers being aware of the operational expenses
     already containing cost-aware orchestration artifacts as easier to     of deploying and delivering software in the cloud, and if yes, then what
     reach targets. This is an obvious extension of the current work,     kind of information can be extracted from this evidence and how this
     but will need a wide experience with multiple programming                                                                       information can be organized for further study.
     languages and platforms on behalf of the researchers.                                                                    Given the wide scope and previously unexamined nature of these
 ➥Use the extracted posts from Stack Overflow to extend the list of                                                                            questions, at least from an MSR perspective, we started tackling them
      topics related to cost awareness, and update the knowledge graph                                                              by focusing on cloud orchestrator descriptor files. We chose reposi-
      of Fig. 8 accordingly.
                                                                           tory mining as our methodology, and designed and executed the first
  ➥Organize the collected information into reusable knowledge con-                                                                   such study searching for evidence in open source code repositories on
     cerning the best practices of managing the operational expenses
                                                               GitHub that contain Terraform orchestration artifacts, a very popular
      of cloud-based software. In a sense, this would be the outcome of
                                                                          provider-agnostic IaC tool.
      this research agenda with the most impact to the wider commu-
                                                               Our search was shown to be successful, insofar as it actually allowed
      nity.
                                                                      us to retrieve and organize in a dataset not only evidence of cost aware-
  We strongly believe that this is only the first study of many to come     ness by software developers, but also of specific actions being taken
on this particular topic.                                                   as a result. More specifically, with respect to extracting information
                                                                from commit messages in the selected repositories (RQ1), our findings
7. Threats to validity                                         show that the most popular topics dominating the developer discourse
                                                                                                is not limited to being aware of the potential or actual cost of deploying
   Like any other empirical study in software engineering, this work’s
                                                              and operating the system in the cloud. Developers seem also to not
validity is also threatened (and these threats mitigated) in several ways.
                                                                      only be taking concrete actions to minimize this cost, but also to avoid
The main threats to this work are discussed in the following.
                                                                           excessive charging to occur when e.g. using specific cloud services
   External Validity: Regarding external validity, the population in
                                                                  and/or offerings within them. Processing cost-related issues from the
our data sets (from GitHub and Stack Overflow) may not represent
                                                            same repositories (RQ2) did not reveal any additional information inall possible cost-related discussions in cloud projects. The inclusion of
                                                                    terms of identified topics of discussion. It did however offer furtherrepositories hosted in other (closed-source) platforms, or that use other
                                                                               insights into the decision-making process entailed in managing cloudcloud orchestrators, or that use no cloud orchestrators, could lead to
                                                                               costs that can be pursued further in future work.the identification of new discussions. The inclusion of discussion forums
other than Stack Overflow could also lead to new discussions. However,        Enriching and organizing the extracted information from the pre-
our decisions were carefully considered with the aim of ensuring data     vious steps into a knowledge graph (RQ3) helped us identify both
quality, diversity and quantity while keeping the execution feasible     higher-level, recurring concepts such as awareness, and specific pain
for the available human resources. Furthermore, our goal was not to     points such CPU and RAM (sizes) in the deployment and operation
collect all possible evidence, to begin with, but rather to see if there     of cloud-based software that dominate the developers’ discussions.
is any evidence available. That said, the results triangulation (between    The follow-up triangulation with Stack Overflow Terraform discussions
GitHub- and Stack Overflow-based discussions) helps mitigate threats     that address cost concerns corroborates these pain points and their
to external validity.                                                    prevalence in the spectrum of discussion topics.
   Construct Validity: The selection criteria, and most noticeably the         Finally, based on that evidence and the limitations of this work we
defined keywords may threat the construct validity of our work. We    developed a list of future research items which both provides us with
mitigated this threat by piloting and testing our selection criteria, and    a clear roadmap for future work, and offers to the wider community
considering the knowledge of both academic and industrial domain    an opportunity to develop a new research topic at the intersection of
experts. Furthermore, the coding activity  is naturally open to sub-    mining software repositories and cloud computing.
jectivity and inconsistencies. To mitigate this threat, we followed a
well-established process, and introduced an extra final step to consol-    CRediT authorship contribution statement
idate the knowledge and systematically discuss the labels. Also, the
topics derived from applying LDA may not fully represent their content.                                                                    Daniel Feitosa: Writing – original draft, Validation, Supervision,
We mitigate this threat by manually inspecting the units of analysis
                                                                         Software, Methodology, Formal analysis, Data Curation, Conceptual-
during the investigation of RQ3, which was part of the axial coding                                                                                  ization. Matei-Tudor Penca: Software, Formal analysis, Data cura-
and selective coding. This threat is also mitigated by the triangulation
                                                                                   tion. Massimiliano Berardi: Software, Formal analysis, Data curation.
presented in Section 5. That said, we acknowledge that the Stack
                                                                 Rares-Dorian Boza: Software, Formal analysis, Data curation. Vasil-
Overflow study itself suffers from its own threats to construct validity,
                                                                          ios Andrikopoulos: Writing – original draft, Validation, Supervision,
mainly related to selection of appropriate data points, i.e., pertaining to
                                                                  Methodology, Conceptualization.cost-related discussion of Terraform-based deployments. The mitigation
strategies in this case entail the use of Terraform-related tags that have
                                                                   Declaration of competing interestbeen assigned by users, on top of using previously-validated keywords
for searching cost-related entries within the filtered posts.
   Reliability: Finally, to mitigate threats to the reliability of the       The authors declare that they have no known competing finan-
study, we have described the data acquisition process in as much detail      cial interests or personal relationships that could have appeared to
as possible. More importantly, the dataset curated through our efforts     influence the work reported in this paper.
is publicly available (Feitosa et al., 2024) together with the scripts
to aid the replication the data collection and topic modeling tasks.    Data availability
This package also includes the dataset and scripts used for the results
triangulation with Stack Overflow questions.                     We have shared the link to my data and code in the manuscript.

                                                                        12

### Página PDF 13

D. Feitosa et al.                                                                                                   The Journal of Systems & Software 215 (2024) 112112

Acknowledgments                                                                   Hindle,  A., 2013. Green mining: A methodology of relating software change and
                                                                                                configuration to power consumption. Empir. Softw. Eng. 20 (2), 374–409. http:
   The authors would like to thank Diomidis Spinellis for providing the         //dx.doi.org/10.1007/s10664-013-9276-6.
                                                                                           Hindle, A., Ernst, N.A., Godfrey, M.W., Mylopoulos, J., 2011. Automated topic naming
inspiration for this work.
                                                                                                    to support cross-project analysis of software maintenance activities. In: Proceedings
                                                                                                     of the 8th Working Conference on Mining Software Repositories. MSR, ACM,
References                                                                                 Waikiki, Honolulu, HI, USA, pp. 163–172. http://dx.doi.org/10.1145/1985441.
                                                                                    1985466.
Abdellatif, A., Costa, D., Badran, K., Abdalkareem, R., Shihab, E., 2020. Challenges     Hoffman, M., Bach, F., Blei, D., 2010. Online learning for latent Dirichlet allocation.
    in chatbot development: A study of stack overflow posts. In: Proceedings of the            In: Lafferty, J., Williams, C., Shawe-Taylor, J., Zemel, R., Culotta, A. (Eds.), In:
    17th International Conference on Mining Software Repositories. MSR, ACM, Seoul,         Advances in Neural Information Processing Systems, vol. 23, Curran Associates,
    Republic of Korea, pp. 174–185. http://dx.doi.org/10.1145/3379597.3387472.                Inc..
Ahmed,  S., Bagherzadeh, M., 2018. What do concurrency developers ask about? A      Hosseinzadeh, M., Hama, H.K., Ghafour, M.Y., Masdari, M., Ahmed, O.H., Khezri, H.,
    large-scale study using stack overflow.  In: Proceedings of the 12th ACM/IEEE         2020. Service selection using  multi-criteria decision making: A comprehensive
    International Symposium on Empirical Software Engineering and Measurement.          overview. J. Netw. Syst. Manage. 28 (4), 1639–1693.
   ACM, Oulu, Finland, http://dx.doi.org/10.1145/3239235.3239524.                  Howard, M.J., Gupta, S., Pollock, L., Vijay-Shanker, K., 2013. Automatically mining
Al Alamin, M.A., Malakar,  S., Uddin, G., Afroz,  S., Haider, T.B., Iqbal, A., 2021.          software-based, semantically-similar words from comment-code mappings. In: Pro-
   An empirical study of developer discussions on low-code software development          ceedings of the 10th Working Conference on Mining Software Repositories. IEEE,
    challenges. In: 2021 IEEE/ACM 18th International Conference on Mining Software          pp. 377–386.
    Repositories. MSR, pp. 46–57. http://dx.doi.org/10.1109/MSR52588.2021.00018.       Jamshidi, P., Ahmad, A., Pahl, C., 2013. Cloud migration research: A systematic review.
Amato,  A.,  Venticinque,  S.,  2016.  Multiobjective  optimization  for  brokering  of         IEEE Trans. Cloud Comput. 1 (2), 142–157.
    multicloud service composition. ACM Trans. Internet Technol. (TOIT) 16 (2), 1–20.      Kovács,  J., Kacsuk,  P., 2017. Occopus: A multi-cloud orchestrator to deploy and
Andrikopoulos, V., Binz, T., Leymann, F., Strauch, S., 2013. How to adapt applications        manage complex scientific infrastructures. J. Grid Comput. 16 (1), 19–37. http:
    for the cloud environment. Computing 95 (6), 493–535. http://dx.doi.org/10.1007/         //dx.doi.org/10.1007/s10723-017-9421-3.
    s00607-012-0248-2.                                                                         LeClair, A., Eberhart, Z., McMillan, C., 2018. Adapting neural text classification for
Armbrust, M., Fox, A., Griffith, R., Joseph, A.D., Katz, R., Konwinski, A., Lee, G.,         improved software  categorization.  In: 2018 IEEE  International Conference on
    Patterson, D., Rabkin, A., Stoica,  I., et  al., 2010. A view of cloud computing.          Software Maintenance and Evolution. ICSME, IEEE, http://dx.doi.org/10.1109/
   Commun. ACM 53 (4), 50–58.                                                         icsme.2018.00056.
Arunarani, A., Manjula, D., Sugumaran, V., 2019. Task scheduling techniques in cloud                                                                                             Lex, A., Gehlenborg, N., Strobelt, H., Vuillemot, R., Pfister, H., 2014. UpSet: Visualiza-
    computing: A literature survey. Future Gener. Comput. Syst. 91, 407–415.                                                                                                    tion of intersecting sets. IEEE Trans. Visual. Comput. Graph. 20 (12), 1983–1992.
Bao, L., Lo, D., Xia, X., Wang, X., Tian, C., 2016. How android app developers manage
                                                                                            http://dx.doi.org/10.1109/tvcg.2014.2346248.
   power consumption?  In: Proceedings  of the 13th International Conference on
                                                                                                    Lin, B., Cassee, N., Serebrenik, A., Bavota, G., Novielli, N., Lanza, M., 2022. Opinion
    Mining Software Repositories. ACM, http://dx.doi.org/10.1145/2901739.2901748.
                                                                                     mining for software development: A systematic literature review. ACM Trans. Softw.
Blei, D.M., 2010. Probabilistic topic models. IEEE Signal Process. Mag. 27, 55–65.
                                                                                          Eng. Methodol. 31 (3), http://dx.doi.org/10.1145/3490388.
Campbell, J.C., Hindle, A., Stroulia, E., 2015. Latent Dirichlet allocation: Extracting
                                                                                              Mell, P., Grance, T., et al., 2011. The NIST definition of cloud computing. NIST Special
    topics from software engineering data. In: The Art and Science of Analyzing Soft-
                                                                                                Publication 800-145.
   ware Data. Elsevier, pp. 139–159. http://dx.doi.org/10.1016/b978-0-12-411519-
                                                                                Moura,  I., Pinto, G., Ebert,  F., Castor,  F., 2015. Mining energy-aware commits. In:
    4.00006-9.
                                                                              2015 IEEE/ACM 12th Working Conference on Mining Software Repositories. IEEE,
Chauhan, M.A., Babar, M.A., Benatallah, B., 2017. Architecting cloud-enabled systems:
                                                                                             http://dx.doi.org/10.1109/msr.2015.13.
   A systematic survey of challenges and solutions. Softw.  - Pract. Exp. 47  (4),
                                                                                                  Pereira, R., Matalonga, H., Couto, M., Castor, F., Cabral, B., Carvalho, P., de Sousa, S.M.,
    599–644.
                                                                                            Fernandes,  J.P., 2021. GreenHub: A large-scale collaborative dataset to battery
Chen, T.-H., Thomas, S.W., Nagappan, M., Hassan, A.E., 2012. Explaining software
                                                                                     consumption analysis of android devices. Empir. Softw. Eng. 26 (3), http://dx.
    defects using topic models. In: Proceedings of the 9th IEEE Working Conference
                                                                                        doi.org/10.1007/s10664-020-09925-5.
   on Mining Software Repositories. MSR, pp. 189–198. http://dx.doi.org/10.1109/
                                                                                                 Pinto, G., Castor, F., Liu, Y.D., 2014. Mining questions about software energy con-
    MSR.2012.6224280.
                                                                                          sumption. In: Proceedings of the 11th Working Conference on Mining Software
Choetkiertikul, M., Dam, H.K., Tran, T., Ghose, A., 2015. Characterization and predic-
                                                                                                     Repositories. pp. 22–31.
    tion of issue-related risks in software projects. In: Proceedings of the 12th Working
                                                                                                Qi, P., Zhang, Y., Zhang, Y., Bolton, J., Manning, C.D., 2020. Stanza: A Python natural
    Conference on Mining Software Repositories. IEEE, pp. 280–291.
                                                                                        language processing toolkit for many human languages. In: Proceedings of the
Choetkiertikul, M., Dam, H.K., Tran, T., Ghose, A., Grundy, J., 2018. Predicting delivery
                                                                                      58th Annual Meeting of the Association for Computational Linguistics: System
    capability in  iterative software development. IEEE Trans. Softw. Eng. 44  (6),
                                                                                            Demonstrations.
    551–573. http://dx.doi.org/10.1109/tse.2017.2693989.
Cong, P., Xu, G., Wei, T., Li, K., 2020. A survey of profit optimization techniques for      Reboucas, M., Pinto, G., Ebert, F., Torres, W., Serebrenik, A., Castor, F., 2016. An
    cloud providers. ACM Comput. Surv. (CSUR) 53 (2), 1–35.                                 empirical study on the usage of the Swift programming language. In: Proceedings
Corbin, J., Strauss, A., 2014. Basics of Qualitative Research: Techniques and Procedures           of the IEEE 23rd International Conference on Software Analysis, Evolution, and
    for Developing Grounded Theory. SAGE Publications.                                      Reengineering. SANER, IEEE, http://dx.doi.org/10.1109/saner.2016.66.
da Costa, D.A., McIntosh, S., Treude, C., Kulesza, U., Hassan, A.E., 2017. The impact       Sas, C., Capiluppi, A., 2022. Antipatterns in software classification taxonomies. J. Syst.
    of rapid release cycles on the integration delay of fixed issues. Empir. Softw. Eng.          Softw. 190, 111343. http://dx.doi.org/10.1016/j.jss.2022.111343.
   23 (2), 835–904. http://dx.doi.org/10.1007/s10664-017-9548-7.                       Shuaib, M., Samad, A., Alam, S., Siddiqui, S.T., 2019. Why adopting cloud is still a
Das, T., Di Penta, M., Malavolta, I., 2016. A quantitative and qualitative investigation         challenge?—A review on issues and challenges for cloud migration in organizations.
    of performance-related commits  in android apps.  In: 2016 IEEE  International            In: Ambient Communications and Computer Systems. Springer, pp. 387–399.
    Conference on Software Maintenance and Evolution. ICSME, IEEE, pp. 443–447.        Spadini, D., Aniche, M., Bacchelli, A., 2018. PyDriller: Python framework for mining
de Carvalho,  L.R., de Araujo,  A.P.F., 2020. Performance comparison of terraform          software repositories. In: Proceedings of the 2018 26th ACM Joint Meeting on
   and cloudify as multicloud orchestrators. In: 2020 20th IEEE/ACM International         European Software Engineering Conference and Symposium on the Foundations
   Symposium on Cluster, Cloud and Internet Computing. CCGRID, IEEE, http://dx.           of Software Engineering. ESEC/FSE 2018, ACM, New York, New York, USA, pp.
    doi.org/10.1109/ccgrid49817.2020.00-55.                                             908–911. http://dx.doi.org/10.1145/3236024.3264598, URL: https://github.com/
Dueñas, S., Cosentino, V., Robles, G., Gonzalez-Barahona, J.M., 2018. Perceval: Software           ishepard/pydriller.
    project data at your will. In: Proceedings of the 40th International Conference on      Tomarchio, O., Calcaterra, D., Modica, G.D., 2020. Cloud resource orchestration in
    Software Engineering: Companion Proceedings. ICSE-C, ACM, Gothenburg, Sweden,          the multi-cloud landscape: A systematic review of existing frameworks. J. Cloud
    pp. 1–4. http://dx.doi.org/10.1145/3183440.3183475, URL: https://github.com/         Comput. 9 (1), 1–24.
    chaoss/grimoirelab-perceval.                                                         Treude, C., Wagner, M., 2019. Predicting good configurations for GitHub and stack
Feitosa, D., Penca, M.-T., Berardi, M., Boza, R.-D., Andrikopoulos, V., 2024. Supple-          overflow topic models. In: Proceedings of the IEEE/ACM 16th International Con-
    mentary material for mining cost awareness in the infrastructure as code artifacts          ference on Mining Software Repositories. MSR, IEEE, http://dx.doi.org/10.1109/
    of cloud-based applications. http://dx.doi.org/10.5281/zenodo.11312689.                 msr.2019.00022.
Han, J., Shihab, E., Wan, Z., Deng, S., Xia, X., 2020. What do programmers discuss      Tricomi, G., Merlino, G., Panarello, A., Puliafito, A., 2020. Optimal selection techniques
    about deep learning frameworks. Empir. Softw. Eng. 25 (4), 2694–2747. http:           for cloud service providers. IEEE Access 8, 203591–203618.
    //dx.doi.org/10.1007/s10664-020-09819-6.                                                 Vakili, A., Navimipour, N.J., 2017. Comprehensive and systematic review of the service
Harms, R., Yamartino, M., 2010. The economics of the cloud. Microsoft whitepaper,          composition mechanisms in the cloud environments. J. Netw. Comput. Appl. 81,
    Microsoft Corporation.                                                               24–36.

                                                                        13

### Página PDF 14

D. Feitosa et al.                                                                                                   The Journal of Systems & Software 215 (2024) 112112


Řehůřek,  R., Sojka,  P., 2010. Software framework  for topic modelling with large       specifically in LLM agents, information retrieval and data mining within the life sciences
    corpora. In: Proceedings of the LREC 2010 Workshop on New Challenges for NLP     domain. Matei is committed to integrating the latest research technologies for optimized
    Frameworks. ELRA, Valletta, Malta, pp. 45–50.                                         data-driven applications.
Wohlin,  C., Runeson,  P., Höst, M., Ohlsson, M.,  Regnell,  B., Wesslén,  A., 2012.
    Experimentation in Software Engineering. In: Computer Science, Springer Berlin,
                                                                                Massimiliano Berardi is a recent graduate of Computing Science from the University of
    Heidelberg.
                                                                                      Groningen, where he also contributed as a teaching assistant for various courses. He is
Zimmerle, C., Gama, K., Castor, F., Filho, J.M.M., 2022. Mining the usage of reactive
                                                                                              currently working as a Software Engineer at Syntho, a startup specializing in synthetic
   programming  APIs: A  study on GitHub and  stack  overflow.  In:  Proceedings
                                                                                        data generation. His expertise in database management and software architecture is
    of the 19th  International Conference on Mining Software  Repositories. MSR,
                                                                              employed in improving their product and growing as a company.
   ACM, Pittsburgh, Pennsylvania, pp. 203–214. http://dx.doi.org/10.1145/3524842.
    3527966.

                                                                                 Rareş-Dorian Boza is pursuing an M.Sc. in Computer Science at Delft University of
                                                                                      Technology, having previously earned his B.Sc. from the University of Groningen,
                                                                                          alongside the completion of the Honours College programme. Currently, he is delving
Daniel Feitosa  is an assistant professor at the University of Groningen, where he
                                                                                                into natural language processing  solutions, software  architecture, and information
contributes to the Software Engineering and Architecture group within the Bernoulli
                                                                                                         retrieval, specifically in the use case of recommender systems. Alongside academia,
Institute for Mathematics, Computer Science, and Artificial Intelligence. Earning his
                                                                                       Rareş is engaged as a software tooling intern for Intel’s department in Eindhoven.
Ph.D. from the same university, Daniel’s research interests are rooted in software
quality, mining software repositories, and developer experience, especially applied to
technical debt management, and energy efficiency. He has participated in EU-funded      Vasilios Andrikopoulos is associate professor at the University of Groningen, and a
project, such as SDK4ED, and  is an active member of various software engineering     member of the Software Engineering and Architecture group in the Bernoulli Institute
communities, having served as a program committee member in several conferences       for Mathematics, Computer Science and Artificial Intelligence. He received his Ph.D.
and referee for multiple journals.                                                   from Tilburg University, the Netherlands, and he has worked as a post-doc for both
                                                                                           Tilburg University and the University of Stuttgart, Germany. His research interests are in
                                                                                         software architectures for cloud-based systems, with an emphasis on their sustainability
Matei Tudor Penca  is a Data Scientist at Elsevier, a scientific publisher and data
                                                                                              across  all  its dimensions. He has participated in a number of EU-funded projects,
analytics company, where he contributes to the Data Science Life Sciences department
                                                                                           including the Network of Excellence S-Cube, and  is reviewing for a multitude of
of the Amsterdam team. He holds a Master’s degree in Information Studies: Data Science
                                                                                                   journals.
from the University of Amsterdam. His expertise lies in natural language processing,


                                                                        14
