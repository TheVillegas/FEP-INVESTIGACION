# Optimization of Resource Provisioning Cost in Cloud Computing

> **Pilar:** P2
> **Clasificación:** Declarada en la matriz
> **Evidencia de clasificación:** Fila académica del CSV titulada “Optimization of Resource Provisioning Cost in Cloud Computing”, código P2.
> **Archivo fuente:** papers-pdf/Chaisiri et al. - 2012 - Optimization of Resource Provisioning Cost in Cloud Computing.pdf
> **Uso previsto:** Lectura personal y apoyo documental; requiere validación humana antes de incorporarse al informe.

## 1. Título

*Optimization of Resource Provisioning Cost in Cloud Computing*.

## 2. Autor y fecha

- **Autores verificados en el PDF:** Sivadon Chaisiri, Bu-Sung Lee y Dusit Niyato.
- **Fecha bibliográfica utilizada:** 2012, *IEEE Transactions on Services Computing*, vol. 5, n.º 2, abril–junio de 2012, pp. 164–177.
- El manuscrito fue recibido en 2010 y publicado en línea en 2011; la edición final visible corresponde a 2012.

## 3. Problema que trata

La reserva anticipada puede ser más barata que el consumo bajo demanda, pero una reserva excesiva genera capacidad ociosa y una insuficiente obliga a comprar recursos caros. La demanda futura y los precios son inciertos, y la decisión debe considerar múltiples tipos de VM, proveedores, recursos y etapas de planificación.

## 4. Qué quiere hacer

Minimizar el costo total esperado de aprovisionamiento mediante un algoritmo que equilibre reserva, expansión de reservas, compra bajo demanda y sobreaprovisionamiento en horizontes de varias etapas.

## 5. Cómo lo hace

Formula **OCRP** como programación entera estocástica multietapa con recurso. Desarrolla una formulación determinista equivalente y estudia dos técnicas para problemas grandes: descomposición de Benders y aproximación por promedio muestral (SAA). Evalúa escenarios con precios y demanda probabilísticos, múltiples proveedores y planes de 2 y 12 etapas; compara OCRP con valor esperado (EVU), reserva máxima (MaxRes) y ausencia de reserva (NoRes) (secciones 3–7).

## 6. Resultados

- En el ejemplo simple, la solución de menor costo reserva 30 VM; la reserva es ventajosa desde una demanda de 15, pero no domina cada realización posible (sección 7.2.1, figuras 7–8, p. 174).
- En 1.000 simulaciones, OCRP obtiene el menor costo promedio; NoRes tiene el mayor por compras bajo demanda y MaxRes el mayor costo de sobreaprovisionamiento. OCRP reserva 59 VM frente a 100 de MaxRes (sección 7.2.3, tabla 4, p. 175).
- Benders converge en 42 iteraciones al mismo óptimo de la formulación directa, aunque el problema maestro puede ser costoso (sección 7.2.4, figura 9).
- En el caso de 12 etapas, SAA identifica una solución con reservas de seis meses en T1 y T7 y 40 VM reservadas en cada una (sección 7.3, tabla 5, p. 176).

## 7. Discusión y trabajo futuro

El modelo prioriza reducir el costo bajo demanda sin caer en reserva máxima. Los autores destacan la utilidad del outsourcing hacia nubes públicas cuando el TCO de ampliar infraestructura privada no conviene. Limitan el enfoque porque la programación estocástica no obtiene por sí sola distribuciones correctas y porque la explosión de escenarios dificulta el cálculo. Proponen reducción de escenarios, mejoras a Benders y estudiar precios óptimos para proveedores con competencia (sección 7.4).

## 8. Conclusión del paper

Los autores concluyen que OCRP permite ajustar de forma óptima el compromiso entre reservas y recursos bajo demanda en un mercado con incertidumbre. Benders facilita paralelización y SAA aproxima problemas con muchos escenarios; los estudios numéricos respaldan su uso como herramienta de aprovisionamiento orientada a costo.

## Relación preliminar con INV-01

Se vincula con 3.7.3–3.7.4, 5.8–5.10 y 5.12–5.13 de INV-01: compromisos, capacidad excedente, optimización y sensibilidad a demanda/precio. Es una base matemática histórica; no ofrece tarifas vigentes ni un caso TCO de cinco años listo para reutilizar.

## Limitaciones de esta síntesis

Los supuestos y precios corresponden al mercado alrededor de 2010–2012. Las tablas contienen notación matemática cuya extracción textual puede perder alineación. Los resultados son simulados y dependen de distribuciones asumidas; deben validarse humanamente antes de usarlos.

## Texto extraído del PDF

> **Advertencia de conversión:** extracción textual automática de 14 páginas (96721 caracteres). Se conservaron títulos, párrafos, referencias y contenido textual por página. La disposición multicolumna, las figuras, las tablas y las ecuaciones pueden no mantener su alineación o representación visual; verifique esos elementos en el PDF original.

### Página PDF 1

164                                                    IEEE TRANSACTIONS ON SERVICES COMPUTING,  VOL. 5,  NO. 2,  APRIL-JUNE 2012

    Optimization of Resource Provisioning
          Cost in Cloud Computing

                          Sivadon Chaisiri, Student Member, IEEE,
                Bu-Sung Lee, Member, IEEE, and Dusit Niyato, Member, IEEE


      Abstract—In cloud computing, cloud providers can offer cloud consumers two provisioning plans for computing resources, namely
       reservation and on-demand plans. In general, cost of utilizing computing resources provisioned by reservation plan is cheaper than
       that provisioned by on-demand plan, since cloud consumer has to pay to provider in advance. With the reservation plan, the consumer
      can reduce the total resource provisioning cost. However, the best advance reservation of resources is difficult to be achieved due to
       uncertainty of consumer’s future demand and providers’ resource prices. To address this problem, an optimal cloud resource
       provisioning (OCRP) algorithm is proposed by formulating a stochastic programming model. The OCRP algorithm can provision
      computing resources for being used in multiple provisioning stages as well as a long-term plan, e.g., four stages in a quarter plan and
       twelve stages in a yearly plan. The demand and price uncertainty is considered in OCRP. In this paper, different approaches to obtain
       the solution of the OCRP algorithm are considered including deterministic equivalent formulation, sample-average approximation, and
      Benders decomposition. Numerical studies are extensively performed in which the results clearly show that with the OCRP algorithm,
       cloud consumer can successfully minimize total cost of resource provisioning in cloud computing environments.


      Index Terms—Cloud computing, resource provisioning, virtualization, virtual machine placement, stochastic programming.
                              Ç


1  INTRODUCTION

    LOUD computing is a large-scale distributed computing   instances, cloud providers which offer IaaS services with
    paradigm in which a pool of computing resources is   both plans. In  general, pricing  in on-demand plan  isC
available to users (called cloud consumers) via the Internet  charged by pay-per-use  basis  (e.g., 1 day). Therefore,
[1]. Computing resources, e.g., processing power, storage,  purchasing  this on-demand  plan, the consumers can
software, and network bandwidth, are represented to cloud   dynamically provision resources at the moment when the
consumers as the accessible public utility services. Infra-   resources are needed to fit the fluctuated and unpredictable
structure-as-a-Service  (IaaS)  is a computational  service  demands. For reservation plan, pricing is charged by a one-
model widely applied in the cloud computing paradigm.   time  fee  (e.g., 1 year)  typically before the computing
In this model, virtualization technologies can be used to   resource will be utilized by cloud consumer. With the
provide resources to cloud consumers. The consumers can   reservation plan, the price to utilize resources is cheaper
specify the required software stack, e.g., operating systems   than that of the on-demand plan. In this way, the consumer
and  applications; then package them  all together  into  can reduce the cost of computing resource provisioning by
virtual machines (VMs). The hardware requirement  of   using the reservation plan. For example, the reservation
VMs can also be adjusted by the consumers. Finally, those  plan  offered by Amazon EC2 can reduce  the  total
VMs will be outsourced to host in computing environments   provisioning cost up to 49 percent when the reserved
operated by third-party sites owned by cloud providers. A   resource is fully utilized (i.e, steady-state usage) [4].
cloud provider is responsible for guaranteeing the Quality     With the reservation plan, the cloud consumers a priori
                                                             reserve the resources in advance. As a result, the under-of Services (QoS) for running the VMs. Since the computing
                                                                 provisioning problem can occur when the reserved resourcesresources are maintained by the provider, the total cost of
                                                             are unable to fully meet the demand due to its uncertainty.ownership to the consumers can be reduced.
                                                    Although this problem can be solved by provisioning more   In cloud computing, a resource provisioning mechanism
                                                            resources with on-demand plan to fit the extra demand, theis required to supply cloud consumers a set of computing
                                                        high cost will be incurred due to more expensive price ofresources for processing the jobs and storing the data. Cloud
                                                           resource provisioning with on-demand plan. On the otherproviders can offer cloud consumers two resource provi-
                                                       hand, the overprovisioning problem can occur if the reserved
sioning plans, namely short-term on-demand and long-term
                                                            resources are more than the actual demand in which part of
reservation plans. Amazon EC2 [2] and GoGrid [3] are, for
                                                        a resource pool will be underutilized. It is important for the
                                                        cloud consumer to minimize the  total cost of resource
.  The authors are with the School  of Computer Engineering, Nanyang   provisioning by reducing the on-demand  cost and  over-
   Technological University (NTU), Nanyang Avenue, Singapore 639798.     subscribed cost of underprovisioning and overprovisioning.
   E-mail: {siva0020, ebslee, dniyato}@ntu.edu.sg.                  To achieve  this  goal, the optimal computing resource
Manuscript received 3 Apr. 2010; revised 6 Sept. 2010; accepted 28 Jan. 2011;  management is the critical issue.
published online 7 Feb. 2011.                                         In this paper, minimizing both underprovisioning and
For information on obtaining reprints of this article, please send e-mail to:
tsc@computer.org and reference IEEECS Log Number TSCSI-2010-04-0030.   overprovisioning problems under the demand and price
Digital Object Identifier no. 10.1109/TSC.2011.7.                      uncertainty  in cloud computing environments  is our

                                                     1939-1374/12/$31.00   2012 IEEE     Published by the IEEE Computer Society

### Página PDF 2

CHAISIRI ET AL.: OPTIMIZATION OF RESOURCE PROVISIONING COST IN CLOUD COMPUTING                                               165

motivation to explore a resource provisioning strategy for  proposed in which extra demanded resources can be more
cloud consumers. In particular, an optimal cloud resource   efficiently provisioned. In [11], the concept of resource slot
provisioning (OCRP) algorithm is proposed to minimize the  was proposed. The objective is to address uncertainty of
total cost for provisioning resources in a certain time period.   resources availability. In [12], a binary integer program to
To make an optimal decision, the demand uncertainty from  maximize revenues and utilization of resource providers
cloud consumer side and price uncertainty from cloud  was formulated. However,  [9],  [10],  [11],  [12] did not
providers are taken into account to adjust the tradeoff   consider uncertainty of future consumer demands. In [13],
between on-demand and oversubscribed costs. This optimal  an optimization framework for resource provisioning was
                                                         developed. This framework considered multiple client QoSdecision is obtained by formulating and solving a stochastic
                                                                 classes under uncertainty of workloads (e.g., demands ofinteger programming problem with multistage recourse [5].
                                                    computing resources). The arrival pattern of workloads isBenders decomposition [6] and sample-average approxima-
                                                          estimated by using online forecasting techniques. In [14],tion [7] are also discussed as the possible techniques to
                                                                 heuristic method for service reservation was proposed.solve the OCRP algorithm. Extensive numerical studies and
                                                             Prediction of demand was performed to define reservationsimulations are performed, and the results show that OCRP
                                                                   prices. In [15], K-nearest-neighbors algorithm was applied
can minimize the total cost under uncertainty.
                                                                 to predict the demand of resources. In contrast, our work
  The major  contributions  of  this paper  lie  in the
                                                                  specifies that demands are given as probability distribu-
mathematical analysis which can be summarized as follows:
                                                                     tions. In addition, the price difference between reservation
   .   The optimal cloud resource provisioning algorithm  and on-demand plans was not taken into account in all
         is proposed for the virtual machine management.  works in the literature.
                                                As virtualization is a core technology of cloud computing,      The optimization formulation of stochastic integer
                                                            the problem of virtual machine placement (VM placement)      programming  is proposed to obtain the decision
                                                   becomes crucial [16], [17], [18], [19], [20]. In [16], the broker-       of the OCRP algorithm as such the total cost of
                                                      based architecture and algorithm for assigning VMs to       resource provisioning in cloud computing environ-
                                                            physical servers were developed. In [17], a resource manage-      ments  is minimized. The formulation considers
                                                 ment consisting of resource provisioning and VM placement       multiple provisioning stages with demand and price
                                                was proposed. In [18], techniques of VM placement and        uncertainties.
                                                             consolidation which leverage min-max and shares features   .   The solution methods based on Benders decomposi-
                                                      provided by hypervisors were explored. In [19], a dynamic       tion and sample-average approximation algorithms
                                                             consolidation mechanism based on constraint programming       are used to solve the optimization formulation in
                                                was developed. This consolidation mechanism was origin-      an efficient way.
                                                                    ally designed for homogeneous clusters. However, hetero-   .   The performance evaluation is performed which can
                                                            geneity which  is common in a multiple cloud provider
       reveal the importance of optimal computing  re-
                                                      environment was ignored. Moreover, [16], [17], [18], [19]
       source provisioning. The performance comparison
                                                       did not consider uncertainty of future demands and prices.
     among the OCRP algorithm and the other ap-
                                                             In [20], a dynamic VM placement was proposed. However,
       proaches is also presented.
                                                            the placement in  [20]  is heuristic-based which cannot
  The proposed mathematical analysis will be useful to the                                                         guarantee the optimal solution.
cloud consumers (e.g., organization and company) for the      Stochastic programming has been developed to solve
management  of  virtual machines  in cloud computing   resource planning under uncertainty [5] in various fields,
environment. The proposed OCRP algorithm will facilitate   e.g., production planning,  financial management, and
the adoption of cloud computing of the users as  it can   capacity planning. For example, in [21], the authors applied
reduce the cost of using computing resource significantly.    the  stochastic programming approach  for planning  of
  The rest of this paper is organized as follows: Related   electrical power generation and transmission line expansion
works are reviewed in Section 2. The system model and   while some uncertainties affecting to the planning are taken
assumption of cloud computing environment are described   into account. It is shown that stochastic programming is the
in Section  3. In Section  4, the stochastic programming  promising mathematical tool which is able to address the
formulation of the OCRP algorithm is presented. Section 5   optimal decision making in the stochastic environment.
presents the Benders decomposition algorithm. Section 6  However, to the best of our knowledge, the application of
presents the sampling-average approximation approach.   stochastic programming to computing resource provision-
Experiments and simulations to evaluate the performance   ing has never been exclusively studied.
of the OCRP algorithm are presented in Section 7. Finally,     The optimal virtual machine placement (OVMP) algorithm
conclusions are stated in Section 8.                     was proposed [22]. This OVMP algorithm can yield the
                                                         optimal solution for both resource provisioning and VM
                                                       placement in two provisioning stages. Motivated by this
2  RELATED WORK                                                         previous work, we introduce the OCRP algorithm in this
Available resource provisioning options were discussed in  paper which achieves many improvements.  First, the
[8]. The resource provisioning  strategies  in distributed  problem is generalized into the multiple stage formulation.
systems were addressed in [9], [10], [11], [12], [13], [14], [15].   Second, the different approaches to obtain the solution of
In [9], an architectural design of on-demand service for grid  computing resource provisioning are considered. Finally,
computing was proposed. In [10], a profile-based approach   the performance evaluation is extended to consider various
to capture expert’s knowledge of scaling applications was   realistic scenarios.

### Página PDF 3

166                                                    IEEE TRANSACTIONS ON SERVICES COMPUTING,  VOL. 5,  NO. 2,  APRIL-JUNE 2012


                                                         load balancer, to support the consumer’s hosting VM. Note
                                                                 that the key notations used in the paper are listed in Table 1.

                                                         3.2  Provisioning Plans
                                    A cloud provider can offer the consumer two provisioning
                                                             plans,  i.e.,  reservation and/or on-demand  plans. For
                                                           planning, the cloud broker considers the reservation plan
                                                            as medium- to long-term planning, since the plan has to be
                                                          subscribed in advance (e.g., 1 or 3 years [2]) and the plan
                                                       can significantly reduce the total provisioning cost [4]. In
                                                                  contrast, the broker considers the on-demand plan as short-
                                                      term planning, since the on-demand plan can be purchased
Fig. 1. System model of cloud computing environment.              anytime for short period of time (e.g., one week) when the
                                                            resources reserved by the reservation-plan are insufficient
3  SYSTEM MODEL AND ASSUMPTION                        (e.g., during peak load).
3.1  Cloud Computing Environment                    3.3  Provisioning Phases
As shown in Fig. 1, the system model of cloud computing  The cloud broker considers both reservation and on-
environment consists of four main components, namely  demand plans for provisioning resources. These resources
cloud consumer, virtual machine (VM) repository, cloud   are used in different time intervals, also called provisioning
providers, and cloud broker. The cloud consumer has   phases. There are three provisioning phases:  reservation,
demand to execute  jobs. Before the jobs are executed,   expending, and on-demand phases. As shown in Fig. 2, these
computing resources has to be provisioned from cloud   phases with their actions perform in different points of time
providers. To obtain such resources, the consumer firstly   (or events) as follows. First in the reservation phase, without
creates VMs integrated with software required by the  knowing the consumer’s actual demand, the cloud broker
jobs. The created VMs are stored in the VM repository.   provisions resources with reservation plan in advance. In
Then,  the VMs  can  be  hosted on  cloud  providers’   the expending phase, the price and demand are realized,
infrastructures whose resources can be  utilized by the  and the reserved resources can be utilized. As a result, the
VMs. In Fig. 1, the cloud broker is located in the cloud   reserved resources could be observed to be either over-
consumer’s site and is responsible on behalf of the cloud   provisioned or underprovisioned. If the demand exceeds
consumer for provision resources for hosting the VMs. In   the amount of reserved resources (i.e., underprovisioned),
addition, the broker can allocate the VMs originally stored   the broker can pay for additional resources with on-demand
in the VM repository to appropriate cloud providers. The   plan, and then the on-demand phase starts.
broker implements  the OCRP  algorithm  to make an                                                         3.4  Provisioning Stages
optimal decision of resource provisioning.
                                    A provisioning stage is the time epoch when the cloud   In OCRP, there are multiple VM classes used to classify
                                           1                        broker makes a decision to provision resources by purchas-
different types of VM. Let I   IN1  denote the set of VM
                                                           ing reservation and/or on-demand plans, and also allocates
classes. It is assumed that one VM class represents a distinct
                                        VMs  to cloud providers  for  utilizing the provisioned
type of jobs (e.g., one class for web application and the other
                                                               resources. Therefore, each provisioning stage can consist
for database application). A certain amount of resources is                                                               of one or more provisioning phases. The number  of
required for running the VM, and this required amount of                                                           provisioning stages is based on the number of planning
resources can be different for VM in different classes. With                                                       epoches considered by the cloud broker, e.g., a yearly plan
this resource requirement, the cloud broker can reserve                                                                consists of 12 provisioning stages (i.e., 12 months). Let T
computing resources from cloud providers to be used in the   IN1 denote the set of all provisioning stages where jT j    2.
future according to the actual demand. This demand can be   For resource provisioning under uncertainty, the broker is
determined as the number of created VMs. In this case, it is  assumed to be able to reserve the resources in the first
possible  that additional resources can be provisioned   provisioning stage. Also, the broker obtains a solution,
instantly from cloud providers if the reserved resources is   called recourse action [5], for provisioning resources against
not enough to accommodate the actual demand.             uncertainty parameters  (i.e., demand and price) in every
   Let J   IN1 denote the set of cloud providers. Each cloud   stage. These uncertainty parameters in each stage will be
provider supplies a pool of resources to the consumer. Let   observed by the broker after the resource reservation has
R denote the set of resource types which can be provided  been made. The observed uncertainty parameters are called
by cloud providers. Resource types can be computing   realization (e.g., the actual number of created VMs after the
power (in unit of CPU-hours), storage (in unit of GBs/   jobs are submitted by the consumers). Then, the broker will
month), and network bandwidth for Internet data transfer   take the recourse action according to the realization, e.g.,
(in unit of GBs/month). Each VM class specifies the amount   utilizing the reserved resource and/or provisioning more
of resources in each resource type. Let bir be the amount of   resource with on-demand plan.
resource type r required by the VM in class i 2 I.  It is      Fig. 3 shows the  relationship between provisioning
assumed that every cloud provider prepares facilities, e.g.,   phases and provisioning stages, where a yearly plan with
virtualization management software, network facility, and   12 provisioning  stages, namely T ¼ fT1; T2; . . . ; T12g,  is
                                                         considered.  Fig. 3a shows the example  of  all  three
    1. IN1 ¼ f1; 2; 3; . . .g.                                          provisioning phases existing in each stage. In Fig. 3b, each

### Página PDF 4

CHAISIRI ET AL.: OPTIMIZATION OF RESOURCE PROVISIONING COST IN CLOUD COMPUTING                                               167


                                          TABLE 1
                                                              List of Key Notations


stage may not  consist  of  all provisioning phases. For   reservation contract refers to the advance reservation of
example, the reservation phase is performed in T1 and the   resources with the specific time duration of usage. For
number of resources are reserved. From T1-T3, the expend-   example, the reservation plan offered by Amazon EC2 has
ing phase  starts  in some points  of time when some  two reservation contracts [2], namely 1-year contract and 3-
resources reserved in T1 are utilized. Then, the on-demand   year contract. The certain amount of resources are reserved
phase starts in T3 due to the insufficient reserved resources,   for 1 year in theone-year contract and 3 years in the three-year
and some resources are provisioned with on-demand plan.   contract starting from the time when they are provisioned.
In T4, the reservation phase starts again and so on.             Let K   IN1 denote the set of all reservation contracts
                                                   which are offered by cloud providers. Let Lk denote the
3.5  Reservation Contracts                            time duration (in unit of provisioning stages) specified in
A cloud provider can offer the consumer multiple reserva-   reservation contract k 2 K. Let T k denote the set of stages at
tion plans with  different reservation  contracts. Each  which the cloud broker can provision resources by contract
                                                                         k. Let F kt be the set of stages at which some resources
                                                          reserved by contract k could be utilized at stage  t 2 T .
                                                    Given the total number of stages jT j, both T k and F kt are
                                                         expressed as follows:

                                                                 T k ¼ f1; . . . ; jT j  Lk þ 1g;               ð1Þ

                                         F kt ¼ fmaxð1; t  Lk þ 1Þ; . . . ; minðt; jT j  Lk þ 1Þg:   ð2Þ
Fig. 2. Transition of provisioning phases.
                                                                In Fig. 4, the example of advance reservation for the
                                                            yearly plan with 3-month (K1) and 6-month (K2) reservation


Fig.  3. Relationship between provisioning phases and provisioning    Fig. 4. Example of advance reservations with 3-month (K1) and 6-month
stages.                                                              (K2) contracts.

### Página PDF 5

168                                                    IEEE TRANSACTIONS ON SERVICES COMPUTING,  VOL. 5,  NO. 2,  APRIL-JUNE 2012

contracts is shown (i.e., LK1 ¼ 3 and LK2 ¼ 6). The boxes  provided by cloud provider  j, respectively. Let  cðrÞijktð!Þ
above the timeline represent the time coverage of some  and cðeÞijktð!Þ, defined with the similar way as (4), denote the
reserved contracts. As shown in (1), T K1 ¼ fT1; T2; . . . ; T10g   reservation and expending costs for provisioning every
and T K2 ¼ fT1; T2; . . . ; T7g are the sets of stages at which   resource type, respectively.
resources can be provisioned by K1 and K2, respectively.      In on-demand phase, let cðoÞjrtð!Þ denote the unit price of
Contract K1 is subscribed three times (e.g., T7-T9), while   resource type r provided by cloud provider j in provision-
contract K2  is subscribed twice (e.g., T5-T10). Fig. 4 also   ing stage t given scenario !. Also, the price can be changed
shows that some stages can be covered by two (or more)  by cloud providers (i.e., uncertain to consumer when the
subscribed contracts, e.g., T1-T3 are covered by contracts K1   resource is reserved). Let cðoÞijt ð!Þ, defined with the similar
and K2. In Fig. 4, any set F kt in (2) can be obtained, e.g.,                                            way as (4), denote the on-demand cost for provisioning
F K1T4 ¼ fT2; T3; T4g, F K1T11 ¼ fT9; T10g, and F K2T12 ¼ fT7g.                                                         every resource type. Given VM class i, cloud provider j,
                                                           provisioning stage t, and scenario !, the expending cost of3.6  Uncertainty of Parameters
                                                   any reservation contract k is assumed to be cheaper than theThe optimal solution used by the cloud broker is obtained
                                                 on-demand cost (i.e., cðeÞijktð!Þ < cðoÞijt ð!Þ).from the OCRP algorithm based on  stochastic  integer
programming [5]. Stochastic programming takes a set of    From the system model and assumption, the optimal
                                                        cloud resource provisioning algorithm  is developed  touncertainty parameters (called scenarios), described by a
                                                     minimize the total provisioning costs under the price andprobability distribution into account. Let  denote the set of
                                              demand uncertainty in multiple provisioning stages. In theall scenarios in every provisioning stage and    t denote the
                                                           next section, the stochastic programming formulation of theset of all scenarios in provisioning stage t. Set    is defined
                                        OCRP algorithm is presented.as the Cartesian product of all    t, namely
      Y
         ¼          t ¼   1      2               jT j:           ð3Þ                                          4  STOCHASTIC PROGRAMMING MODEL
                      t2T
                                                             In this section, the stochastic programming with multistage
It is assumed that the probability distribution of   has finite                                                           recourse [5] is presented as the core formulation of the
support,  i.e., set   has a finite number of scenarios with                                        OCRP algorithm.  First, the  original form  of  stochastic
respective probabilities pð!Þ 2 ½0; 1 where ! is a composite                                                               integer programming formulation  is derived. Then, the
variable defined as ! ¼ ð!1; . . . ; !jT jÞ 2    . In this paper,                                                          formulation is transformed into the deterministic equivalent
demand and price are considered as scenarios in   whose                                                          formulation (DEF) which can be solved by  traditional
probability distribution  is assumed to be available. The                                                           optimization solver software.
actual scenario of uncertainty parameter after it is observed
by the broker is called realization.                          4.1  Stochastic Integer Programming for OCRP
                                                        Minimize:3.7  Provisioning Costs
With three aforementioned provisioning phases, there are  X X X                                                             z ¼              cðRÞijk xðRÞijk þ IE Q xðRÞijk ; !   ;                 ð5Þ
three corresponding provisioning costs incurred in these         i2I j2J k2K
phases, namely reservation, expending, and on-demand
                                                                subject to:costs. The main objective of the OCRP algorithm  is to
minimize all of these costs while the consumer’s demand is
                                                                     xðRÞijk 2 IN0;   8i 2 I; 8j 2 J ; 8k 2 K:                       ð6Þmet, given the uncertainty of demand and price.
   For cloud provider, the price is defined in dollars ($) per                                                  The general form of stochastic integer program of the
resource unit. Let cðRÞjkr denote the unit price (i.e., costs to the                                        OCRP algorithm is formulated in (5) and (6). The objective
consumer) of resource type r subscribed to reservation
                                                            function  (5)  is to minimize the cloud consumer’s  total
contract k provided by cloud provider j in reservation
                                                         provisioning  cost.  Decision  variable  xðRÞijk  denotes  thephase of the first provisioning stage. It is assumed that the
                                                number of VMs provisioned in the first provisioning stage.price of reservation plan in the first stage is charged by a
fixed one-time fee. The reservation cost cðRÞijk  is the cost for   In other words, this number refers to as the total amount of
                                                          reserved resources. The expected cost under the uncer-provisioning every resource type defined as follows:
                                                                 tainty     is defined as IE ½QðxðRÞijk ; !Þ where QðxðRÞijk ; !Þ is
         X
                          cðRÞijk ¼     bircðRÞjkr:                    ð4Þ   expressed as follows:
                            r2R
                                  Q xðRÞijk ; ! ¼       min       CðY Þ;  Y 2    xðRÞijk ; !  :  ð7Þ
The prices in reservation and expending phases could be                 Y ¼ðxðrÞijktð!Þ;xðeÞijktð!Þ;xðoÞijt ð!ÞÞ
adjusted by cloud providers without informing the con-
sumer in advance, except the price of the reservation plan in      In (7), the objective of QðxðRÞijk ; !Þ is to minimize the cost
the first provisioning stage. For instance, the cost of electric  under uncertainty given scenario ! and xðRÞijk . Such cost is
power to supply a cloud provider’s data center could be   represented by Cð Þ and defined in (9). Composite variable
increased by power plants in the next few months, and the  Y  representing  the  solution  of  QðxðRÞijk ; !Þ  consists  of
cloud provider  will be able  to increase the  costs  of   variables, namely  xðrÞijktð!Þ,  xðeÞijktð!Þ, and  xðoÞijt ð!Þ, which
computing resources in the future as well. For the prices   denote the numbers of VMs provisioned in reservation,
in provisioning stage t given scenario ! in both reservation  expending, and on-demand phases,  respectively.  Set
and expending phases, cðrÞjkrtð!Þ and cðeÞjkrtð!Þ denote the unit     ðxðRÞijk ; !Þ controls the relationship among the variables by
prices  of resource type  r with reservation  contract k   constraints as expressed in (8)-(15). The constraint in (10)

### Página PDF 6

CHAISIRI ET AL.: OPTIMIZATION OF RESOURCE PROVISIONING COST IN CLOUD COMPUTING                                               169


maintains the amount of resources utilized in expending   subject to:   (6)
phase to be less than or equal to the number of reserved    X
resources as stated in (2). In (11), the constraint implies that   xðeÞijktð!Þ       xðrÞijk^tð!Þ; 8i2I; 8j2J; 8k2K; 8t2T; 8!2   ; ð17Þ
the reservation in the first stage can be performed without                 ^t2F kt
any uncertainty. The constraint in (12) ensures that the
consumer’s demand for VM class i 2 I in stage t 2 T  is   xðRÞijk ¼ xðrÞijktð!Þ;  t ¼ 1; 8i2I; 8j2J ; 8k2K; 8!2   ;       ð18Þ
met. The constraint in (13) states that the allocation of
resources for VMs must not exceed the maximum resource               !
capacity offered by a cloud provider. Constraints (14) and X X                                                                                          xðeÞijktð!ÞþxðoÞijt ð!Þ    ditð!Þ; 8i2I; 8t2T; 8!2   ; ð19Þ
(15) indicate that variables take the values from a set of   j2J  k2K
nonnegative integer numbers (i.e., IN0).
                                                 !
          Q xðRÞijk ; ! ¼ min CðY Þ;                 ð8Þ Xbir X xðeÞijktð!ÞþxðoÞijt ð!Þ   ajrtð!Þ; 8j2J;8r2R;8t2T; 8!2   ;
                                                                             i2I    k2K
where
                                                                                                                       ð20Þ
  X X X X
CðY Þ ¼                      cðrÞijktð!ÞxðrÞijktð!Þ
          i2I j2J k2K t2T k                                                     xðrÞijktð!Þ2IN0;  8i2I; 8j2J ; 8k2K; 8t2T k; 8!2   ;      ð21Þ                               ! ð9Þ
   X X X X
    þ                       cðeÞijktð!ÞxðeÞijktð!Þ þ cðoÞijt ð!ÞxðoÞijt ð!Þ   ;
            i2I j2J t2T  k2K                                                xðeÞijktð!Þ2IN0;  8i2I; 8j2J ; 8k2K; 8t2T ; 8!2   ;      ð22Þ

subject to:
   X                                                             xðoÞijt ð!Þ2IN0;  8i2I; 8j2J ; 8t2T ; 8!2   :              ð23Þ
xðeÞijktð!Þ        xðrÞijk^tð!Þ; 8i2I; 8j2J; 8k2K; 8t2T;       ð10Þ
              ^t2F kt
                                          5  BENDERS DECOMPOSITION
xðRÞijk ¼ xðrÞijktð!Þ;  t ¼ 1; 8i2I; 8j2J; 8k2K;              ð11Þ   In this section, the Benders decomposition algorithm [6] is
                                                         applied  to solve the  stochastic programming problem
             !                                 formulated in Section 4. The goal of this algorithm is to
X X                                                 break down the optimization problem into multiple smaller
           xðeÞijktð!ÞþxðoÞijt ð!Þ   ditð!Þ; 8i2I; 8t2T ;        ð12Þ  problems which can be solved independently and paral-
 j2J  k2K
                                                                              lelly. As a result, the time to obtain the solution of the OCRP
              !                                  algorithm can be reduced. The Benders decomposition
X X                                                algorithm can decompose integer programming problems
     bir      xðeÞijktð!ÞþxðoÞijtð!Þ   ajrtð!Þ; 8j2J; 8r2R; 8t2T; ð13Þ  with complicating  variables  into two major problems:
 i2I    k2K                                                    master problem and subproblem.

                                                         Property 1. The DEF derived in (16)-(23) is the problem whose
xðrÞijktð!Þ2IN0; 8i2I; 8j2J ; 8k2K; 8t2T k;              ð14Þ      structure has multiple complicating variables.
                                                             Proof. Variables xðeÞijktð!Þ from the DEF defined in (16)-(23)
xðeÞijktð!Þ2IN0; xðoÞijt ð!Þ2IN0; 8i2I; 8j2J ; 8k2K; 8t2T :  ð15Þ     are considered as complicating  variables  [6]. Since
                                                                  variables xðeÞijktð!Þ exist in constraints (17), (19), and (20),
4.2  Deterministic Equivalent Formulation                 the variables prevent the decomposability of the DEF. If
Given a probability distribution of all scenarios in set     ,      variables xðeÞijktð!Þ are given the fixed values are denoted
the formulation in (5)-(15) can be transformed into the     by xðfixÞijkt ð!Þ, the DEF can be decomposed into two types of
deterministic  integer programming  called  deterministic     independent optimization subproblems, namely S1 and
equivalent formulation as expressed in (16)-(23). To solve     S2ð!Þ presented as follows:
this DEF,  probability  distributions  of both  price and      ½S1 Minimize:
demand must be available,  i.e., pð!Þ in  (16). Then, the   XX X
DEF can be solved by using traditional optimization solver        zðrÞ ¼            cðRÞijk xðRÞijk
software. For example, the formulation  is implemented             i2I j2J k2K
using MathProg script, and then the script is solved by    XX XX X                              ð24Þ                                         þ                   pð!ÞcðrÞijktð!ÞxðrÞijktð!Þ;
GNU Linear Programming Kit (GLPK) [23].                           !2  i2I j2J k2K t2T k
Minimize:
                                                                   subject to:   (6), (17), (18), (21)
  X XX   XXX X X
 ^z ¼             cðRÞijk xðRÞijk þ                   pð!ÞcðrÞijktð!ÞxðrÞijktð!Þ                                                                                   xðeÞijktð!Þ¼xðfixÞijkt ð!Þ; 8i2I; 8j2J; 8k2K; 8t2T; 8!2   ; ð25Þ       i2I j2J k2K          !2  i2I j2J k2K t2T k
                                 !
  XXX X  X                                    ½S2ð!Þ Minimize:
   þ             pð!Þ       cðeÞijktð!ÞxðeÞijktð!ÞþcðoÞijt ð!ÞxðoÞijt ð!Þ  ;
       !2  i2I j2J t2T       k2K              X X X                                                                                       zðoÞ ð!Þ ¼            pð!ÞcðoÞijt ð!ÞxðoÞijt ð!Þ;                ð26Þ
                                                        ð16Þ                  i2I j2J t2T

### Página PDF 7

170                                                    IEEE TRANSACTIONS ON SERVICES COMPUTING,  VOL. 5,  NO. 2,  APRIL-JUNE 2012


                                                    The objective function (28) is directly derived from that in
                                                                         (16). xðeÞijkt ð!Þ represents variable xðeÞijktð!Þ in iteration   of
                                                        master problem, while variable    provides the minimum
                                                                cost given reservation and on-demand costs. This    will be
                                                   improved in consequent iterations. Initially,   can be fixed
                                                   by constant   ðlbÞ as shown in constraint (29). This   ðlbÞ can be
                                                          estimated from an economical analysis or historical data of
                                                               prior solutions [6]. Constraints (30)-(32) define the boundary
                                                                of xðeÞijkt ð!Þ. After solving the master problem, the algorithm
                                                        proceeds to the Step-1.
                                                                       Step-1: Subproblem solution. In Step-1, multiple subpro-
                                                     blems are formulated and solved. Lets assign solution
                                                                               xðeÞijkt ð!Þ obtained from the master problem to variables

                                                                                                                              xðfixÞijkt ð!Þ:
                                                    Given  the  fixed  solution  xðfixÞijkt ð!Þ, two aforementioned
Fig. 5. Flowchart of Benders decomposition algorithm.
                                                     subproblems,  namely,  S1 and  S2ð!Þ can  be  solved
                                                              concurrently.
   subject to:   (19), (20), (23)
                                                    The subproblem S1 is presented in (24)-(25) in which the
    xðeÞijktð!Þ ¼ xðfixÞijkt ð!Þ; 8i2I; 8j2J ; 8k2K; 8t2T :      ð27Þ   objective functionðrÞ        is to minimize the reservation cost. Let
                                                              variable    ijkt ð!Þ denote the optimal solution of the dual
  From this decomposition, we conclude that the DEF has  problem of S1 in iteration   associated with constraint (25).
   the structure with multiple complicating variables.     tu  The solution of   ðrÞijkt ð!Þ will be used in Step-3.
                                                    The subproblem S2ð!Þ is presented in (26)-(27) in which  From Property 1, the problem can be solved by Benders
                                                            the objective function is to minimize the on-demand costdecomposition algorithm. The algorithm consists of steps
                                             when the realization is set to !. S2ð!Þ associates with the
which are performed iteratively. At each iteration, the master
                                                number of scenarios  j   j, and hence  j   j subproblems are
problem constituted by the complicating variables and
                                                            generated. Note that  j   j is the Cardinality of set     . Let
subproblems constituted by the other decision variables                    ðoÞ
                                                              variable    ijkt ð!Þ denote the optimal value of the dual
are solved, then lower and upper bounds are calculated. The                                                    problem of S2ð!Þ in iteration   associated with constraint
algorithm stops when optimal solution converges, i.e., the                                     ðoÞ                                                                         (27). The solution of   ijkt ð!Þ will be used in Step-3.
lower and upper bounds are satisfactorily close to each other.      Step-2: Convergence checking. In Step-2, the convergence of
   In  Fig.  5, the flowchart  of Benders decompostion                                                       lower and upper bounds of the solutions obtained from
algorithm is shown. The algorithm for solving OCRP is   master problem and subproblems is checked. Both bounds
presented in four steps (i.e., Step-0 to Step-3) as follows.     are adjusted in each iteration. The lower bound in iteration
   Step-0: Initialization of the master problem. In Step-0, the     denoted as  zðlbÞ can be obtained from the  objective
step is the initialization of the master problem. This Step-0   function of the master problem, i.e., zðlbÞ ¼ z ðeÞ . The upper
is performed only once, while Step-1  to Step-3  are  bound in iteration  denoted by zðubÞ can be obtained from
repeatable in the algorithm. Let    denote the  iteration
counter and  initially set  ¼ 1. The master problem as                                     ðeÞ                ðrÞ X   ðoÞ                                                                                             zðubÞ ¼ z     þ z  þ    z   ð!Þ:        ð33Þ
expressed  in  (28)-(32)  is an  alternative form  of the                                        !2
formulation DEF shown in (16)-(23).
                                                         Let   denote a small  tolerance value  to  verify  the
Minimize:
                                                       convergence of both lower and upper bounds. The Benders
   X X X X X                               decomposition algorithm stops when zðubÞ    zðlbÞ <   , which     zðeÞ ¼                     pð!ÞcðeÞijktð!ÞxðeÞijkt ð!Þ þ     ;    ð28Þ                                                means both bounds are acceptably close to each other and
          !2  i2I j2J t2T k2K
                                                            the optimal solution can be found in iteration   . Otherwise,
subject to:                                                  the algorithm proceeds to the next iteration in which Step-3
                                                                 will perform.
          ðlbÞ;                                               ð29Þ      Step-3: Master problem solution.

X                      X X X X X      ðrÞ             ðoÞ     xðeÞijkt ð!Þ   ditð!Þ; 8i2I; 8t2T ; 8!2   ;              ð30Þ                                                      ijkt ð!Þ þ   ijkt ð!Þ
 j2J                                                                      !2  i2I j2J k2K t2T
                                                                                             xðeÞijkt ð!Þ   xðeÞijkt ð!Þ                           ð34ÞX X
         birxðeÞijktð!Þ   ajrtð!Þ; 8j2J ; 8r2R; 8t2T ; 8!2   ; ð31Þ                            ðrÞ X   ðoÞ
 i2I k2K                                      þ z  þ    z   ð!Þ;   2 f1; . . . ;     1g:
                                                                                  !2
xðeÞijkt ð!Þ2IN0; 8i2I; 8j2J ; 8k2K; 8t2T ; 8!2   ;      ð32Þ     Let the  iteration counter be increased by     þ 1.
                                                        Then, the master problem in (28)-(32) can be further relaxed

### Página PDF 8

CHAISIRI ET AL.: OPTIMIZATION OF RESOURCE PROVISIONING COST IN CLOUD COMPUTING                                               171

by additional constraints called Benders cuts [6]. In addition,    xðrÞijktð!nÞ2IN0; 8i2I; 8j2J ; 8k2K; 8t2T k; 8n2N ;     ð40Þ
the solution of the master problem will adjust the cost
and  also the expending  cost according  to  solution  of   xðeÞijktð!nÞ;xðoÞijt ð!nÞ2IN0; 8i2I;8j2J;8k2K;8t2T;8n2N:ð41ÞxðeÞijkt ð!Þ. As shown in (34), the Benders cuts are constructed
from the optimal costs obtained from master problem and
subproblems  in the  prior  iterations. After solving  this              1 XN
                                                                    ^Q xðRÞijk ; N ¼                                            Q xðRÞijk ; !n  :                          ð42Þmaster problem, Step-1 is repeated and the same iterative                                          N                                                                                n¼1
process continues.
                                                              Let z and x denote the optimal objective function value
                                                 and optimal solution of the original formulation (defined in
6  SAMPLE-AVERAGE APPROXIMATION
                                                                        (5) and (6)), respectively. Let ^zN and ^xN denote the optimal
In the case that the number of scenarios is numerous,  it   objective function value and optimal solution of the AP
may not be efficient to obtain the solution of the OCRP   formulation, respectively. Note that although  ^zN becomes
algorithm by solving the stochastic programming formula-   closer to z  when N  is large, value  ^zN naturally varies
tion defined in (16)-(23) directly  if  all scenarios in the   according to set of samples   N. Therefore, an estimation
problem are considered. To address this complexity issue,  method is required to achieve the SAA lower and upper
the sample-average approximation (SAA) approach  is  bounds of the optimal solution. Obviously,  ^zN forms the
applied [7]. This approach selects a set of scenarios, e.g.,  SAA upper bound of z  as follows:
N scenarios, where N is smaller than the total number of
scenarios  j   j. Then, these N scenarios can be solved in a                            z      ^zN:                      ð43Þ
deterministic equivalent formulation. The optimal solution
                                                                In addition, the SAA lower bound of z  is formed by the
can be obtained if N is large enough which can be verified
                                                           following unbiased propertynumerically.
   In  this  section,  the SAA approach  is applied  to                                    IE½^zN    z :                    ð44Þ
approximate the expected cost in every considered provi-
sioning stage,  i.e., QðxðRÞijk ; !Þ in  (7). A sampling method     For the properties in (43) and (44), bounding method is
                                                          required to obtain the estimates of both SAA upper and(e.g., Monte Carlo [24] and Latin hypercube [25]), is used to
generate scenarios  N ¼ f!1; . . . ; !Ng, where N denotes the  lower bounds on z with a certain confidence interval. The
                                                           next two following sections present the estimation of thesample size. Let N ¼ f1; . . . ; Ng be the set of indices of
                                        SAA bounds by applying the similar method to that in [7],samples. Then, the expected  cost can be redefined as
                                                                         [21], [24].shown in (42).
  The function  ^QðxðRÞijk ; NÞ  is the SAA to the objective   6.1 SAA Lower Bound Estimates
function in (5). Then, the problem can be transformed into a
                                                  The expected value IE½^zN  can be estimated by generating
deterministic equivalent formulation, as called approxima-                             M  independent  batches,2 each  of  size N, denoted  as
tion problem (AP) formulation, as expressed in (35)-(41).
                                                                   !1;m; . . . ; !N;m where m 2 f1; . . . ; Mg, then solving the AP
Minimize:
                                                            formulation. Let  ^zN;m denote the solution given batch m.
  XX X         1 X XXX X                  Next, the SAA lower bound can be obtained from
 ^zN ¼            cðRÞijk xðRÞijk þ                            cðrÞijktð!nÞxðrÞijktð!nÞ             N       i2I j2J k2K                         n2N i2I j2J k2K t2T k                                           1 XM                                  !                  LN;M ¼            ^zN;m:                ð45Þ       1 X X XX X                                                                                   m¼1   þ                                      cðeÞijkð!nÞxðeÞijktð!nÞþcðoÞijt ð!nÞxðoÞijt ð!nÞ              M    N
         n2N i2I j2J t2T  k2K                          Due to (44), this LN;M is an unbiased estimator of the mean
                                                        ð35Þ    IE½^zN which forms a statistical lower bound for z  . When
                                                            the generated M batches are independent and identicallysubject to:   (6)
                                                             distributed  (i.i.d.) by the Central Limit Theorem, the
   X
xðeÞijktð!nÞ        xðrÞijk^t; 8i2I; 8j2J; 8k2K; 8t2T; 8n2N;  ð36Þ   distribution of SAA lower2 bound estimate converges to a               ^t2F kt                                         normal distribution N ð0;  LÞ,3 namely
                                     pﬃﬃﬃﬃﬃ             D          2
                                M ðLN;M    IE½^zN Þ ! N ð0;  LÞ; as M ! 1;      ð46ÞxðRÞijk ¼xðrÞijktð!nÞ;  t¼1; 8i2I; 8j2J; 8k2K; 8n2N;      ð37Þ
                                                  where   2L ¼ Var½^zN 4 which can be approximated by the
               !                             sample variance estimator s2LðMÞ as follows:
X X
           xðeÞijktð!nÞ þ xðoÞijt ð!nÞ    ditð!nÞ; 8i2I; 8t2T; 8n2N;                     M
 j2J  k2K                                                                      1 X                                                                                   s2LðMÞ ¼               ð^zN;m   LN;MÞ2:         ð47Þ                                       M   1                                                        ð38Þ                            m¼1
               !                                     Finally, the ð1    Þ-confidence interval of the SAA lower
X X                                        bound can be defined as
    bir      xðeÞijktð!nÞþxðoÞijt ð!nÞ   ajrtð!nÞ;
i2I    k2K                                              ð39Þ
                                                                                                  2. A batch is a set of samples generated by a sampling technique.
                       8j2J; 8r2R;8t2T;8n2N ;               3. N ð0;  2LÞ denotes the normal distribution with mean 0 and variance  2L.
                                                                                                  4. Var½^zN denotes the variance of samples.

### Página PDF 9

172                                                    IEEE TRANSACTIONS ON SERVICES COMPUTING,  VOL. 5,  NO. 2,  APRIL-JUNE 2012

                   z =2sLðMÞ         z =2sLðMÞ
         LN;M   pﬃﬃﬃﬃﬃ     ; LN;M þ  p ﬃﬃﬃﬃﬃ       ;      ð48Þ  7  PERFORMANCE EVALUATION           M        M
                                                             In this section, the performance evaluation of the proposed
 where z  satisfies ProbfNð0; 1Þ   z g ¼ 1       . Note that the  OCRP algorithm  is  presented. Two  case  studies  are
 value z =2 from the Z-distribution can be replaced by critical   considered in this evaluation, namely two provisioning stage
 value t =2;M  1 from the Student’s t-distribution if M is small.   problem (2-PSP) and 12 provisioning stage problem (12-PSP).
                                                  The former, 2-PSP, has only two provisioning stages. We
 6.2 SAA Upper Bound Estimates                   assume that the cloud broker  is making a decision for
As shown in (43), ^zN forms the SAA upper bound of z  . By   provisioning resources at the end of year. Under price and
 selecting a solution ^xN obtained by solving the AP formula-  demand  uncertainty,  the cloud  broker performs  the
 tion, the SAA upper bound can be estimated by using the  advance reservation of resources in the  first stage  for
 unbiased estimator of ^zN. To achieve this estimator, we can   being used in the next whole year which is the second
 generate M~ independent batches, each of size ~N, denoted as   stage. Therefore, the 1-year reservation contract  is suffi-
 !1;m; . . . ; !N;m~  where m 2 f1; . . . ; Mg.~   Since solution  ^xN  is   ciently required by the broker since the contract can cover
 already fixed to the SAA problem,  i.e., ^zNð^xNÞ, given N~   the time duration. At the second stage, the price and
                                              demand  are observed. Then,  the number  of reserved samples of each generated batch, the objective function (35)
 can be decomposed into N~ independent subproblems in   resources are  utilized and some additional amount  of
                                                            resources can be provisioned in an on-demand fashion.
 which each of them can be solved independently and in
                                                           For 12-PSP, we consider 12 months in a year and hence
 parallel. Thus, these subproblems can be solved more
                                                             the stage is defined as T ¼ fT1; T2; . . . ; T12g. In each stage, efficiently than the original AP formulation. After  all
                                                             the cloud broker can perform an advance reservation of
 subproblems are solved, each batch yields the solution
                                                            resources for being used in the next incoming months
 denoted as  ^zN;mð^x~    NÞ. Then, the SAA upper bound can be
                                                          within these 12 months. Moreover, additional resources can
 estimated from
                                                      be provisioned by purchasing on-demand plans  if the
                     M~                           reserved resources cannot meet the actual demand. For both                          1 X
           U~N; Mð^x~  NÞ ¼            ^z~N;mð^xNÞ:            ð49Þ   case studies, the optimal solution obtained from the OCRP
             M~ m¼1                          algorithm is the amount of reserved resources in different
                                                            provisioning stages (or the first stage for 2-PSP). Since the   Again, the distribution of SAA upper bound estimate
                                                           2            amount of resources is reserved for the number of VMs, this
 converges  to a normal  distribution N ð0;  Uð^xNÞÞ given
                                                         optimal solution can be considered to the number of reserved
 solution ^xN, namely
                                         VMs in other words.
 p ﬃﬃﬃﬃﬃ
  M~ UN;~ Mð^x~  NÞ   ^zNð^xNÞ !D N  0;  2Uð^xNÞ  ; as M~ !1;  ð50Þ   7.1  Experiment Setup
 where   2Uð^xNÞ ¼ Var½^zNð^xNÞ which can be approximated   7.1.1  Setting of Cloud Computing Environment
 by the sample variance estimator s2Uð M;~  ^xNÞ as follows:    We first present the parameter setting of a cloud computing
                                                      environment used in  this performance evaluation. The
                                                      environment                                                                               consists                                                                                        of only                                                                                one cloud                                                                                        consumer                                                                                                                                                                           (i.e.,                  1        XM~
     s2UðM;~  ^xNÞ ¼                                        ð^zN;mð^x~    NÞ  UN;~ Mð^x~   NÞÞ2:    ð51Þ                                                              organization) who                                                                                                     is renting                                                                            computing                                                                                                  resources                                                                                                               offered                                                                                                 by        M~                    1 m¼1
                                                        cloud providers. The consumer has two different types of
 Finally, the ð1    Þ-confidence interval of the SAA upper   applications representing two distinct VM classes, namely
bound can be obtained from                            I ¼ fI1; I2g. For instance, I1 is a database server and I2 is a
"                                         #      web server. Each VM class requires different amount of
             z =2sUðM;^x~  NÞ             z =2sUðM;^x~  NÞ         resources. Processing time units required by a VM in classes
                                                                                           : ð52Þ UN;~ Mð^x~  NÞ   p ﬃﬃﬃﬃﬃ                                             ; UN;~ Mð^x~  NÞ þ  p ﬃﬃﬃﬃﬃ                                                                       I1 and  I2 are 8,748 and 6,570 CPU-hours per year,         M~                      M~
                                                                 respectively. Permanent storage capacities required by a
 6.3  Monte Carlo Sampling                 VM in classes I1 and I2 are 1,920 and 1,200 GBs per year,
 The Monte Carlo sampling technique can be applied to   respectively. Network bandwidth regarding outbound data-
 generate scenarios  N. Each scenario is from   as follows.   transfer required by a VM in classes I1 and I2 are 24,000 and
 First, the random number is uniformly selected from ½0; 1 .   30,000 GBs per year, respectively. The cost of inbound data
 Then, the scenario is derived by the inverse transformation   transfer is assumed to be free of charge. Furthermore, a
 method given the random number and cumulative prob-   software package is needed to be installed in a VM of each
 ability distribution of     . The same process is iteratively  VM class. A software package consists of operating system,
 performed until the N scenarios are completely chosen.     database software  (for class  I1  only), web application
                                                           software (for class I2 only), and other utility software. The
 6.4  Obtaining the Optimal Solution                    software cost is additionally charged to the consumer as the
 The optimal solution based on the SAA approach can be   license cost per a running VM. The license software costs
 obtained when N  is sufficiently large. However, we can   corresponding to a VM in classes I1 and I2 are $500 and
 select an optimal  solution by solving  different SAA   $1,200, respectively. The consumer is assumed to purchase
 problems with different size of N. Until the same solution   these software licenses from software vendors when VMs are
 is found in these problems, we can choose the solution as  running in expending and on-demand phases.
 the desired solution. The detail and result of this solution    The environment  consists  of four cloud providers,
 method is presented in the next section.                  namely J ¼ fJ1; J2; J3; J4g. J1 represents the private cloud

### Página PDF 10

CHAISIRI ET AL.: OPTIMIZATION OF RESOURCE PROVISIONING COST IN CLOUD COMPUTING                                               173


                                          TABLE 2
                                              Pricing Defined by Each Cloud Provider


and the other represent the three public clouds. The private  phase of all resource types can be doubly increased, with
cloud J1 is the data center belonging to the cloud consumer.   probability 0.1, from the price defined in Table 2. With
This data center has housed only 10 physical servers. Each   probability 0.9, the price in the on-demand phase remains
server  is assumed to  offer 100 percent uptime system  unchanged. For the demand uncertainty, the actual re-
availability,  i.e., 24  365 ¼ 8;760 CPU-hours per  year.   quired number of VMs in the second provisioning stage of
Therefore, for the whole data center, J1 can offer 87,600  VM class (i.e., I1 and I2) varies from 1 to 50. The demand of
CPU-hours as the maximum processing capacity. The other  one VM class is assumed to be the same as the other class.
resource types in J1 is assumed to be abundant to serve all  Three  distributions  of demand are considered  in the
VMs run by the consumer. The total cost to utilize the   experiment, namely discrete normal distribution, uniform
servers in J1 is only considered from the annual energy cost.   distribution, and distribution from test data. Means of both
This annual cost is assumed to be the average energy cost  normal and uniform distributions are set to 25.50. The
taken by Dell PowerEdge M600 blade server as presented in   variance  of normal  distribution  is  set  to  6, while the
[26]. The  cost  is calculated as  454:39=1;000 kilowatts   variance  of uniform  distribution  is  208.25. The  last
(average power consumption per server5)   $0:0897 (elec-   distribution  is generated from the logged data obtained
tric charge per watt-hour)  24 (hours per day)   365 (days  from Institute of High Performance Computing (IHPC) in
per year)   $357 per server per year. For only J1, this cost   Singapore. The data are collected from the actual usage of
($357)  is considered as the reservation cost to reserve   shared computing resources located in the computer cluster
resources for a VM, while the expending cost of processing   maintained by IHPC. The probability distribution (with
time and storage capacity are omitted. Only the cost of  mean = 21.64 and variance = 389.93) of the resource usage
network bandwidth is charged to $0.10 per GB per month of   representing the number of required VMs is derived as
outbound data transfer. Furthermore, the on-demand plan  shown in Fig. 6.
for provisioning resources is unavailable in J1.
                                                         7.2  Case Study: Two Provisioning Stage Problem  The public cloud providers (J2, J3, and J4) are assumed
to offer unlimited capacity of all resource types, so the   7.2.1  Cost Structure
constraint in (13) is omitted. Pricing of resources in provider   First, the cost structure to provision resources is studied. To
J2  is based on the prices defined by Amazon EC2 (in   ease the illustration, this study considers only single VM
February 2010), and the price of processing time is based on   class  I1 and single cloud provider  J2. The number of
that of the Small Instance type  [2]. However, pricing in   required VMs (i.e., demand) is varied following the normal
providers J3 and J4 is artificially and reasonably defined.   distribution. In Fig. 7, given different number of reserved
Providers J2 and J3 offer customers both reservation and  VMs, cost in the first stage called first stage cost (which is
on-demand plans, while J4 has only an on-demand plan.   actually reservation cost), cost in the second stage called
Providers  J2 and  J3  offer customers  three  different   second stage cost including expending and on-demand costs,
reservation  contracts, namely 3-month (3M), 6-month                                                 and total cost, are presented. As expected, the first stage
(6M), and 1-year (1Y) contracts. Pricing of resource in                                                                cost increases, as the number of reserved VMs increases.
expending and on-demand phases is charged as the pay-                                                   However, the second stage cost decreases after the demand
per-use basis based on the actual usage per resource unit.                                                                              is realized, since the cloud consumer needs smaller number
The resource unit of processing time is CPU-hour, while                                                                of VMs provisioned by on-demand plan. In this case, the
one of storage capacity and network bandwidth is GBs per
month. For the network bandwidth, only the outbound data
transfer is charged, while the inbound one is free of charge
in every cloud provider.6 Pricing defined by every cloud
provider is listed in Table 2.

7.1.2  Uncertainty Parameters
In this part, two main uncertainty parameters including the
price of resource and the demand as the number of required
VMs per VM class, are defined. The price in the on-demand


    5. We omit the power consumption of cooling system as it is the fixed
cost of private cloud in the organization.
    6. The charge of inbound data transfer offered by Amazon EC2 has been
free through June 30, 2010.                                                    Fig. 6. The probability distribution of the real data.

### Página PDF 11

174                                                    IEEE TRANSACTIONS ON SERVICES COMPUTING,  VOL. 5,  NO. 2,  APRIL-JUNE 2012


                                                                                Fig. 8. Comparison between total costs of resource provision with and
Fig. 7. The optimal solution in a simple cloud computing environment.    without reservation.

                                                         provisioned  in the  first stage  is presented. Also, theoptimal number of reserved VMs can be determined to be
                                                        expected second stage  costs incurred due  to  different30 reserved VMs as shown in Fig. 7, which is the point that
                                                               probability distributions are shown. The costs include thethe total cost is minimum. Clearly, even in this small setting
                                                              reservation cost (R.C.), expending cost (E.C.), on-demand(one VM class and one provider), the optimal solution is not
                                                                cost (O.C.), oversubscribed cost (O.S.C.), and total cost. The
trivial to obtain due to the demand uncertainty. Therefore,
                                                           probability  distributions include normal  distribution
the OCRP algorithm would be required to guarantee the
                                                       (Norm), uniform distribution (Uniform), and distribution
minimum cost to the consumer.                                                    from test data. Furthermore, three variances of the normal
   Given the optimal reservation of 30 VMs as shown in
                                                                distribution are considered, namely variance = 4 (Norm v4),
Fig. 7, the comparison between resource provisioning with
                                                        6 (Norm v6), and 8 (Norm v8).
and without reservation can be made as illustrated in                                                                In Table 3, we observe that as the variance increases the
Fig.  8. Without reservation, the number of VMs  is to                                                number of VMs also needs to be increased. Therefore, the
dynamically provision resources in the second stage by                                                number of reserved VMs in the test data is highest, while
only purchasing resources in the on-demand plan. Given                                                                 that in Norm v4 is lowest. Larger variance increases the
different demands (or realization of required number of                                                       chance that the demand will be smaller or larger than the
VMs) from 1 to 50, the cost in resource provision with                                                    mean. Consequently, Norm v8 incurs more total cost and
reservation becomes cheaper than that without reservation                                                             reserves more VMs than those in Norm v4 and Norm v6.
due to the discounted price of processing time. However,                                                         Again, the increment of number of reserved VMs can
the cost with reservation may not always be the cheapest.                                                        ensure that the on-demand cost can be minimized.
As shown in Fig. 8, the total cost in the resource provision
without reservation is lower than the other one until the   7.2.3 Comparison with Other Provisioning Algorithms
demand  is 15 in which the effective reservation begins.                                                          Next, the comparison between provisioning algorithms is
This fact indicates that even if the solution is optimal,  it                                                        performed. The algorithms include the proposed OCRP,
cannot guarantee the best solution in  all realizations of
                                                          expected-value of uncertainty provisioning (EVU), max-
observed parameters. Therefore, the effective way to tackle
                                          imum advance reservation provisioning (MaxRes), and
the uncertainty is not to search for the best solution for
                                                          nonreservation provisioning (NoRes) algorithms. EVU uses
every possible situation happening in the future, but to
                                                            the average values of uncertainty parameters and solves
obtain the solution which is able to minimize the tradeoff
                                                them by a  traditional deterministic program. MaxResbetween advance reservation and on-demand provision
                                                             reserves the maximum number of available VMs, whilewhile the uncertainty is carefully considered.
                                               NoRes does not reserve any resources. Both MaxRes and
7.2.2  Impact of Probability Distributions               NoRes also apply the traditional deterministic program for
For the next experiments,  all parameters of the cloud   allocating VMs to cloud providers. All algorithms with the
computing environment are applied. The  deterministic   defined input parameters are coded and solved by GLPK.
equivalent formulation derived in Section 4.2 is implemen-  The given distributions are applied to the possible scenarios
ted and solved by GLPK.                                     of demand and price, respectively. The solution obtained
  The stochastic effect of demand under different prob-  from each solved algorithm yields the number of reserved
ability distributions is investigated. In Table 3, the number  VMs (N.R.) and the allocation of VMs to providers. Then, a
of reserved VMs  (indicated as  label N.R.  in Table  3)   simulation program is developed to evaluate the solution of


                                          TABLE 3
                    Number of Reserved VMs and Costs Given Different Probability Distributions

### Página PDF 12

CHAISIRI ET AL.: OPTIMIZATION OF RESOURCE PROVISIONING COST IN CLOUD COMPUTING                                               175


                                          TABLE 4
            Number of Reserved VMs and Average Costs Given Different Resource Provisioning Algorithms


each algorithm. The simulation contains 1,000 iterations. In  However, solving the master problem requires substantial
each iteration, the random number is uniformly selected  amount of time since more Benders cuts have to be added.
from  ½0; 1 . Next, the scenario is derived by the inverse
                                                         7.3  Case Study: Twelve Provisioning Stagetransformation method given the random number and
                                                  Problemcumulative probability distributions of the scenarios. The
provisioning costs incurred by purchasing the provisioning  The SAA approach presented in Section 6 is studied. In this
plans given by the solution of each algorithm are recorded.   12-PSP, only provider J2 and J3  are considered.  It  is
After finishing the last iteration, the simulation calculates  assumed that the resource price is stable and the demand
the average costs as presented in Table 4. The costs include   varies within set f10; 20; 30; 40; 50g  (i.e., 512 ¼ 244;140;625
reservation cost (R.C.), expending cost (E.C.), on-demand   scenarios for the 12 stages). For sampling data, four sample
cost (O.C.), oversubscribed cost (OS.C.), and total cost.       sizes  are determined, namely N 2 f200; 500; 600; 750g.
   In Table 4, the proposed OCRP achieves the lowest total  Then, the Monte Carlo sampling technique generates
cost, while NoRes yields the highest total cost due to the  demand realizations for five batches per each size,  i.e.,
highest on-demand  cost. The OCRP algorithm reserves M ¼ 5. Lower bound estimate  of each sample  size  is
59 VMs (including both  classes  I1 and  I2). Although                                                              calculated by solving five SAA problems with respective
MaxRes reserves 100 VMs (50 per VM class) to entirely                                                               batches. For upper bound estimate, the solution obtained
avoid the higher cost in the on-demand plan, it still incurs
                                                    from each solved SAA problem is fixed to another new
much higher cost than that of OCRP. Additionally, MaxRes
                                        SAA problem whose sample size is 750, i.e., ~N ¼ 750. Tenincurs the highest oversubscribed cost since the reserved
                                                           batches of the new SAA problem are constructed andresources are unnecessarily overprovisioned. EVU incurs
the  total cost lower than those of MaxRes and NoRes   solved, i.e., M~ ¼ 10. Then, the solutions obtained from the
algorithms. Although the oversubscribed cost of OCRP is   ten batches can be calculated as the upper bound estimate.
higher than that of EVU, the on-demand cost of the OCRP      In Table 5, the estimates of SAA lower and upper bounds
algorithm is much lower. Again, it is possible that the on-   are presented. The optimal solution is found in the sample
demand cost can increase due to the price uncertainty. As a   size of 750. From this optimal solution, advance reserva-
result, the diminution of the on-demand  cost  is more   tions with only the 6-month reservation contract are used in
important. The result of this experiment shows the balance   only T1 and T7. That is, 10 VMs will be reserved to provider
between the number  of provisioning resources  to be                                                              J2 in stages T1 and T7 each and 30 VMs will be reserved to
acquired in the first and second stages in which OCRP
can provide the most optimal tradeoff.
                                                                 TABLE 5
7.2.4 Bender Decomposition                                   Estimation of Lower and Upper Bounds of Provisioning
Fig. 9 shows the bound convergence obtained by solving           Costs in the 12 Provisioning Stage Problem
Bender decomposition algorithm. The adjustment of lower
and upper bounds  is performed in each  iteration. At
iteration ¼ 42, algorithm converges. The optimal solution
obtained from the decomposition  is the same as one
obtained by solving DEF without decomposition. We
observe that the subproblems can be solved efficiently due
to their smaller number of variables and parallelization.


Fig. 9. Convergence of the upper and lower bounds by applying the
Benders decomposition.

### Página PDF 13

176                                                    IEEE TRANSACTIONS ON SERVICES COMPUTING,  VOL. 5,  NO. 2,  APRIL-JUNE 2012

provider J3 in stages T1 and T7 each. We conclude that 40         with deterministic equivalent formulation directly.
reserved VMs are only needed in stages T1 and T7 each. This         In  contrast, the approximation algorithm with
solution can avoid the higher on-demand cost, since only 10          estimation of SAA lower and upper bounds can
more VMs could be provisioned with on-demand plan in          yield tolerably solutions while the problems can be
any provisioning stages.                                               practically solved in timely manner.
                                                                            4.   Limitation of stochastic programming. Stochastic pro-
7.4  Discussion                                                     gramming does not address the method to obtain
7.4.1  Experimental Results                                     appropriate probability distributions describing un-
                                                                        certainty  (i.e., distributions of scenarios    ). How-
    1.   Balance of costs. We observe that the cloud broker          ever, this limitation can be alleviated by applying
      with OCRP will minimize on-demand cost rather         variance reduction techniques  (e.g., importance
       than the oversubscribed cost. Since resource pricing                                                           sampling  [27])  to  increase the precision  of the
       in  the on-demand plan  is higher and  possibly                                                                    estimates of uncertainty.
       increased by cloud providers, the reservation plan
         is more attractive by the cloud broker. However,   7.4.3  Future Research Direction
       reserving too many VMs may not be optimal (e.g.,                                                        For the future work, scenario reduction techniques [28] will
       as that of MaxRes from Table  4). Therefore, the                                                      be applied to reduce the number of scenarios. In addition,
       tradeoff between on-demand and oversubscribed                                                            the optimal pricing scheme  for cloud providers with
        costs needs to be adjusted in which OCRP can                                                            the consideration of competition in the market will be
       optimally perform.                                                                investigated.
    2.   Virtual machine outsourcing. As presented in Sec-
       tion 7.2, the VM outsourcing from a private cloud to
      a public cloud provider (or public cloud) shows  8  CONCLUSION
        interesting  result. In the experiment, the private                                                             In this paper, we have proposed an optimal cloud resource
       cloud fully utilizes its own resources. Then, extra
                                                          provisioning (OCRP) algorithm  to provision resources
     VMs can be spilled over to public clouds. Purchasing
                                                             offered by multiple cloud providers. The optimal solution
      and deploying new hardware to a private cloud may
                                                         obtained from OCRP  is obtained by formulating and       not be an optimal solution, since the total cost of
                                                            solving stochastic integer programming with multistage      ownership (TCO) must be considered. To reduce this
                                                              recourse. We have also applied Benders decomposition      TCO, workload outsourcing is the attractive choice
                                                     approach to divide an OCRP problem into subproblems      which is shown from our evaluation.
                                                   which can be solved  parallelly. Furthermore, we have
7.4.2  Implementation Issues                             applied the SAA approach for solving the OCRP problem
                                                       with a large  set of  scenarios. The SAA approach can
    1.   Multiple provisioning stages planning issue. As shown   effectively achieve an estimated optimal solution even the
       in Section 7.3, the OCRP algorithm can be applied to  problem size is greatly large. The performance evaluation
       multiple provisioning stages representing long-term   of the OCRP algorithm has been performed by numerical
       planning. Since the optimal solution of the  first   studies and simulations. From the results, the algorithm can
       provisioning stage depends on multiple probability                                                         optimally  adjust  the  tradeoff between  reservation  of
       distributions describing the uncertainty occurring in                                                            resources and  allocation  of on-demand  resources. The
      consequent time epochs, multiple stages planning is                                        OCRP algorithm can be used as a resource provisioning
      needed. For example, the workload of some online                                                                  tool for the emerging cloud computing market in which the
       souvenir shopping websites could be dramatically
                                                                  tool can effectively save the total cost.
       increased in the high-season consisting of many time
       periods in a year (e.g., Christmas Day, Valentine’s
      Day, etc.). As a result, the websites should provision  ACKNOWLEDGMENTS
       resources by considering multiple time epochs (i.e.,
                                                         This work was done  in the  Parallel and Distributed
       provisioning stages) in advance, while reservation
                                                 Computing Centre (PDCC) of the School of Computer       contracts offered by cloud providers can be taken
                                                           Engineering, Nanyang Technological University, Singapore.       into account to reduce the provisioning cost.
                                                          This work was supported by the projects “User and Domain    2.  Use of decomposition method. The use of decomposi-
                                                      Driven Data Analytics” and “Design and Analysis of Cloud       tion method for OCRP has to be carefully consid-
                                                 Computing  for Data Value Chain: Operation Research       ered, since the formulation of the OCRP algorithm is
                                                      Approach,” granted by the A*STAR Thematic Strategic      a pure  integer program which  is the NP-hard
                                                        Research Programme.      problem  [5]. Although the subproblems can be
       solved in  parallel, the master problem with the
       additional Benders cuts requires considerable com-  REFERENCES
       putational time. The performance improvement of                                                                                     [1]    I. Foster, Y. Zhao, and  S. Lu, “Cloud Computing and Grid
       the decomposition algorithm will be considered in       Computing 360-Degree Compared,” Proc. Grid Computing Envir-
       the future work.                                              onments Workshop (GCE ’08), 2008.
    3.   Benefit of SAA. Sample-average approximation meth-    [2]  Amazon EC2, http://aws.amazon.com/ec2, 2012.
                                                                                               [3]  GoGrid, http://www.gogrid.com, 2012.
      od can overcome the provisioning problems with a    [4]  Amazon EC2 Reserved Instances, http://aws.amazon.com/ec2/
       large set of scenarios which are impossible to solve        reserved-instances, 2012.

### Página PDF 14

CHAISIRI ET AL.: OPTIMIZATION OF RESOURCE PROVISIONING COST IN CLOUD COMPUTING                                               177


[5]   F.V. Louveaux, “Stochastic Integer Programming,” Handbooks in                     Sivadon Chaisiri received the MEng degree
   OR & MS, vol. 10, pp. 213-266, 2003.                                                 from Kasetsart University, Bangkok, Thailand, in
[6]   A.J. Conejo, E. Castillo, and R. Garcı´a-Bertrand, “Linear Program-                        2005. He is currently working toward the PhD
    ming: Complicating  Variables,” Decomposition Techniques  in                       degree  at Nanyang Technological University,
     Mathematical Programming, chapter 3, pp. 107-139, Springer, 2006.                         Singapore. His current research interests  in-
[7]    J. Linderoth, A. Shapiro, and S. Wright, “The Empirical Behavior                         clude cloud computing and distributed systems.
     of Sampling Methods for Stochastic Programming,” Ann. Opera-                   He is a student member of the IEEE.
      tional Research, vol. 142, no. 1, pp. 215-241, 2006.
[8]  G. Juve and  E. Deelman, “Resource Provisioning Options
      for Large-Scale Scientific Workflows,” Proc. IEEE Fourth Int’l Conf.
      e-Science, 2008.
[9]   Z. Huang, C. He, and  J. Wu, “On-Demand Service in Grid:
     Architecture Design, and Implementation,” Proc. 11th Int’l Conf.                    Bu-Sung Lee received the BSc (Hons.) and
      Parallel and Distributed Systems (ICPADS ’05), 2005.                            PhD degrees from the Electrical and Electronics
[10]  Y. Jie, Q. Jie, and L. Ying, “A Profile-Based Approach to Just-in-                        Department, Loughborough University of Tech-
    Time Scalability for Cloud Applications,” Proc. IEEE Int’l Conf.                          nology, United Kingdom,  in 1982 and 1987,
     Cloud Computing (CLOUD ’09), 2009.                                                          respectively. He is currently an associate pro-
[11]  Y. Kee and C. Kesselman, “Grid Resource Abstraction, Virtualiza-                          fessor with the School of Computer Engineering,
                                                                            Nanyang Technological University, Singapore.      tion, and Provisioning for Time-Target Applications,” Proc. IEEE
                                                                    He was elected the inaugural president  of       Int’l Symp. Cluster Computing and the Grid, 2008.
                                                                                       Singapore Research and Education Networks[12] A.  Filali, A.S. Hafid, and M. Gendreau, “Adaptive Resources
                                                                                  (SingAREN), 2003-2007, and has been an
     Provisioning for Grid Applications and Services,” Proc. IEEE Int’l
                                                                            active member of several national standards organizations, such as a
     Conf. Comm., 2008.
                                                                 board member of Asia Pacific Advanced Networks (APAN) Ltd. In 2010,
[13] D. Kusic and N. Kandasamy, “Risk-Aware Limited Lookahead
                                                            he held a joint appointment as director, Service Platform Lab, HP Labs
     Control for Dynamic Resource Provisioning in Enterprise Com-
                                                                     Singapore. His research interests include computer networks protocols,
     puting Systems,” Proc. IEEE Int’l Conf. Autonomic Computing, 2006.
                                                                                distributed computing, network management, and grid/cloud computing.
[14] K. Miyashita, K. Masuda, and  F. Higashitani, “Coordinating                                                    He is a member of the IEEE.
     Service Allocation through Flexible Reservation,” IEEE Trans.
      Services Computing, vol. 1, no. 2, pp. 117-128, Apr.-June 2008.
                                                                                       Dusit Niyato received the BE degree from King
[15]  J. Chen, G. Soundararajan, and C. Amza, “Autonomic Provision-                                                                                      Mongkut’s Institute of Technology Ladkrabang,
     ing of Backend Databases in Dynamic Content Web Servers,” Proc.                                                                                    Bangkok, Thailand, in 1999 and the PhD degree
    IEEE Int’l Conf. Autonomic Computing, 2006.                                                                                                                 in electrical and computer engineering from the
[16]  L. Grit, D. Irwin, A. Yumerefendi, and J. Chase, “Virtual Machine                           University of Manitoba, Winnipeg, Canada, in
     Hosting for Networked Clusters: Building the Foundations for                        2008. He is currently an assistant professor in
    Autonomic Orchestration,” Proc. IEEE Int’l Workshop Virtualization                         the  Division  of Computer Communications,
     Technology in Distributed Computing, 2006.                                           School  of Computer Engineering, Nanyang
[17] H.N. Van, F.D. Tran, and J.-M. Menaud, “SLA-Aware Virtual                         Technological University, Singapore. His current
     Resource Management  for Cloud Infrastructures,”  Proc. IEEE                        research interests include the design, analysis,
     Ninth Int’l Conf. Computer and Information Technology, 2009.        and optimization of wireless communication, smart grid systems, green
[18] M. Cardosa, M.R. Korupolu, and A. Singh, “Shares and Utilities   radio communications, and mobile cloud computing. He is a member of
    Based Power Consolidation in Virtualized Server Environments,”   the IEEE.
      Proc. IFIP/IEEE 11th Int’l Conf. Symp. Integrated Network Manage-
     ment (IM ’09), 2009.
[19]  F. Hermenier,  X.  Lorca, and  J.-M. Menaud, “Entropy: A
     Consolidation Manager  for  Clusters,”  Proc. ACM SIGPLAN/
    SIGOPS Int’l Conf. Virtual Execution Environments (VEE ’09), 2009.
[20] N. Bobroff, A. Kochut, and K. Beaty, “Dynamic Placement of
     Virtual Machines for Managing SLA Violations,” Proc. IFIP/IEEE
       Int’l Symp. Integrated Network Management (IM ’07), pp. 119-128,
    May 2007.
[21]  P. Jirutitijaroen and C. Singh, “Reliability Constrained Multi-Area
    Adequacy Planning Using Stochastic Programming with Sample-
    Average Approximations,” IEEE Trans. Power Systems, vol. 23,
     no. 2, pp. 504-513, May 2008.
[22]  S. Chaisiri, B.S. Lee, and D. Niyato, “Optimal Virtual Machine
     Placement across Multiple Cloud Providers,” Proc. IEEE Asia-
      Pacific Services Computing Conf. (APSCC), 2009.
[23] GNU Linear Programming Kit (GLPK), http://www.gnu.org/
     software/glpk, 2012.
[24] W.-K. Mak, D.P. Morton, and R.K. Wood, “Monte Carlo Bounding
     Techniques  for Determining Solution Quality  in  Stochastic
     Programs,” Operations Research Letter, vol. 24, pp. 47-56, 1999.
[25] M.D. McKay, R.J. Beckman, and W.J. Conover, “A Comparison of
     Three Methods for Selecting Values of Input Variables in the
     Analysis  of Output from a Computer Code,”  Technometrics,
      vol. 21, no. 2, pp. 239-245, 1979.
[26]  R. Chheda, D. Shookowsky,  S. Stefanovich, and  J. Toscano,
     “Profiling Energy Usage for Efficient Consumption,” Architecture
        J., no. 18, 2008.
[27]  G.B. Dantzig and G. Infangerm, “Large-Scale Stochastic Linear
     Programs: Importance Sampling and Benders Decomposition,”
      Proc. IMACS World Congress on Computation and Applied Math.,
     1991.
[28] H. Heitsch and W. Ro¨misch, “Scenario Reduction Algorithms in
     Stochastic Programming,”  J. Computational Optimization and
      Applications, vol. 24, pp. 187-206, 2003.
