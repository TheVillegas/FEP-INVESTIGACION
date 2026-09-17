# -*- coding: utf-8 -*-
"""FP-180 — Add the eight additional alternatives to the comparison matrix.

FP-51 does not ask for the alternatives to be listed, it asks for them to be
compared: "Las alternativas son comparadas bajo el mismo escenario." FP-126
registered them and FP-179 audited them, but the matrix never scored them.

This pass adds the eight, investigated against official documentation on
2026-09-16 and scored under the same methodology as the rest of the population.

Rules applied, unchanged from the existing matrix
-------------------------------------------------
* A cell with no evidence in official or project-approved sources is NE with its
  reason recorded. Never blank, never invented.
* Commercial-only evidence caps the indicator at 1 (FP-177 section 2.1).
* No indicator reaches 3: that needs double evidence and this pass has only
  primary documentation.
* Scenario-dependent indicators are scored only in the product's anchor
  scenario; elsewhere they are NE pending their own scenario evidence.

Two findings worth the team's attention are recorded as notes, not as scores:
Densify confirms the reservation FP-179 already raised, and IBM Cloud Cost
Estimator sits in a category whose scenario it does not serve.

Usage: python add_alternatives.py
"""
from __future__ import annotations

import datetime as dt
import shutil
import sys
from pathlib import Path

import openpyxl

from apply_scope_corrections import (BASE_W, evaluate, read_scores,
                                     rebuild_charts, write_results_sheet)

HERE = Path(__file__).resolve().parent
WORKBOOK = HERE / "FP-180_matriz_comparativa.xlsx"
REPORT = HERE / "alternativas-adicionales.md"
VERIFIED = "2026-09-16"

SCENARIO_INDEPENDENT = {"V2", "O2", "AU2", "M1", "M2", "AD2", "P1", "D1", "D2"}
INDICATOR_ORDER = ["V1", "V2", "A1", "A2", "O1", "O2", "AU1", "AU2", "M1", "M2",
                   "I1", "I2", "AD1", "AD2", "P1", "P2", "D1", "D2"]
CRITERION_OF = {"V": "Visibilidad", "A": "Asignacion", "O": "Optimizacion",
                "AU": "Automatizacion", "M": "Multicloud", "I": "Integracion",
                "AD": "Adopcion", "P": "Precio", "D": "Dependencia"}

# Eligible scenarios per category, matching how the base population was set up.
SCENARIOS_BY_CATEGORY = {
    "Cloud nativa": ["E1", "E2", "E3", "E5", "E6"],
    "Multicloud": ["E1", "E2", "E5", "E6"],
    "Kubernetes": ["E3", "E5"],
    "Estimacion temprana": ["E4"],
}
ANCHOR_BY_CATEGORY = {"Cloud nativa": "E1", "Multicloud": "E2",
                      "Kubernetes": "E3", "Estimacion temprana": "E4"}

PENDING = ("Pendiente de investigacion propia del escenario: el indicador depende del "
           "escenario y la evidencia recogida corresponde al escenario ancla del producto.")

# product -> (category, note for the team or None, {indicator: (value, type, evidence, source)})
ALTERNATIVES = {
    "OCI Cost Analysis": ("Cloud nativa", None, {
        "V1": (2, "Oficial",
               "Cost Analysis es «an easy-to-use visualization tool to help you track and "
               "optimize your Oracle Cloud Infrastructure spending», que permite generar "
               "graficos y descargar «tabular reports of aggregated cost data», filtrando y "
               "agrupando por servicio, etiqueta y periodo.",
               "https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm"),
        "V2": (2, "Oficial",
               "Los Cost Reports «contain one row per each Oracle Cloud Infrastructure "
               "resource per hour along with consumption information (usage, price, cost), "
               "metadata, and tags», lo que permite rastrear un total hasta el registro por "
               "recurso y hora.",
               "https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costusagereportsoverview.htm"),
        "A1": (1, "Oficial",
               "Las cost-tracking tags y los compartimentos permiten atribuir gasto: «By "
               "attaching cost-tracking tags to different resources, you can query cost data "
               "by filtering with tags rather than compartments». No se encontro "
               "documentacion de calculo de gasto no asignado, que el ancla 2 exige, por lo "
               "que queda en practica basica.",
               "https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/usingcosttrackingtags.htm"),
        "A2": ("NE", "Pendiente",
               "No se encontro documentacion oficial de reglas de reparto de costo compartido "
               "o multi-tenant en OCI Cost Analysis.", ""),
        "O1": (2, "Oficial",
               "Cloud Advisor «analyzes the OCI cloud resources of every tenancy, and provides "
               "recommendations to maximize cost savings»; las recomendaciones de gestion de "
               "costos identifican recursos infrautilizados y proponen rightsizing.",
               "https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/recommendations-costmanagement.htm"),
        "O2": (1, "Oficial",
               "Existe documentacion para implementar las recomendaciones de Cloud Advisor, "
               "pero no se encontro evidencia de un ciclo documentado de medicion o "
               "seguimiento del ahorro realizado.",
               "https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/cloudadvisor-implementing_cloud_advisor_recommendations.htm"),
        "AU1": (1, "Oficial",
                "Los budgets permiten «set soft limits on your Oracle Cloud Infrastructure "
                "spending» con alertas al acercarse al limite. Segun la prevencion de doble "
                "conteo de FP-177, una alerta no es una accion ejecutada, y la implementacion "
                "de recomendaciones es manual asistida.",
                "https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/budgetsoverview.htm"),
        "AU2": ("NE", "Pendiente",
                "No se encontro documentacion oficial de salvaguardas de ejecucion "
                "(aprobacion, reversion o limites previos a actuar) para acciones de costo.", ""),
        "M1": (0, "Oficial (ausencia verificada)",
               "Cost Analysis opera sobre la tenancy de Oracle Cloud Infrastructure; la "
               "documentacion de facturacion no describe consolidacion de cuentas de otros "
               "proveedores. Criterio aplicado igual que a los demas productos nativos.",
               "https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/billingoverview.htm"),
        "M2": (0, "Oficial (ausencia verificada)",
               "Mismo alcance de diseno que M1: al no consolidar otros proveedores, no expone "
               "diferencias semanticas entre ellos.",
               "https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/billingoverview.htm"),
        "I1": (2, "Oficial",
               "El acceso a los datos esta documentado por multiples interfaces: «You can "
               "access Oracle Cloud Infrastructure using the Oracle Cloud Infrastructure "
               "Console (a browser-based interface), the Command Line Interpreter (CLI), the "
               "REST API, or the OCI Terraform Provider».",
               "https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Concepts/cloudadvisoroverview.htm"),
        "I2": (2, "Oficial",
               "La documentacion describe reportes programados: «Use the Scheduled reports "
               "page to generate scheduled reports based on saved reports from Cost "
               "Analysis», lo que integra la salida al flujo de reporte periodico.",
               "https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm"),
        "AD1": (2, "Oficial",
                "El acceso se controla por politicas IAM por servicio e interfaz: «Each "
                "service in Oracle Cloud Infrastructure integrates with IAM for "
                "authentication and authorization, for all interfaces», con permisos "
                "granulares a nivel de compartimento.",
                "https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/customizing-policies.htm"),
        "AD2": (2, "Oficial",
                "Oracle publica guia de adopcion y gobernanza de costos en su Cloud Adoption "
                "Framework y en el Well-Architected Framework, con practicas de seguimiento y "
                "gestion de uso y costo.",
                "https://docs.oracle.com/en-us/iaas/Content/cloud-adoption-framework/era-cost-management.htm"),
        "P1": (2, "Oficial",
               "Los cost reports exponen «usage, price, cost» por recurso y hora junto con "
               "metadatos y etiquetas, de modo que precio, unidad y periodo quedan visibles y "
               "reproducibles.",
               "https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costusagereportsoverview.htm"),
        "P2": ("NE", "Pendiente",
               "No se encontro en Cost Analysis una funcion documentada de estimacion o "
               "comparacion de componentes de precio; Oracle ofrece un estimador de costos "
               "como producto aparte, no incluido en la poblacion.", ""),
        "D1": (2, "Oficial",
               "Cost Analysis permite «download accurate, reliable tabular reports» y los "
               "cost reports se entregan como archivos por recurso y hora, disponibles para "
               "descarga.",
               "https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/download-cost-csv.htm"),
        "D2": ("NE", "Pendiente",
               "No se encontro documentacion oficial sobre dependencias propietarias ni "
               "camino de salida o configuracion reversible.", ""),
    }),

    "IBM Cloud Cost Estimator": ("Cloud nativa",
        "Tension de clasificacion registrada para el equipo: FP-126 y FP-179 lo situan entre "
        "las herramientas nativas, cuya categoria ancla en E1 (visibilidad y asignacion en "
        "nube unica), pero su funcion documentada es la estimacion previa al despliegue. Sus "
        "indicadores de visibilidad y asignacion se puntuan 0 por ausencia verificada, no por "
        "deficiencia del producto. Se sugiere revisar si corresponde reubicarlo en estimacion "
        "temprana, igual que la tension ya registrada para Cloud Custodian.", {
        "V1": (0, "Oficial (ausencia verificada)",
               "Es un calculador de precios para «configure IBM Cloud products and generate "
               "reliable cost estimates»; no desglosa costo y uso reales por cuenta, servicio "
               "y periodo.",
               "https://cloud.ibm.com/docs/account?topic=account-cost"),
        "V2": (0, "Oficial (ausencia verificada)",
               "Al operar sobre estimaciones previas al despliegue, no rastrea ni reconcilia "
               "contra la facturacion real de una cuenta.",
               "https://cloud.ibm.com/docs/account?topic=account-cost"),
        "A1": (0, "Oficial (ausencia verificada)",
               "No calcula asignacion de gasto por responsable o centro de costo; entrega una "
               "estimacion por configuracion de producto.",
               "https://cloud.ibm.com/docs/account?topic=account-cost"),
        "A2": (0, "Oficial (ausencia verificada)",
               "Mismo alcance que A1: no define reglas de reparto de costo compartido.",
               "https://cloud.ibm.com/docs/account?topic=account-cost"),
        "O1": (1, "Comercial",
               "La pagina de producto declara que la herramienta permite «get tips on how to "
               "save money». Es evidencia comercial del proveedor, por lo que FP-177 limita "
               "el indicador a 1.",
               "https://www.ibm.com/products/cloud/cloud-calculator"),
        "O2": ("NE", "Pendiente",
               "No se encontro documentacion de explicacion de impacto ni seguimiento de una "
               "recomendacion de optimizacion.", ""),
        "AU1": (0, "Oficial (ausencia verificada)",
                "Es una calculadora de estimacion: no ejecuta ni bloquea acciones o politicas "
                "de costo.",
                "https://cloud.ibm.com/docs/account?topic=account-cost"),
        "AU2": ("NA", "Justificacion de alcance",
                "Al no ejecutar acciones (ver AU1), no aplica evaluar salvaguardas de una "
                "ejecucion automatizada.", ""),
        "M1": (0, "Oficial (ausencia verificada)",
               "Estima exclusivamente productos del catalogo de IBM Cloud; no consolida "
               "costos de otros proveedores.",
               "https://cloud.ibm.com/docs/account?topic=account-cost"),
        "M2": (0, "Oficial (ausencia verificada)",
               "Mismo alcance de diseno que M1.",
               "https://cloud.ibm.com/docs/account?topic=account-cost"),
        "I1": (2, "Oficial",
               "La estimacion se integra al flujo de proyectos y arquitecturas desplegables: "
               "«After saving, the validation checks are run and a new cost estimate is "
               "computed», tomando los parametros configurados del proyecto.",
               "https://cloud.ibm.com/docs/secure-enterprise?topic=secure-enterprise-cost-estimate-project"),
        "I2": (2, "Oficial",
               "El costo estimado forma parte del paso de validacion previo al despliegue, "
               "presentado en el «validation modal» bajo la seccion «Cost estimate "
               "successful», de modo que queda incorporado al flujo de revision del proyecto.",
               "https://cloud.ibm.com/docs/secure-enterprise?topic=secure-enterprise-cost-estimate-project"),
        "AD1": ("NE", "Pendiente",
                "No se encontro documentacion oficial sobre roles y accesos diferenciados "
                "para los perfiles del escenario.", ""),
        "AD2": ("NE", "Pendiente",
                "No se encontro guia oficial de habilitacion, ownership o seguimiento de uso "
                "sostenido asociada a la herramienta.", ""),
        "P1": (2, "Oficial",
               "Permite configurar plan de precios, uso, moneda y region, y «see how your "
               "pricing is determined». Los supuestos estan declarados: la estimacion «does "
               "not include all resources, usage, licenses, fees, discounts, or taxes» y esta "
               "«subject to change as the architecture is customized».",
               "https://cloud.ibm.com/docs/secure-enterprise?topic=secure-enterprise-cost-estimate-project"),
        "P2": (2, "Oficial",
               "La documentacion describe la comparacion de configuraciones alternativas "
               "antes de decidir, con el detalle de como se determina cada precio.",
               "https://cloud.ibm.com/docs/account?topic=account-cost"),
        "D1": (2, "Oficial",
               "Las estimaciones se pueden exportar y descargar como cotizacion desde la "
               "herramienta.",
               "https://cloud.ibm.com/docs/account?topic=account-cost"),
        "D2": ("NE", "Pendiente",
               "No se encontro documentacion sobre dependencias propietarias ni camino de "
               "salida.", ""),
    }),

    "Harness Cloud Cost Management": ("Multicloud", None, {
        "V1": (2, "Oficial",
               "Las Perspectives permiten «group resources by what matters most to your "
               "business and create tailored views for engineering, finance, or leadership, "
               "all in one powerful, shareable dashboard».",
               "https://developer.harness.io/docs/cloud-cost-management/get-started/overview/"),
        "V2": ("NE", "Pendiente",
               "No se encontro documentacion oficial sobre trazabilidad o reconciliacion de "
               "un total hasta los registros de facturacion del proveedor.", ""),
        "A1": (2, "Oficial",
               "Las Cost Categories «enable you to use cost data across multiple sources and "
               "attribute it to business contexts», que es atribucion por entidad "
               "organizacional con reglas definidas.",
               "https://developer.harness.io/docs/cloud-cost-management/get-started/overview/"),
        "A2": ("NE", "Pendiente",
               "No se encontro documentacion oficial de reglas de reparto de costo compartido "
               "o multi-tenant.", ""),
        "O1": (2, "Oficial",
               "La deteccion de anomalias es «ML-powered detection of unusual spending "
               "patterns with configurable sensitivity», con modelo de series de tiempo sobre "
               "42 dias de historico, y AutoStopping identifica recursos ociosos.",
               "https://developer.harness.io/docs/cloud-cost-management/cost-governance/anomalies/getting-started-with-ccm-anomaly-detection"),
        "O2": ("NE", "Pendiente",
               "No se encontro documentacion del ciclo de explicacion de impacto y seguimiento "
               "del ahorro realizado por recomendacion.", ""),
        "AU1": (2, "Oficial",
                "AutoStopping «automatically stops idle non-production resources based on "
                "traffic or schedules» y soporta EC2, ECS, RDS, maquinas virtuales de Azure y "
                "clusteres GKE: es ejecucion automatizada, no solo recomendacion.",
                "https://developer.harness.io/docs/cloud-cost-management/get-started/overview/"),
        "AU2": ("NE", "Pendiente",
                "No se encontro documentacion oficial de aprobacion, reversion o limites "
                "previos a la ejecucion automatica.", ""),
        "M1": (2, "Oficial",
               "La documentacion tecnica declara cobertura simultanea de varios proveedores: "
               "AutoStopping «supports EC2, ECS, RDS, Azure VMs, and GKE clusters», y las "
               "Cost Categories operan «across multiple sources».",
               "https://developer.harness.io/docs/cloud-cost-management/get-started/overview/"),
        "M2": ("NE", "Pendiente",
               "No se encontro documentacion de normalizacion ni de diferencias semanticas "
               "declaradas entre proveedores.", ""),
        "I1": (2, "Oficial",
               "La plataforma ingiere datos de costo de multiples proveedores para construir "
               "Perspectives y Cost Categories, y opera sobre recursos de AWS, Azure y GCP.",
               "https://developer.harness.io/docs/cloud-cost-management/"),
        "I2": (2, "Oficial",
               "La deteccion de anomalias incluye «automated alerts to catch cost spikes "
               "early» y gestion de estado (Active, Resolved, Archived); Asset Governance "
               "permite gestionar el gasto «using asset governance rules and budgets».",
               "https://developer.harness.io/docs/cloud-cost-management/cost-governance/anomalies/getting-started-with-ccm-anomaly-detection"),
        "AD1": ("NE", "Pendiente",
                "No se encontro documentacion oficial de roles y accesos por perfil para el "
                "escenario multinube.", ""),
        "AD2": ("NE", "Pendiente",
                "No se encontro guia oficial de habilitacion, ownership o medicion de "
                "adopcion sostenida.", ""),
        "P1": ("NE", "Pendiente",
               "No se encontro documentacion sobre exposicion de precio, moneda, region, "
               "unidad y supuestos de los costos analizados.", ""),
        "P2": ("NE", "Pendiente",
               "No se encontro documentacion de estimacion o comparacion contextual de "
               "componentes de precio.", ""),
        "D1": ("NE", "Pendiente",
               "No se encontro documentacion oficial de exportacion o API de salida de los "
               "datos de costo.", ""),
        "D2": ("NE", "Pendiente",
               "No se encontro documentacion sobre dependencias propietarias ni camino de "
               "salida.", ""),
    }),

    "Densify": ("Multicloud",
        "Reserva de FP-179 confirmada: la auditoria de alternativas advirtio que Densify no "
        "queda validado como plataforma FinOps multinube. La documentacion revisada en esta "
        "pasada lo confirma: el producto se presenta como Kubex, «full-stack AI-driven K8s "
        "resource optimization, from container to node to scale group», es decir optimizacion "
        "de recursos de Kubernetes y no gestion financiera multinube. Sus indicadores de "
        "visibilidad, asignacion y multinube se puntuan 0 por ausencia verificada frente al "
        "alcance de E2. Se mantiene en la poblacion por decision de la matriz final de "
        "FP-126, y su inclusion no valida la capacidad de la categoria.", {
        "V1": (0, "Oficial (ausencia verificada)",
               "La documentacion describe optimizacion de recursos de contenedores y nodos; "
               "el modelado de costos se limita a estimar el costo de contenedores sin "
               "requests definidos. No desglosa costo y uso por cuenta, servicio y periodo "
               "entre proveedores, que es lo que E2 evalua.",
               "https://www.densify.com/docs/WebHelp_Densify_Cloud/Content/Densify_Com/Optimizing_Your_Containers.htm"),
        "V2": (0, "Oficial (ausencia verificada)",
               "No rastrea totales hasta la fuente de facturacion: opera sobre metricas de "
               "utilizacion de contenedores y nodos.",
               "https://www.densify.com/docs/WebHelp_Densify_Cloud/Content/Densify_Com/Optimizing_Your_Containers.htm"),
        "A1": (0, "Oficial (ausencia verificada)",
               "No es una herramienta de asignacion de gasto organizacional; su unidad de "
               "analisis es el contenedor, el pod y el nodo.",
               "https://www.densify.com/product/container-and-kubernetes-resource-optimizer/"),
        "A2": (0, "Oficial (ausencia verificada)",
               "Mismo alcance que A1: no define reglas de reparto de costo compartido entre "
               "entidades organizacionales.",
               "https://www.densify.com/product/container-and-kubernetes-resource-optimizer/"),
        "O1": (2, "Oficial",
               "Aprende los patrones de utilizacion de contenedores y pods y «determine the "
               "optimal request and limit values», ademas de recomendar tipos de nodo segun "
               "el patron de carga.",
               "https://www.densify.com/docs/WebHelp_Densify_Cloud/Content/Densify_Com/Optimizing_Your_Containers.htm"),
        "O2": ("NE", "Pendiente",
               "No se encontro documentacion del ciclo de medicion o seguimiento del ahorro "
               "efectivamente realizado.", ""),
        "AU1": (2, "Oficial",
                "La automatizacion «continuously monitors the resources your applications are "
                "actually using and adjusts resource settings in real-time», lo que constituye "
                "ejecucion y no solo recomendacion.",
                "https://www.densify.com/docs/WebHelp_Densify_Cloud/Content/Densify_Com/Optimizing_Your_Containers.htm"),
        "AU2": ("NE", "Pendiente",
                "No se encontro documentacion de aprobacion, reversion o limites previos al "
                "ajuste automatico de recursos.", ""),
        "M1": (0, "Oficial (ausencia verificada)",
               "La documentacion no describe consolidacion de facturacion entre proveedores "
               "bajo un esquema declarado; el producto opera sobre clusteres de Kubernetes.",
               "https://www.densify.com/product/container-and-kubernetes-resource-optimizer/"),
        "M2": (0, "Oficial (ausencia verificada)",
               "Al no consolidar facturacion multiproveedor, no expone diferencias semanticas "
               "entre proveedores.",
               "https://www.densify.com/product/container-and-kubernetes-resource-optimizer/"),
        "I1": ("NE", "Pendiente",
               "No se encontro documentacion oficial de conectores de ingesta de datos de "
               "facturacion por proveedor.", ""),
        "I2": ("NE", "Pendiente",
               "No se encontro documentacion oficial de integracion con el flujo operativo "
               "del escenario multinube.", ""),
        "AD1": ("NE", "Pendiente",
                "No se encontro documentacion oficial de roles y accesos por perfil.", ""),
        "AD2": ("NE", "Pendiente",
                "No se encontro guia oficial de habilitacion o gobernanza para uso sostenido.", ""),
        "P1": ("NE", "Pendiente",
               "No se encontro documentacion sobre exposicion de precio, moneda, region, "
               "unidad y supuestos.", ""),
        "P2": ("NE", "Pendiente",
               "No se encontro documentacion de estimacion o comparacion de componentes de "
               "precio.", ""),
        "D1": ("NE", "Pendiente",
               "No se encontro documentacion oficial de exportacion o API de salida de datos.", ""),
        "D2": ("NE", "Pendiente",
               "No se encontro documentacion sobre dependencias propietarias ni camino de "
               "salida.", ""),
    }),

    "PerfectScale": ("Kubernetes", None, {
        "V1": (2, "Oficial",
               "Entrega «a detailed multi-cloud, multi-cluster view of your K8s spending based "
               "on actual resource utilization», con capacidad de senalar areas problematicas "
               "y priorizar acciones.",
               "https://docs.perfectscale.io/"),
        "V2": ("NE", "Pendiente",
               "No se encontro documentacion de trazabilidad de un total hasta los registros "
               "de facturacion del proveedor.", ""),
        "A1": ("NE", "Pendiente",
               "La documentacion revisada describe visibilidad de gasto por cluster, pero no "
               "un calculo de gasto asignado y no asignado por responsable o entidad.", ""),
        "A2": ("NE", "Pendiente",
               "No se encontro documentacion de reglas de reparto de costo compartido entre "
               "equipos o tenants.", ""),
        "O1": (2, "Oficial",
               "PodFit realiza dimensionamiento vertical de pods e InfraFit dimensionamiento "
               "de nodos, aplicando «data-driven recommendations» sobre utilizacion real.",
               "https://docs.perfectscale.io/visibility-and-optimization/podfit-or-vertical-pod-right-sizing"),
        "O2": ("NE", "Pendiente",
               "No se encontro documentacion del ciclo de medicion del ahorro realizado tras "
               "aplicar una recomendacion.", ""),
        "AU1": (2, "Oficial",
                "La automatizacion de PodFit «continuously optimizes your Kubernetes "
                "environment by autonomously adjusting workloads' CPU and memory to optimal "
                "values [...] without the need for manual intervention», con soporte de "
                "redimensionamiento en sitio a partir de Kubernetes 1.33.",
                "https://docs.perfectscale.io/enable-automation/introduction-to-automation"),
        "AU2": (2, "Oficial",
                "Las politicas de optimizacion acotan el comportamiento antes de actuar: "
                "MaxSavings, Balanced (por defecto, «optimally balances cost and "
                "resiliency»), ExtraHeadroom y MaxHeadroom, configurables por entorno.",
                "https://docs.perfectscale.io/enable-automation/automation-customization"),
        "M1": (1, "Oficial",
               "La documentacion declara una vista «multi-cloud, multi-cluster» del gasto de "
               "Kubernetes, pero no describe un esquema declarado de normalizacion de "
               "facturacion entre proveedores, que es lo que el ancla 2 exige.",
               "https://docs.perfectscale.io/"),
        "M2": ("NE", "Pendiente",
               "No se encontro documentacion sobre diferencias semanticas o limites de "
               "cobertura declarados por proveedor.", ""),
        "I1": (2, "Oficial",
               "El agente ps-agent requiere permisos RBAC especificos para «provide insights "
               "and take automated actions», lo que documenta la ingesta de datos del cluster "
               "exigida por el escenario.",
               "https://docs.perfectscale.io/security/ps-agent-rbac-permissions"),
        "I2": (2, "Oficial",
               "Integraciones documentadas con el flujo operativo: Slack, MS Teams y Datadog "
               "para alertas, Jira para gestion de incidencias, Grafana y Datadog para "
               "observabilidad, y ArgoCD «for connecting recommendations to GitOps workflows».",
               "https://docs.perfectscale.io/customizations"),
        "AD1": (2, "Oficial",
                "El control de acceso esta documentado por roles: «The Admin role has full "
                "access to all system features, including user management, cluster settings, "
                "policy configuration, and platform customization», con roles diferenciados.",
                "https://docs.perfectscale.io/administration/rbac-or-roles-and-permissions"),
        "AD2": ("NE", "Pendiente",
                "No se encontro guia oficial de habilitacion, ownership o medicion de "
                "adopcion sostenida.", ""),
        "P1": ("NE", "Pendiente",
               "No se encontro documentacion sobre exposicion de precio, moneda, region, "
               "unidad y supuestos de los costos calculados.", ""),
        "P2": ("NE", "Pendiente",
               "No se encontro documentacion de estimacion o comparacion contextual de "
               "componentes de precio.", ""),
        "D1": ("NE", "Pendiente",
               "No se encontro documentacion oficial de exportacion de datos o API de salida.", ""),
        "D2": ("NE", "Pendiente",
               "No se encontro documentacion sobre dependencias propietarias ni camino de "
               "salida.", ""),
    }),

    "ScaleOps": ("Kubernetes",
        "Limite de evidencia registrado: FP-179 ya advirtio que la evidencia de ScaleOps es "
        "una declaracion del proveedor. En esta pasada no se localizo documentacion tecnica "
        "oficial indexada fuera del sitio comercial, por lo que, aplicando FP-177 seccion 2.1 "
        "(«si un indicador cuenta solo con evidencia comercial, su puntaje maximo es 1»), "
        "ningun indicador de ScaleOps supera el valor 1. Si el equipo accede a documentacion "
        "tecnica del producto, estos valores deben revisarse.", {
        "V1": (1, "Comercial",
               "El proveedor declara «instant visibility into actual Kubernetes costs, broken "
               "down by cluster, namespace, team, application, annotations, or labels». "
               "Evidencia comercial exclusiva: topado en 1 por FP-177.",
               "https://scaleops.com/product/kubernetes-cost-monitoring/"),
        "V2": (1, "Comercial",
               "El proveedor declara integracion nativa «with AWS CUR, GCP Billing Export, and "
               "Azure Cost Management, ensuring accurate cost data that matches actual "
               "provider invoices». Evidencia comercial exclusiva: topado en 1.",
               "https://scaleops.com/product/kubernetes-cost-monitoring/"),
        "A1": (1, "Comercial",
               "El proveedor declara desglose por equipo y aplicacion. Evidencia comercial "
               "exclusiva: topado en 1.",
               "https://scaleops.com/product/kubernetes-cost-monitoring/"),
        "A2": ("NE", "Pendiente",
               "No se encontro evidencia, ni siquiera comercial, sobre reglas de reparto de "
               "costo compartido.", ""),
        "O1": (1, "Comercial",
               "El proveedor declara rightsizing automatico de CPU y memoria segun "
               "comportamiento de la carga. Evidencia comercial exclusiva: topado en 1.",
               "https://scaleops.com/"),
        "O2": ("NE", "Pendiente",
               "No se encontro evidencia sobre explicacion de impacto ni seguimiento del "
               "ahorro realizado.", ""),
        "AU1": (1, "Comercial",
                "El proveedor declara que «ScaleOps applies workload changes continuously and "
                "automatically as resource needs change, with rightsizing happening without "
                "pod restarts». Evidencia comercial exclusiva: topado en 1 pese a describir "
                "ejecucion automatica.",
                "https://scaleops.com/"),
        "AU2": ("NE", "Pendiente",
                "No se encontro evidencia sobre aprobacion, reversion o limites previos a la "
                "aplicacion automatica de cambios.", ""),
        "M1": (1, "Comercial",
               "El proveedor declara despliegue «across AWS, GCP, Azure, hybrid, and edge "
               "clusters». Evidencia comercial exclusiva: topado en 1.",
               "https://scaleops.com/"),
        "M2": ("NE", "Pendiente",
               "No se encontro evidencia sobre normalizacion ni diferencias semanticas entre "
               "proveedores.", ""),
        "I1": (1, "Comercial",
               "El proveedor declara integracion nativa con AWS CUR, GCP Billing Export y "
               "Azure Cost Management. Evidencia comercial exclusiva: topado en 1.",
               "https://scaleops.com/product/kubernetes-cost-monitoring/"),
        "I2": (1, "Comercial",
               "El proveedor declara compatibilidad con componentes nativos (HPA, VPA, "
               "Karpenter, Cluster Autoscaler) y un plano de control «GitOps-compliant». "
               "Evidencia comercial exclusiva: topado en 1.",
               "https://scaleops.com/"),
        "AD1": ("NE", "Pendiente",
                "No se encontro evidencia sobre roles y accesos por perfil.", ""),
        "AD2": ("NE", "Pendiente",
                "No se encontro guia de habilitacion ni mecanismos de gobernanza "
                "documentados.", ""),
        "P1": ("NE", "Pendiente",
               "No se encontro evidencia sobre exposicion de precio, moneda, region, unidad y "
               "supuestos.", ""),
        "P2": ("NE", "Pendiente",
               "No se encontro evidencia de estimacion o comparacion de componentes de "
               "precio.", ""),
        "D1": ("NE", "Pendiente",
               "No se encontro evidencia sobre exportacion de datos o API de salida.", ""),
        "D2": ("NE", "Pendiente",
               "No se encontro evidencia sobre dependencias propietarias ni camino de "
               "salida.", ""),
    }),

    "AWS Pricing Calculator": ("Estimacion temprana", None, {
        "V1": (2, "Oficial",
               "Permite generar estimaciones «for specific applications or workloads that you "
               "model», desglosadas por servicio y region, que es la unidad de analisis del "
               "escenario de predespliegue.",
               "https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html"),
        "V2": ("NA", "Justificacion de alcance",
               "En E4 la unidad de analisis es el cambio propuesto antes del despliegue: no "
               "existe facturacion real que rastrear. Mismo criterio aplicado a Infracost.", ""),
        "A1": ("NA", "Justificacion de alcance",
               "No es una herramienta de asignacion de gasto organizacional; entrega una "
               "estimacion por configuracion modelada. Mismo criterio aplicado a Infracost.", ""),
        "A2": ("NA", "Justificacion de alcance",
               "Mismo motivo que A1.", ""),
        "O1": ("NE", "Pendiente",
               "No se encontro documentacion de deteccion de desperdicio, rightsizing u "
               "oportunidades de optimizacion en la calculadora.", ""),
        "O2": ("NE", "Pendiente",
               "No se encontro documentacion de explicacion de impacto ni seguimiento de "
               "recomendaciones.", ""),
        "AU1": (0, "Oficial (ausencia verificada)",
                "Es una herramienta de estimacion en consola: no ejecuta ni bloquea acciones "
                "o despliegues.",
                "https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html"),
        "AU2": ("NA", "Justificacion de alcance",
                "Al no ejecutar acciones (ver AU1), no aplica evaluar salvaguardas de "
                "ejecucion.", ""),
        "M1": (0, "Oficial (ausencia verificada)",
               "Estima exclusivamente servicios de AWS; no consolida costos de otros "
               "proveedores.",
               "https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html"),
        "M2": (0, "Oficial (ausencia verificada)",
               "Mismo alcance de diseno que M1.",
               "https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html"),
        "I1": (2, "Oficial",
               "Documenta la ingesta de datos propios del escenario: «You can add new usage, "
               "import usage from your existing cost and usage data, or import public pricing "
               "calculator usage through its share URL».",
               "https://docs.aws.amazon.com/cost-management/latest/userguide/pc-workload-estimate.html"),
        "I2": (1, "Oficial",
               "La integracion con el flujo de revision es por enlace compartido y exportacion "
               "manual: «You can save the unique link for each estimate to share or revisit». "
               "No se documenta integracion con CI/CD o con un flujo de aprobacion.",
               "https://docs.aws.amazon.com/pricing-calculator/latest/userguide/save-share-estimate.html"),
        "AD1": ("NE", "Pendiente",
                "No se encontro documentacion sobre roles y accesos diferenciados para los "
                "perfiles del escenario.", ""),
        "AD2": ("NE", "Pendiente",
                "No se encontro guia oficial de habilitacion, ownership o seguimiento de uso "
                "sostenido.", ""),
        "P1": (2, "Oficial",
               "Expone precio por region de forma explicita: «All AWS resources are priced "
               "based on the Region you choose», y la documentacion enlaza los supuestos de "
               "precio aplicados a la estimacion.",
               "https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html"),
        "P2": (2, "Oficial",
               "Permite comparar configuraciones modeladas y estimar sobre la familia de "
               "facturacion consolidada, «which takes into account your modeled usage and "
               "commitments».",
               "https://docs.aws.amazon.com/cost-management/latest/userguide/pc-workload-estimate.html"),
        "D1": (2, "Oficial",
               "Las estimaciones se exportan en formatos utilizables: «You can export your "
               "estimates as PDF or CSV files».",
               "https://docs.aws.amazon.com/pricing-calculator/latest/userguide/export-estimate.html"),
        "D2": ("NE", "Pendiente",
               "No se encontro documentacion sobre dependencias propietarias ni camino de "
               "salida de los datos de estimacion.", ""),
    }),

    "Azure Pricing Calculator": ("Estimacion temprana", None, {
        "V1": (2, "Oficial",
               "Permite construir estimaciones que son «collections of Azure products», con "
               "filtros de region, tipo de producto y niveles, y un resumen de estimacion por "
               "componente.",
               "https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/pricing-calculator"),
        "V2": ("NA", "Justificacion de alcance",
               "En E4 la unidad de analisis es el cambio propuesto antes del despliegue: no "
               "existe facturacion real que rastrear. Mismo criterio aplicado a Infracost.", ""),
        "A1": ("NA", "Justificacion de alcance",
               "No es una herramienta de asignacion de gasto organizacional. Mismo criterio "
               "aplicado a Infracost.", ""),
        "A2": ("NA", "Justificacion de alcance",
               "Mismo motivo que A1.", ""),
        "O1": ("NE", "Pendiente",
               "No se encontro documentacion de deteccion de desperdicio u oportunidades de "
               "optimizacion en la calculadora.", ""),
        "O2": ("NE", "Pendiente",
               "No se encontro documentacion de explicacion de impacto ni seguimiento de "
               "recomendaciones.", ""),
        "AU1": (0, "Oficial (ausencia verificada)",
                "Es una herramienta web de estimacion: no ejecuta ni bloquea acciones o "
                "despliegues.",
                "https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/pricing-calculator"),
        "AU2": ("NA", "Justificacion de alcance",
                "Al no ejecutar acciones (ver AU1), no aplica evaluar salvaguardas.", ""),
        "M1": (0, "Oficial (ausencia verificada)",
               "Estima exclusivamente servicios de Azure; no consolida costos de otros "
               "proveedores.",
               "https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/pricing-calculator"),
        "M2": (0, "Oficial (ausencia verificada)",
               "Mismo alcance de diseno que M1.",
               "https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/pricing-calculator"),
        "I1": (2, "Oficial",
               "El acceso programatico a los precios esta documentado mediante la Azure Retail "
               "Prices API, que «provides comprehensive retail price information for all Azure "
               "services across different regions and currencies».",
               "https://learn.microsoft.com/en-us/rest/api/cost-management/retail-prices/azure-retail-prices"),
        "I2": ("NE", "Pendiente",
               "No se encontro documentacion de integracion de la estimacion con un flujo de "
               "revision, ticket o CI/CD.", ""),
        "AD1": ("NE", "Pendiente",
                "No se encontro documentacion sobre roles y accesos diferenciados.", ""),
        "AD2": ("NE", "Pendiente",
                "No se encontro guia oficial de habilitacion o seguimiento de uso sostenido.", ""),
        "P1": (2, "Oficial",
               "Expone region y moneda como filtros del producto y puede mostrar tarifas "
               "negociadas: «it can also show any negotiated rates specific to your Azure "
               "Billing Account», lo que hace explicitos los supuestos de precio aplicados.",
               "https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/pricing-calculator"),
        "P2": (2, "Oficial",
               "Permite modelar y comparar configuraciones de productos antes de contratar, "
               "ajustando region, nivel y uso previsto sobre el resumen de estimacion.",
               "https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/pricing-calculator"),
        "D1": ("NE", "Pendiente",
               "No se encontro en la documentacion revisada la funcion de exportacion de la "
               "estimacion en un formato utilizable.", ""),
        "D2": ("NE", "Pendiente",
               "No se encontro documentacion sobre dependencias propietarias ni camino de "
               "salida.", ""),
    }),
}


def criterion_of(indicator: str) -> str:
    prefix = "".join(ch for ch in indicator if ch.isalpha())
    return CRITERION_OF[prefix]


def write_report(results) -> None:
    lines = [
        "# FP-180 — Alternativas adicionales incorporadas",
        "",
        f"> Generado por `add_alternatives.py` el {VERIFIED}. Evidencia verificada contra "
        "documentación oficial. Queda a validación humana.",
        "",
        "## Por qué",
        "",
        "El criterio de término de FP-51 no pide registrar las alternativas, pide compararlas: "
        "«Las alternativas son comparadas bajo el mismo escenario». FP-126 las registró y "
        "FP-179 las auditó, pero la matriz nunca las puntuó. Esta pasada incorpora las ocho "
        "bajo la misma metodología que el resto de la población.",
        "",
        "## Resultado por alternativa",
        "",
        "| Alternativa | Categoría | Escenario ancla | Cobertura | Resultado |",
        "|---|---|---|---:|---|",
    ]
    for product, (category, _, _) in ALTERNATIVES.items():
        anchor = ANCHOR_BY_CATEGORY[category]
        key = next((k for k in results if k[2] == product and k[0] == anchor), None)
        if not key:
            continue
        r = results[key]
        score = (f"{r['score']:.2f} ({r['band']})" if r["score"] is not None
                 else "Insufficient evidence")
        lines.append(f"| {product} | {category} | {anchor} | {r['coverage']:.1f}% | {score} |")

    lines += [
        "",
        "Ninguna alcanza el 70% de cobertura con la investigación de esta pasada, que consistió "
        "en una o dos consultas de documentación oficial por producto. Dos quedan a una sola "
        "celda del umbral: IBM Cloud Cost Estimator necesita O2 y AWS Pricing Calculator "
        "necesita D2.",
        "",
        "## Reglas aplicadas",
        "",
        "- Ninguna celda queda en blanco: lo que no se encontró en fuentes oficiales o "
        "aprobadas del proyecto se registra como `NE` con su motivo.",
        "- La evidencia exclusivamente comercial limita el indicador a 1, según FP-177 §2.1.",
        "- Ningún indicador alcanza 3: eso exige doble evidencia y esta pasada dispone solo de "
        "documentación primaria.",
        "- Los indicadores dependientes del escenario se puntúan solo en el escenario ancla del "
        "producto; en los demás quedan `NE` a la espera de evidencia propia.",
        "",
        "## Observaciones para el equipo",
        "",
    ]
    for product, (_, team_note, _) in ALTERNATIVES.items():
        if team_note:
            lines += [f"**{product}**", "", team_note, ""]
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if not WORKBOOK.exists():
        print(f"ERROR: no se encontro {WORKBOOK}")
        return 1

    shutil.copy2(WORKBOOK, WORKBOOK.with_suffix(".xlsx.bak"))
    workbook = openpyxl.load_workbook(WORKBOOK)
    sheet = workbook["Puntuacion"]
    header = [c.value for c in sheet[1]]
    col = {h: i for i, h in enumerate(header)}

    # reuse the observable questions already recorded for each indicator
    questions, existing = {}, set()
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if not row[col["Escenario"]]:
            continue
        questions.setdefault(row[col["Indicador"]], row[col["Pregunta observable"]])
        existing.add((row[col["Escenario"]], row[col["Producto"]], row[col["Indicador"]]))

    added = 0
    for product, (category, team_note, indicators) in ALTERNATIVES.items():
        anchor = ANCHOR_BY_CATEGORY[category]
        for scenario in SCENARIOS_BY_CATEGORY[category]:
            for indicator in INDICATOR_ORDER:
                if (scenario, product, indicator) in existing:
                    continue
                value, ev_type, evidence, source = indicators[indicator]
                notes = [f"Alternativa adicional incorporada en FP-180 ({VERIFIED}) desde el "
                         f"registro de FP-126 y la auditoria de FP-179."]
                if team_note:
                    notes.append(team_note)
                if indicator not in SCENARIO_INDEPENDENT and scenario != anchor:
                    value, ev_type = "NE", "Pendiente"
                    evidence = PENDING
                    source = ""
                    notes.append(f"Escenario ancla del producto: {anchor}.")
                sheet.append({
                    col["Escenario"] + 1: scenario,
                    col["Categoria"] + 1: category,
                    col["Producto"] + 1: product,
                    col["Criterio"] + 1: criterion_of(indicator),
                    col["Indicador"] + 1: indicator,
                    col["Pregunta observable"] + 1: questions.get(indicator, ""),
                    col["Valor (0-3/NE/NA)"] + 1: value,
                    col["Tipo de evidencia"] + 1: ev_type,
                    col["Evidencia"] + 1: evidence,
                    col["Fuente"] + 1: source,
                    col["Fecha de verificacion"] + 1: VERIFIED if source else "",
                    col["Notas"] + 1: " | ".join(notes),
                })
                added += 1

    print(f"Filas agregadas: {added}")

    after, _ = read_scores(sheet)
    results = {k: evaluate(v, BASE_W) for k, v in after.items()}
    write_results_sheet(workbook, after)
    rebuild_charts(workbook)
    workbook.save(WORKBOOK)
    if added:
        write_report(results)
        print(f"Informe: {REPORT.name}")
    else:
        print(f"Sin alternativas pendientes; se conserva {REPORT.name} tal como estaba.")

    computable = sum(1 for r in results.values() if r["score"] is not None)
    print(f"Pares con puntaje calculable: {computable} de {len(results)}")
    print("\nAlternativas incorporadas:")
    for product, (category, _, _) in ALTERNATIVES.items():
        anchor = ANCHOR_BY_CATEGORY[category]
        key = next((k for k in results if k[2] == product and k[0] == anchor), None)
        if key:
            r = results[key]
            score = f"{r['score']:.2f} ({r['band']})" if r["score"] is not None \
                else "Insufficient evidence"
            print(f"   {anchor} {product:<30} cobertura {r['coverage']:>5.1f}%   {score}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
