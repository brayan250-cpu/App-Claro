## 3. Requerimientos Funcionales

### 3.1 Módulo: Gestión de Solicitudes de Gastos de Viaje

| ID | Requerimiento | Descripción |
| :-- | :-- | :-- |
| RF-SOL-001 | Crear Solicitud de Gastos | El sistema permitirá al empleado crear una solicitud de gastos de viaje ingresando datos obligatorios: origen, destino, fecha de inicio, fecha de fin, motivo del viaje, tipo de transporte (aéreo/terrestre), modalidad (con anticipo/sin anticipo), y presupuesto estimado desglosado por conceptos (alojamiento, alimentación, transporte local, otros gastos). |
| RF-SOL-002 | Calcular Presupuesto Total | El sistema calculará automáticamente el presupuesto total sumando los importes estimados de todos los conceptos ingresados. |
| RF-SOL-003 | Guardar Borrador de Solicitud | El empleado podrá guardar la solicitud como borrador sin enviarla a aprobación, permitiendo ediciones posteriores. |
| RF-SOL-004 | Enviar Solicitud a Aprobación | Una vez completados todos los campos obligatorios, el empleado podrá enviar la solicitud al flujo de aprobación, cambiando su estado a "Pendiente de Aprobación Nivel 1". |
| RF-SOL-005 | Consultar Estado de Solicitud | El empleado podrá consultar en cualquier momento el estado actual de sus solicitudes (Borrador, Pendiente Aprobación, Aprobada, Rechazada, En Rendición, Liquidada), así como el historial de transiciones de estado. |
| RF-SOL-006 | Editar Solicitud en Borrador | El empleado podrá modificar cualquier campo de una solicitud que se encuentre en estado "Borrador". |
| RF-SOL-007 | Cancelar Solicitud | El empleado podrá cancelar una solicitud en estado "Borrador" o "Pendiente de Aprobación", indicando el motivo de la cancelación. |
| RF-SOL-008 | Validar Fecha de Viaje | El sistema validará que la fecha de inicio del viaje sea posterior a la fecha de creación de la solicitud y que la fecha de fin sea posterior o igual a la fecha de inicio. |
| RF-SOL-009 | Asignar Centro de Costo Automático | El sistema asignará automáticamente el centro de costo del empleado basándose en su perfil organizacional (área/departamento). |
| RF-SOL-010 | Registrar Información de Pasaje Aéreo | Para solicitudes con tipo de transporte "Aéreo", el sistema registrará información adicional de vuelos (aerolínea, número de vuelo, clase, fecha/hora de salida y llegada, origen/destino). |
| RF-SOL-011 | Registrar Información de Pasaje Terrestre | Para solicitudes con tipo de transporte "Terrestre", el sistema registrará información adicional (empresa de transporte, distancia en km, duración estimada, ruta). |

### 3.2 Módulo: Proceso de Aprobaciones

| ID | Requerimiento | Descripción |
| :-- | :-- | :-- |
| RF-APR-001 | Notificar Aprobador Nivel 1 | Al enviar una solicitud a aprobación, el sistema enviará automáticamente una notificación por correo electrónico al Aprobador Nivel 1 configurado para el centro de costo del solicitante. |
| RF-APR-002 | Visualizar Solicitudes Pendientes | Los aprobadores podrán visualizar un listado de todas las solicitudes pendientes de su aprobación, con información resumida (solicitante, destino, fechas, monto total, fecha de solicitud). |
| RF-APR-003 | Consultar Detalle de Solicitud | Los aprobadores podrán acceder al detalle completo de cualquier solicitud para revisión, incluyendo todos los conceptos presupuestados y justificaciones. |
| RF-APR-004 | Aprobar Solicitud Nivel 1 | El Aprobador Nivel 1 podrá aprobar una solicitud, generando automáticamente una notificación al Aprobador Nivel 2 y cambiando el estado a "Pendiente de Aprobación Nivel 2". |
| RF-APR-005 | Rechazar Solicitud Nivel 1 | El Aprobador Nivel 1 podrá rechazar una solicitud, debiendo ingresar obligatoriamente el motivo del rechazo. El sistema notificará al solicitante y cambiará el estado a "Rechazada". |
| RF-APR-006 | Aprobar Solicitud Nivel 2 | El Aprobador Nivel 2 podrá aprobar definitivamente una solicitud, cambiando el estado a "Aprobada" y notificando al solicitante y al asistente de viaje (si requiere gestión de pasajes). |
| RF-APR-007 | Rechazar Solicitud Nivel 2 | El Aprobador Nivel 2 podrá rechazar una solicitud en segunda instancia, ingresando el motivo. El sistema notificará al solicitante y al Aprobador Nivel 1, cambiando el estado a "Rechazada". |
| RF-APR-008 | Delegar Aprobación | Los aprobadores podrán delegar temporalmente sus aprobaciones a otro usuario autorizado, especificando el rango de fechas de vigencia de la delegación. |
| RF-APR-009 | Historial de Aprobaciones | El sistema registrará un historial detallado de cada acción de aprobación o rechazo, incluyendo usuario que aprobó, fecha/hora, nivel de aprobación y observaciones. |
| RF-APR-010 | Recordatorio de Aprobación Pendiente | El sistema enviará recordatorios automáticos por correo electrónico a los aprobadores que tengan solicitudes pendientes por más de 48 horas. |

### 3.3 Módulo: Gestión de Cotización y Pasajes

| ID | Requerimiento | Descripción |
| :-- | :-- | :-- |
| RF-COT-001 | Notificar Asistente de Solicitud Aprobada | Cuando una solicitud de viaje con transporte aéreo sea aprobada definitivamente (Nivel 2), el sistema notificará al asistente de viajes para gestión de cotización de pasajes. |
| RF-COT-002 | Listar Solicitudes para Cotización | El asistente de viajes podrá visualizar un listado de solicitudes aprobadas pendientes de cotización de pasajes, con filtros por fecha de viaje, destino y solicitante. |
| RF-COT-003 | Cargar Opciones de Pasajes mediante Excel | El asistente podrá cargar múltiples opciones de pasajes aéreos mediante una plantilla Excel predefinida, incluyendo: aerolínea, número de vuelo, clase (económica, ejecutiva), fecha/hora de salida y llegada, origen/destino, tarifa neta, impuestos, tarifa total, moneda. |
| RF-COT-004 | Validar Plantilla de Pasajes | El sistema validará que la plantilla Excel cargada cumpla con el formato esperado, incluyendo validación de tipos de datos, valores obligatorios y coherencia de fechas/horarios. |
| RF-COT-005 | Registrar Opción de Pasaje Manual | El asistente podrá registrar opciones de pasaje de forma manual (campo por campo) como alternativa a la carga masiva. |
| RF-COT-006 | Notificar Solicitante de Opciones Disponibles | Una vez cargadas las opciones de pasajes, el sistema enviará una notificación por correo al solicitante indicando que tiene opciones disponibles para selección. |
| RF-COT-007 | Visualizar y Comparar Opciones de Pasajes | El solicitante podrá visualizar todas las opciones de pasajes cotizadas para su solicitud, con información completa de horarios, escalas, duración total del viaje y precio. |
| RF-COT-008 | Seleccionar Opción de Pasaje | El solicitante podrá seleccionar la opción de pasaje de su preferencia. El sistema notificará al asistente de viajes la opción seleccionada. |
| RF-COT-009 | Registrar Comprobante de Compra de Pasaje | El asistente de viajes registrará el comprobante de compra del pasaje (factura o boleta) con datos: tipo de documento, número, fecha de emisión, RUC del proveedor, razón social, importe neto, IGV, importe total, y adjuntará el PDF del comprobante. |
| RF-COT-010 | Calcular IGV del Comprobante | El sistema calculará automáticamente el IGV al 18% cuando el asistente ingrese el importe neto de un comprobante tipo Factura. |
| RF-COT-011 | Registrar Pasaje Terrestre | Para solicitudes con transporte terrestre, el asistente registrará información del pasaje: empresa de transporte, tipo de servicio, distancia recorrida (km), duración del viaje, fecha/hora de salida, origen/destino, número de comprobante, importe. |
| RF-COT-012 | Adjuntar Documentos de Pasaje | El sistema permitirá adjuntar archivos PDF de comprobantes y tickets de pasajes (máximo 5 MB por archivo). |

### 3.4 Módulo: Rendición de Gastos

| ID | Requerimiento | Descripción |
| :-- | :-- | :-- |
| RF-REN-001 | Iniciar Rendición de Gastos | Una vez finalizado el viaje, el empleado podrá iniciar el proceso de rendición asociado a la solicitud aprobada, cambiando el estado a "En Rendición". |
| RF-REN-002 | Registrar Comprobante de Gasto | El empleado registrará cada comprobante de gasto efectuado durante el viaje, ingresando: tipo de comprobante (Factura/Boleta), número de documento, RUC/DNI del emisor, razón social/nombre, fecha de emisión, concepto de gasto (alojamiento, alimentación, transporte local, otros), importe neto, IGV, importe total, moneda. |
| RF-REN-003 | Calcular IGV Automático en Rendición | Para comprobantes tipo Factura, el sistema calculará automáticamente el IGV al 18% cuando el empleado ingrese el importe neto. |
| RF-REN-004 | Adjuntar Comprobante Digital | El empleado podrá adjuntar el archivo PDF o imagen (JPG/PNG) del comprobante físico. El sistema validará que el tamaño no exceda 5 MB por archivo. |
| RF-REN-005 | Validar Límites de Gastos | El sistema validará que los gastos registrados por cada concepto no excedan los límites configurados en las políticas corporativas (ej. alojamiento: S/. 350 por noche, alimentación: S/. 100 por día). |
| RF-REN-006 | Justificar Exceso de Límites | Si un gasto excede el límite configurado, el sistema solicitará obligatoriamente al empleado una justificación textual del exceso. |
| RF-REN-007 | Calcular Total Gastado | El sistema calculará automáticamente el total de gastos efectuados sumando todos los comprobantes registrados en la rendición. |
| RF-REN-008 | Calcular Diferencia con Anticipo | Si la solicitud fue con anticipo, el sistema calculará la diferencia entre el monto anticipado y el total gastado, determinando si corresponde reembolso adicional al empleado o descuento/devolución. |
| RF-REN-009 | Editar Comprobante en Rendición | El empleado podrá editar o eliminar comprobantes de gasto mientras la rendición se encuentre en estado "En Rendición" (antes de enviarla a liquidación). |
| RF-REN-010 | Enviar Rendición a Liquidación | Una vez registrados todos los comprobantes, el empleado enviará la rendición al área de contabilidad para su revisión y liquidación, cambiando el estado a "Pendiente de Liquidación". |
| RF-REN-011 | Validar Rendición Completa | El sistema validará que se haya registrado al menos un comprobante antes de permitir el envío a liquidación. |
| RF-REN-012 | Notificar Operador de Rendición Pendiente | Al enviar una rendición a liquidación, el sistema notificará por correo al operador de liquidación asignado. |

### 3.5 Módulo: Integración con SAP FI

| ID | Requerimiento | Descripción |
| :-- | :-- | :-- |
| RF-SAP-001 | Generar Documento de Anticipo en SAP | Para solicitudes aprobadas con modalidad "con anticipo", el sistema generará automáticamente un documento contable de anticipo en SAP FI con: cuenta 1103010541 ANTICIPO FUNCIONARIOS, centro de costo del empleado, división, importe del anticipo, moneda, indicador CME. |
| RF-SAP-002 | Asignar Cuenta Contable según Concepto | El sistema asignará automáticamente la cuenta contable en SAP según el concepto de gasto: 4610130154 para Viáticos, 1103013002 COSTOS A COMPROBAR para anticipos, según configuración de catálogo de cuentas. |
| RF-SAP-003 | Generar Documento de Gasto en SAP | Al liquidar una rendición, el sistema generará documentos contables en SAP para cada concepto de gasto con: cuenta de gasto correspondiente, centro de costo, división, importe neto, IGV, indicador de impuesto. |
| RF-SAP-004 | Generar Documento de Compensación en SAP | Si la rendición es con anticipo, el sistema generará un documento de compensación en SAP que descuenta el anticipo del total de gastos. |
| RF-SAP-005 | Generar Documento de Reembolso/Descuento | Según el resultado de la liquidación (total gastado vs anticipo), el sistema generará un documento de reembolso o descuento en SAP: cuenta deudora si el empleado debe devolver saldo, cuenta acreedora si se le debe reembolsar. |
| RF-SAP-006 | Enviar Datos a SAP mediante Interfaz | El sistema enviará los datos contables a SAP FI mediante interfaz técnica (web service, RFC o archivo plano según arquitectura definida), incluyendo validación de respuesta de SAP. |
| RF-SAP-007 | Registrar Número de Documento SAP | Una vez confirmada la contabilización en SAP, el sistema registrará el número de documento SAP generado y la fecha de contabilización, asociándolos a la liquidación. |
| RF-SAP-008 | Reprocesar Documento SAP Rechazado | Si SAP rechaza un documento contable (ej. por error en cuenta o centro de costo), el sistema permitirá al operador corregir los datos y reenviar el documento. |
| RF-SAP-009 | Validar Disponibilidad Presupuestaria | Antes de generar documentos contables, el sistema consultará a SAP la disponibilidad presupuestaria del centro de costo para el período. |
| RF-SAP-010 | Trazabilidad de Integración SAP | El sistema registrará un log detallado de cada transacción con SAP, incluyendo: fecha/hora, tipo de documento, datos enviados, respuesta de SAP, errores (si los hay). |

### 3.6 Módulo: Generación de Archivos Bancarios

| ID | Requerimiento | Descripción |
| :-- | :-- | :-- |
| RF-BAN-001 | Seleccionar Liquidaciones para Pago | El operador de liquidación podrá seleccionar múltiples liquidaciones contabilizadas en SAP para agrupar en un lote de pago (remesa bancaria). |
| RF-BAN-002 | Agrupar Pagos por Referencia | El sistema agrupará los pagos por número de referencia, sumando los importes de liquidaciones del mismo empleado para generar un único pago por persona. |
| RF-BAN-003 | Validar Cuenta Bancaria del Empleado | El sistema validará que el empleado tenga registrada al menos una cuenta bancaria activa (banco, número de cuenta, moneda). |
| RF-BAN-004 | Seleccionar Cuenta Bancaria | Si el empleado tiene múltiples cuentas bancarias registradas, el sistema permitirá seleccionar en cuál depositar el reembolso. |
| RF-BAN-005 | Generar Archivo SCT para BCP | El sistema generará un archivo de texto en formato SCT (estándar Banco de Crédito del Perú) con los datos de cada pago: tipo de registro, número de cuenta destino, importe, moneda, referencia (número de liquidación). |
| RF-BAN-006 | Generar Archivo SCT para Scotiabank | El sistema generará un archivo de texto en formato SCT (estándar Scotiabank) con estructura específica del banco, adaptando los campos según su especificación técnica. |
| RF-BAN-007 | Convertir Moneda en Archivo Bancario | El sistema incluirá en el archivo bancario los importes en la moneda original (Soles o Dólares) según la cuenta bancaria seleccionada. |
| RF-BAN-008 | Descargar Archivo Bancario | El operador podrá descargar el archivo SCT generado en formato .txt para subirlo al portal del banco. |
| RF-BAN-009 | Registrar Fecha de Generación de Remesa | El sistema registrará la fecha y hora de generación de cada archivo bancario, así como el usuario que lo generó. |
| RF-BAN-010 | Confirmar Ejecución de Remesa | El operador podrá confirmar en el sistema que la remesa bancaria fue ejecutada exitosamente, registrando la fecha de pago efectivo y cambiando el estado de las liquidaciones a "Pagada". |
| RF-BAN-011 | Cancelar Archivo Bancario | El operador podrá anular un archivo bancario generado si detecta errores antes de subirlo al banco, permitiendo regenerar el archivo con correcciones. |

### 3.7 Módulo: Liquidación y Cierre

| ID | Requerimiento | Descripción |
| :-- | :-- | :-- |
| RF-LIQ-001 | Listar Rendiciones Pendientes de Liquidación | El operador de liquidación podrá visualizar todas las rendiciones en estado "Pendiente de Liquidación", con filtros por fecha, solicitante, centro de costo y monto. |
| RF-LIQ-002 | Revisar Comprobantes de Rendición | El operador podrá acceder a todos los comprobantes registrados en una rendición, incluyendo visualización de los archivos PDF adjuntos. |
| RF-LIQ-003 | Solicitar Corrección de Rendición | Si detecta errores o falta de documentación, el operador podrá devolver la rendición al empleado solicitando correcciones, ingresando obligatoriamente las observaciones. El sistema notificará al empleado y cambiará el estado a "En Corrección". |
| RF-LIQ-004 | Corregir Rendición Observada | El empleado recibirá notificación de rendición observada, podrá visualizar las observaciones del operador, corregir los comprobantes y reenviar a liquidación. |
| RF-LIQ-005 | Ejecutar Proceso de Visado | Una vez validados todos los comprobantes, el operador ejecutará el proceso de "visado" que: genera los documentos contables en SAP (anticipos, gastos, compensaciones, reembolsos/descuentos), registra número de documento SAP, marca la rendición como "Liquidada y Visada". |
| RF-LIQ-006 | Calcular Líquido a Pagar | El sistema calculará el importe líquido a pagar al empleado: Total Gastado - Anticipo Recibido + Ajustes (si los hay) = Líquido a Pagar/Descontar. |
| RF-LIQ-007 | Generar Resumen de Liquidación | El sistema generará un documento PDF resumen de la liquidación con: datos del solicitante, datos del viaje, detalle de gastos por concepto, anticipo recibido, total gastado, líquido a pagar, números de documentos SAP, fecha de visado. |
| RF-LIQ-008 | Descargar Resumen de Liquidación | El empleado y el operador podrán descargar el PDF resumen de liquidación para archivo o impresión. |
| RF-LIQ-009 | Consultar Histórico de Liquidaciones | Los usuarios podrán consultar el histórico completo de todas las liquidaciones procesadas, con filtros por fecha, estado, empleado, centro de costo. |
| RF-LIQ-010 | Reversar Liquidación | En casos excepcionales, un usuario con permisos especiales (administrador o supervisor de contabilidad) podrá reversar una liquidación ya visada, ingresando obligatoriamente el motivo. El sistema generará documentos de reversión en SAP. |

### 3.8 Módulo: Reportes y Dashboards

| ID | Requerimiento | Descripción |
| :-- | :-- | :-- |
| RF-REP-001 | Dashboard de Indicadores de Gestión | El sistema mostrará un dashboard con indicadores clave: total de solicitudes del mes, total de gastos autorizados, promedio de días en aprobación, solicitudes por estado (gráfico de torta), top 10 destinos, top 10 solicitantes por gasto total. |
| RF-REP-002 | Reporte de Solicitudes por Período | Generar reporte en Excel con listado de todas las solicitudes en un rango de fechas, incluyendo: solicitante, destino, fecha viaje, monto estimado, monto real, estado, aprobadores, fechas de aprobación. |
| RF-REP-003 | Reporte de Gastos por Centro de Costo | Generar reporte consolidado de gastos por centro de costo y concepto (alojamiento, alimentación, transporte, otros), con totales por mes y comparativo año anterior. |
| RF-REP-004 | Reporte de Liquidaciones Pendientes | Listar todas las rendiciones pendientes de liquidación con más de X días (configurable), incluyendo alertas por antigüedad. |
| RF-REP-005 | Reporte de Comprobantes por Proveedor | Generar reporte de comprobantes registrados agrupados por proveedor (RUC), con totales de gasto por proveedor y concepto. |
| RF-REP-006 | Reporte de Documentos SAP Generados | Listar todos los documentos contables generados en SAP en un rango de fechas, con filtros por tipo de documento, centro de costo, cuenta contable. |
| RF-REP-007 | Reporte de Anticipos Pendientes de Rendir | Generar reporte de empleados con anticipos entregados que aún no han rendido gastos, con antigüedad y saldo pendiente. |
| RF-REP-008 | Exportar Reportes a Excel | Todos los reportes del sistema podrán ser exportados a formato Excel (.xlsx) para análisis fuera del sistema. |
| RF-REP-009 | Programar Envío Automático de Reportes | El administrador podrá configurar el envío automático de reportes específicos por correo electrónico con periodicidad (diaria, semanal, mensual). |
| RF-REP-010 | Monitor de Documentos en Proceso | Pantalla de monitoreo en tiempo real que muestra documentos en cada etapa del proceso (solicitud → aprobación → cotización → rendición → liquidación → pago) con códigos de colores según antigüedad. |

### 3.9 Módulo: Administración y Configuración

| ID | Requerimiento | Descripción |
| :-- | :-- | :-- |
| RF-ADM-001 | Gestión de Usuarios | El administrador podrá crear, modificar y desactivar usuarios del sistema, ingresando: nombre completo, correo electrónico, número de documento, centro de costo, área, cargo, usuario de acceso, contraseña inicial. |
| RF-ADM-002 | Asignación de Roles | El administrador asignará uno o más roles a cada usuario (Empleado, Asistente, Aprobador Nivel 1, Aprobador Nivel 2, Operador Liquidación, Auditor, Administrador). |
| RF-ADM-003 | Configurar Flujo de Aprobación | El administrador configurará por centro de costo quiénes son los Aprobadores Nivel 1 y Nivel 2, permitiendo asignar múltiples aprobadores y definir si es aprobación en serie o paralela. |
| RF-ADM-004 | Gestión de Catálogo de Monedas | Mantener el catálogo de monedas disponibles en el sistema (PEN - Soles, USD - Dólares), con código ISO, símbolo y tipo de cambio de referencia. |
| RF-ADM-005 | Gestión de Catálogo de Tipos de Gasto | Mantener el catálogo de conceptos de gasto (Alojamiento, Alimentación, Transporte Local, Transporte Aéreo, Transporte Terrestre, Otros Gastos), cada uno con su cuenta contable SAP asociada. |
| RF-ADM-006 | Gestión de Límites de Gastos | Configurar los límites máximos de gastos por concepto (ej. Alojamiento: S/. 350/noche, Alimentación: S/. 100/día) para diferentes categorías de empleados o destinos. |
| RF-ADM-007 | Gestión de Catálogo de Aerolíneas | Mantener el catálogo de aerolíneas con código IATA, nombre comercial, país de origen. |
| RF-ADM-008 | Gestión de Empresas de Transporte Terrestre | Mantener el catálogo de empresas de transporte terrestre con RUC, razón social, tipo de servicio (ómnibus, van, taxi). |
| RF-ADM-009 | Gestión de Centros de Costo | Mantener el catálogo de centros de costo con código SAP, descripción, área/departamento, responsable. |
| RF-ADM-010 | Gestión de Cuentas Contables SAP | Mantener el catálogo de cuentas contables con código SAP, descripción, tipo de cuenta (deudora/acreedora), indicador de impuesto. |
| RF-ADM-011 | Configurar Parámetros del Sistema | El administrador configurará parámetros globales: días de recordatorio para aprobaciones pendientes, días de antigüedad para alertas de rendición, tamaño máximo de archivos adjuntos, formato de archivos bancarios por banco, tasa de IGV. |
| RF-ADM-012 | Auditar Acciones de Usuarios | El sistema registrará en un log de auditoría todas las acciones críticas realizadas por usuarios: login, creación/modificación de solicitudes, aprobaciones/rechazos, liquidaciones, modificación de configuraciones, con fecha/hora, IP y usuario. |
| RF-ADM-013 | Gestión de Cuentas Bancarias de Empleados | El administrador o el propio empleado podrá registrar/modificar sus cuentas bancarias personales, ingresando: banco, número de cuenta, tipo de cuenta (ahorros/corriente), moneda, condición de activa/inactiva. |
| RF-ADM-014 | Configurar Plantilla de Correos | El administrador podrá personalizar las plantillas HTML de correos electrónicos enviados por el sistema (notificaciones de aprobación, recordatorios, rechazos) incluyendo logo corporativo y firma. |
| RF-ADM-015 | Backup y Restauración | El administrador podrá ejecutar respaldos manuales de la base de datos y restaurar desde backups previos en caso de contingencia. |
