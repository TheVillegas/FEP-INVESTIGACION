# Resource Accounting of Shared IT Resources in Multi-Tenant Clouds

> **Pilar:** P1
> **Clasificación:** Declarada en la matriz
> **Evidencia de clasificación:** Fila académica del CSV titulada “Resource Accounting of Shared IT Resources in Multi-Tenant Clouds”, código P1.
> **Archivo fuente:** papers-pdf/Tak et al. - 2017 - Resource Accounting of Shared IT Resources in Multi-Tenant Clouds.pdf
> **Uso previsto:** Lectura personal y apoyo documental; requiere validación humana antes de incorporarse al informe.

## 1. Título

*Resource Accounting of Shared IT Resources in Multi-Tenant Clouds*.

## 2. Autor y fecha

- **Autores verificados en el PDF:** Byung Chul Tak, Youngjin Kwon y Bhuvan Urgaonkar.
- **Fecha bibliográfica utilizada:** 2017, *IEEE Transactions on Services Computing*, vol. 10, n.º 2, marzo/abril de 2017, pp. 302–315.
- El PDF también informa publicación en línea en 2015; se usa 2017 por corresponder a la edición bibliográfica visible.

## 3. Problema que trata

En servicios multiarrendatario, varias entidades comparten procesos, hilos y componentes distribuidos. Las métricas agregadas de herramientas como `top` o `iostat` no permiten atribuir de manera confiable CPU, red o disco a cada entidad cobrable. La falta de identidad propagada, el caché, el buffering y los efectos entre servicios pueden romper las correlaciones usadas por métodos inferenciales simples.

## 4. Qué quiere hacer

Diseñar una técnica general y no intrusiva que contabilice recursos de servicios compartidos con granularidad de hilo, sin modificar las aplicaciones, y demostrar que esa atribución mejora acciones operativas como control de carga, fairness y cumplimiento de SLA.

## 5. Cómo lo hace

Propone **Rameter**, con dos módulos en el hipervisor Xen: seguimiento de causalidad de solicitudes distribuidas y contabilización de eventos de planificación, creación de hilos y E/S. Compara Rameter con un método de regresión lineal (LR) que infiere consumo desde tráfico agregado. Evalúa un servicio sintético con verdad de referencia y dos servicios reales, MySQL Cluster y HBase; además aplica throttling dirigido a la entidad responsable de saturación (secciones 5–7).

## 6. Resultados

- En el servicio sintético, Rameter mantiene error inferior a **1 %**, mientras LR varía entre **5 % y 150 %** según el resumen; bajo factores de caché y buffering, LR presenta 10–60 % y Rameter sigue bajo 1 % (sección 7.2, figura 5).
- En MySQL, LR atribuye erróneamente la saturación a C3; Rameter identifica a C2 y el throttling mantiene el tiempo de respuesta bajo el límite SLA de 600 ms (sección 7.3.1, figuras 7–9).
- En HBase, LR conserva un orden incorrecto del consumidor dominante tras un cambio de carga; Rameter refleja el cambio observado (sección 7.3.2, figura 12).
- Interceptar y registrar llamadas añade 422 ns; el impacto típico es 1–2 % y el peor caso informado es menor a 3 % (sección 7.4, tabla 3).

## 7. Discusión y trabajo futuro

Los autores señalan limitaciones: la implementación no cubre memoria, depende de instrumentación privilegiada en Xen y puede dejar consumo “no atribuible” que debe repartirse mediante una política externa. Presentan como extensiones la aplicación a contenedores, políticas de fairness, más fuentes de monitoreo y mejores mecanismos de control. Distinguen contabilización precisa de facturación al cliente: el estudio apoya gestión del proveedor, no prescribe una política de cobro.

## 8. Conclusión del paper

Los autores concluyen que la observación fina dentro del hipervisor puede superar a la inferencia sobre métricas agregadas, tanto en precisión como en decisiones operativas. Rameter combina monitoreo por hilo e inferencia ligera con sobrecarga limitada, y los experimentos muestran que una atribución correcta puede evitar decisiones de control equivocadas.

## Relación preliminar con INV-01

Ofrece base técnica para 3.1–3.4 de INV-01: visibilidad, costos compartidos y tasas de asignación. Explica por qué la asignación requiere medición causal y granular, especialmente en servicios compartidos. No proporciona una política FinOps de showback/chargeback ni precios actuales.

## Limitaciones de esta síntesis

La plataforma experimental usa Xen 3.1.4 y tecnologías anteriores al ecosistema cloud-native actual. Los resultados de precisión no deben extrapolarse automáticamente a Kubernetes o servicios administrados. Esta síntesis conserva la distinción entre medición observada, utilidad propuesta y extensiones futuras, y requiere validación humana.

## Texto extraído del PDF

> **Advertencia de conversión:** extracción textual automática de 14 páginas (111536 caracteres). Se conservaron títulos, párrafos, referencias y contenido textual por página. La disposición multicolumna, las figuras, las tablas y las ecuaciones pueden no mantener su alineación o representación visual; verifique esos elementos en el PDF original.

### Página PDF 1

302                                                   IEEE TRANSACTIONS ON SERVICES COMPUTING,  VOL. 10,  NO. 2,  MARCH/APRIL 2017

  Resource Accounting of Shared IT Resources
                 in Multi-Tenant Clouds

             Byung Chul Tak, Youngjin Kwon, and Bhuvan Urgaonkar, Senior Member, IEEE


         Abstract—In today’s IT platforms, the capability to accurately account overall resource usage among applications is crucial for
           variety of management actions (e.g., capacity planning, dynamic resource reallocation and/or load balancing). However, in the
         environments where small number of shared services cater to a large number of distinct entities’ requests, resource accounting
        becomes signiﬁcantly challenging. First, the overall resource consumption at the shared service is the aggregate of the resource
         consumption for multiple remote entities whose identities are not visible to the shared service. Second, even if such information
        becomes available, common monitoring tools (e.g., top, iostat) are unable to deliver accurate break-down of resource consumption
          since sharing occurs at sub-instance level (i.e., service instances are not exclusive). We study inherent challenges of performing
         resource accounting of shared resource. We compare two nonintrusive approaches having different balance between local monitoring
        and collective inference - (i) LR that uses easily-available tools which provide aggregate measurement and applying well-known linear
          regression as inference, and (ii) Rameter that puts more emphasis on gathering ﬁne-grained per-thread information from within the
          hypervisor and applying light inference on the data. Evaluation shows that Rameter offers less than 1% error in accounting whereas
         LR’s error ﬂuctuates between 5-150%.


         Index Terms—Cloud computing, distributed system, and resource management
                               Ç

  1  INTRODUCTION

       CHIEVING operational excellence on modern IT (Infor-  management scenarios. For one thing, it can be crucial for
       mation Technology) platforms continues to become  performance management. Suboptimal or untimely reaction A
   ever more challenging. The complexity of IT platforms   to the current resource sharing state may adversely impact
   keeps growing with emergent paradigms such as SDN   business operations. For instance, a load imbalance towards
   (Software Deﬁned Network). Furthermore,  recent “Big  one of the replicas in a shared database VM may impact neg-
   Data” trends are necessitating increase of platform scales to   atively the end-to-end delay of all the services that rely on it.
   unprecedented degrees. Today’s management capabilities  Many industry data support that revenue is highly sensitive
   struggle to keep up with the increase of such complexity   to even sub-second increase of delays [5]. Such understand-
  and scale [1], [2]. A large portion of this complexity stems   ing also helps administrators get answers to questions that
  from the sharing and consolidation of computing resources.   are difﬁcult to address otherwise. E.g., which app’s request
   Increasingly, IT platforms consolidate multiple S/W appli-    is triggering sudden burst of CPU saturations in one of the
   cations on a shared set of hardware equipment for reasons   key-value storage servers deep down in the service pipeline?
   of cost-efﬁcacy or organizational necessity. Such consolida-  To which replica should I redirect such workloads so that
   tion and sharing occur in a wide variety of platforms such   overall resource utilization stays within a safe range? Is it
   as public clouds, private clouds, and even medium/small-   also possible to apply resource capping so that fairness is
                                                          maintained for the end users, and on what basis can we   scale data centers or clusters in enterprises or labs running
                                                           charge the user for the resource usage of the target server?   multiple applications. Popular cloud-based shared services
                                                                   Proactively taking actions for resource usage adjustment   such as key-value stores (e.g., Amazon SimpleDB [3]) and
                                                              or resource usage policy enforcement require accurate meas-   relational database services (e.g., SQL Azure [4]) exemplify
                                                        urements of them. However, ascertainment of accurate   this trend. Considering a broader context, sharing also
                                                              resource usage information (the activity we refer to as   occurs for S/W, non-IT infrastructure resources such as
                                                                      resource accounting in this paper) is challenging within sys-   cooling and power, and even personnel.
                                                       tems consisting of multiple servers running heterogeneous     Clear understanding of how sharing happens for various
                                                                 distributed applications. First, in many cases there are no   resources can provide signiﬁcant advantages in numerous
                                                                     clear indicators that tell us to which remote component or
                                                                     entity the resource usage should be attributed at a given
       B. C. Tak is with the IBM T. J. Watson Research Center.                 time. For instance, at the database node of a multi-tier e-com-
       Y. Kwon is with the Computer Science Department, University of Texas at
       Austin, Austin, TX.                                     merce application that is shared by several unrelated group
       B. Urgaonkar is with the Department of CSE, The Pennsylvania State   of end-users, there is no explicit information about whose
       University, PA.                                                          initial requests triggered for given currently issued database
   Manuscript received 30 Jan. 2015; revised 8 June 2015; accepted 1 July 2015.   queries are unless the S/W stacks at each tier is modiﬁed to
   Date of publication 8 July 2015; date of current version 7 Apr. 2017.          carry request identiﬁers. Such condition poses difﬁculties in
   For information on obtaining reprints of this article, please send e-mail to:
    reprints@ieee.org, and reference the Digital Object Identiﬁer below.         managing the resource utilization of the database server by
    Digital Object Identiﬁer no. 10.1109/TSC.2015.2453980               means of admission control at the user-facing component.


                                        1939-1374  2015 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
                                        See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore. Restrictions apply.

### Página PDF 2

TAK ET AL.: RESOURCE ACCOUNTING OF SHARED IT RESOURCES IN MULTI-TENANT CLOUDS                                                 303


   Another  difﬁculty  is  that, even with such knowledge,
   resource attribution is non-trivial due to the followings. Sim-
   ple utilization information of processes or threads (such as
  top, iostat) may be insufﬁcient because those numbers
   are the aggregate resource utilization caused by multiple
   remote entities. This is due to the granularity of resource
   principals being as ﬁne as threads and even the bindings
   between the remote resource consuming entities and such
   resource principals could change dynamically over time.
   This implies that we need to further break down the moni-
   tored values using inference techniques. Other example is
   the write activity of disk I/O in which OS kernel combines
   multiple writes and issues them much later in time non-
   deterministically. These challenges are intensiﬁed especially
   in today’s complex service architectures in which many serv-
   ices are built on top of other heterogeneous services via inter-    Fig. 1. Problem model. CE (Chargeable Entity) is deﬁned to be any entity
                                                                              or group of entities that sends requests directly or indirectly.
   face such as REST APIs (Representational State Transfer).
     Based on our study, we believe that current state-of-the-art
   needs to be improved to deliver aforementioned resource   data collection and inferencing during the overall resource
   accounting capabilities for improving cloud operations and   accounting. One central concern in our design is to achieve
  management. Toward this end, we have designed and imple-   generality by avoiding application modiﬁcation. Speciﬁ-
  mented the resource accounting technique, called Rameter.   cally, we make the following key contributions. First, we
   Rameter consists of two modules—(i) distributed request   formulate the problem of resource accounting for shared
   (message) causality tracking module running within the   servers running distributed applications, and introduce the
   hypervisor, and (ii) resource usage accounting module that   design of Rameter, capable of providing accurate resource
   gathers thread scheduling, spawning and I/O activities. Our  usage information of shared services. To the best of our
   distributed request tracking technique allows us to ﬁrst deter-  knowledge, our design goes beyond the state-of-the-art by
  mine the ownership of request messages at any VM or server   being the accounting solution that is both: (i) implemented
   nodes without the need to modify the application codes.   within privileged code (VMM in our case) with no need for
  Once the ownership is determined, the resource accounting   application modiﬁcation, and (ii) capable of accounting the
  module observes ﬁne-grained thread level events from the  usage of shared services. Second, using a mix of synthetic
   hypervisor to further break down the CPU and I/O usages.    and real-world shared services, we present the comparison
    Compared to our Rameter, some of the existing techni-   of two approaches—LR that uses easily-available system
   ques rely on modifying (all or part of) the OS or middleware   utilities which provide aggregate measurement data and
   stacks to enrich the collected data [6], [7]. Often, they spe-   applying well-known linear regression as inference, and
   cialize on one speciﬁc component and implement the    (ii) Rameter that puts more emphasis on gathering ﬁne-
   accounting and/or  controlling  functions by modifying   grained information from within the hypervisor and apply-
   source code [8], [9]. However, such instrumentation-based   ing light inference on the data. Third, we demonstrate the
   approaches are viable only to the organization who builds   usefulness of Rameter’s resource accounting information by
   their own S/W stacks or to the relatively small environment   applying it to online resource control (speciﬁcally via throt-
   such as embedded systems. And, even with some instru-   tling) using the scenario of enforcing the SLA requirements
   mentation, gathered monitoring data may not  contain   for RUBiS application under heavy workloads. Such capabil-
  enough information for the purpose of accurate resource   ity of online resource control for shared services is achievable
   accounting. In response to such limitations, we pursue the   only when ﬁne-grained thread-level information is available,
   goal of building effective resource accounting technique  which aggregate monitoring data cannot provide.
   that  is  (i) focusing on obtaining ﬁne-grained per-thread     The rest of this paper is organized as follows. Section 2
   resource usage information,  (ii) generally applicable to   provides some background knowledge and explains what
   existing environments,  (iii) accurate enough for any type  makes the resource accounting problem challenging. In
   of resources, including both IT and non-IT resources, and   Section 3, we deﬁne our problem. In Section 4, we identify
    (iv)  ﬂexible enough  to accommodate a wide-range  of  key design requirements. Descriptions of our solution are
   resource management policies. As an initial step, we focus   given in Section 5, and it is followed by implementation
  on IT resource such as CPU, I/O and network in a virtual-   details in Section 6. In Section 7, we present our experimen-
   ized environment. Note that our study is not about propos-   tal evaluation. Then, we provide related work in Section 8.
   ing the adoption of more detailed billing information to the   Finally, in Section 9, we present concluding remarks.
   cloud users. We address the resource management problem
  from the perspective of cloud service providers with the
                                            2  BACKGROUND AND CHALLENGES
   goal of improving the cloud management operations.
    We study the resource accounting problem and investi-   2.1  Problem Model, Terminology and Scope
   gate solutions that addresses all challenges identiﬁed above.  We use Fig. 1 that shows a representative platform that we
  Towards ﬁnding the right solution we build and compare   use to drive our discussion. It illustrates various key entities
  two approaches that differ in where they focus more among  and the relationships between them. We refer to a platform
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore. Restrictions apply.

### Página PDF 3

304                                                   IEEE TRANSACTIONS ON SERVICES COMPUTING,  VOL. 10,  NO. 2,  MARCH/APRIL 2017


   user or their application whose resource usage must be      In resource management, fairness can be deﬁned in sev-
   separately tracked and accounted as a chargeable entity   eral ways. They could be either strictly in terms of the
   (CE). The concept of CE is not limited to subscribers of  amount of resource usage, or in relation to how much user
   software services. We deﬁne it in a broader sense to rec-    is willing to pay for the service quality. In any case, accurate
   ognize groups of computing equipment as CEs as well.   resource accounting is the basis for the enforcement of the
   Fig. 1 shows several types of such CEs—Group 1, 2, User   fairness. The scope in this work is to build supporting mech-
   1, 2, and 3. However, if necessary, any other entities such  anism to enable the enforcement of various fairness policies.
   as “Business Logic VM” or individual VMs in Group 2  Extending Rameter to enforce the fairness in terms of the
   can be treated as separate CEs. We assume the virtualized   service quality and payment is our future plan.
   environment in which CEs’ software components run
   within virtual machines (VM).                                                            2.2  Real-World Examples of Shared Services
     Also shown in the ﬁgure are example shared services
                                                                                         It is not hard to ﬁnd the shared services in both the public
   that the platform offers to its CEs—a database service and a
                                                            clouds (especially in PaaS) and/or non-cloud environments
   conﬁguration management service. These shared services
                                                                   that conform well to our model. Valid example should
   themselves have multiple components that span across sev-
                                                                   exhibit the behavior in which the resource sharing occurs at
   eral VMs or physical servers. Internally the database service
                                                               the instance-level (i.e., process). If separate instance of VMs
   maintains functionally separate group of VMs for load bal-
                                                              or  processes  serves  different CEs, then managing  the
   ancing. Whereas its front-end tier communicates directly
                                                              resource usage becomes  signiﬁcantly  easier. However,
   with the chargeable entities, its back-end components are
                                                                   instance-level sharing is becoming more common because it   exercised indirectly, i.e., via requests made to the front-end
                                                            provides better scalability and resource efﬁciency. Real-    tier. The arrow from the conﬁguration management service
                                                      world examples of shared services that conform to our   to the database service represents the fact that services may
                                                    model are listed below.   build on top of other services. Note that each CE does not
                                                SQL Azure. The ﬁrst example of a shared service is the   exclusively own its database process. One database instance
                                                              Microsoft SQL Azure [4], the multi-tenant SaaS database   (in our example, two front-ends and three query processing
                                                                      service. In SQL Azure, tenants see only their own database  VMs for one instance) may be shared by an unrelated group
                                                                 spaces,  but  they  physically  share  the  underlying   of tenants.1 Shared services in our model are frequently
                                                            database server instance with other tenants [4]. Windows  found in Platform-as-a-Service (Paas) type cloud where cus-
                                                     Azure also offers three different types of shared storage   tomers pay for the usage of services rather than owning
                                                            services—Blob, Table, and Queue—intended for different   exclusive service instances.
                                                            purpose. Tenants are given separate database spaces, but     Unlike for ‘Web Server VM’ or ‘Business Logic VM’
                                                               the database instances are shared [4].  where an accounting-capable VMM (e.g., using an exist-
                                                                      Force.com.  It is a (Platform-as-a-Service version of the   ing accounting solution such as resource containers [10])
                                                                        Salesforce.com, which is a SaaS cloud service specializing in   could associate the VMs with appropriate CEs, existing
                                                           providing an online CRM (Customer Relationship Manage-   solutions  cannot  be  directly  adapted  for  accounting
                                                        ment) solution. By design, Force.com adopts an architecture   within servers that belong to shared services where the
                                                                   in which all the users share a single software instance and  VMM-visible resource principals do not have a ﬁxed asso-
                                                               the set of H/W. [16]. This architecture is chosen to increase   ciation with any CE. Additionally, since the back-end tier
                                                               the manageability.   of the database service is only exercised by the CEs indi-
                                                              SimpleDB. An example of the shared service can also be    rectly,  i.e.,  via work  generated during  processing  of
                                                      found in AWS (Amazon Web Services) cloud. Amazon   requests that are made by CEs to the front-end, additional
                                                                      offers non-relational key-value data store service, called   thought is needed to identify what portion of its resource
                                                    SimpleDB [3]. Subscribers are charged by the machine utili-   usage should be attributed to which CE. Consequently, a
                                                                    zation, data transfer size incurred by user requests and the   resource may be used by a CE either directly (e.g., resour-
                                                                          total storage space used. Especially, SimpleDB measures the   ces on server VMs exclusively assigned for the software
  owned by them) or indirectly via a shared service (e.g.,  CPU utilization at the individual request level. CPU utiliza-
   resources on servers hosting the database-as-a-service,   tion consumption is estimated based on the amount of data
   within  the  SaaS  (Software-as-a-Service)  database,  the   size. Although system architecture is not publically avail-
   shared network, or the SAN).                                   able, it can be inferred that SimpleDB adopts some form of
     Recently a number of data center resource management   resource accounting mechanism.
   solutions (e.g., DCOS [11], [12], [13], fos [14], and Open-      Bigtable. Bigtable [17] is Google’s proprietary database
   Stack [15]) have emerged all of which require solutions for   built with massive scalability in mind. Bigtable service
   keeping track of and accounting the overall usage of shared   builds on top of two other services—Chubby [18] and GFS
   resources, typically at the granularity of a container or VM.   (Google File System) [19]. Chubby is a distributed lock ser-
  We view our work as highly complementary to these solu-   vice manager that provides coarse-grained synchronization
   tions in that our technique can be used in these solutions for  on shared resources. Bigtable uses Chubby for maintaining
   even ﬁner task granularity accounting.                      a master Bigtable server and for storing the metadata for
                                                            data locations. GFS is used by the Bigtable to store logs and
                                                            data ﬁles. Bigtable internally serves the needs of multiple
        1. The term, tenant, is the equivalent of the CE in database terminol-
   ogy. However, it typically refers to the direct subscribers of the data-  groups in Google. Each group is given isolated table space,
   base service itself, not of the entire platform as how CE is deﬁned.       but they share the Bigtable instance similar to SQL Azure.
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore. Restrictions apply.

### Página PDF 4

TAK ET AL.: RESOURCE ACCOUNTING OF SHARED IT RESOURCES IN MULTI-TENANT CLOUDS                                                 305

   2.3  Challenges                                                     TABLE 1
   2.3.1  Lack of Direct Indicators                                     Summary of Symbols
  A key difﬁculty arises due to lack of direct indicators of CEs  Symbol                       Description
   responsible for the currently in-progress resource activities
                                                                        c              Chargeable entity, CE
   at the servers, especially in shared services. Unlike applica-                                                           C               Total set of CE
   tion-owned software, a shared service may only be exercised   s               Server
   by a CE indirectly, making it more difﬁcult to ascertain this  S            Group of servers comprising a shared service
   relationship. In Fig. 1, the query processing VMs of the data-   r              Resource type (e.g. CPU, Disk I/O and/or
   base service (Shared Service 1) is merely invoked indirectly                Network I/O)
                                                    n           Number of resource types we consider  by the CEs through the front-ends, oblivious of who it is
                                                                                Ur;sðtÞ          Resource utilization time-series of type r at s  working for. Likewise for the front-ends, they are only able
                                                                                 Ur;sc  ðtÞ          Resource utilization time-series of type r at s
   to identify whether the request is from Group 1,2, Business                                                                                          attributable to c
   Logic VMs or the Conﬁg. collector. But, it is hard to identify    Vr;sðtÞ          Unaccountable resource utilization time-series
   further whether the requests coming from the Business                    of type r at s
   Logic VMs are from User 1, 2 or 3. One approach for infer-   Wr;sðtÞ         Resource idle time-series of type r at s
   ring such relationship may be to instrument the messaging
  S/W to inject identiﬁers, which is not generally applicable
  and may be prohibitive.                                 produce n time-series, one per resource type r at a measure-
    How accurately the local monitoring on server can iden-  ment granularity D. We denote as Ur;sðtÞ the utilization mea-
    tify such indirect usage depends on its accuracy in recogniz-  surement for resource r at server s during the tth time slot.
   ing the underlying causation (i.e., some activities of a CE    Its range is 0   Ur;sðtÞ   1 to indicate proportions. Table 1
   caused certain activities of a component which consumed  summarizes the symbols and their meanings.
  some resources). When a CE is only “one hop away” from     The goal of resource accounting is to infer, for each CE c at
   the component,  the presence  of  direct communication    s, the contribution of c to the utilization, Ur;sc  ðtÞ. In addition,
   between them can yield this causation information. How-  we are interested in ﬁnding out the proportion that is not
   ever, identifying causation becomes trickier when the com-   attributable to any c, denoted as Vr;sðtÞ. That is, we want to
   ponent is “more than one hop away” from the CE. Solving  ﬁnd Ur;sc  ðtÞ and Vr;sðtÞ such that
   this problem, in general, requires some form of statistical                         X
   inference based on probabilistic models to capture this cau-                          Ur;sc  ðtÞ þ Vr;sðtÞ ¼ Ur;sðtÞ:               (1)
   sation, and closely related examples can be seen in some                       c2C
  work [6], [20].
                                                  As a corollary,  if we let Wr;sðtÞ be the proportion of
                                                     unused (i.e., idle) resource at time t at server s, it would fol-   2.3.2  Mismatch of Resource Principals and CEs          P
                                                    low   that                                                                                                  Ur;sc  ðtÞ þ Vr;sðtÞ þ Wr;sðtÞ ¼ 1.   Similarly,                            P                               P      c2C    If  application-owned S/W  components  are  contained                                                                                             Ur;sc  ðtÞ would represent the usage of resource                                                                                                                                      ti  t  tj   s2S
   within resource principals that are likely to be easily identi-
                                                            type r by c in the entire shared service group S during the
   ﬁable by underlying resource management software (e.g.,
                                                           time period of ti    t    tj.
   the virtual machine monitors (VMMs)), this implies an
   existing local accounting solution such as resource contain-
                                            4  DESIGN PRINCIPLES   ers can be easily used by this management software to asso-
   ciate these resource principals with the corresponding CE.2  Any accounting solution that forms the basis for the deci-
  On the other hand, the shared service’s software design and   sion of resource controlling actions must have two ele-
   conﬁguration may not be amenable to easy adaption of such   ments: (i) local monitoring and (ii) collective inference. We
   existing solutions for local accounting. For example, the data  use the phrase “local monitoring” to refer to  facilities
   store component  in  Fig.  1  multiplexes  the  resources   within each server that record events and statistics per-
   assigned to its internal schedulable entities (e.g., threads) in   taining to the resource usage of (or on behalf of) each CE.
   highly application-speciﬁc (and possibly unknown) ways   E.g., in resource containers, local monitoring is carried
  among the activities it carries out on behalf of CEs, render-   out by the server operating system that is modiﬁed to
   ing a solution such as resource containers difﬁcult to adapt.    identify resource allocation/scheduling events (e.g., when
                                                            threads are scheduled/descheduled on the CPU) and
  3  PROBLEM DEFINITION                              using this information to charge their usage to appropri-
                                                                  ate  containers  [10]. The phrase  “collective  inference”
   Let us denote the chargeable entity by c 2 C where C is the                                                                    refers to the functionality needed to combine the pieces of
   set of all CEs, and a server by s. Server s is one of the servers                                                            information offered by local monitoring to create a correct
   in a shared service group S for which we are interested                                                                 overall picture of accounting. Since resource containers
   in performing the resource accounting. For server s we                                                               are  only  concerned  with  a  single  server,  collective
                                                               inference  is trivially realized from the monitored data.
        2. In fact, this is the essential idea behind distributed resource con-   Distributed resource  containers must address a more
    tainers  [21]:  individual  servers use resource  containers  for  local   complicated version of collective inference, and  it does
   accounting and the network stacks within server operating systems are
   modiﬁed to embed tokens within messages sent to/by components   this by augmenting the locally monitored data within
    that uniquely identify their CEs.                               each server with the identity of the distributed container
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore. Restrictions apply.

### Página PDF 5

306                                                   IEEE TRANSACTIONS ON SERVICES COMPUTING,  VOL. 10,  NO. 2,  MARCH/APRIL 2017


   (carried within messages exchanged between container
   components) that they correspond to [21].
    As argued in Section 3, both local monitoring and collec-
   tive inference need to be reconsidered for servers running
   shared services. There exist a large number of techniques
  and tools for local monitoring that one could choose from.
   These existing techniques span a wide spectrum of the
   “level of detail” they offer at the cost of generality, applica-
   tion intrusiveness, and overheads posed. At one end of this
   spectrum are techniques that can instrument user-space
  and OS/VMM code to create a very detailed record of a    Fig. 2. Illustration of solution concept using an end-to-end ﬂow of one of
                                                                      incoming requests.   shared  service’s resource usage that contains sufﬁcient
   information for collective inference [22]. At the other end of
                                                                Section 2.3, that real challenges in answering this question
   the spectrum are CE-oblivious resource usage reporting
                                                                      arise when CE c uses resources on server s indirectly, i.e.,
   tools that rely on information available within the server’s
                                               when a shared service running on s consumes resources on  OS and VMM. E.g., top, and iostat.
                                                                behalf of c.
    As we will empirically show in Section 7, collective infer-
   ence that relies on data offered by these tools can have sig-
   niﬁcant inaccuracies in accounting. Furthermore, as we will   5.1.1   Identifying the Causation and Interval
   ﬁnd, such inference can be extremely sensitive to a variety  To recognize a CE c that is more than one hop away, we
   of system properties and environmental conditions, an  have devised a technique that could track the causal rela-
   undesirable feature. Although our analysis of inference   tionship between incoming and outgoing messages in a
   using existing tools will be based on a speciﬁc inference  component. Let us use Fig. 2 to explain its key idea. The
   technique, we argue that the root cause of these inaccuracies  ﬁgure illustrates an example end-to-end ﬂow of a user
    is the inadequacy of information contained in the monitor-   request across distributed components. Although it shows
   ing information offered by these  tools, and even more   the message ﬂow of a single request across components, it
   sophisticated inference techniques relying on such informa-  should be noted that multiple requests are being processed
   tion would falter.                                            concurrently. Starting from the ﬁrst recv system call by the
     Generally speaking, collective inference is a statistical   Threadx, the initial request originated from a CE produces a
   learning problem that must derive models that can mean-  ﬂow of causally related system call events until a reply is
   ingfully tie together the data provided by local monitors,   sent back to the CE. Between these recv and send, we can
   possibly ﬁlling in any gaps or discrepancies within these   track the sequence of system call events across components
   data. The efﬁcacy of such inference crucially depends upon   using the following rules. First, within the component, the
   the resource usage phenomena collected by local monitor-   causality is carried by the thread. Second, when the thread
   ing elements. Existing monitoring tools that are not applica-   sends a message to other components, the causality moves
   tion-intrusive have been designed for information collection   to a thread in the receiving component. In order to apply
   at the granularity of OS/VMM-relevant abstractions (e.g.,   these rules, we collect the system call events related to the
   threads, TCP connections) that may not coincide with the  network activities. Additionally, it records the thread IDs
   needs of our accounting. Consequently we identify the fol-  and socket tuple information (i.e., IP and port number of
   lowing design principle that underlies our accounting solu-   sender and receiver components) for each events. Thread
   tion: our local monitoring must explicitly capture information  ID enables us to connect the activities that belong to the
   pertaining to resource usage on behalf of CEs to allow accurate  same threads, and the socket tuple allows us to connect
   accounting by our collective inference.                     send and recv pairs across components.
                                                        However, resource accounting requires detecting more
  5  RAMETER: RESOURCE ACCOUNTING                events than only those related to network activities. First,
    FRAMEWORK                                           creation of new threads must be tracked. Processing one
                                                              request may involve spawning of multiple threads or pro-
  Guided by the design principles stated in Section 4 regard-   cesses and each may consume system resources in a differ-
   ing the consequence of choosing the local monitoring tech-   ent way. Component2 of Fig. 2 illustrates such example.
   nique and the collective inference algorithms, we develop a  Suppose that Thread1 spawns two threads via fork (or
   resource accounting technique, called Rameter, that pos-   clone) system  calls upon receiving a request message.
   sesses following characteristics. First, our solution does not   Thread2 incurs multiple disk I/Os, whereas Thread3 inter-
   require modiﬁcations to applications and/or middleware.   acts with another component. In this example, the correct
   Second, the granularity of data collected from the local mon-  CPU consumption for processing of the request message
   itoring is at the thread-level. In this section we describe the   given to the Component2 is the sum of CPU cycles con-
   general ideas underlying Rameter.                     sumed by all three threads. Second, the return value of sys-
                                                    tem calls are needed. Return values of system calls indicate
   5.1  Local Monitoring                                    the amount of data handled by the system call. In order to
  The key aspect of local monitoring that we need to perform   determine the size of I/Os performed, we need to extract
    is identifying and recording information about resource   those return values. Another requirement for the capability
   principals and scheduling events of interest. Recall from   of resource control is the online causality tracking within
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore. Restrictions apply.

### Página PDF 6

TAK ET AL.: RESOURCE ACCOUNTING OF SHARED IT RESOURCES IN MULTI-TENANT CLOUDS                                                 307


   the hypervisor. We provide implementation details speciﬁc  We observe the occurrences and return values of system
   to our environment in Section 6 and discuss other techni-   calls such as recv, send, recvfrom, and sendto,3 and
   ques for different environments.                           accumulate their return values to come up with network
                                                      bandwidth usage. Note that this quantity does not include
   5.1.2  Thread Scheduling Events                          the bandwidth consumption due to protocol-speciﬁc over-
   This aspect of local monitoring is concerned with detecting  heads such as retransmissions and various header/trailer
   the exact moment of thread context switch and collecting   portions added across the protocol stacks.
   information about when the thread begins to use a resource     Disk I/O accounting is done similarly as the network
  on behalf of which CE as well as when it stops doing so.  I/O  (i.e., by tracking the return values of read and
                                                write system calls). However, the resource usage we col-  The local monitoring must record such information solely
   based on what the hypervisor can observe about the   lect is different from the actual disk bandwidth consump-
   resource principals on that server, and the events corre-   tion observed by  the  storage  device. This  is due  to
   sponding to their scheduling.                            nondeterminism introduced by the page cache and block
     For a server s indirectly used by a CE c (i.e., running a  I/O optimization mechanisms by the  kernel.  If exact
   shared service component s exercised by c), we need to   accounting of physical disk bandwidth is required, appro-
   identify CPU (de-)scheduling events within the software of s   priate inference technique must be employed on top of
   that correspond to durations for which s was using the CPU   the accounting information we provide.
  on behalf of c. Identiﬁcation of any I/O activities initiated
   during these same periods allows for accounting I/O band-   5.3  Limitations
   width usage by s on behalf of c. For example, Thread1 of  We describe some of known limitations of current Rameter.
  Component2 in Fig. 2 may experience three different types   First, Rameter  is currently not able to account memory
   of scheduling events between recv and send - VM, process  usage due to overhead in tracking individual memory
  and thread (de-)scheduling events. Speciﬁc implementation   accesses. Detecting the memory access by inducing page
   details we have employed to achieve these are provided in   faults is one option, but high performance impact renders it
   Section 6.                                                      impractical. Second, there are some gaps between reported
                                                           Rameter’s I/O accounting results and the actual ‘physical’
   5.2  Collective Inference                                 resource usage as pointed out in previous subsection. This
  Given the extensive information that our local monitoring    is because some of the I/Os detected by Rameter may not
   gathers, collective inference for accounting CPU, network   translate to actual physical I/Os due to caching. Locks held
  and disk I/O bandwidth essentially boils down to aggrega-  by shared resources may also cause Rameter to produce
   tion of the resource usage information collected by various   misleading results. Resources consumed by a thread while
   local monitoring units. Depending on the type and owner-   busy-waiting on locks are counted as resource consumption
   ship of resources, different methods should be employed.    by Rameter when there is no actual progress of work being
      Deﬁnition. We use the term, segment, as referring to the  made. Third, Rameter does not try to account for the effects
   duration of time starting from the arrival of a request mes-   of interleaved workloads from multiple CEs. For example,
   sage by recv until sending of another message by send  CE c1 may end up issuing more disk I/O requests because
   within a component. Interacting components of those recv   the workload from concurrently running c2 ﬂushes c1’s data
  and send are not necessarily the same.                    from the internal cache. However, Rameter still focuses on
                                                                       faithfully reporting what has happened, rather than who
   5.2.1  CPU                                           caused it. Such analysis requires additional inferences and
                                                                                               it is left as a future work.   Basic idea of CPU accounting is to measure the time differ-
   ence between recv and send events of each request message
    (i.e., segment), and to add the difference to the corresponding  6  IMPLEMENTATION
   CE’s variable that holds the accumulated CPU usage. In addi-                                                                In this section, we describe implementation details speciﬁc
   tion, we subtract the time when the thread was descheduled                                                                    to our environment. Our  virtualization environment  is
   using the information about scheduling events collected as a                                                         based on Xen  3.1.4, 32-bit para-virtualization. Required
   part of local monitoring. The time is measured by RDTSC                                                          modiﬁcations are mostly for enabling the local monitoring
   instruction, which contains the number of cycle counts since                                                             techniques as described in Section 5.1. Collective inference
   boot. Sometimes we can encounter a segment of thread exe-                                                                                 is independent of environment speciﬁcs since it is a process-
   cution that does not start with recv. These CPU consump-                                                             ing of data gathered from the local monitoring step. In order
   tions can be due to background (periodic) activities of OS or                                                                    to realize the local monitoring of Section 5.1, we need to
   daemons. These segments that cannot be labeled with appro-                                                      implement three capabilities—system call interception, cap-
   priate CE is treated as ‘unaccountable’ (See Figs. 7b and 13a                                                                turing of system call return values, and detection of sched-
   for example). The ‘unaccountable’ quantities tell us the possi-                                                               uling events. Techniques described below are dependent on
   ble range of errors in CPU accounting. It is our future goal to                                                         our platform’s speciﬁcations, and different set of techniques
   extend accountings to them and reduce errors.                                             may need to be implemented to achieve similar capabilities
                                                                   in other environment.
   5.2.2  Network and Disk I/O
   All the network related activities within the segment  is        3. The read and write syscalls are used for both network and
   accounted to the CE currently associated with the thread.   disk I/Os.
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore. Restrictions apply.

### Página PDF 7

308                                                   IEEE TRANSACTIONS ON SERVICES COMPUTING,  VOL. 10,  NO. 2,  MARCH/APRIL 2017

   6.1  System Call Interception
   For intercepting the entry point of the system calls invoked
  by user applications in guest VMs, we modify the Xen
   hypervisor in the following way. In our para-virtualized
  Xen environment, system calls use INT 80 h mechanism. To
   intercept the system calls, we ﬁrst add an system call han-
   dler entry in the exception table. Then, we register a system
   gate for interrupt 80 h to the IDT(interrupt descriptor table).
  Whenever a guest VM ﬁres a system call, the software inter-    Fig. 3. Hypervisor-based CPU resource control mechanism by manipula-
   rupt 80 h is triggered. CPU, then, looks up the IDT and    tion of VM-bound timer interrupts.
  jumps to the system gate we installed. Within it, the address
                                                                      32-bit Xen para-virtualization environment, whenever stack
   of the custom handler is searched from the exception table                                                             switching happens,  it traps to the Xen hypervisor (do_
   and, ﬁnally, the control comes to the custom handler.                                                stack_switch function in mm.c). We have added here
    More common system call mechanism is SYSENTER/
                                                               the codes for recording thread scheduling events using
   SYSEXIT. INT 80 h is mainly used in the para-virtualization
                                                         Xen-provided TRACE macro.
   since SYSENTER/SYSEXIT is hardwired in the processor to
  assume that the kernel resides in ring 0, whereas in para-vir-
   tualization, the guest VM’s kernel is in ring 1. In full-virtual-   6.4 CPU Resource Control from Hypervisor
   ization, SYSENTER mechanism is being used because the   In order to demonstrate the effectiveness of Rameter in
   guest kernel runs in ring 0. Although we didn’t need to han-   the  evaluation, we employ  a  hypervisor-based CPU
   dle this, system call based on SYSENTER can still be inter-   resource control mechanism to a reactive resource control
   cepted using techniques described in Ether [23].              scenario (see Section 7.3.1).  It takes Rameter’s resource
                                                           accounting results as  its input and performs targeted
                                                                    throttling of the CPU consumption caused by the CE that   6.2  Capturing System Call Return Values
                                                                                is overusing  the CPU  at  the shared  server.  This  is
  At the entry point of the system calls, we have access to
                                                          achieved by manipulating VM-bound timer  interrupts
   information such as ﬁle descriptor number, buffer address,
                                                     from within the hypervisor. It is non-intrusive and trans-
   buffer  size and  buffer  contents. However,  the  return
                                                            parent to the guest VMs. Currently this technique is lim-
   value is available only at the exit point of the system call.
                                                                   ited to the CPU resource only. We describe key principles
   There are several techniques for intercepting the exit point.
                                                   and implementation details in this subsection.
  One way is to leverage the IRET hypercall handler built into
                                                         Rameter logic in the hypervisor maintains current status
   the Xen hypervisor. In 64-bit Xen, they are invoked trans-
                                                                   of per-CE CPU resource consumption of the target VM.
   parently, whereas in 32-bit mode, it is enabled only when
                                            When it detects that one of the CE starts to exceed the CPU
  VM86 mode is set, which is the backward compatibility
                                                       consumption deﬁned by a policy, it initiates the resource
  mode that allows real mode instructions to execute in the
   protected mode. For 32-bit Xen, we need to modify one jnz   control technique, whose principle is described in Fig. 3. It
   instruction to jmp in arch/i386/kernel/entry-xen.S  shows an example thread scheduling sequence at a CPU
                                                                   that  is assigned to the target VM, where two threads,
   to force the IRET hypercall. Another method is to use the
                                                               thread1 and thread2, alternate. Let us assume Rameter has
  page protection mechanism. At the system call entry point,
  we perform two tasks. First, we turn off the PAGE_PRESENT   already determined that thread1 and thread2 are bound to
                                                    CE1 and CE2, respectively. Rameter aims to reduce the CPU
   bit of the page table entry that holds the use stack page
                                                         usage of CE2, and, thus, thread2 is the subject of throttling
   address. Second, we record the address of kernel stack
                                                                   in this case. Whenever Rameter in the hypervisor detects
  which  is available in one of the Xen-deﬁned variables.
                                                               the scheduling event of the VM, it checks if next thread is
  When the system call exits, it will attempt to write the return
                                                                  thread2.  If so, Rameter increases the frequency of timer
   value from EAX to the user stack. This will trap and, when
                                                                  interrupts from 100/s to 200/s until next scheduling event
   the Xen hypervisor gains the control, the EAX value can be
                                                                    ﬁres. Since VM’s notion of time is based on the timer inter-
   read from the kernel stack. We have tested these mecha-
                                                              rupts from the hypervisor, faster timer causes the next
   nisms and conﬁrmed that they were able to retrieve the
                                                            scheduling to happen sooner. In the ﬁgure, thread2  is
   return values. However, for the convenience in the experi-
                                                         descheduled only after 5 ms, although VM’s OS kernels
   ment, we have inserted custom hypercalls to the exit point
                                                               thinks 10 ms has passed. Timer rate  is restored when
   of the guest kernel system calls and directly delivered the
                                                               thread2 is descheduled.
   return values to the hypervisor.
                                    VM scheduling events are captured by Rameter when
                                                            thread context switch occurs. In Xen 3.1.4, all the context
   6.3  Detection of Scheduling Events                    switching traps at do_stack_switch() in xen/arch/
   There are three types of scheduling events we need to  x86/x86_32/mm.c. Within that function we identify the
  detect—VM scheduling, process scheduling and thread   thread by observing the kernel stack address given by esp
   scheduling. Detection of VM scheduling events is trivial   parameter. If it matches the stack of target thread, we change
   since  it is done by the hypervisor. For other scheduling   the timer rate by assigning new rate as this: current-
   events, the scheduling object in Linux is the light weight  >periodic_period=MILLISECS(1).  Later when  this
   process, equivalent to the thread. Thus, detection of thread   thread is descheduled, we switch back to MILLISECS(10)
   scheduling event covers the process scheduling. In our   to restore the normal rate.
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore. Restrictions apply.

### Página PDF 8

TAK ET AL.: RESOURCE ACCOUNTING OF SHARED IT RESOURCES IN MULTI-TENANT CLOUDS                                                 309


    Fig. 4. Set-up of our synthetic shared service and the CEs exercising it,
   where each server here is a separate VM.

                                                                                    Fig. 5. Impact of workload burstiness on the accuracy by Rameter
     The principles of resource control described here can be   versus LR at S1 in our synthetic shared service, and CPU utilization.
   readily applied to container environments as well. Monitor-  We show error percentages for three CEs (C1,C2,C3) with LR, and label
   ing and/or changing scheduling behavior in containers is    their average as “LR Average.” In all cases, Rameter offers less than
                                                               1 percent error.
   generally easier than from the native hypervisors. Threads
   in containers are visible from the host in the same way it
   sees any other threads. It is also straightforward to change   non-existence of multi-collinearity among x, constant vari-
   the scheduling quantum of targeted threads which is the   ance of errors holds. As will be shown, various system
   basis of our resource control. Note that timer manipulation   properties can violate such pre-conditions and lead to unde-
    is no longer needed for containers because of that.              sirable results. We solve it using the least squares method to
                                                               obtain the coefﬁcients ða0; a1 . . . anÞ for each interval t. Since
  7  EVALUATION                                       each coefﬁcient represents the contribution of each xiðtÞ to
                                                               the resource usage, we treated them as proportions to   In this section we evaluate the efﬁcacy of Rameter and com-
                                                             divide the resource utilization yðtÞ, giving us the break-   pare  it against a baseline technique that uses commonly
                                             down by each CE at Si at time  t. Since we wrote server   available statistics combined with linear regression as an
                                                               codes, we were able to measure the exact amount of CPU   inference method.  First, we explore Rameter’s accuracy
                                                               resources consumed by each CE, which enabled us to calcu-   using CEs and a shared service that are based on home-
                                                                         late the accuracy of LR-based technique.  grown programs for which the “ground truth” can be found
   with conﬁdence. Next, we employ Rameter for accounting
   the usage of two real-life applications used as shared serv-   7.2  Accounting Accuracy for a Synthetic Service
   ices—a clustered MySQL database server and an HBase   7.2.1  Experimental Setup
   key-value store. Throughout, we compare Rameter against   Fig. 4 shows the design and conﬁguration of a synthetic
   a baseline accounting technique called LR (described below)   shared service we employ. We use a two-tiered design for
   that relies upon readily available resource usage informa-   the shared service with the front-end acting as a caching
   tion available in today’s servers.                                       tier. This is a simple data store service in which the front-
                                                    end simulates the data processing and the back-end the
   7.1  Baseline Accounting Technique                                                            data storage. The front-end  is conﬁgured to maintain a
  Our baseline is based on the linear regression model. LR-   cache size of 300 KB. A user request speciﬁes the data
   based modeling technique  is popular  in modeling the   address and the data size in unit of KB. Each user request
   resource usage due to its simplicity, interpretability and   incurs CPU consumption to mimic the data processing over-
  good conformance  to  linearity  for many  cases. Gupta   head. Cache misses at the front-tier result in work generated
   et al. [24] have applied LR to predicting the CPU usage of a   at the back-end. Multiple clients send requests to the front-
  VM using the incoming network trafﬁc volume as the input  end during long-lasting sessions and correspond to our syn-
  and have found that it performed well. LR is also shown to   thetic CEs. Statistics collector gathers CPU, network, and
   be  effective  in modeling and  predicting  the  resource   disk I/O utilizations for LR. LR equation is formed using xi
   requirements due  to  virtualization overhead by Wood  and y as marked in the ﬁgure. Separately, Xen hypervisor
   et al. [25]. Power resource usage modeling is another active   runs its own local monitoring. The reason we use the syn-
  domain of LR’s application [26], [27]. All of the existing   thetic benchmark  is because, having the source code,  it
   application LR tries to model the resource usage at the gran-   allows us to engineer the exact amount of true resource con-
   ularity of VM or individual server. Our key point of study is  sumption we want for determining the error of each tech-
   whether LR is still effective when modeling the resource   nique we apply.
   usage of shared services by various CEs.
    Our LR model relates the resource usage yðtÞ of Si (e.g.
                                                              7.2.2   Effect of Bursty versus Non-Bursty Workload
  CPU utilization time-series) to the inbound network trafﬁc
                                                                       Fig. 5 compares the effect of burstiness/variance in work-  volume xiðtÞ from each Ci. That is, we form the following
                                                           load on the accuracy of CPU accounting at S1. Different   equation for each interval t:
                                                            values of the average request rate are imposed on the
         a0 þ a1  x1ðtÞ þ a2  x2ðtÞ þ  þ an  xnðtÞ ¼ yðtÞ:    (2)  shared service by a group of three chargeable entities C1,
                                                                C2, C3, (which create different CPU utilization levels at
      In applying  this model, we assume  that conditions   the server S1). Eight levels of request rates are chosen for
   for linear regression such as linearity between x and y,  each CE ranging from 15 to 120 req/s at an increment of
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore. Restrictions apply.

### Página PDF 9

310                                                   IEEE TRANSACTIONS ON SERVICES COMPUTING,  VOL. 10,  NO. 2,  MARCH/APRIL 2017


   15. We pick a “non-bursty” scenario where the requests   relevant phenomena  accurately, Rameter  is  robust  to
   are uniformly spaced in time, and a “bursty” scenario  such effects, and offers high-accuracy accounting infor-
  where the request inter-arrival times follow lognormal  mation across a wide range of operating conditions.
   (0,1.0) distribution. We ﬁnd that the efﬁcacy of LR varies
  depending upon  the  extent  of  variation  within  the   7.3  Evaluation With Real-World Services
  imposed workload. This is in line with results known in   In this section, we report on the results of accounting the
   existing work that ﬁnds non-stationarity in workloads  CPU and network bandwidth usage of two real-world
   useful for certain kinds of prediction and modeling [28].  applications—MySQL Cluster and HBase. They are both set
   Intuitively, better accuracy is achieved with bursty work-  up to be shared by multiple Chargeable Entities. MySQL
   loads because the higher variety/dynamism in the input   Cluster represents the class of relational database services,
   data supplies more information to LR; we expect this  and the HBase the class of key-value store services, both
   basic insight to apply to any statistical inference tech-  commonly found in modern cloud services. We compare
   nique for accounting. For a less bursty workload, a large   the resource accounting capabilities of LR with our Rameter
   part of the input data may be redundant and not offer   technique and present the case where LR makes an incorrect
  new information to an inference technique. On the other   conclusion whereas Rameter remains robust. In general, we
   hand, by virtue of its direct measurement of relevant phe-   cannot expect to determine a real-world application’s actual
  nomena, Rameter is able to achieve accurate accounting   resource usage on behalf of different chargeable entities
   that is robust to changes in such workload conditions.      without resorting to extensive application and OS instru-
                                                             mentation. Consequently, unlike for our synthetic shared
                                                                      service, we cannot obtain/present a direct comparison of   7.2.3   Effect of Other Factors
                                                               the efﬁcacy of our techniques, i.e., distance of the account-
  We have also studied the effect of caching and buffering as                                                             ing information offered by Rameter versus that offered by
   well as varying number of chargeable entities. We ﬁnd that                                              LR from the “ground truth.” Therefore the focus of this sec-
   caching and buffering—both valuable and prevalent perfor-                                                                   tion is not on the accuracy of the accounting results from
  mance enhancement techniques—affect the accuracy  of                                                          both LR and Rameter. In actual systems management, this
   accounting of a technique like LR. As is well-known in gen-                                                                rank order can be more important than the accuracy of
   eral, a cache within or in front of a service can destroy/dis-                                                              resource accounting since management algorithms often
   tort correlations between its incoming request/trafﬁc events                                                      need to pick the victim to enforce actions to. If a resource
  and the workload imposed on its underlying server in com-                                                            accounting technique tells you the resource consumption
   plex ways. Buffering of requests/trafﬁc can also have a sim-                                                              quantity with certain level of error (although  it may be
    ilar effect by modifying the time lag between an event (e.g.,                                                      unknown), it can be less problematic than the case in which
   the issuance of a request) and its cause (e.g., the actual ser-                                                                                               it picks the wrong entity as the largest consumer of the
   vicing) in complicated ways. We have carried out experi-                                                                 resource. We demonstrate in this section that such cases do
  ments where we vary several factors affecting the degree                                                                       exist under LR in both MySQL Cluster setting and the
  and nature of caching within the front-tier of our shared ser-                                                   HBase setting. We also show that Rameter does not suffer
   vice (see Fig. 4): request size (ﬁxed or varying), read/write                                                      from such problem. In MySQL Cluster experiments, we
   ratio (from 10:1 to 1:1), temporal locality (non-existent to                                                        mainly focus on the CPU resource accounting. We show
   very high), and the extent of common/overlapping content                                                                     results for the accounting of the most bottlenecked resource
   requested by the chargeable entities. Although graphs are                                                                     for the shared service, which we ﬁnd to be CPU cycles for
   omitted for the interest of space, we observe that caching                                           MySQL and network bandwidth for HBase. One interesting
   factors described above also have various degree of impacts                                                   power of Rameter is the capability to control the resource
   to the accuracy LR results. The error of LR-based resource                                                         usage at the thread-level in real-time, transparently to the
   accounting ranged from 10 to 60 percent with high variance                                                             guest VMs. We demonstrate our early implementation of
   whereas Rameter exhibited less than 1 percent error for all                                                                        this functionality by showing how it can be used in systems
   cases. Accuracy gains from the burstiness of the workloads                                                  management tasks. In HBase experiments, we put more
   can be easily offset if application happens to employ some                                                        emphasis on the accounting of network I/O bandwidth.
  form of caching structure internally.                                                                Also, in order to provide the proof of Rameter’s capability
                                                                    to perform resource accounting at any node within the
   7.2.4  Summary of Key Findings                         shared service infrastructure, we present the accounting
  To summarize, we ﬁnd that the efﬁcacy of LR relies upon   results of non-front-end node of HBase settings.
   both the quality of data  it gathers as well as the pres-
   ence/extent of correlation between  its inputs and out-   7.3.1   Clustered MySQL as the Shared Service
   puts. Even when accurate data can be obtained (as with   Experimental setup. Fig. 6 shows the set-up of our MySQL
   our implementation of LR), several factors including  (i)   cluster that is used as a shared service by three CEs. Two of
   inherent workload properties  (e.g., variance, temporal   these CEs use the TPC-W benchmark [29] to generate work-
   locality,  intensity),  (ii) system mechanisms and  algo-   load for the database, while the third CE uses RUBiS [30].
   rithms (e.g., caching or buffering), and (iii) environmental  The cluster consists of a front-end SQL node that interacts
   conditions  (e.g., degree  of resource  interference from  with the CEs, three data nodes, and a management node;
   other S/W) might affect such correlation and affect the   each node is hosted within its dedicated server. One inter-
   accuracy of the accounting technique. We ﬁnd empirical   esting aspect of the cluster’s operation is that even in the
   evidence that, owing to  its ability to directly measure   absence of any workload imposed by the CEs, a large
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore. Restrictions apply.

### Página PDF 10

TAK ET AL.: RESOURCE ACCOUNTING OF SHARED IT RESOURCES IN MULTI-TENANT CLOUDS                                                 311


    Fig. 6. Shared MySQL cluster setting. Three CEs labeled C1, C2, and C3
   share this database service.


  number of small messages are exchanged between all pairs
   of nodes within the cluster for liveness check. The CEs
   house separate/non-overlapping data within the database
  which is spread across the three data nodes, and the cluster
   has a replication degree of 1.
      Experiment design and key ﬁndings. Given exact accuracy
  numbers are elusive, we compare the efﬁcacy of Rameter
  and LR in the following online resource control situation: we    Fig. 7. Comparison of CPU accounting results. CPU usage of MySQL
                                                                             Cluster SQL node is being accounted. By comparing the areas of equiv-  wish to ensure that when the aggregate workload imposed
                                                                                alent color we see the rank order determined by each technique as well
  upon the MySQL cluster causes its server CPUs to saturate,   as accuracies.
  we  identify  the  contribution  of  various CEs  to  this
   “overload,” and then enforce targeted CPU throttling only to  LR and Rameter at one of the MySQL servers, SN, and how
   the CE causing the overload. We implement a CPU throttling    it evolves during phases 1-3 (results for CPU accounting of
  mechanism within the Xen hypervisors of the MySQL cluster   other nodes are qualitatively similar and we do not present
   servers which manipulates the rate at which timer interrupts  them in the interest of space).
   are delivered to the guest VM only when the thread serving      Figs. 7a, 7b show CPU accounting for the SQL node (SN)
   the CE causing the overload is to be scheduled.                as carried out by LR and Rameter, respectively. We use a
    We conﬁgure CEs to impose a dynamically changing   “stacked” representation, where the area under the curve
  workload  (consisting  of  three  phases) on MySQL  as   corresponding to a CE represents the CPU usage charged to
   described in Table 2. In phase 1, all CEs generate a low-    it. During phase 1, both LR and Rameter produce correct
   intensity workload, whose aggregate does not saturate the   rank orders of CEs, although LR slightly overestimates the
  MySQL servers. During phase 2, starting at t = 400 s, C2  CPU consumption for C2. However, during phase 2, LR
   starts to issue CPU-intensive requests. We are interested in   starts to report incorrect rank order: it determines C3 to be
   observing how LR and Rameter handle this sudden change   the cause of the increased CPU usage. Upon investigating
   of behavior. Finally, in phase 3, starting at t = 600 s, C2   the reason for this mistake by LR, we ﬁnd the following.
   issues continually increasing workloads that cause the CPU  While C2 issues CPU-heavy requests and waits for MySQL’s
   to saturate. Here we are interested in observing how our   response, the CPU utilization stays at high level. During
   simple resource throttling performs based on the account-   this, C3 continues to issue requests at a relatively high rate
   ing information offered by LR and Rameter.                    that are not CPU-heavy. However, the higher  rate  of
      Since we do not have precise knowledge  (i.e., ground   requests coming from C3 causes LR to infer spurious posi-
   truth) about true resource consumption, we engineer the   tive correlation between C3’s requests and SN’s CPU usage.
   workloads so that the CPU consumption imposed by the   In fact, LR is unable to correct this throughout phase 2.
  CEs is signiﬁcantly different from each other, allowing us to    As we show in Fig. 7b, besides correctly identifying the
   rank their contributions without ambiguity. For example,   correct rank order in its accounting, Rameter also reports
  we make the CPU consumption of C2 much larger than  what portion of the CPU usage of SN’s server it ﬁnds unac-
   others starting at t = 400 s so that other CEs cannot be mis-   countable. This amount indicates that Rameter’s algorithm
   taken as heavy CPU consumers. We begin by taking an in-  was unable to charge the given thread’s resource usage to
   depth look at the CPU accounting information offered by  any of the chargeable entities because no direct association
                                                  was found. This can happened if some thread is spawned
                      TABLE 2                         independently of input requests from the chargeable enti-
                 Workload Playback Scenario                       ties and performs maintenance jobs. Or, it could be due to
                                                               the nature of the thread that is created to service other run-
   Phase    Time Window       Workload       Top User   ning threads. In any case, Rameter provides this resource
   Phase 1       0-400 s        All 3 CEs generate       C2      usage to the user and it is up to the user to divide up among
                                    light loads                       chargeable entities. The most reasonable division would be
   Phase 2      400-600 s      C2 starts to issue         C2       to divide the ‘unaccountable’ portion according to the pro-
                          CPU-heavy requests              portion of resource usage by each chargeable entity within
                                C2’s workload                     that time window.
                           overwhelms                           Fig. 9 quantiﬁes the accuracy of accounting results of
   Phase 3     600-1,200 s     CPU, load increases      C2                                                                       Fig. 7. In order to get the ground truth, we perform separate
                              every 100 s
                                                               individual  runs and  use  the CPU  measurements  as
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore. Restrictions apply.

### Página PDF 11

312                                                   IEEE TRANSACTIONS ON SERVICES COMPUTING,  VOL. 10,  NO. 2,  MARCH/APRIL 2017


                                                                                    Fig. 10. Set-up of HBase as a shared service. We have two CEs labels
                                                                  as YCSB1 and YCSB2 running YCSB workload generator.    Fig. 8. Response time development of RUBiS for two cases—throttled by
   LR, and controlled by Rameter. LR incorrectly picks C3 as a culprit for
   performance degradation. Throttling the request rate of C3 has no effect.   servers” and the HBase “master” that manages these region
   However, Rameter is able to prevent SLA violation.                      servers. The region servers act as in-memory caches for the
                                                               contents of the data nodes. HBase stores  its data in a
   estimations of true consumption (labeled as ‘separate runs’).  Hadoop cluster, and this is a great example of a shared ser-
  Comparing the SUM columns, we observe that combined   vice (HBase) relying upon another shared service (Hadoop)
  workload generates less CPU consumption than the sum of   to cater to the needs of CEs using  it. Due to space con-
   individual runs in our application. Therefore, we use the   straints, we only discuss accounting of HBase servers. A
   percentage of totals as the basis for comparison. Fig. 9b   region server employs an HDFS client to communicate with
  shows the average difference of the percentage of totals for   the Hadoop cluster that stores data persistently. HBase
   Rameter and LR when compared to the ‘Separate Runs’.  employs Zookeeper for coordinating distributed operations
   Rameter consistently differs by 4.3 5.3 percent whereas LR  and locating region servers. We conﬁgure our HBase with a
   deviates by larger amount as workload intensiﬁes from   single region server. HBase operation involves signiﬁcant
   phase 1 to phase 3.                                        data transfer from the data nodes to the region server,
     During phase 3, starting at t ¼ 600 s, C2 starts to saturate  whereas the CPU load imposed by most requests is small as
   the CPU by drastically increasing the workload it imposes  most requests are for simple data retrieval or inversions.
   as described in Table 2. As portions of Figs. 7a and 7b for   Since the network bandwidth available to the region server
   this phase show, LR continues to perform incorrect account-  becomes the bottleneck resource well before the CPU, we
   ing. This has a detrimental effect on our CPU policing based   highlight accounting results for network bandwidth. Our
   resource control. Fig. 8 shows the change of response time  HBase caters to requests from two CEs derived from the
   for C3 whose RUBiS application is accessing the shared  YCSB workload generator [31] (CA and CB).
  MySQL Cluster service. Starting from time 600, the response     Experiment design and key ﬁndings. Fig. 10 is the conﬁgura-
   time increases. We have set the response time of 300 ms as   tion of our HBase installation used in this experiments. We
   the initial warning level and 600 ms as the SLA violation  run an experiment lasting 500 seconds, during which the
   level. The CPU  saturation caused by C2  continues  to   loads offered by CA and CB are varied as follows: (i) during t
   degrade the response time of RUBiS and eventually it viola-  = 0 to t = 100 s, both CA and CB generates identical work-
   tes the SLA. Since LR determines that C3, not C2, is the   loads which contains 5 percent update requests, (ii) at t =
   source of overload (see Fig. 7a), C2 is not marked for any   100 s, CB changes to a read-intensive mode with good tem-
   counter actions. However, Rameter is able to identify true   poral locality, which incurs high hits in the region server
   cause of the overload and, starting at time 730, it initiates   causing its CPU usage to increase proportionally with the
   the CPU throttling for C2. Fig. 8 indicates that the moving  network trafﬁc sent to CB, (iii) at t = 200 s, CA starts to issue
   average of response time under the control of Rameter is   CPU-intensive insert-type requests that cause the CPU usage
   able to contain the response time below the SLA limit. This   at the region server to increase. Fig. 11 shows the network
   demonstrates one promising capability of Rameter (i.e., the   trafﬁc size inbound to the region server from the two CEs.
   thread-level monitoring technique) in critical resource man-      Fig. 12a and 12b shows the result of accounting the net-
   agements of such shared resources.                     work bandwidth by LR and Rameter at the region server of
                                                        HBase. The inputs to the LR are two time series of inbound
   7.3.2  HBase as the Shared Service                    network trafﬁc from two chargeable entities as shown in
   Experimental setup. Our second real-world shared service is   Fig. 11. We have conﬁgured LR to use 100 second-long data
   HBase, a key-value storage system offering an open-source   as an input length in this HBase’s resource accounting, pro-
   implementation of Google’s Bigtable, that has signiﬁcantly  ducing no accounting results for the ﬁrst 100 seconds of the
   different resource usage characteristics from a database
   such as MySQL. An HBase cluster consists of “region


                                                                                    Fig. 11. Evolution of incoming network trafﬁc to the region server from
                                                                    two CEs. Both CA and CB sends similar requests to HBase during t = 0
                                                                                   to t = 100 s consuming equal network bandwidth. CA changes its behav-
    Fig. 9. Comparison of accounting accuracy.                                       ior at t = 100 s, and CB changes its behavior at t = 200 s.
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore. Restrictions apply.

### Página PDF 12

TAK ET AL.: RESOURCE ACCOUNTING OF SHARED IT RESOURCES IN MULTI-TENANT CLOUDS                                                 313

                                                                     TABLE 3
                                                         Overhead of System call Interception and Information Recording

                                                          System        Typical Avg     System call    System call
                                                                                call name  Turn-around time   Interception   Intcpt&Record

                                                              read          72.0 microsec        .38%          .59%
                                                                 recv           39.6 microsec        .71%         1.07%
                                                                  write          26.4 microsec       1.07%         1.60%
                                                          send         134.3 microsec       .21%          .31%
                                                        open          41.9 microsec        .67%         1.01%
                                                                  accept         14.6 microsec       1.93%         2.89%
                                                               connect      148.0 microsec       0.19%         0.29%
                                                           pread         54.0 microsec       0.52%         0.78%


                                                            (orange color). It includes CPU cycles consumed for com-
                                                          municating with the Zookeeper, HBase master and Hadoop
    Fig. 12. Comparison of accounting results between LR and Rameter on  Namenodes. Especially, we have noticed two high peaks at
   the out-bound network trafﬁc from data node to the region server.        around 80 and 470 sec. By studying the HBase documenta-
                                                                        tions, we have concluded that these would most likely be
   run. The accounting results from Rameter are presented in  due to the I/O compaction at the region server.
   Fig. 12b. In both of the stacked graphs, the upper area corre-
   sponds to the portion of network bandwidth used by CB   7.4  Overhead
  and the lower one, the portion used by CA. The network                                                    The overhead of Rameter exists at both the local monitoring
  bandwidth usage of CA drops at t = 200, thus making CB                                                   and the collective inference steps. During the local monitor-
   the heavier consumer of network bandwidth. LR continues                                                             ing step, the control of the intercepted system call is deliv-
   to report CA as the dominant consumer of network band-                                                           ered to the hypervisor and several information including
   width. In contrast, Rameter correctly reﬂects this resource
                                                         system call parameters, time stamps and thread identiﬁers
   usage by CEs. (See Fig. 12b after t = 200 s). The misjudgment
                                                                are recorded. Since these tasks must be completed before
  by LR can be explained in terms of caching effects. After
                                                              returning the control back to the system call handler of
    t = 200, the trafﬁc from CB to the region server doubles by
                                                 VM’s guest kernel, the delay here directly affects the perfor-
   the end of the run (See Fig. 11) whereas the trafﬁc from data
                                                        mance.  Therefore,  our  overhead measurement  closely
   nodes increases by only 20 percent. We believe this is due to
                                                               focuses on this aspect. However, we consider the overhead
   caching within the region server and HBase documentation
                                                                   of collective inference to be negligible. For the ofﬂine mode,
   supports this conjecture.
                                                               the overhead of inference is out of the critical path since it is
    We also present some of the selected accounting results
                                                       performed at separate server node. For the online mode
   using Rameter. Fig. 13a shows the CPU accounting at the
                                                      needed by the resource control, the hypervisor manages   region server for CA and CB. According to our preplanned
                                                             small number of variables corresponding to the CEs and  workload scenario, CB should consume more CPU than CA
                                                                     carries out simple arithmetic. Thus, we present the over-   after time 200 sec. The accounting result indicates this
                                                      head of the local monitoring step below.   behavior. Notice the signiﬁcant portion of unaccountable
                                                                 In order to better explain the overhead of Rameter’s  CPU usage at the bottom region of the stacked graph
                                                                     local monitoring step, we provide our measurement data
                                                                  in Table 3. It shows the performance impact of two core
                                                    mechanisms to various system calls. The ﬁrst mechanism
                                                                                is the system call interception alone within the hypervi-
                                                                       sor. The second mechanism is the system call interception
                                                   and data recording (via TRACE_xD macro of xen). We
                                                                  ﬁrst measured pure time overhead of these two opera-
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
    Fig. 13. Results by Rameter at various nodes of HBase. (b) shows   less than 3 percent. Therefore, the data gathering during
   Rameter’s capability to account resource at multiple hops away from the
    front-end of the shared service. Note that data node of HBase does not   the local monitoring step incurs small overhead to the
   have a direct contact with CEs.                                running applications within the guest VM.
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore. Restrictions apply.

### Página PDF 13

314                                                   IEEE TRANSACTIONS ON SERVICES COMPUTING,  VOL. 10,  NO. 2,  MARCH/APRIL 2017

  8  RELATED WORK                                       logs as well as network usage of distributed applications.
                                                       Rameter can be beneﬁt from such monitoring tools by
   Earlier works by Banga et al. have addressed the issue of
                                                            extending it to leverage the information provided by them.
   resource accounting within a single host [10]. They intro-
                                                                  In the evaluation we have demonstrated a use of resource
  duced new abstraction, called resource containers, to be used
                                                            accounting in preventing SLA violation via our resource   as a new resource principal within the kernel. Realization of
                                                                 control technique. The problem of resource control has been   the resource container required modiﬁcations of the kernel as
                                                                investigated in several studies and various effective techni-   well as applications. Distributed resource container [21],
                                                        ques have been developed [37], [38], [39], [40], [41].. One  and Power Container [32] are extensions of it to the distrib-
                                                    main difference of our resource control problem is that we   uted environment in which local resource containers are
                                                                are required to control the resource usage at ﬁner thread  bound together by exchanging global identiﬁers via IPv6
                                                                granularity within a shared instance, whereas these studies   optional ﬁeld in order to coordinate the resource consump-
                                                    aim to better-schedule separate VM instances. However,   tion across hosts. The goal is to throttle the energy con-
                                                                 control theoretic techniques such as the one in Q-clouds [40]   sumption per applications. The use of resource container
                                                         can be applied to ours to achieve accurate CPU usage ratio   relies on the help from the application for correct and timely
                                                among CEs.   binding of resource principals to the container, although
   they also describe heuristics to automatically detect the
   bindings. The OS has to be modiﬁed to support the neces-                                            9  CONCLUSION
   sary data structure for representing the resource containers
   (and the propagation of it to other hosts in case of the dis-   In this paper we have presented our study on the problem
   tributed resource container).                                   of resource accounting within an IT platform that offers
     The resource accounting problem has been studied by a   shared services. In order to understand the nature of the
  number of researchers. Reumann et al. [7] have recognized  problem and ﬁnd effective solution we have explored two
   the problem and proposed a mechanism, Stateful Distributed   different accounting techniques built with different balance
   Interposition, for sharing the application context information   of emphasis - LR-based technique and Rameter. Our main
   across  multi-tiered  servers  to support  actions such as   contribution is the resource accounting framework, Rameter,
   enforcing resource quota. They deﬁned the context abstrac-   that operates at the hypervisor. It combines the monitoring
   tion that included the identity of the client and achieved the   unit that collects ﬁne-grained thread-level data and the
   creation of the contexts and propagation of them across   inference unit that applies light-weight inference. Compar-
   server via modiﬁcation of OS and applications. Users are   ing with LR-based approach, our analysis revealed that
   required to recompile the application after instrumenting it.   there could be cases where more ﬁne-grained monitoring
   Fonseca et  al. [8] described an architecture, Quanto, for   information does not only provide better accuracy, but also
   tracking the energy consumption of embedded devices. To  impact critical management decisions. Rameter also incurs
   achieve the goal of energy tracking, they have developed a   only about 1-2% of the turn-around time overhead to the
  framework for resource accounting of distributed devices.  system calls that are intercepted.
   Since their target environment is embedded systems, they
  were able to support the scenario in which they make modi-  REFERENCES
   ﬁcations to the OS kernel and require the developers to                                                                                         [1]   E. M. Haber, E. Kandogan, and P. Maglio, “Collaboration in
   write applications that notify the OS of the owner of various        system administration,” Queue, vol. 8, no. 12, pp. 10:10–10:20,
    activities. In one of the most recent work by Narasayya        Dec. 2010.
   et  al.  [9],  the  resource  accounting problem has been    [2]   E. Kotsovinos, “Virtualization: Blessing or curse?” Queue, vol. 8,
                                                                            pp. 40:40–40:46, 2010.
   addressed in the context of mitigating the performance    [3]  Amazon  SimpleDB.  [Online].  Available:  http://aws.amazon.
   interferences due to resource sharing within SQL Azure       com/simpledb/, 2015.
  RDBMS. Their accounting mechanism relies on modifying    [4]  SQL Azure Whitepaper. [Online]. Available: http://social.technet.
                                                                               microsoft.com/wiki/contents/articles/1695.inside-windows-
   the internals of the SQL Azure database.
                                                                                    azure-sql-database.aspx, 2010.
     There are plenty of works related to monitoring of distrib-    [5]  Latency is everywhere and  it costs you sales-how to crush  it.
   uted systems that are relevant to the resource accounting         [Online].  Available:  http://highscalability.com/blog/2009/7/
   although they do not explicitly target the resource accounting        25/latency-is-everywhere-and-it-costs-you\\-sales-how-to-crush-
  problem we address in this work. Ganglia [33] is a distrib-          it.html, 2009.
                                                                                         [6]   S. Agarwala, F. Alegre, K. Schwan, and J. Mehalingham, “E2eprof:
   uted monitoring system with scalability in mind. The goal is       Automated end-to-end performance management for enterprise
   to provide statistics related to various resource types per        systems,” in Proc. 37th Annu. IEEE/IFIP Int. Conf. Dependable Syst.
   server in clusters. It does not support ﬁne-grained resource         Netw., 2007, pp. 749–758.
                                                                                         [7]    J. Reumann and K. G. Shin, “Stateful distributed interposition,”
   usage monitoring per chargeable entities. Chopstix [34] pro-                                                ACM Trans. Comput. Syst., vol. 22, no. 1, pp. 1–48, Feb. 2004.
   vides detailed monitoring information about low-level OS    [8]   R. Fonseca, P. Dutta, P. Levis, and I. Stoica, “Quanto: Tracking
   events. It adds a data structure, sketches, to the kernel in order        energy in networked embedded systems,” in Proc. 8th USENIX
   to monitor page allocation, mutex/semaphore locking, and         Conf. Operating Syst. Des. Implementation, Berkeley, CA, USA, 2008,
                                                                            pp. 323–338.
  CPU utilization. They focus on building a sampling-based                                                                                         [9]   V. R. Narasayya, S. Das, M. Syamala, B. Chandramouli, and
   system that monitors events of interest as a high resolution          S. Chaudhuri, “Sqlvm: Performance isolation in Multi-tenant rela-
   with low overhead. OProﬁle [35] is capable of delivering         tional Database-as-a-service,” in Proc. CIDR, 2013, pp. 1–9.
   detailed system-wide proﬁle information. It provides conve-    [10] G. Banga, P. Druschel, and J. C. Mogul, “Resource containers: A
                                                           new facility for resource management in server systems,” in Proc.
   nient access to the performance counters. Nagios [36] is an        3rd Symp. Operating Syst. Des. Implementation. Berkeley, CA, USA,
  open source monitoring system that monitors CPU, disk,         1999, pp. 45–58.
Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore. Restrictions apply.

### Página PDF 14

TAK ET AL.: RESOURCE ACCOUNTING OF SHARED IT RESOURCES IN MULTI-TENANT CLOUDS                                                 315


    [11]  B. Hindman, A. Konwinski, M. Zaharia, A. Ghodsi, A. D. Joseph,    [35] John  Levon.  Oproﬁle.  [Online].  Available:  http://oproﬁle.
         R. Katz, S. Shenker, and I. Stoica, “Mesos: A platform for Fine-         sourceforge.net/credits/, 2014.
        grained resource sharing in the data center,” in Proc. 8th USENIX    [36]  Introducing the Windows Azure Paltform. [Online]. Available:
         Conf. Netw. Syst. Des. Implementation, Berkeley, CA, USA, 2011,        http://go.microsoft.com/?linkid=9752185, 2011.
        pp. 295–308.                                                            [37]  F. Checconi, G. Anastasi, and L. Abeni, “Respecting temporal con-
    [12] Mesosphere. [Online]. Available: https://mesosphere.com/, 2015.          straints in virtualised services,” in Proc. 2nd IEEE Int. Workshop
    [13]  Stratoscale.  [Online].  Available: http://www.stratoscale.com/,        Real-Time Serv.-Oriented Archit. Appl., 2009, pp. 73–78.
         2015.                                                                    [38]  F. Checconi, T. Cucinotta, D. Faggioli, and G. Lipari, “Hierarchical
    [14] D. Wentzlaff and A. Agarwal, “Factored operating systems (FOS):        multiprocessor cpu reservations for the linux kernel,” in Proc. 5th
       The case for a scalable operating system for multicores,” SIGOPS           Int. Workshop Operating Syst. Platforms Embedded Real-Time Appl.,
         Oper. Syst. Rev., vol. 43, no. 2, pp. 76–85, Apr. 2009.                        2009, pp. 15–22.
    [15] Openstack.  [Online].  Available:  http://www.openstack.org/,    [39]  J. Lee, S. Xi, S. Chen, L. T. X. Phan, C. Gill, I. Lee, C. Lu, and O.
         2015.                                                                  Sokolsky,   “Realizing   compositional   scheduling   through
    [16]  (2008). The Force.com Multitenant Architecture: Understanding         virtualization,” in Proc. IEEE 18th Real Time Embedded Technol.
         the Design of Salesforce.com’s Internet Application Development         Appl. Symp.,  Washington, DC, USA, 2012, pp. 13–22.
         Platform. [Online]. Available: in Force.com Whitepaper http://wiki.    [40]  R. Nathuji, A. Kansal, and A. Ghaffarkhah, “Q-clouds: Manag-
         developerforce.com/index.php/Multi_Tenant_Architecture                    ing performance interference effects for qos-aware clouds,” in
    [17]  F. Chang, J. Dean, S. Ghemawat, W. C. Hsieh, D. A. Wallach, M.         Proc. 5th Eur. Conf. Comput. Syst., New York, NY, USA, 2010,
        Burrows, T. Chandra, A. Fikes, and R. E. Gruber, “Bigtable: A dis-        pp. 237–250.
         tributed storage system for structured data,” in Proc. 7th USENIX    [41]  S. Xi, J. Wilson, C. Lu, and C. Gill, “Rt-xen: Towards Real-time
        Symp. Operating Syst. Des. Implementation, Berkeley, CA, USA,        hypervisor scheduling in xen,” in Proc. 9th ACM Int. Conf. Embed-
         2006.                                                                   ded Softw., New York, NY, USA, 2011, pp. 39–48.
    [18] M. Burrows, “The chubby lock service for loosely-coupled distrib-
        uted systems,” in Proc. 7th Symp. Operating Syst. Des. Implementa-                  Byung Chul Tak is a research staff member at
           tion, Berkeley, CA, USA, 2006, pp. 335–350.                                     IBM  T.J. Watson Research  Center, Yorktown
    [19]  S. Ghemawat, H. Gobioff, and S.-T. Leung, “The google ﬁle sys-                         Height, NY. He received his PhD in computer sci-
        tem,” in Proc. 19th ACM Symp. Operating Syst. Principles, New                     ence in 2012 from Pennsylvania State University.
        York, NY, USA, 2003, pp. 29–43.                                          He received his MS degree in computer science
    [20] M. Y. Chen, A. Accardi, E. Kiciman, J. Lloyd, D. Patterson, A. Fox,                       from Korea Advanced Institute of Science and
       and E. Brewer, “Path-based faliure and evolution management,”                       Technology (KAIST) in 2003, and his BS from
         in Proc. 1st Conf. Netw. Syst Des Implementation, Berkeley, CA,                       Yonsei University, Korea in 2000. Prior to joining
       USA, 2004, pp. 23–23.                                                                Pennsylvania State University, he worked as a
    [21] A. Weissel and F. Bellosa, “Dynamic thermal management for dis-                        researcher in the Electronics and Telecommuni-
         tributed systems,” in Proc. 1st Workshop Temperature-Aware Com-                         cations  Research  Institute  (ETRI),  Daejeon,
          put. Syst., Munich, Germany, Jun. 2004, pp. 1–11.                   Korea. His research interest includes virtualization, operating systems
    [22]  P. Barham, A. Donnelly, R. Isaacs, and R. Mortier, “Using magpie   and cloud computing.
         for request extraction and workload modelling,” in Proc. 6th Conf.
        Symp. Opearting Syst. Des. Implementation, Berkeley, CA, USA,
         2004, pp. 18–18.                                                               Youngjin Kwon is a PhD candidate at computer
    [23] A. Dinaburg, P. Royal, M. Sharif, and W. Lee, “Ether: Malware                        science department, the University of Texas at
         analysis via hardware virtualization extensions,” in Proc. 15th                          Austin. He received his BS degree in computer
     ACM Conf. Comput. Commun. Security, New York, NY, USA, 2008,                        science from Sogang University in 2007, and his
        pp. 51–62.                                                MS degree  in computer science from Korea
    [24] D. Gupta, L. Cherkasova, R. Gardner, and A. Vahdat, “Enforcing                     Advanced Institute of Science and Technology
        performance isolation across virtual machines in xen,” in Proc.                       (KAIST) in 2009. He started his PhD program in
       ACM/IFIP/USENIX Int. Conf. Middleware, 2006, pp. 342–362.                             Sep, 2012. His current research interests are in
    [25]  T. Wood, L. Cherkasova, K. Ozonat, and P. Shenoy, “Proﬁling and                             virtualization  technology,  improving  operating
       modeling resource usage of virtualized applications,” in Proc. 9th                       system, and system security.
       ACM/IFIP/USENIX Int. Conf. Middleware, 2008, pp. 366–387.
    [26] A. Kansal, F. Zhao, J. Liu, N. Kothari, and A. A. Bhattacharya,
         “Virtual machine power metering and provisioning,” in Proc. 1st
     ACM Symp. Cloud Comput., New York, NY, USA, 2010, pp. 39–50.                    Bhuvan Urgaonkar is an associate professor in
    [27]  J. C. McCullough, Y. Agarwal,  J. Chandrashekar, S. Kuppusw-                         the department of computer science and engi-
       amy, A. C. Snoeren, and R. K. Gupta, “Evaluating the effective-                        neering at the Pennsylvania State University. He
        ness of Model-based power characterization,” in Proc USENIX                         received his MS (2002) and PhD (2005) degrees
         Conf. USENIX Annu. Tech. Conf., Berkeley, CA, USA, 2011, p. 12.                                 in computer science at the University of Massa-
    [28] C. Stewart, T. Kelly, and A. Zhang, “Exploiting nonstationarity for                          chusetts, and his BTech (1999) in computer sci-
        performance prediction,” in Proc. 2nd ACM SIGOPS/EuroSys Eur.                     ence and engineering at IIT Kharagpur. He is a
         Conf. Comput. Syst., 2007, pp. 31–44.                                                            recipient of the NSF CAREER Award, research
    [29] W.  Smith. TPC-W: Benchmarking An Ecommerce  Solution.                      awards from HP Labs and Cisco, and has co-
         [Online].  Availabole:  http://www.tpc.org/information/other/                       authored best student papers at IEEE MASCOTS
          techarticles.asp, 2010.                                                        2008 and ICAC 2005 conferences. His research
    [30] RUBiS. [Online]. Availabole: http://rubis.objectweb.org/, 2008.      involves applying ideas from distributed computing, resource manage-
    [31]  B. F. Cooper, A. Silberstein, E. Tam, R. Ramakrishnan, and R. Sears,   ment, scheduling, performance evaluation, and analytical modeling to
       “Benchmarking cloud serving systems with ycsb,” in Proc. 1st   the design and evaluation of data centers, networked systems, operating
     ACM Symp. Cloud Comput., New York, NY, USA, 2010, pp. 143–154.   systems, virtualization techniques, and storage systems. His current
    [32] K. Shen, A. Shriraman, S. Dwarkadas, X. Zhang, and Z. Chen,   research focus is in cloud computing, power management of data cen-
       “Power containers: An os facility for ﬁne-grained power and    ters, and storage systems. Urgaonkar is a senior member of IEEE and
        energy management on multicore servers,” in Proc. 18th Int. Conf.   senior member of ACM.
          Archit. Support Program. Lang. Operating Syst., 2013, pp. 65–76.
    [33] M. L. Massie, B. N. Chun, and D. E. Culler, “The ganglia distrib-
        uted monitoring system: Design, implementation and experi-
         ence,” Parallel Comput., vol. 30, pp. 817–840, 2003.
    [34]  S.  Bhatia,  A. Kumar, M.  E.  Fiuczynski, and  L.  Peterson,
        “Lightweight, High-resolution monitoring  for troubleshooting
        production systems,” in Proc. 8th USENIX Conf. Operating Syst.
         Des. Implementation, Berkeley, CA, USA, 2008, pp. 103–116.

Authorized licensed use limited to: Pontificia Universidad Catolica de Valparaiso. Downloaded on September 13,2026 at 20:19:44 UTC from IEEE Xplore. Restrictions apply.
