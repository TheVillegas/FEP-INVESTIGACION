# -*- coding: utf-8 -*-
"""FP-180 — Research pass on E3, optimisation and automation in Kubernetes.

E3 had a single scored pair (OpenCost) despite six eligible Kubernetes tools
plus the native and multicloud categories. This pass fills the cells that were
blocking the closest products, investigated against official documentation on
2026-09-16.

CloudZero enters E3 under the FP-177 condition for multicloud platforms, "si
integran datos de clúster". That condition is verified here rather than assumed:
its documentation describes a Kubernetes agent collecting pod-level usage, plus
AWS Split Cost Allocation Data and GKE Cost Allocation as alternative paths. Its
E3 cells are scored against E3's own inputs and outputs — cluster metrics,
namespace breakdown — not carried over from E2, because consolidating several
providers says nothing about reading a cluster.

Usage: python apply_e3_kubernetes.py
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
REPORT = HERE / "investigacion-e3.md"
VERIFIED = "2026-09-16"
SCENARIO = "E3"

# (product, indicator) -> (value, evidence type, evidence, source)
RESEARCH = {
    ("Kubecost", "AU1"): (
        2, "Oficial",
        "El Cluster Controller ejecuta el redimensionamiento, no solo lo recomienda: la Apply "
        "API «is available at /cluster/requestsizer/plan and expects a POST request with a body "
        "identical to a response from the Plan API», y la interfaz ofrece el boton "
        "«Automatically implement recommendations» para aplicar las recomendaciones de request "
        "sizing.",
        "https://docs.kubecost.com/apis/apis/api-request-recommendation-apply ; "
        "https://docs.kubecost.com/using-kubecost/getting-started/guide-one-click-request-sizing"),

    ("Kubecost", "AU2"): (
        2, "Oficial",
        "La salvaguarda esta documentada como limite duro de la propia API: «The Apply APIs "
        "only 'size down', meaning they will never increase container requests, only lower "
        "them». El alcance de la automatizacion tambien se declara: soporta Deployments, "
        "DaemonSets, StatefulSets y ReplicaSets, y «do not support clusters other than the "
        "'local' cluster».",
        "https://docs.kubecost.com/apis/apis/api-request-recommendation-apply"),

    ("Kubecost", "AD1"): (
        2, "Oficial",
        "El acceso por rol esta documentado con proveedores de identidad externos: la "
        "documentacion cubre integracion SAML con Microsoft Entra ID y Okta, e integracion "
        "OIDC con RBAC, donde los roles se adjuntan «to users and groups within your identity "
        "provider» mediante claims, incluyendo un rol «readonly» para acceso de solo lectura.",
        "https://docs.kubecost.com/install-and-configure/advanced-configuration/user-management-saml ; "
        "https://docs.kubecost.com/install-and-configure/advanced-configuration/user-management-oidc/"
        "microsoft-entra-id-oidc-integration-for-kubecost"),

    ("Kubecost", "D2"): (
        2, "Oficial",
        "El camino de salida y la reversibilidad estan documentados, algo infrecuente en la "
        "poblacion: los respaldos de ETL «are executed by customers in their own environment» y "
        "los datos «can be downloaded to local disk using automated or manual backup methods», "
        "de modo que el historico queda en poder del cliente. La desinstalacion tambien esta "
        "descrita: la remocion manual se hace borrando el namespace de Kubecost. El producto se "
        "despliega por Helm dentro del propio cluster, lo que acota la dependencia de "
        "infraestructura del proveedor.",
        "https://docs.kubecost.com/1.0x/install-and-configure/install/etl-backup ; "
        "https://docs.kubecost.com/1.0x/troubleshooting/troubleshoot-install"),

    ("CloudZero", "O1"): (
        2, "Oficial",
        "Evidencia propia de E3: el agente de Kubernetes aporta, ademas de las metricas de uso "
        "por pod, el calculo de costo ocioso («idle cost calculation»), que es la deteccion de "
        "desperdicio relevante a este escenario.",
        "https://docs.cloudzero.com/docs/container-cost-track"),

    ("CloudZero", "A2"): (
        2, "Oficial",
        "CostFormation define reglas explicitas para el gasto compartido y no atribuible, "
        "aplicables a los costos de cluster: el remanente se asigna a un elemento por defecto "
        "de modo que «the total always reconciles with the actual bill». La regla es "
        "declarativa y versionable en el lenguaje de CostFormation.",
        "https://docs.cloudzero.com/docs/costformation-allocating-shared-costs ; "
        "https://docs.cloudzero.com/docs/cfdl-reference"),

    ("CloudZero", "AU1"): (
        0, "Oficial (ausencia verificada)",
        "La documentacion describe a CloudZero Optimize como una funcion de recomendacion: no "
        "ejecuta ni bloquea acciones sobre los recursos del cluster. La ausencia es una "
        "propiedad del producto y no depende del escenario, por lo que se sostiene igual en E3.",
        "https://docs.cloudzero.com/docs/cloudzero"),

    ("CloudZero", "I2"): (
        2, "Oficial",
        "El flujo operativo del escenario esta cubierto por las mismas integraciones "
        "documentadas para la plataforma: Jira para crear y seguir elementos de trabajo desde "
        "recomendaciones y anomalias, y Slack o Google Chat para notificaciones enrutadas por "
        "View. Son propiedades del producto, no del escenario.",
        "https://docs.cloudzero.com/docs/integrations"),

    ("CloudZero", "AD1"): (
        2, "Oficial",
        "El acceso por rol esta documentado: «CloudZero uses role-based access control (RBAC) "
        "to manage who can see your cost data and what actions they can take in the platform, "
        "with each user assigned one or more Roles that control both data visibility and "
        "platform permissions», lo que cubre los perfiles de plataforma y FinOps que pide E3.",
        "https://docs.cloudzero.com/docs/users-and-permissions"),

    ("Cast AI", "A2"): (
        2, "Oficial",
        "Los grupos de asignacion son una regla de reparto configurable y versionable: "
        "«Allocation groups is a custom-made report that lets you allocate the costs of your "
        "cluster per team, application, or other criteria by selecting relevant labels and "
        "namespaces», y ademas «Allocation Groups are now also supported in the Cast AI "
        "Terraform provider, enabling Infrastructure as Code management of cost allocation "
        "strategies», lo que las hace reproducibles.",
        "https://docs.cast.ai/docs/allocation-groups"),

    ("Cast AI", "AD1"): (
        2, "Oficial",
        "RBAC documentado con roles predefinidos: «Owner role has full administrative access to "
        "all organization and cluster resources, Member role can perform all cluster-related "
        "operations but has limited access to organizational features, and Viewer role provides "
        "read-only access across all features», gestionables por consola, API y Terraform.",
        "https://docs.cast.ai/docs/role-based-access-control-rbac"),

    ("Cast AI", "I2"): (
        2, "Oficial",
        "Integracion nativa con el flujo operativo del escenario: «Cast AI now supports native "
        "Slack integration as a delivery method for alert notifications», conectando el "
        "workspace por OAuth desde la consola y permitiendo entregar cada alerta «to up to 5 "
        "selected Slack channels per alert».",
        "https://docs.cast.ai/changelog/february-2025"),

    # CloudZero in E3: eligibility condition verified, then scored against E3's inputs.
    ("CloudZero", "V1"): (
        2, "Oficial",
        "Evidencia propia de E3: la plataforma permite «see your Kubernetes costs broken down "
        "by cluster, namespace, workload, and label, alongside your entire cloud bill», que es "
        "exactamente la unidad de desglose que pide este escenario.",
        "https://docs.cloudzero.com/docs/container-cost-track"),

    ("CloudZero", "A1"): (
        2, "Oficial",
        "Evidencia propia de E3: el agente «collects pod-level CPU, memory, and GPU usage from "
        "your clusters and sends it to CloudZero, which combines this usage data with the "
        "actual cost of each VM from your cloud provider bill to allocate Kubernetes costs by "
        "cluster, namespace, workload, and label».",
        "https://docs.cloudzero.com/docs/container-cost-track"),

    ("CloudZero", "I1"): (
        2, "Oficial",
        "Evidencia propia de E3 y verificacion de la condicion de elegibilidad que FP-177 §4 "
        "impone a las plataformas multinube en este escenario («si integran datos de "
        "cluster»): la documentacion describe tres vias de ingesta —el agente de CloudZero, "
        "AWS Split Cost Allocation Data para clusteres EKS sobre EC2, y GKE Cost Allocation—, "
        "con metricas de uso por pod y calculo de costo ocioso.",
        "https://docs.cloudzero.com/docs/container-cost-track ; "
        "https://docs.cloudzero.com/docs/installation-of-cloudzero-agent-for-kubernetes"),
}


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if not WORKBOOK.exists():
        print(f"ERROR: no se encontro {WORKBOOK}")
        return 1

    shutil.copy2(WORKBOOK, WORKBOOK.with_suffix(".xlsx.bak"))
    workbook = openpyxl.load_workbook(WORKBOOK)
    sheet = workbook["Puntuacion"]
    header = [c.value for c in sheet[1]]
    col = {h: i + 1 for i, h in enumerate(header)}

    changes = []
    for row in range(2, sheet.max_row + 1):
        if sheet.cell(row, col["Escenario"]).value != SCENARIO:
            continue
        product = sheet.cell(row, col["Producto"]).value
        indicator = sheet.cell(row, col["Indicador"]).value
        target = RESEARCH.get((product, indicator))
        if not target:
            continue
        cell = sheet.cell(row, col["Valor (0-3/NE/NA)"])
        if str(cell.value).strip().upper() != "NE":
            continue
        value, ev_type, evidence, source = target
        cell.value = value
        sheet.cell(row, col["Tipo de evidencia"]).value = ev_type
        sheet.cell(row, col["Evidencia"]).value = evidence
        sheet.cell(row, col["Fuente"]).value = source
        sheet.cell(row, col["Fecha de verificacion"]).value = VERIFIED
        note_cell = sheet.cell(row, col["Notas"])
        note = (f"Investigacion propia de E3 ({VERIFIED}): celda verificada contra las entradas "
                "y salidas del escenario de Kubernetes.")
        note_cell.value = f"{note_cell.value} | {note}" if note_cell.value else note
        changes.append({"prod": product, "ind": indicator, "val": value})

    print(f"Celdas completadas en E3: {len(changes)}")

    after, _ = read_scores(sheet)
    after_results = {k: evaluate(v, BASE_W) for k, v in after.items()}
    write_results_sheet(workbook, after)
    rebuild_charts(workbook)
    workbook.save(WORKBOOK)

    lines = [
        "# FP-180 — Escenario E3, optimizacion y automatizacion en Kubernetes",
        "",
        f"> Generado por `apply_e3_kubernetes.py` el {VERIFIED}. Queda a validacion humana.",
        "",
        "## Por que",
        "",
        "E3 tenia un solo par puntuado (OpenCost) pese a contar con seis herramientas de "
        "Kubernetes elegibles, mas las categorias nativa y multinube. Esta pasada completa las "
        "celdas que bloqueaban a los productos mas cercanos al umbral.",
        "",
        "## CloudZero y la condicion de elegibilidad",
        "",
        "FP-177 §4 admite plataformas multinube en E3 solo «si integran datos de cluster». Esa "
        "condicion se **verifico** en lugar de suponerse: la documentacion de CloudZero "
        "describe un agente de Kubernetes que recoge uso por pod, mas dos vias alternativas de "
        "ingesta (AWS Split Cost Allocation Data y GKE Cost Allocation).",
        "",
        "Sus celdas de E3 se puntuaron contra las entradas y salidas de este escenario, **no se "
        "arrastraron desde E2**: consolidar varios proveedores no dice nada sobre leer un "
        "cluster, asi que ahi no hay subsuncion posible.",
        "",
        f"## Celdas completadas ({len(changes)})",
        "",
        "| Producto | Indicador | Valor |",
        "|---|---|---:|",
    ]
    for c in sorted(changes, key=lambda x: (x["prod"], x["ind"])):
        lines.append(f"| {c['prod']} | {c['ind']} | {c['val']} |")

    lines += ["", "## Estado de E3 tras esta pasada", "",
              "| Producto | Categoria | S linea base | Banda | Cobertura |",
              "|---|---|---:|---|---:|"]
    scored = [(k, v) for k, v in after_results.items()
              if k[0] == SCENARIO and v["score"] is not None]
    for k, r in sorted(scored, key=lambda kv: -kv[1]["score"]):
        lines.append(f"| {k[2]} | {k[1]} | {r['score']:.2f} | {r['band']} | "
                     f"{r['coverage']:.1f}% |")

    unscored = sorted((k[2], v["coverage"]) for k, v in after_results.items()
                      if k[0] == SCENARIO and v["score"] is None)
    if unscored:
        lines += ["", "## Siguen sin puntaje en E3", "",
                  "| Producto | Cobertura |", "|---|---:|"]
        for name, cov in unscored:
            lines.append(f"| {name} | {cov:.1f}% |")
        lines.append("")
        lines.append("El motivo de cada celda pendiente esta registrado en la hoja Puntuacion.")
    lines.append("")
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Informe: {REPORT.name}")

    e3 = [(k, v) for k, v in after_results.items()
          if k[0] == SCENARIO and v["score"] is not None]
    print(f"\nE3 con puntaje ({len(e3)}):")
    for k, r in sorted(e3, key=lambda kv: -kv[1]["score"]):
        print(f"   {k[2]:<30} {r['score']:>6.2f}  {r['band']:<8} cob {r['coverage']:.1f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
