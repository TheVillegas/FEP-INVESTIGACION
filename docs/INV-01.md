# CHECKLIST OPERATIVA

### **CHECKLIST OPERATIVA: TI-06 FinOps (Pauta FEP00.3.26)**

**Datos de Entrega y Control**

* **Empresa y Tema:** N.º 8 ONEBYTE | TI-06: FinOps: economía y optimización de costos en la nube.  
* **Fecha Límite:** Lunes 21 de septiembre de 2026\.  
* **Asunto Correo:** \[ICI544\] \- 08 \- ONEBYTE \- TI-06.  
* **Archivos Requeridos:** 08 \- ONEBYTE \- TI-06.pdf (informe de 10 a 15 páginas \+ anexo IA) y 08 \- ONEBYTE \- TI-06.pptx (o PDF de presentación).

#### **1\. Mapeo de Subtemas Obligatorios**

* \[ \] **Marco FinOps:** Fases informar, optimizar y operar; matriz de roles (ingeniería, finanzas, adquisiciones).  
* \[ \] **Asignación de Costos:** Políticas de etiquetado, showback vs. chargeback, costos compartidos y tasa de asignación efectiva.  
* \[ \] **Economía Unitaria:** Costo unitario por transacción, por cliente, por request y por token de IA como KPI de producto.  
* \[ \] **Palancas de Optimización:** Right-sizing, apagado de recursos ociosos, compromisos (Savings Plans, RI, CUD), capacidad excedente (Spot), storage tiering y optimización de arquitectura.  
* \[ \] **Costos Subestimados:** Data egress, tráfico inter-AZ, licenciamiento propietario, soporte comercial y ambientes no productivos.  
* \[ \] **Estandarización y Shift-Left:** Especificación FOCUS (FinOps Foundation) y estimación temprana de costos en CI/CD.  
* \[ \] **Regiones Cloud Sudamérica:** Disponibilidad local, prima de precio Santiago vs. EE.UU. y análisis de residencia de datos.

#### **2\. Entregable Específico de TI-06**

* \[ \] **TCO a 5 años:** Modelado sobre una arquitectura concreta con $\\ge 3$ palancas de optimización cuantificadas.  
* \[ \] **Comparativa Regional:** Comparación de precios para la misma arquitectura en Santiago vs. EE.UU. (con fecha y fuente oficial).  
* \[ \] **Análisis de Sensibilidad:** Evaluación de variación sobre las 2 variables de mayor impacto en la factura.  
* \[ \] **Vínculo con Propuesta:** Integración de cifras en el flujo de caja, estructura de costos, VAN y TIR del proyecto.

#### **3\. Reglas de Aporte Propio y Ampliación ("Otros")**

* \[ \] **Párrafo de Aporte Propio:** Párrafo explícito al final de la Introducción diferenciando el alcance de la ficha del aporte del grupo.  
* \[ \] **Herramientas Nativas (+2):** AWS Cost Explorer, Azure Cost Management, GCP Billing \+ (2 adicionales).  
* \[ \] **Plataformas Multinube (+2):** Cloudability, CloudHealth, CloudZero, Vantage, Finout, nOps \+ (2 adicionales).  
* \[ \] **Costos en Kubernetes (+2):** OpenCost, Kubecost, CAST AI, StormForge \+ (2 adicionales).  
* \[ \] **Estimación Temprana (+2):** Infracost, Cloud Custodian \+ (2 adicionales).  
* \[ \] **Estándares (+2 o declaración):** FOCUS \+ (2 adicionales o búsqueda documentada con descarte y fecha si no existen más).

#### **4\. Verificación de Precios y Fuentes**

* \[ \] **Estructura por Cifra:** Cada precio incluye producto/SKU, moneda, región geográfica, fecha de consulta y tipo (precio de lista o cotización).  
* \[ \] **Proveedores Cerrados:** Declaración expresa de "solo por cotización" ante ausencia de precios públicos.  
* \[ \] **Fuentes Válidas:** Documentación oficial de proveedores, estándares (CNCF, FinOps Foundation, ISO), papers revisados o biblioteca PUCV (prohibidas comparativas de proveedores o blogs sin autoría).

#### **5\. Cuestionario de 30 Preguntas**

* \[ \] **Cantidad y Formatos:** Exactamente 30 preguntas combinando selección múltiple, V/F, términos pareados/completar y respuesta corta.  
* \[ \] **Detalle por Pregunta:** Respuesta correcta \+ justificación técnica individual de autoría 100% humana.  
* \[ \] **Graduación de Dificultad:** 12 Básicas (40%), 12 Intermedias (40%) y 6 Avanzadas (20%).  
* \[ \] **Índice Temático:** Matriz inicial que vincula cada pregunta con su sección del informe.

#### **6\. Anexo de Declaración de Inteligencia Artificial**

* \[ \] **Autoría Humana Exclusiva:** Sin uso de IA en comparativas, conclusiones, párrafo de aporte propio, cifras/referencias y el cuestionario de 30 preguntas.  
* \[ \] **Declaración por Sección:** Niveles 0 a 3 asignados sección por sección con herramientas y versiones.  
* \[ \] **Trazabilidad (Niveles 2 y 3):** Prompts transcritos, links a conversaciones exportadas e historial de versiones auditable (Docs/Git).  
* \[ \] **Firmas Individuales:** Declaración completada y firmada por cada integrante del equipo.

&nbsp;

# base (pauta))

INFORME DE INVESTIGACIÓN  
**Estructura adaptada y traducida directamente de la rúbrica del profe**

FinOps: economía y optimización de costos en la nube

&nbsp;

1\. INTRODUCCIÓN Y CONTEXTO

&nbsp;

   1.1 Resumen ejecutivo

   1.2 Contexto de la computación en la nube

   1.3 Problema de la gestión de costos cloud

   1.4 Pregunta orientadora del informe

   1.5 Objetivo general

   1.6 Objetivos específicos

   1.7 Alcance del informe

   1.8 Metodología y criterios de selección de fuentes

   1.9 Identificación del aporte propio del grupo

&nbsp;

2\. FUNDAMENTOS DE FINOPS

&nbsp;

   2.1 Conceptos previos para comprender FinOps

       2.1.1 Consumo de servicios cloud

       2.1.2 Costos variables y modelo bajo demanda

       2.1.3 Diferencia entre costo, eficiencia y valor

   2.2 Definición operativa de FinOps

   2.3 Qué es y qué no es FinOps

   2.4 FinOps como gestión del valor y no solo reducción de costos

   2.5 Fases del marco FinOps

       2.5.1 Informar

       2.5.2 Optimizar

       2.5.3 Operar

   2.6 Roles y responsabilidades

       2.6.1 Ingeniería

       2.6.2 Finanzas

       2.6.3 Adquisiciones

       2.6.4 Negocio y producto

&nbsp;

&nbsp;

3\. DE LOS DATOS DE COSTO A LAS DECISIONES

&nbsp;

   3.1 Visibilidad y asignación de costos

   3.2 Etiquetado de recursos

   3.3 Showback y chargeback

   3.4 Costos compartidos y tasas de asignación

   3.5 Economía unitaria

       3.5.1 Costo por transacción

       3.5.2 Costo por cliente atendido

       3.5.3 Costo por solicitud

       3.5.4 Costo por token de inteligencia artificial

   3.6 Costos subestimados en la nube

       3.6.1 Salida de datos a Internet

       3.6.2 Tráfico entre zonas

       3.6.3 Licencias de software

       3.6.4 Soporte

       3.6.5 Ambientes no productivos

   3.7 Palancas de optimización

       3.7.1 Dimensionamiento correcto

       3.7.2 Apagado de recursos ociosos

       3.7.3 Descuentos por compromiso

       3.7.4 Capacidad excedente

       3.7.5 Niveles de almacenamiento

       3.7.6 Optimización de la arquitectura

   3.8 Compromisos entre costo, calidad, velocidad y riesgo

&nbsp;

4\. ECOSISTEMA FINOPS Y CONTEXTO CLOUD

&nbsp;

   4.1 Estandarización de facturación multinube

   4.2 Especificación FOCUS

   4.3 Estimación temprana de costos

   4.4 Herramientas nativas de los proveedores cloud

   4.5 Plataformas multinube

   4.6 Herramientas para costos en Kubernetes

   4.7 Herramientas de estimación temprana

   4.8 Criterios de comparación

   4.9 Comparación de herramientas y proveedores

   4.10 Alternativas adicionales identificadas por el grupo

   4.11 Regiones cloud en Chile y Sudamérica

   4.12 Disponibilidad, precios y residencia de datos

&nbsp;

5\. CASO APLICADO Y EVALUACIÓN ECONÓMICA

&nbsp;

   5.1 Contexto y necesidad de ONEBYTE

   5.2 Arquitectura de referencia

   5.3 Componentes y servicios utilizados

   5.4 Supuestos técnicos, operativos y económicos

   5.5 Volumen de usuarios, solicitudes y almacenamiento

   5.6 Costo base mensual y anual

   5.7 Costo total de propiedad a cinco años

   5.8 Aplicación de la primera palanca de optimización

   5.9 Aplicación de la segunda palanca de optimización

   5.10 Aplicación de la tercera palanca de optimización

   5.11 Comparación de la arquitectura en Santiago de Chile y Estados Unidos

   5.12 Análisis de sensibilidad

   5.13 Variables de mayor impacto en la factura

&nbsp;

   5.14 Relación con el flujo de caja, VAN y TIR

   5.15 Aporte propio aplicado al caso

&nbsp;

6\. DISCUSIÓN Y CONCLUSIONES

&nbsp;

   6.1 Interpretación de los resultados

   6.2 Discusión crítica de las alternativas

   6.3 Relación entre arquitectura y costos

   6.4 Limitaciones y riesgos del análisis

   6.5 Principales aportes propios del grupo

   6.6 Recomendación para ONEBYTE

   6.7 Conclusiones

&nbsp;

Criterio de orden

\- La sección 1 introduce el problema y deja declarado el aporte propio.

\- La sección 2 enseña FinOps desde cero.

\- La sección 3 explica cómo se miden, asignan y optimizan los costos.

\- La sección 4 presenta herramientas, estándares y regiones después de explicar para qué sirven.

\- La sección 5 demuestra todo mediante una arquitectura concreta y números.

\- La sección 6 interpreta los resultados y permite comprometerse con una recomendación.

&nbsp;

# fp-103 / Preguntas de inv

**Pregunta orientadora recomendada**

¿Cómo puede aplicarse FinOps en un proyecto de TI en la nube para conectar las decisiones de arquitectura y operación con la gestión y optimización de costos, y cómo se refleja en su evaluación económica?

&nbsp;

**Preguntas guía internas**

Estas pueden orientar la investigación y la redacción, pero no necesariamente deben aparecer como RQ formales:

&nbsp;

1\. ¿Qué es FinOps, qué problema resuelve y cómo se organiza mediante las fases Informar,

   Optimizar y Operar?

&nbsp;

2\. ¿Cómo se asignan, explican y transforman los costos cloud en métricas comprensibles para ingeniería, finanzas, adquisiciones y negocio?

&nbsp;

3\. ¿Qué decisiones de optimización, herramientas, estándares y regiones cloud permiten

   mejorar la eficiencia y el valor de una arquitectura?

&nbsp;

4\. ¿Qué resultados económicos se obtienen al aplicar FinOps a una arquitectura concreta,

   considerando su TCO a cinco años, las optimizaciones, la comparación regional y el

   análisis de sensibilidad?

&nbsp;