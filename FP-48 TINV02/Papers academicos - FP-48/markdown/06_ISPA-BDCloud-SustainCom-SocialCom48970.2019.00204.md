2108 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.53,NO.4,APRIL2015
A Subspace Projection Approach for Wall Clutter
Mitigation in Through-the-Wall Radar Imaging
FokHingChiTivive,Member,IEEE,AbdesselamBouzerdoum,SeniorMember,IEEE,and
MoenessG.Amin,Fellow,IEEE
Abstract—Oneofthemainchallengesinthrough-the-wallradar rescuemissions,behind-walltargetdetection,andsurveillance
imaging (TWRI) is the strong exterior wall returns, which tend and reconnaissance in urban environments [1]–[5]. One of the
to obscure indoor stationary targets, rendering target detection
main issues of imaging stationary targets inside a building is
and classification difficult, if not impossible. In this paper, an
thestrongclutterinducedbytheexteriorwall,whichisusually
effective wall clutter mitigation approach is proposed for TWRI
thatdoesnotrequireknowledgeofthebackgroundscenenordoes ahighlyreflectiveandattenuativemedium.
it rely on accurate modeling and estimation of wall parameters. Most TWRI studies dealing with stationary targets [6]–[8]
The proposed approach is based on the relative strength of the assume to have access of a background or reference scene,
exteriorwallreturnscomparedtobehind-walltargets.Itapplies
where background subtraction is performed on the raw data
singularvaluedecompositiontothedatamatrixconstructedfrom
prior to applying an image formation method for scene re-
thespace-frequencymeasurementstoidentifythewallsubspace.
Orthogonalsubspaceprojectionisperformedtoremovethewall construction. This approach, although effective in removing
electromagnetic signature from the radar signals. Furthermore, wall returns, is not feasible in practice. Therefore, different
this paper provides an analysis of the wall and target subspace approacheshavebeenproposedtodealwithstrongwallreflec-
characteristics,demonstratingthatbothwallandtargetsubspaces
tions without relying on the background scene data [9]–[14].
canbemultidimensional.Whilethewallsubspacedependsonthe
From the received signals, particularly the first wave arrivals,
wall type and building material, the target subspace depends on
thelocationofthetarget,thenumberoftargetsinthescene,and it is possible to estimate the front wall parameters, such as
the size of the target. Experimental results using simulated and dielectric constant and thickness [11]. The estimated param-
realdatademonstratetheeffectivenessofthesubspaceprojection eters can be used to model the EM wall returns, which are
method in mitigating wall clutter while preserving the target
subsequentlysubtractedfromthetotalradarreturns,rendering
image.Itisshownthattheperformanceoftheproposedapproach,
the received signals free of wall reflections. This approach
intermsoftheimprovementfactorofthetarget-to-clutterratio,
is better than existing approaches and is comparable to that of requires accuracy in parameter estimation and modeling. An-
backgroundsubtraction,whichrequiresknowledgeofareference othermethodofsuppressingthewallreflectionsistousethree
backgroundscene. antenna arrays placed parallel to the wall at different heights,
Index Terms—Singular value decomposition (SVD), subspace where the upper and lower arrays comprise receivers and the
projection, target subspace, through-the-wall radar imaging middlearrayconsistsoftransmitters[10].Asimplesubtraction
(TWRI),wallclutterremoval,wallsubspace. of the radar returns from the lower and upper arrays can lead
to wall clutter reduction. Due to the receiver symmetry with
I. INTRODUCTION respect to the transmitter, the contribution of the reflection
THROUGH-the-wallradarimaging(TWRI)isanemerging from the wall in the difference signal is suppressed. In this
scheme,twoadditionalarraysarerequired,andtheeffectofthe
technologyofincreasinginterest.Themainobjectiveisto
subtraction operation on the target reflections is unknown and
sense through the wall and inside enclosed building structures
cannot be controlled. A spatial filtering method was proposed
by using electromagnetic (EM) waves for determining the
forwallcluttermitigation[9].Thismethodreliesoninvariance
building layouts, discerning the intent of activities inside the
of the wall characteristic and is based on the assumption that
building, and detecting, identifying, and tracking moving tar-
the wall returns have the same characteristics with changing
gets.Thistypeoftechnologyishighlydesirableinsearch-and-
antenna location. This spatial invariance can be horizontal,
vertical, or along both dimensions in the wall plane. Thus, a
notch filter was applied across the antenna array to remove
ManuscriptreceivedJanuary14,2013;revisedDecember2,2013andJune9,
2014;acceptedAugust16,2014.Thisworkwassupportedbyagrantfromthe the zero frequency or low spatial frequencies, which capture
AustralianResearchCouncil.TheworkofM.G.Aminwassupportedbythe constant or slowly varying wall returns. It is noted, however,
OfficeofNavalResearchunderGrantN00014-11-0576.
that the filtering method is effective only for homogeneous or
F. H. C. Tivive and A. Bouzerdoum are with the School of Electrical,
Computer and Telecommunications Engineering, University of Wollongong, near-homogeneouswallsandatlowoperatingfrequencies.
Wollongong, N.S.W. 2522, Australia (e-mail: tivive@uow.edu.au; In this paper, we assume that the scene is stationary, and
a.bouzerdoum@uow.edu.au).
hence, change detection or Doppler/micro-Doppler processing
M. G. Amin is with the Radar Imaging Laboratory, Center for Advanced
Communications, Villanova University, Villanova, PA 19085 USA (e-mail: is not applicable for wall clutter removal and deletion of
moeness.amin@villanova.edu). animate and inanimate targets [16]–[18]. We present a new
Colorversionsofoneormoreofthefiguresinthispaperareavailableonline
subspace method for mitigating wall clutter, or at least sig-
athttp://ieeexplore.ieee.org.
DigitalObjectIdentifier10.1109/TGRS.2014.2355211 nificantly suppressing it, to reveal the targets behind the wall.
0196-2892©2014IEEE.Translationsandcontentminingarepermittedforacademicresearchonly.Personaluseisalsopermitted,butrepublication/redistribution
requiresIEEEpermission.Seehttp://www.ieee.org/publications_standards/publications/rights/index.htmlformoreinformation.

TIVIVEetal.:SUBSPACEPROJECTIONAPPROACHFORWALLCLUTTERMITIGATIONINTWRI 2109
The proposed technique first identifies the wall clutter and
target signal subspaces using singular value decomposition
(SVD); then, it projects the radar signal onto a subspace or-
thogonal to the wall subspace. SVD has been used previously
inground-penetratingradartoimprovethesignal-to-noiseratio
(SNR) of the radar images [19], [20]; the B-scan image is
decomposed into several eigenimages, and the first eigenim-
age is considered the target image. SVD has been used in
TWRI to remove the wall clutter and to detect behind-the-
wall targets from B-scan images [12]–[15]. The wall clutter
and the target reflections are assumed to reside in the first
and second eigenimages, respectively, whereas the remaining
eigenimages contain noise. Another SVD-based method was
proposedtoremovewallclutterintheformedimage,wherethe
wallreflectionsstillresideinthefirsteigenimagesandthetarget
reflections span several eigenimages [15]. However, recently,
we have shown that the wall clutter is generally characterized
by a high-dimensional subspace [21], [22]. Furthermore, the
weak wall singular components (SCs) may interleave with the
target SCs. Therefore, a more effective technique is required
to separate the wall and target subspaces since the first SC is
unlikelytoaccountforallwallreturns.
This paper extends our previous work [21], [22] in both
analysis and experimentation. It considers SVD of the data
matrix constructed from stepped-frequency matched filtered
measurements obtained at different antenna positions. In so
doing, it operates on the data and not on the beamformed
image. The results of the two operations are entirely different
due to the target localization through coherent combining. We
show that, in near field imaging, the wall returns can span
a multidimensional subspace, which depends, among other
factors, on the periodic structure of the wall, the frequency
response, the uniformity of the wall thickness, and the array
geometry.Moreover,thetargetreflectionscanspanasubspace
whosedimensiondependsonthetargetsize,thetargetlocation,
the number of targets, and the configuration of the antenna
array.Bothempiricaldataandsimulationsconfirmthatthewall
returnsgenerallyspanamultidimensionalsubspace,wherethe Fig.1. TWRIgeometry.(a)Infreespace.(b)Throughthewall.
significanttargetSCscaninterleavewithsomeoftheweakwall
schemeisderivedforfreespaceandthenextendedtoimaging
SCs.Thispaperconductsacomprehensiveanalysisofthewall
behindahomogeneouswall.ThegeometricmodelofTWRIas
andtargeteigensubspaces.Furthermore,itpresentsasubspace
describedin[5]isusedtoestimatethesignalpropagationdelay
classification method to segregate between the target and wall
inthepresenceofahomogeneouswall.
subspaces.Asubspaceprojectionmethodisthenproposedfor
In free space, the geometric model of a TWRI system is
wall clutter mitigation, which works on the space-frequency
depicted in Fig. 1(a). Here, a ground-based monostatic syn-
datamatrixinsteadoftheformedimage.
thetic aperture radar (SAR) system is used to synthesize an
The remainder of this paper is organized as follows. The
N-elementlineararray.Alocalcoordinatesystemisdefinedto
next section presents the geometric model of TWRI and de-
representtheregionofinterestwiththehorizontalandvertical
scribesdelay-and-sum(DS)beamformingforimageformation. axesdenotedasx(cid:2) andz(cid:2),respectively.Thecenterofthescene
SectionIIIpresentstheanalysisofthewallandtargeteigensub-
is at (0, 0), and θ is the viewing angle of the nth antenna.
n
spaces supported by simulation results. Section IV describes
Let R (0,0) and c denote the distance of the nth antenna to
n n
the proposed subspace projection approach for wall clutter
the center of the scene and to the center of the array aperture,
mitigation. Experimental results using real data are given in
respectively. The distance from the nth antenna to the pixel
SectionV.Finally,theconclusionispresentedinSectionVI. location (x(cid:2),z(cid:2)) within the region of interest is denoted by
p p
R (x(cid:2),z(cid:2))andcanbecomputedas
n p p
II. THROUGH-WALLRADARIMAGINGSIGNALMODEL (cid:2) (cid:3) (cid:2)
R x (cid:2) ,z (cid:2) = R (0,0)2+2R (0,0)z (cid:2) cos(θ )
n p p n n p n (cid:4)
ThissectionpresentstheTWRIsignalmodelusedtoexplain 1
the proposed wall clutter mitigation approach. The imaging −2R n (0,0)x (cid:2) p sin(θ n )+x (cid:2) p 2+z p (cid:2)2 2 . (1)

2110 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.53,NO.4,APRIL2015
Theviewingangleθ
n
ofthenthantennaisgivenby III. ANALYSISOFWALLANDTARGETEIGENSUBSPACES
(cid:5) (cid:6)
θ =sin −1 c n . (2) Several SVD-based wall clutter mitigation approaches have
n R (0,0) been proposed which assume that the wall reflections are
n
characterized by the first singular vector associated with the
Withoutlossofgenerality,letusassumeasingletargetlocated
most dominant singular value [12]–[15]. In [21] and [22], we
at(x(cid:2),z(cid:2)).Thetwo-waypropagationdelayτ (x(cid:2),z(cid:2))fromthe
p p n p p have shown that multiple singular vectors can span the wall
nthantennatothetargetisgivenby
subspace. In this section, we investigate the factors affecting
(cid:2) (cid:3)
(cid:2) (cid:3) 2R x(cid:2),z(cid:2) thewallandtargeteigensubspaces.Thedimensionofthewall
τ n x (cid:2) p ,z p (cid:2) = n c p p (3) subspace is related to, among other factors, the wall hetero-
geneity, the wall thickness uniformity, and the antenna array
wherecisthespeedoflightinfreespace.
configuration.Forthetargetsubspace,itsdimensionisaffected
When there is a homogeneous wall in front of the radar
by the target location, the target size, the number of targets
system as shown in Fig. 1(b), the two-way propagation delay
behind the wall, and the configuration of the array aperture.
oftheradarsignalfromthenthantennatothetargetisgivenby
Numerical simulations using XFDTD are included to support
2 theanalysisofthewallandtargetsubspaces.
τ (x ,z )= (R (x ,z )
n p p c n√,air1 p p (cid:3)
+ (cid:4)R (x ,z )+R (x ,z ) (4)
n,w p p n,air2 p p A. EigenstructureofWallSubspace
where (cid:4) is the relative permittivity of the wall and InpracticalTWRIapplications,weoftendealwithtwotypes
R n,air1 (x p ,z p ), R n,w (x p ,z p ), and R n,air2 (x p ,z p ) denote the ofwalls:homogeneousandheterogeneouswalls.Thefollowing
distances traveled by the signal from the nth antenna to the twosubsectionsanalyzetheeigenstructureofthewallsubspace,
target at location (x p ,z p ) before, through, and after the wall, usingbothtypesofwalls.
respectively.Thesedistancescanbeestimatedasfollows[8]: 1) Homogeneous Wall: A homogeneous wall can be mod-
z eled as a uniform dielectric slab of thickness d and dielectric
R (x ,z )= a (5)
n,air1 p p cos(ϕ (x ,z )) constant(cid:4).Assumingthatthesignalistransmittedperpendicu-
n p p
d larlytothesurfaceofthewall,thewallreturnofahomogeneous
R (x ,z )= (6)
n,w p p cos(φ (x ,z )) wall is calculated based on the plane wave Fresnel reflection
n p p
R (x ,z )= z t (7) and transmission coefficients obtained from Maxwell’s equa-
n,air2 p p cos(ϕ (x ,z )) tions [28]. Let ρ be the local Fresnel reflection coefficient,
n p p
givenby
wherez a isthestandoffdistancefromtheantennaarraytothe √
wall, d is the wall thickness, z t is the distance from the wall ρ= 1− √ (cid:4) . (10)
to the target, and ϕ (x ,z ) and φ (x ,z ) are the angles of 1+ (cid:4)
n p p n p p
incidence and refraction from the nth antenna to the target at
The reflection coefficient at the mth frequency Γ can be
location (x ,z ), respectively. To image the behind-the-wall m
p p
writtenas
scene, a stepped-frequency signal is synthesized by emitting √
monochromatic signals with frequencies equispaced over the ρ(1−exp(−2j (cid:4)k d))
desiredbandwidthω M−1 −ω 0 Γ m = 1−ρ2exp(−2j √ (cid:4)k m m d) (11)
ω m =ω 0 +mΔω, form=0,...,M −1 (8) where k m =ω m /c is the wavenumber. The radar signal
backscattered from the wall and received by the nth antenna
whereω isthelowestfrequencyinthedesiredfrequencyband,
0 canbeexpressedas
Δω is the frequency step size, and M is the total number of
frequencies. s (m,n)= G m λ m exp(−j2k m z n ) Γ (12)
There are several approaches for image formation, includ- w 8π z n m
ing tomographic approaches [23], differential SAR [24], com-
where z is the distance between the nth antenna and the
n
pressed sensing [25], and adaptive beamformers [26], [27].
wall, λ is the wavelength of the mth monochromatic signal,
m
Here, we employ DS beamforming to compute the complex
and G is the antenna gain at the mth frequency [11]. The
m
amplitudeofthepixel,whichisgivenby
wallbackscatteredsignalsreceivedbytheN-elementarraycan
1
N(cid:7)−1M(cid:7)−1 be arranged into a matrix Φ
w
∈CM×N, where each column
I(x,z)= NM s(m,n)exp(jω m τ n (x,z)) (9) contains the signal received at one antenna location and each
n=0m=0 rowcontainsthesignalsfromonefrequency
wheres(m,n)istheradarsignalatthemthfrequencyreceived
Φ =[φ ] (13)
w mn
by the nth antenna and τ (x,z) is the focusing delay for
n
the pixel at location (x,z) with respect to the nth antenna, where φ =s (m,n). Assuming that the antenna gain and
mn w
including the propagation through the wall. Before describing wallreflectioncoefficientdonotchangewithantennalocation,
theproposedwallcluttermitigationmethod,wefirstpresentthe Φ can be expressed as the product of a diagonal matrix
w
analysisofthewallandtargeteigensubspaces. A, containing the antenna gains and reflection coefficients

TIVIVEetal.:SUBSPACEPROJECTIONAPPROACHFORWALLCLUTTERMITIGATIONINTWRI 2111
×N
| (as a | function | of frequency), |     | with | an M | matrix | B   | which |     |     |     |     |     |     |
| ----- | -------- | -------------- | --- | ---- | ---- | ------ | --- | ----- | --- | --- | --- | --- | --- | --- |
dependsontheantennastandoffdistance
|     |     |     |     | Φ =AB |     |     |     | (14) |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
w
where
|     | A=diag(G |        | λ   | Γ ,...,G |     | λ Γ | )   | (15) |     |     |     |     |     |     |
| --- | -------- | ------ | --- | -------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
|     |          |        | 0 0 | 0        | M−1 | M−1 | M−1 |      |     |     |     |     |     |     |
|     | B        | =[b mn | ]   |          |     |     |     | (16) |     |     |     |     |     |     |
with
|     |     |     |     | exp(−j2k | z   | )   |     |      |     |     |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
|     |     | b   | =   |          | m   | n . |     | (17) |     |     |     |     |     |     |
mn
|        |             |               |            | 8πz      | n          |          |            |          |     |     |     |     |     |     |
| ------ | ----------- | ------------- | ---------- | -------- | ---------- | -------- | ---------- | -------- | --- | --- | --- | --- | --- | --- |
| The    | wall        | eigensubspace |            | can be   | obtained   | by       | applying   | SVD      |     |     |     |     |     |     |
| and    | identifying | the           | singular   | vectors  | containing |          | the        | wall re- |     |     |     |     |     |     |
| turns. | Since       | A is a        | full rank  | diagonal |            | matrix,  | it follows | that     |     |     |     |     |     |     |
| rank(Φ | )=rank(B);  |               | therefore, |          | the wall   | subspace | dimension  |          |     |     |     |     |     |     |
w
| is determined |                                             | by the  | rank | of B.    | Furthermore, |             | it is clear | from     |     |     |     |     |     |     |
| ------------- | ------------------------------------------- | ------- | ---- | -------- | ------------ | ----------- | ----------- | -------- | --- | --- | --- | --- | --- | --- |
| (17)          | that the                                    | columns | of   | B depend | on           | the antenna |             | standoff |     |     |     |     |     |     |
| distancez     | ;therowsofBdependonthefrequency.Inpractice, |         |      |          |              |             |             |          |     |     |     |     |     |     |
n
| the number  |          | of antennas |     | N is          | smaller | than          | the number | of     |     |     |     |     |     |     |
| ----------- | -------- | ----------- | --- | ------------- | ------- | ------------- | ---------- | ------ | --- | --- | --- | --- | --- | --- |
| frequencies |          | M. Thus,    | the | rank          | of B    | is determined |            | by the |     |     |     |     |     |     |
| standoff    | distance | of          | the | antenna       | to the  | wall.         | Although   | the    |     |     |     |     |     |     |
| gain        | of the   | transceiver | in  | a synthesized |         | array         | aperture   | varies |     |     |     |     |     |     |
withfrequenciesandnotantennalocations,ithasnoeffecton
the rank of the matrix Φ and therefore does not change the Fig.2. Perturbationanalysisintheantennastandoffdistance:(a)Subspace
w
dimensionofthewallsubspace. distortionindexasafunctionofthetiltangleand(b)thefirst20normalized
singularvaluesatatiltangleof5◦.Forclarity,thefirstsingularvalueisomitted;
| There | are | two cases | where | the | signals | backscattered |     | from |     |     |     |     |     |     |
| ----- | --- | --------- | ----- | --- | ------- | ------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
theothersingularvaluesarenormalizedwiththefirstone.
| a homogeneous |     | wall | span | a multidimensional |     |     | subspace: | the |     |     |     |     |     |     |
| ------------- | --- | ---- | ---- | ------------------ | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
antenna array is not perfectly aligned (parallel to) the wall ≥σ ≥0. Ideally, a homogeneous wall subspace is spanned
N
surface, or the wall exhibits nonuniform thickness along the by the first singular vector associated with the dominant sin-
antenna array. In the first case, each antenna is positioned at a gularvalue.Perturbations intheremainingsingularvaluesare
|                            |     |     |     |                               |     |     |     |     | considered | as subspace distortions. |     | We define | the subspace |     |
| -------------------------- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | ---------- | ------------------------ | --- | --------- | ------------ | --- |
| differentstandoffdistancez |     |     |     | n fromthewall;thus,thecolumns |     |     |     |     |            |                          |     |           |              |     |
ofB becomelinearlyindependent,therebyincreasingtherank distortion index of a homogeneous wall δ as the fraction of
s
of the matrix and the dimension of the wall subspace. In the powercarriedbythenondominantSCs
secondcase,duetothevariationsinthewallthickness,thetwo- (cid:8)N
| waypropagationdelayofthesignalreflectedfromthebackof |     |     |     |     |     |     |     |     |     |     | σ2  |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i
i=2
thewallvariesfromoneantennatoanother,causingthesignals δ s = . (19)
(cid:8)N
| receivedacrosstheantennastobedifferentfromeachotherand |            |     |           |     |        |                |     |       |     |     | σ2  |     |     |     |
| ------------------------------------------------------ | ---------- | --- | --------- | --- | ------ | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
| hence                                                  | increasing | the | dimension |     | of the | wall subspace. |     | These |     |     |     | i   |     |     |
i=1
| two | cases are | investigated |     | using | numerical | simulations |     | with |        |                         |       |           |       |       |
| --- | --------- | ------------ | --- | ----- | --------- | ----------- | --- | ---- | ------ | ----------------------- | ----- | --------- | ----- | ----- |
|     |           |              |     |       |           |             |     |      | In the | first case, the antenna | array | is tilted | at an | angle |
XFDTDsoftware.Thefirstnumericalsimulationscenariocon-
withrespecttothewallsurface.Thesubspacedistortionindex
sistsofahomogeneouswallofthickness0.15mandadielectric
|     |     |     |     |     |     |     |     |     | of a homogeneous | wall is | computed | while | varying | the tilt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------- | -------- | ----- | ------- | -------- |
constant7.6placedinfrontoftheradaratastandoffdistanceof 1◦ 10◦.
|     |     |     |     |     |     |     |     |     | angle from | to Fig. | 2(a) illustrates | the | variations | of the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ---------------- | --- | ---------- | ------ |
1m.A51-elementantennaarrayofsize1.2missynthesizedfor
|     |     |     |     |     |     |     |     |     | subspace | distortion index as | a function | of the | tilt angle, | and |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------------- | ---------- | ------ | ----------- | --- |
imaging. The excitation signal is a modulated Gaussian pulse Fig. 2(b) depicts the normalized singular values of the wall
| which | covers | the frequency |     | range | from | 2 to 3 | GHz. The | time |     |     |     |     |     |     |
| ----- | ------ | ------------- | --- | ----- | ---- | ------ | -------- | ---- | --- | --- | --- | --- | --- | --- |
subspaceatasubspacedistortionindexof0.15.Amisalignment
| domain | responses | are | transformed |     | into | the frequency |     | domain |     |     |     |     |     |     |
| ------ | --------- | --- | ----------- | --- | ---- | ------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
of5◦withrespecttothesurfaceofthewallproducesasubspace
| and | sampled | to produce |     | the stepped-frequency |     |     | signals | which |     |     |     |     |     |     |
| --- | ------- | ---------- | --- | --------------------- | --- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- |
distortionindexof0.15,resultingin16nonzerosingularvalues,
| arearrangedintoamatrixΦ |     |     |     | .UsingSVD,thematrixΦ |     |     |     | can |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
w w as shown in Fig. 2(b). Therefore, we can conclude that the
bedecomposedas signals backscattered from a homogeneous wall that is not
=UΣVH paralleltotheantennaarrayspanamultidimensionalsubspace.
|     |     |     | Φ   | w   |     |     |     | (18) |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
Inthesecondcase,thewallthicknessisincreasedgradually
H
where denotes the Hermitian transpose, U =[u 1 ,...,u M ] alongtheantennaarray:Thewallthicknessinfrontofthefirst
and V =[v ,...,v ] are unitary matrices containing the left antennaisd,andthatatthelastantennaisd+Δd.Inthesimu-
|     |     | 1   | N   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and right singular vectors, respectively, and Σ is a rectangular lations,theparameterΔdisincreasedfrom0.03to0.3mwhile
matrix of the same size as Φ with singular values σ on the d is fixed at 0.15 m. The subspace distortion index computed
|     |     |     |     | w   |     |     |     | i   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
maindiagonalarrangedindecreasingorder,i.e.,σ ≥σ ≥··· as a function of the relative variations in the wall thickness
|     |     |     |     |     |     |     | 1   | 2   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

2112 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.53,NO.4,APRIL2015
|     |     |     |     |     |     |     | Fig.4. Eigenstructureofaheterogeneouswall:(a)Imageofthehollowcon- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
creteblockwall,(b)itsnormalizedsingularvalues,(c)imageofthereinforced
concretewallwithverticalrebarsonly,and(d)itsnormalizedsingularvalues.
|     |     |     |     |     |     |     | For clarity, | the first | singular | value is omitted; | the | other singular | values are |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | -------- | ----------------- | --- | -------------- | ---------- |
normalizedwiththefirstone.
metallicrebarsspacingatanintervalof0.2m.TheTWRIscene
Fig. 3. Perturbation analysis in the wall thickness: (a) Subspace distortion devoid of targets is illuminated with a modulated Gaussian
indexasafunctionoftherelativevariationsinthewallthicknessand(b)thefirst pulse centered at 1.5 GHz. The time domain responses ob-
20normalizedsingularvaluesexcludingthefirstoneatarelativeperturbation tained from each of these walls are transformed into stepped-
of0.06.
|     |     |     |     |     |     |     | frequency | signals | covering | the | frequency | band of | 2–3 GHz; |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | -------- | --- | --------- | ------- | -------- |
is shown in Fig. 3(a). Fig. 3(b) illustrates the normalized wall theyarethenarrangedintoamatrixΦ .Fig.4showstheDS-
w
singularvaluesatarelativevariationof0.06(Δd/d=0.06)in beamformedimagesandthenormalizedsingularvaluesofthe
thewallthickness.Thenumericalsimulationsshowthat,when signal matrix for both types of heterogeneous walls: Fig. 4(a)
the homogeneous wall does not have uniform thickness, the and(b)areforthehollowconcreteblockwall,andFig.4(c)and
wallreflectionsspanamultidimensionalsubspace. (d)areforthereinforcedconcretewall.Thenumberofnonzero
|     |     |     |     |     |     |     | singular | values | in Fig. | 4(b) and | (d) indicates | that | the rank of |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------- | -------- | ------------- | ---- | ----------- |
B. HeterogeneousWall the matrix Φ w is greater than one. Thus, we conclude that the
wallreturnsfromaheterogeneouswallspanamultidimensional
| A wall | is considered | heterogeneous |     | when | the | dielectric |     |     |     |     |     |     |     |
| ------ | ------------- | ------------- | --- | ---- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
subspace.
| properties  | of its building | material | vary   | along     | either   | or both |               |      |                 |          |            |             |            |
| ----------- | --------------- | -------- | ------ | --------- | -------- | ------- | ------------- | ---- | --------------- | -------- | ---------- | ----------- | ---------- |
|             |                 |          |        |           |          |         | To summarize, |      | the wall        | subspace | is not     | necessarily | char-      |
| dimensions, | i.e., height    | and      | width. | If a wall | is built | from    |               |      |                 |          |            |             |            |
|             |                 |          |        |           |          |         | acterized     | by a | single singular |          | vector but | can be      | spanned by |
severalverticalplaneswhosedielectricconstantsvaryalongthe
|     |     |     |     |     |     |     | multiple | singular | vectors. | There | are several | factors | that affect |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | -------- | ----- | ----------- | ------- | ----------- |
horizontalantennaarray,itisclearfrom(11)thatthereflection
thedimensionofthewallsubspace,namely,thewallEMchar-
| coefficient | will be a function |     | of the | antenna | location; | thereby, |     |     |     |     |     |     |     |
| ----------- | ------------------ | --- | ------ | ------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
acteristics,thewallthicknessuniformity,andtheconfiguration
| the columns | of the matrix | Φ   | become | linearly | independent, |     |     |     |     |     |     |     |     |
| ----------- | ------------- | --- | ------ | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
w
|         |               |            |     |           |      |           | of the antenna |     | array. The | next | section presents | an  | analysis of |
| ------- | ------------- | ---------- | --- | --------- | ---- | --------- | -------------- | --- | ---------- | ---- | ---------------- | --- | ----------- |
| and the | wall subspace | increases. | In  | practice, | most | heteroge- |                |     |            |      |                  |     |             |
thetargetsubspace.
| neous walls  | are built    | in such | a way       | that they | exhibit | some  |                                   |     |     |     |     |     |     |
| ------------ | ------------ | ------- | ----------- | --------- | ------- | ----- | --------------------------------- | --- | --- | --- | --- | --- | --- |
| periodicity. | For example, | walls   | constructed | from      | cinder  | block |                                   |     |     |     |     |     |     |
|              |              |         |             |           |         |       | C. EigenstructureofTargetSubspace |     |     |     |     |     |     |
orcrossbarreinforcedconcreteare2-Dperiodicheterogeneous
walls, whereas drywalls with vertical wooden studs and rein- In this section, we analyze the eigensubspace of a target,
|     |     |     |     |     |     |     | where the | received | signals | comprise | only | the target | returns. |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ------- | -------- | ---- | ---------- | -------- |
forcedconcretewallswithverticalrebarsonlyare1-Dperiodic
walls. Due to the fast-fading phenomenon caused by the wall First, we consider a point target with frequency-dependent
(x(cid:2) (cid:2)).
heterogeneity,thistypeofwallsisanalyzedbyeitherusingEM reflection coefficient σ located at the location ,z The
|     |     |     |     |     |     |     |     |     | m   |     |     |     | p p |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
targetsignalreceivedbythenthantennacanbewrittenas
simulationtoolorperformingrealexperiments.
For eigensubspace analysis, we conduct several numerical σ G λ (cid:2) (cid:2) (cid:3)(cid:3)
|     |     |     |     |     |     |     |            |     | m m | m   | −jω   | (cid:2) (cid:2) |        |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | ----- | --------------- | ------ |
|     |     |     |     |     |     |     | s t (m,n)= |     |     | exp | m τ n | x ,z            | . (20) |
simulations using two kinds of heterogeneous walls: hollow 4π p p
| concrete | block wall and | reinforced | concrete |     | wall. The | hollow |            |         |          |        |             |       |         |
| -------- | -------------- | ---------- | -------- | --- | --------- | ------ | ---------- | ------- | -------- | ------ | ----------- | ----- | ------- |
|          |                |            |          |     |           |        | The target | signals | received | across | the antenna | array | are ar- |
concreteblockwallisbuiltusingcinderblocksofsize0.2m×
rangedintothematrixΦ
t
0.4mwithathicknessof0.15m.Thereinforcedconcretewall
hasathicknessof0.15mandconsistsof0.025-m-thickvertical Φ =AB (21)
t

TIVIVEetal.:SUBSPACEPROJECTIONAPPROACHFORWALLCLUTTERMITIGATIONINTWRI 2113
where
|         | (cid:5)      |                                |       |             | (cid:6) |     |     |     |     |     |
| ------- | ------------ | ------------------------------ | ----- | ----------- | ------- | --- | --- | --- | --- | --- |
|         | σ 0 G 0 λ 0, | σ 1 G 1 λ 1,...,               | σ M−1 | G M−1 λ M−1 |         |     |     |     |     |     |
| A=diag  |              |                                |       |             | (22)    |     |     |     |     |     |
|         | 4π           | 4π                             |       | 4π          |         |     |     |     |     |     |
| (cid:9) | (cid:2)      | (cid:2) (cid:3)(cid:3)(cid:10) |       |             |         |     |     |     |     |     |
|         | −jω          | (cid:2) (cid:2)                |       |             |         |     |     |     |     |     |
| B = exp | m τ          | n x ,z                         | .     |             | (23)    |     |     |     |     |     |
p p
Sincethetwo-waypropagationdelaybetweenthenthantenna
| andthetargetτ  | (x(cid:2),z(cid:2))isdependentontheantennalocation, |          |         |          |             |     |     |     |     |     |
| -------------- | --------------------------------------------------- | -------- | ------- | -------- | ----------- | --- | --- | --- | --- | --- |
|                | n p                                                 | p        |         |          |             |     |     |     |     |     |
| it is expected | to vary                                             | from one | antenna | location | to another, |     |     |     |     |     |
causingthecolumnsofthematrixBin(23)tobecomelinearly
| independent.Therefore,therankofΦ |              |          | t changeswiththetarget |               |             |     |     |     |     |     |
| -------------------------------- | ------------ | -------- | ---------------------- | ------------- | ----------- | --- | --- | --- | --- | --- |
| location.                        | For example, | a target | placed                 | at the center | of the      |     |     |     |     |     |
| array will                       | reduce the   | rank of  | Φ since the            | signal        | propagation |     |     |     |     |     |
t
| delays      | from the antennas       | on               | the left half                            | of the array | are the              |     |     |     |     |     |
| ----------- | ----------------------- | ---------------- | ---------------------------------------- | ------------ | -------------------- | --- | --- | --- | --- | --- |
| same as     | those on the            | right half       | of the array,                            | i.e., τ      | (x(cid:2),z(cid:2))= |     |     |     |     |     |
|             |                         |                  |                                          |              | 0 p p                |     |     |     |     |     |
| τ (x(cid:2) | ,z (cid:2)),τ (x(cid:2) | ,z (cid:2))=τ    | (x(cid:2) ,z (cid:2)),etc.Inarecentstudy |              |                      |     |     |     |     |     |
| N−1         | p p 1 p                 | p N−2            | p p                                      |              |                      |     |     |     |     |     |
| [21], we    | have shown              | that reflections | from                                     | a point      | target span          |     |     |     |     |     |
amultidimensionalsubspace,whichdependsonthenumberof
targetsinthesceneandtheconfigurationoftheantennaarray.
Thetargetlocationwithrespecttotheradaralsoinfluencesthe
targetsubspacedimension.
| Next,     | we investigate | the dimension | of      | the target  | subspace |                                                                  |     |     |     |     |
| --------- | -------------- | ------------- | ------- | ----------- | -------- | ---------------------------------------------------------------- | --- | --- | --- | --- |
| under two | imaging        | scenarios,    | namely, | short range | and long |                                                                  |     |     |     |     |
|           |                |               |         |             |          | Fig.5. Formedimagesandsingularvaluesoftwodifferentimagingranges: |     |     |     |     |
range,wherethetargetisplacedclosetoorfarfromtheradar (a)Imageofaneartarget,(b)itsnormalizedsingularvalues,(c)imageofadis-
system. In the former, the viewing angle θ of the antenna tanttarget,and(d)itsnormalizedsingularvalues.Forclarity,thefirstsingular
|                     |             |                    |                 | n       |            | valueisomitted;theothersingularvaluesarenormalizedwiththefirstone. |     |     |     |     |
| ------------------- | ----------- | ------------------ | --------------- | ------- | ---------- | ------------------------------------------------------------------ | --- | --- | --- | --- |
| varies considerably |             | across the         | array aperture, | causing | the dis-   |                                                                    |     |     |     |     |
| tance traveled      | by the      | signal from        | each antenna    | to the  | target     | to                                                                 |     |     |     |     |
| be different.       | Based       | on the propagation | delay           | given   | in (3), it | is                                                                 |     |     |     |     |
| clear that          | the target  | signal is          | related to the  | viewing | angle, and |                                                                    |     |     |     |     |
| therefore,          | the number  | of linearly        | independent     | columns | in the     |                                                                    |     |     |     |     |
| matrix              | Φ increases | when the           | viewing angle   | varies  | markedly   |                                                                    |     |     |     |     |
t
| across the      | array aperture. | On             | the other hand, | for a              | long-range  |     |     |     |     |     |
| --------------- | --------------- | -------------- | --------------- | ------------------ | ----------- | --- | --- | --- | --- | --- |
| target,         | the changes     | in the viewing | angle           | across             | the antenna |     |     |     |     |     |
| array are       | much smaller,   | resulting      | in almost       | the same           | distance    |     |     |     |     |     |
| between         | each antenna    | element        | and the         | target; therefore, | the         |     |     |     |     |     |
| target subspace | is narrower     | compared       | to              | that of a          | short-range |     |     |     |     |     |
| target.         | To illustrate   | this, a target | is placed       | at two             | different   |     |     |     |     |     |
| locations:      | a short range   | at (0,         | 1.2) m          | and a long         | range       | at  |     |     |     |     |
(0,6.2)m.Theformedimagesandthesingularvaluesforboth
casesareshowninFig.5.Fig.5(a)and(b)depictstheformed
| image and | the singular | values | of the near | target, respectively, |     |     |     |     |     |     |
| --------- | ------------ | ------ | ----------- | --------------------- | --- | --- | --- | --- | --- | --- |
andFig.5(c)and(d)showstheimageandsingularvaluesofthe
distanttarget.Thedifferenceinthenumberofnonzerosingular
valuesbetweenFig.5(b)and(d)confirmsthatthesubspaceof
adistanttargetisnarrowerthanthatofaneartarget.
Anotherfactorthatcanaffectthetargetsubspacedimension
|     |     |     |     |     |     | Fig. 6. Formed | images and singular | values of | two different target | sizes: |
| --- | --- | --- | --- | --- | --- | -------------- | ------------------- | --------- | -------------------- | ------ |
is the target size. For illustration, we simulate a square plate (a)Imageofthesmalldihedral,(b)itsnormalizedsingularvalues,(c)imageof
dihedraloftwodifferentareas:0.09and1m2.Thedihedralis thelargedihedral,and(d)itsnormalizedsingularvalues.Forclarity,thefirstsin-
placed at a standoff distance of 2.2 m from the radar without gularvalueisomitted;theothersingularvaluesarenormalizedwiththefirstone.
any wall. Fig. 6(a) and (b) presents the formed image and the In summary, the target returns do not span a 1-D subspace
normalizedsingularvaluesofthesmalldihedral,andFig.6(c) as reported in some existing literatures [12]–[14] but a mul-
and (d) shows the formed image and the normalized singular tidimensional subspace, depending on several factors. These
values of the large dihedral. The difference in the number of factors include, among others, the target location, the target
nonzero singular values between Fig. 6(b) and (d) shows that size, the number of targets in the scene, and the antenna
the target subspace of the large dihedral is wider than that of array configuration. Next, we investigate the eigenstructure of
| thesmalldihedral. |     |     |     |     |     | combinedwallandtargetreturns. |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- |

2114 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.53,NO.4,APRIL2015
Fig.7. Imageofascenewithtwodihedralsplacedbehindahomogeneous
wall:(a)Imageoftargetsandwall,(b)imagewithoutthefirstdominantSC,
and(c)imagewithoutthefirsttwoleadingSCs.Thetargetsarecircledbythe
rectangles.
D. CombinedWall–TargetEigensubspace
Intheaforementionedanalysis,wehaveshownthatthewall
subspacecanbemultidimensional,andthetargetreflectionsspan
a multidimensional subspace. Here, we investigate the eigen- Fig.8. RangeprofilesofthefirstsixdominantSCs(1st-SCto6th-SC).
structure of combined wall and target returns. From a TWRI identifythesingularvectorscharacterizingthewallreturns,we
| scene comprising | a wall | and | target(s), | the received | signal | can |     |     |     |     |     |     |     |     |
| ---------------- | ------ | --- | ---------- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
proposeasimpleprocedure.From(25),thematrixΦconsistsof
beexpressedasasuperpositionofthewallandtargetreturns
|     |     |     |     |     |     |     | aweightedsumofN |     |     | SCs,whereeachSCisgivenbytheouter |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | -------------------------------- | --- | --- | --- | --- |
s(m,n)=s (m,n)+s (m,n)+s (m,n) (24) product of a pair of left and right singular vectors multiplied
|     | w   |     | t   |     | wt  |     |                    |     |     |                |      |        |           |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | -------------- | ---- | ------ | --------- | --- |
|     |     |     |     |     |     |     | byitscorresponding |     |     | singularvalue. | LetΨ | denote | theithSC, |     |
i
| wheres          | (m,n)denotesthewallreturns,s |       |        | (m,n)denotesthe  |     |          | givenby |     |     |     |     |     |     |     |
| --------------- | ---------------------------- | ----- | ------ | ---------------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| w               |                              |       |        | t                |     |          |         |     |     |     |     |     |     |     |
| target returns, | and s wt                     | (m,n) | models | the interactions |     | (if they |         |     |     |     |     |     |     |     |
vH
exist)betweenthetargetandthewall.Sincethewallreflections Ψ i =σ i u i =[ψ ,...,ψ ] (26)
|                                                         |          |          |                 |     |        |         |        |                                 |     | i   | i1  | iN  |           |     |
| ------------------------------------------------------- | -------- | -------- | --------------- | --- | ------ | ------- | ------ | ------------------------------- | --- | --- | --- | --- | --------- | --- |
| are relatively                                          | stronger | than the | behind-the-wall |     | target | reflec- |        |                                 |     |     |     |     |           |     |
|                                                         |          |          |                 |     |        |         | whereψ | denotesthejthcolumnofthematrixΨ |     |     |     |     | .Therange |     |
| tions,itisassumedthatthewallreturnsmostlylieinasubspace |          |          |                 |     |        |         |        | ij                              |     |     |     |     | i         |     |
profileassociatedwiththeithSCcanbecomputedas
| spanned | by the singular | vectors | associated | with | the dominant |     |     |     |     |     |     |     |     |     |
| ------- | --------------- | ------- | ---------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
singular values. Therefore, discarding the singular vectors as- (cid:7)N
1
sociated with the dominant singular values can suppress the r = IFFT(ψ ) (27)
|              |               |        |     |                |     |         |     |     | i   | N   |     | ik  |     |     |
| ------------ | ------------- | ------ | --- | -------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| wall clutter | in the formed | image. | For | demonstration, |     | we sim- |     |     |     |     |     |     |     |     |
k=1
m2
| ulate a scene | with two      | square      | plate dihedrals |             | of area         | 0.16 |       |          |          |             |                    |          |            |          |
| ------------- | ------------- | ----------- | --------------- | ----------- | --------------- | ---- | ----- | -------- | -------- | ----------- | ------------------ | -------- | ---------- | -------- |
|               |               |             |                 |             |                 |      | where | IFFT     | denotes  | the inverse | fast Fourier       |          | transform. | The      |
| placed behind | a homogeneous |             | wall at         | coordinates | (−0.6,          | 1.6) |       |          |          |             |                    |          |            |          |
|               |               |             |                 |             |                 |      | main  | peak in  | a range  | profile     | is used to         | indicate | whether    | the      |
| m and (0.6,   | 1.3) m. The   | homogeneous |                 | wall        | has a thickness | of   |       |          |          |             |                    |          |            |          |
|               |               |             |                 |             |                 |      | SC    | contains | the wall | or target   | returns, depending |          | on         | the peak |
0.15mandadielectricconstantof7.6.Here,weslightlytiltthe
locationwithrespecttotheantennastandoffdistance.
| antennaarrayatanangleof2◦ |     |     | withrespecttothewallsurface |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.8showstherangeprofilesofthefirstsixSCs.Therange
toproduceamultidimensionalwallsubspace.UsingSVD,we
|                                      |     |     |     |     |     |     | profiles | depicted | in Fig.       | 8(a) | and (b) show    | that | the      | first two |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | -------- | -------- | ------------- | ---- | --------------- | ---- | -------- | --------- |
| decomposethesignalmatrixΦintoasetofN |     |     |     |     | SCs |     |          |          |               |      |                 |      |          |           |
|                                      |     |     |     |     |     |     | SCs      | span the | wall subspace |      | as the distance | of   | the main | peak      |
(cid:7)N
|     |        |     |     |     |     |      | of their | associated | range | profiles | is less | than the | wall | standoff |
| --- | ------ | --- | --- | --- | --- | ---- | -------- | ---------- | ----- | -------- | ------- | -------- | ---- | -------- |
|     | Φ=Φ +Φ | +Φ  | =   | σ u | vH  | (25) |          |            |       |          |         |          |      |          |
w t wt i i i distance.TherangeprofilesinFig.8(c)and(d)associatedwith
i=1
|     |     |     |     |     |     |     | the | third and | fourth SCs | have | peaks beyond | the | wall | standoff |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ---- | ------------ | --- | ---- | -------- |
where Φ is the signal matrix comprising the interactions distance;theseSCsspanthetargetsubspace.Thesmalldiffer-
wt
betweenthewallandthetarget(s).Fig.7illustratestheformed ence between the location of the peak in the range profile and
images of the two targets behind the wall. Fig. 7(a) shows the the actual target range is due to the wall attenuation. Fig. 8(e)
image formed by using all N SCs in (25). Clearly, the wall presents the range profiles of the fifth SC (5th-SC), indicating
reflectionsandringingeffectsdominatetheimageandobscure thatsomeweakwallreflectionsresideinthisSC.Fig.9presents
thetargets.Fig.7(b)presentstheimageafterremovingthefirst images obtained from a subset of selected SCs. The image
leading SC, and Fig. 7(c) shows the image without the first in Fig. 9(a) is reconstructed from the 5th-SC only, and that
twodominantSCs.DiscardingjustthefirstdominantSCelim- depicted in Fig. 9(b) is obtained from the following subset
inatesmostofthewallreflections andtheringingeffects.The of SCs: 3rd-SC, 4th-SC, and 6th-SC. The simulation results
target image in Fig. 7(c) is further enhanced by removing the show that, apart from the first few dominant singular vectors,
secondSC. there are other nondominant singular vectors that capture the
Since the antenna array is not parallel to the wall surface, wall returns. Although the nondominant wall singular vectors
thewallsubspaceisspannedbyseveralsingularvectors.After interleavewiththetargetsingularvectors,theirassociatedrange
the removal of the dominant SCs, the radar signal can still profiles can be used to identify them. In the next section, we
contain some wall residuals. These remaining wall returns are proposeatechniquetoestimatethewallsubspaceandintroduce
capturedbysingularvectorsassociatedwithnondominantsin- a subspace projection method for mitigating the wall returns
gularvalues,whichinterleavewiththetargetsingularvalues.To fromtheradarsignals.

TIVIVEetal.:SUBSPACEPROJECTIONAPPROACHFORWALLCLUTTERMITIGATIONINTWRI 2115
∈[0,σ
|     |     |     |     |     |     |     |     | is[0,σ   | ].Givenathresholdδ |             |      |        | ],thesingularvalue |        |       |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------------ | ----------- | ---- | ------ | ------------------ | ------ | ----- |
|     |     |     |     |     |     |     |     | max      |                    |             |      |        | max                |        |       |
|     |     |     |     |     |     |     |     | spectrum | can be             | partitioned | into | two    | classes:           | C ={σ  | ≥δ}   |
|     |     |     |     |     |     |     |     |          |                    |             |      |        |                    | w      | i     |
|     |     |     |     |     |     |     |     | C        | ={σ <δ}.           |             |      |        |                    |        |       |
|     |     |     |     |     |     |     |     | and t    | i                  | Here,       | we   | employ | Otsu’s             | method | [30], |
(cid:11)
|     |     |     |     |     |     |     |     | which computes |     | the optimum | threshold |     | δ by maximizing |     | the |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | --------- | --- | --------------- | --- | --- |
between-classvariance
|     |     |     |     |     |     |     |     |              | =P   |                            | −μ )2+P       |     | −μ                 | )2   |          |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | -------------------------- | ------------- | --- | ------------------ | ---- | -------- |
|     |     |     |     |     |     |     |     |              | Σ 0  | w (μ                       | w 0           |     | t (μ t             | 0    | (30)     |
|     |     |     |     |     |     |     |     | whereP       | andP | aretheclassprobabilities,μ |               |     |                    | andμ |          |
|     |     |     |     |     |     |     |     |              | w    | t                          |               |     | w                  |      | t arethe |
|     |     |     |     |     |     |     |     | class means, | and  | μ is                       | the totalmean |     | of the classes.For |      | more     |
0
|     |     |     |     |     |     |     |     | details | on how to | determine | the | optimum | threshold | of  | Otsu’s |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --------- | --- | ------- | --------- | --- | ------ |
method,theinterestedreaderisreferredtoAppendixA.
Fig.9. ImagesformedusingasubsetofSCs:(a)Imageobtainedfromthe Then, (27) is used to compute the range profiles associated
5th-SC only and (b) image obtained from the combination of these SCs: with the singular values in the class C . Let h denote the
|     |     |     |     |     |     |     |     |     |     |     |     |     | w   | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3rd-SC,4th-SC,and6th-SC.
|     |     |     |     |     |     |     |     | distance | of the main | peak | in the | range | profile | associated | with |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ---- | ------ | ----- | ------- | ---------- | ---- |
IV. WALLCLUTTERMITIGATIONMETHOD the ith singular value belonging to the wall. The wall range η
Theproposedwallcluttermitigationmethodisbasedonthe canbeestimatedas
assumptionthatthewallreturnsarerelativelystrongerthanthe
|                                                           |     |     |     |     |     |     |     |     |     |     | η =max(h | i ). |     |     | (31) |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | --- | --- | ---- |
| targetreturns,andtheyresideinseparatesubspaces.Therefore, |     |     |     |     |     |     |     |     |     |     | i        |      |     |     |      |
SVDisusedtodecomposethesignalmatrixΦasfollows:
Fromtheestimatedwallrange,wecannowidentifytheremain-
|     | (cid:7) |         | (cid:7) |         | (cid:7) |     |         |          |         |           |     |          |         |          |     |
| --- | ------- | ------- | ------- | ------- | ------- | --- | ------- | -------- | ------- | --------- | --- | -------- | ------- | -------- | --- |
|     |         |         |         |         |         |     |         | ing wall | SCs and | determine | the | singular | vectors | spanning | the |
| Φ=  |         | σ u vH+ |         | σ u vH+ |         | σ u | vH (28) |          |         |           |     |          |         |          |     |
|     |         | i i     | i       | i i     | i       | i i | i       |          |         |           |     |          |         |          |     |
wallsubspace.Weclassifyasingularvectorspanningthewall
|     | i∈W |     | i∈T |     | i∈N |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
subspacewhenthemainpeakofitsassociatedrangeprofileis
whereW,T,andN
arethesetsofindicesforwall,target,and
locatedinsidethewallrangeη.Thisclassificationisperformed
noisesingularvectors,respectively.However,notallwallSCs
onallSCsofΦ,andtheindicesofthewallsingularvectorsare
| will be | associated | with | the | dominant | singular | values. | While | it  |     |     |     |     |     |     |     |
| ------- | ---------- | ---- | --- | -------- | -------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
storedintheindexsetW.
| is expected | that      | the strong | wall    | reflections |     | will be  | represented |     |     |     |     |     |     |     |     |
| ----------- | --------- | ---------- | ------- | ----------- | --- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| by the      | first few | singular   | vectors | associated  |     | with the | dominant    |     |     |     |     |     |     |     |     |
B. WallClutterMitigation
| singular   | values, | some          | weak | components | of       | the        | wall returns |       |             |     |                |     |           |     |          |
| ---------- | ------- | ------------- | ---- | ---------- | -------- | ---------- | ------------ | ----- | ----------- | --- | -------------- | --- | --------- | --- | -------- |
| may reside |         | in a subspace |      | spanned    | by other | singular   | vectors      |       |             |     |                |     |           |     |          |
|            |         |               |      |            |          |            |              | After | identifying | the | wall subspace, |     | we remove |     | the wall |
| associated | with    | nondominant   |      | singular   | values.  | Therefore, | we           |       |             |     |                |     |           |     |          |
returnsbyprojectingtheradarsignalsontothesubspaceorthog-
| propose | a method | for | estimating | the | wall | subspace, | followed |     |     |     |     |     |     |     |     |
| ------- | -------- | --- | ---------- | --- | ---- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
onaltothewallsubspace.Similarly,thenoisecanberemoved
byasubspaceprojectionmethodformitigatingthewallreturns
|     |     |     |     |     |     |     |     | by projecting | the | radar | signals | onto the | subspace | orthogonal |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----- | ------- | -------- | -------- | ---------- | --- |
fromtheradarsignals.
tothenoisesubspace.First,theradarsignalispreprocessedto
(cid:12)
removethecommonsignalacrossthearrayaperture.LetΦbe
A. WallSubspaceEstimation
thematrixobtainedaftersubtractingthemeanvectorfromeach
| Theproposedestimationmethodforwallsubspaceisbased |     |     |     |     |     |     |     | columnofΦ |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
ontheassumptionthatthestrongreflectionsfromthefrontand
(cid:12)
backofthewallarecapturedbythefirstfewdominantSCs.In Φ =Φ−meT (32)
[29],asimilarassumptionwasmadetoestimatethetimedelay
|     |     |     |     |     |     |     |     | wheremisthemeanofthecolumnsofΦandeT |     |     |     |     |     | =[1,...,1], |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | ----------- | --- |
ofultrawidebandradarsignalsbackscatteredfromawall.First,
(cid:12)
we estimate the wall range, i.e., the distance from the antenna e∈RN.UsingSVD,wedecomposethematrixΦ as
tothebackofthewallfromtherangeprofilesofthedominant (cid:12) (cid:12) (cid:12) (cid:12)H
|            |     |             |     |           |     |      |              |     |     |     | Φ =U | Σ V |     |     | (33) |
| ---------- | --- | ----------- | --- | --------- | --- | ---- | ------------ | --- | --- | --- | ---- | --- | --- | --- | ---- |
| SCs. Then, |     | we classify | the | remaining | SCs | into | the wall and |     |     |     |      |     |     |     |      |
target classes based on their range profiles. The indices of the (cid:12) =[u(cid:12) ,...,u(cid:12) (cid:12) =[v(cid:12) ,...,v(cid:12) (cid:12) =σ(cid:12)
|          |         |         |     |          |     |        |              | where U | 1         |         | M ], V | 1        | N ],        | and Σ   | i,i i . |
| -------- | ------- | ------- | --- | -------- | --- | ------ | ------------ | ------- | --------- | ------- | ------ | -------- | ----------- | ------- | ------- |
| singular | vectors | forming | the | wall SCs | are | stored | in the index |         |           |         |        |          |             |         |         |
|          |         |         |     |          |     |        |              | Summing | the outer | product | of     | the pair | of singular | vectors | in      |
setW.Letηdenotethewallrange.Whenthestandoffdistance
|     |     |     |     |     |     |     |     | theindexsetW |     | generatesthewallsubspace,whichisgivenby |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------------------------------------- | --- | --- | --- | --- | --- |
z and the wall thickness d are known, the wall range can be (cid:7)
a
| approximatedas |     |     |     |     |     |     |     |     |     |     |     | u(cid:12) v(cid:12)H. |     |     |      |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | ---- |
|                |     |     |     |     |     |     |     |     |     | P   | =   |                       |     |     | (34) |
|                |     |     |     | √   |     |     |     |     |     |     | w   | i i                   |     |     |      |
i∈W
|     |     |     | η ≈(d | (cid:4)+z | ).  |     | (29) |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | --------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
a
Thesubspaceorthogonaltothewallsubspaceiscomputedas
| In practice,                                           |     | the exact | values | of the | wall | parameters | are not |     |     |     |      |     |     |     |      |
| ------------------------------------------------------ | --- | --------- | ------ | ------ | ---- | ---------- | ------- | --- | --- | --- | ---- | --- | --- | --- | ---- |
| readilyavailable.Therefore,wedeterminethewallrangefrom |     |           |        |        |      |            |         |     |     |     | ⊥    |     |     |     |      |
|                                                        |     |           |        |        |      |            |         |     |     | P   | =I−P | PH  |     |     | (35) |
|                                                        |     |           |        |        |      |            |         |     |     |     | w    | w   | w   |     |      |
therangeprofilesassociatedwiththedominantsingularvectors.
To determine the leading singular vectors associated with the where I denotes the identity matrix. To mitigate the wall
wall, we apply a threshold technique to segment the singular (cid:12)
|     |     |     |     |     |     |     |     | returns,thematrixΦ |     | isprojectedontotheorthogonalsubspace |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------------------------------------ | --- | --- | --- | --- | --- |
valuespectrumintotwoclasses,oneofwhichisthedominant
|     |     |     |     |     |     |     |     |     |     |     | (cid:11) | ⊥(cid:12) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --- | --- | --- |
wallsingularvalues.Supposethattherangeofsingularvalues Φ=P Φ. (36)
w

2116 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.53,NO.4,APRIL2015
(cid:11)
| The resulting |          | matrix     | Φ is | further | processed | to       | remove |     |     |     |     |     |     |     |     |
| ------------- | -------- | ---------- | ---- | ------- | --------- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| noise. The    | subspace | orthogonal |      | to the  | noise     | subspace | can be |     |     |     |     |     |     |     |     |
expressedas
|     |     |     | ⊥ =I−P | PH  |     |     |      |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | P   |        | n   |     |     | (37) |     |     |     |     |     |     |     |     |
|     |     |     | n      | n   |     |     |      |     |     |     |     |     |     |     |     |
(cid:8)
u(cid:11) v(cid:11)H
| where P | n = | i∈N i | is the | noise | subspace. | The | pair of |     |     |     |     |     |     |     |     |
| ------- | --- | ----- | ------ | ----- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
i
| left and | right singular | vectors, |     | i.e., u(cid:11) and | v(cid:11), | is obtained | from |     |     |     |     |     |     |     |     |
| -------- | -------------- | -------- | --- | ------------------- | ---------- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:11)
theSVDofΦ.Sincenoiseischaracterizedbysingularvectors
associatedwithsmallsingularvalues,thereareseveralmethods Fig. 10. Images before and after wall clutter mitigation: (a) Image formed
to determine the noise subspace. Akaike information criterion without wall clutter mitigation, (b) image obtained after using background
subtraction,and(c)imageobtainedwiththeproposedmethod.
(AIC)andminimumdescriptionlength(MDL)methodsaretwo
| commonly | used | methods | to estimate | the | noise | subspace | [15]. |     |     |     |       |     |     |     |     |
| -------- | ---- | ------- | ----------- | --- | ----- | -------- | ----- | --- | --- | --- | ----- | --- | --- | --- | --- |
|          |      |         |             |     |       |          |       |     |     |     | TABLE | I   |     |     |     |
TheAICisgivenby IFOFTHEIMAGEPRODUCEDBYTHEPROPOSEDSUBSPACEPROJECTION
(cid:13)(cid:13) (cid:4) (cid:4) METHODA N D T H E B A S IC S V D -B A S E D M E T H O D W I T H T H E REMOVAL
|     |     |     | (cid:8) |     | M−i |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
M O F D O M IN A N T S C S, T ES T E D O N S Y N T H ET I C D A T A
|             |     | 1     |          | σ   |          |     |      |     |     |     |     |     |     |     |     |
| ----------- | --- | ----- | -------- | --- | -------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|             |     | (M−i) | m=i+1    | m   |          |     |      |     |     |     |     |     |     |     |     |
| AIC(i)=Nlog |     |       | (cid:14) |     | +(2M−i)i |     | (38) |     |     |     |     |     |     |     |     |
M
σ m
m=i+1
(cid:11)
| where σ | is the | ith singular | value | of Φ. | Similarly, | the | MDL | is  |     |     |     |     |     |     |     |
| ------- | ------ | ------------ | ----- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i
givenby
|             |     | (cid:13)(cid:13) | (cid:4)  |       | (cid:4) |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ---------------- | -------- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|             |     |                  | (cid:8)  |       | M−i     |     |     |     |     |     |     |     |     |     |     |
|             |     |                  | 1        | M σ   |         |     |     |     |     |     |     |     |     |     |     |
|             |     | (M−i)            |          | m=i+1 | m       |     |     |     |     |     |     |     |     |     |     |
| MDL(i)=Nlog |     |                  | (cid:14) |       |         |     |     |     |     |     |     |     |     |     |     |
M
|            |     |            |        | σ         |             |           |          |                 |                  |              | (cid:8)    |             |              |         |               |
| ---------- | --- | ---------- | ------ | --------- | ----------- | --------- | -------- | --------------- | ---------------- | ------------ | ---------- | ----------- | ------------ | ------- | ------------- |
|            |     |            | m      | =i + 1 m  |             |           |          |                 | P =              | ( 1 / N      | )          | | I         | ( x , z) | 2 | P       | = (1 /N )     |
|            |     |            |        | 1         |             |           |          | w (cid:8) h e r | e 0              |              | t          | ∈ 0         |              | ,       | j t           |
|            |     |            |        | + ( 2M    | −i)log(N)i. |           | (39)     |                 |                  |              | (x, z      | ) A t       |              |         |               |
|            |     |            |        |           |             |           |          |                 | | I              | (x , z ) |2, | and I      | ( x , z )   | a n d I      | ( x,z ) | d eno te th e |
|            |     |            |        | 2         |             |           |          | ( x ,           | z)∈At j          |              |            | 0           | j            |         |               |
|            |     |            |        |           |             |           |          | formed          | image            | after        | background | subtraction |              | and     | the formed    |
| The number | of  | singular   | values | belonging | to          | the noise | class    | is              |                  |              |            |             |              |         |               |
|            |     |            |        |           |             |           |          | image           | after removing   |              | the first  | j dominant  |              | SCs     | from the      |
| determined | by  | minimizing | the    | AIC or    | MDL.        | Once      | the wall |                 |                  |              |            |             |              |         |               |
|            |     |            |        |           |             |           |          | matrix          | Φ, respectively. |              | Fig. 10    | shows       | images       | formed  | by DS         |
Φ¯,
| and noise | subspaces | are | computed, | the | new | matrix | which |             |     |        |           |              |             |     |         |
| --------- | --------- | --- | --------- | --- | --- | ------ | ----- | ----------- | --- | ------ | --------- | ------------ | ----------- | --- | ------- |
|           |           |     |           |     |     |        |       | beamforming |     | before | and after | wall clutter | mitigation. |     | Without |
containsthetargetreflections,iswrittenas
(cid:13) (cid:4) wall clutter mitigation, Fig. 10(a) shows an image with strong
|     |     | Φ¯  | ⊥   | ⊥ (cid:12) | (cid:12) |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
=P P Φ =P Φ (40) clutter.Withbackgroundsubtraction,theformedimageshown
|     |     |     | n   | w   | t   |     |     |         |       |         |         |          |              |     |             |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ------- | ------- | -------- | ------------ | --- | ----------- |
|     |     |     |     |     |     |     |     | in Fig. | 10(b) | is free | of wall | clutter; | both targets |     | are clearly |
=P⊥P⊥ visible. However, in practice, it is difficult to have access to
| where P |     | is the | target | subspace | projection |     | operator. |     |     |     |     |     |     |     |     |
| ------- | --- | ------ | ------ | -------- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
|         | t n | w      |        |          |            |     |           |     |     |     |     |     |     |     |     |
Finally,DSbeamformingisappliedtosignalsofΦ¯ toforman the measurements of the background scene devoid of targets.
|     |     |     |     |     |     |     |     | Fig. | 10(c) depicts | the | image | obtained | with | the | proposed |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------- | --- | ----- | -------- | ---- | --- | -------- |
imageofthescene.
Theproposedmethodisinitiallytestedonthesimulateddata method,wherethewallclutterismarkedlysuppressed.TableI
obtained from the scene with two dihedrals placed behind a liststheIFandtheTPRoftheformedimagesafterwallclutter
|             |       |     |         |                 |     |     |          | mitigation. | Background |     | subtraction |     | obtains | the | highest IF |
| ----------- | ----- | --- | ------- | --------------- | --- | --- | -------- | ----------- | ---------- | --- | ----------- | --- | ------- | --- | ---------- |
| homogeneous | wall. | To  | measure | the performance |     | of  | the wall |             |            |     |             |     |         |     |            |
cluttermitigationmethod,wecomputetheimprovementfactor of 11.14 dB, followed by the proposed subspace projection
methodwithanIFof10.09dB.IntermsofTPR,theproposed
(IF)intermsofthetarget-to-clutterratio(TCR)
(cid:5) (cid:6) methodachievesaTPRof−3.06dB.WhenthedominantSCs
TCR
|     |     |          |     |     | o   |     |      | are removed                                          |     | without | the use | of the | proposed | wall | subspace |
| --- | --- | -------- | --- | --- | --- | --- | ---- | ---------------------------------------------------- | --- | ------- | ------- | ------ | -------- | ---- | -------- |
|     |     | IF=10log |     |     |     |     | (41) |                                                      |     |         |         |        |          |      |          |
|     |     |          |     | TCR |     |     |      | estimationmethod,theIFsoftheformedimagesarepresented |     |         |         |        |          |      |          |
i
|           |         |         |         |              |            |        |         | as follows.                                         | After | the | removal | of the | dominant | SC  | from the |
| --------- | ------- | ------- | ------- | ------------ | ---------- | ------ | ------- | --------------------------------------------------- | ----- | --- | ------- | ------ | -------- | --- | -------- |
| where TCR | and     | TCR     | are the | TCRs         | of the     | formed | image   |                                                     |       |     |         |        |          |     |          |
|           | o       |         | i       |              |            |        |         | matrixΦ,theIFoftheformedimageis4.89dB.Discardingthe |       |     |         |        |          |     |          |
| with and  | without | the use | of a    | wall clutter | mitigation |        | method, |                                                     |       |     |         |        |          |     |          |
firsttwoleadingSCsimprovestheIFoftheimageto9.98dB.
respectively.TheTCRofaradarimageiscalculatedas
However,whenweremovethefirstthreeSCsfromthematrix
(cid:8)
|I(x,z)|2 Φ, the IF of the formed images decreases slightly to 7.32 dB.
1
Nt (cid:8)(x,z)∈At
TCR= (42) The TPR of the formed target image also decreases markedly
|         |          |                | 1           | |I(x,z)|2  |         |        |         |                                 |          |          |      |                    |     |           |     |
| ------- | -------- | -------------- | ----------- | ---------- | ------- | ------ | ------- | ------------------------------- | -------- | -------- | ---- | ------------------ | --- | --------- | --- |
|         |          |                | Nc (x,z)∈Ac |            |         |        |         | whendiscardingthefirstthreeSCs. |          |          |      |                    |     |           |     |
|         |          |                |             |            |         |        |         | So                              | far, the | proposed | wall | clutter mitigation |     | technique | has |
| where A | t is the | target region, |             | A c is the | clutter | region | defined |                                 |          |          |      |                    |     |           |     |
beenappliedtoanoiselessTWRIscene.Theproposedmethod
| as the entire | image   | excluding |        | the target     | region, | and    | N and    |            |        |       |           |       |         |       |          |
| ------------- | ------- | --------- | ------ | -------------- | ------- | ------ | -------- | ---------- | ------ | ----- | --------- | ----- | ------- | ----- | -------- |
|               |         |           |        |                |         |        | c        | is further | tested | under | different | noise | levels, | where | the sim- |
| N are the     | numbers | of        | pixels | in the clutter | and     | target | regions, |            |        |       |           |       |         |       |          |
t
|               |     |         |        |        |       |             |     | ulated | radar signals | are          | corrupted | by  | additive     | white | Gaussian  |
| ------------- | --- | ------- | ------ | ------ | ----- | ----------- | --- | ------ | ------------- | ------------ | --------- | --- | ------------ | ----- | --------- |
| respectively. | The | quality | of the | target | image | is measured |     | in     |               |              |           |     |              |       |           |
|               |     |         |        |        |       |             |     | noise. | The IF        | of the image | formed    | by  | the proposed |       | method is |
termsofthetargetpowerratio(TPR)givenby
computedasafunctionoftheSNRoftheinputsignal.Fig.11
P
j illustrates the variations in the IF of the formed image as a
|     |     |     | TPR= |     |     |     | (43) |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
P function of the SNR of the input signal. The IF of the formed
0

TIVIVEetal.:SUBSPACEPROJECTIONAPPROACHFORWALLCLUTTERMITIGATIONINTWRI 2117
Fig.11. IFoftheimageasafunctionoftheSNRoftheinputradarsignal.
Fig.12. ExamplesofimagesobtainedfrominputsignalofdifferentSNRs:
(a)ImagesformedusinginputsignalwithSNRof20dBand(b)imageformed
usinginputsignalwithSNRof40dB.
| image remains | unchanged            | until the SNR          | of the       | input signal |     |     |     |     |     |
| ------------- | -------------------- | ---------------------- | ------------ | ------------ | --- | --- | --- | --- | --- |
| decreases     | to 40 dB.            | Fig. 12 shows examples | of           | radar images |     |     |     |     |     |
| obtained      | from input           | signal with SNRs       | of 20 and    | 40 dB. In    |     |     |     |     |     |
| the next      | section, the         | subspace projection    | method       | is evaluated |     |     |     |     |     |
| on real       | radar data collected | from a                 | ground-based | stepped-     |     |     |     |     |     |
frequencyTWRIsystem.
V. EXPERIMENTALRESULTS
RealradarsignalsarecollectedintheRadarImagingLabora-
toryoftheCenterforAdvancedCommunicationsatVillanova
Fig.13. Pictureofthedrywallscene:(a)Imagedepictingtheninetargetsand
University,Villanova,PA,USA.AnAgilentnetworkanalyzer,
(b)theground-truthimage.
ModelENA5017B,isusedtoimplementastepped-frequency
| waveform | for synthesizing | 1-D and 2-D | array | apertures. | A   |     |     |     |     |
| -------- | ---------------- | ----------- | ----- | ---------- | --- | --- | --- | --- | --- |
7.62 by 7.62 meter room with pyramidal foam and laminated fromtheconcretewall,andadihedralisplacedat2.1mbehind
polyurethane foam sheet absorbers on the side and back walls the wall. An array aperture of length 1.2446 m is synthesized
is constructed for imaging. For more details about the room with 0.0222-m interelement spacing, and a stepped-frequency
signalcovering0.7–3.1-GHzfrequencybandisusedtointerro-
settingandthespecificationoftheradarsystem,theinterested
readerisreferredto[6]. gatethescene.Thesecondscenarioinvolvesascenepopulated
withninetargetsofdifferentradarcrosssections(RCSs)placed
behindthedrywall.Fig.13showsapictureofthesecondscene
A. ExperimentalSetup
|     |     |     |     |     | and its ground | truth. The nine | targets in | the second scene | are |
| --- | --- | --- | --- | --- | -------------- | --------------- | ---------- | ---------------- | --- |
For evaluation purposes, 1-D and 2-D synthesized array three dihedrals, four trihedrals, a sphere, and a top hat. Each
apertures are used for 2-D and 3-D TWRIs, respectively. Fur- target is located at a certain height and position, as shown
thermore, two different TWRI scenarios are designed using in Fig. 13(a). Its location within the scene is given in the
two types of walls: a 0.14-m-thick solid concrete wall and a ground-truthimagedepictedinFig.13(b).A69-antennaarray
0.127-m-thick hollow drywall. The drywall is built from a of length 1.5 m is used to interrogate the scene. The stepped-
woodenframe,whichisfastenedwith0.019-mplywoodonone frequencysignalhasabandwidthof1GHzcenteredat2.5GHz.
side and 0.016-m gypsum wallboard on the other side. In the TableIIliststhecharacteristicsofthereflectorsusedinthetwo
| firstscenario,theradarisplacedatastandoffdistanceof1.16m |     |     |     |     | TWRIscenes. |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |

2118 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.53,NO.4,APRIL2015
|     |     |     | TABLE | II  |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
REFLECTORSUSEDINTHETWRIEXPERIMENTS
B. Two-DimensionalTWRI
| A line    | array  | aperture   | is  | synthesized  |     | for the previously |       |     |     |     |     |     |
| --------- | ------ | ---------- | --- | ------------ | --- | ------------------ | ----- | --- | --- | --- | --- | --- |
| described | scenes | to perform |     | 2-D imaging. |     | Before DS          | beam- |     |     |     |     |     |
forming,fourdifferentmethodsareusedforwallcluttermitiga-
tion:backgroundsubtraction,timegating,spatialfiltering,and
| B-scan-based | SVD         | methods |       | [12]–[15].  | In  | [12]–[14], SVD | is  |     |     |     |     |     |
| ------------ | ----------- | ------- | ----- | ----------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
| applied to   | the B-scan, |         | which | is obtained | by  | applying IFFT  | on  |     |     |     |     |     |
thespace-frequencymeasurements.Thefirstandseconddom-
| inant SCs     | are assumed |       | to contain | the     | wall      | and target returns, |        |     |     |     |     |     |
| ------------- | ----------- | ----- | ---------- | ------- | --------- | ------------------- | ------ | --- | --- | --- | --- | --- |
| respectively. | In          | [15], | SVD is     | used to | decompose | the                 | formed |     |     |     |     |     |
imageintoasetofeigenimages.Forwallcluttermitigation,the
| first dominant | eigenimage |     | is  | discarded. | Then, | an information |     |     |     |     |     |     |
| -------------- | ---------- | --- | --- | ---------- | ----- | -------------- | --- | --- | --- | --- | --- | --- |
theoreticcriteriamethodisusedtodeterminetheeigenimages
| spanning        | the target | subspace.      |     | In time  | gating,     | the stepped- |       |     |     |     |     |     |
| --------------- | ---------- | -------------- | --- | -------- | ----------- | ------------ | ----- | --- | --- | --- | --- | --- |
| frequency       | signal     | is transformed |     | into     | a range     | profile.     | Based |     |     |     |     |     |
| on the standoff |            | distance       | and | the wall | parameters, | the          | radar |     |     |     |     |     |
returnscorrespondingtothewallregionaresettozero,andthe
| range profile | is  | converted | back | to the | frequency | domain. | For |     |     |     |     |     |
| ------------- | --- | --------- | ---- | ------ | --------- | ------- | --- | --- | --- | --- | --- | --- |
backgroundsubtraction,radarsignalsfromanemptyscenede-
voidoftarget(s)aresubtractedfromtheradarsignalsreceived
fromthescenepopulatedwithtarget(s)beforeDSbeamforming
| is applied | to reconstruct |     | the | image. | Background | subtraction |     |     |     |     |     |     |
| ---------- | -------------- | --- | --- | ------ | ---------- | ----------- | --- | --- | --- | --- | --- | --- |
represents an ideal scenario, where access to the background Fig.14. Imageoftheconcretewallsceneobtainedusingdifferentwallclutter
|          |            |      |        |          |     |                 | mitigation | methods: | (a) No wall clutter | mitigation, | (b) background | subtrac- |
| -------- | ---------- | ---- | ------ | -------- | --- | --------------- | ---------- | -------- | ------------------- | ----------- | -------------- | -------- |
| scene is | available; | this | is not | possible | in  | real scenarios. | In         |          |                     |             |                |          |
tion,(c)timegating,(d)spatialfiltering,(e)image-basedSVDmethod,and
spatialfiltering,aninfinite-impulse-responsenotchfilterisused
(f)proposedsubspaceprojectionmethod.
toremovezerofrequencycomponent.Thefrequencyresponse
ofthenotchfilterisdefinedas
|     |     |     |     |     |     |     | suppress | the wall | clutter because | the wall | reverberations | and |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --------------- | -------- | -------------- | --- |
1−exp(−jω)
targetreflectionshighlyoverlapinthetimedomain.Theimage
|     |     | H(jω)= |     |     |     |     | (44) |     |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
1−aexp(−jω)
inFig.14(d)showsthatspatialfilteringiseffectiveinremoving
|     |     |     |     |     |     |     | the wall | reflections | without | significantly | compromising | the |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ------- | ------------- | ------------ | --- |
where ω is the angular frequency and a(<1) is a positive target image. The image-based SVD method [15] produces an
constant denoting the width of the filter notch. In our experi- imagewheremostofthewallclutterissuppressedbuttheshape
ments,wedefineaatthepointofachievingmaximumIF.The ofthetargetisdistortedcomparedtothatshowninFig.14(b),
concretewallscene,whichhasadihedral,isilluminatedbythe obtainedusingbackgroundsubtraction.Fig.14(f)illustratesthe
synthesizedarrayaperture,producingasignalmatrixΦofsize image produced by the proposed subspace projection method.
801 × 57, i.e., 801 frequencies and 57 antennas. All five wall This image does not contain the wall clutter and is as clear as
cluttermitigationapproaches,includingtheproposedsubspace thatofthespatialfilteringmethod.Fig.15depictsthewalland
projection method, are used to suppress the wall clutter in the targetsingularvaluesidentifiedbytheproposedwallsubspace
formedimage. estimation method. The singular values depicted in Fig. 15(a)
Fig. 14 illustrates images before and after wall clutter and (b) belong to the wall and target, respectively. From
mitigation, using different wall mitigation methods. With the Fig. 15(a), we can see that the wall subspace comprises the
availabilityofthebackgroundmeasurements,backgroundsub- firsttwodominantSCsandcomponents5,23,24,and25.Itis
traction produces a clear image [Fig. 14(b)] in which most of clearfromFig.15(a)thatthenondominantwallsingularvalues
thewallandbackgroundclutterisremoved.Withtimegating, interleavewiththetargetsingularvalues.TableIIIpresentsthe
the formed image contains strong wall clutter; see Fig. 14(c). IF in terms of TCR of the wall clutter mitigation methods for
Eventhoughthetargetisfarfromthewall,timegatingcannot theimagesshowninFig.14.Backgroundsubtractionachieves

TIVIVEetal.:SUBSPACEPROJECTIONAPPROACHFORWALLCLUTTERMITIGATIONINTWRI 2119
Fig.15. Singularvaluespectrumof(a)thewalland(b)thetargetsubspaces
asidentifiedbytheproposedwallsubspaceestimationmethodforthescene
withadihedralbehindtheconcretewall.
|     |     |     | TABLE | III |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
IFOFTHEWALLMITIGATIONMETHODSTESTEDONRADAR
DATACOLLECTEDFROMTHECONCRETEWALLSCENE
thehighestIFof16.16dB,followedbytheproposedsubspace
| projection | method | with     | an IF  | of 11.01 | dB.      | Spatial          | filtering |     |     |     |     |     |
| ---------- | ------ | -------- | ------ | -------- | -------- | ---------------- | --------- | --- | --- | --- | --- | --- |
| gives an   | IF of  | 8.26 dB. | Among  | the SVD  | methods, | the              | image-    |     |     |     |     |     |
| based SVD  | method | gives    | better | result   | than     | the B-scan-based |           |     |     |     |     |     |
SVDmethodasitassumesthatthetargetreflectionsresideina
multidimensionalsubspace.
| For the    | drywall    | scene,  | Fig.    | 16 depicts  | the         | formed | images   |     |     |     |     |     |
| ---------- | ---------- | ------- | ------- | ----------- | ----------- | ------ | -------- | --- | --- | --- | --- | --- |
| before and | after      | wall    | clutter | mitigation. | Without     | any    | prepro-  |     |     |     |     |     |
| cessing,   | Fig. 16(a) | depicts | an      | image       | with strong | wall   | clutter. |     |     |     |     |     |
Withtheavailabilityofanemptyscene,backgroundsubtraction
| produces        | a clear   | radar       | image       | [Fig. 16(b)]. |                    | Time gating | and    |     |     |     |     |     |
| --------------- | --------- | ----------- | ----------- | ------------- | ------------------ | ----------- | ------ | --- | --- | --- | --- | --- |
| spatial         | filtering | fail to     | remove      | the           | wall contributions |             | from   |     |     |     |     |     |
| the radar       | data      | [Fig. 16(c) | and         | (d)].         | The SVD            | methods     | can    |     |     |     |     |     |
| hardly suppress |           | the wall    | clutter     | in the        | formed             | radar       | image. |     |     |     |     |     |
| This is         | because   | the wall    | reflections | are           | assumed            | to          | reside | in  |     |     |     |     |
thefirstSConly.However,thereflectionsbackscatteredfroma
| heterogeneous |                 | wall span | a multidimensional |        |             | subspace | space,   |                     |                |                          |                 |              |
| ------------- | --------------- | --------- | ------------------ | ------ | ----------- | -------- | -------- | ------------------- | -------------- | ------------------------ | --------------- | ------------ |
|               |                 |           |                    |        |             |          |          | Fig. 16. Image      | of the drywall | scene obtained           | using different | wall clutter |
| as described  | in              | Section   | III-B.             | Fig.   | 16(e) shows | the      | output   |                     |                |                          |                 |              |
|               |                 |           |                    |        |             |          |          | mitigation methods: | (a) No         | wall clutter mitigation, | (b) background  | subtrac-     |
| image of      | the image-based |           | SVD                | method | with        | AIC;     | only the |                     |                |                          |                 |              |
tion,(c)timegating,(d)spatialfiltering,(e)image-basedSVDmethod,and
| targets | with large | RCS | are barely | visible. | The | B-scan-based |     |     |     |     |     |     |
| ------- | ---------- | --- | ---------- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
(f)proposedsubspaceprojectionmethod.
| SVD methods |     | perform | poorly | because | the | wall subspace |     | is  |     |     |     |     |
| ----------- | --- | ------- | ------ | ------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
TABLE IV
assumedtobe1-D.Fig.16(f)showstheimageobtainedusing
IFOFWALLMITIGATIONMETHODSBASEDONTHESCENE
the proposed wall clutter mitigation method, where most of WITHNINETARGETSBEHINDTHEDRYWALL
| the wall  | clutter | is significantly |     | suppressed. |     | Table IV | lists the |     |     |     |     |     |
| --------- | ------- | ---------------- | --- | ----------- | --- | -------- | --------- | --- | --- | --- | --- | --- |
| IF of the | images  | presented        | in  | Fig. 16.    | The | proposed | method    |     |     |     |     |     |
achievesthesecondhighestIFof22.35dB.TheB-scan-based
SVDmethoddescribedin[14]givesthelowestIFof2.08dB.
Theexperimentalresultsdemonstratethattheproposedmethod
| can be as   | effective | as          | background | subtraction |               | in removing | the       |     |     |     |     |     |
| ----------- | --------- | ----------- | ---------- | ----------- | ------------- | ----------- | --------- | --- | --- | --- | --- | --- |
| clutter due | to both   | homogeneous |            | and         | heterogeneous |             | walls. In |     |     |     |     |     |
thenextsection,weapplytheproposedwallcluttermitigation
methodto3-DTWRI.

2120 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.53,NO.4,APRIL2015
Fig.17. Three-dimensionalimagesoftheconcretewallscene:(a)Beforewallcluttermitigation,aftertheuseof(b)backgroundsubtraction,and(c)theproposed
subspaceprojectionmethod.Forvisualization,the3-Dimagesaredisplayedinlinearscale,andvoxelslessthan−25dBareremoved.
Fig.18. Three-dimensionalimagesofthedrywallsceneaftertheuseof(a)backgroundsubtractionand(b)theproposedsubspaceprojectionmethod.For
visualization,the3-Dimagesaredisplayedinlinearscale,andvoxelslessthan−25dBareremoved.
C. Three-DimensionalTWRI where τ (x,z,y) is the focusing delay from the nth antenna
n
ofthe2-Darrayaperturetothevoxelatlocation(x,z,y).The
| For 3-D | imaging, | the | scene | is scanned |     | by a | 2-D array |     |     |     |     |     |     |     |
| ------- | -------- | --- | ----- | ---------- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
aperture along the horizontal and vertical directions to reveal computationofthetwo-waypropagationdelayfromanantenna
toavoxelisdescribedin[8].
thepropertiesoftargetsresidingbehindthewall,e.g.,theheight
A2-Darrayapertureisusedtointerrogatetheconcretewall
| ofthetarget.ThereceivedmonochromaticsignalsforallM |     |     |     |     |     |     | fre- |             |         |            |     |             |     |              |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | ----------- | ------- | ---------- | --- | ----------- | --- | ------------ |
|                                                    |     |     |     |     |     |     |      | and drywall | scenes. | Background |     | subtraction | and | the proposed |
quenciesateachantennalocationofthe2-Darrayapertureare
Φ∈CM×N, subspace projection method are then applied to mitigate the
| stacked to | form a | column | of signal | matrix |     |     | where |     |     |     |     |     |     |     |
| ---------- | ------ | ------ | --------- | ------ | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
N isthenumberofantennalocationsinthe2-Darrayaperture. wall returns. We should point out that, for the sake of clar-
|           |                |     |              |            |                  |             |            | ity, the        | voxels below        | −25      | dB      | were thresholded |             | in the 3-D  |
| --------- | -------------- | --- | ------------ | ---------- | ---------------- | ----------- | ---------- | --------------- | ------------------- | -------- | ------- | ---------------- | ----------- | ----------- |
| The order | of selecting   |     | the antenna  | locations, |                  | i.e.,       | processing |                 |                     |          |         |                  |             |             |
|           |                |     |              |            |                  |             |            | images.         | Fig. 17 illustrates |          | the 3-D | radar            | images      | of the con- |
| rowwise   | or columnwise, |     | only results |            | in a permutation |             | of the     |                 |                     |          |         |                  |             |             |
|           |                |     |              |            |                  |             |            | crete wall      | scene.              | Applying | DS      | beamforming      | directly    | to the      |
| columns   | of Φ.Itcan     | be  | readily      | shown      | that the         | permutation | of         |                 |                     |          |         |                  |             |             |
|           |                |     |              |            |                  |             |            | space-frequency | measurements        |          |         | produces         | a cluttered | 3-D im-     |
thecolumnsofthematrixΦdoesnotchangethecolumnorder
of the left and right singular vectors, and more importantly, it age [Fig. 17(a)]. Fig. 17(b) shows the image obtained from
backgroundsubtraction,whichdoesnothavewallclutter.The
| does not | affect the | singular | values. | Hence, | the | arrangement | of  |     |     |     |     |     |     |     |
| -------- | ---------- | -------- | ------- | ------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
imageshowninFig.17(c),whichisproducedbytheproposed
| the received | signals    | into | a matrix | Φ does      | not | affect         | the wall |              |            |         |     |          |         |             |
| ------------ | ---------- | ---- | -------- | ----------- | --- | -------------- | -------- | ------------ | ---------- | ------- | --- | -------- | ------- | ----------- |
|              |            |      |          |             |     |                |          | wall clutter | mitigation | method, | is  | as clear | as that | produced by |
| and target   | subspaces. | To   | form     | 3-D images, |     | DS beamforming |          |              |            |         |     |          |         |             |
backgroundsubtraction.Forthedrywallscene,theformedim-
| is applied | to compute |     | the complex | amplitude |     | of  | each voxel |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | ----------- | --------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
I(z,x,y) ages obtained using background subtraction and the proposed
|     |     |     |     |     |     |     |     | method | are shown | in Fig. | 18; | both images | are | free of wall |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | ------- | --- | ----------- | --- | ------------ |
N(cid:7)−1M(cid:7)−1 clutter. Table V presents the IF of the thresholded 3-D images
1
I(x,z,y)= s(m,n)exp(jω τ (x,z,y)) (45) depictedinFigs.17and18.Theproposedsubspaceprojection
|     | NM  |     |     |     | m   | n   |     |        |             |          |     |         |          |            |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | -------- | --- | ------- | -------- | ---------- |
|     |     |     |     |     |     |     |     | method | gives an IF | of 21.33 | dB  | for the | concrete | wall scene |
n=0m=0

TIVIVEetal.:SUBSPACEPROJECTIONAPPROACHFORWALLCLUTTERMITIGATIONINTWRI 2121
TABLE V where i denotes the index of the left endpoint of the interval
δ
IFOFTHEWALLCLUTTERMITIGATIONMETHODSFOR3-DIMAGING thatincludesδ,andP (δ)andP (δ)arenormalizingconstants
w t
givenby
L(cid:7)−1 i(cid:7)
δ
−1
P (δ)= P(ξ ) P (δ)= P(ξ ).
w i w i
i=iδ i=0
and 25.26 dB for the drywall scene, compared to background
subtraction, which yields IF values of 20.83 and 25.06 dB, Thetotalmeanoftheclasses,whichisindependentofδ,is
respectively.
L(cid:7)−1
μ = ξ P(ξ ). (48)
0 i i
VI. CONCLUSION
i=0
Strongsignalreflectionsfromanexteriorwallhinderthevis-
The optimum Otsu threshold is obtained by maximizing the
ibilityofstationarytargetsinTWRI.Thispaperhaspresenteda
between-classvariance
comprehensiveanalysisoftheeigenstructureofimagedTWRI
scenes. The analysis showed that, when the radar is placed δ (cid:11) =argmax{Σ (δ)} (49)
0
parallel to a homogeneous wall of uniform thickness, the wall δ
returnsspana1-Dsubspace.However,whentheantennaisnot wherethebetween-classvarianceisgivenby
perfectlyalignedwiththewallsurfaceorthewallthicknessis
not uniform, which is often the case in practice, the wall re- Σ 0 (δ)=P w [μ w (δ)−μ 0 ]2+P t [μ t (δ)−μ 0 ]2.
flectionsspanamultidimensionalsubspace.Forheterogeneous
walls,thewallreturnsalsospanamultidimensionalsubspace.
Furthermore, the analysis showed that the target subspace is
ACKNOWLEDGMENT
spanned by several singular vectors, depending on the target The authors would like to thank Dr. F. Ahmad from the
location, target size, number of targets in the scene, and the Center of Advanced Communications at Villanova University,
configurationoftheantennaarray. Villanova,PA,USA,forprovidingtheexperimentaldata.
Forwallcluttermitigation,wehaveproposedamethodthat
estimatesthewallsubspaceandasubspaceprojectionapproach
to remove, or at least significantly suppress, the wall clutter. REFERENCES
The proposed approach does not assume prior knowledge of [1] M.G.Amin,Ed.,Through-the-WallRadarImaging. BocaRaton,FL,
the scene nor the wall EM characteristics. It was applied to USA:CRCPress,2010.
[2] M.AminandK.Sarabandi,“Specialissueonremotesensingofbuilding
mitigate wall clutter in 2-D and 3-D TWRIs. Experiments
interior,” IEEE Trans. Geosci. Remote Sens., vol. 47, no. 5, pp. 1267–
withsimulatedandrealdatashowedthattheproposedmethod 1268,May2009.
was as effective as background subtraction in removing wall [3] M.Amin,“Specialissueonadvancesinindoorradarimaging,”J.Franklin
Inst.,vol.345,no.6,pp.556–722,2008.
clutterandrevealingthebehind-the-walltargets—withoutprior
[4] E.J.Baranoski,“Through-wallimaging:Historicalperspectiveandfuture
knowledgeofthebackgroundscene. directions,”J.FranklinInst.,vol.345,no.6,pp.556–569,Sep.2008.
[5] M.G.AminandF.Ahmad,“Widebandsyntheticaperturebeamforming
APPENDIXA forthrough-the-wallimaging,”IEEESignalProcess.Mag.,vol.25,no.4,
pp.110–113,Jul.2008.
OTSUTHRESHOLDINGMETHOD
[6] R.Dilsavoretal.,“Experimentsonwidebandthroughthewallimaging,”
in Proc. SPIE Symp. Defense Security, Algorithms Synthetic Aperture
Suppose that we have N singular values which lie in the
RadarImageryXIIConf.,2005,vol.5808,pp.196–209.
range[0,σ ],andthespectrumofsingularvaluesisdivided [7] J.Moulton,S.A.Kassam,F.Ahmad,M.G.Amin,andK.Yemelyanov,
max
intoLequalintervals[ξ ,ξ ),fori=0,...,L−1.LetP(ξ ) “Targetandchangedetectioninsyntheticapertureradarsensingofurban
i i+1 i structures,”inProc.IEEERadarConf.,2008,pp.1–6.
denotetheprobabilitymassdefinedbytherelativefrequencyof
[8] F. Ahmad, Y. Zhang, and M. G. Amin, “Three-dimensional wideband
singularvaluesintheithinterval,i.e., beamformingforimagingthroughasinglewall,”IEEEGeosci.Remote
Sens.Lett.,vol.5,no.2,pp.176–179,Apr.2008.
P(ξ )= n(ξ i ) [9] Y.-S.YoonandM.G.Amin,“Spatialfilteringforwall-cluttermitigation
i N inthrough-the-wallradarimaging,”IEEETrans.Geosci.RemoteSens.,
vol.47,no.9,pp.3192–3208,Sep.2009.
where n(ξ ) is the number of singular values σ ∈[ξ ,ξ ). [10] M. Dehmollaian and K. Sarabandi, “Analytical, numerical, and experi-
i i i i+1 mentalmethodsforthrough-the-wallradarimaging,”inProc.IEEEInt.
For a given threshold τ =ξ k , k =0,...,L−1, the spectrum Conf.Acoust.,SpeechSignalProcess.,2008,pp.5181–5184.
of singular values can be partitioned into two classes: C = [11] M.DehmollaianandK.Sarabandi,“Refocusingthroughbuildingwalls
w
{σ ≥δ} and C ={σ <δ}. The class means of C and C using synthetic aperture radar,” IEEE Trans. Geosci. Remote Sens.,
i t i w t vol.46,no.6,pp.1589–1599,Jun.2008.
arerespectively [12] A. N. Gaikwad, D. Singh, and M. J. Nigam, “Study of effect of room
window on through wall imaging in UWB range,” in Proc. Int. Conf.
1
L(cid:7)−1
EmergingTrendsElectron.Photon.DevicesSyst.,2009,pp.395–398.
μ w (δ)= P (δ) ξ i P(ξ i ) (46) [13] R.Chandra,A.N.Gaikwad,D.Singh,andM.J.Nigam,“Anapproachto
w removetheclutteranddetectthetargetforultra-widebandthrough-wall
μ (δ)= 1 i(cid:7) δ i= − i 1 δ ξ P(ξ ) (47) [14] P im .K ag . in V g e , r ” m J a . , G A e . op N h . y G s. a E ik n w g. a , d v , o D l. . 5, S n in o g . h 4 , , a p n p d .4 M 12 . – J 4 . 1 N 9 i , g D am ec , . “ 2 A 00 n 8 al . ysisof
t P (δ) i i clutter reduction techniques for through wall imaging in UWB range,”
t i=0 ProgressElectromagnet.Res.B,vol.17,pp.29–48,2009.

2122 IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,VOL.53,NO.4,APRIL2015
[15] M.M.RiazandA.Ghafoor,“Through-wallimageenhancementbasedon AbdesselamBouzerdoum(M’89–SM’03)received
singularvaluedecomposition,”Int.J.AntennasPropag.,vol.2012,pp.1– theM.Sc.andPh.D.degreesinelectricalengineering
20,2012,ArticleID961829. fromtheUniversityofWashington,Seattle,WA,USA.
[16] P.Setlur,M.G.Amin,andF.Ahmad,“Analysisofmicro-Dopplersignals In 1991, he joined The University of Adelaide,
usinglinearFMbasisdecomposition,”inProc.SPIERadarSens.Technol. Adelaide,Australia,andin1998,hewasanAsso-
X,2006,vol.6210,pp.62100M1–62100M11. ciateProfessorwithEdithCowanUniversity,Perth,
[17] Y. Kim and H. Ling, “Human activity classification based on micro- Australia.Since2004,hehasbeenwiththeUniver-
Dopplersignaturesusingasupportvectormachine,”IEEETrans.Geosci. sityofWollongong,Wollongong,Australia,asPro-
RemoteSens.,vol.47,no.5,pp.1328–1337,May2009. fessorofcomputerengineering,wherehealsoserved
[18] F. Ahmad, M. G. Amin, and P. Setlur, “Through-the-wall target lo- as the Head of the School of Electrical, Computer
calization using dual-frequency CW radars,” in Proc. SPIE Sens. C3I and Telecommunications Engineering (2004–2006)
Technol. Homeland Security Homeland Defense V, 2006, vol. 6201, and the Associate Dean of Research (2007–2013). From 2009 to 2011, he
pp.62010H1–62010H12. was a Member of the Australian Research Council College of Experts and
[19] F.Abujarad,A.Jostingmeier,andA.S.Omar,“Clutterremovalforland- servedasDeputyChairoftheEngineering,MathematicsandInformaticspanel
mine using different signal processing techniques,” in Proc. 10th Int. from2010to2011.Hehaspublishedover300technicalpapersandgraduated
Conf.GroundPenetratingRadar,2004,pp.697–700. 34Ph.D.andResearchMastersstudents.
[20] F.Abujarad,G.Nadimy,andA.Omar,“Clutterreductionanddetectionof Dr.Bouzerdoumwastherecipientofnumerousawardsandprizes,including
landmineobjectsingroundpenetratingradardatausingsingularvaluede- aDistinguishedResearcherAward(ChercheurdeHautNiveau)fromtheFrench
composition(SVD),”inProc.3rdInt.WorkshopAdv.GroundPenetrating MinistryofResearchin2001,theChesterSallAwardin2005,andtheEureka
Radar,2005,pp.37–42. PrizeforOutstandingScienceinSupportofDefenceorNationalSecurityin
[21] F.H.C.Tivive,M.G.Amin,andA.Bouzerdoum,“Wallcluttermitigation 2011. He served as Associate Editor for four international journals, includ-
basedoneigen-analysisinthrough-the-wallradarimaging,”inProc.Int. ing the IEEE TRANSACTIONS ON SYSTEMS, MAN, AND CYBERNETICS
Conf.DigitalSignalProcess.,2011,pp.1–8. (1999–2006).
[22] F.H.C.Tivive,A.Bouzerdoum,andM.G.Amin,“AnSVD-basedap-
proachformitigatingwallreflectionsinthrough-the-wallradarimaging,”
inProc.IEEERadarConf.,2011,pp.519–524. Moeness G. Amin (S’82–SM’91–M’93–F’01) re-
[23] L.-P.Song,C.Yu,andQ.H.Lui,“Through-wallimaging(TWI)byradar: ceived the Ph.D. degree in electrical engineering
2-Dtomographicresultsandanalysis,”IEEETrans.Geosci.RemoteSens., fromtheUniversityofColorado,Boulder,CO,USA,
vol.43,no.12,pp.2793–2798,Dec.2005. in1984.
[24] M.Dehmollaian,M.Thiel,andK.Sarabandi,“Through-the-wallimaging Since1985,hehasbeenaFacultyMemberwith
usingdifferentialSAR,”IEEETrans.Geosci.RemoteSens.,vol.47,no.5, the Department of Electrical and Computer Engi-
pp.1289–1296,May2009. neering,VillanovaUniversity,Villanova,PA,USA,
[25] M.AminandF.Ahmad,“Compressivesensingforthroughthewallradar where,in2002,hebecametheDirectoroftheCenter
imaging,”J.Electron.Imag.,vol.22,no.3,pp.1–21,Jul.2013. for Advanced Communications, College of Engi-
[26] S.M.LiandX.F.Liu,“Robustadaptivebeamformingimagingapproach neering. He has over 600 journal and conference
forstepped-frequencythrough-the-wallradar,”Appl.Mech.Mater.,Mech. publications in the areas of wireless communica-
Electron.Eng.III,vol.130–134,pp.45–49,2011. tions,time–frequencyanalysis,sensorarrayprocessing,waveformdesignand
[27] Y.-S. Yoon and M. G. Amin, “High-resolution through-the-wall radar diversity, interference cancellation in broadband communication platforms,
imagingusingbeamspacemusic,”IEEETrans.AntennasPropag.,vol.56, satellitenavigations,targetlocalizationandtracking,directionfinding,channel
no.6,pp.1763–1774,Jun.2008. diversityandequalization,ultrasoundimaging,andradarsignalprocessing.He
[28] C.A.Balanis,AdvancedEngineeringElectromagnetics. NewYork,NY, coauthored18bookchapters.HeistheEditorofthebookThroughtheWall
USA:Wiley,1989. RadarImaging(CRCPress,2011)andCompressiveSensingforUrbanRadar
[29] P.Protiva,J.Mrkvica,andJ.Machácˇ,“TimedelayestimationofUWB (CRCPress,2014).HewasaGuestEditoroftheJournalofFranklinInstitute
radar signals backscattered from a wall,” Microw. Opt. Technol. Lett., September 2008 special issue on Advances in Indoor Radar Imaging; Insti-
vol.53,no.6,pp.1444–1450,Jun.2011. tuteofEngineeringandTechnology(IET)SignalProcessingDecember2009
[30] N.Otsu,“Athresholdselectionmethodforgraylevelhistograms,”IEEE specialissueonTime–FrequencyApproachtoRadarDetection,Imaging,and
Trans.Syst.,Man,Cybern.,vol.SMC-9,no.1,pp.62–66,Jan.1979. Classification;andtheEuropeanAssociationforSignalProcessing(EURASIP)
JournalonAdvancesinSignalProcessing,specialissueonSparseSensingin
RadarandSonarSignalProcessingin2014.
Dr. Amin is a Fellow of the International Society of Optical Engineering
in2007andtheIETin2010.HewasarecipientoftheVillanovaUniversity
OutstandingFacultyResearchAwardin1997,theIEEEPhiladelphiaSection
Awardin1997,theIEEEThirdMillenniumMedalin2000,the2009Individual
TechnicalAchievementAwardfromtheEURASIP,the2010NATOScientific
Achievement Award, and the Chief of Naval Research Challenge Award in
2010.HewasaDistinguishedLectureroftheIEEESignalProcessingSociety
in2003–2004andiscurrentlytheChairoftheElectricalClusteroftheFranklin
InstituteCommitteeonScienceandtheArts.HewasaPlenarySpeakeratIEEE
International Symposium on Signal Processing and Information Technology
2003 (ISSPIT-03), the 2010 IEEE International Conference on Acoustics,
Speech and Signal Processing, The 29th International Review of Progress
Fok Hing Chi Tivive (M’02) received the Ph.D.
inAppliedComputationalElectromagnetics2013(ACES-13),IET2013,the
degreeincomputerengineeringfromtheUniversity
2013 European Signal Processing Conference, Statistics, Optimization, and
ofWollongong,Wollongong,Australia,in2006.
Signal Processing Workshop 2013 (STATOS-13), IEEE International Work-
Since2006,hehasbeenaPostdoctoralResearch
shoponComputationalAdvancesinMulti-SensorAdaptiveProcessing2013
Fellow with the School of Electrical, Computer
(CAMSAP-13), and International Radar Conference 2014 (RADAR-14). He
andTelecommunicationsEngineering,Universityof
was a Guest Editor of the IEEE TRANSACTIONS ON GEOSCIENCE AND
Wollongong.Hisresearchinterestsincludemachine
REMOTE SENSINGMay2009SpecialIssueonRemoteSensingofBuilding
learning,patternrecognition,imageprocessing,and
InteriorandtheIEEESIGNALPROCESSINGMAGAZINENovember2013and
through-the-wallradarimaging.
July2014SpecialIssuesonTime–FrequencyAnalysisandApplications,and
RecentAdvancesinSyntheticApertureRadarImaging.