## 1. Objetivo y Alcance

### 1.1 Objetivo general

Desarrollar un sistema integral de gestión de viajes y gastos corporativos para América Móvil Perú S.A.C. (CLARO), que automatice el ciclo completo de solicitud, aprobación, rendición y liquidación de gastos de viaje del personal, asegurando el control presupuestario, la trazabilidad contable y el cumplimiento de las políticas corporativas de viáticos. El sistema facilitará la gestión end-to-end desde la creación de la solicitud hasta la contabilización en SAP y el reembolso al empleado.

### 1.2 Alcance del sistema

El sistema cubrirá los siguientes módulos y funcionalidades:

* **Gestión de Solicitudes de Gastos de Viaje:** Registro de solicitudes de viaje por parte de los empleados, indicando origen, destino, fechas, motivo del viaje, tipo de transporte (aéreo/terrestre), modalidad (con/sin anticipo) y presupuesto estimado por conceptos (alojamiento, alimentación, transporte, otros gastos).

* **Proceso de Aprobación Multinivel:** Flujo configurable de aprobaciones con roles de aprobador1, aprobador2 y delegados, incluyendo notificaciones automáticas por correo electrónico, seguimiento de estado y gestión de rechazos con motivo.

* **Cotización y Gestión de Pasajes Aéreos:** Módulo para asistentes de viaje que permite solicitar cotizaciones a agencias, cargar pasajes disponibles mediante plantilla Excel (con datos de aerolínea, vuelo, clase, horarios, tarifa), notificar opciones al solicitante y registrar comprobantes de compra.

* **Registro de Pasajes Terrestres:** Captura de información de viajes por carretera, incluyendo empresa de transporte, distancia, duración, tipo de comprobante y costos asociados.

* **Rendición de Gastos de Viaje:** Registro detallado de comprobantes de gasto (facturas, boletas) por concepto (alojamiento, alimentación, transporte, otros), con cálculo automático de IGV (18%), validación de límites y justificaciones, adjunto de documentos sustentatorios y liquidación de diferencias respecto al anticipo.

* **Integración con SAP FI:** Generación automática de documentos contables en SAP (contabilización de anticipos, descuentos, compensaciones y reembolsos), con asignación a centros de costo, divisiones y cuentas de mayor específicas (ej. 1103013002 COSTOS A COMPROBAR, 1103010541 ANTICIPO FUNCIONARIOS).

* **Generación de Archivos Bancarios:** Creación de archivos SCT para bancos (BCP, Scotiabank) en formatos estándar, agrupando reembolsos por referencia, con selección de cuenta bancaria del empleado (cuando tiene múltiples cuentas) y soporte para monedas Soles y Dólares.

* **Liquidación y Cierre:** Proceso de visado que genera la contabilización definitiva y compensación en SAP, con descarga opcional del archivo bancario para remesa de pagos.

* **Reportes y Dashboards:** Visualización de métricas de gestión de gastos con indicadores clave, monitor de documentos en proceso, histórico de solicitudes y rendiciones por estado.

* **Mantenimiento de Datos Maestros:** Gestión de catálogos de monedas, tipos de gasto, rubros de viáticos, empresas de transporte, aerolíneas, centros de costo y configuración de parámetros del sistema.

### 1.3 Límites del sistema (Fuera de Alcance)

* **Portal del Cliente Externo:** No se incluye funcionalidad para clientes o usuarios externos ajenos a la organización. El sistema está orientado exclusivamente a empleados internos de CLARO.

* **Gestión de Proveedores y Contratos:** La administración de contratos con agencias de viaje, hoteles o proveedores de servicios queda fuera del alcance; el sistema solo registra la información de los comprobantes.

* **Planificación de Viajes Corporativos:** No incluye funcionalidades de planificación estratégica, análisis de rutas óptimas o negociación de tarifas corporativas con proveedores.

* **Gestión de Recursos Humanos:** El sistema no gestiona vacaciones, permisos o aspectos de nómina que no estén directamente relacionados con los gastos de viaje.

* **Facturación a Terceros:** No contempla la emisión de facturas a clientes externos o entidades ajenas a la organización.

* **Integración con Sistemas de Reservas Externas:** El sistema no se integra directamente con plataformas de reserva de vuelos o hoteles (GDS como Amadeus o Sabre); las cotizaciones se cargan manualmente.

* **Módulo SAP Completo:** Aunque existe integración con SAP FI para contabilización, el sistema no reemplaza ni replica toda la funcionalidad de SAP; se limita a la generación de documentos contables específicos para viajes y gastos.

* **Auditoría Financiera Avanzada:** Si bien el sistema mantiene trazabilidad, no incluye herramientas de auditoría forense o análisis de fraude más allá de las validaciones básicas de límites y políticas.
