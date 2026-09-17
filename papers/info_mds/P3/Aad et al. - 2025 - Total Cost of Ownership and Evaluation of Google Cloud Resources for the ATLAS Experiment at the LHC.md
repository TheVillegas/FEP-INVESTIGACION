# Total Cost of Ownership and Evaluation of Google Cloud Resources for the ATLAS Experiment at the LHC

> **Pilar:** P3
> **Clasificación:** Declarada en la matriz
> **Evidencia de clasificación:** Fila académica del CSV titulada “Total Cost of Ownership and Evaluation of Google Cloud Resources for the ATLAS Experiment at the LHC”, código P3.
> **Archivo fuente:** papers-pdf/Aad et al. - 2025 - Total Cost of Ownership and Evaluation of Google Cloud Resources for the ATLAS Experiment at the LHC.pdf
> **Uso previsto:** Lectura personal y apoyo documental; requiere validación humana antes de incorporarse al informe.

## 1. Título

*Total Cost of Ownership and Evaluation of Google Cloud Resources for the ATLAS Experiment at the LHC*.

## 2. Autor y fecha

- **Autoría verificada en el PDF:** **The ATLAS Collaboration**. El título del archivo usa “Aad et al.”, mientras que la matriz y la portada atribuyen el artículo a la colaboración. Se conserva el nombre del archivo para correspondencia 1:1, pero se usa la autoría colectiva en la referencia.
- **Fecha bibliográfica utilizada:** 2025, *Computing and Software for Big Science*, 9:2. El artículo fue aceptado en 2024 y publicado con copyright 2025.

## 3. Problema que trata

ATLAS necesitaba conocer la viabilidad técnica y el costo real de usar una nube comercial a gran escala como extensión del WLCG. Las tarifas son granulares, pero contratos, descuentos y tráfico de red pueden alterar drásticamente el TCO; una comparación directa con centros grid también oculta diferencias de financiación y costos locales.

## 4. Qué quiere hacer

Integrar Google Cloud durante un período prolongado, medir la contribución relativa de cómputo, almacenamiento y red al TCO, identificar impulsores dominantes, probar bursting y evaluar mecanismos de control de costos sin depender de tecnología propietaria.

## 5. Cómo lo hace

Analiza **15 meses**, julio de 2022–octubre de 2023, bajo una suscripción plana de USD 56.630,54 mensuales. Integra Kubernetes, PanDA y Rucio con interfaces cloud-native; ejecuta fases de aprendizaje, workflows individuales, bursts y operación comparable a un sitio grande. Compara costo contractual con precio de lista, desglosa servicios y recoge retroalimentación de administradores Tier-1 (secciones 2–6).

## 6. Resultados

- El contrato totaliza **USD 849.458**; el mismo uso a lista habría costado **USD 3,162 millones**, una diferencia de 73 %. Equivalentemente, se usaron 3,72 veces los recursos comprables a lista (sección 8, pp. 18–19).
- El sitio escala hasta **100.000 slots adicionales en una hora** y permite bursting con poca carga operativa adicional (Executive Summary y sección 8).
- Casi la mitad del costo de lista se atribuye a egress; en noviembre de 2022 llegó a 54 % del costo mensual (sección 5, figura 7 y tabla 1, pp. 14–15).
- Para tráfico superior a 3 PB/mes, una conexión dedicada podría reducir egress a menos de la mitad según el cálculo presentado; es una estimación a investigar, no un resultado implementado (sección 5.1).
- La tasa de tiempo perdido por fallos fue 5 % y las expulsiones Spot se estimaron en 1–2 %, dependientes de región y período (sección 6.1).

## 7. Discusión y trabajo futuro

La nube es flexible para CPU, GPU y ARM, pero almacenamiento y red dominan el riesgo económico. Se proponen peering dedicado, adaptación de gestión de datos/workflows, selección de cargas con menor egress, estudios de popularidad, privacidad y contratos. Los autores advierten sobre lock-in, soberanía, compra pública y que el acuerdo negociado no representa precio de lista universal (sección 7).

## 8. Conclusión del paper

La colaboración concluye que la nube comercial es técnicamente viable como capacidad adicional y de bursting para ATLAS, pero no universalmente adecuada para cualquier workflow. La suscripción fue crítica para controlar el costo; el egress sigue siendo el principal obstáculo y condiciona almacenamiento y reprocesamiento intensivo.

## Relación preliminar con INV-01

Se vincula con 3.6.1–3.6.2, 3.7.3–3.7.6, 5.7, 5.11–5.14 y 6.4 de INV-01: TCO, descuentos, egress, arquitectura, sensibilidad y riesgo contractual. Es un caso especializado y no una tarifa comparable directamente con ONEBYTE.

## Limitaciones de esta síntesis

El acuerdo es negociado y específico de ATLAS; el paper no intenta comparar directamente Google Cloud con un sitio grid. Los costos de lista son contrafactuales para el mismo uso y no precios vigentes. La autoría del archivo difiere de la portada. Las cifras deben verificarse humanamente en las secciones y tablas citadas.

## Texto extraído del PDF

> **Advertencia de conversión:** extracción textual automática de 35 páginas (189147 caracteres). Se conservaron títulos, párrafos, referencias y contenido textual por página. La disposición multicolumna, las figuras, las tablas y las ecuaciones pueden no mantener su alineación o representación visual; verifique esos elementos en el PDF original.

### Página PDF 1

Comput Softw Big Sci       (2025) 9:2
https://doi.org/10.1007/s41781-024-00128-x

 Research


Total Cost of Ownership and Evaluation of Google Cloud
Resources for the ATLAS Experiment at the LHC

The ATLAS Collaboration⋆

CERN, Geneva, Switzerland


Received: 24 May 2024 / Accepted: 27 September 2024
© The Author(s) 2025


Abstract  The ATLAS Google Project was established as    ponents within the cloud service to the total cost of owner-
part of an ongoing evaluation of the use of commercial clouds    ship, including compute, storage, and network, for different
by the ATLAS Collaboration, in anticipation of the poten-   ATLAS workﬂows and under different operating conditions,
tial future adoption of such resources by WLCG grid sites    and identify the dominant cost drivers.
to fulﬁl or complement their computing pledges. Seamless  A substantial amount of technical development work was
integration of Google cloud resources into the worldwide    dedicated to the seamless integration of cloud resources into
ATLAS distributed computing infrastructure was achieved    the ATLAS distributed computing infrastructure, employ-
at large scale and for an extended period of time, and hence    ing the same software stack, primarily through cloud-native
cloud resources are shown to be an effective mechanism to    interfaces like Kubernetes and signed HTTP URLs follow-
provide additional, ﬂexible computing capacity to ATLAS.    ing a cloud signature standard like S3v4. Care was taken
For the ﬁrst time a total cost of ownership analysis has been    to avoid vendor-speciﬁc choices and technology to mitigate
performed, to identify the dominant cost drivers and explore    the risk of potential price volatility in scenarios where one
effective mechanisms for cost control. Network usage sig-    resource or service provider has a monopoly. The ATLAS
niﬁcantly impacts the costs of certain ATLAS workﬂows,    GoogleProject has beenkeytotest andvalidateat scale. Once
underscoring the importance of implementing such mech-    these interfaces were established, the operation of an ATLAS
anisms. Resource bursting has been successfully demon-     site in the cloud has proven to be very effective, unlocking
strated, whilst exposing the true cost of this type of activity.     capabilities that would be either unfeasible or considerably
A follow-up to the project is underway to investigate meth-    time-consuming in an on-premises setting. For example, it
ods for improving the integration of cloud resources in data-    has enabled rapid scaling of the number of processing jobs
intensive distributed computing environments and reducing    within a few hours and the deployment of non-x86 architec-
costs related to network connectivity, which represents the    ture resources on a large scale, tasks that could ordinarily
primary expense when extensively utilising cloud resources.    take months to accomplish.
                                               From the technical perspective, the project was a success,
                                                          demonstrating that an ATLAS site can be deployed in a com-
Executive Summary                                        mercial cloud at a very large scale and in a very effective
                                                        manner, requiring little additional operational effort. No sig-
The ATLAS Google Project was established to continue an    niﬁcant technical issue was discovered to prevent the exper-
evaluation of commercial clouds, in anticipation of the poten-    iment routinely employing such resources in the future, and
tial future adoption of such resources by WLCG grid sites    the existing workﬂow and data management services and
to fulﬁl or complement their computing pledges to ATLAS.    software packages used by ATLAS are found to be adequate
Cost estimates of commercial cloud resources have been    foreffectivelymanagingtheoperationofasigniﬁcantamount
done within ATLAS before, but this is the ﬁrst time a total    of resources in the Google Cloud Platform.
cost of ownership evaluation was performed for a long-term   Over the course of the project, running jobs on the ATLAS
15-month period. Whilst commercial cloud pricing struc-   Google site may be broken down into several phases. The ini-
tures are usually ﬁne grained, like most clients ATLAS has     tial phase, which is described in some detail, was a process of
negotiated a ﬂat rate subscription agreement with Google for    familiarisation, learning how the site behaves, and applying
the duration of the project. Therefore, the method employed    necessary changes to bring the respective costs of the differ-
here is to analyse the relative contributions of various com-    ent services under control. This was followed by an extended
                                                            period of running individual ATLAS workﬂows. Bursting to
⋆e-mail: atlas.publications@cern.ch

                                     0123456789().: V,-vol                  123

### Página PDF 2

2  Page 2 of 35                                                     Comput Softw Big Sci        (2025) 9:2


a much greater number of cores was then examined, fol-   1 Introduction
lowed by the ﬁnal phase, where for the last few months of
the project both the CPU and storage were expanded to the   The ATLAS experiment [1] at the LHC [2] employs dis-
size of a typical large ATLAS site.                               tributed computing resources of up to one million cores of
This project has shown that commercial cloud computing is    computing, 350 PB of disk and over 500 PB of tape storage.
an effective technical mechanism for ATLAS for providing    These resources comprise the Tier-0 at CERN, the Tier-1 and
additional CPU resources at the level of a large WLCG site.    Tier-2 Worldwide LHC Computing Grid (WLCG) sites [3,4],
Resource bursting was successfully demonstrated, where    opportunistic resources at High Performance Computing
available CPU resources can be increased by 100,000 addi-   (HPC) sites and cloud computing providers, as well as volun-
tional cores within an hour and with no additional opera-     teer computing. In recent years such non-WLCG resources,
tional overhead. The utilisation of cloud-based storage was    particularly from HPC sites, have made increasingly sig-
alsodemonstrated,andtheimpactofnetworkcostsevaluated.    niﬁcant contributions to ATLAS computing, a trend that is
Networkegresscostscanbeveryhighandcurrentlydominate    expected to continue in the future.
the overall cost depending on the workloads run at the cloud   The use of commercial clouds has been investigated by all
site. This study has quantiﬁed this effect, whilst also con-    LHCexperiments[5–8],andwasrecentlyreviewedbytheUS
ﬁrming that the ATLAS data management software, Rucio,   ATLAS and CMS communities as part of a blueprint publi-
includes features that allow network trafﬁc and derived costs    cation [9]. ATLAS has examined the viability of both Google
to be effectively controlled. The ATLAS computing model    and Amazon cloud resources [10], including the integration
currently relies on a plentiful network connectivity between    of the two core components of the distributed computing
all sites, but it might evolve to reduce data trafﬁc if the actual    environment: the workload management system PanDA [11]
network costs were exposed.                             and the data management system Rucio [12]. These initial
By leveraging the Google Cloud Subscription Agreement    studies showed that such resources can be adopted for both
pricing model, ATLAS has effectively harnessed between    the ATLAS production and user analysis workﬂows, albeit
three and four times the resources compared to what the same     at a limited capacity, as well as demonstrating the potential
investment would deliver for the list-price. This underscores    for future R&D [10].
the vital importance of establishing such agreements with   As the start of Run 4 and the HL-LHC [13] era approaches,
cloud providers, which serve as essential tools for accessing    the need for additional CPU and especially disk resources
signiﬁcant volume discounts and ensuring cost predictabil-    continues to grow, to satisfy the computing requirements
ity, while retaining the ﬂexibility and scalability advantages    of the experiments [14,15]. At the same time, WLCG sites
inherent to cloud services. In essence, these agreements    are increasingly exploring methods to utilise new resources,
are not merely advantageous but rather a prerequisite for    aiming to fulﬁl their pledges in the most cost-effective and
enabling large-scale cloud deployments. As such, the list-    energy-efﬁcient manner while also making emerging tech-
price should therefore be seen as the upper limit of the actual    nologies accessible to users. With this in mind, the ATLAS
price paid for large-scale cloud services.                   Google Project (AGP) was established to continue an evalu-
Whilst many valuable insights into the use of commercial    ation of commercial clouds as a resource for ATLAS.
clouds have been provided,  it is  still possible to further    Whilst basic cost estimates of commercial cloud resources
develop the ATLAS workload and data management soft-    have been done before [7,10], one of the primary goals of
ware stack in order to integrate commercial clouds in the    the AGP is to develop  a Total Cost of Ownership (TCO)
most efﬁcient way. Key areas for future work include evalu-   model for commercial clouds, which is made possible by the
ating how the private cloud and LHC research network infras-    highly granular pricing information available from the cloud
tructure can be interconnected and how the orchestration of    provider. By comparison, other types of computing resources
data and workﬂows can provide maximal gains in the perfor-   employed by ATLAS, namely the grid, HPCs, clouds, and
mance and ﬂexibility of the computing model with minimal    volunteer computing, incur different effective costs to the
additional cost. The full implementation of these develop-    experiment, which are often difﬁcult to evaluate and com-
ments is important to enable exploring a potential evolution    pare since funding methodologies vary by resource type, by
of the ATLAS computing model that tackles the issue of net-    country, and even between different funding agencies within
work costs. An extension of the project would also enable the    the same country. Additionally, there are local arrangements
current, wide ranging R&D programme to continue, which     at the sites or savings, for example where some sites, typi-
exploits the elastic availability of special resources such as    cally at universities, do not directly pay electricity or WAN
GPUs and alternative architectures such as ARM, otherwise    access costs. It is therefore important to note that this TCO
not readily available to ATLAS, enabling fast validation and    evaluation is not attempting to directly compare the cost of
benchmarking of new architectures without the need to make    running ATLAS jobs in the Google Cloud with the cost of
upfront investment in hardware.                             running an ATLAS grid site. A TCO comparison of data

123

### Página PDF 3

Comput Softw Big Sci        (2025) 9:2                                                           Page 3 of 35    2


centre colocation and commercial cloud solutions has been     hibitively high for the distributed computing workﬂows used
previously performed in the context of expanding computing   by ATLAS. These workﬂows often exploit the high intercon-
resources at CERN [16], using input from the Helix Nebula    nectivity of the grid sites and incorporate many data transfers,
Science Cloud project [17].                                   as data hosted by one site is transferred to be used elsewhere.
The   structure   of   this   paper    is   the   following.    This high network interconnectivity may incur signiﬁcant
“CommercialCloudCostModelling”(Sect.2)delvesintothe    expense, which goes on top of the site budgets, as discussed
critical elements of commercial cloud cost models relevant    in “Dedicated Networks” (Sect. 5.1). Egress costs associated
to this study, examining the subscription agreement model    with cloud resources were a concern expressed by several
employed by ATLAS and outlining the methodology and    Tier-1 site administrators when interviewed for this report
scope of the TCO analysis. “ATLAS Google Site Integration”    (see “Feedback from Grid Site Administrators” (Sect. 6)).
(Sect. 3) brieﬂy outlines the technical aspects of integrating    Whilst discounts, credits and subscription plans may increase
the Google site and “Running the ATLAS Google Site” (Sect.    the complexity in determining future costs, they also pro-
4) offers a detailed account of the various tests conducted    vide mechanisms to reduce the total cost of using commer-
at different phases and the resulting conclusions. “Cloud and     cial clouds for ATLAS. It should however still be noted that
Network Costs” (Sect. 5) more closely examines the role of    even with deep discounts and credits, continuous monitoring
network trafﬁc in overall costs and underscores the rationale    of expenditure must be done, and as automated as possible,
for considering dedicated links. “Feedback from Grid Site    especially for large-scale use.
Administrators” (Sect. 6) presents feedback received from
a number of system administrators regarding the adoption    2.1 Subscription Model Employed by the ATLAS Google
of commercial clouds. Finally, “Further Investigations and        Project
Future Work” (Sect. 7) provides an outline of potential future
working directions and a summary is presented in “Sum-    For this latest phase of the AGP, a Google Cloud Service
mary” (Sect. 8).                                        Agreement for Public Sector contract was negotiated with
                                                    Google to explore more solid ideas about employing Google
                                                             as an ATLAS production site. This contract, which uses the
2 Commercial Cloud Cost Modelling                            latest pricing model, was negotiated via US national labo-
                                                                    ratories and is based on an initial assumption of an average
In contrast  to other computing resources employed by    of 7000 compute cores together with up to 7 PB of storage,
ATLAS, including those deployed via the WLCG grid, com-    and an estimated egress of no more than 0.7 PB per month.
mercial cloud resources have well-deﬁned pricing for com-   As is often the case with commercial cloud resources, there
puting time and services used, for example at Amazon Web     is no charge for data ingress, that is for uploading ATLAS
Services (AWS) [18] or on the Google Cloud Platform    data to the Google Cloud Platform. The contract ran for 15
(GCP) [19]. While each cloud may differ in their speciﬁc    months, from July 2022 to October 2023, at a ﬂat rate cost of
pricing structure, the cost of the individual services used by    $56,630.54 per month, which resulted in a subscription price
the client is usually published in an itemised and highly gran-    of around $1900 per day.
ular way, making it easier to develop future cost models for   The subscription model does not put a limit on usage once
commercial clouds. In this way, a client can choose from a     active, and ATLAS can use the available resources at any time
menu of services, which are charged or billed directly.           at any scale. For example, for 1 month the disk usage could
While the list price-based cost model is suitable for ad hoc    be 10 PB, and the next month 1 PB, or for 1 month ATLAS
or specialised short-term resource needs, it is likely to prove   may use 3000 cores, and the next month use 20,000 cores.
more costly for consistent, long-term usage of resources    This resource elasticity may be very useful for short-duration
compared to grid-based, general-purpose ofﬂine computing.    data-processing campaigns and is explored in dedicated tests.
However, most commercial cloud providers offer discounts   The TCO for the subscription model is the total price of
and credits for large-scale users, which has been previously    the contract for 15 months, $849,458, although there is a
explored by ATLAS with varying degrees of success. Such    clear caveat to be considered, namely that the negotiation
discounts and credits can signiﬁcantly reduce the cost com-    for any subsequent contract will likely examine the actual
pared to the list-price. Funding agencies can often negotiate    average usage during the previous contract. If a signiﬁcantly
even better deals. The list price-based cost model therefore    higher usage is observed than the initial estimate, it may be
provides a maximum ceiling for a TCO, but rarely reﬂects    the case that the monthly price may be higher in any subse-
the actual price paid for large-scale cloud services.            quent contract. A key part of the TCO evaluation is there-
The primary obstacle to using commercial clouds is usu-    fore to use the detailed usage breakdown provided by the
ally egress costs, which are network costs incurred when   GCP accounting, without applying the subscription model,
data is exported from the cloud resource, and may be pro-    to understand which site conﬁgurations produce the most sig-

                                  123

### Página PDF 4

2  Page 4 of 35                                                     Comput Softw Big Sci        (2025) 9:2


niﬁcant increase to the total cost according to the list-price,     sites, typically hosted by national universities and laborato-
and which particular services drive this increase.                  ries, provide disk storage that is used for data processing and
                                                             user analysis.
2.2 Total Cost of Ownership Methodology              When setting up an ATLAS site using GCP resources the
                                                                objective is to fully support all ATLAS production work-
As previously mentioned, this TCO evaluation is not trying to    ﬂows. This includes not only processing the RAW collision
directly compare the cost of running an ATLAS grid site with    data into reconstructed data (Analysis Object Data, AOD),
the costs associated with running ATLAS jobs in the Google    but also running all components of the multi-step Monte
Cloud. This is primarily for two reasons, as described above.    Carlo (MC) production workﬂow, such as Event Generation
Firstly, a signiﬁcant cost variation exists already among dif-   (EVNT), Full or Fast Simulation which produces simulated
ferent resources, and among different grid sites, which is at    detector interaction data (HITS), simulated detector output
least in part attributable to the variation in service costs, as    data (Raw Data Object, RDO) and reconstructed simulated
well as regional variation in labour costs for site administra-    data (AOD), as well as creating data and MC derived for-
tors.Secondly,relyingsolelyonabsolutenumbersforGoogle    mats (DAOD) for input to analysis (a process referred to as
Cloud costs may not provide meaningful insights, due to the   “Group Production”). Additional formats such as Derived
substantial inﬂuence of individual agreements and contracts,    Event Summary Data (DESD), which are tailored to the spe-
which include volume discounts that vary case by case and    ciﬁc needs of various subdetector and object reconstruction
over time.                                             and identiﬁcation performance groups, may also be produced
The focus of this TCO is therefore rather on gaining a com-    in data-processing campaigns. The site is also expected to
prehensive understanding of how to make the best use of such    handle user workloads, which can encompass a diverse range
a resource, including how the conﬁguration may differ from    of demands. Further details on ATLAS production workﬂows
a standard grid site. To accomplish this, the relative contri-    and data formats can be found elsewhere [21].
butions of various components within the cloud service to    In the ATLAS grid site setup, production tasks running
the TCO are analysed, including compute, storage, and net-   ATLAS jobs at various locations consolidate their outputs
work, across different operating models. By identifying the     at a designated site known as the nucleus. The nucleus is
dominant cost drivers and exploring effective cost control    chosen during task deﬁnition and can be either a Tier-1 site
mechanisms, it is possible to optimise resource allocation    or a substantial and reliable Tier-2 site. Considering its size
and management to maximise cost efﬁciency.               and expected performance, this responsibility could also be
In addition to hardware considerations, the invaluable contri-    anticipated from the ATLAS Google site and is also exam-
bution of dedicated personnel at the grid sites should not be    ined here.
overlooked. These individuals not only fulﬁl the role of sys-   The integration of compute at cloud-based sites with ATLAS
tem administrators but also play a vital part in maintaining    distributed computing  relies on Kubernetes [22], where
the middleware and the distributed computing infrastructure    the resource-facing component of PanDA, Harvester [23],
of the experiment, and in some cases contribute to federated     utilises the native job controller of the Kubernetes clusters
support services, including user-support, and areas such as    for submitting batch jobs to the PanDA queue associated with
R&D, outreach and education. Their expertise and involve-    the site [24,25]. ATLAS software is provided in the same way
ment are crucial to sustain a high efﬁciency and effective-    as at grid sites via CVMFS [26].
ness in the operation of the ATLAS computing infrastructure,   The access to Google storage was conﬁgured as a standard
more so if sites opt for using cloud computing resources at    Rucio Storage Element (RSE), as used by other WLCG stor-
scale.                                                  age systems abstracted via standard HTTP/WebDAV using
                                                                authorisation tokens based on the S3v4 format [27]. At the
                                                           lowest layer in the stack, the Davix [28] library implements
3 ATLAS Google Site Integration                   HTTP/WebDAV access to all storage systems used in the
                                        WLCG, and already supports chunked transport required by
The ATLAS data are distributed worldwide across data cen-    object stores, which are used by ATLAS for cloud-based
tres or sites, organised into Tiers with varying capacities and     sites [29]. Further signiﬁcant development was then required
responsibilities under the umbrella of the WLCG [3,4]. The    to make access to Google storage work, as described in the
single Tier-0 centre is CERN, and there are ten Tier-1 sites,    following.
connected via dedicated National Research and Education   The Rucio server was extended to allow only speciﬁc
Networks (NRENs) typically with between 10 and 100 Gbps,    accounts to access cloud storage and to generate cloud stor-
using the LHCOPN and LHCONE overlays [20]. The Tier-    age tokens ad hoc when listing replicas, a functionality that
1 sites provide both disk and tape storage and function as     is needed both by interactive command line interface users as
the perpetual archival of the collision data. Around 50 Tier-2    well as production and analysis jobs. It was also necessary to

123

### Página PDF 5

Comput Softw Big Sci        (2025) 9:2                                                           Page 5 of 35    2


extendthefunctionalityoftheRucioclientstoallowseamless   4 Running the ATLAS Google Site
upload/download for object stores, as object stores prohibit
several useful functions from the HTTP/WebDAV standard    4.1 Initial Phase
that Rucio uses to ensure safe uploads such as checksum ver-
iﬁcation. The CERN File Transfer Service (FTS) [30] was   The ATLAS Google site was initially conﬁgured with a
also extended to dynamically generate authorisation tokens   PanDA queue able to run up to 5000 CPU slots, together with
based on the S3v4 format when enacting a transfer.            a single RSE where data ﬁles could be stored. The PanDA
Making the Google storage available within the WLCG    queue could be conﬁgured to accept certain types of jobs and
infrastructurealsorequiredacreativeauthenticationsolution,    the initial goal was to try to increase the number of different
as Google is not part of the Interoperable Global Trust Feder-    workloads and eventually test all the job workﬂows at the
ation (IGTF) [31]. To do this, a dedicated load-balancer was     site. Figure1 displays various metrics of the ATLAS Google
set up on the Google Cloud side with a fake hostname in the     site during the ﬁrst 6 months of running.
CERN DNS server such that a CERN-based X.509 host cer-   The number of running jobs is shown in Fig. 1a. Aside
tiﬁcate could be issued and uploaded. This load-balancer was    from alternating the number of CPU slots between ﬁve
conﬁgured based on path-based regular expressions, which    and ten thousand, the conﬁguration of the site was essen-
allowed two RSEs to be deployed: a DATADISK to store     tially unchanged during this period. The number of different
production input and output data and a SCRATCHDISK to    types of job running in the PanDA queue was progressively
temporarily store analysis job outputs. With this setup, the    increased by changing the brokerage decisions to adjust the
Google storage could be globally integrated into the ATLAS    job mix of the PanDA queue. The thin spikes that can be
distributed computing infrastructure like any other WLCG    seen in the number of running jobs are due to short-term site
site, and could be used by any account with the appropriate    conﬁguration changes.
permissions.                                                 In the 3 months from August 24th until November 24th 2022,
Due to the proximity to CERN and the low carbon-intensive    the overall job mix that was run corresponded to approxi-
energy usage in the region, the Google europe-west1 region    mately 30% MC Event Generation, 30% MC Full Simula-
in Belgium was chosen to host the primary ATLAS Google     tion, 30% MC Reconstruction and 10% Group Production,
site, although during investigations into the network connec-   which is a typical job mix seen on a standard grid site. Analy-
tivity a second site in the US Google us-east4 region in Vir-     sis workloads were not tested in this period as many changes
ginia was also employed (see “Cloud and Network Costs”    needed to be made to the ATLAS middleware.
(Sect. 4)). The number of running single-core slots (“job   As jobs continued to run at the site, the accumulated data
slots”) at the ATLAS Google site can be manually conﬁg-    from the various production steps steadily increased at the
ured, and is typically set to either 5000 or 10,000, although   Google RSE at a rate of approximately 50 TB per day, until
additional set-ups such as those used for the evaluation of      it reached 6 PB on November 24th as can be seen in Fig. 1b.
larger scale “bursts” were also deployed, as described in   At the same time, the availability of these data generated an
“Resource Bursting” (Sect. 4.1). CPU cores are provided    increasing number of accesses from other ATLAS sites. The
as “spot instances” [32], so that allocated resources may be    egress network trafﬁc from the ATLAS Google site due to
preempted at any time depending on current situation at the    production and analysis jobs elsewhere using data at Google
cloud, but have the advantage of costing signiﬁcantly less in    as input ramped up from an average of about 20 TB per day
real terms. The storage limit at the ATLAS Google site is    in August to about 130 TB per day in October and November.
initially conﬁgured to be between 2 and 5 PB.                 In November, there were periods with egress network trafﬁc
Thanks to the development of support for cloud-native inter-   over200TBperdayforseveraldaysinarow,ascanbeseenin
faces, the deployment of an ATLAS site in the Google Cloud    Fig. 1c. It is worth noting that this trafﬁc is above the average
capable of scaling to tens of thousands of CPUs and several    seen at ATLAS sites, relative to the stored data volume. The
petabytes of disk could be accomplished within a matter of   ATLAS Google site was generating egress trafﬁc at the level
weeks. Moreover, the operation and maintenance of the site    of 4 PB per month in November whilst hosting 5–6 PB data,
has required only a fraction of a full-time equivalent (FTE)   which is signiﬁcantly more than the initial estimate of 0.7 PB.
staff with expertise in cloud administration. This achieve-   By comparison, the MWT2 grid site in the US also generates
ment paves the way for exploring cost–beneﬁt scenarios in    an average of 4 PB per month of egress trafﬁc, whilst hosting
which the agility and scalability of cloud computing can be   more than 15 PB of data.
harnessed to accelerate the ATLAS science programme.       Fig.1d shows the breakdown of the Google list-price cost per
                                                                   service, where the various contributions from compute, stor-
                                                       age and egress are presented. It can clearly be seen that the
                                                                costs of egress trafﬁc and storage can quickly become dom-
                                                                inant in cloud resources. To contain these costs, on Novem-

                                  123

### Página PDF 6

2  Page 6 of 35                                                     Comput Softw Big Sci        (2025) 9:2


Fig. 1 Monitoring plots for the ﬁrst 6 months of running at the ATLAS     (blue), HITS (purple) and DAOD (yellow). c The daily egress trafﬁc
Google site, from July to December 2022. a The number of running     out of the ATLAS Google site, split into the various destination sites. d
jobs at the Google site. b The accumulated data at the Google RSE    The monthly list-price cost per service from the Google billing console,
split into different formats, the main ones being AOD (green), RDO    where the six main components are shown in the legend


123

### Página PDF 7

Comput Softw Big Sci        (2025) 9:2                                                           Page 7 of 35    2


Fig. 2 Data stored (blue) and egressed for job inputs (red) at the ATLAS Google site per month from July 2022 to September 2023. The ratio is
also indicated by the black line


ber 25th the conﬁguration of the ATLAS Google site RSE    cycle is usually done on a longer time scale. This is in part
was changed in Rucio by enabling greedy deletion, so that    because the administration domain for networks is typically
data were deleted as soon as the corresponding replication    broader and often spans national or continental institutions
rules had expired [33]. This had the immediate effect that the    beyond the sites themselves. This has probably had an effect
5.5 PB of accumulated cached data were quickly removed,    in the experiment computing models, whose workﬂows rely
and from then on new temporary data would stay on the RSE    to some extent on a plentiful any-to-any connectivity.
for only 1 or 2 weeks. This drastically reduced the egress   The long-term large-scale test of the ATLAS Google site
trafﬁc, since before the change there was signiﬁcant egress    has provided useful insights into the management of the
as the cached data were being transferred multiple times to    associated network trafﬁc. Given that the site was newly
other sites as job inputs.                                     deployed, it was possible to monitor how the consumption
After this change, the remaining egress was mainly due to job    of different types of resources evolved. CPU usage was con-
output being sent to the task nucleus. Another change was     stant as expected, as a ﬁxed conﬁguration parameter, whereas
then applied to the Google RSE on December 8th that set the    storage usage increased at an essentially constant rate. The
distance [34] of the RSE to any other ATLAS site to a very    steady increase in egress network trafﬁc was correlated with
large value. This had the effect of completely eliminating the    increased use of storage, albeit with a much larger variabil-
remaining egress trafﬁc due to job inputs then preferentially      ity. An interesting outcome of this ﬁrst period of the ATLAS
being read from other sites. The number of CPU slots at   Google site was that it was possible to reduce the egress net-
the ATLAS Google site was also reduced back to 5000. The   work trafﬁc by adjusting a few parameters in Rucio, allowing
effect of these changes can be seen in the distributions in    the cost of cloud resources to be very effectively controlled.
Fig. 1.                                A key question remains about how useful a grid site is with
With this new conﬁguration, the stored data at the Google    limited egress network trafﬁc. Whilst this question is beyond
RSE stayed around 300 TB and egress trafﬁc fell below    the scope of this report, it is an important topic that deserves
5–10 TB per day. The solitary spike in transfer volume in    dedicated studies in the future in the context of computing
December visible in Fig. 1c is from the egress of the outputs   model evolution. The approach taken here is to quantify the
of a small data reprocessing running at the ATLAS Google     tests that were done with the ATLAS Google site. As pre-
site, visible as the yellow contribution in Fig. 1a.               viously described, after the ﬁrst 3–4 months of continuous
                                                          unattended operations, the site had accumulated 6 PB of data
                                                   on disk. The values for average stored data and total egress
4.2 First Observations on Network Considerations
                                                             of data for job inputs are depicted in Fig. 2. Remarkably,
                                                      between September and December 2022, between 75% and
Cloud resources have well-deﬁned price structures for each
                                            100% of all the data at the site was egressed each month
resource type, not only compute and storage, but also net-
                                                                  for production or analysis job inputs. Comparing this with
work trafﬁc. The ﬁrst two are the usual capacity metrics
                                                              other large ATLAS sites, typically having storage sizes rang-
that are closely accounted for in a distributed infrastructure
                                                            ing from 4 to 30 PB, this metric falls to between 15% and
like the WLCG. The network capacity is certainly also con-
                                                 20%. Consequently, the signiﬁcant amount of new data at the
sidered within WLCG, but the planning and provisioning

                                  123

### Página PDF 8

2  Page 8 of 35                                                     Comput Softw Big Sci        (2025) 9:2


Fig. 3 a The variation of workﬂows running at the ATLAS Google site     billing console for the period from January to April. The dominant ser-
from January to April 2023 featuring several periods of running with a     vices are compute CPU/RAM (blue/red), local storage on the worker
single workﬂow. The contribution from user analysis jobs can be seen    nodes (orange), cloud storage (purple) and network egress (green and
from March. b The daily list-price cost per service from the Google     turquoise)


ATLAS Google site generated data movement dynamics that    jobs in mid-February and a 6-day period of only MC Event
signiﬁcantly deviated from the average. This is relevant when    Generation jobs at the beginning of April.
evaluating a cloud resource, since abnormally high egress   The Google billing console provides daily list-price cost
trafﬁc levels will have an impact on costs.                     information, shown in Fig.3b, which can be used to infer
                                                             general trends. It was observed that 80–90% of the cost is
                                                                consistently dominated by three services: compute, storage
                                                     and network egress. The remainder comes from a combi-4.3 Understanding the Cost Impact of Different ATLAS
                                                             nation of infrastructure overhead and costs associated with   Workﬂows
                                                           orthogonal ATLAS R&D activities at Google. The compute
                                                                cost (which has three components associated with it: CPU,Between January and April 2023 the ATLAS Google site
                                  RAM and local disk) remains pretty much constant through-ran at an approximately constant CPU capacity of around
                                                            out this period, as expected from the fact that the number of5000 job slots. The types of jobs allowed to run were con-
                                                                      slots in the ATLAS Google site was set to 5000 job slots andtrolled through the fairshare policy parameter associated with
                                                            not modiﬁed. This cost is consistent with the advertised pric-the PanDA queue. By adjusting this parameter, four periods
                                                            ing for the spot n2-standard-8 instances of around $0.01 perof running only one activity were carried out, as shown in
                                                   CPU-h. This situation can be compared to the ﬁrst monthsFig. 3a: a 14-day period with only MC Simulation jobs in
                                                             of the project, where egress costs dominated, as shown inJanuary, a 5-day period with only MC Reconstruction jobs
                                                             Fig.1d.in early February, a 9-day period with only Group Production

123

### Página PDF 9

Comput Softw Big Sci        (2025) 9:2                                                           Page 9 of 35    2


Compute is the dominant cost for these four workﬂows. Stor-    period, the storage is seen to contribute a signiﬁcant fraction
age and network costs for a given day are partially but not    of the total cost at 30%; however this is from the replication
fully correlated with the activity that is running at that time.    of almost 1 PB of DAOD data sets to the Google site done
If data are not purged from the storage, the storage costs will    during the same week. The most striking observation is that
reﬂect the accumulation of any past activity. On the other    the period of Data Reprocessing activity shows a very differ-
hand, if there are old data stored at the site that are accessed    ent pattern compared to the others, with the network egress
from outside for any reason, this will generate egress costs    cost clearly dominating and averaging 63% of the total cost.
that are not correlated with the activity running at that pre-   The relative costs of different workﬂows are further exam-
cise moment. Still, the single workﬂow testing periods were    ined in “Cloud and Network Costs” (Sect. 5) when discussing
of relatively short duration and the Rucio storage conﬁgu-    networks.
ration meant that no background egress was present, so any    User analysis workﬂows have also been running on the
correlation observed should be meaningful.             ATLAS Google site since March 2023, as can be seen in
A ﬁnal, signiﬁcant single workﬂow test was done in July    Fig. 3a. Whilst it would have been desirable to run only
2023, by running a fraction of the reprocessing of the 2022    user analysis at the ATLAS Google site for some period, this
data on 10,000 job slots at the ATLAS Google site. About    proved difﬁcult, primarily due to the unpredictable nature of
15% of the proton–proton collision data recorded in 2022    such workﬂows, compared to the rather standard production
for physics analysis, comprising around 600M events, were   workﬂows employed in the single job type periods described
processed into multiple formats for analysis and further, sec-    in this section. Despite replicating several popular analysis
ondary processing between July 11th and 18th. The data    datasets to the site, it was difﬁcult to get enough user jobs in
carousel mechanism [35] was employed as done for the grid,    the queue, and ultimately it was not possible to run only anal-
whereby input ﬁles, in this case RAW data, were recalled    ysis workﬂows on the site, although this was almost achieved
from ATLAS tape resources and replicated to the Google    in the second half of March.
site, without observing any adverse effects.
Fig.4a shows the data reprocessing jobs during the period    4.4 Resource Bursting
July 11th to July 18th, as well as a small number of associ-
ated output data merging jobs. Further data reprocessing jobs   Cloud computing is intrinsically highly elastic in its nature,
can be seen in Fig. 4a after July 18th, which are part of the    and offers the opportunity to acquire a signiﬁcant number of
wider campaign to reprocess the remaining 85% of the 2022    additional resources, potentiallyat short notice. Inthecontext
data on all ATLAS distributed computing sites, including the    of Active Learning [36] this is particularly advantageous,
ATLAS Google site. Figure4b shows the daily data volume   when it is essential to increase the speed of each iteration
transferred out of the ATLAS Google site to the various grid    of MC sample production. Previous studies [25] have shown
sites, where it can be seen that during the data reprocessing     that it is possible to quickly ramp up many tens of thousands
a total of about 100 TB of data were exported daily.            of job slots at Google and process a small number of MC
Fig.4c also shows the daily data volume transferred, but now    events through all steps in the MC production chain to arrive
broken down into the different activities. Production Output     at the DAOD used for analysis.
(cyan) accounts for approximately half of the egress, which    Bursting a large amount of additional compute capacity
is equivalent to the export to CERN shown as the purple   may also be useful if for example a particular MC sample
component in Fig. 4b. Most of the remaining egress during     is urgently required, and this scenario was explored at the
this period is attributable to Data Consolidation, which is a   ATLAS Google site in June 2023. In this case a 50M event
rebalancing procedure performed on the ATLAS distributed    standard top-quark pair production MC sample was chosen
computing system as a whole. It may be interpreted as other    to undergo Full Simulation as quickly as possible, by burst-
data moved out of the Google storage to make room for the    ing to 100,000 job slots. The task was conﬁgured as standard
output of the data reprocessing. The egress from the data   2000 event 8-core jobs, which each take on average between
reprocessing jobs after July 18th is also visible in Fig. 4b and    6–8h, so that all 50M events should be processed within 24h.
c, albeit at a lower level.                               The input EVNT data was replicated to the Google storage
The periods with different types of activities show differ-    and the site was drained of all other running jobs before start-
ent trends on the relative cost of the three main services, as    ing the test. Whilst this was not strictly required, it allowed
shown in Table 1. The average values for the full duration    the burst of resources to be isolated, which was useful for
of the project are also displayed. For the ﬁrst four columns,    monitoring purposes.
a few trends are visible in the numbers in the table. In the   The results of the burst test are shown in Fig. 5. The ramp up
Group Production period, the egress network activity and its    to 100,000 running job slots was achieved in 1–2h without
associated costs show a clear increase, averaging 21% over     issue, as can be seen in Fig. 5a. Wall-clock consumption is
the 9-day testing period. In the 6-day MC Event Generation   shown in Fig. 5b, which revealed a considerable amount of

                                  123

### Página PDF 10

2  Page 10 of 35                                                    Comput Softw Big Sci        (2025) 9:2


Table 1  Relative cost of each of the main services during periods of     Generation and Data Reprocessing. The ﬁnal column shows the average
time when only one workﬂow was running at the ATLAS Google Site:     values for the full duration of the project, from July 2022 to September
MC Full Simulation, MC Reconstruction, Group Production, MC Event    2023

            MC Full      MC               Group        MC Event         Data                 Full
                      Simulation         Reconstruction        Production         Generation         Reprocessing        Project
                     06/01–19/01       05/02–09/02          11/02–19/02       07/04–12/04       12/07–16/07        07/22–09/23

Compute          73%           65%            52%           47%           21%           28%

Storage           10%           10%           9%            32%           11%           20%

Network egress     7%            11%            26%          3%            63%           46%

Other            10%           14%            14%           19%          4%           6%


lost wall-time in the ramp up phase. This was due to nodes   was increased from 2.5 PB to 5 PB. At this time, the site was
accepting jobs while CVMFS was still being initialised, and    also reconﬁgured as a nucleus, so that not only unique data
hence the burst test was repeated with a slower ramp up pro-    could be stored there but the site could also act as the output
ﬁle. In both cases, the overall lost wall-time was 11–13%,    destination for a task running jobs at all other ATLAS grid
somewhat more than observed on the grid, and coming from     sites. Furthermore, the large distances to other RSEs set in
the ramp up phase and the low and constant level of preemp-    an earlier phase of the project were somewhat reduced, in
tions throughout both tests. Nevertheless, in both cases all    particular to the German Tier-1 and associated Tier-2sites,
50M events were processed within 24h as expected.         which are geographically close to the ATLAS Google site
The same MC Full Simulation sample has been processed    in Belgium. Figure6 shows the changes to the data stored
several times on the various resources currently employed    and the transfers out during the month following these site
by ATLAS, without draining queues or using a dedicated    reconﬁgurations.
site or queue. Each of these tasks took between 8 and 10    Fig.6a shows the data stored at the ATLAS Google site,
days to process, even when a signiﬁcant fraction of the work,    grouped into three different replica types: Persistent, which
between 30% and 75%, was executed on a few powerful sites    has a Rucio rule with no lifetime (typically data placed at
such as the ATLAS High Level Trigger Farm [37,38] when    the site); Temporary, which has a Rucio rule with a lifetime
used in Sim@P1 [39,40] conﬁguration or the Vega [41] and    (typically data replicated to the site via PanDA for produc-
NERSC-Perlmutter [42] HPCs. In this sense, the burst test    tion jobs, with a lifetime of 2 weeks) and Cached, which is
can be considered a success, whilst at the same time having    data with no current Rucio rule and therefore may be deleted
the advantage of exposing the cost of a well-deﬁned data-     at any time. The main consequence of the site changes was,
processing activity. The list-price cost of each burst run at    as expected, an increase in the Cached data as a result of
the ATLAS Google site can be seen in Fig.5c, where the    the increased space available for output data from produc-
sum of the compute-based components is around $23,000    tion tasks running at the site. The volume of Persistent and
each time.                                            Temporary data remains roughly constant.
                                                 The variety of data types stored at the ATLAS Google site
                                                           during this period can be seen in Fig. 6b, where a marked
4.5 Scaling Up the Site Again                                                        increaseinRDOﬁlesisvisible.Thesedataareusedasinputto
                                 MC Reconstruction tasks in combination with HITS, which
For the ﬁnal few weeks of the current project, the size of                                                                             is the output of MC Simulation. It is likely that the nucleus
the ATLAS Google site was scaled up again to between the                                                             nature of the site, in combination with the reduced distances,
size of an ATLAS Tier-1 and Tier-2 grid site, with around                                                  means that more HITS datasets remain on the RSE and are
5 PB of storage and 10,000 running jobs slots, utilised by all                                                                 available as favourable input for MC Reconstruction tasks,
job types. This was done in July 2023, ahead of launching                                                          both at the ATLAS Google site and elsewhere. A steady
the data reprocessing single workﬂow period described in                                                               increase in HITS and AOD (the output of MC Reconstruc-
“Understanding the Cost Impact of Different ATLAS Work-                                                                    tion) is also observed as well as the presence of some RAW
ﬂows” (Sect. 4.3), and this conﬁguration remained until the                                                             data ﬁles used as input to data reprocessing tasks.
end of the project in September. The 15 largest Tier-2 grid                                                          Fig.6c shows the daily transfers out of the ATLAS Google
sites and about half of the Tier-1 sites typically each pro-                                                                              site, which show a steady increase after the end of July. Most
vide at least this number of job slots to ATLAS computing.                                                             of the egress is due to ﬁles replicated from the site to use as
Almost all of the Tier-1 sites and the ten largest Tier-2 sites                                                           production input elsewhere, for example AODs to be used
have at least 5 PB allocated to their DATADISKs, so at the                                                             as input for the production of analysis-level data (DAOD)
end of July the size of the ATLAS Google Site DATADISK

123

### Página PDF 11

Comput Softw Big Sci        (2025) 9:2                                                          Page 11 of 35    2


Fig. 4  Distributions covering the data reprocessing campaign per-     period to different grid sites, where the main contribution in dark purple
formed on the Google ATLAS site. a Number of running jobs, where      is the replication of the reprocessing output data to CERN. This is also
the single job type period from July 11th to July 18th shows the data     visible for the data reprocessing jobs after July 18th. c The different
jobs in yellow, together with a small number of associated merge jobs     types of transfers out of the ATLAS Google site for the same period
in blue. b The data transfers out of the ATLAS Google site for the same


at another ATLAS grid site. The level of egress is however    ﬁrst activated. At the beginning of the project, the RSE was
signiﬁcantly less than in 2022, which at its peak had a rate   empty and all data were newly written there, whereas in July
of more than 1 PB per week (see Fig. 1c). This reduction is   2023 there was already around 2 PB stored there before the
likely due to two main reasons. Firstly, compared to 2022,     site was scaled up again.
the short distances set in Rucio between RSEs were limited    Decommissioning of the ATLAS Google site took place in
to only the sites in the German cloud. Secondly, there was a    September 2023, so that all resources employed during the
higher fraction of new data at the Google RSE when it was    project were effectively switched off from the holistic per-

                                  123

### Página PDF 12

2  Page 12 of 35                                                    Comput Softw Big Sci        (2025) 9:2


Fig. 5  Distributions covering the resource burst tests done at the     ning on the Google site. c The daily list-price cost per service from the
ATLAS Google site in June 2023. a The running jobs of the two bursts    Google billing console, where the compute contributions are seen to
of MC Full Simulation. b The wall-clock consumption of the jobs run-    dominate on the burst days


spective of ATLAS distributed computing. The PanDA queue   5 Cloud and Network Costs
was disabled mid-September and all unique data moved to
one of the ATLAS Tier-1 sites. Any remaining user data from    Deploying grid resources in commercial clouds creates a
R&D projects were removed and the site was fully decom-   demand for networking services that can have an impact on
missioned by September 21st. No signiﬁcant difﬁculties were    performance and potentially also on cost. Egress trafﬁc is a
encountered during this process, which was similar to the    particularly expensive resource in the cloud, due in part to the
usual decommissioning of a typical ATLAS grid site.         commercial strategy of providers to incentivise to continue to
                                                          use their resources and not migrate to other cloud providers.
                                                   At the time of writing, the list-price for storing data in the

123

### Página PDF 13

Comput Softw Big Sci        (2025) 9:2                                                          Page 13 of 35    2


Fig. 6 Data stored at the ATLAS Google site: a grouped into different replica types and b grouped into different ATLAS data formats. c The
different types of daily transfers out of the ATLAS Google site


Google europe-west1 region is $20 per TB per month [43],    depending on the activity of the site. Figure7a shows the
while the price for egressing data is between $45 and $85 per    monthly list-price cost proﬁle for the full 15-month duration
TB, depending on the volume [44].                            of the project. The cost of compute is basically stable, only
As previously described, probably the most important feature    showing small variations at the times when the number of
of the cloud resources is that the costs involved are heavily    running job slots at the sites was changed (for example when
dependent on which services are used. This dependence can    the site was increased from ﬁve to ten thousand job slots
be seen in the cost breakdown of running the ATLAS Google    from August to November 2022, and the CPU burst test in
site, which varied signiﬁcantly month to month, or day to day,


                                  123

### Página PDF 14

2  Page 14 of 35                                                    Comput Softw Big Sci        (2025) 9:2


Fig. 7 Cost breakdown for the ATLAS Google site for the period July 2022 to September 2023. a The monthly list-price cost per service from the
Google billing console. b The percentage contribution to the monthly cost from each of the services grouped as indicated in the legend


June 2023). However, the cost of storage and network egress      if some data at the site become popular and are suddenly
varies considerably, depending on the dominant activity.       accessed by thousands of jobs at other sites. Moreover, the
Fig.7b shows the relative fraction of each service to the total    data going from the ATLAS Google site to other ATLAS grid
monthlycost.Fortheﬁrstmonthsoftheproject,untilNovem-     sites do so through the general purpose internet, as opposed
ber 2022, the egress cost increased as new data accumulated    to using the LHCONE/LHCOPN private networks that link
at the site and jobs running at other grid sites accessed these    most of the ATLAS sites. This has the effect of generat-
data. By November 2022, the costs associated with egress    ing potentially very large trafﬁc over the internet link into
reached 54% of the monthly total. Other patterns can be    the destination sites, which can have cost implications at the
observed in 2023, such as in April and May when the analysis    destination, since some sites have higher costs or lower avail-
input data was replicated to the ATLAS Google site, corre-    able bandwidth associated with their general purpose inter-
spondingly increasing the fraction of the total cost spent on    net links compared to the dedicated LHCONE links. The
storage. The increase in egress due to the data reprocessing     utilisation of such links can lead to operational disruptions,
performed at Google is also visible in July.                      potentially impacting a site’s availability to its users. This is
                                                              often due to lower provisioning of general internet bandwidth
                                                   by the sites, primarily stemming from the associated higher5.1 Dedicated Networks
                                                                    costs, resulting in rapid saturation. It is therefore important
                                                                  to investigate mechanisms that could control and potentiallyEgress network trafﬁc is the resource that can have the largest
                                                          reduce the egress costs. One such mechanism is dedicatedimpact on the running costs over short timescales. It is an
                                                       network links with the cloud providers.expensive resource, and its use can increase very rapidly

123

### Página PDF 15

Comput Softw Big Sci        (2025) 9:2                                                          Page 15 of 35    2


The price for sending trafﬁc through a dedicated link [45]   6 Feedback from Grid Site Administrators
has two components: a ﬁxed one of the order of $2.4 per
hour for a 10 Gbps circuit for instance, plus a variable one   As part of this study, feedback was collected from several
that depends on trafﬁc, priced at $20 per TB. Additional    system administrators representing various ATLAS Tier-1
costs might also arise, depending on the speciﬁc service    grid sites. In particular, their experiences with commercial
provider and route of the intermediate connection. Accord-    clouds were discussed, to gain some insights into the primary
ing to this, routing the trafﬁc exiting the ATLAS Google    advantages and drawbacks associated with these services.
site through a dedicated link could potentially reduce the
egress costs to less than half if trafﬁc above 3 PB per month    6.1 Concerns Related to Cloud Computing and
is generated. A recent study within the IceCube Collabora-       Comparisons to this Project
tion [46] came to a similar conclusion, where by employing
dedicated network links the egress costs for data-intensive      It was a common view among site administrators that cloud
applications could be reduced by between 50% and 75%. It     is more expensive than on-premises solutions. In particular,
is however worth emphasising that the scope of the study    concerns were raised about high egress costs, which can sig-
undertaken by IceCube signiﬁcantly differs from that of    niﬁcantly impact the overall expenses. Some of these com-
ATLAS. IceCube utilised dedicated links connecting the    parisons may have been made against dedicated compute
cloud to a speciﬁc site at UW-Madison, whereas ATLAS    instances rather than spot instances, which have a higher cost.
is currently investigating the feasibility of deploying dedi-    Past experiences [7] with spot instances revealed eviction
cated links to establish connections between cloud resources     rates of up to 15%, which administrators considered unac-
and the LHCONE overlay network, facilitating data trans-    ceptably high. This issue becomes particularly critical since
fers to numerous sites worldwide. It is therefore important   many sites support multiple users beyond LHC activities,
to recognise that the complexity and potentially the cost    and these users might be less tolerant to evictions than the
associated with these two approaches may differ consider-   LHC experiments, affecting the overall service reliability.
ably.                                                  During this project preemption was observed to be signiﬁ-
To explore this option, an engagement has been started with    cantly lower, where only around 20% of all failed jobs were
ESnet [47] to provision a dedicated 10 Gbps link to the    due to evictions. With an overall rate of 5% lost wall-clock
Google us-east4 cloud through their ESnet Cloud Connect    from failed jobs over the duration of the project, the result-
service. The aim of this exercise is to test two things: ﬁrst,    ing eviction rate of between 1–2% compares favourably to
to measure and conﬁrm a reduction of the egress costs for    the previous result described above. However, it is important
large data transfers, and second, to try to route the egress    to note that eviction rates for spot instances can vary based
trafﬁc from the ATLAS Google site into LHCONE to avoid   on several factors, including the time of the year, the cloud
downstream costs associated to high-volume trafﬁc through    provider, the geographical region, the volume, and the types
the regular internet links at receiving sites.                     of resources utilised.
The expectation is that dedicated network links will provide    Worries were also expressed about unpredictable perfor-
a way to lower the networking costs, but at the same time they   mance variations over time in cloud environments. Adminis-
will also add complexity to the deployment and operations     trators were concerned that cloud providers might change the
of the cloud resources. Moreover, besides the technical com-    underlying hardware behind a speciﬁc instance type, leading
plexity of provisioning the dedicated network links, there is    to potential performance ﬂuctuations that could affect the
also an organisational complexity that arises from the fact    quality of services. The PanDA queue associated with the
that the implementation of this setup will vary depending on   ATLAS Google site was very stable, experiencing negligible
the combination of cloud provider (and even region inside   downtime throughout the duration of the project. While some
a provider) and NREN that provides the peering. In differ-    cloud providers do not specify the exact provided CPU mod-
ent countries, NRENs will have different capabilities and     els, within CPU families it is possible to deﬁne a preference
conditions for peering with cloud providers. Furthermore,    for the newer generations. The masked CPU values (publish-
each cloud provider likely offers their own speciﬁc tools to    ing clock frequency and cache size) collected by the work-
deploy and manage the dedicated links, each with very differ-    load management system were homogeneous throughout the
ent provisioningprocedures. Another considerationwouldbe    duration of the project, indicating a stable performance. The
if multiple experiments, for example ATLAS and CMS, were    adoption of the new, more ﬂexible HEPScore [48] bench-
to provision resources from the same cloud provider whether    marking model should provide further information about this
they could both use the same dedicated network link. There is    topic in the near future.
clearly a signiﬁcant programme of work in this area, beyond    Site administrators expressed a general concern about the
the time frame of the current AGP.                               risks associated with vendor lock-in. They emphasised the
                                                         importance of maintaining ﬂexibility and the  ability to

                                  123

### Página PDF 16

2  Page 16 of 35                                                    Comput Softw Big Sci        (2025) 9:2


migrate between different cloud providers to avoid being    ness [50] and provide dynamic information about the car-
tied to a single vendor and potentially facing challenges   bon  intensity of  their  regions, enabling  users  to  steer
with cost escalation, integration or data portability. The solu-     their load to minimise emissions. In particular, the site
tions implemented by this project to interface Google Cloud     utilised by this project, europe-west1, has one of the low-
resources are essentially cloud-agnostic, not only avoiding     est grid carbon intensities [51] among Google data cen-
vendor lock-in, but also potentially enabling access to other     tres.
commercial cloud resources, as demonstrated at a lower scale
at AWS [18].                                                 6.2 Purchasing Procedures
Dataownershipandcontrolweresigniﬁcantworries.Another
concern was about having critical data solely stored in the    Public institutions, including those operating grid sites, often
cloud, without having direct control over the physical infras-    encounter the requirement to procure services through public
tructurewherethedataishosted.Ensuringdigitalsovereignty    tendering processes. However, when it comes to large-scale
is seen as crucial when handling data from unique scien-    purchasing of cloud services, the administrative demands
tiﬁc experiments. The Google Cloud data access policy is    involved can be quite difﬁcult. In response to this challenge,
clearly and strictly deﬁned [49], and user data is fully pro-    the OCRE [52] project was initiated in 2019 with the aim of
tected and accessible only to the customer cloud adminis-    streamlining the procurement process for cloud services in
trators, designated users, and contract managers. Ultimately,    Europe.
ATLASretainsdata(andalgorithm)ownershipwhenrunning    For organisations contracting cloud services within Europe
in the Google Cloud. In addition, an assurance on privacy is    today, utilising a framework like OCRE becomes a viable
made that customer data will not be used for any commercial    option to do their purchasing. OCRE facilitates this purchas-
use or for training purposes. A further, related point of con-    ing process through NRENs, which in turn maintain lists
cern is that as cloud resources are essentially leased, there    of country-speciﬁc authorised resellers that offer cloud ser-
is no opportunity to ensure that the hardware is responsi-    vices covered under the OCRE framework agreements. One
bly and sustainably deployed to its maximum capability and    of the key beneﬁts provided by OCRE is the provision-
longevity.                                                   ing of a standardised contract. While this contract serves
According to the feedback gathered from one site adminis-    as a baseline, further negotiations at the country or site
trator, the cost breakdown of operating a grid site generally    level are possible. These negotiations could lead to larger
comprises approximately one-third for personnel, one-third   volume discounts, ultimately beneﬁting the organisations
for operational expenses, and one-third for hardware invest-    involved.
ments. The technical personnel effort required to operate one    Whilst OCRE is available for institutions within Europe,
of the ATLAS Tier-1 centres is estimated to be around 10      it is not applicable in countries other than the 40 mem-
FTEs. Some site administrators hold the view that even with    bers of the framework. The process for contracting cloud
a substantial migration of resources to the cloud, the essen-    services in the USA, for example via HEPCloud [53] or
tial operational effort needed to run a site would not expe-   CloudBank [54], or in Asia may be completely different
rience a signiﬁcant reduction. This is because only a lim-    and may result in different pricing conditions compared to
ited number of hardware-oriented technical positions may    those in Europe. It is crucial to recognise that the landscape
no longer be required. However, some issues arise that make    for cloud service procurement can vary between regions,
this comparison inherently challenging. The experience of    necessitating tailored approaches based on the speciﬁc reg-
the Google site primarily focuses on the operational effort    ulatory and contractual requirements of each region.  If
required to provide CPU and storage at scale for a single    multiple sites were to buy into the same cloud provider,
experiment. In contrast, the roles and responsibilities of tech-   some of these differences could be overcome, although
nical personnel at on-premises sites may be much broader in    remaining administrative hurdles would need to be clari-
scope.                                                     ﬁed.
Finally, site administrators emphasised that funding agen-    For international organisations like ATLAS seeking to imple-
cies are making substantial investments in building new,   ment a coherent strategy for utilising cloud services, the vary-
energy-efﬁcient data centres, which does not indicate a trend    ingregulationsandprocurementprocessesacrossregionsadd
or incentive to increase the utilisation of cloud resources.    complexity to the management and planning efforts. Flexi-
In this context, Google cloud resources operate with net-     bility and adaptability become essential for navigating the
zero operational greenhouse gas emissions by neutralis-    diverse cloud landscapes and effectively leveraging cloud
ing any remainder via investing in carbon offsets. Google    resources across different geographical areas.
data centres have above average Power Usage Effective-


123

### Página PDF 17

Comput Softw Big Sci        (2025) 9:2                                                          Page 17 of 35    2


7 Further Investigations and Future Work               would involve for example only storing data in the cloud that
                                                                             is currently in use, which is rather different to the current
There are several areas that would beneﬁt from an extension    grid storage model. In this way, the complexity of a hetero-
of the ATLAS Google Project, to allow further exploration    geneous infrastructure setup reduces the egress volume, but
of employing commercial cloud resources for ATLAS.             still allows bursting to cloud compute with large data inputs.
Firstly, this could involve further investigation of the ATLAS    Alternatively, the necessary capabilities to exploit cloud stor-
Google Site, evaluating the typical grid site conﬁguration    age and network features such as bucket-level copy could
but at a lower level of resources than deployed at the end    be developed, to facilitate internal transfers between differ-
of this project cycle. As discussed in “Scaling Up the Site    ent cloud regions. This would remove the need to egress
Again” (Sect. 4.5), whilst the egress is more under control    the data via FTS, which incurs the usual associated transfer
it is nevertheless still signiﬁcant, so a more detailed evalua-     costs.
tion of which workﬂows are suitable for commercial cloud    Thirdly, beyond the ATLAS Google Site conﬁguration and
should be done, including any necessary, additional conﬁg-    network considerations, many areas of R&D were performed
uration changes. Understanding how the subscription agree-    as part of the AGP, using multiple services offered within the
ment structure works and what a reasonable discount looks   Google Cloud [59]. Most of these projects have taken advan-
like is also an important factor when considering workﬂow    tage of the elastic availability of special types of resources
restrictions, site structure adjustments or long-term contract    to ramp up and down ephemeral compute clusters using
costs. The impact of these studies could also be expanded to    for example GPUs, large amounts of memory, or ARM
potentially evolve the ATLAS workﬂow and data manage-   CPUs depending on the current need. This was done either
ment systems to take into account the cost of the network.     through the ATLAS PanDA workﬂow management system
Secondly, peering with commercial cloud networks would    or using interactive compute with Jupyter [60] notebooks and
be the main focus for further investigation, as this multi-   Dask [61] task scheduling.
faceted, time-intensive activity is only just beginning now.   The usage of such non-standard resources that are not eas-
The network costs incurred due to transfers via the inter-     ily available at standard WLCG grid sites has proven to be
net are a critical roadblock to widespread commercial cloud    extremely valuable and effective, helping to develop and
storage adoption for scientiﬁc computing overall and in    expedite new ATLAS data analysis techniques using machine
the case of the LHC experiments, transfers need to be    learning and the migration of the ATLAS software to ARM
routed through the LHCONE overlay to eliminate these   CPUs. Compact data formats with columnar data access have
costs for the WLCG sites. At the same time, data schedul-    been investigated using Google resources.
ing should be introduced to reduce the data volumes that   ATLAS plans to continue to take advantage of non-standard
incur transfer and storage costs. Widespread peering is nec-    resources like GPUs and ARM CPUs to work on innova-
essary to reduce the need to route via complicated paths.     tive and novel analysis and software techniques, accelerating
There are several NRENs in the US and EU, which should    the process to discoveries. Another larger focus area could
be approached to discuss the technical details of network    be the development of high-energy physics algorithms using
peering, for example ESnet [55], Internet2 [56], or GÉANT    tools not available before, such as Large Language Models
Network [57].                                         and Generative Artiﬁcial Intelligence. A continuation of the
There are various options in the Google Network stack to   AGP will facilitate these initiatives, providing proven access
support this activity, but at the same time the necessary    to such resources. Like the other activities proposed in this
Google documentation does not seem to be publicly avail-    section, they are not expected to be resource or cost intensive.
able. Detailed discussions would be needed between WLCG    There are several other topics of interest that might be inves-
and CERN IT network experts together with the correspond-    tigated during a continuation of the AGP. Running analysis
ing network experts from Google. If necessary, short-term    jobs at the ATLAS Google Site was only brieﬂy examined
Google premium support could be ﬁnanced once the peering    and this workﬂow, which is unique in its highly variable
options with the NRENs have been explored.                   nature, may warrant further scrutiny. In particular, actions
There is the potential need to develop new features in the    to replicate the most highly requested analysis-level data
Rucio [12], GFAL [58], Davix [28], and FTS [30] stack    samples were not measurably successful, requiring further
to support this R&D and ATLAS would continue to work    understanding of data popularity and data placement. Tak-
with the respective teams to discuss the objectives and mile-    ing running analysis on the Google Cloud further, the idea
stones, and to follow the implementation, deployment, and    of extending the resources of the ATLAS Google site with
operations. There are two distinct analyses and respective    user-speciﬁc Google credits has also been raised. Authen-
evolutions of the ATLAS computing model that could be     tication issues could also be interesting to look into, when
explored. One idea is to improve the necessary workﬂow and    considering using the site not only for ATLAS data, but also
data management policies when using cloud storage. This    for hosting Open Data, available to all. On the other hand,

                                  123

### Página PDF 18

2  Page 18 of 35                                                    Comput Softw Big Sci        (2025) 9:2


it may be worth investing some time in understanding the    Whilst it was also shown that it is possible to integrate, adjust
privacy implications of the data stored in commercial cloud    and expand associated storage at the cloud site, this is less
resources, which may contain protected information, at least     trivial than CPU as the intrinsic network costs must be taken
according to GDPR [62], and whether this must be taken into    into consideration. Storage and in particular network costs
consideration.                                                 are known to dominate the TCO of commercial clouds, so
The ATLAS Google Project has provided valuable insights   much so this often dissuades sites taking an active interest
into the use of commercial clouds, and there remain many    in employing such resources. The studies performed during
avenues of investigation that could be pursued. This next    the AGP and outlined in this TCO analysis have shown that
phase could feature a signiﬁcant reduction of resources    commercial cloud is a technically viable option for ATLAS
required, and hence ﬁnancial expense, as the focus shifts    distributed computing, albeit with additional costs not neces-
to network connectivity and continued R&D. The ATLAS     sarily considered when employing traditional grid resources.
Google site could nevertheless still continue, albeit at a lower    Within the WLCG model the cost of the network is some-
level, although if the network R&D is successful in reducing    times hidden, and whilst in reality this is probably rather
the egress cost, it could once again be ramped up to verify the    high and means to reduce it are worth investigating, it can
savings arising from the implementation of dedicated peering    also be considered as irreducible and somewhat independent
solutions.                                                    of ATLAS. Conversely, commercial cloud data transfers over
                                                            standard internet networks incur signiﬁcant costs for the data
                                                                  centres.
8 Summary                                       The TCO evaluation has shown that without the subscription
                                                        model, the cost of commercial cloud resources is signiﬁ-
While traditional, site-based resources have always formed    cantly increased. The Google Cloud resources used during
the backbone of ATLAS computing, commercial clouds may     this project cost a total of $3.162M at list-price compared
in some cases provide a viable and attractive alternative or    to the $849,458 paid via the subscription agreement, repre-
addition. Much experience was gained in the integration of    senting a discount of 73%. Alternatively, ATLAS used 3.72
the ATLAS Google site into ATLAS distributed computing    times more Google Cloud resources than were purchased via
and no signiﬁcant technical issue was discovered to prevent    the subscription agreement, which means the resources used
the experiment employing such resources in the future. Fur-    during this project would have been 272% more expensive at
thermore, the current workﬂow and data management tools     list-price. This is most obvious in the costs associated with
employed by ATLAS are shown to be adequate for apply-    the bursting test shown in Fig. 5c, which depicts daily expen-
ing changes to the site conﬁguration. The technical solutions    diture considerably in excess of the $1900 per day rate of the
implemented are essentially cloud-agnostic, not only avoid-    subscription agreement.
ing vendor lock-in, but also potentially enabling access to   As shown in Table 1, almost half of the total list-price costs
other commercial cloud resources. The subscription pricing    areduetoegress.Withthisinmind,theATLASCollaboration
model applied in this project has proven to be beneﬁcial to     is investigating ways to reduce this cost via dedicated net-
ATLAS, although questions remain how this may change   work solutions, as outlined in “Dedicated Networks” (Sect.
going forward.                                                      5.1). It was also shown that egress costs are workﬂow depen-
The project has shown that commercial cloud sites are an    dent, which may be a consideration when employing such
effective mechanism for providing additional, on-demand    resources in the future. In particular, the substantial egress
CPU resources. At the level employed by ATLAS, typically    associated with data reprocessing means that for now this
ﬁve or ten thousand cores, preemption of the allocated job   workﬂow is best avoided until further improvements in net-
slots is barely an issue, even when using the spot instance   work connectivity are deployed, and that until then the site
model as is done here. Whilst higher eviction rates were    cannot be seen as universally suitable for ATLAS. If work-
occasionally noticeable, for example during the data repro-   ﬂows such as Fast or Full Chain [63] can be employed, where
cessing single workﬂow period, the overall failure rate was    the egress of intermediate MC formats is avoided, this will
not signiﬁcantly higher than that observed on the grid. The    also help to reduce these costs.
ATLAS Google site was also shown to be extremely effec-    Establishing a viable and cost-effective subscription agree-
tive as a bursting resource, quickly providing up to one hun-   ment between experiment and commercial cloud provider is
dred thousand additional job slots, resulting in a signiﬁcantly    clearly a critical consideration of the TCO, given the large
faster production turnaround than is possible on the ATLAS    discrepancybetweenthelist-pricesandtheagreementassoci-
grid sites. In addition, the project has enabled parallel R&D    ated with this project. A collaborative approach may be nec-
efforts to ﬂourish by providing different types of resources,    essary to obtain the best deal with a large volume discount.
for example GPU or ARM, on an elastic basis, demonstrating   One option could be for CERN to make a signiﬁcant purchase
rapid integration [59].                                        of cloud capacity and give the option to pay to be part of it,

123

### Página PDF 19

Comput Softw Big Sci        (2025) 9:2                                                          Page 19 of 35    2


which has been done before [64]. This offer could extend    SERI, SNSF and Cantons of Bern and Geneva, Switzerland; MOST,
not only to multiple sites, but also multiple experiments, and     Taipei; TENMAK, Türkiye; STFC, United Kingdom; DOE and NSF,
                                                      USA.
could even be done cooperatively with other international
                                                                          Individual groups and members have received support from BCKDF,
organisations such as EMBL [65]. Another important con-   CANARIE,CRCandDRAC,Canada;CERN-CZ,FORTEandPRIMUS,
sideration going forward, especially if commercial clouds are    Czech Republic; COST, ERC, ERDF, Horizon 2020, ICSC-Next-
employed by a signiﬁcant number of sites, is to understand    GenerationEU and Marie Skłodowska-Curie Actions, European Union;
                                                                        Investissements d’Avenir Labex, Investissements d’Avenir Idex and
how such resources ﬁt into the WLCG pledge structure.
                                                             ANR,France;DFGandAvHFoundation,Germany;Herakleitos,Thales
The initial concerns about a signiﬁcant loss of on-site person-    and Aristeia programmes co-ﬁnanced by EU-ESF and the Greek NSRF,
nel when outsourcing computing to the cloud, and the poten-     Greece; BSF-NSF and MINERVA, Israel; NCN and NAWA, Poland;
tial wider implications for ATLAS due to additional parallel    La Caixa Banking Foundation, CERCA Programme Generalitat de
                                                                   Catalunya and PROMETEO and GenT Programmes Generalitat Valen-
support roles, appear to be less pronounced. This is because,
                                                                             ciana, Spain; Göran Gustafssons Stiftelse, Sweden; The Royal Society
for the most part, these individuals at the sites would still be    and Leverhulme Trust, United Kingdom.
needed to contribute to ATLAS distributed computing. As     In addition, individual members wish to acknowledge support from
such, at least for larger sites, employing commercial clouds    Armenia: Yerevan Physics  Institute (FAPERJ); CERN: European
                                                                      Organization  for Nuclear Research (CERN PJAS); Chile: Agen-
and off-premises resources may not immediately result in
                                                                              cia Nacional de Investigación y Desarrollo (FONDECYT 1230812,
signiﬁcant cost savings.                            FONDECYT 1230987, FONDECYT 1240864); China: Chinese Min-
In summary, commercial cloud computing is an effective      istry of Science and Technology (MOST-2023YFA1605700), National
technical solution for ATLAS for providing additional CPU     Natural Science Foundation of China (NSFC  - 12175119, NSFC
                                                                12275265, NSFC-12075060); Czech Republic: Czech Science Foun-
resources, and whilst the seamless integration of cloud-based
                                                                        dation (GACR - 24-11373S), Ministry of Education Youth and Sports
storage was also achieved, network costs may be signiﬁcant,    (FORTE CZ.02.01.01/00/22_008/0004632), PRIMUS Research Pro-
based on the list-price. Some ATLAS workﬂows are found to    gramme (PRIMUS/21/SCI/017); EU: H2020 European Research Coun-
be better than others with respect to egress. Resource burst-      cil (ERC - 101002463); European Union: European Research Coun-
                                                                                          cil (ERC  - 948254, ERC 101089007), Horizon 2020 Framework
ing was shown to be very effective, albeit at signiﬁcant cost.
                                                          Programme (MUCCA - CHIST-ERA-19-XAI-00), European Union,
Establishing a favourable subscription agreement model that     Future  Artiﬁcial  Intelligence  Research  (FAIR-NextGenerationEU
makes sense to both the cloud provider and the client is    PE00000013), Italian Center for High Performance Computing, Big
an advantage. By leveraging the Google Cloud Subscription    Data and Quantum Computing (ICSC, NextGenerationEU); France:
                                                           Agence Nationale de la Recherche (ANR-20-CE31-0013, ANR-21-
Agreement pricing model, ATLAS has effectively harnessed
                                                              CE31-0013, ANR-21-CE31-0022), Investissements d’Avenir Labex
between three to four times the resources compared to what    (ANR-11-LABX-0012); Germany: Baden-Württemberg Stiftung (BW
the same investment would deliver for the list-price. It is yet     Stiftung-Postdoc Eliteprogramme), Deutsche Forschungsgemeinschaft
to be seen how much this project inﬂuences the structure and   (DFG - 469666862, DFG - CR 312/5-2); Italy: Istituto Nazionale di
                                                                            Fisica Nucleare (ICSC, NextGenerationEU); Japan: Japan Society for
cost of any potential follow-up deal to be brokered. There
                                                                          the Promotion of Science (JSPS KAKENHI JP22H01227, JSPS KAK-
is much interest for ATLAS to continue this project, where   ENHI JP22H04944, JSPS KAKENHI JP22KK0227, JSPS KAKENHI
network connectivity would be the main focus.                JP23KK0245); Netherlands: Netherlands Organisation for Scientiﬁc
                                                                  Research (NWO Veni 2020 - VI.Veni.202.179); Norway: Research
Acknowledgements WethankCERNfortheverysuccessfuloperation    Council of Norway (RCN-314472); Poland: Polish National Agency
of the LHC and its injectors, as well as the support staff at CERN and at     for Academic Exchange (PPN/PPO/2020/1/00002/U/00001), Polish
our institutions worldwide without whom ATLAS could not be operated     National Science Centre (NCN 2021/42/E/ST2/00350, NCN OPUS
efﬁciently.                                                              nr 2022/47/B/ST2/03059, NCN UMO-2019/34/E/ST2/00393, UMO-
The crucial computing support from all WLCG partners is acknowl-    2020/37/B/ST2/01043,  UMO-2021/40/C/ST2/00187,  UMO-2022/
edged gratefully, in particular from CERN, the ATLAS Tier-1 facilities    47/O/ST2/00148, UMO-2023/49/B/ST2/04085); Slovenia: Slovenian
at TRIUMF/SFU (Canada), NDGF (Denmark, Norway, Sweden), CC-    Research Agency (ARIS grant J1-3010); Spain: Generalitat Valen-
IN2P3 (France), KIT/GridKA (Germany), INFN-CNAF (Italy), NL-T1     ciana (Artemisa, FEDER, IDIFEDER/2018/048), Ministry of Science
(Netherlands), PIC (Spain), RAL (UK) and BNL (USA), the Tier-2    and Innovation (MCIN & NextGenEU PCI2022-135018-2, MICIN &
facilities worldwide and large non-WLCG resource providers. Major   FEDER PID2021-125273NB, RYC2019-028510-I, RYC2020-030254-
contributors of computing resources are listed in Ref. [66].                       I, RYC2021-031273-I, RYC2022-038164-I), PROMETEO and GenT
We gratefully acknowledge the support of ANPCyT, Argentina; YerPhI,    Programmes Generalitat Valenciana (CIDEGENT/2019/027); Swe-
Armenia; ARC, Australia; BMWFW and FWF, Austria; ANAS, Azer-     den: Swedish Research Council (Swedish Research Council 2023-
baijan; CNPq and FAPESP, Brazil; NSERC, NRC and CFI, Canada;    04654, VR 2018-00482, VR 2022-03845, VR 2022-04683, VR 2023-
CERN; ANID, Chile; CAS, MOST and NSFC, China; Minciencias,    03403, VR grant 2021-03651), Knut and Alice Wallenberg Foun-
Colombia; MEYS CR, Czech Republic; DNRF and DNSRC, Den-     dation (KAW 2018.0157, KAW 2018.0458, KAW 2019.0447, KAW
mark; IN2P3-CNRS and CEA-DRF/IRFU, France; SRNSFG, Georgia;     2022.0358); Switzerland: Swiss National Science Foundation (SNSF
BMBF, HGF and MPG, Germany; GSRI, Greece; RGC and Hong Kong      - PCEFP2_194658); United Kingdom: Leverhulme Trust (Leverhulme
SAR, China; ISF and Benoziyo Center, Israel; INFN, Italy; MEXT and     Trust RPG-2020-004), Royal Society (NIF-R1-231091); United States
JSPS, Japan; CNRST, Morocco; NWO, Netherlands; RCN, Norway;     of America: U.S. Department of Energy (ECA DE-AC02-76SF00515),
MNiSW, Poland; FCT, Portugal; MNE/IFA, Romania; MESTD, Ser-    Neubauer Family Foundation.
bia; MSSR, Slovakia; ARRS and MIZŠ, Slovenia; DSI/NRF, South
Africa; MICINN, Spain; SRC and Wallenberg Foundation, Sweden;


                                  123

### Página PDF 20

2  Page 20 of 35                                                    Comput Softw Big Sci        (2025) 9:2


Author contributions  All authors have contributed to the publication,     10. Megino F Barreiro et al (2021) Seamless integration of commer-
being variously involved in the design and the construction of the detec-           cial clouds with ATLAS distributed computing. EPJ Web Conf
tors, in writing software, calibrating subsystems, operating the detectors        251:02005. https://doi.org/10.1051/epjconf/202125102005
andacquiringdata,andﬁnallyanalysingtheprocesseddata.TheATLAS     11. Megino F Barreiro et al (2017) PanDA for ATLAS distributed com-
Collaboration members discussed and approved the scientiﬁc results.         puting in the next decade. J Phys Conf Ser 898:052002. https://doi.
The manuscript was prepared by a subgroup of authors appointed by        org/10.1088/1742-6596/898/5/052002
the collaboration and subject to an internal collaboration-wide review     12.  Barisits M et al (2019) Rucio: scientiﬁc data management. Comput
process. All authors reviewed and approved the ﬁnal version of the        Softw Big Sci. https://doi.org/10.1007/s41781-019-0026-3
manuscript.                                                             13. Apollinari G et al (2015) High–luminosity Large Hadron Collider
                                                            (HL–LHC): preliminary design report, CERN-2015-005. https://
Funding Open access funding provided by CERN (European Organi-         cds.cern.ch/record/2116337
zation for Nuclear Research).                                            14. ATLAS Collaboration (2020) ATLAS HL–LHC computing con-
                                                                             ceptual design  report, CERN-LHCC-2020-015, LHCC-G-178.
Data Availability No datasets were generated or analysed during the         https://cds.cern.ch/record/2729668
current study.                                                           15. ATLAS Collaboration (2022) ATLAS software and comput-
                                                                           ing HL–LHC roadmap, CERN-LHCC-2022-005, LHCC-G-182.
Declarations                                                                https://cds.cern.ch/record/2802918
                                                                        16. Devouassoux M (2018) Method to calculate the total cost of own-
Competing interests The authors declare no competing interests.             ership of infrastructure as a service, version 2. https://doi.org/10.
                                                                    5281/zenodo.2161088
Open Access This article is licensed under a Creative Commons Attri-     17. Helix Nebula – the science cloud. https://doi.org/10.3030/687614
bution 4.0 International License, which permits use, sharing, adaptation,     18. Amazon Web Services pricing. https://aws.amazon.com/pricing
distribution and reproduction in any medium or format, as long as you     19. Google  Cloud  Platform   pricing.  https://cloud.google.com/
give appropriate credit to the original author(s) and the source, pro-         products/calculator
vide a link to the Creative Commons licence, and indicate if changes     20. Martelli E (2024) Evolving the LHCOPN and LHCONE net-
were made. The images or other third party material in this article        works to support HL-LHC computing requirements. EPJ Web Conf
are included in the article’s Creative Commons licence, unless indi-        295:07016. https://doi.org/10.1051/epjconf/202429507016
cated otherwise in a credit line to the material. If material is not     21. ATLAS Collaboration (2024) Software and computing for Run 3
included in the article’s Creative Commons licence and your intended         of the ATLAS experiment at the LHC. arXiv:2404.06335 [hep-ex]
use is not permitted by statutory regulation or exceeds the permit-     22. Kubernetes. https://kubernetes.io/docs/home/
ted use, you will need to obtain permission directly from the copy-     23. Maeno T et al (2019) Harvester: an edge service harvesting hetero-
right holder. To view a copy of this licence, visit http://creativecomm        geneous resources for ATLAS. EPJ Web Conf 214:03030. https://
ons.org/licenses/by/4.0/.                                                  doi.org/10.1051/epjconf/201921403030
                                                                        24. Megino F Barreiro et al (2020) Using Kubernetes as an ATLAS
                                                                   computing site. EPJ Web Conf 245:07025. https://doi.org/10.1051/
                                                                     epjconf/202024507025
                                                                        25. Megino F Barreiro et al (2024) Accelerating science: The usage
                                                                             of commercial clouds in ATLAS Distributed Computing. EPJ Web
References                                                     Conf 295:07002. https://doi.org/10.1051/epjconf/202429507002
                                                                        26. Blomer J et al (2020) The CernVM ﬁle system, version 2.7.5.
 1. ATLAS Collaboration (2008) The ATLAS experiment at the CERN         https://doi.org/10.5281/zenodo.4114078
    Large Hadron Collider. JINST 3:S08003. https://doi.org/10.1088/     27. Authenticating   requests  (AWS   Signature,   version    4).
    1748-0221/3/08/S08003                                              https://docs.aws.amazon.com/AmazonS3/latest/API/
 2. Evans L, Bryant P (2008) LHC machine. JINST 3:S08001. https://         sig-v4-authenticating-requests.html
    doi.org/10.1088/1748-0221/3/08/S08001                            28. Davix. https://davix.web.cern.ch/davix/docs/devel/
 3. Bird I et al (2005) LHC computing grid: technical design report,     29.  Barisits M et al (2024) Extending Rucio with modern cloud stor-
   CERN-LHCC-2005-024. https://cds.cern.ch/record/840543              age support. EPJ Web Conf 295:01030. https://doi.org/10.1051/
 4. Bird I et al (2014) Update of the computing models of the WLCG        epjconf/202429501030
    and the LHC experiments, CERN-LHCC-2014-014. https://cds.     30. CERN File Transfer Service. https://fts.web.cern.ch/fts/
    cern.ch/record/1695401                                             31. Interoperable Global Trust Federation. https://www.igtf.net/
 5. Úbeda García M et al (2014) Integration of cloud resources in the     32. Google   spot  VMs.   https://cloud.google.com/compute/docs/
   LHCb distributed computing. J Phys Conf Ser 513:032099. https://          instances/spot
    doi.org/10.1088/1742-6596/513/3/032099                           33. Rucio replica management. https://rucio.cern.ch/documentation/
 6. Panitkin S (2015) Look to the clouds and beyond. Nat Phys 11:373.         started/concepts/replica_management/
    https://doi.org/10.1038/nphys3319                                  34. Rucio RSE conﬁguration.  https://rucio.cern.ch/documentation/
 7. Holzman B et al (2017) HEPCloud, a new paradigm for HEP facil-         started/concepts/rucio_storage_element/
      ities: CMS Amazon web services investigation. Comput Softw Big     35. Borodin M et al (2021) The ATLAS data carousel project sta-
     Sci. https://doi.org/10.1007/s41781-017-0001-9                              tus. EPJ Web Conf 251:02006. https://doi.org/10.1051/epjconf/
 8. Lonˇcar P (2023) Scalable data processing model of the ALICE        202125102006
    experiment in the cloud, PhD thesis: Sveuˇcilište u Splitu. Fakul-     36. ATLAS Collaboration (2022) Active learning reinterpretation of
     tet elektrotehnike, strojarstva i brodogradnje. Zavod za elektron-        an ATLAS dark matter search constraining a model of a dark
    iku i raˇcunarstvo., University of Split. https://cds.cern.ch/record/        Higgs boson decaying to two (b)-quarks, ATL-PHYS-PUB-2022-
    2874778                                                             045, 2022. https://cds.cern.ch/record/2839789
 9. Megino F Barreiro, Bryant L, Hufnagel D, Anampa K Hurtado     37. ATLAS Collaboration (2017) Performance of the ATLAS trigger
    (2023) US ATLAS and US CMS HPC and cloud blueprint. ArXiv:        system in 2015. Eur Phys J C 77:317. https://doi.org/10.1140/epjc/
    2304.07376 [physics.comp-ph]                                     s10052-017-4852-3

123

### Página PDF 21

Comput Softw Big Sci        (2025) 9:2                                                          Page 21 of 35    2


38. ATLAS Collaboration (2024) The ATLAS trigger system for LHC     52. The OCRE project. https://www.ocre-project.eu/
    run 3 and trigger performance in 2022. arXiv:2401.06630 [hep-ex]     53. HEPCloud. https://computing.fnal.gov/hep-cloud/
39. Berghaus F et al (2020) ATLAS Sim@P1 upgrades during long     54. CloudBank. https://www.cloudbank.org/
    shutdown two. EPJ Web Conf 245:07044. https://doi.org/10.1051/     55. Energy   Sciences   Network   peering.   https://www.es.net/
    epjconf/202024507044                                                  engineering-services/the-network/peering-connections/
40. Glushkov I, Lee C, Di Girolamo A, Walker R, Gottardo CA (2024)     56. Internet2 cloud access. https://internet2.edu/cloud/cloud-access/
    Optimization of opportunistic utilization of the ATLAS high-level     57. GÉANT Network. https://network.geant.org/
     trigger farm for LHC Run 3. EPJ Web Conf 295:07035. https://doi.     58. Grid File Access Library, version 2. https://dmc-docs.web.cern.ch/
    org/10.1051/epjconf/202429507035                                    dmc-docs/gfal2/gfal2.html
41. HPC Vega. https://www.izum.si/en/vega-en/                         59. Megino F Barreiro et al (2024) Operational experience and R&D
42. HPC Perlmutter. https://docs.nersc.gov/systems/perlmutter/             resultsusingthegooglecloudforhighenergyphysicsintheATLAS
43. Google storage pricing. https://cloud.google.com/storage/pricing#         experiment. arXiv:2403.15873 [hep-ex]
    europe                                                             60. JupyterHub. https://jupyter.org/hub
44. Google network service tiers pricing. https://cloud.google.com/     61. Dask. https://www.dask.org
     network-tiers/pricing                                               62. General Data Protection Regulation. https://gdpr-info.eu
45. Google Cloud  interconnect  pricing.  https://cloud.google.com/     63. Javurkova M et al (2021) The fast simulation chain in the ATLAS
    network-connectivity/docs/interconnect/pricing                          experiment. EPJ Web Conf 251:03012. https://doi.org/10.1051/
46. Sﬁligoi I et al (2021) Managing cloud networking costs for data–        epjconf/202125103012
     intensive applications by provisioning dedicated network links.     64. CloudBank EU NGI. https://ngiatlantic.eu/funded-experiments/
    arXiv:2104.06913 [cs.NI]                                            cloudbank-eu-ngi
47. Energy Sciences Network. https://www.es.net                        65. The European Molecular Biology Laboratory. https://www.embl.
48. Giordano D et al (2023) HEPScore: a new CPU benchmark for the         org
   WLCG. arXiv:2306.08118 [hep-ex]                                 66. ATLAS Collaboration, ATLAS Computing Acknowledgements,
49. Google Cloud Platform terms of service. https://cloud.google.com/        ATL-SOFT-PUB-2023-001,   2023.   https://cds.cern.ch/record/
    terms                                                        2869272
50. Google data centers: efﬁciency. https://www.google.com/about/
    datacenters/efﬁciency/
51. Carbon free energy for Google Cloud regions. https://cloud.google.
                                                                     Publisher’s Note Springer Nature remains neutral with regard to juris-
    com/sustainability/region-carbon
                                                                              dictional claims in published maps and institutional afﬁliations.


                                  123

### Página PDF 22

2  Page 22 of 35                                                    Comput Softw Big Sci        (2025) 9:2


The ATLAS Collaboration

G. Aad104    , E. Aakvaag17    , B. Abbott123    , S. Abdelhameed119a    , K. Abeling56    , N. J. Abicht50    , S. H. Abidi30    ,
M. Aboelela45    , A. Aboulhorma36e    , H. Abramowicz154    , H. Abreu153    , Y. Abulaiti120    , B. S. Acharya70a,70b,m    ,
A. Ackermann64a    ,    C. Adam Bourdarios4    ,    L. Adamczyk87a    ,     S. V. Addepalli27    ,   M. J. Addison103    ,
J. Adelman118    , A. Adiguzel22c    , T. Adye137    , A. A. Affolder139    , Y. Aﬁk40    , M. N. Agaras13    , J. Agarwala74a,74b    ,
A. Aggarwal102    ,   C. Agheorghiesei28c    ,    F. Ahmadov39,y    ,   W. S. Ahmed106    ,    S. Ahuja97    ,   X. Ai63e    ,
G. Aielli77a,77b    , A. Aikot166    , M. Ait Tamlihat36e    , B. Aitbenchikh36a    , M. Akbiyik102    ,  T. P. A. Åkesson100    ,
A. V. Akimov38    ,  D. Akiyama171    ,  N. N. Akolkar25    ,   S. Aktas22a    ,  K. Al Khoury42    ,  G. L. Alberghi24b    ,
J. Albert168    ,    P. Albicocco54    ,   G. L. Albouy61    ,    S. Alderweireldt53    ,   Z. L. Alegria124    ,  M. Aleksa37    ,
I. N. Aleksandrov39    ,   C. Alexa28b    ,   T. Alexopoulos10    ,    F. Alfonsi24b    ,  M. Algren57    ,  M. Alhroob170    ,
B. Ali135    ,  H. M. J. Ali93    ,   S. Ali32    ,   S. W. Alibocus94    ,  M. Aliev34c    ,  G. Alimonti72a    ,  W. Alkakhi56    ,
C. Allaire67    , B. M. M. Allbrooke149    , J. F. Allen53    , C. A. Allendes Flores140f    , P. P. Allport21    , A. Aloisio73a,73b    ,
F. Alonso92    ,   C. Alpigiani141    ,   Z. M. K. Alsolami93    ,  M. Alvarez Estevez101    ,   A. Alvarez Fernandez102    ,
M. Alves Cardoso57    , M. G. Alviggi73a,73b    , M. Aly103    , Y. Amaral Coutinho84b    , A. Ambler106    , C. Amelung37,
M. Amerl103    ,  C. G. Ames111    ,  D. Amidei108    ,  B. Amini55    ,  K. J. Amirie158    ,  S. P. Amor Dos Santos133a    ,
K. R. Amos166    ,   D. Amperiadou155    ,    S. An85,    V. Ananiev128    ,    C. Anastopoulos142    ,    T. Andeen11    ,
J. K. Anders37    ,    A. C. Anderson60    ,     S. Y. Andrean48a,48b    ,    A. Andreazza72a,72b    ,     S. Angelidakis9    ,
A. Angerami42    ,   A. V. Anisenkov38    ,   A. Annovi75a    ,   C. Antel57    ,    E. Antipov148    ,   M. Antonelli54    ,
F. Anulli76a    ,  M. Aoki85    ,  T. Aoki156    ,  M. A. Aparo149    ,  L. Aperio Bella49    ,  C. Appelt19    ,  A. Apyan27    ,
S. J. Arbiol Val88    ,  C. Arcangeletti54    ,  A. T. H. Arce52    ,  J-F. Arguin110    ,  S. Argyropoulos55    ,  J.-H. Arling49    ,
O. Arnaez4    ,  H. Arnold148    ,  G. Artoni76a,76b    ,  H. Asada113    ,  K. Asai121    ,   S. Asai156    ,  N. A. Asbah37    ,
R. A. Ashby Pickering170    , K. Assamagan30    , R. Astalos29a    , K. S. V. Astrand100    , S. Atashi162    , R. J. Atkin34a    ,
M. Atkinson165,  H. Atmani36f,   P. A. Atmasiddha131    ,  K. Augsten135    ,   S. Auricchio73a,73b    ,  A. D. Auriol21    ,
V. A. Austrup103    , G. Avolio37    , K. Axiotis57    , G. Azuelos110,ad    , D. Babal29b    , H. Bachacou138    , K. Bachas155,q    ,
A. Bachiu35    ,    F. Backman48a,48b    ,   A. Badea40    ,    T. M. Baer108    ,    P. Bagnaia76a,76b    ,   M. Bahmani19    ,
D. Bahner55    ,  K. Bai126    ,  J. T. Baines137    ,  L. Baines96    ,  O. K. Baker175    ,  E. Bakos16    ,  D. Bakshi Gupta8    ,
L. E. Balabram Filho84b    ,    V. Balakrishnan123    ,    R. Balasubramanian117    ,    E. M. Baldin38    ,     P. Balek87a    ,
E. Ballabene24b,24a    ,    F. Balli138    ,   L. M. Baltes64a    ,   W. K. Balunas33    ,     J. Balz102    ,     I. Bamwidhi119b    ,
E. Banas88    ,  M. Bandieramonte132    ,   A. Bandyopadhyay25    ,   S. Bansal25    ,   L. Barak154    ,  M. Barakat49    ,
E. L. Barberio107    ,  D. Barberis58b,58a    ,  M. Barbero104    ,  M. Z. Barel117    ,   T. Barillari112    ,  M-S. Barisits37    ,
T. Barklow146    ,    P. Baron125    ,   D. A. Baron Moreno103    ,   A. Baroncelli63a    ,   A. J. Barr129    ,    J. D. Barr98    ,
F. Barreiro101    ,    J. Barreiro Guimarães da Costa14    ,  U. Barron154    ,  M. G. Barros Teixeira133a    ,   S. Barsov38    ,
F. Bartels64a    , R. Bartoldus146    , A. E. Barton93    ,  P. Bartos29a    , A. Basan102    , M. Baselga50    , A. Bassalat67,b    ,
M. J. Basso159a    ,  S. Bataju45    ,  R. Bate167    ,  R. L. Bates60    ,  S. Batlamous101,  B. Batool144    , M. Battaglia139    ,
D. Battulga19    ,  M. Bauce76a,76b    ,  M. Bauer80    ,   P. Bauer25    ,   L. T. Bazzano Hurrell31    ,    J. B. Beacham52    ,
T. Beau130    ,    J. Y. Beaucamp92    ,    P. H. Beauchemin161    ,    P. Bechtle25    ,   H. P. Beck20,p    ,   K. Becker170    ,
A. J. Beddall83    ,  V. A. Bednyakov39    ,  C. P. Bee148    ,  L. J. Beemster16    ,  T. A. Beermann37    ,  M. Begalli84d    ,
M. Begel30    ,  A. Behera148    ,   J. K. Behr49    ,   J. F. Beirer37    ,   F. Beisiegel25    ,  M. Belfkir119b    ,  G. Bella154    ,
L. Bellagamba24b    ,  A. Bellerive35    ,   P. Bellos21    ,  K. Beloborodov38    ,  D. Benchekroun36a    ,  F. Bendebba36a    ,
Y. Benhammou154  ,K. C. Benkendorfer62  ,L. Beresford49  ,M. Beretta54  ,E. Bergeaas Kuutmann164  ,N. Berger4    ,
B. Bergmann135    ,    J. Beringer18a    ,  G. Bernardi5    ,   C. Bernius146    ,   F. U. Bernlochner25    ,   F. Bernon37,104    ,
A. Berrocal Guardia13    , T. Berry97    , P. Berta136    , A. Berthold51    , S. Bethke112    , A. Betti76a,76b    , A. J. Bevan96    ,
N. K. Bhalla55    ,  S. Bhatta148    ,  D. S. Bhattacharya169    ,  P. Bhattarai146    ,  K. D. Bhide55    ,  V. S. Bhopatkar124    ,
R. M. Bianchi132    ,   G. Bianco24b,24a    ,   O. Biebel111    ,   R. Bielski126    ,  M. Biglietti78a    ,   C. S. Billingsley45,
Y. Bimgdi36f    ,  M. Bindi56    ,  A. Bingul22b    ,  C. Bini76a,76b    ,  G. A. Bird33    ,  M. Birman172    ,  M. Biros136    ,
S. Biryukov149    ,  T. Bisanz50    ,  E. Bisceglie44b,44a    ,  J. P. Biswal137    ,  D. Biswas144    ,   I. Bloch49    ,  A. Blue60    ,
U. Blumenschein96    ,  J. Blumenthal102    ,  V. S. Bobrovnikov38    , M. Boehler55    ,  B. Boehm169    ,  D. Bogavac37    ,
A. G. Bogdanchikov38    ,  C. Bohm48a    ,  V. Boisvert97    ,  P. Bokan37    ,  T. Bold87a    , M. Bomben5    , M. Bona96    ,
M. Boonekamp138    ,  C. D. Booth97    ,  A. G. Borbély60    ,   I. S. Bordulev38    ,  G. Borissov93    ,  D. Bortoletto129    ,
D. Boscherini24b    ,  M. Bosman13    ,   J. D. Bossio Sola37    ,  K. Bouaouda36a    ,  N. Bouchhar166    ,   L. Boudet4    ,
J. Boudreau132    , E. V. Bouhova-Thacker93    , D. Boumediene41    , R. Bouquet58b,58a    , A. Boveia122    ,  J. Boyd37    ,
D. Boye30    ,    I. R. Boyko39    ,   L. Bozianu57    ,   J. Bracinik21    ,  N. Brahimi4    ,  G. Brandt174    ,  O. Brandt33    ,

123

### Página PDF 23

Comput Softw Big Sci        (2025) 9:2                                                          Page 23 of 35    2

F. Braren49    ,  B. Brau105    ,   J. E. Brau126    ,  R. Brener172    ,  L. Brenner117    ,  R. Brenner164    ,  S. Bressler172    ,
G. Brianti79a,79b    ,   D. Britton60    ,   D. Britzger112    ,     I. Brock25    ,   G. Brooijmans42    ,    E. M. Brooks159b    ,
E. Brost30    , L. M. Brown168    , L. E. Bruce62    , T. L. Bruckler129    ,  P. A. Bruckman de Renstrom88    , B. Brüers49    ,
A. Bruni24b    ,  G. Bruni24b    , M. Bruschi24b    ,  N. Bruscino76a,76b    ,  T. Buanes17    ,  Q. Buat141    ,  D. Buchin112    ,
A. G. Buckley60    ,   O. Bulekov38    ,   B. A. Bullard146    ,   S. Burdin94    ,   C. D. Burgard50    ,   A. M. Burger37    ,
B. Burghgrave8    ,  O. Burlayenko55    ,   J. Burleson165    ,   J. T. P. Burr33    ,   J. C. Burzynski145    ,   E. L. Busch42    ,
V. Büscher102    ,   P. J. Bussey60    ,    J. M. Butler26    ,  C. M. Buttar60    ,    J. M. Butterworth98    ,  W. Buttinger137    ,
C. J. Buxo Vazquez109    , A. R. Buzykaev38    ,  S. Cabrera Urbán166    , L. Cadamuro67    , D. Caforio59    , H. Cai132    ,
Y. Cai14,114c    ,  Y. Cai114a    ,  V. M. M. Cairo37    ,  O. Cakir3a    ,  N. Calace37    ,  P. Calaﬁura18a    ,  G. Calderini130    ,
P. Calfayan69    , G. Callea60    , L. P. Caloba84b, D. Calvet41    , S. Calvet41    , M. Calvetti75a,75b    , R. Camacho Toro130    ,
S. Camarda37    ,    D. Camarero Munoz27    ,     P. Camarri77a,77b    ,   M. T. Camerlingo73a,73b    ,    D. Cameron37    ,
C. Camincher168    ,  M. Campanelli98    ,  A. Camplani43    ,  V. Canale73a,73b    ,  A. C. Canbay3a    ,  E. Canonero97    ,
J. Cantero166    ,    Y. Cao165    ,    F. Capocasa27    ,   M. Capua44b,44a    ,   A. Carbone72a,72b    ,   R. Cardarelli77a    ,
J. C. J. Cardenas8    ,  G. Carducci44b,44a    ,   T. Carli37    ,  G. Carlino73a    ,    J. I. Carlotto13    ,   B. T. Carlson132,r    ,
E. M. Carlson168,159a    , J. Carmignani94    , L. Carminati72a,72b    , A. Carnelli138    , M. Carnesale76a,76b    , S. Caron116    ,
E. Carquin140f    ,   S. Carrá72a    ,   G. Carratta24b,24a    ,   A. M. Carroll126    ,   T. M. Carter53    ,  M. P. Casado13,j    ,
M. Caspar49    ,     F. L. Castillo4    ,     L. Castillo Garcia13    ,     V. Castillo Gimenez166    ,    N. F. Castro133a,133e    ,
A. Catinaccio37    , J. R. Catmore128    , T. Cavaliere4    , V. Cavaliere30    , N. Cavalli24b,24a    , L. J. Caviedes Betancourt23b,
Y. C. Cekmecelioglu49    ,   E. Celebi83    ,   S. Cella37    ,    F. Celli129    ,  M. S. Centonze71a,71b    ,   V. Cepaitis57    ,
K. Cerny125    , A. S. Cerqueira84a    , A. Cerri149    , L. Cerrito77a,77b    , F. Cerutti18a    , B. Cervato144    , A. Cervelli24b    ,
G. Cesarini54    ,    S. A. Cetin83    ,   D. Chakraborty118    ,     J. Chan18a    ,   W. Y. Chan156    ,     J. D. Chapman33    ,
E. Chapon138    ,   B. Chargeishvili152b    ,  D. G. Charlton21    ,  M. Chatterjee20    ,   C. Chauhan136    ,   Y. Che114a    ,
S. Chekanov6    , S. V. Chekulaev159a    , G. A. Chelkov39,a    , A. Chen108    , B. Chen154    , B. Chen168    , H. Chen114a    ,
H. Chen30    ,  J. Chen63c    ,  J. Chen145    , M. Chen129    , S. Chen156    , S. J. Chen114a    , X. Chen63c    , X. Chen15,ac    ,
Y. Chen63a    ,   C. L. Cheng173    ,  H. C. Cheng65a    ,   S. Cheong146    ,  A. Cheplakov39    ,   E. Cheremushkina49    ,
E. Cherepanova117    , R. Cherkaoui El Moursli36e    ,  E. Cheu7    , K. Cheung66    ,  L. Chevalier138    ,  V. Chiarella54    ,
G. Chiarelli75a    ,   N. Chiedde104    ,   G. Chiodini71a    ,   A. S. Chisholm21    ,   A. Chitan28b    ,  M. Chitishvili166    ,
M. V. Chizhov39    , K. Choi11    , Y. Chou141    , E. Y. S. Chow116    , K. L. Chu172    , M. C. Chu65a    , X. Chu14,114c    ,
Z. Chubinidze54    ,    J. Chudoba134    ,    J. J. Chwastowski88    ,   D. Cieri112    ,   K. M. Ciesla87a    ,   V. Cindro95    ,
A. Ciocio18a    , F. Cirotto73a,73b    , Z. H. Citron172    , M. Citterio72a    , D. A. Ciubotaru28b, A. Clark57    , P. J. Clark53    ,
N. Clarke Hall98    , C. Clarry158    , J. M. Clavijo Columbie49    , S. E. Clawson49    , C. Clement48a,48b    , Y. Coadou104    ,
M. Cobal70a,70c    , A. Coccaro58b    , R. F. Coelho Barrue133a    , R. Coelho Lopes De Sa105    , S. Coelli72a    , B. Cole42    ,
J. Collot61    , P. Conde Muiño133a,133g    , M. P. Connell34c    , S. H. Connell34c    , E. I. Conroy129    , F. Conventi73a,ae    ,
H. G. Cooke21    ,  A. M. Cooper-Sarkar129    ,   F. A. Corchia24b,24a    ,  A. Cordeiro Oudot Choi130    ,  L. D. Corpe41    ,
M. Corradi76a,76b    ,  F. Corriveau106,x    , A. Cortes-Gonzalez19    , M. J. Costa166    ,  F. Costanza4    , D. Costanzo142    ,
B. M. Cote122    ,   J. Couthures4    ,  G. Cowan97    ,  K. Cranmer173    ,  D. Cremonini24b,24a    ,  S. Crépé-Renaudin61    ,
F. Crescioli130    , M. Cristinziani144    , M. Cristoforetti79a,79b    ,  V. Croft117    ,  J. E. Crosby124    , G. Crosetti44b,44a    ,
A. Cueto101    ,  H. Cui98    ,  Z. Cui7    , W. R. Cunningham60    ,  F. Curcio166    ,  J. R. Curran53    ,  P. Czodrowski37    ,
M. J. Da Cunha Sargedas De Sousa58b,58a    ,      J. V. Da Fonseca Pinto84b    ,    C. Da Via103    ,    W. Dabrowski87a    ,
T. Dado37    ,   S. Dahbi151    ,   T. Dai108    ,  D. Dal Santo20    ,  C. Dallapiccola105    ,  M. Dam43    ,  G. D’amen30    ,
V. D’Amico111    ,  J. Damp102    ,  J. R. Dandoy35    , D. Dannheim37    , M. Danninger145    , V. Dao148    , G. Darbo58b    ,
S. J. Das30,af    ,    F. Dattola49    ,    S. D’Auria72a,72b    ,   A. D’avanzo73a,73b    ,   C. David34a    ,    T. Davidek136    ,
I. Dawson96    ,   H. A. Day-hall135    ,   K. De8    ,   R. De Asmundis73a    ,   N. De Biase49    ,   S. De Castro24b,24a    ,
N. De Groot116    ,  P. de Jong117    , H. De la Torre118    , A. De Maria114a    , A. De Salvo76a    , U. De Sanctis77a,77b    ,
F. De Santis71a,71b    , A. De Santo149    , J. B. De Vivie De Regie61    , D. V. Dedovich39, J. Degens94    , A. M. Deiana45    ,
F. Del Corso24b,24a    ,   J. Del Peso101    ,   F. Del Rio64a    ,  L. Delagrange130    ,   F. Deliot138    ,  C. M. Delitzsch50    ,
M. Della Pietra73a,73b    ,    D. Della Volpe57    ,    A. Dell’Acqua37    ,     L. Dell’Asta72a,72b    ,    M. Delmastro4    ,
P. A. Delsart61    ,   S. Demers175    ,  M. Demichev39    ,   S. P. Denisov38    ,   L. D’Eramo41    ,   D. Derendarz88    ,
F. Derue130    ,    P. Dervan94    ,   K. Desch25    ,   C. Deutsch25    ,    F. A. Di Bello58b,58a    ,   A. Di Ciaccio77a,77b    ,
L. Di Ciaccio4    ,   A. Di Domenico76a,76b    ,    C. Di Donato73a,73b    ,   A. Di Girolamo37    ,   G. Di Gregorio37    ,
A. Di Luca79a,79b    ,   B. Di Micco78a,78b    ,   R. Di Nardo78a,78b    ,   K. F. Di Petrillo40    ,  M. Diamantopoulou35    ,
F. A. Dias117    , T. Dias Do Vale145    , M. A. Diaz140a,140b    , F. G. Diaz Capriles25    , A. R. Didenko39, M. Didenko166    ,
E. B. Diehl108    , S. Díez Cornell49    , C. Diez Pardos144    , C. Dimitriadi164    , A. Dimitrievska21    ,  J. Dingfelder25    ,

                                  123

### Página PDF 24

2  Page 24 of 35                                                    Comput Softw Big Sci        (2025) 9:2

T. Dingley129    , I-M. Dinu28b    , S. J. Dittmeier64b    , F. Dittus37    , M. Divisek136    , F. Djama104    , T. Djobava152b    ,
C. Doglioni103,100    ,   A. Dohnalova29a    ,    J. Dolejsi136    ,   Z. Dolezal136    ,   K. Domijan87a    ,   K. M. Dona40    ,
M. Donadelli84d    ,   B. Dong109    ,     J. Donini41    ,   A. D’Onofrio73a,73b    ,   M. D’Onofrio94    ,     J. Dopke137    ,
A. Doria73a    , N. Dos Santos Fernandes133a    ,  P. Dougan103    , M. T. Dova92    , A. T. Doyle60    , M. A. Draguet129    ,
E. Dreyer172    ,     I. Drivas-koulouris10    ,  M. Drnevich120    ,  M. Drozdova57    ,   D. Du63a    ,   T. A. du Pree117    ,
F. Dubinin38    , M. Dubovsky29a    , E. Duchovni172    , G. Duckeck111    , O. A. Ducu28b    , D. Duda53    , A. Dudarev37    ,
E. R. Duden27    ,   M. D’ufﬁzi103    ,   L. Duﬂot67    ,   M. Dührssen37    ,     I. Duminica28g    ,   A. E. Dumitriu28b    ,
M. Dunford64a    ,    S. Dungs50    ,   K. Dunne48a,48b    ,   A. Duperrin104    ,   H. Duran Yildiz3a    ,   M. Düren59    ,
A. Durglishvili152b    , B. L. Dwyer118    , G. I. Dyckes18a    , M. Dyndal87a    , B. S. Dziedzic37    , Z. O. Earnshaw149    ,
G. H. Eberwein129    ,   B. Eckerova29a    ,    S. Eggebrecht56    ,    E. Egidio Purcino De Souza84e    ,    L. F. Ehrke57    ,
G. Eigen17    , K. Einsweiler18a    , T. Ekelof164    , P. A. Ekman100    , S. El Farkh36b    , Y. El Ghazali63a    , H. El Jarrari37    ,
A. El Moussaouy36a    ,   V. Ellajosyula164    ,  M. Ellert164    ,   F. Ellinghaus174    ,   N. Ellis37    ,    J. Elmsheuser30    ,
M. Elsawy119a    ,  M. Elsing37    ,  D. Emeliyanov137    ,  Y. Enari85    ,    I. Ene18a    ,   S. Epari13    ,   P. A. Erland88    ,
D. Ernani Martins Neto88    ,  M. Errenst174    ,  M. Escalier67    ,  C. Escobar166    ,   E. Etzion154    ,  G. Evans133a    ,
H. Evans69    , L. S. Evans97    , A. Ezhilov38    , S. Ezzarqtouni36a    , F. Fabbri24b,24a    , L. Fabbri24b,24a    , G. Facini98    ,
V. Fadeyev139    ,    R. M. Fakhrutdinov38    ,   D. Fakoudis102    ,    S. Falciano76a    ,    L. F. Falda Ulhoa Coelho37    ,
F. Fallavollita112    , G. Falsetti44b,44a    ,  J. Faltova136    ,  C. Fan165    ,  Y. Fan14    ,  Y. Fang14,114c    , M. Fanti72a,72b    ,
M. Faraj70a,70b    , Z. Farazpay99    , A. Farbin8    , A. Farilla78a    , T. Farooque109    , S. M. Farrington53    , F. Fassi36e    ,
D. Fassouliotis9    , M. Faucci Giannelli77a,77b    , W. J. Fawcett33    , L. Fayard67    ,  P. Federic136    ,  P. Federicova134    ,
O. L. Fedin38,a    , M. Feickert173    , L. Feligioni104    , D. E. Fellers126    , C. Feng63b    , Z. Feng117    , M. J. Fenton162    ,
L. Ferencz49    , R. A. M. Ferguson93    , S. I. Fernandez Luengo140f    , P. Fernandez Martinez13    , M. J. V. Fernoux104    ,
J. Ferrando93    , A. Ferrari164    , P. Ferrari117,116    , R. Ferrari74a    , D. Ferrere57    , C. Ferretti108    , D. Fiacco76a,76b    ,
F. Fiedler102    ,   P. Fiedler135    ,  A. Filipˇciˇc95    ,   E. K. Filmer1    ,   F. Filthaut116    ,  M. C. N. Fiolhais133a,133c,c    ,
L. Fiorini166    , W. C. Fisher109    , T. Fitschen103    , P. M. Fitzhugh138, I. Fleck144    , P. Fleischmann108    , T. Flick174    ,
M. Flores34d,aa    ,   L. R. Flores Castillo65a    ,   L. Flores Sanz De Acedo37    ,   F. M. Follega79a,79b    ,   N. Fomin33    ,
J. H. Foo158    , A. Formica138    , A. C. Forti103    , E. Fortin37    , A. W. Fortman18a    , M. G. Foti18a    , L. Fountas9,k    ,
D. Fournier67    ,  H. Fox93    ,  P. Francavilla75a,75b    ,  S. Francescato62    ,  S. Franchellucci57    , M. Franchini24b,24a    ,
S. Franchino64a    , D. Francis37, L. Franco116    , V. Franco Lima37    , L. Franconi49    , M. Franklin62    , G. Frattari27    ,
Y. Y. Frid154    ,    J. Friend60    ,  N. Fritzsche37    ,  A. Froch55    ,  D. Froidevaux37    ,    J. A. Frost129    ,   Y. Fu63a    ,
S. Fuenzalida Garrido140f    , M. Fujimoto104    ,  K. Y. Fung65a    ,  E. Furtado De Simas Filho84e    , M. Furukawa156    ,
J. Fuster166    , A. Gaa56    , A. Gabrielli24b,24a    , A. Gabrielli158    , P. Gadow37    , G. Gagliardi58b,58a    , L. G. Gagnon18a    ,
S. Gaid163    ,  S. Galantzan154    ,  E. J. Gallas129    ,  B. J. Gallop137    ,  K. K. Gan122    ,  S. Ganguly156    ,  Y. Gao53    ,
F. M. Garay Walls140a,140b    ,    B. Garcia30,    C. García166    ,   A. Garcia Alonso117    ,   A. G. Garcia Caffaro175    ,
J. E. García Navarro166    , M. Garcia-Sciveres18a    , G. L. Gardner131    , R. W. Gardner40    , N. Garelli161    , D. Garg81    ,
R. B. Garg146    , J. M. Gargan53, C. A. Garner158, C. M. Garvey34a    , V. K. Gassmann161, G. Gaudio74a    , V. Gautam13,
P. Gauzzi76a,76b    ,    J. Gavranovic95    ,     I. L. Gavrilenko38    ,   A. Gavrilyuk38    ,   C. Gay167    ,   G. Gaycken126    ,
E. N. Gazis10    , A. A. Geanta28b    , C. M. Gee139    , A. Gekow122, C. Gemme58b    , M. H. Genest61    , A. D. Gentry115    ,
S. George97    ,   W. F. George21    ,    T. Geralis47    ,    P. Gessinger-Befurt37    ,   M. E. Geyik174    ,   M. Ghani170    ,
K. Ghorbanian96    , A. Ghosal144    , A. Ghosh162    , A. Ghosh7    , B. Giacobbe24b    , S. Giagu76a,76b    , T. Giani117    ,
A. Giannini63a    , S. M. Gibson97    , M. Gignac139    , D. T. Gil87b    , A. K. Gilbert87a    , B. J. Gilbert42    , D. Gillberg35    ,
G. Gilles117    , L. Ginabat130    , D. M. Gingrich2,ad    , M. P. Giordani70a,70c    , P. F. Giraud138    , G. Giugliarelli70a,70c    ,
D. Giugni72a    , F. Giuli37    ,  I. Gkialas9,k    , L. K. Gladilin38    , C. Glasman101    , G. R. Gledhill126    , G. Glemža49    ,
M. Glisic126,    I. Gnesi44b,f    ,   Y. Go30    ,  M. Goblirsch-Kolb37    ,  B. Gocke50    ,  D. Godin110,  B. Gokturk22a    ,
S. Goldfarb107    ,  T. Golling57    , M. G. D. Gololo34g    ,  D. Golubkov38    ,   J. P. Gombas109    ,  A. Gomes133a,133b    ,
G. Gomes Da Silva144    ,   A. J. Gomez Delegido166    ,    R. Gonçalo133a    ,    L. Gonella21    ,   A. Gongadze152c    ,
F. Gonnella21    ,   J. L. Gonski146    ,  R. Y. González Andana53    ,  S. González de la Hoz166    ,  R. Gonzalez Lopez94    ,
C. Gonzalez Renteria18a    ,   M. V. Gonzalez Rodrigues49    ,    R. Gonzalez Suarez164    ,     S. Gonzalez-Sevilla57    ,
L. Goossens37    ,    B. Gorini37    ,    E. Gorini71a,71b    ,   A. Gorišek95    ,    T. C. Gosart131    ,   A. T. Goshaw52    ,
M. I. Gostkin39    ,   S. Goswami124    ,   C. A. Gottardo37    ,   S. A. Gotz111    ,  M. Gouighri36b    ,   V. Goumarre49    ,
A. G. Goussiou141    ,    N. Govender34c    ,    R. P. Grabarczyk129    ,       I. Grabowska-Bold87a    ,    K. Graham35    ,
E. Gramstad128    , S. Grancagnolo71a,71b    , C. M. Grant1,138, P. M. Gravila28f    , F. G. Gravili71a,71b    , H. M. Gray18a    ,
M. Greco71a,71b    , M. J. Green1    , C. Grefe25    , A. S. Grefsrud17    , I. M. Gregor49    , K. T. Greif162    , P. Grenier146    ,
S. G. Grewe112, A. A. Grillo139    , K. Grimm32    , S. Grinstein13,t    , J.-F. Grivaz67    , E. Gross172    , J. Grosse-Knetter56    ,

123

### Página PDF 25

Comput Softw Big Sci        (2025) 9:2                                                          Page 25 of 35    2

J. C. Grundy129    ,  L. Guan108    ,  J. G. R. Guerrero Rojas166    , G. Guerrieri37    ,  R. Gugel102    ,  J. A. M. Guhit108    ,
A. Guida19    , E. Guilloton170    , S. Guindon37    , F. Guo14,114c    , J. Guo63c    , L. Guo49    , Y. Guo108    , R. Gupta132    ,
S. Gurbuz25    ,    S. S. Gurdasani55    ,    G. Gustavino76a,76b    ,     P. Gutierrez123    ,    L. F. Gutierrez Zagazeta131    ,
M. Gutsche51    ,   C. Gutschow98    ,   C. Gwenlan129    ,   C. B. Gwilliam94    ,   E. S. Haaland128    ,   A. Haas120    ,
M. Habedank49    , C. Haber18a    , H. K. Hadavand8    , A. Hadef51    , S. Hadzic112    , A. I. Hagan93    ,  J. J. Hahn144    ,
E. H. Haines98    , M. Haleem169    , J. Haley124    , J. J. Hall142    , G. D. Hallewell104    , L. Halser20    , K. Hamano168    ,
M. Hamer25    ,  G. N. Hamity53    ,   E. J. Hampshire97    ,    J. Han63b    ,  K. Han63a    ,   L. Han114a    ,   L. Han63a    ,
S. Han18a    ,  Y. F. Han158    ,  K. Hanagaki85    , M. Hance139    ,  D. A. Hangal42    ,  H. Hanif145    , M. D. Hank131    ,
J. B. Hansen43    ,    P. H. Hansen43    ,   D. Harada57    ,    T. Harenberg174    ,    S. Harkusha38    ,   M. L. Harris105    ,
Y. T. Harris129    ,  J. Harrison13    , N. M. Harrison122    ,  P. F. Harrison170, N. M. Hartman112    , N. M. Hartmann111    ,
R. Z. Hasan97,137    ,   Y. Hasegawa143    ,    F. Haslbeck129    ,   S. Hassan17    ,   R. Hauser109    ,   C. M. Hawkes21    ,
R. J. Hawkings37    , Y. Hayashi156    , D. Hayden109    , C. Hayes108    , R. L. Hayes117    , C. P. Hays129    , J. M. Hays96    ,
H. S. Hayward94    ,    F. He63a    ,  M. He14,114c    ,   Y. He49    ,   Y. He98    ,   N. B. Heatley96    ,   V. Hedberg100    ,
A. L. Heggelund128    ,  N. D. Hehir96,*    ,  C. Heidegger55    ,  K. K. Heidegger55    ,    J. Heilman35    ,   S. Heim49    ,
T. Heim18a    , J. G. Heinlein131    , J. J. Heinrich126    , L. Heinrich112,ab    , J. Hejbal134    , A. Held173    , S. Hellesund17    ,
C. M. Helling167    ,   S. Hellman48a,48b    ,   R. C. W. Henderson93,   L. Henkelmann33    ,   A. M. Henriques Correia37,
H. Herde100    , Y. Hernández Jiménez148    , L. M. Herrmann25    , T. Herrmann51    , G. Herten55    , R. Hertenberger111    ,
L. Hervas37    , M. E. Hesping102    , N. P. Hessey159a    , M. Hidaoui36b    , N. Hidic136    , E. Hill158    , S. J. Hillier21    ,
J. R. Hinds109    ,   F. Hinterkeuser25    ,  M. Hirose127    ,   S. Hirose160    ,  D. Hirschbuehl174    ,   T. G. Hitchings103    ,
B. Hiti95    , J. Hobbs148    , R. Hobincu28e    , N. Hod172    , M. C. Hodgkinson142    , B. H. Hodkinson129    , A. Hoecker37    ,
D. D. Hofer108    , J. Hofer49    , T. Holm25    , M. Holzbock37    , L. B. A. H. Hommels33    , B. P. Honan103    , J. J. Hong69    ,
J. Hong63c    ,   T. M. Hong132    ,  B. H. Hooberman165    ,  W. H. Hopkins6    ,  M. C. Hoppesch165    ,   Y. Horii113    ,
S. Hou151    , A. S. Howard95    ,  J. Howarth60    ,  J. Hoya6    , M. Hrabovsky125    , A. Hrynevich49    ,  T. Hryn’ova4    ,
P. J. Hsu66    , S.-C. Hsu141    , T. Hsu67    , M. Hu18a    , Q. Hu63a    , S. Huang65b    , X. Huang14,114c    , Y. Huang142    ,
Y. Huang102    , Y. Huang14    , Z. Huang103    , Z. Hubacek135    , M. Huebner25    , F. Huegging25    , T. B. Huffman129    ,
C. A. Hugli49    , M. Huhtinen37    , S. K. Huiberts17    , R. Hulsken106    , N. Huseynov12,h    , J. Huston109    , J. Huth62    ,
R. Hyneman146    ,  G. Iacobucci57    ,  G. Iakovidis30    ,  L. Iconomidou-Fayard67    ,   J. P. Iddon37    ,  P. Iengo73a,73b    ,
R. Iguchi156    ,   Y. Iiyama156    ,   T. Iizawa129    ,   Y. Ikegami85    ,  N. Ilic158    ,  H. Imam84c    ,  M. Ince Lezki57    ,
T. Ingebretsen Carlson48a,48b    ,      J. M. Inglis96    ,    G. Introzzi74a,74b    ,    M. Iodice78a    ,     V. Ippolito76a,76b    ,
R. K. Irwin94    ,  M. Ishino156    ,  W. Islam173    ,  C. Issever19,49    ,  S. Istin22a,ah    ,  H. Ito171    ,  R. Iuppa79a,79b    ,
A. Ivina172    ,  J. M. Izen46    , V. Izzo73a    ,  P. Jacka134    ,  P. Jackson1    , C. S. Jagfeld111    , G. Jain159a    ,  P. Jain49    ,
K. Jakobs55    ,  T. Jakoubek172    ,  J. Jamieson60    , W. Jang156    , M. Javurkova105    ,  P. Jawahar103    ,  L. Jeanty126    ,
J. Jejelava152a,z    ,  P. Jenni55,g    , C. E. Jessiman35    , C. Jia63b,  J. Jia148    , X. Jia14,114c    , Z. Jia114a    , C. Jiang53    ,
S. Jiggins49    ,  J. Jimenez Pena13    , S. Jin114a    , A. Jinaru28b    , O. Jinnouchi157    ,  P. Johansson142    , K. A. Johns7    ,
J. W. Johnson139    ,  F. A. Jolly49    ,  D. M. Jones149    ,  E. Jones49    ,  K. S. Jones8,  P. Jones33    ,  R. W. L. Jones93    ,
T. J. Jones94    , H. L. Joos56,37    , R. Joshi122    , J. Jovicevic16    , X. Ju18a    , J. J. Junggeburth105    , T. Junkermann64a    ,
A. Juste Rozas13,t    ,   M. K. Juzek88    ,    S. Kabana140e    ,   A. Kaczmarska88    ,   M. Kado112    ,   H. Kagan122    ,
M. Kagan146    ,  A. Kahn131    ,  C. Kahra102    ,  T. Kaji156    ,  E. Kajomovitz153    ,  N. Kakati172    ,   I. Kalaitzidou55    ,
C. W. Kalderon30    ,   N. J. Kang139    ,   D. Kar34g    ,   K. Karava129    ,   M. J. Kareem159b    ,    E. Karentzos55    ,
O. Karkout117    ,  S. N. Karpov39    ,  Z. M. Karpova39    ,  V. Kartvelishvili93    ,  A. N. Karyukhin38    ,  E. Kasimi155    ,
J. Katzy49    ,  S. Kaur35    , K. Kawade143    , M. P. Kawale123    , C. Kawamoto89    ,  T. Kawamoto63a    , E. F. Kay37    ,
F. I. Kaya161    , S. Kazakos109    , V. F. Kazanin38    , Y. Ke148    , J. M. Keaveney34a    , R. Keeler168    , G. V. Kehris62    ,
J. S. Keller35    ,   A. S. Kelly98,     J. J. Kempster149    ,    P. D. Kennedy102    ,   O. Kepka134    ,   B. P. Kerridge137    ,
S. Kersten174    , B. P. Kerševan95    , L. Keszeghova29a    , S. Ketabchi Haghighat158    , R. A. Khan132    , A. Khanov124    ,
A. G. Kharlamov38    , T. Kharlamova38    , E. E. Khoda141    , M. Kholodenko133a    , T. J. Khoo19    , G. Khoriauli169    ,
J. Khubua152b,*    , Y. A. R. Khwaira130    , B. Kibirige34g, D. Kim6    , D. W. Kim48a,48b    , Y. K. Kim40    , N. Kimura98    ,
M. K. Kingston56    , A. Kirchhoff56    , C. Kirfel25    ,  F. Kirfel25    ,  J. Kirk137    , A. E. Kiryunin112    , C. Kitsaki10    ,
O. Kivernyk25    ,  M. Klassen161    ,  C. Klein35    ,  L. Klein169    ,  M. H. Klein45    ,  S. B. Klein57    ,  U. Klein94    ,
P. Klimek37    , A. Klimentov30    , T. Klioutchnikova37    , P. Kluit117    , S. Kluth112    , E. Kneringer80    , T. M. Knight158    ,
A. Knue50    , D. Kobylianskii172    , S. F. Koch129    , M. Kocian146    , P. Kodyš136    , D. M. Koeck126    , P. T. Koenig25    ,
T. Koffas35    ,  O. Kolay51    ,    I. Koletsou4    ,   T. Komarek88    ,  K. Köneke55    ,  A. X. Y. Kong1    ,   T. Kono121    ,
N. Konstantinidis98    ,   P. Kontaxakis57    ,   B. Konya100    ,   R. Kopeliansky42    ,   S. Koperny87a    ,  K. Korcyl88    ,
K. Kordas155,d    ,  A. Korn98    ,  S. Korn56    ,   I. Korolkov13    ,  N. Korotkova38    ,  B. Kortman117    ,  O. Kortner112    ,

                                  123

### Página PDF 26

2  Page 26 of 35                                                    Comput Softw Big Sci        (2025) 9:2

S. Kortner112    , W. H. Kostecka118    , V. V. Kostyukhin144    , A. Kotsokechagia37    , A. Kotwal52    , A. Koulouris37    ,
A. Kourkoumeli-Charalampidi74a,74b    , C. Kourkoumelis9    , E. Kourlitis112,ab    , O. Kovanda126    , R. Kowalewski168    ,
W. Kozanecki138    , A. S. Kozhin38    , V. A. Kramarenko38    , G. Kramberger95    ,  P. Kramer102    , M. W. Krasny130    ,
A. Krasznahorkay37    ,  A. C. Kraus118    ,   J. W. Kraus174    ,   J. A. Kremer49    ,  T. Kresse51    ,  L. Kretschmann174    ,
J. Kretzschmar94    , K. Kreul19    ,  P. Krieger158    , M. Krivos136    , K. Krizka21    , K. Kroeninger50    , H. Kroha112    ,
J. Kroll134    , J. Kroll131    , K. S. Krowpman109    , U. Kruchonak39    , H. Krüger25    , N. Krumnack82, M. C. Kruse52    ,
O. Kuchinskaia38    ,  S. Kuday3a    ,  S. Kuehn37    , R. Kuesters55    ,  T. Kuhl49    ,  V. Kukhtin39    ,  Y. Kulchitsky38,a    ,
S. Kuleshov140d,140b    , M. Kumar34g    , N. Kumari49    ,  P. Kumari159b    , A. Kupco134    , T. Kupfer50, A. Kupich38    ,
O. Kuprash55    ,  H. Kurashige86    ,  L. L. Kurchaninov159a    ,  O. Kurdysh67    ,  Y. A. Kurochkin38    ,  A. Kurova38    ,
M. Kuze157    , A. K. Kvam105    , J. Kvita125    , T. Kwan106    , N. G. Kyriacou108    , L. A. O. Laatu104    , C. Lacasta166    ,
F. Lacava76a,76b    , H. Lacker19    , D. Lacour130    , N. N. Lad98    ,  E. Ladygin39    , A. Lafarge41    ,  B. Laforge130    ,
T. Lagouri175    , F. Z. Lahbabi36a    , S. Lai56    , J. E. Lambert168    , S. Lammers69    , W. Lampl7    , C. Lampoudis155,d    ,
G. Lamprinoudis102,  A. N. Lancaster118    ,  E. Lançon30    ,  U. Landgraf55    ,  M. P. J. Landon96    ,  V. S. Lang55    ,
O. K. B. Langrekken128    ,  A. J. Lankford162    ,   F. Lanni37    ,  K. Lantzsch25    ,  A. Lanza74a    ,   J. F. Laporte138    ,
T. Lari72a    ,    F. Lasagni Manghi24b    ,  M. Lassnig37    ,   V. Latonova134    ,   A. Laurier153    ,   S. D. Lawlor142    ,
Z. Lawrence103    ,  R. Lazaridou170,  M. Lazzaroni72a,72b    ,  B. Le103,  E. M. Le Boulicaut52    ,  L. T. Le Pottier18a    ,
B. Leban24b,24a    , A. Lebedev82    , M. LeBlanc103    , F. Ledroit-Guillon61    , S. C. Lee151    , S. Lee48a,48b    , T. F. Lee94    ,
L. L. Leeuw34c    ,  H. P. Lefebvre97    ,  M. Lefebvre168    ,  C. Leggett18a    ,  G. Lehmann Miotto37    ,  M. Leigh57    ,
W. A. Leight105    ,  W. Leinonen116    ,  A. Leisos155,s    ,  M. A. L. Leite84c    ,   C. E. Leitgeb19    ,   R. Leitner136    ,
K. J. C. Leney45    , T. Lenz25    , S. Leone75a    , C. Leonidopoulos53    , A. Leopold147    , R. Les109    , C. G. Lester33    ,
M. Levchenko38    ,    J. Levêque4    ,   L. J. Levinson172    ,   G. Levrini24b,24a    ,  M. P. Lewicki88    ,   C. Lewis141    ,
D. J. Lewis4    , A. Li5    , B. Li63b    , C. Li63a, C-Q. Li112    , H. Li63a    , H. Li63b    , H. Li114a    , H. Li15    , H. Li63b    ,
J. Li63c    ,  K. Li141    ,  L. Li63c    ,  M. Li14,114c    ,  S. Li14,114c    ,  S. Li63d,63c    ,  T. Li5    ,  X. Li106    ,  Z. Li129    ,
Z. Li156    , Z. Li14,114c    , Z. Li63a    , S. Liang14,114c    , Z. Liang14    , M. Liberatore138    , B. Liberti77a    , K. Lie65c    ,
J. Lieber Marin84e    , H. Lien69    , H. Lin108    , K. Lin109    , R. E. Lindley7    , J. H. Lindon2    , J. Ling62    , E. Lipeles131    ,
A. Lipniacka17    ,  A. Lister167    ,   J. D. Little69    ,  B. Liu14    ,  B. X. Liu114b    ,  D. Liu63d,63c    ,  E. H. L. Liu21    ,
J. B. Liu63a    , J. K. K. Liu33    , K. Liu63d    , K. Liu63d,63c    , M. Liu63a    , M. Y. Liu63a    , P. Liu14    , Q. Liu63d,141,63c    ,
X. Liu63a    ,  X. Liu63b    ,  Y. Liu114b,114c    ,  Y. L. Liu63b    ,  Y. W. Liu63a    ,  S. L. Lloyd96    ,  E. M. Lobodzinska49    ,
P. Loch7    , T. Lohse19    , K. Lohwasser142    , E. Loiacono49    , M. Lokajicek134,*    ,  J. D. Lomas21    ,  J. D. Long165    ,
I. Longarini162    , R. Longo165    , I. Lopez Paz68    , A. Lopez Solis49    , N. A. Lopez-canelas7    , N. Lorenzo Martinez4    ,
A. M. Lory111    ,  M. Losada119a    ,  G. Löschcke Centeno149    ,  O. Loseva38    ,  X. Lou48a,48b    ,  X. Lou14,114c    ,
A. Lounis67    ,     P. A. Love93    ,   G. Lu14,114c    ,   M. Lu67    ,    S. Lu131    ,    Y. J. Lu66    ,   H. J. Lubatti141    ,
C. Luci76a,76b    ,   F. L. Lucio Alves114a    ,   F. Luehring69    ,    I. Luise148    ,  O. Lukianchuk67    ,  O. Lundberg147    ,
B. Lund-Jensen147,*    , N. A. Luongo6    , M. S. Lutz37    , A. B. Lux26    , D. Lynn30    , R. Lysak134    , E. Lytken100    ,
V. Lyubushkin39    ,   T. Lyubushkina39    ,  M. M. Lyukova148    ,  M.Firdaus M. Soberi53    ,  H. Ma30    ,  K. Ma63a    ,
L. L. Ma63b    , W. Ma63a    ,  Y. Ma124    ,  J. C. MacDonald102    ,  P. C. Machado De Abreu Farias84e    ,  R. Madar41    ,
T. Madula98    ,     J. Maeda86    ,    T. Maeno30    ,   H. Maguire142    ,    V. Maiboroda138    ,   A. Maio133a,133b,133d    ,
K. Maj87a    ,   O. Majersky49    ,    S. Majewski126    ,   N. Makovec67    ,    V. Maksimovic16    ,   B. Malaescu130    ,
Pa. Malecki88    ,   V. P. Maleev38    ,   F. Malek61,o    ,  M. Mali95    ,  D. Malito97    ,  U. Mallik81    ,   S. Maltezos10,
S. Malyukov39,    J. Mamuzic13    ,   G. Mancini54    ,  M. N. Mancini27    ,   G. Manco74a,74b    ,    J. P. Mandalia96    ,
S. S. Mandarry149    ,  I. Mandi´c95    ,  L. Manhaes de Andrade Filho84a    ,  I. M. Maniatis172    ,  J. Manjarres Ramos91    ,
D. C. Mankad172    , A. Mann111    , S. Manzoni37    , L. Mao63c    , X. Mapekula34c    , A. Marantis155,s    , G. Marchiori5    ,
M. Marcisovsky134    ,  C. Marcon72a    ,  M. Marinescu21    ,  S. Marium49    ,  M. Marjanovic123    ,  A. Markhoos55    ,
M. Markovitch67    ,   E. J. Marshall93    ,   Z. Marshall18a    ,   S. Marti-Garcia166    ,   J. Martin98    ,   T. A. Martin137    ,
V. J. Martin53    ,    B. Martin dit Latour17    ,    L. Martinelli76a,76b    ,   M. Martinez13,t    ,     P. Martinez Agullo166    ,
V. I. Martinez Outschoorn105    , P. Martinez Suarez13    , S. Martin-Haugh137    , G. Martinovicova136    , V. S. Martoiu28b    ,
A. C. Martyniuk98    ,  A. Marzin37    ,  D. Mascione79a,79b    ,  L. Masetti102    ,   J. Masik103    ,  A. L. Maslennikov38    ,
P. Massarotti73a,73b    ,   P. Mastrandrea75a,75b    ,  A. Mastroberardino44b,44a    ,   T. Masubuchi127    ,   T. Mathisen164    ,
J. Matousek136    ,     J. Maurer28b    ,    A. J. Maury67    ,    B. Maˇcek95    ,    D. A. Maximov38    ,    A. E. May103    ,
R. Mazini151    ,      I. Maznas118    ,   M. Mazza109    ,    S. M. Mazza139    ,    E. Mazzeo72a,72b    ,    C. Mc Ginn30    ,
J. P. Mc Gowan168    ,    S. P. Mc Kee108    ,   C. C. McCracken167    ,   E. F. McDonald107    ,   A. E. McDougall117    ,
J. A. Mcfayden149    ,    R. P. McGovern131    ,    R. P. Mckenzie34g    ,    T. C. Mclachlan49    ,   D. J. Mclaughlin98    ,
S. J. McMahon137    , C. M. Mcpartland94    , R. A. McPherson168,x    , S. Mehlhase111    , A. Mehta94    , D. Melini166    ,

123

### Página PDF 27

Comput Softw Big Sci        (2025) 9:2                                                          Page 27 of 35    2

B. R. Mellado Garcia34g    ,  A. H. Melo56    ,   F. Meloni49    ,  A. M. Mendes Jacques Da Costa103    ,  H. Y. Meng158    ,
L. Meng93    ,     S. Menke112    ,   M. Mentink37    ,    E. Meoni44b,44a    ,    G. Mercado118    ,     S. Merianos155    ,
G. Merino Arevaloe,  C. Merlassino70a,70c    ,  L. Merola73a,73b    ,  C. Meroni72a,72b    ,   J. Metcalfe6    ,  A. S. Mete6    ,
E. Meuser102    ,   C. Meyer69    ,    J-P. Meyer138    ,   R. P. Middleton137    ,    L. Mijovi´c53    ,   G. Mikenberg172    ,
M. Mikestikova134    ,   M. Mikuž95    ,   H. Mildner102    ,   A. Milic37    ,   D. W. Miller40    ,    E. H. Miller146    ,
L. S. Miller35    ,  A. Milov172    ,  D. A. Milstead48a,48b,   T. Min114a,  A. A. Minaenko38    ,    I. A. Minashvili152b    ,
L. Mince60    , A. I. Mincer120    , B. Mindur87a    , M. Mineev39    , Y. Mino89    , L. M. Mir13    , M. Miralles Lopez60    ,
M. Mironova18a    ,   M. C. Missio116    ,   A. Mitra170    ,    V. A. Mitsou166    ,    Y. Mitsumori113    ,   O. Miu158    ,
P. S. Miyagawa96    ,  T. Mkrtchyan64a    , M. Mlinarevic98    ,  T. Mlinarevic98    , M. Mlynarikova37    ,  S. Mobius20    ,
P. Mogg111    ,  M. H. Mohamed Farook115    ,  A. F. Mohammed14,114c    ,  S. Mohapatra42    ,  G. Mokgatitswane34g    ,
L. Moleri172    ,   B. Mondal144    ,    S. Mondal135    ,   K. Mönig49    ,   E. Monnier104    ,   L. Monsonis Romero166,
J. Montejo Berlingen13    ,    A. Montella48a,48b    ,   M. Montella122    ,     F. Montereali78a,78b    ,     F. Monticelli92    ,
S. Monzani70a,70c    , A. Morancho Tarda43    , N. Morange67    , A. L. Moreira De Carvalho49    , M. Moreno Llácer166    ,
C. Moreno Martinez57    ,  P. Morettini58b    , S. Morgenstern37    , M. Morii62    , M. Morinaga156    ,  F. Morodei76a,76b    ,
L. Morvaj37    ,    P. Moschovakos37    ,   B. Moser129    ,  M. Mosidze152b    ,   T. Moskalets45    ,    P. Moskvitina116    ,
J. Moss32,l    ,   P. Moszkowicz87a    ,  A. Moussa36d    ,   E. J. W. Moyse105    ,  O. Mtintsilana34g    ,   S. Muanza104    ,
J. Mueller132    , D. Muenstermann93    , R. Müller37    , G. A. Mullier164    , A. J. Mullin33, J. J. Mullin131, D. P. Mungo158    ,
D. Munoz Perez166    , F. J. Munoz Sanchez103    , M. Murin103    , W. J. Murray170,137    , M. Muškinja95    , C. Mwewa30    ,
A. G. Myagkov38,a    ,  A. J. Myers8    ,  G. Myers108    ,  M. Myska135    ,  B. P. Nachman18a    ,  O. Nackenhorst50    ,
K. Nagai129    , K. Nagano85    ,  J. L. Nagle30,af    , E. Nagy104    , A. M. Nairz37    , Y. Nakahama85    , K. Nakamura85    ,
K. Nakkalil5    , H. Nanjo127    , E. A. Narayanan115    , I. Naryshkin38    , L. Nasella72a,72b    , M. Naseri35    , S. Nasri119b    ,
C. Nass25    ,   G. Navarro23a    ,     J. Navarro-Gonzalez166    ,   R. Nayak154    ,   A. Nayaz19    ,    P. Y. Nechaeva38    ,
S. Nechaeva24b,24a    , F. Nechansky49    , L. Nedic129    , T. J. Neep21    , A. Negri74a,74b    , M. Negrini24b    , C. Nellist117    ,
C. Nelson106    , K. Nelson108    , S. Nemecek134    , M. Nessi37,i    , M. S. Neubauer165    , F. Neuhaus102    , J. Neundorf49    ,
P. R. Newman21    ,  C. W. Ng132    ,  Y. W. Y. Ng49    ,  B. Ngair119a    ,  H. D. N. Nguyen110    ,  R. B. Nickerson129    ,
R. Nicolaidou138    ,    J. Nielsen139    ,  M. Niemeyer56    ,    J. Niermann56    ,  N. Nikiforou37    ,   V. Nikolaenko38,a    ,
I. Nikolic-Audit130    , K. Nikolopoulos21    ,  P. Nilsson30    ,  I. Ninca49    , G. Ninio154    , A. Nisati76a    , N. Nishu2    ,
R. Nisius112    ,  J-E. Nitschke51    ,  E. K. Nkadimeng34g    ,  T. Nobe156    ,  T. Nommensen150    ,  M. B. Norfolk142    ,
B. J. Norman35    , M. Noury36a    ,   J. Novak95    ,  T. Novak95    ,  L. Novotny135    ,  R. Novotny115    ,  L. Nozka125    ,
K. Ntekas162    ,  N. M. J. Nunes De Moura Junior84b    ,  J. Ocariz130    ,  A. Ochi86    ,   I. Ochoa133a    ,  S. Oerdek49,u    ,
J. T. Offermann40    ,  A. Ogrodnik136    ,  A. Oh103    ,  C. C. Ohm147    ,  H. Oide85    ,  R. Oishi156    , M. L. Ojeda49    ,
Y. Okumura156    ,   L. F. Oleiro Seabra133a    ,    I. Oleksiyuk57    ,   S. A. Olivares Pino140d    ,   G. Oliveira Correa13    ,
D. Oliveira Damazio30    , J. L. Oliver162    , Ö. O. Öncel55    , A. P. O’Neill20    , A. Onofre133a,133e    , P. U. E. Onyisi11    ,
M. J. Oreglia40    ,  G. E. Orellana92    ,  D. Orestano78a,78b    ,  N. Orlando13    ,  R. S. Orr158    ,  L. M. Osojnak131    ,
R. Ospanov63a    ,   G. Otero y Garzon31    ,   H. Otono90    ,     P. S. Ott64a    ,   G. J. Ottino18a    ,   M. Ouchrif36d    ,
F. Ould-Saada128    , T. Ovsiannikova141    , M. Owen60    , R. E. Owen137    , V. E. Ozcan22a    , F. Ozturk88    , N. Ozturk8    ,
S. Ozturk83    , H. A. Pacey129    , A. Pacheco Pages13    , C. Padilla Aranda13    , G. Padovano76a,76b    , S. Pagan Griso18a    ,
G. Palacino69    , A. Palazzo71a,71b    ,  J. Pampel25    ,  J. Pan175    ,  T. Pan65a    , D. K. Panchal11    ,  C. E. Pandini117    ,
J. G. Panduro Vazquez137    ,   H. D. Pandya1    ,   H. Pang15    ,    P. Pani49    ,   G. Panizzo70a,70c    ,   L. Panwar130    ,
L. Paolozzi57    , S. Parajuli165    , A. Paramonov6    , C. Paraskevopoulos54    , D. Paredes Hernandez65b    , A. Pareti74a,74b    ,
K. R. Park42    ,    T. H. Park158    ,   M. A. Parker33    ,    F. Parodi58b,58a    ,    E. W. Parrish118    ,    V. A. Parrish53    ,
J. A. Parsons42    ,    U. Parzefall55    ,    B. Pascual Dias110    ,    L. Pascual Dominguez101    ,    E. Pasqualucci76a    ,
S. Passaggio58b    ,   F. Pastore97    ,   P. Patel88    ,  U. M. Patel52    ,   J. R. Pater103    ,   T. Pauly37    ,  C. I. Pazos161    ,
J. Pearkes146    , M. Pedersen128    , R. Pedro133a    ,  S. V. Peleganchuk38    , O. Penc37    ,  E. A. Pender53    ,  S. Peng15,
G. D. Penn175    , K. E. Penski111    , M. Penzin38    , B. S. Peralva84d    , A. P. Pereira Peixoto141    , L. Pereira Sanchez146    ,
D. V. Perepelitsa30,af    , G. Perera105    , E. Perez Codina159a    , M. Perganti10    , H. Pernegger37    , S. Perrella76a,76b    ,
O. Perrin41    , K. Peters49    , R. F. Y. Peters103    , B. A. Petersen37    , T. C. Petersen43    , E. Petit104    , V. Petousis135    ,
C. Petridou155,d    , T. Petru136    , A. Petrukhin144    , M. Pettee18a    , A. Petukhov38    , K. Petukhova37    , R. Pezoa140f    ,
L. Pezzotti37    ,   G. Pezzullo175    ,    T. M. Pham173    ,    T. Pham107    ,    P. W. Phillips137    ,   G. Piacquadio148    ,
E. Pianori18a    ,   F. Piazza126    ,  R. Piegaia31    ,  D. Pietreanu28b    ,  A. D. Pilkington103    ,  M. Pinamonti70a,70c    ,
J. L. Pinfold2    ,  B. C. Pinheiro Pereira133a    ,  A. E. Pinto Pinoargote138,138    ,  L. Pintucci70a,70c    ,  K. M. Piper149    ,
A. Pirttikoski57    , D. A. Pizzi35    , L. Pizzimento65b    , A. Pizzini117    , M.-A. Pleier30    , V. Pleskot136    , E. Plotnikova39,
G. Poddar96    , R. Poettgen100    , L. Poggioli130    , I. Pokharel56    , S. Polacek136    , G. Polesello74a    , A. Poley145,159a    ,

                                  123

### Página PDF 28

2  Page 28 of 35                                                    Comput Softw Big Sci        (2025) 9:2

A. Polini24b    , C. S. Pollard170    , Z. B. Pollock122    , E. Pompa Pacchi76a,76b    , N. I. Pond98    , D. Ponomarenko116    ,
L. Pontecorvo37    , S. Popa28a    , G. A. Popeneciu28d    , A. Poreba37    , D. M. Portillo Quintero159a    , S. Pospisil135    ,
M. A. Postill142    ,   P. Postolache28c    ,  K. Potamianos170    ,   P. A. Potepa87a    ,    I. N. Potrap39    ,   C. J. Potter33    ,
H. Potti150    ,   J. Poveda166    ,  M. E. Pozo Astigarraga37    ,  A. Prades Ibanez77a,77b    ,   J. Pretel168    ,  D. Price103    ,
M. Primavera71a    , L. Primomo70a,70c    , M. A. Principe Martin101    , R. Privara125    , T. Procter60    , M. L. Profﬁtt141    ,
N. Proklova131    ,  K. Prokoﬁev65c    ,  G. Proto112    ,    J. Proudfoot6    ,  M. Przybycien87a    ,  W. W. Przygoda87b    ,
A. Psallidas47    , J. E. Puddefoot142    , D. Pudzha55    , D. Pyatiizbyantseva38    , J. Qian108    , D. Qichen103    , Y. Qin13    ,
T. Qiu53    ,  A. Quadt56    ,  M. Queitsch-Maitland103    ,  G. Quetant57    ,  R. P. Quinn167    ,  G. Rabanal Bolanos62    ,
D. Rafanoharana55    ,  F. Raffaeli77a,77b    ,  F. Ragusa72a,72b    ,  J. L. Rainbolt40    ,  J. A. Raine57    ,  S. Rajagopalan30    ,
E. Ramakoti38    , L. Rambelli58b,58a    , I. A. Ramirez-Berend35    , K. Ran49,114c    , D. S. Rankin131    , N. P. Rapheeha34g    ,
H. Rasheed28b    ,    V. Raskina130    ,   D. F. Rassloff64a    ,   A. Rastogi18a    ,    S. Rave102    ,    S. Ravera58b,58a    ,
B. Ravina56    ,   I. Ravinovich172    , M. Raymond37    ,  A. L. Read128    ,  N. P. Readioff142    ,  D. M. Rebuzzi74a,74b    ,
G. Redlinger30    , A. S. Reed112    , K. Reeves27    , J. A. Reidelsturz174    , D. Reikher126    , A. Rej50    , C. Rembser37    ,
M. Renda28b    ,    F. Renner49    ,   A. G. Rennie162    ,   A. L. Rescia49    ,   S. Resconi72a    ,  M. Ressegotti58b,58a    ,
S. Rettie37    ,    J. G. Reyes Rivera109    ,   E. Reynolds18a    ,   O. L. Rezanova38    ,    P. Reznicek136    ,   H. Riani36d    ,
N. Ribaric93    ,    E. Ricci79a,79b    ,   R. Richter112    ,    S. Richter48a,48b    ,    E. Richter-Was87b    ,   M. Ridel130    ,
S. Ridouani36d    ,    P. Rieck120    ,    P. Riedler37    ,   E. M. Riefel48a,48b    ,    J. O. Rieger117    ,  M. Rijssenbeek148    ,
M. Rimoldi37    ,   L. Rinaldi24b,24a    ,    P. Rincke56,164    ,   T. T. Rinn30    ,  M. P. Rinnagel111    ,   G. Ripellino164    ,
I. Riu13    ,    J. C. Rivera Vergara168    ,   F. Rizatdinova124    ,   E. Rizvi96    ,   B. R. Roberts18a    ,   S. S. Roberts139    ,
S. H. Robertson106,x    , D. Robinson33    , M. Robles Manzano102    , A. Robson60    , A. Rocchi77a,77b    , C. Roda75a,75b    ,
S. Rodriguez Bosca37    , Y. Rodriguez Garcia23a    , A. Rodriguez Rodriguez55    , A. M. Rodríguez Vera118    , S. Roe37,
J. T. Roemer37    ,  A. R. Roepe-Gier139    ,  O. Røhne128    ,   R. A. Rojas105    ,   C. P. A. Roland130    ,    J. Roloff30    ,
A. Romaniouk38    ,    E. Romano74a,74b    ,   M. Romano24b    ,   A. C. Romero Hernandez165    ,   N. Rompotis94    ,
L. Roos130    ,   S. Rosati76a    ,  B. J. Rosser40    ,  E. Rossi129    ,  E. Rossi73a,73b    ,  L. P. Rossi62    ,  L. Rossini55    ,
R. Rosten122    ,  M. Rotaru28b    ,  B. Rottler55    ,  C. Rougier91    ,  D. Rousseau67    ,  D. Rousso49    ,  A. Roy165    ,
S. Roy-Garand158    , A. Rozanov104    ,  Z. M. A. Rozario60    ,  Y. Rozen153    , A. Rubio Jimenez166    , A. J. Ruby94    ,
V. H. Ruelas Rivera19    , T. A. Ruggeri1    , A. Ruggiero129    , A. Ruiz-Martinez166    , A. Rummler37    , Z. Rurikova55    ,
N. A. Rusakovich39    ,  H. L. Russell168    ,  G. Russo76a,76b    ,    J. P. Rutherfoord7    ,   S. Rutherford Colmenares33    ,
M. Rybar136    , E. B. Rye128    , A. Ryzhov45    , J. A. Sabater Iglesias57    , H.F-W. Sadrozinski139    , F. Safai Tehrani76a    ,
B. Safarzadeh Samani137    , S. Saha1    , M. Sahinsoy83    , A. Saibel166    , M. Saimpert138    , M. Saito156    , T. Saito156    ,
A. Sala72a,72b    ,  D. Salamani37    ,  A. Salnikov146    ,    J. Salt166    ,  A. Salvador Salas154    ,  D. Salvatore44b,44a    ,
F. Salvatore149    , A. Salzburger37    , D. Sammel55    ,  E. Sampson93    , D. Sampsonidis155,d    , D. Sampsonidou126    ,
J. Sánchez166    , V. Sanchez Sebastian166    , H. Sandaker128    , C. O. Sander49    , J. A. Sandesara105    , M. Sandhoff174    ,
C. Sandoval23b    , L. Sanﬁlippo64a    , D. P. C. Sankey137    , T. Sano89    , A. Sansoni54    , L. Santi37,76b    , C. Santoni41    ,
H. Santos133a,133b    ,  A. Santra172    ,  E. Sanzani24b,24a    ,  K. A. Saoucha163    ,  J. G. Saraiva133a,133d    ,  J. Sardain7    ,
O. Sasaki85    ,   K. Sato160    ,   C. Sauer64b,   E. Sauvan4    ,    P. Savard158,ad    ,   R. Sawada156    ,   C. Sawyer137    ,
L. Sawyer99    ,   C. Sbarra24b    ,   A. Sbrizzi24b,24a    ,    T. Scanlon98    ,     J. Schaarschmidt141    ,   U. Schäfer102    ,
A. C. Schaffer67,45    , D. Schaile111    , R. D. Schamberger148    , C. Scharf19    , M. M. Schefer20    , V. A. Schegelsky38    ,
D. Scheirich136    ,  M. Schernau162    ,  C. Scheulen56    ,  C. Schiavi58b,58a    ,  M. Schioppa44b,44a    ,  B. Schlag146,n    ,
K. E. Schleicher55    ,  S. Schlenker37    ,  J. Schmeing174    , M. A. Schmidt174    ,  K. Schmieden102    ,  C. Schmitt102    ,
N. Schmitt102    ,    S. Schmitt49    ,    L. Schoeffel138    ,   A. Schoening64b    ,     P. G. Scholer35    ,    E. Schopf129    ,
M. Schott25    ,  J. Schovancova37    ,  S. Schramm57    ,  T. Schroer57    , H-C. Schultz-Coulon64a    , M. Schumacher55    ,
B. A. Schumm139    , Ph. Schune138    , A. J. Schuy141    , H. R. Schwartz139    , A. Schwartzman146    , T. A. Schwarz108    ,
Ph. Schwemling138    ,   R. Schwienhorst109    ,   F. G. Sciacca20    ,   A. Sciandra30    ,   G. Sciolla27    ,   F. Scuri75a    ,
C. D. Sebastiani94    ,   K. Sedlaczek118    ,    S. C. Seidel115    ,   A. Seiden139    ,   B. D. Seidlitz42    ,   C. Seitz49    ,
J. M. Seixas84b    , G. Sekhniaidze73a    , L. Selem61    , N. Semprini-Cesari24b,24a    , D. Sengupta57    , V. Senthilkumar166    ,
L. Serin67    ,  M. Sessa77a,77b    ,  H. Severini123    ,   F. Sforza58b,58a    ,  A. Sfyrla57    ,  Q. Sha14    ,  E. Shabalina56    ,
A. H. Shah33    ,  R. Shaheen147    ,   J. D. Shahinian131    ,  D. Shaked Renous172    ,  L. Y. Shan14    ,  M. Shapiro18a    ,
A. Sharma37    , A. S. Sharma167    ,  P. Sharma81    ,  P. B. Shatalov38    , K. Shaw149    ,  S. M. Shaw103    , Q. Shen63c    ,
D. J. Sheppard145    ,  P. Sherwood98    , L. Shi98    , X. Shi14    , S. Shimizu85    , C. O. Shimmin175    ,  J. D. Shinner97    ,
I. P. J. Shipsey129    ,   S. Shirabe90    ,  M. Shiyakova39,v    ,  M. J. Shochet40    ,  D. R. Shope128    ,  B. Shrestha123    ,
S. Shrestha122,ag    , M. J. Shroff168    ,  P. Sicho134    ,  A. M. Sickles165    ,  E. Sideras Haddad34g    ,  A. C. Sidley117    ,
A. Sidoti24b    , F. Siegert51    , Dj. Sijacki16    , F. Sili92    , J. M. Silva53    , I. Silva Ferreira84b    , M. V. Silva Oliveira30    ,

123

### Página PDF 29

Comput Softw Big Sci        (2025) 9:2                                                          Page 29 of 35    2

S. B. Silverstein48a    ,  S. Simion67,  R. Simoniello37    ,  E. L. Simpson103    ,  H. Simpson149    ,  L. R. Simpson108    ,
N. D. Simpson100,   S. Simsek83    ,   S. Sindhu56    ,   P. Sinervo158    ,   S. Singh158    ,   S. Sinha49    ,   S. Sinha103    ,
M. Sioli24b,24a    ,    I. Siral37    ,   E. Sitnikova49    ,    J. Sjölin48a,48b    ,  A. Skaf56    ,   E. Skorda21    ,   P. Skubic123    ,
M. Slawinska88    ,   V. Smakhtin172,  B. H. Smart137    ,   S.Yu. Smirnov38    ,   Y. Smirnov38    ,   L. N. Smirnova38,a    ,
O. Smirnova100    ,   A. C. Smith42    ,   D. R. Smith162,    E. A. Smith40    ,   H. A. Smith129    ,     J. L. Smith103    ,
R. Smith146,   M. Smizanska93    ,   K. Smolek135    ,   A. A. Snesarev38    ,    S. R. Snider158    ,   H. L. Snoek117    ,
S. Snyder30    ,  R. Sobie168,x    ,  A. Soffer154    ,  C. A. Solans Sanchez37    ,  E.Yu. Soldatov38    ,  U. Soldevila166    ,
A. A. Solodkov38    ,  S. Solomon27    ,  A. Soloshenko39    ,  K. Solovieva55    ,  O. V. Solovyanov41    ,  P. Sommer51    ,
A. Sonay13    ,   W. Y. Song159b    ,   A. Sopczak135    ,   A. L. Sopio98    ,    F. Sopkova29b    ,     J. D. Sorenson115    ,
I. R. Sotarriva Alvarez157    ,  V. Sothilingam64a,  O. J. Soto Sandoval140c,140b    ,  S. Sottocornola69    ,  R. Soualah163    ,
Z. Soumaimi36e    ,   D. South49    ,   N. Soybelman172    ,    S. Spagnolo71a,71b    ,  M. Spalla112    ,   D. Sperlich55    ,
G. Spigo37    , B. Spisso73a,73b    , D. P. Spiteri60    , M. Spousta136    , E. J. Staats35    , R. Stamen64a    , A. Stampekis21    ,
M. Standke25    , E. Stanecka88    , W. Stanek-Maslouska49    , M. V. Stange51    , B. Stanislaus18a    , M. M. Stanitzki49    ,
B. Stapf49    , E. A. Starchenko38    , G. H. Stark139    ,  J. Stark91    ,  P. Staroba134    ,  P. Starovoitov64a    ,  S. Stärz106    ,
R. Staszewski88    , G. Stavropoulos47    , P. Steinberg30    , B. Stelzer145,159a    , H. J. Stelzer132    , O. Stelzer-Chilton159a    ,
H. Stenzel59    ,   T. J. Stevenson149    ,  G. A. Stewart37    ,   J. R. Stewart124    ,  M. C. Stockton37    ,  G. Stoicea28b    ,
M. Stolarski133a    ,  S. Stonjek112    , A. Straessner51    ,  J. Strandberg147    ,  S. Strandberg48a,48b    , M. Stratmann174    ,
M. Strauss123    ,   T. Strebler104    ,    P. Strizenec29b    ,   R. Ströhmer169    ,   D. M. Strom126    ,   R. Stroynowski45    ,
A. Strubig48a,48b    ,   S. A. Stucci30    ,   B. Stugu17    ,    J. Stupak123    ,   N. A. Styles49    ,   D. Su146    ,   S. Su63a    ,
W. Su63d    ,  X. Su63a    ,  D. Suchy29a    ,  K. Sugizaki156    ,  V. V. Sulin38    , M. J. Sullivan94    ,  D. M. S. Sultan129    ,
L. Sultanaliyeva38    ,   S. Sultansoy3b    ,   T. Sumida89    ,   S. Sun173    ,  O. Sunneborn Gudnadottir164    ,  N. Sur104    ,
M. R. Sutton149    , H. Suzuki160    , M. Svatos134    , M. Swiatlowski159a    , T. Swirski169    , I. Sykora29a    , M. Sykora136    ,
T. Sykora136    , D. Ta102    , K. Tackmann49,u    , A. Taffard162    , R. Taﬁrout159a    , J. S. Tafoya Vargas67    , Y. Takubo85    ,
M. Talby104    , A. A. Talyshev38    , K. C. Tam65b    , N. M. Tamir154, A. Tanaka156    ,  J. Tanaka156    , R. Tanaka67    ,
M. Tanasini148    ,    Z. Tao167    ,    S. Tapia Araya140f    ,    S. Tapprogge102    ,   A. Tarek Abouelfadl Mohamed109    ,
S. Tarem153    ,  K. Tariq14    ,  G. Tarna28b    ,  G. F. Tartarelli72a    , M. J. Tartarin91    ,  P. Tas136    , M. Tasevsky134    ,
E. Tassi44b,44a    ,   A. C. Tate165    ,   G. Tateno156    ,    Y. Tayalati36e,w    ,   G. N. Taylor107    ,   W. Taylor159b    ,
R. Teixeira De Lima146    ,    P. Teixeira-Dias97    ,    J. J. Teoh158    ,   K. Terashi156    ,    J. Terron101    ,   S. Terzo13    ,
M. Testa54    , R. J. Teuscher158,x    , A. Thaler80    , O. Theiner57    , N. Themistokleous53    , T. Theveneaux-Pelzer104    ,
O. Thielmann174    , D. W. Thomas97,  J. P. Thomas21    , E. A. Thompson18a    ,  P. D. Thompson21    , E. Thomson131    ,
R. E. Thornberry45    ,   C. Tian63a    ,   Y. Tian56    ,   V. Tikhomirov38,a    ,   Yu.A. Tikhonov38    ,   S. Timoshenko38,
D. Timoshyn136    ,  E. X. L. Ting1    ,   P. Tipton175    ,  A. Tishelman-Charny30    ,   S. H. Tlou34g    ,  K. Todome157    ,
S. Todorova-Nova136    , S. Todt51, L. Toffolin70a,70c    , M. Togawa85    ,  J. Tojo90    , S. Tokár29a    , K. Tokushuku85    ,
O. Toldaiev69    ,  M. Tomoto85,113    ,  L. Tompkins146,n    ,  K. W. Topolnicki87b    ,  E. Torrence126    ,  H. Torres91    ,
E. Torró Pastor166    , M. Toscani31    , C. Tosciri40    , M. Tost11    , D. R. Tovey142    , I. S. Trandaﬁr28b    , T. Trefzger169    ,
A. Tricoli30    ,    I. M. Trigger159a    ,   S. Trincaz-Duvoid130    ,   D. A. Trischuk27    ,   B. Trocmé61    ,   A. Tropina39,
L. Truong34c    , M. Trzebinski88    , A. Trzupek88    ,  F. Tsai148    , M. Tsai108    , A. Tsiamis155,d    ,  P. V. Tsiareshka38,
S. Tsigaridas159a    ,    A. Tsirigotis155,s    ,     V. Tsiskaridze158    ,     E. G. Tskhadadze152a    ,   M. Tsopoulou155    ,
Y. Tsujikawa89    ,  I. I. Tsukerman38    ,  V. Tsulaia18a    ,  S. Tsuno85    , K. Tsuri121    , D. Tsybychev148    ,  Y. Tu65b    ,
A. Tudorache28b    ,   V. Tudorache28b    ,  A. N. Tuna62    ,   S. Turchikhin58b,58a    ,    I. Turk Cakir3a    ,  R. Turra72a    ,
T. Turtuvshin39    , P. M. Tuts42    , S. Tzamarias155,d    , E. Tzovara102    , F. Ukegawa160    , P. A. Ulloa Poblete140c,140b    ,
E. N. Umaka30    , G. Unal37    , A. Undrus30    , G. Unel162    , J. Urban29b    , P. Urrejola140a    , G. Usai8    , R. Ushioda157    ,
M. Usman110    ,  Z. Uysal83    ,  V. Vacek135    ,  B. Vachon106    ,  T. Vafeiadis37    ,  A. Vaitkus98    ,  C. Valderanis111    ,
E. Valdes Santurio48a,48b    ,  M. Valente159a    ,   S. Valentinetti24b,24a    ,   A. Valero166    ,   E. Valiente Moreno166    ,
A. Vallier91    ,     J. A. Valls Ferrer166    ,   D. R. Van Arneman117    ,    T. R. Van Daalen141    ,   A. Van Der Graaf50    ,
P. Van Gemmeren6    , M. Van Rijnbach37    , S. Van Stroud98    ,  I. Van Vulpen117    ,  P. Vana136    , M. Vanadia77a,77b    ,
W. Vandelli37    , E. R. Vandewall124    , D. Vannicola154    , L. Vannoli54    , R. Vari76a    , E. W. Varnes7    , C. Varni18b    ,
T. Varol151    , D. Varouchas67    , L. Varriale166    , K. E. Varvell150    , M. E. Vasile28b    , L. Vaslin85, G. A. Vasquez168    ,
A. Vasyukov39    ,  L. M. Vaughan124    ,  R. Vavricka102,   T. Vazquez Schroeder37    ,   J. Veatch32    ,  V. Vecchio103    ,
M. J. Veen105    ,    I. Veliscek30    ,   L. M. Veloce158    ,   F. Veloso133a,133c    ,   S. Veneziano76a    ,  A. Ventura71a,71b    ,
S. Ventura Gonzalez138    ,  A. Verbytskyi112    ,  M. Verducci75a,75b    ,  C. Vergis96    ,  M. Verissimo De Araujo84b    ,
W. Verkerke117    , J. C. Vermeulen117    , C. Vernieri146    , M. Vessella105    , M. C. Vetterli145,ad    , A. Vgenopoulos102    ,
N. Viaux Maira140f    ,     T. Vickey142    ,    O. E. Vickey Boeriu142    ,    G. H. A. Viehhauser129    ,    L. Vigani64b    ,

                                  123

### Página PDF 30

2  Page 30 of 35                                                    Comput Softw Big Sci        (2025) 9:2

M. Vigl112    ,  M. Villa24b,24a    ,  M. Villaplana Perez166    ,   E. M. Villhauer53,   E. Vilucchi54    ,  M. G. Vincter35    ,
A. Visibile117,  C. Vittori37    ,   I. Vivarelli24b,24a    ,  E. Voevodina112    ,  F. Vogel111    ,  J. C. Voigt51    ,  P. Vokac135    ,
Yu. Volkotrub87b   ,J. Von Ahnen49  ,E. Von Toerne25  ,B. Vormwald37  ,V. Vorobel136  ,K. Vorobev38  ,M. Vos166    ,
K. Voss144    , M. Vozak117    ,  L. Vozdecky123    ,  N. Vranjes16    , M. Vranjes Milosavljevic16    , M. Vreeswijk117    ,
N. K. Vu63d,63c    , R. Vuillermet37    , O. Vujinovic102    , I. Vukotic40    , S. Wada160    , C. Wagner105, J. M. Wagner18a    ,
W. Wagner174    , S. Wahdan174    , H. Wahlberg92    ,  J. Walder137    , R. Walker111    , W. Walkowiak144    , A. Wall131    ,
E. J. Wallin100    ,   T. Wamorkar6    ,  A. Z. Wang139    ,  C. Wang102    ,  C. Wang11    ,  H. Wang18a    ,   J. Wang65c    ,
P. Wang98    , R. Wang62    , R. Wang6    , S. M. Wang151    , S. Wang63b    , S. Wang14    , T. Wang63a    , W. T. Wang81    ,
W. Wang14    , X. Wang114a    , X. Wang165    , X. Wang63c    , Y. Wang63d    , Y. Wang114a    , Y. Wang63a    , Z. Wang108    ,
Z. Wang63d,52,63c    ,   Z. Wang108    ,   A. Warburton106    ,   R. J. Ward21    ,   N. Warrack60    ,    S. Waterhouse97    ,
A. T. Watson21    , H. Watson60    , M. F. Watson21    , E. Watton60,137    , G. Watts141    , B. M. Waugh98    , J. M. Webb55    ,
C. Weber30    , H. A. Weber19    , M. S. Weber20    ,  S. M. Weber64a    , C. Wei63a    ,  Y. Wei55    , A. R. Weidberg129    ,
E. J. Weik120    ,  J. Weingarten50    , C. Weiser55    , C. J. Wells49    ,  T. Wenaus30    , B. Wendland50    ,  T. Wengler37    ,
N. S. Wenke112, N. Wermes25    , M. Wessels64a    , A. M. Wharton93    , A. S. White62    , A. White8    , M. J. White1    ,
D. Whiteson162    , L. Wickremasinghe127    , W. Wiedenmann173    , M. Wielers137    , C. Wiglesworth43    , D. J. Wilbern123,
H. G. Wilkens37    ,  J. J. H. Wilkinson33    ,  D. M. Williams42    ,  H. H. Williams131,  S. Williams33    ,  S. Willocq105    ,
B. J. Wilson103    ,  P. J. Windischhofer40    ,  F. I. Winkel31    ,  F. Winklmeier126    ,  B. T. Winter55    ,  J. K. Winter103    ,
M. Wittgen146, M. Wobisch99    , T. Wojtkowski61, Z. Wolffs117    , J. Wollrath162, M. W. Wolter88    , H. Wolters133a,133c    ,
M. C. Wong139,  E. L. Woodward42    ,  S. D. Worm49    ,  B. K. Wosiek88    ,  K. W. Wo´zniak88    ,  S. Wozniewski56    ,
K. Wraight60    ,   C. Wu21    ,  M. Wu114b    ,  M. Wu116    ,   S. L. Wu173    ,  X. Wu57    ,   Y. Wu63a    ,   Z. Wu4    ,
J. Wuerzinger112,ab    ,   T. R. Wyatt103    ,  B. M. Wynne53    ,  S. Xella43    ,  L. Xia114a    ,  M. Xia15    ,  M. Xie63a    ,
S. Xin14,114c    , A. Xiong126    ,  J. Xiong18a    , D. Xu14    , H. Xu63a    , L. Xu63a    , R. Xu131    , T. Xu108    , Y. Xu15    ,
Z. Xu53    ,  Z. Xu114a,  B. Yabsley150    ,  S. Yacoob34a    ,  Y. Yamaguchi85    ,  E. Yamashita156    ,  H. Yamauchi160    ,
T. Yamazaki18a    , Y. Yamazaki86    , J. Yan63c, S. Yan60    , Z. Yan105    , H. J. Yang63c,63d    , H. T. Yang63a    , S. Yang63a    ,
T. Yang65c    ,  X. Yang37    ,  X. Yang14    ,  Y. Yang45    ,  Y. Yang63a,  Z. Yang63a    ,  W-M. Yao18a    ,  H. Ye114a    ,
H. Ye56    ,   J. Ye14    ,   S. Ye30    ,  X. Ye63a    ,  Y. Yeh98    ,    I. Yeletskikh39    ,  B. K. Yeo18b    ,  M. R. Yexley98    ,
T. P. Yildirim129    ,   P. Yin42    ,  K. Yorita171    ,  S. Younas28b    ,  C. J. S. Young37    ,  C. Young146    ,  C. Yu14,114c    ,
Y. Yu63a    , J. Yuan14,114c    , M. Yuan108    , R. Yuan63d,63c    , L. Yue98    , M. Zaazoua63a    , B. Zabinski88    , E. Zaid53,
Z. K. Zak88    ,   T. Zakareishvili166    ,   S. Zambito57    ,    J. A. Zamora Saa140d,140b    ,    J. Zang156    ,   D. Zanzi55    ,
O. Zaplatilek135    ,  C. Zeitnitz174    , H. Zeng14    ,  J. C. Zeng165    ,  D. T. Zenger Jr27    , O. Zenin38    ,  T. Ženiš29a    ,
S. Zenz96    ,   S. Zerradi36a    ,  D. Zerwas67    ,  M. Zhai14,114c    ,  D. F. Zhang142    ,    J. Zhang63b    ,    J. Zhang6    ,
K. Zhang14,114c    ,  L. Zhang63a    ,  L. Zhang114a    ,  P. Zhang14,114c    ,  R. Zhang173    ,  S. Zhang108    ,  S. Zhang91    ,
T. Zhang156    , X. Zhang63c    , X. Zhang63b    , Y. Zhang63c    , Y. Zhang98    , Y. Zhang114a    , Z. Zhang18a    , Z. Zhang63b    ,
Z. Zhang67    , H. Zhao141    , T. Zhao63b    , Y. Zhao139    , Z. Zhao63a    , Z. Zhao63a    , A. Zhemchugov39    , J. Zheng114a    ,
K. Zheng165    , X. Zheng63a    ,  Z. Zheng146    , D. Zhong165    , B. Zhou108    , H. Zhou7    , N. Zhou63c    ,  Y. Zhou15,
Y. Zhou114a    , Y. Zhou7, C. G. Zhu63b    , J. Zhu108    , X. Zhu63d, Y. Zhu63c    , Y. Zhu63a    , X. Zhuang14    , K. Zhukov69    ,
N. I. Zimine39   ,J. Zinsser64b  ,M. Ziolkowski144  ,L. Živkovi´c16  ,A. Zoccoli24b,24a  ,K. Zoch62  ,T. G. Zorbas142    ,
O. Zormpa47    , W. Zou42    , L. Zwalinski37

  1 Department of Physics, University of Adelaide, Adelaide, Australia
 2 Department of Physics, University of Alberta, Edmonton, AB, Canada
  3 (a)Department of Physics, Ankara University, Ankara, Türkiye; (b)Division of Physics, TOBB University of Economics
  and Technology, Ankara, Türkiye
 4 LAPP, Université Savoie Mont Blanc, CNRS/IN2P3, Annecy, France
  5 APC, Université Paris Cité, CNRS/IN2P3, Paris, France
  6 High Energy Physics Division, Argonne National Laboratory, Argonne, IL, USA
  7 Department of Physics, University of Arizona, Tucson, AZ, USA
  8 Department of Physics, University of Texas at Arlington, Arlington, TX, USA
  9 Physics Department, National and Kapodistrian University of Athens, Athens, Greece
10 Physics Department, National Technical University of Athens, Zografou, Greece
 11 Department of Physics, University of Texas at Austin, Austin, TX, USA
12 Institute of Physics, Azerbaijan Academy of Sciences, Baku, Azerbaijan
 13 Institut de Física d’Altes Energies (IFAE), Barcelona Institute of Science and Technology, Barcelona, Spain

123

### Página PDF 31

Comput Softw Big Sci        (2025) 9:2                                                          Page 31 of 35    2

14 Institute of High Energy Physics, Chinese Academy of Sciences, Beijing, China
 15 Physics Department, Tsinghua University, Beijing, China
 16 Institute of Physics, University of Belgrade, Belgrade, Serbia
 17 Department for Physics and Technology, University of Bergen, Bergen, Norway
 18 (a)Physics Division, Lawrence Berkeley National Laboratory, Berkeley, CA, USA; (b)University of California, Berkeley,
  CA, USA
 19 Institut für Physik, Humboldt Universität zu Berlin, Berlin, Germany
20 Albert Einstein Center for Fundamental Physics and Laboratory for High Energy Physics, University of Bern, Bern,
   Switzerland
 21 School of Physics and Astronomy, University of Birmingham, Birmingham, UK
22 (a)Department of Physics, Bogazici University, Istanbul, Türkiye; (b)Department of Physics Engineering, Gaziantep
   University, Gaziantep, Türkiye; (c)Department of Physics, Istanbul University, Istanbul, Türkiye
 23 (a)Facultad de Ciencias y Centro de Investigaciónes, Universidad Antonio Nariño, Bogotá, Colombia; (b)Departamento
   de Física, Universidad Nacional de Colombia, Bogotá, Colombia
24 (a)Dipartimento di Fisica e Astronomia A. Righi, Università di Bologna, Bologna, Italy; (b)INFN Sezione di Bologna,
   Bologna, Italy
 25 Physikalisches Institut, Universität Bonn, Bonn, Germany
 26 Department of Physics, Boston University, Boston, MA, USA
 27 Department of Physics, Brandeis University, Waltham, MA, USA
 28 (a)Transilvania University of Brasov, Brasov, Romania; (b)Horia Hulubei National Institute of Physics and Nuclear
   Engineering, Bucharest, Romania; (c)Department of Physics, Alexandru Ioan Cuza University of Iasi, Iasi,
  Romania; (d)National Institute for Research and Development of Isotopic and Molecular Technologies, Physics
   Department, Cluj-Napoca, Romania; (e)National University of Science and Technology Politechnica, Bucharest,
  Romania; (f)West University in Timisoara, Timisoara, Romania; (g)Faculty of Physics, University of Bucharest,
   Bucharest, Romania
 29 (a)Faculty of Mathematics, Physics and Informatics, Comenius University, Bratislava, Slovakia; (b)Department of
   Subnuclear Physics, Institute of Experimental Physics of the Slovak Academy of Sciences, Kosice, Slovak Republic
30 Physics Department, Brookhaven National Laboratory, Upton, NY, USA
 31 Universidad de Buenos Aires, Facultad de Ciencias Exactas y Naturales, Departamento de Física, y CONICET, Instituto
   de Física de Buenos Aires (IFIBA), Buenos Aires, Argentina
32 California State University, Los Angeles, CA, USA
 33 Cavendish Laboratory, University of Cambridge, Cambridge, UK
34 (a)Department of Physics, University of Cape Town, Cape Town, South Africa; (b)iThemba Labs, Western Cape, South
   Africa; (c)Department of Mechanical Engineering Science, University of Johannesburg, Johannesburg,
   South Africa; (d)National Institute of Physics, University of the Philippines Diliman (Philippines), Quezon City,
   Philippines; (e)University of South Africa, Department of Physics, Pretoria, South Africa; (f)University of Zululand,
  KwaDlangezwa, South Africa; (g)School of Physics, University of the Witwatersrand, Johannesburg, South Africa
 35 Department of Physics, Carleton University, Ottawa, ON, Canada
 36 (a)Faculté des Sciences Ain Chock, Réseau Universitaire de Physique des Hautes Energies-Université Hassan II,
   Casablanca, Morocco; (b)Faculté des Sciences, Université Ibn-Tofail, Kénitra, Morocco; (c)Faculté des Sciences
   Semlalia, Université Cadi Ayyad, LPHEA-Marrakech, Marrakech, Morocco; (d)LPMR, Faculté des Sciences, Université
  Mohamed Premier, Oujda, Morocco; (e)Faculté des sciences, Université Mohammed V, Rabat, Morocco; (f)Institute of
   Applied Physics, Mohammed VI Polytechnic University, Ben Guerir, Morocco
 37 CERN, Geneva, Switzerland
 38 Afﬁliated with an institute covered by a cooperation agreement with CERN, Geneva, Switzerland
 39 Afﬁliated with an international laboratory covered by a cooperation agreement with CERN, Geneva, Switzerland
40 Enrico Fermi Institute, University of Chicago, Chicago, IL, USA
 41 LPC, Université Clermont Auvergne, CNRS/IN2P3, Clermont-Ferrand, France
42 Nevis Laboratory, Columbia University, Irvington, NY, USA
 43 Niels Bohr Institute, University of Copenhagen, Copenhagen, Denmark
44 (a)Dipartimento di Fisica, Università della Calabria, Rende, Italy; (b)INFN Gruppo Collegato di Cosenza, Laboratori
   Nazionali di Frascati, Frascati, Italy
 45 Physics Department, Southern Methodist University, Dallas, TX, USA

                                  123

### Página PDF 32

2  Page 32 of 35                                                    Comput Softw Big Sci        (2025) 9:2

46 Physics Department, University of Texas at Dallas, Richardson, TX, USA
47 National Centre for Scientiﬁc Research “Demokritos”, Agia Paraskevi, Greece
48 (a)Department of Physics, Stockholm University, Stockholm, Sweden; (b)Oskar Klein Centre, Stockholm, Sweden
49 Deutsches Elektronen-Synchrotron DESY, Hamburg and Zeuthen, Hamburg, Germany
50 Fakultät Physik , Technische Universität Dortmund, Dortmund, Germany
51 Institut für Kern- und Teilchenphysik, Technische Universität Dresden, Dresden, Germany
52 Department of Physics, Duke University, Durham, NC, USA
53 SUPA-School of Physics and Astronomy, University of Edinburgh, Edinburgh, UK
54 INFN e Laboratori Nazionali di Frascati, Frascati, Italy
55 Physikalisches Institut, Albert-Ludwigs-Universität Freiburg, Freiburg, Germany
56 II. Physikalisches Institut, Georg-August-Universität Göttingen, Göttingen, Germany
57 Département de Physique Nucléaire et Corpusculaire, Université de Genève, Genève, Switzerland
58 (a)Dipartimento di Fisica, Università di Genova, Genova, Italy; (b)INFN Sezione di Genova, Genova, Italy
59 II. Physikalisches Institut, Justus-Liebig-Universität Giessen, Giessen, Germany
60 SUPA-School of Physics and Astronomy, University of Glasgow, Glasgow, UK
61 LPSC, Université Grenoble Alpes, CNRS/IN2P3, Grenoble INP, Grenoble, France
62 Laboratory for Particle Physics and Cosmology, Harvard University, Cambridge, MA, USA
63 (a)Department of Modern Physics and State Key Laboratory of Particle Detection and Electronics, University of Science
  and Technology of China, Hefei, China; (b)Institute of Frontier and Interdisciplinary Science and Key Laboratory of
   Particle Physics and Particle Irradiation (MOE), Shandong University, Qingdao, China; (c)School of Physics and
  Astronomy, Shanghai Jiao Tong University, Key Laboratory for Particle Astrophysics and Cosmology (MOE), SKLPPC,
  Shanghai, China; (d)Tsung-Dao Lee Institute, Shanghai, China; (e)School of Physics and Microelectronics, Zhengzhou
   University, China
64 (a)Kirchhoff-Institut für Physik, Ruprecht-Karls-Universität Heidelberg, Heidelberg, Germany; (b)Physikalisches Institut,
  Ruprecht-Karls-Universität Heidelberg, Heidelberg, Germany
65 (a)Department of Physics, Chinese University of Hong Kong, Shatin, N.T., Hong Kong; (b)Department of Physics,
  University of Hong Kong, Pok Fu Lam, Hong Kong, China; (c)Department of Physics and Institute for Advanced Study,
  Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, Hong Kong, China
66 Department of Physics, National Tsing Hua University, Hsinchu, Taiwan
67 IJCLab, Université Paris-Saclay, CNRS/IN2P3, 91405 Orsay, France
68 Centro Nacional de Microelectrónica (IMB-CNM-CSIC), Barcelona, Spain
69 Department of Physics, Indiana University, Bloomington, IN, USA
70 (a)INFN Gruppo Collegato di Udine, Sezione di Trieste, Udine, Italy; (b)ICTP, Trieste, Italy; (c)Dipartimento Politecnico
   di Ingegneria e Architettura, Università di Udine, Udine, Italy
71 (a)INFN Sezione di Lecce, Lecce, Italy; (b)Dipartimento di Matematica e Fisica, Università del Salento, Lecce, Italy
72 (a)INFN Sezione di Milano, Milano, Italy; (b)Dipartimento di Fisica, Università di Milano, Milano, Italy
73 (a)INFN Sezione di Napoli, Napoli, Italy; (b)Dipartimento di Fisica, Università di Napoli, Napoli, Italy
74 (a)INFN Sezione di Pavia, Pavia, Italy; (b)Dipartimento di Fisica, Università di Pavia, Pavia, Italy
75 (a)INFN Sezione di Pisa, Pisa, Italy; (b)Dipartimento di Fisica E. Fermi, Università di Pisa, Pisa, Italy
76 (a)INFN Sezione di Roma, Roma, Italy; (b)Dipartimento di Fisica, Sapienza Università di Roma, Roma, Italy
77 (a)INFN Sezione di Roma Tor Vergata, Roma, Italy; (b)Dipartimento di Fisica, Università di Roma Tor Vergata, Roma,
   Italy
78 (a)INFN Sezione di Roma Tre, Roma, Italy; (b)Dipartimento di Matematica e Fisica, Università Roma Tre, Roma, Italy
79 (a)INFN-TIFPA, Povo, Italy; (b)Università degli Studi di Trento, Trento, Italy
80 Department of Astro and Particle Physics, Universität Innsbruck, Innsbruck, Austria
81 University of Iowa, Iowa City, IA, USA
82 Department of Physics and Astronomy, Iowa State University, Ames, IA, USA
83 Istinye University, Sariyer, Istanbul, Türkiye
84 (a)Departamento de Engenharia Elétrica, Universidade Federal de Juiz de Fora (UFJF), Juiz de Fora,
   Brazil; (b)Universidade Federal do Rio De Janeiro COPPE/EE/IF, Rio de Janeiro, Brazil; (c)Instituto de Física,
  Universidade de São Paulo, São Paulo, Brazil; (d)Rio de Janeiro State University, Rio de Janeiro, Brazil; (e)Federal
  University of Bahia, Bahia, Brazil
85 KEK, High Energy Accelerator Research Organization, Tsukuba, Japan

123

### Página PDF 33

Comput Softw Big Sci        (2025) 9:2                                                          Page 33 of 35    2

 86 Graduate School of Science, Kobe University, Kobe, Japan
 87 (a)Faculty of Physics and Applied Computer Science, AGH University of Krakow, Krakow, Poland; (b)Marian
   Smoluchowski Institute of Physics, Jagiellonian University, Krakow, Poland
 88 Institute of Nuclear Physics Polish Academy of Sciences, Krakow, Poland
 89 Faculty of Science, Kyoto University, Kyoto, Japan
 90 Research Center for Advanced Particle Physics and Department of Physics, Kyushu University, Fukuoka , Japan
 91 L2IT, Université de Toulouse, CNRS/IN2P3, UPS, Toulouse, France
 92 Instituto de Física La Plata, Universidad Nacional de La Plata and CONICET, La Plata, Argentina
 93 Physics Department, Lancaster University, Lancaster, UK
 94 Oliver Lodge Laboratory, University of Liverpool, Liverpool, UK
 95 Department of Experimental Particle Physics, Jožef Stefan Institute and Department of Physics, University of Ljubljana,
   Ljubljana, Slovenia
 96 School of Physics and Astronomy, Queen Mary University of London, London, UK
 97 Department of Physics, Royal Holloway University of London, Egham, UK
 98 Department of Physics and Astronomy, University College London, London, UK
 99 Louisiana Tech University, Ruston, LA, USA
100 Fysiska institutionen, Lunds universitet, Lund, Sweden
101 Departamento de Física Teorica C-15 and CIAFF, Universidad Autónoma de Madrid, Madrid, Spain
102 Institut für Physik, Universität Mainz, Mainz, Germany
103 School of Physics and Astronomy, University of Manchester, Manchester, UK
104 CPPM, Aix-Marseille Université, CNRS/IN2P3, Marseille, France
105 Department of Physics, University of Massachusetts, Amherst, MA, USA
106 Department of Physics, McGill University, Montreal, QC, Canada
107 School of Physics, University of Melbourne, Victoria, Australia
108 Department of Physics, University of Michigan, Ann Arbor, MI, USA
109 Department of Physics and Astronomy, Michigan State University, East Lansing, MI, USA
110 Group of Particle Physics, University of Montreal, Montreal, QC, Canada
111 Fakultät für Physik, Ludwig-Maximilians-Universität München, München, Germany
112 Max-Planck-Institut für Physik (Werner-Heisenberg-Institut), München, Germany
113 Graduate School of Science and Kobayashi-Maskawa Institute, Nagoya University, Nagoya, Japan
114 (a)Department of Physics, Nanjing University, Nanjing, China; (b)School of Science, Shenzhen Campus of Sun Yat-sen
   University, Shenzhen, China; (c)University of Chinese Academy of Science (UCAS), Beijing, China
115 Department of Physics and Astronomy, University of New Mexico, Albuquerque, NM, USA
116 Institute for Mathematics, Astrophysics and Particle Physics, Radboud University/Nikhef, Nijmegen, Netherlands
117 Nikhef National Institute for Subatomic Physics and University of Amsterdam, Amsterdam, Netherlands
118 Department of Physics, Northern Illinois University, DeKalb, IL, USA
119 (a)New York University Abu Dhabi, Abu Dhabi, United Arab Emirates; (b)United Arab Emirates University, Al Ain,
   United Arab Emirates
120 Department of Physics, New York University, New York, NY, USA
121 Ochanomizu University, Otsuka, Bunkyo-ku, Tokyo, Japan
122 Ohio State University, Columbus, OH, USA
123 Homer L. Dodge Department of Physics and Astronomy, University of Oklahoma, Norman, OK, USA
124 Department of Physics, Oklahoma State University, Stillwater, OK, USA
125 Palacký University, Joint Laboratory of Optics, Olomouc, Czech Republic
126 Institute for Fundamental Science, University of Oregon, Eugene, OR, USA
127 Graduate School of Science, Osaka University, Osaka, Japan
128 Department of Physics, University of Oslo, Oslo, Norway
129 Department of Physics, Oxford University, Oxford, UK
130 LPNHE, Sorbonne Université, Université Paris Cité, CNRS/IN2P3, Paris, France
131 Department of Physics, University of Pennsylvania, Philadelphia, PA, USA
132 Department of Physics and Astronomy, University of Pittsburgh, Pittsburgh, PA, USA
133 (a)Laboratório de Instrumentação e Física Experimental de Partículas - LIP, Lisbon, Portugal; (b)Departamento de Física,
   Faculdade de Ciências, Universidade de Lisboa, Lisbon, Portugal; (c)Departamento de Física, Universidade de Coimbra,

                                  123

### Página PDF 34

2  Page 34 of 35                                                    Comput Softw Big Sci        (2025) 9:2


   Coimbra, Portugal; (d)Centro de Física Nuclear da Universidade de Lisboa, Lisbon, Portugal; (e)Departamento de Física,
   Universidade do Minho, Braga, Portugal; (f)Departamento de Física Teórica y del Cosmos, Universidad de Granada,
   Granada, Spain; (g)Departamento de Física, Instituto Superior Técnico, Universidade de Lisboa, Lisbon, Portugal
134 Institute of Physics of the Czech Academy of Sciences, Prague, Czech Republic
135 Czech Technical University in Prague, Prague, Czech Republic
136 Charles University, Faculty of Mathematics and Physics, Prague, Czech Republic
137 Particle Physics Department, Rutherford Appleton Laboratory, Didcot, UK
138 IRFU, CEA, Université Paris-Saclay, Gif-sur-Yvette, France
139 Santa Cruz Institute for Particle Physics, University of California Santa Cruz, Santa Cruz, CA, USA
140 (a)Departamento de Física, Pontiﬁcia Universidad Católica de Chile, Santiago, Chile; (b)Millennium Institute for
   Subatomic physics at high energy frontier (SAPHIR), Santiago, Chile; (c)Instituto de Investigación Multidisciplinario en
   Ciencia y Tecnología, y Departamento de Física, Universidad de La Serena, La Serena, Chile; (d)Universidad Andres
   Bello, Department of Physics, Santiago, Chile; (e)Instituto de Alta Investigación, Universidad de Tarapacá, Arica,
   Chile; (f)Departamento de Física, Universidad Técnica Federico Santa María, Valparaíso, Chile
141 Department of Physics, University of Washington, Seattle, WA, USA
142 Department of Physics and Astronomy, University of Shefﬁeld, Shefﬁeld, UK
143 Department of Physics, Shinshu University, Nagano, Japan
144 Department Physik, Universität Siegen, Siegen, Germany
145 Department of Physics, Simon Fraser University, Burnaby, BC, Canada
146 SLAC National Accelerator Laboratory, Stanford, CA, USA
147 Department of Physics, Royal Institute of Technology, Stockholm, Sweden
148 Departments of Physics and Astronomy, Stony Brook University, Stony Brook, NY, USA
149 Department of Physics and Astronomy, University of Sussex, Brighton, UK
150 School of Physics, University of Sydney, Sydney, Australia
151 Institute of Physics, Academia Sinica, Taipei, Taiwan
152 (a)E. Andronikashvili Institute of Physics, Iv. Javakhishvili Tbilisi State University, Tbilisi, Georgia; (b)High Energy
   Physics Institute, Tbilisi State University, Tbilisi, Georgia; (c)University of Georgia, Tbilisi, Georgia
153 Department of Physics, Technion, Israel Institute of Technology, Haifa, Israel
154 Raymond and Beverly Sackler School of Physics and Astronomy, Tel Aviv University, Tel Aviv, Israel
155 Department of Physics, Aristotle University of Thessaloniki, Thessaloniki, Greece
156 International Center for Elementary Particle Physics and Department of Physics, University of Tokyo, Tokyo, Japan
157 Department of Physics, Tokyo Institute of Technology, Tokyo, Japan
158 Department of Physics, University of Toronto, Toronto, ON, Canada
159 (a)TRIUMF, Vancouver, BC, Canada; (b)Department of Physics and Astronomy, York University, Toronto, ON, Canada
160 Division of Physics and Tomonaga Center for the History of the Universe, Faculty of Pure and Applied Sciences,
   University of Tsukuba, Tsukuba, Japan
161 Department of Physics and Astronomy, Tufts University, Medford, MA, USA
162 Department of Physics and Astronomy, University of California Irvine, Irvine, CA, USA
163 University of Sharjah, Sharjah, United Arab Emirates
164 Department of Physics and Astronomy, University of Uppsala, Uppsala, Sweden
165 Department of Physics, University of Illinois, Urbana, IL, USA
166 Instituto de Física Corpuscular (IFIC), Centro Mixto Universidad de Valencia-CSIC, Valencia, Spain
167 Department of Physics, University of British Columbia, Vancouver, BC, Canada
168 Department of Physics and Astronomy, University of Victoria, Victoria, BC, Canada
169 Fakultät für Physik und Astronomie, Julius-Maximilians-Universität Würzburg, Würzburg, Germany
170 Department of Physics, University of Warwick, Coventry, UK
171 Waseda University, Tokyo, Japan
172 Department of Particle Physics and Astrophysics, Weizmann Institute of Science, Rehovot, Israel
173 Department of Physics, University of Wisconsin, Madison, WI, USA
174 Fakultät für Mathematik und Naturwissenschaften, Fachgruppe Physik, Bergische Universität Wuppertal, Wuppertal,
   Germany
175 Department of Physics, Yale University, New Haven, CT, USA


123

### Página PDF 35

Comput Softw Big Sci        (2025) 9:2                                                          Page 35 of 35    2

  a Also Afﬁliated with an institute covered by a cooperation agreement with CERN, Geneva, Switzerland
  b Also at An-Najah National University, Nablus, Palestine
  c Also at Borough of Manhattan Community College, City University of New York, New York, NY, USA
 d Also at Center for Interdisciplinary Research and Innovation (CIRI-AUTH), Thessaloniki, Greece
  e Associated at Centro de Investigaciones Energéticas, Medioambientales y Tecnológicas, Spain
   f Also at Centro Studi e Ricerche Enrico Fermi, Roma, Italy
  g Also at CERN, Geneva, Switzerland
 h Also at CMD-AC UNEC Research Center, Azerbaijan State University of Economics (UNEC), Baku, Azerbaijan
   i Also at Département de Physique Nucléaire et Corpusculaire, Université de Genève, Genève, Switzerland
   j Also at Departament de Fisica de la Universitat Autonoma de Barcelona, Barcelona, Spain
 k Also at Department of Financial and Management Engineering, University of the Aegean, Chios, Greece
   l Also at Department of Physics, California State University, Sacramento, USA
 m Also at Department of Physics, King’s College London, London, UK
 n Also at Department of Physics, Stanford University, Stanford, CA, USA
  o Also at Department of Physics, Stellenbosch University, Stellenbosch, South Africa
  p Also at Department of Physics, University of Fribourg, Fribourg, Switzerland
 q Also at Department of Physics, University of Thessaly, Volos, Greece
   r Also at Department of Physics, Westmont College, Santa Barbara, USA
  s Also at Hellenic Open University, Patras, Greece
   t Also at Institucio Catalana de Recerca i Estudis Avancats, ICREA, Barcelona, Spain
 u Also at Institut für Experimentalphysik, Universität Hamburg, Hamburg, Germany
 v Also at Institute for Nuclear Research and Nuclear Energy (INRNE) of the Bulgarian Academy of Sciences, Soﬁa,
   Bulgaria
 w Also at Institute of Applied Physics, Mohammed VI Polytechnic University, Ben Guerir, Morocco
 x Also at Institute of Particle Physics (IPP), Toronto, Canada
 y Also at Institute of Physics, Azerbaijan Academy of Sciences, Baku, Azerbaijan
  z Also at Institute of Theoretical Physics, Ilia State University, Tbilisi, Georgia
 aa Also at National Institute of Physics, University of the Philippines Diliman (Philippines), Quezon City, Philippines
 ab Also at Technical University of Munich, Munich, Germany
 ac Also at The Collaborative Innovation Center of Quantum Matter (CICQM), Beijing, China
 ad Also at TRIUMF, Vancouver, BC, Canada
 ae Also at Università di Napoli Parthenope, Napoli, Italy
 af Also at University of Colorado Boulder, Department of Physics, Colorado, USA
 ag Also at Washington College, Chestertown, MD, USA
 ah Also at Yeditepe University, Physics Department, Istanbul, Türkiye
  ∗Deceased


                                  123
