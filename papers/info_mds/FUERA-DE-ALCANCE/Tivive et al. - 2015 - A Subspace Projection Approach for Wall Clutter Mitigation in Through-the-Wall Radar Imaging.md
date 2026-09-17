# A Subspace Projection Approach for Wall Clutter Mitigation in Through-the-Wall Radar Imaging

> **Pilar:** Fuera de alcance
> **Clasificación:** Inferida
> **Evidencia de clasificación:** No aparece entre las fuentes académicas FinOps de la matriz. El PDF trata mitigación de clutter en radar through-the-wall, sin relación temática con TI-06 FinOps; se conserva por completitud del conjunto de 14 PDF.
> **Archivo fuente:** papers-pdf/Tivive et al. - 2015 - A Subspace Projection Approach for Wall Clutter Mitigation in Through-the-Wall Radar Imaging.pdf
> **Uso previsto:** Lectura personal y apoyo documental; requiere validación humana antes de incorporarse al informe.

## 1. Título

*A Subspace Projection Approach for Wall Clutter Mitigation in Through-the-Wall Radar Imaging*.

## 2. Autor y fecha

- **Autores verificados en el PDF:** Fok Hing Chi Tivive, Abdesselam Bouzerdoum y Moeness G. Amin.
- **Fecha bibliográfica utilizada:** 2015, *IEEE Transactions on Geoscience and Remote Sensing*, vol. 53, n.º 4, abril de 2015, pp. 2108–2122. El copyright es 2014; se usa el año de la edición.

## 3. Problema que trata

En imágenes radar a través de paredes, las reflexiones intensas del muro ocultan objetivos estacionarios. Restar una escena de fondo es eficaz pero suele ser impracticable; otros métodos dependen de parámetros exactos o asumen erróneamente que el muro ocupa un único componente singular.

## 4. Qué quiere hacer

Mitigar el clutter del muro sin una escena de referencia ni un modelo preciso de sus parámetros electromagnéticos, preservando la imagen de objetivos detrás de paredes homogéneas y heterogéneas.

## 5. Cómo lo hace

Construye una matriz espacio-frecuencia, aplica descomposición en valores singulares, clasifica los subespacios de muro y objetivo y proyecta la señal sobre el complemento ortogonal del muro. Analiza cómo geometría, grosor, material, posición, tamaño y número de objetivos cambian la dimensionalidad. Evalúa simulaciones y datos reales en imágenes 2D/3D y compara con sustracción de fondo, time gating, filtrado espacial y métodos SVD (secciones II–V).

## 6. Resultados

- Para pared de hormigón 2D, la sustracción de fondo logra 16,16 dB de mejora y el método propuesto 11,01 dB; el filtrado espacial obtiene 8,26 dB (tabla III, p. 2119).
- Para drywall 2D, el método propuesto alcanza **22,35 dB** y el SVD de B-scan citado 2,08 dB (tabla IV, p. 2119).
- En 3D, la proyección obtiene 21,33 dB en hormigón y 25,26 dB en drywall, comparables con 20,83 y 25,06 dB de sustracción de fondo (tabla V, pp. 2120–2121).
- Los experimentos respaldan que muro y objetivos pueden ocupar subespacios multidimensionales e intercalados.

## 7. Discusión y trabajo futuro

El método evita conocer el fondo, pero depende de separar correctamente valores singulares y de las condiciones geométricas y materiales. El PDF no presenta una sección específica de trabajo futuro; la conclusión se concentra en los hallazgos y la eficacia observada. **No especificado en el documento** como agenda futura formal.

## 8. Conclusión del paper

Los autores concluyen que las reflexiones del muro suelen ser multidimensionales y que el subespacio del objetivo también varía con la escena. La proyección propuesta suprime clutter en 2D y 3D con resultados comparables a la sustracción de fondo, sin requerir escena de referencia ni parámetros electromagnéticos previos.

## Relación preliminar con INV-01

No se identifica relación sustantiva con los subtemas de TI-06 FinOps en INV-01. El artículo pertenece a procesamiento de señales y radar through-the-wall. Se mantiene como **Fuera de alcance** para preservar la trazabilidad 1:1 de los 14 PDF, no como fuente para el informe FinOps.

## Limitaciones de esta síntesis

La extracción textual no reproduce imágenes radar, espectros ni ecuaciones con fidelidad visual; las cifras requieren contraste con tablas III–V. La clasificación es inferida porque la fuente no aparece en la matriz FinOps. No debe forzarse una conexión temática inexistente.

## Texto extraído del PDF

> **Advertencia de conversión:** extracción textual automática de 15 páginas (94070 caracteres). Se conservaron títulos, párrafos, referencias y contenido textual por página. La disposición multicolumna, las figuras, las tablas y las ecuaciones pueden no mantener su alineación o representación visual; verifique esos elementos en el PDF original.

### Página PDF 1

2108                                                    IEEE TRANSACTIONS ON GEOSCIENCE AND REMOTE SENSING, VOL. 53, NO. 4, APRIL 2015

 A Subspace Projection Approach for Wall Clutter
   Mitigation in Through-the-Wall Radar Imaging

          Fok Hing Chi Tivive, Member, IEEE, Abdesselam Bouzerdoum, Senior Member, IEEE, and
                                 Moeness G. Amin, Fellow, IEEE


  Abstract—One of the main challenges in through-the-wall radar   rescue missions, behind-wall target detection, and surveillance
imaging (TWRI) is the strong exterior wall returns, which tend  and reconnaissance in urban environments [1]–[5]. One of the
to obscure indoor stationary targets, rendering target detection                                                     main issues of imaging stationary targets inside a building is
and classiﬁcation difﬁcult,  if not impossible. In this paper, an
                                                                 the strong clutter induced by the exterior wall, which is usuallyeffective wall clutter mitigation approach is proposed for TWRI
that does not require knowledge of the background scene nor does   a highly reﬂective and attenuative medium.
it rely on accurate modeling and estimation of wall parameters.    Most TWRI studies dealing with stationary targets [6]–[8]
The proposed approach is based on the relative strength of the  assume to have access of a background or reference scene,
exterior wall returns compared to behind-wall targets. It applies                                                      where background subtraction is performed on the raw data
singular value decomposition to the data matrix constructed from
                                                                    prior to applying an image formation method for scene re-the space-frequency measurements to identify the wall subspace.
Orthogonal subspace projection is performed to remove the wall   construction. This approach, although effective in removing
electromagnetic signature from the radar signals. Furthermore,   wall returns, is not feasible in practice. Therefore, different
this paper provides an analysis of the wall and target subspace   approaches have been proposed to deal with strong wall reﬂec-
characteristics, demonstrating that both wall and target subspaces                                                                    tions without relying on the background scene data [9]–[14].
can be multidimensional. While the wall subspace depends on the
                                                 From the received signals, particularly the ﬁrst wave arrivals,wall type and building material, the target subspace depends on
the location of the target, the number of targets in the scene, and    it is possible to estimate the front wall parameters, such as
the size of the target. Experimental results using simulated and   dielectric constant and thickness [11]. The estimated param-
real data demonstrate the effectiveness of the subspace projection   eters can be used to model the EM wall returns, which are
method in mitigating wall clutter while preserving the target                                                             subsequently subtracted from the total radar returns, rendering
image. It is shown that the performance of the proposed approach,
                                                                 the received signals free of wall reﬂections. This approachin terms of the improvement factor of the target-to-clutter ratio,
is better than existing approaches and is comparable to that of   requires accuracy in parameter estimation and modeling. An-
background subtraction, which requires knowledge of a reference   other method of suppressing the wall reﬂections is to use three
background scene.                                           antenna arrays placed parallel to the wall at different heights,
  Index Terms—Singular value decomposition (SVD), subspace  where the upper and lower arrays comprise receivers and the
projection,  target  subspace,  through-the-wall radar imaging   middle array consists of transmitters [10]. A simple subtraction
(TWRI), wall clutter removal, wall subspace.                      of the radar returns from the lower and upper arrays can lead
                                                                    to wall clutter reduction. Due to the receiver symmetry with
                              I. INTRODUCTION                         respect to the transmitter, the contribution of the reﬂection
                                                      from the wall in the difference signal is suppressed. In this    HROUGH-the-wall radar imaging (TWRI) is an emerging
                                                         scheme, two additional arrays are required, and the effect of the     technology of increasing interest. The main objective is toT                                                             subtraction operation on the target reﬂections is unknown andsense through the wall and inside enclosed building structures
                                                           cannot be controlled. A spatial ﬁltering method was proposedby using electromagnetic (EM) waves for determining the
                                                                    for wall clutter mitigation [9]. This method relies on invariancebuilding layouts, discerning the intent of activities inside the
                                                               of the wall characteristic and is based on the assumption thatbuilding, and detecting, identifying, and tracking moving tar-
                                                                 the wall returns have the same characteristics with changinggets. This type of technology is highly desirable in search-and-
                                                           antenna location. This spatial invariance can be horizontal,
                                                                          vertical, or along both dimensions in the wall plane. Thus, a
                                                           notch ﬁlter was applied across the antenna array to remove  Manuscript received January 14, 2013; revised December 2, 2013 and June 9,
2014; accepted August 16, 2014. This work was supported by a grant from the   the zero frequency or low spatial frequencies, which capture
Australian Research Council. The work of M. G. Amin was supported by the   constant or slowly varying wall returns. It is noted, however,
Ofﬁce of Naval Research under Grant N00014-11-0576.
                                                                      that the ﬁltering method is effective only for homogeneous or   F. H. C. Tivive and A. Bouzerdoum are with the School of Electrical,
Computer and Telecommunications Engineering, University of Wollongong,   near-homogeneous walls and at low operating frequencies.
Wollongong,   N.S.W.   2522,   Australia   (e-mail:   tivive@uow.edu.au;     In this paper, we assume that the scene is stationary, and
a.bouzerdoum@uow.edu.au).
                                                             hence, change detection or Doppler/micro-Doppler processing  M. G. Amin is with the Radar Imaging Laboratory, Center for Advanced
Communications, Villanova University, Villanova, PA 19085 USA (e-mail:    is not applicable for wall  clutter removal and deletion of
moeness.amin@villanova.edu).                                    animate and inanimate targets [16]–[18]. We present a new
  Color versions of one or more of the ﬁgures in this paper are available online
at http://ieeexplore.ieee.org.                                       subspace method for mitigating wall clutter, or at least sig-
   Digital Object Identiﬁer 10.1109/TGRS.2014.2355211                   niﬁcantly suppressing it, to reveal the targets behind the wall.

0196-2892 © 2014 IEEE. Translations and content mining are permitted for academic research only. Personal use is also permitted, but republication/redistribution
                 requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.

### Página PDF 2

TIVIVE et al.: SUBSPACE PROJECTION APPROACH FOR WALL CLUTTER MITIGATION IN TWRI                                                    2109


The proposed technique ﬁrst identiﬁes the wall clutter and
target signal subspaces using singular value decomposition
(SVD); then, it projects the radar signal onto a subspace or-
thogonal to the wall subspace. SVD has been used previously
in ground-penetrating radar to improve the signal-to-noise ratio
(SNR) of the radar images [19], [20]; the B-scan image is
decomposed into several eigenimages, and the ﬁrst eigenim-
age is considered the target image. SVD has been used in
TWRI to remove the wall clutter and to detect behind-the-
wall targets from B-scan images [12]–[15]. The wall clutter
and the target reﬂections are assumed to reside in the ﬁrst
and second eigenimages, respectively, whereas the remaining
eigenimages contain noise. Another SVD-based method was
proposed to remove wall clutter in the formed image, where the
wall reﬂections still reside in the ﬁrst eigenimages and the target
reﬂections span several eigenimages [15]. However, recently,
we have shown that the wall clutter is generally characterized
by a high-dimensional subspace [21], [22]. Furthermore, the
weak wall singular components (SCs) may interleave with the
target SCs. Therefore, a more effective technique is required
to separate the wall and target subspaces since the ﬁrst SC is
unlikely to account for all wall returns.
  This paper extends our previous work [21], [22] in both
analysis and experimentation.  It considers SVD of the data
matrix constructed from stepped-frequency matched ﬁltered
measurements obtained at different antenna positions. In so
doing,  it operates on the data and not on the beamformed
image. The results of the two operations are entirely different
due to the target localization through coherent combining. We
show that, in near ﬁeld imaging, the wall returns can span
a multidimensional subspace, which depends, among other
factors, on the periodic structure of the wall, the frequency
response, the uniformity of the wall thickness, and the array
geometry. Moreover, the target reﬂections can span a subspace
whose dimension depends on the target size, the target location,
the number of targets, and the conﬁguration of the antenna
array. Both empirical data and simulations conﬁrm that the wall
returns generally span a multidimensional subspace, where the    Fig. 1.  TWRI geometry. (a) In free space. (b) Through the wall.
signiﬁcant target SCs can interleave with some of the weak wall                                                     scheme is derived for free space and then extended to imaging
SCs. This paper conducts a comprehensive analysis of the wall                                                          behind a homogeneous wall. The geometric model of TWRI as
and target eigensubspaces. Furthermore, it presents a subspace                                                              described in [5] is used to estimate the signal propagation delay
classiﬁcation method to segregate between the target and wall                                                                    in the presence of a homogeneous wall.
subspaces. A subspace projection method is then proposed for                                                                  In free space, the geometric model of a TWRI system is
wall clutter mitigation, which works on the space-frequency                                                              depicted in Fig. 1(a). Here, a ground-based monostatic syn-
data matrix instead of the formed image.                                                                       thetic aperture radar (SAR) system is used to synthesize an
  The remainder of this paper is organized as follows. The                                                      N-element linear array. A local coordinate system is deﬁned to
next section presents the geometric model of TWRI and de-                                                                 represent the region of interest with the horizontal and vertical
scribes delay-and-sum (DS) beamforming for image formation.                                                            axes denoted as x′ and z′, respectively. The center of the scene
Section III presents the analysis of the wall and target eigensub-                                                                               is at (0, 0), and θn is the viewing angle of the nth antenna.
spaces supported by simulation results. Section IV describes                                                           Let Rn(0, 0) and cn denote the distance of the nth antenna to
the proposed subspace projection approach for wall clutter                                                                 the center of the scene and to the center of the array aperture,
mitigation. Experimental results using real data are given in                                                                     respectively. The distance from the nth antenna to the pixel
Section V. Finally, the conclusion is presented in Section VI.                                                                  location (x′p, z′p) within the region of interest is denoted by
                                                      Rn(x′p, z′p) and can be computed as
   II. THROUGH-WALL RADAR IMAGING SIGNAL MODEL
                                          Rn  x′p, z′p = Rn(0, 0)2 + 2Rn(0, 0)z′p cos(θn)
                                                                                                                                               1  This section presents the TWRI signal model used to explain                                                                                                                                               2                                                                                                                2      2
the proposed wall clutter mitigation approach. The imaging              −2Rn(0, 0)x′p sin(θn) + x′p + z′p       .   (1)

### Página PDF 3

2110                                                    IEEE TRANSACTIONS ON GEOSCIENCE AND REMOTE SENSING, VOL. 53, NO. 4, APRIL 2015


The viewing angle θn of the nth antenna is given by                    III. ANALYSIS OF WALL AND TARGET EIGENSUBSPACES

                               cn                             Several SVD-based wall clutter mitigation approaches have
               θn = sin−1                    .                (2)
                          Rn(0, 0)                     been proposed which assume that the wall reﬂections are
                                                                characterized by the ﬁrst singular vector associated with the
Without loss of generality, let us assume a single target located                                                      most dominant singular value [12]–[15]. In [21] and [22], we
at (x′p, z′p). The two-way propagation delay τn(x′p, z′p) from the   have shown that multiple singular vectors can span the wall
nth antenna to the target is given by                                                              subspace. In this section, we investigate the factors affecting
                      2Rn  x′p, z′p                      the wall and target eigensubspaces. The dimension of the wall
               τn  x′p, z′p =                              (3)   subspace is related to, among other factors, the wall hetero-                                   c
                                                                    geneity, the wall thickness uniformity, and the antenna array
where c is the speed of light in free space.                                                             conﬁguration. For the target subspace, its dimension is affected
  When there is a homogeneous wall in front of the radar                                                     by the target location, the target size, the number of targets
system as shown in Fig. 1(b), the two-way propagation delay                                                          behind the wall, and the conﬁguration of the array aperture.
of the radar signal from the nth antenna to the target is given by                                                        Numerical simulations using XFDTD are included to support
           2                                                  the analysis of the wall and target subspaces.
τn(xp, zp) =   (Rn,air1(xp, zp)
             c
        + √ϵRn,w(xp, zp) + Rn,air2(xp, zp)       (4)                                                             A. Eigenstructure of Wall Subspace

where  ϵ   is  the  relative  permittivity  of  the  wall  and     In practical TWRI applications, we often deal with two types
Rn,air1(xp, zp), Rn,w(xp, zp), and Rn,air2(xp, zp) denote the   of walls: homogeneous and heterogeneous walls. The following
distances traveled by the signal from the nth antenna to the  two subsections analyze the eigenstructure of the wall subspace,
target at location (xp, zp) before, through, and after the wall,   using both types of walls.
respectively. These distances can be estimated as follows [8]:       1) Homogeneous Wall: A homogeneous wall can be mod-
                                   za                       eled as a uniform dielectric slab of thickness d and dielectric
             Rn,air1(xp, zp) =                             (5)
                             cos (ϕn(xp, zp))                constant ϵ. Assuming that the signal is transmitted perpendicu-
                               d                           larly to the surface of the wall, the wall return of a homogeneous
             Rn,w(xp, zp) =                             (6)
                             cos (φn(xp, zp))                wall is calculated based on the plane wave Fresnel reﬂection
                                         zt                    and transmission coefﬁcients obtained from Maxwell’s equa-
             Rn,air2(xp, zp) =                             (7)
                             cos (ϕn(xp, zp))                  tions [28]. Let ρ be the local Fresnel reﬂection coefﬁcient,
                                                             given by
where za is the standoff distance from the antenna array to the
wall, d is the wall thickness, zt is the distance from the wall                          1 −√ϵ                                                                      ρ =                             (10)to the target, and ϕn(xp, zp) and φn(xp, zp) are the angles of                          1 + √ϵ.
incidence and refraction from the nth antenna to the target at
                                                   The reﬂection coefﬁcient at the mth frequency Γm can belocation (xp, zp), respectively. To image the behind-the-wall
                                                                 written as
scene, a stepped-frequency signal is synthesized by emitting
monochromatic signals with frequencies equispaced over the                   ρ (1 −exp(−2j√ϵkmd))
                                                 Γm =                                    (11)desired bandwidth ωM−1 −ω0                                              1 −ρ2 exp(−2j√ϵkmd)

     ωm = ω0 + mΔω,   for m = 0, . . . , M −1      (8)  where km = ωm/c  is  the wavenumber. The  radar  signal
                                                               backscattered from the wall and received by the nth antenna
where ω0 is the lowest frequency in the desired frequency band,                                                         can be expressed as
Δω is the frequency step size, and M is the total number of
frequencies.                                            Gmλm exp(−j2kmzn)                                                          sw(m, n) =               Γm       (12)
  There are several approaches for image formation, includ-                      8π        zn
ing tomographic approaches [23], differential SAR [24], com-                                                      where zn  is the distance between the nth antenna and the
pressed sensing [25], and adaptive beamformers [26], [27].                                                                   wall, λm is the wavelength of the mth monochromatic signal,
Here, we employ DS beamforming to compute the complex                                                       and Gm is the antenna gain at the mth frequency [11]. The
amplitude of the pixel, which is given by                                                              wall backscattered signals received by the N-element array can
              N−1 M−1                               be arranged into a matrix Φw ∈CM×N, where each column             1
   I(x, z) =             s(m, n) exp (jωmτn(x, z))    (9)   contains the signal received at one antenna location and each
      NM
                n=0 m=0                             row contains the signals from one frequency

where s(m, n) is the radar signal at the mth frequency received                                                        Φw = [φmn]                    (13)
by the nth antenna and τn(x, z)  is the focusing delay for
the pixel at location (x, z) with respect to the nth antenna,  where φmn = sw(m, n). Assuming that the antenna gain and
including the propagation through the wall. Before describing   wall reﬂection coefﬁcient do not change with antenna location,
the proposed wall clutter mitigation method, we ﬁrst present the  Φw can be expressed as the product of a diagonal matrix
analysis of the wall and target eigensubspaces.                A, containing the antenna gains and reﬂection coefﬁcients

### Página PDF 4

TIVIVE et al.: SUBSPACE PROJECTION APPROACH FOR WALL CLUTTER MITIGATION IN TWRI                                                    2111


(as a function of frequency), with an M × N matrix B which
depends on the antenna standoff distance

                Φw = AB                     (14)

where

     A = diag(G0λ0Γ0, . . . , GM−1λM−1ΓM−1)     (15)
     B = [bmn]                                     (16)

with

                    exp(−j2kmzn)
              bmn =                         .              (17)
                         8πzn

  The wall eigensubspace can be obtained by applying SVD
and identifying the singular vectors containing the wall re-
turns. Since A is a full rank diagonal matrix, it follows that
rank(Φw) = rank(B); therefore, the wall subspace dimension
is determined by the rank of B. Furthermore, it is clear from
(17) that the columns of B depend on the antenna standoff
distance zn; the rows of B depend on the frequency. In practice,
the number of antennas N  is smaller than the number of
frequencies M. Thus, the rank of B  is determined by the
standoff distance of the antenna to the wall. Although the
gain of the transceiver in a synthesized array aperture varies
with frequencies and not antenna locations, it has no effect on
the rank of the matrix Φw and therefore does not change the    Fig. 2.  Perturbation analysis in the antenna standoff distance: (a) Subspace
dimension of the wall subspace.                                            distortion index as a function of the tilt angle and (b) the ﬁrst 20 normalized
                                                                                  singular values at a tilt angle of 5◦. For clarity, the ﬁrst singular value is omitted;  There are two cases where the signals backscattered from
                                                                                 the other singular values are normalized with the ﬁrst one.
a homogeneous wall span a multidimensional subspace: the
antenna array is not perfectly aligned (parallel to) the wall  ≥σN ≥0. Ideally, a homogeneous wall subspace is spanned
surface, or the wall exhibits nonuniform thickness along the  by the ﬁrst singular vector associated with the dominant sin-
antenna array. In the ﬁrst case, each antenna is positioned at a   gular value. Perturbations in the remaining singular values are
different standoff distance zn from the wall; thus, the columns   considered as subspace distortions. We deﬁne the subspace
of B become linearly independent, thereby increasing the rank   distortion index of a homogeneous wall δs as the fraction of
of the matrix and the dimension of the wall subspace. In the  power carried by the nondominant SCs
second case, due to the variations in the wall thickness, the two-                      N
way propagation delay of the signal reﬂected from the back of                              σ2i
the wall varies from one antenna to another, causing the signals                           δs = i=2     .                    (19)                                                              N
received across the antennas to be different from each other and                              σ2i
hence increasing the dimension of the wall subspace. These                               i=1
two cases are investigated using numerical simulations with                                                                  In the ﬁrst case, the antenna array  is  tilted at an angle
XFDTD software. The ﬁrst numerical simulation scenario con-                                                           with respect to the wall surface. The subspace distortion index
sists of a homogeneous wall of thickness 0.15 m and a dielectric                                                               of a homogeneous wall is computed while varying the  tilt
constant 7.6 placed in front of the radar at a standoff distance of                                                             angle from 1◦to 10◦. Fig. 2(a) illustrates the variations of the
1 m. A 51-element antenna array of size 1.2 m is synthesized for                                                           subspace distortion index as a function of the tilt angle, and
imaging. The excitation signal is a modulated Gaussian pulse                                                                   Fig. 2(b) depicts the normalized singular values of the wall
which covers the frequency range from 2 to 3 GHz. The time                                                           subspace at a subspace distortion index of 0.15. A misalignment
domain responses are transformed into the frequency domain                                                               of 5◦with respect to the surface of the wall produces a subspace
and sampled to produce the stepped-frequency signals which                                                                     distortion index of 0.15, resulting in 16 nonzero singular values,
are arranged into a matrix Φw. Using SVD, the matrix Φw can                                                               as shown in Fig. 2(b). Therefore, we can conclude that the
be decomposed as                                                                   signals backscattered from a homogeneous wall that is not
                         H                             parallel to the antenna array span a multidimensional subspace.               Φw = UΣV                      (18)
                                                                  In the second case, the wall thickness is increased gradually
where H denotes the Hermitian transpose, U = [u1, . . . , uM]   along the antenna array: The wall thickness in front of the ﬁrst
and V = [v1, . . . , vN] are unitary matrices containing the left   antenna is d, and that at the last antenna is d + Δd. In the simu-
and right singular vectors, respectively, and Σ is a rectangular   lations, the parameter Δd is increased from 0.03 to 0.3 m while
matrix of the same size as Φw with singular values σi on the  d is ﬁxed at 0.15 m. The subspace distortion index computed
main diagonal arranged in decreasing order, i.e., σ1 ≥σ2 ≥· · ·   as a function of the relative variations in the wall thickness

### Página PDF 5

2112                                                    IEEE TRANSACTIONS ON GEOSCIENCE AND REMOTE SENSING, VOL. 53, NO. 4, APRIL 2015


                                                                                   Fig. 4.  Eigenstructure of a heterogeneous wall: (a) Image of the hollow con-
                                                                                     crete block wall, (b) its normalized singular values, (c) image of the reinforced
                                                                              concrete wall with vertical rebars only, and (d) its normalized singular values.
                                                                        For clarity, the ﬁrst singular value is omitted; the other singular values are
                                                                         normalized with the ﬁrst one.

                                                                  metallic rebars spacing at an interval of 0.2 m. The TWRI scene
Fig. 3.  Perturbation analysis in the wall thickness: (a) Subspace distortion   devoid of targets is illuminated with a modulated Gaussian
index as a function of the relative variations in the wall thickness and (b) the ﬁrst   pulse centered at 1.5 GHz. The time domain responses ob-
20 normalized singular values excluding the ﬁrst one at a relative perturbation   tained from each of these walls are transformed into stepped-
of 0.06.
                                                            frequency signals covering the frequency band of 2–3 GHz;
is shown in Fig. 3(a). Fig. 3(b) illustrates the normalized wall   they are then arranged into a matrix Φw. Fig. 4 shows the DS-
singular values at a relative variation of 0.06 (Δd/d = 0.06) in  beamformed images and the normalized singular values of the
the wall thickness. The numerical simulations show that, when   signal matrix for both types of heterogeneous walls: Fig. 4(a)
the homogeneous wall does not have uniform thickness, the  and (b) are for the hollow concrete block wall, and Fig. 4(c) and
wall reﬂections span a multidimensional subspace.                (d) are for the reinforced concrete wall. The number of nonzero
                                                                  singular values in Fig. 4(b) and (d) indicates that the rank of
B. Heterogeneous Wall                                          the matrix Φw is greater than one. Thus, we conclude that the
                                                              wall returns from a heterogeneous wall span a multidimensional
 A wall  is considered heterogeneous when the dielectric
                                                              subspace.
properties of its building material vary along either or both
                                                     To summarize, the wall subspace is not necessarily char-
dimensions,  i.e., height and width.  If a wall  is built from
                                                                  acterized by a single singular vector but can be spanned by
several vertical planes whose dielectric constants vary along the
                                                               multiple singular vectors. There are several factors that affect
horizontal antenna array, it is clear from (11) that the reﬂection
                                                                 the dimension of the wall subspace, namely, the wall EM char-
coefﬁcient will be a function of the antenna location; thereby,
                                                                           acteristics, the wall thickness uniformity, and the conﬁguration
the columns of the matrix Φw become linearly independent,
                                                               of the antenna array. The next section presents an analysis of
and the wall subspace increases. In practice, most heteroge-
                                                                 the target subspace.
neous walls are built in such a way that they exhibit some
periodicity. For example, walls constructed from cinder block
                                                          C. Eigenstructure of Target Subspace
or crossbar reinforced concrete are 2-D periodic heterogeneous
walls, whereas drywalls with vertical wooden studs and rein-     In this section, we analyze the eigensubspace of a target,
forced concrete walls with vertical rebars only are 1-D periodic  where the received signals comprise only the target returns.
walls. Due to the fast-fading phenomenon caused by the wall   First, we consider a point target with frequency-dependent
heterogeneity, this type of walls is analyzed by either using EM   reﬂection coefﬁcient σm located at the location (x′p, z′p). The
simulation tool or performing real experiments.                    target signal received by the nth antenna can be written as
  For eigensubspace analysis, we conduct several numerical            σmGmλm
                                                            st(m, n) =                                                                          exp −jωmτn  x′p, z′p    .     (20)simulations using two kinds of heterogeneous walls: hollow                                                                 4π
concrete block wall and reinforced concrete wall. The hollow
                                                   The target signals received across the antenna array are ar-
concrete block wall is built using cinder blocks of size 0.2 m ×
                                                          ranged into the matrix Φt
0.4 m with a thickness of 0.15 m. The reinforced concrete wall
has a thickness of 0.15 m and consists of 0.025-m-thick vertical                       Φt = AB                      (21)

### Página PDF 6

TIVIVE et al.: SUBSPACE PROJECTION APPROACH FOR WALL CLUTTER MITIGATION IN TWRI                                                    2113


where


         σ0G0λ0 σ1G1λ1    σM−1GM−1λM−1
A = diag               ,             , . . .,                       (22)
           4π     4π            4π

B = exp −jωmτn  x′p, z′p      .                         (23)


Since the two-way propagation delay between the nth antenna
and the target τn(x′p, z′p) is dependent on the antenna location,
it is expected to vary from one antenna location to another,
causing the columns of the matrix B in (23) to become linearly
independent. Therefore, the rank of Φt changes with the target
location. For example, a target placed at the center of the
array will reduce the rank of Φt since the signal propagation
delays from the antennas on the left half of the array are the
same as those on the right half of the array, i.e., τ0(x′p, z′p) =
τN−1(x′p, z′p), τ1(x′p, z′p) = τN−2(x′p, z′p), etc. In a recent study
[21], we have shown that reﬂections from a point target span
a multidimensional subspace, which depends on the number of
targets in the scene and the conﬁguration of the antenna array.
The target location with respect to the radar also inﬂuences the
target subspace dimension.
  Next, we investigate the dimension of the target subspace
under two imaging scenarios, namely, short range and long    Fig. 5.  Formed images and singular values of two different imaging ranges:
range, where the target is placed close to or far from the radar    (a) Image of a near target, (b) its normalized singular values, (c) image of a dis-
system. In the former, the viewing angle θn of the antenna    tant target, and (d) its normalized singular values. For clarity, the ﬁrst singular
                                                                             value is omitted; the other singular values are normalized with the ﬁrst one.
varies considerably across the array aperture, causing the dis-
tance traveled by the signal from each antenna to the target to
be different. Based on the propagation delay given in (3), it is
clear that the target signal is related to the viewing angle, and
therefore, the number of linearly independent columns in the
matrix Φt increases when the viewing angle varies markedly
across the array aperture. On the other hand, for a long-range
target, the changes in the viewing angle across the antenna
array are much smaller, resulting in almost the same distance
between each antenna element and the target; therefore, the
target subspace is narrower compared to that of a short-range
target. To illustrate this, a target is placed at two different
locations: a short range at (0, 1.2) m and a long range at
(0, 6.2) m. The formed images and the singular values for both
cases are shown in Fig. 5. Fig. 5(a) and (b) depicts the formed
image and the singular values of the near target, respectively,
and Fig. 5(c) and (d) shows the image and singular values of the
distant target. The difference in the number of nonzero singular
values between Fig. 5(b) and (d) conﬁrms that the subspace of
a distant target is narrower than that of a near target.
  Another factor that can affect the target subspace dimension
                                                                                   Fig. 6.  Formed images and singular values of two different target sizes:
is the target size. For illustration, we simulate a square plate    (a) Image of the small dihedral, (b) its normalized singular values, (c) image of
dihedral of two different areas: 0.09 and 1 m2. The dihedral is    the large dihedral, and (d) its normalized singular values. For clarity, the ﬁrst sin-
placed at a standoff distance of 2.2 m from the radar without    gular value is omitted; the other singular values are normalized with the ﬁrst one.
any wall. Fig. 6(a) and (b) presents the formed image and the     In summary, the target returns do not span a 1-D subspace
normalized singular values of the small dihedral, and Fig. 6(c)   as reported in some existing literatures [12]–[14] but a mul-
and (d) shows the formed image and the normalized singular   tidimensional subspace, depending on several factors. These
values of the large dihedral. The difference in the number of   factors include, among others, the target location, the target
nonzero singular values between Fig. 6(b) and (d) shows that   size, the number of targets in the scene, and the antenna
the target subspace of the large dihedral is wider than that of   array conﬁguration. Next, we investigate the eigenstructure of
the small dihedral.                                       combined wall and target returns.

### Página PDF 7

2114                                                    IEEE TRANSACTIONS ON GEOSCIENCE AND REMOTE SENSING, VOL. 53, NO. 4, APRIL 2015


Fig. 7.  Image of a scene with two dihedrals placed behind a homogeneous
wall: (a) Image of targets and wall, (b) image without the ﬁrst dominant SC,
and (c) image without the ﬁrst two leading SCs. The targets are circled by the
rectangles.

D. Combined Wall–Target Eigensubspace

  In the aforementioned analysis, we have shown that the wall
subspacecanbemultidimensional,andthetargetreﬂectionsspan
a multidimensional subspace. Here, we investigate the eigen-    Fig. 8.  Range proﬁles of the ﬁrst six dominant SCs (1st-SC to 6th-SC).
structure of combined wall and target returns. From a TWRI                                                                    identify the singular vectors characterizing the wall returns, we
scene comprising a wall and target(s), the received signal can                                                          propose a simple procedure. From (25), the matrix Φ consists of
be expressed as a superposition of the wall and target returns                                                           a weighted sum of N SCs, where each SC is given by the outer
                                                             product of a pair of left and right singular vectors multiplied       s(m, n) = sw(m, n) + st(m, n) + swt(m, n)    (24)
                                                     by its corresponding singular value. Let Ψi denote the ith SC,
where sw(m, n) denotes the wall returns, st(m, n) denotes the   given by
target returns, and swt(m, n) models the interactions (if they
exist) between the target and the wall. Since the wall reﬂections              Ψi = σiuivHi = [ψi1, . . . , ψiN]           (26)
are relatively stronger than the behind-the-wall target reﬂec-
                                                      where ψij denotes the jth column of the matrix Ψi. The rangetions, it is assumed that the wall returns mostly lie in a subspace
                                                             proﬁle associated with the ith SC can be computed asspanned by the singular vectors associated with the dominant
singular values. Therefore, discarding the singular vectors as-                    N
                                                                          1
sociated with the dominant singular values can suppress the                     ri =       IFFT(ψik)               (27)
                                              Nwall clutter in the formed image. For demonstration, we sim-                          k=1
ulate a scene with two square plate dihedrals of area 0.16 m2
                                                      where IFFT denotes the inverse fast Fourier transform. The
placed behind a homogeneous wall at coordinates (−0.6, 1.6)
                                                     main peak in a range proﬁle is used to indicate whether the
m and (0.6, 1.3) m. The homogeneous wall has a thickness of
                                           SC contains the wall or target returns, depending on the peak
0.15 m and a dielectric constant of 7.6. Here, we slightly tilt the
                                                                  location with respect to the antenna standoff distance.antenna array at an angle of 2◦with respect to the wall surface
                                                                     Fig. 8 shows the range proﬁles of the ﬁrst six SCs. The range
to produce a multidimensional wall subspace. Using SVD, we
                                                              proﬁles depicted in Fig. 8(a) and (b) show that the ﬁrst two
decompose the signal matrix Φ into a set of N SCs
                                                 SCs span the wall subspace as the distance of the main peak
                         N                         of their associated range proﬁles is less than the wall standoff
       Φ = Φw + Φt + Φwt =    σiuivHi         (25)   distance. The range proﬁles in Fig. 8(c) and (d) associated with
                                   i=1                        the third and fourth SCs have peaks beyond the wall standoff
where Φwt  is the signal matrix comprising the interactions   distance; these SCs span the target subspace. The small differ-
between the wall and the target(s). Fig. 7 illustrates the formed   ence between the location of the peak in the range proﬁle and
images of the two targets behind the wall. Fig. 7(a) shows the   the actual target range is due to the wall attenuation. Fig. 8(e)
image formed by using all N SCs in (25). Clearly, the wall   presents the range proﬁles of the ﬁfth SC (5th-SC), indicating
reﬂections and ringing effects dominate the image and obscure   that some weak wall reﬂections reside in this SC. Fig. 9 presents
the targets. Fig. 7(b) presents the image after removing the ﬁrst   images obtained from a subset of selected SCs. The image
leading SC, and Fig. 7(c) shows the image without the ﬁrst   in Fig. 9(a) is reconstructed from the 5th-SC only, and that
two dominant SCs. Discarding just the ﬁrst dominant SC elim-   depicted in Fig. 9(b) is obtained from the following subset
inates most of the wall reﬂections and the ringing effects. The   of SCs: 3rd-SC, 4th-SC, and 6th-SC. The simulation results
target image in Fig. 7(c) is further enhanced by removing the  show that, apart from the ﬁrst few dominant singular vectors,
second SC.                                                       there are other nondominant singular vectors that capture the
  Since the antenna array is not parallel to the wall surface,   wall returns. Although the nondominant wall singular vectors
the wall subspace is spanned by several singular vectors. After   interleave with the target singular vectors, their associated range
the removal of the dominant SCs, the radar signal can still   proﬁles can be used to identify them. In the next section, we
contain some wall residuals. These remaining wall returns are   propose a technique to estimate the wall subspace and introduce
captured by singular vectors associated with nondominant sin-   a subspace projection method for mitigating the wall returns
gular values, which interleave with the target singular values. To  from the radar signals.

### Página PDF 8

TIVIVE et al.: SUBSPACE PROJECTION APPROACH FOR WALL CLUTTER MITIGATION IN TWRI                                                    2115


                                                                               is [0, σmax]. Given a threshold δ ∈[0, σmax], the singular value
                                                          spectrum can be partitioned into two classes: Cw = {σi ≥δ}
                                                       and Ct = {σi < δ}. Here, we employ Otsu’s method [30],
                                                      which computes the optimum threshold δ by maximizing the
                                                             between-class variance

                                                        Σ0 = Pw(μw −μ0)2 + Pt(μt −μ0)2        (30)

                                                      where Pw and Pt are the class probabilities, μw and μt are the
                                                                    class means, and μ0 is the total mean of the classes. For more
                                                                       details on how to determine the optimum threshold of Otsu’s
                                                         method, the interested reader is referred to Appendix A.
Fig. 9.  Images formed using a subset of SCs: (a) Image obtained from the     Then, (27) is used to compute the range proﬁles associated
5th-SC only and (b) image obtained from the combination of these SCs:
                                                           with the singular values in the class Cw. Let hi denote the3rd-SC, 4th-SC, and 6th-SC.
                                                                distance of the main peak in the range proﬁle associated with
         IV. WALL CLUTTER MITIGATION METHOD           the ith singular value belonging to the wall. The wall range η
  The proposed wall clutter mitigation method is based on the   can be estimated as
assumption that the wall returns are relatively stronger than the
                                                                         η = max (hi).                   (31)
target returns, and they reside in separate subspaces. Therefore,                                                i
SVD is used to decompose the signal matrix Φ as follows:                                                 From the estimated wall range, we can now identify the remain-
   Φ =    σiuivHi +    σiuivHi +    σiuivHi      (28)   ing wall SCs and determine the singular vectors spanning the
         i∈W            i∈T           i∈N                    wall subspace. We classify a singular vector spanning the wall
                                                           subspace when the main peak of its associated range proﬁle is
where W, T , and N are the sets of indices for wall, target, and                                                                located inside the wall range η. This classiﬁcation is performed
noise singular vectors, respectively. However, not all wall SCs                                                     on all SCs of Φ, and the indices of the wall singular vectors are
will be associated with the dominant singular values. While it                                                                 stored in the index set W.
is expected that the strong wall reﬂections will be represented
by the ﬁrst few singular vectors associated with the dominant
singular values, some weak components of the wall returns   B. Wall Clutter Mitigation
may reside in a subspace spanned by other singular vectors
                                                                 After identifying the wall subspace, we remove the wall
associated with nondominant singular values. Therefore, we
                                                                   returns by projecting the radar signals onto the subspace orthog-
propose a method for estimating the wall subspace, followed
                                                             onal to the wall subspace. Similarly, the noise can be removed
by a subspace projection method for mitigating the wall returns
                                                     by projecting the radar signals onto the subspace orthogonal
from the radar signals.
                                                                    to the noise subspace. First, the radar signal is preprocessed to
                                                     remove the common signal across the array aperture. Let Φ be
A. Wall Subspace Estimation
                                                                 the matrix obtained after subtracting the mean vector from each
  The proposed estimation method for wall subspace is based  column of Φ
on the assumption that the strong reﬂections from the front and
back of the wall are captured by the ﬁrst few dominant SCs. In               Φ = Φ −meT                   (32)
[29], a similar assumption was made to estimate the time delay
                                                      where m is the mean of the columns of Φ and eT = [1, . . . , 1],of ultrawideband radar signals backscattered from a wall. First,
we estimate the wall range, i.e., the distance from the antenna  e ∈RN. Using SVD, we decompose the matrix Φ as
to the back of the wall from the range proﬁles of the dominant                           H                                                   Φ = U Σ V                      (33)SCs. Then, we classify the remaining SCs into the wall and
target classes based on their range proﬁles. The indices of the
                                                      where U = [ u1, . . . , uM], V = [ v1, . . . , vN], and Σi,i = σi.
singular vectors forming the wall SCs are stored in the index
                                                Summing the outer product of the pair of singular vectors in
set W. Let η denote the wall range. When the standoff distance                                                                 the index set W generates the wall subspace, which is given by
za and the wall thickness d are known, the wall range can be
approximated as                                                Pw =    ui vHi .                  (34)
                                                                                i∈W                  η ≈(d√ϵ + za).                  (29)
                                                   The subspace orthogonal to the wall subspace is computed as  In practice, the exact values of the wall parameters are not
readily available. Therefore, we determine the wall range from                    ⊥         H
                                                       P w = I −PwP w                  (35)
the range proﬁles associated with the dominant singular vectors.
To determine the leading singular vectors associated with the  where I denotes the identity matrix. To mitigate the wall
wall, we apply a threshold technique to segment the singular   returns, the matrix Φ is projected onto the orthogonal subspace
value spectrum into two classes, one of which is the dominant
wall singular values. Suppose that the range of singular values                Φ = P w⊥ Φ.                     (36)

### Página PDF 9

2116                                                    IEEE TRANSACTIONS ON GEOSCIENCE AND REMOTE SENSING, VOL. 53, NO. 4, APRIL 2015


  The  resulting matrix Φ  is  further processed  to remove
noise. The subspace orthogonal to the noise subspace can be
expressed as

              P n⊥ = I −PnP nH                  (37)
where Pn =   i∈N ui vHi  is the noise subspace. The pair of
left and right singular vectors, i.e., u and v, is obtained from
the SVD of Φ. Since noise is characterized by singular vectors
associated with small singular values, there are several methods    Fig. 10.  Images before and after wall clutter mitigation: (a) Image formed
to determine the noise subspace. Akaike information criterion   without wall clutter mitigation, (b) image obtained after using background
                                                                                    subtraction, and (c) image obtained with the proposed method.
(AIC) and minimum description length (MDL) methods are two
commonly used methods to estimate the noise subspace [15].                        TABLE  I
The AIC is given by                                                 IF OF THE IMAGE PRODUCED BY THE PROPOSED SUBSPACE PROJECTION
                                                     METHOD AND THE BASIC SVD-BASED METHOD WITH THE REMOVAL
                             M−i                              OF DOMINANT SCS, TESTED ON SYNTHETIC DATA                     1    M
                (M−i)   m=i+1σm
AIC(i)=N log     M          +(2M −i)i  (38)
                    m=i+1 σm

where σi is the ith singular value of Φ. Similarly, the MDL is
given by

                                M−i
                        1    M
                         m=i+1 σm                   (M−i)
MDL(i) = N log      M
                      m=i+1 σm
                          1                          where  P0 = (1/Nt)   (x,z)∈At |I0(x, z)|2,   Pj = (1/Nt)
                + 2(2M −i) log(N)i.     (39)      (x,z)∈At |Ij(x, z)|2, and I0(x, z) and Ij(x, z) denote the
                                                       formed image after background subtraction and the formed
The number of singular values belonging to the noise class is
                                                      image  after removing the  ﬁrst j dominant SCs from the
determined by minimizing the AIC or MDL. Once the wall
                                                             matrix Φ, respectively. Fig. 10 shows images formed by DSand noise subspaces are computed, the new matrix ¯Φ, which
                                                      beamforming before and after wall clutter mitigation. Without
contains the target reﬂections, is written as
                                                              wall clutter mitigation, Fig. 10(a) shows an image with strong
                     ¯Φ = P n⊥ P w⊥ Φ = Pt Φ              (40)   clutter. With background subtraction, the formed image shown
                                                                    in Fig. 10(b) is free of wall clutter; both targets are clearly
where Pt = P n⊥ P w⊥ is the target subspace projection operator.   visible. However, in practice, it is difﬁcult to have access to
Finally, DS beamforming is applied to signals of ¯Φ to form an   the measurements of the background scene devoid of targets.
image of the scene.                                               Fig. 10(c)  depicts  the image obtained with  the proposed
  The proposed method is initially tested on the simulated data   method, where the wall clutter is markedly suppressed. Table I
obtained from the scene with two dihedrals placed behind a    lists the IF and the TPR of the formed images after wall clutter
homogeneous wall. To measure the performance of the wall   mitigation. Background  subtraction obtains the highest IF
clutter mitigation method, we compute the improvement factor   of 11.14 dB, followed by the proposed subspace projection
(IF) in terms of the target-to-clutter ratio (TCR)               method with an IF of 10.09 dB. In terms of TPR, the proposed
                                                     method achieves a TPR of −3.06 dB. When the dominant SCs
                        TCRo                         are removed without the use of the proposed wall subspace                  IF = 10 log                          (41)
                         TCRi                         estimation method, the IFs of the formed images are presented
                                                               as follows. After the removal of the dominant SC from the
where TCRo and TCRi are the TCRs of the formed image                                                             matrix Φ, the IF of the formed image is 4.89 dB. Discarding the
with and without the use of a wall clutter mitigation method,
                                                                    ﬁrst two leading SCs improves the IF of the image to 9.98 dB.
respectively. The TCR of a radar image is calculated as
                                                       However, when we remove the ﬁrst three SCs from the matrix
                         1                                 Φ, the IF of the formed images decreases slightly to 7.32 dB.                                     |I(x, z)|2                     Nt    (x,z)∈At
         TCR =                                   (42)  The TPR of the formed target image also decreases markedly                         1
                    Nc                              (x,z)∈Ac |I(x, z)|2              when discarding the ﬁrst three SCs.
                                                    So far, the proposed wall clutter mitigation technique has
where At is the target region, Ac is the clutter region deﬁned                                                        been applied to a noiseless TWRI scene. The proposed method
as the entire image excluding the target region, and Nc and                                                                               is further tested under different noise levels, where the sim-
Nt are the numbers of pixels in the clutter and target regions,                                                                 ulated radar signals are corrupted by additive white Gaussian
respectively. The quality of the target image is measured in
                                                                   noise. The IF of the image formed by the proposed method is
terms of the target power ratio (TPR) given by
                                                      computed as a function of the SNR of the input signal. Fig. 11
                        Pj                                 illustrates the variations in the IF of the formed image as a
                 TPR =                         (43)
                       P0                            function of the SNR of the input signal. The IF of the formed

### Página PDF 10

TIVIVE et al.: SUBSPACE PROJECTION APPROACH FOR WALL CLUTTER MITIGATION IN TWRI                                                    2117


Fig. 11.  IF of the image as a function of the SNR of the input radar signal.


Fig. 12.  Examples of images obtained from input signal of different SNRs:
(a) Images formed using input signal with SNR of 20 dB and (b) image formed
using input signal with SNR of 40 dB.

image remains unchanged until the SNR of the input signal
decreases to 40 dB. Fig. 12 shows examples of radar images
obtained from input signal with SNRs of 20 and 40 dB. In
the next section, the subspace projection method is evaluated
on real radar data collected from a ground-based stepped-
frequency TWRI system.


               V. EXPERIMENTAL RESULTS

  Real radar signals are collected in the Radar Imaging Labora-
tory of the Center for Advanced Communications at Villanova
                                                                                   Fig. 13.  Picture of the drywall scene: (a) Image depicting the nine targets and
University, Villanova, PA, USA. An Agilent network analyzer,    (b) the ground-truth image.
Model ENA 5017B, is used to implement a stepped-frequency
waveform for synthesizing 1-D and 2-D array apertures. A
7.62 by 7.62 meter room with pyramidal foam and laminated  from the concrete wall, and a dihedral is placed at 2.1 m behind
polyurethane foam sheet absorbers on the side and back walls   the wall. An array aperture of length 1.2446 m is synthesized
is constructed for imaging. For more details about the room   with 0.0222-m interelement spacing, and a stepped-frequency
setting and the speciﬁcation of the radar system, the interested   signal covering 0.7–3.1-GHz frequency band is used to interro-
reader is referred to [6].                                         gate the scene. The second scenario involves a scene populated
                                                           with nine targets of different radar cross sections (RCSs) placed
                                                          behind the drywall. Fig. 13 shows a picture of the second scene
A. Experimental Setup
                                                       and its ground truth. The nine targets in the second scene are
  For evaluation purposes, 1-D and 2-D synthesized array   three dihedrals, four trihedrals, a sphere, and a top hat. Each
apertures are used for 2-D and 3-D TWRIs, respectively. Fur-   target is located at a certain height and position, as shown
thermore, two different TWRI scenarios are designed using   in Fig. 13(a). Its location within the scene is given in the
two types of walls: a 0.14-m-thick solid concrete wall and a   ground-truth image depicted in Fig. 13(b). A 69-antenna array
0.127-m-thick hollow drywall. The drywall is built from a   of length 1.5 m is used to interrogate the scene. The stepped-
wooden frame, which is fastened with 0.019-m plywood on one   frequency signal has a bandwidth of 1 GHz centered at 2.5 GHz.
side and 0.016-m gypsum wallboard on the other side. In the   Table II lists the characteristics of the reﬂectors used in the two
ﬁrst scenario, the radar is placed at a standoff distance of 1.16 m  TWRI scenes.

### Página PDF 11

2118                                                    IEEE TRANSACTIONS ON GEOSCIENCE AND REMOTE SENSING, VOL. 53, NO. 4, APRIL 2015


                      TABLE  II
          REFLECTORS USED IN THE TWRI EXPERIMENTS


B. Two-Dimensional TWRI

 A  line array aperture  is synthesized  for the previously
described scenes to perform 2-D imaging. Before DS beam-
forming, four different methods are used for wall clutter mitiga-
tion: background subtraction, time gating, spatial ﬁltering, and
B-scan-based SVD methods [12]–[15]. In [12]–[14], SVD is
applied to the B-scan, which is obtained by applying IFFT on
the space-frequency measurements. The ﬁrst and second dom-
inant SCs are assumed to contain the wall and target returns,
respectively. In [15], SVD is used to decompose the formed
image into a set of eigenimages. For wall clutter mitigation, the
ﬁrst dominant eigenimage is discarded. Then, an information
theoretic criteria method is used to determine the eigenimages
spanning the target subspace. In time gating, the stepped-
frequency signal is transformed into a range proﬁle. Based
on the standoff distance and the wall parameters, the radar
returns corresponding to the wall region are set to zero, and the
range proﬁle is converted back to the frequency domain. For
background subtraction, radar signals from an empty scene de-
void of target(s) are subtracted from the radar signals received
from the scene populated with target(s) before DS beamforming
is applied to reconstruct the image. Background subtraction
represents an ideal scenario, where access to the background    Fig. 14.  Image of the concrete wall scene obtained using different wall clutter
                                                                                mitigation methods: (a) No wall clutter mitigation, (b) background subtrac-
scene is available; this is not possible in real scenarios. In                                                                                           tion, (c) time gating, (d) spatial ﬁltering, (e) image-based SVD method, and
spatial ﬁltering, an inﬁnite-impulse-response notch ﬁlter is used     (f) proposed subspace projection method.
to remove zero frequency component. The frequency response
of the notch ﬁlter is deﬁned as
                                                             suppress the wall clutter because the wall reverberations and
                       1 −exp(−jω)                       target reﬂections highly overlap in the time domain. The image             H(jω) =                              (44)
                       1 −a exp(−jω)                      in Fig. 14(d) shows that spatial ﬁltering is effective in removing
                                                                 the wall reﬂections without signiﬁcantly compromising the
where ω  is the angular frequency and a(< 1) is a positive   target image. The image-based SVD method [15] produces an
constant denoting the width of the ﬁlter notch. In our experi-  image where most of the wall clutter is suppressed but the shape
ments, we deﬁne a at the point of achieving maximum IF. The   of the target is distorted compared to that shown in Fig. 14(b),
concrete wall scene, which has a dihedral, is illuminated by the   obtained using background subtraction. Fig. 14(f) illustrates the
synthesized array aperture, producing a signal matrix Φ of size  image produced by the proposed subspace projection method.
801 × 57, i.e., 801 frequencies and 57 antennas. All ﬁve wall   This image does not contain the wall clutter and is as clear as
clutter mitigation approaches, including the proposed subspace   that of the spatial ﬁltering method. Fig. 15 depicts the wall and
projection method, are used to suppress the wall clutter in the   target singular values identiﬁed by the proposed wall subspace
formed image.                                                 estimation method. The singular values depicted in Fig. 15(a)
   Fig. 14  illustrates images before and  after wall  clutter  and (b) belong to the wall and  target, respectively. From
mitigation, using different wall mitigation methods. With the   Fig. 15(a), we can see that the wall subspace comprises the
availability of the background measurements, background sub-   ﬁrst two dominant SCs and components 5, 23, 24, and 25. It is
traction produces a clear image [Fig. 14(b)] in which most of   clear from Fig. 15(a) that the nondominant wall singular values
the wall and background clutter is removed. With time gating,   interleave with the target singular values. Table III presents the
the formed image contains strong wall clutter; see Fig. 14(c).   IF in terms of TCR of the wall clutter mitigation methods for
Even though the target is far from the wall, time gating cannot   the images shown in Fig. 14. Background subtraction achieves

### Página PDF 12

TIVIVE et al.: SUBSPACE PROJECTION APPROACH FOR WALL CLUTTER MITIGATION IN TWRI                                                    2119


Fig. 15.  Singular value spectrum of (a) the wall and (b) the target subspaces
as identiﬁed by the proposed wall subspace estimation method for the scene
with a dihedral behind the concrete wall.


                     TABLE  III
      IF OF THE WALL MITIGATION METHODS TESTED ON RADAR
       DATA COLLECTED FROM THE CONCRETE WALL SCENE


the highest IF of 16.16 dB, followed by the proposed subspace
projection method with an IF of 11.01 dB. Spatial ﬁltering
gives an IF of 8.26 dB. Among the SVD methods, the image-
based SVD method gives better result than the B-scan-based
SVD method as it assumes that the target reﬂections reside in a
multidimensional subspace.
  For the drywall scene, Fig. 16 depicts the formed images
before and after wall clutter mitigation. Without any prepro-
cessing, Fig. 16(a) depicts an image with strong wall clutter.
With the availability of an empty scene, background subtraction
produces a clear radar image [Fig. 16(b)]. Time gating and
spatial ﬁltering  fail to remove the wall contributions from
the radar data [Fig. 16(c) and (d)]. The SVD methods can
hardly suppress the wall clutter in the formed radar image.
This is because the wall reﬂections are assumed to reside in
the ﬁrst SC only. However, the reﬂections backscattered from a
heterogeneous wall span a multidimensional subspace space,
as described in Section III-B. Fig. 16(e) shows the output    Fig. 16.  Image of the drywall scene obtained using different wall clutter
                                                                                mitigation methods: (a) No wall clutter mitigation, (b) background subtrac-
image of the image-based SVD method with AIC; only the    tion, (c) time gating, (d) spatial ﬁltering, (e) image-based SVD method, and
targets with large RCS are barely visible. The B-scan-based     (f) proposed subspace projection method.
SVD methods perform poorly because the wall subspace is
                                                                          TABLE IV
assumed to be 1-D. Fig. 16(f) shows the image obtained using          IF OF WALL MITIGATION METHODS BASED ON THE SCENE
the proposed wall clutter mitigation method, where most of            WITH NINE TARGETS BEHIND THE DRYWALL
the wall clutter is signiﬁcantly suppressed. Table IV lists the
IF of the images presented in Fig. 16. The proposed method
achieves the second highest IF of 22.35 dB. The B-scan-based
SVD method described in [14] gives the lowest IF of 2.08 dB.
The experimental results demonstrate that the proposed method
can be as effective as background subtraction in removing the
clutter due to both homogeneous and heterogeneous walls. In
the next section, we apply the proposed wall clutter mitigation
method to 3-D TWRI.

### Página PDF 13

2120                                                    IEEE TRANSACTIONS ON GEOSCIENCE AND REMOTE SENSING, VOL. 53, NO. 4, APRIL 2015


Fig. 17.  Three-dimensional images of the concrete wall scene: (a) Before wall clutter mitigation, after the use of (b) background subtraction, and (c) the proposed
subspace projection method. For visualization, the 3-D images are displayed in linear scale, and voxels less than −25 dB are removed.


Fig. 18.  Three-dimensional images of the drywall scene after the use of (a) background subtraction and (b) the proposed subspace projection method. For
visualization, the 3-D images are displayed in linear scale, and voxels less than −25 dB are removed.

C. Three-Dimensional TWRI                              where τn(x, z, y) is the focusing delay from the nth antenna
                                                               of the 2-D array aperture to the voxel at location (x, z, y). The  For 3-D imaging, the scene  is scanned by a 2-D array
                                                          computation of the two-way propagation delay from an antennaaperture along the horizontal and vertical directions to reveal
                                                                    to a voxel is described in [8].the properties of targets residing behind the wall, e.g., the height
                                      A 2-D array aperture is used to interrogate the concrete wallof the target. The received monochromatic signals for all M fre-
                                                       and drywall scenes. Background subtraction and the proposedquencies at each antenna location of the 2-D array aperture are
                                                           subspace projection method are then applied to mitigate thestacked to form a column of signal matrix Φ ∈CM×N, where
                                                              wall returns. We should point out that, for the sake of clar-N is the number of antenna locations in the 2-D array aperture.
                                                                                     ity, the voxels below −25 dB were thresholded in the 3-DThe order of selecting the antenna locations, i.e., processing
                                                            images. Fig. 17 illustrates the 3-D radar images of the con-rowwise or columnwise, only results in a permutation of the
                                                                    crete wall scene. Applying DS beamforming directly to thecolumns of Φ. It can be readily shown that the permutation of
                                                             space-frequency measurements produces a cluttered 3-D im-the columns of the matrix Φ does not change the column order
                                                         age [Fig. 17(a)]. Fig. 17(b) shows the image obtained fromof the left and right singular vectors, and more importantly, it
                                                        background subtraction, which does not have wall clutter. Thedoes not affect the singular values. Hence, the arrangement of
                                                      image shown in Fig. 17(c), which is produced by the proposedthe received signals into a matrix Φ does not affect the wall
                                                              wall clutter mitigation method, is as clear as that produced byand target subspaces. To form 3-D images, DS beamforming
                                                        background subtraction. For the drywall scene, the formed im-is applied to compute the complex amplitude of each voxel
                                                           ages obtained using background subtraction and the proposedI(z, x, y)
                                                     method are shown in Fig. 18; both images are free of wall
              N−1M−1                                            clutter. Table V presents the IF of the thresholded 3-D images
             1
  I(x, z, y)=           s(m, n) exp(jωmτn(x, z, y))  (45)   depicted in Figs. 17 and 18. The proposed subspace projection
      NM               n=0 m=0                               method gives an IF of 21.33 dB for the concrete wall scene

### Página PDF 14

TIVIVE et al.: SUBSPACE PROJECTION APPROACH FOR WALL CLUTTER MITIGATION IN TWRI                                                    2121


                      TABLE V                         where iδ denotes the index of the left endpoint of the interval
  IF OF THE WALL CLUTTER MITIGATION METHODS FOR 3-D IMAGING
                                                                      that includes δ, and Pw(δ) and Pt(δ) are normalizing constants
                                                             given by

                                                                   L−1                       iδ−1
                                                        Pw(δ) =    P(ξi)      Pw(δ) =     P(ξi).
                                                                                        i=iδ                      i=0
and 25.26 dB for the drywall scene, compared to background
subtraction, which yields IF values of 20.83 and 25.06 dB,  The total mean of the classes, which is independent of δ, is
respectively.                                                                  L−1
                                                                       μ0 =     ξiP(ξi).                 (48)
                    VI. CONCLUSION                                                                                       i=0
  Strong signal reﬂections from an exterior wall hinder the vis-                                                   The optimum Otsu threshold is obtained by maximizing the
ibility of stationary targets in TWRI. This paper has presented a                                                             between-class variance
comprehensive analysis of the eigenstructure of imaged TWRI
scenes. The analysis showed that, when the radar is placed                     δ = arg max {Σ0(δ)}                (49)
parallel to a homogeneous wall of uniform thickness, the wall                                     δ
returns span a 1-D subspace. However, when the antenna is not  where the between-class variance is given by
perfectly aligned with the wall surface or the wall thickness is
not uniform, which is often the case in practice, the wall re-        Σ0(δ) = Pw [μw(δ) −μ0]2 + Pt [μt(δ) −μ0]2 .
ﬂections span a multidimensional subspace. For heterogeneous
walls, the wall returns also span a multidimensional subspace.
                                                        ACKNOWLEDGMENTFurthermore, the analysis showed that the target subspace is
spanned by several singular vectors, depending on the target    The authors would like to thank Dr. F. Ahmad from the
location, target size, number of targets in the scene, and the   Center of Advanced Communications at Villanova University,
conﬁguration of the antenna array.                               Villanova, PA, USA, for providing the experimental data.
  For wall clutter mitigation, we have proposed a method that
estimates the wall subspace and a subspace projection approach
to remove, or at least signiﬁcantly suppress, the wall clutter.                    REFERENCES
The proposed approach does not assume prior knowledge of     [1] M. G. Amin, Ed., Through-the-Wall Radar Imaging.  Boca Raton, FL,
the scene nor the wall EM characteristics. It was applied to      USA: CRC Press, 2010.
                                                                                      [2] M. Amin and K. Sarabandi, “Special issue on remote sensing of building
mitigate wall clutter in 2-D and 3-D TWRIs. Experiments          interior,” IEEE Trans. Geosci. Remote Sens., vol. 47, no. 5, pp. 1267–
with simulated and real data showed that the proposed method        1268, May 2009.
was as effective as background subtraction in removing wall     [3] M. Amin, “Special issue on advances in indoor radar imaging,” J. Franklin
                                                                                                          Inst., vol. 345, no. 6, pp. 556–722, 2008.
clutter and revealing the behind-the-wall targets—without prior     [4] E. J. Baranoski, “Through-wall imaging: Historical perspective and future
knowledge of the background scene.                                            directions,” J. Franklin Inst., vol. 345, no. 6, pp. 556–569, Sep. 2008.
                                                                                      [5] M. G. Amin and F. Ahmad, “Wideband synthetic aperture beamforming
                  APPENDIX A                                         for through-the-wall imaging,” IEEE Signal Process. Mag., vol. 25, no. 4,
                                                                                    pp. 110–113, Jul. 2008.
          OTSU THRESHOLDING METHOD                        [6] R. Dilsavor et al., “Experiments on wideband through the wall imaging,”
                                                                                          in Proc. SPIE Symp. Defense Security, Algorithms Synthetic Aperture
  Suppose that we have N singular values which lie in the       Radar Imagery XII Conf., 2005, vol. 5808, pp. 196–209.
range [0, σmax], and the spectrum of singular values is divided     [7]  J. Moulton, S. A. Kassam, F. Ahmad, M. G. Amin, and K. Yemelyanov,
into L equal intervals [ξi, ξi+1), for i = 0, . . . , L −1. Let P(ξi)         “Target and change detection in synthetic aperture radar sensing of urban                                                                                            structures,” in Proc. IEEE Radar Conf., 2008, pp. 1–6.
denote the probability mass deﬁned by the relative frequency of     [8] F. Ahmad, Y. Zhang, and M. G. Amin, “Three-dimensional wideband
singular values in the ith interval, i.e.,                                 beamforming for imaging through a single wall,” IEEE Geosci. Remote
                                                                                    Sens. Lett., vol. 5, no. 2, pp. 176–179, Apr. 2008.
                               n(ξi)                                    [9] Y.-S. Yoon and M. G. Amin, “Spatial ﬁltering for wall-clutter mitigation
                     P(ξi) =                                                 in through-the-wall radar imaging,” IEEE Trans. Geosci. Remote Sens.,
                 N                                                                                             vol. 47, no. 9, pp. 3192–3208, Sep. 2009.
                                                                               [10] M. Dehmollaian and K. Sarabandi, “Analytical, numerical, and experi-
where n(ξi) is the number of singular values σi ∈[ξi, ξi+1).                                                                              mental methods for through-the-wall radar imaging,” in Proc. IEEE Int.
For a given threshold τ = ξk, k = 0, . . . , L −1, the spectrum        Conf. Acoust., Speech Signal Process., 2008, pp. 5181–5184.
of singular values can be partitioned into two classes: Cw =    [11] M. Dehmollaian and K. Sarabandi, “Refocusing through building walls
{σi ≥δ} and Ct = {σi < δ}. The class means of Cw and Ct         using synthetic aperture radar,” IEEE Trans. Geosci. Remote Sens.,                                                                                             vol. 46, no. 6, pp. 1589–1599, Jun. 2008.
are respectively                                                            [12] A. N. Gaikwad, D. Singh, and M. J. Nigam, “Study of effect of room
                                                                  window on through wall imaging in UWB range,” in Proc. Int. Conf.
                           L−1                                 Emerging Trends Electron. Photon. Devices Syst., 2009, pp. 395–398.                       1
              μw(δ) =           ξiP(ξi)            (46)    [13] R. Chandra, A. N. Gaikwad, D. Singh, and M. J. Nigam, “An approach to
                    Pw(δ)                                      remove the clutter and detect the target for ultra-wideband through-wall                                    i=iδ
                                 iδ−1                                      imaging,” J. Geophys. Eng., vol. 5, no. 4, pp. 412–419, Dec. 2008.
                       1                                           [14] P. K. Verma, A. N. Gaikwad, D. Singh, and M. J. Nigam, “Analysis of
                μt(δ) =           ξiP(ξi)             (47)          clutter reduction techniques for through wall imaging in UWB range,”                       Pt(δ)                               i=0                                      Progress Electromagnet. Res. B, vol. 17, pp. 29–48, 2009.

### Página PDF 15

2122                                                    IEEE TRANSACTIONS ON GEOSCIENCE AND REMOTE SENSING, VOL. 53, NO. 4, APRIL 2015


[15] M. M. Riaz and A. Ghafoor, “Through-wall image enhancement based on                       Abdesselam Bouzerdoum (M’89–SM’03) received
     singular value decomposition,” Int. J. Antennas Propag., vol. 2012, pp. 1–                             the M.Sc. and Ph.D. degrees in electrical engineering
     20, 2012, Article ID 961829.                                                                fromtheUniversityofWashington,Seattle,WA,USA.
[16] P. Setlur, M. G. Amin, and F. Ahmad, “Analysis of micro-Doppler signals                               In 1991, he joined The University of Adelaide,
     using linear FM basis decomposition,” in Proc. SPIE Radar Sens. Technol.                            Adelaide, Australia, and in 1998, he was an Asso-
     X, 2006, vol. 6210, pp. 621 00M 1–621 00M 11.                                                          ciate Professor with Edith Cowan University, Perth,
[17] Y. Kim and H. Ling, “Human activity classiﬁcation based on micro-                               Australia. Since 2004, he has been with the Univer-
     Doppler signatures using a support vector machine,” IEEE Trans. Geosci.                                 sity of Wollongong, Wollongong, Australia, as Pro-
    Remote Sens., vol. 47, no. 5, pp. 1328–1337, May 2009.                                                fessor of computer engineering, where he also served
[18] F. Ahmad, M. G. Amin, and P. Setlur, “Through-the-wall target lo-                             as the Head of the School of Electrical, Computer
      calization using dual-frequency CW radars,” in Proc. SPIE Sens. C3I                         and Telecommunications Engineering (2004–2006)
     Technol. Homeland Security Homeland Defense V, 2006, vol. 6201,   and the Associate Dean of Research (2007–2013). From 2009 to 2011, he
     pp. 620 10H 1–620 10H 12.                                      was a Member of the Australian Research Council College of Experts and
[19] F. Abujarad, A. Jostingmeier, and A. S. Omar, “Clutter removal for land-   served as Deputy Chair of the Engineering, Mathematics and Informatics panel
    mine using different signal processing techniques,” in Proc. 10th Int.   from 2010 to 2011. He has published over 300 technical papers and graduated
     Conf. Ground Penetrating Radar, 2004, pp. 697–700.                   34 Ph.D. and Research Masters students.
[20] F. Abujarad, G. Nadimy, and A. Omar, “Clutter reduction and detection of      Dr. Bouzerdoum was the recipient of numerous awards and prizes, including
     landmine objects in ground penetrating radar data using singular value de-   a Distinguished Researcher Award (Chercheur de Haut Niveau) from the French
     composition (SVD),” in Proc. 3rd Int. Workshop Adv. Ground Penetrating   Ministry of Research in 2001, the Chester Sall Award in 2005, and the Eureka
     Radar, 2005, pp. 37–42.                                                   Prize for Outstanding Science in Support of Defence or National Security in
[21] F. H. C. Tivive, M. G. Amin, and A. Bouzerdoum, “Wall clutter mitigation   2011. He served as Associate Editor for four international journals, includ-
     based on eigen-analysis in through-the-wall radar imaging,” in Proc. Int.    ing the IEEE TRANSACTIONS ON SYSTEMS, MAN, AND CYBERNETICS
     Conf. Digital Signal Process., 2011, pp. 1–8.                             (1999–2006).
[22] F. H. C. Tivive, A. Bouzerdoum, and M. G. Amin, “An SVD-based ap-
     proach for mitigating wall reﬂections in through-the-wall radar imaging,”
      in Proc. IEEE Radar Conf., 2011, pp. 519–524.                                           Moeness G. Amin (S’82–SM’91–M’93–F’01) re-
[23] L.-P. Song, C. Yu, and Q. H. Lui, “Through-wall imaging (TWI) by radar:                            ceived the Ph.D. degree in electrical engineering
    2-D tomographic results and analysis,” IEEE Trans. Geosci. Remote Sens.,                         from the University of Colorado, Boulder, CO, USA,
      vol. 43, no. 12, pp. 2793–2798, Dec. 2005.                                                              in 1984.
[24] M. Dehmollaian, M. Thiel, and K. Sarabandi, “Through-the-wall imaging                             Since 1985, he has been a Faculty Member with
     using differential SAR,” IEEE Trans. Geosci. Remote Sens., vol. 47, no. 5,                             the Department of Electrical and Computer Engi-
     pp. 1289–1296, May 2009.                                                                           neering, Villanova University, Villanova, PA, USA,
[25] M. Amin and F. Ahmad, “Compressive sensing for through the wall radar                           where, in 2002, he became the Director of the Center
     imaging,” J. Electron. Imag., vol. 22, no. 3, pp. 1–21, Jul. 2013.                                         for Advanced Communications, College of Engi-
[26] S. M. Li and X. F. Liu, “Robust adaptive beamforming imaging approach                              neering. He has over 600 journal and conference
      for stepped-frequency through-the-wall radar,” Appl. Mech. Mater., Mech.                             publications in the areas of wireless communica-
     Electron. Eng. III, vol. 130–134, pp. 45–49, 2011.                             tions, time–frequency analysis, sensor array processing, waveform design and
[27] Y.-S. Yoon and M. G. Amin, “High-resolution through-the-wall radar    diversity, interference cancellation in broadband communication platforms,
     imaging using beamspace music,” IEEE Trans. Antennas Propag., vol. 56,    satellite navigations, target localization and tracking, direction ﬁnding, channel
     no. 6, pp. 1763–1774, Jun. 2008.                                              diversity and equalization, ultrasound imaging, and radar signal processing. He
[28] C. A. Balanis, Advanced Engineering Electromagnetics. New York, NY,   coauthored 18 book chapters. He is the Editor of the book Through the Wall
    USA: Wiley, 1989.                                              Radar Imaging (CRC Press, 2011) and Compressive Sensing for Urban Radar
[29] P. Protiva, J. Mrkvica, and J. Macháˇc, “Time delay estimation of UWB   (CRC Press, 2014). He was a Guest Editor of the Journal of Franklin Institute
     radar signals backscattered from a wall,” Microw. Opt. Technol. Lett.,   September 2008 special issue on Advances in Indoor Radar Imaging; Insti-
      vol. 53, no. 6, pp. 1444–1450, Jun. 2011.                                      tute of Engineering and Technology (IET) Signal Processing December 2009
[30] N. Otsu, “A threshold selection method for gray level histograms,” IEEE    special issue on Time–Frequency Approach to Radar Detection, Imaging, and
     Trans. Syst. , Man, Cybern., vol. SMC-9, no. 1, pp. 62–66, Jan. 1979.        Classiﬁcation; and the European Association for Signal Processing (EURASIP)
                                                                           Journal on Advances in Signal Processing, special issue on Sparse Sensing in
                                                                     Radar and Sonar Signal Processing in 2014.
                                                                                  Dr. Amin is a Fellow of the International Society of Optical Engineering
                                                                                     in 2007 and the IET in 2010. He was a recipient of the Villanova University
                                                                          Outstanding Faculty Research Award in 1997, the IEEE Philadelphia Section
                                                               Award in 1997, the IEEE Third Millennium Medal in 2000, the 2009 Individual
                                                                             Technical Achievement Award from the EURASIP, the 2010 NATO Scientiﬁc
                                                                     Achievement Award, and the Chief of Naval Research Challenge Award in
                                                                         2010. He was a Distinguished Lecturer of the IEEE Signal Processing Society
                                                                                     in 2003–2004 and is currently the Chair of the Electrical Cluster of the Franklin
                                                                                           Institute Committee on Science and the Arts. He was a Plenary Speaker at IEEE
                                                                                    International Symposium on Signal Processing and Information Technology
                                                                  2003 (ISSPIT-03), the 2010 IEEE International Conference on Acoustics,
                                                                     Speech and Signal Processing, The 29th International Review of Progress
                   Fok Hing Chi Tivive (M’02) received the Ph.D.                                                                                     in Applied Computational Electromagnetics 2013 (ACES-13), IET 2013, the
                        degree in computer engineering from the University                                                                  2013 European Signal Processing Conference, Statistics, Optimization, and
                         of Wollongong, Wollongong, Australia, in 2006.                                                                             Signal Processing Workshop 2013 (STATOS-13), IEEE International Work-
                          Since 2006, he has been a Postdoctoral Research                                                                      shop on Computational Advances in Multi-Sensor Adaptive Processing 2013
                       Fellow with the School of  Electrical, Computer                                                              (CAMSAP-13), and International Radar Conference 2014 (RADAR-14). He
                      and Telecommunications Engineering, University of                                                                was a Guest Editor of the IEEE TRANSACTIONS ON GEOSCIENCE AND
                      Wollongong. His research interests include machine
                                                      REMOTE SENSING May 2009 Special Issue on Remote Sensing of Building
                           learning, pattern recognition, image processing, and
                                                                                        Interior and the IEEE SIGNAL PROCESSING MAGAZINE November 2013 and
                         through-the-wall radar imaging.
                                                                               July 2014 Special Issues on Time–Frequency Analysis and Applications, and
                                                                       Recent Advances in Synthetic Aperture Radar Imaging.
