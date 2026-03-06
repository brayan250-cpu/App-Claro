## 5. Historias de Usuario

### 5.1 Módulo: Gestión de Solicitudes de Gastos de Viaje

#### **HU-001: Crear solicitud de gastos de viaje**
**Como** empleado
**Quiero** crear una solicitud de gastos de viaje ingresando todos los detalles del viaje (origen, destino, fechas, motivo, presupuesto)
**Para** obtener la autorización y el presupuesto necesario para mi viaje corporativo

**Criterios de aceptación:**
- [ ] El sistema muestra un formulario con campos obligatorios: origen, destino, fecha inicio, fecha fin, motivo, tipo de transporte, modalidad (con/sin anticipo)
- [ ] Puedo ingresar el presupuesto estimado desglosado por conceptos (alojamiento, alimentación, transporte, otros)
- [ ] El sistema calcula automáticamente el presupuesto total sumando todos los conceptos
- [ ] El sistema asigna automáticamente mi centro de costo según mi perfil organizacional
- [ ] Puedo guardar la solicitud como borrador sin enviarla a aprobación
- [ ] El sistema valida que la fecha de inicio sea posterior a hoy y que la fecha fin sea posterior o igual a la fecha inicio
- [ ] Si el transporte es aéreo, puedo ingresar información adicional de vuelos (aerolínea, número de vuelo, clase, horarios)
- [ ] Si el transporte es terrestre, puedo ingresar información adicional (empresa, distancia, duración, ruta)

**ID Requerimientos relacionados:** RF-SOL-001, RF-SOL-002, RF-SOL-008, RF-SOL-009, RF-SOL-010, RF-SOL-011

#### **HU-002: Enviar solicitud a aprobación**
**Como** empleado
**Quiero** enviar mi solicitud de gastos al flujo de aprobación una vez completados todos los datos
**Para** que mis superiores autoricen mi viaje

**Criterios de aceptación:**
- [ ] El sistema valida que todos los campos obligatorios estén completos antes de permitir el envío
- [ ] Al enviar, el estado de la solicitud cambia a "Pendiente de Aprobación Nivel 1"
- [ ] El sistema envía automáticamente una notificación por correo electrónico al Aprobador Nivel 1
- [ ] No puedo editar la solicitud una vez enviada a aprobación
- [ ] Recibo una confirmación en pantalla del envío exitoso

**ID Requerimientos relacionados:** RF-SOL-004, RF-APR-001

#### **HU-003: Consultar estado de mis solicitudes**
**Como** empleado
**Quiero** consultar en cualquier momento el estado actual de mis solicitudes
**Para** hacer seguimiento a su proceso de aprobación y saber cuándo puedo realizar el viaje

**Criterios de aceptación:**
- [ ] Puedo ver un listado de todas mis solicitudes con información resumida (destino, fechas, monto, estado)
- [ ] Puedo filtrar por estado (Borrador, Pendiente Aprobación, Aprobada, Rechazada, En Rendición, Liquidada)
- [ ] Puedo ver el historial de transiciones de estado con fechas y responsables
- [ ] Si la solicitud fue rechazada, puedo visualizar el motivo del rechazo
- [ ] Puedo acceder al detalle completo de cada solicitud

**ID Requerimientos relacionados:** RF-SOL-005

#### **HU-004: Editar o cancelar solicitud en borrador**
**Como** empleado
**Quiero** modificar o cancelar una solicitud que guardé como borrador
**Para** corregir información antes de enviarla a aprobación o descartar solicitudes que ya no proceden

**Criterios de aceptación:**
- [ ] Solo puedo editar solicitudes en estado "Borrador"
- [ ] Puedo modificar cualquier campo de la solicitud
- [ ] Puedo cancelar la solicitud ingresando un motivo de cancelación
- [ ] Al cancelar, el estado cambia a "Cancelada" y no puedo reactivarla
- [ ] El sistema confirma la acción antes de cancelar definitivamente

**ID Requerimientos relacionados:** RF-SOL-006, RF-SOL-007

### 5.2 Módulo: Proceso de Aprobaciones

#### **HU-005: Visualizar solicitudes pendientes de aprobación**
**Como** aprobador (Nivel 1 o Nivel 2)
**Quiero** visualizar todas las solicitudes pendientes de mi aprobación
**Para** revisarlas y tomar una decisión de autorización

**Criterios de aceptación:**
- [ ] Veo un listado de todas las solicitudes pendientes de mi aprobación según mi nivel
- [ ] Cada solicitud muestra información resumida: solicitante, destino, fechas, monto total, fecha de solicitud
- [ ] Puedo filtrar por fecha, solicitante, monto o estado
- [ ] Puedo ordenar la lista por antigüedad o monto
- [ ] El sistema indica visualmente las solicitudes con más de 48 horas pendientes (alerta de prioridad)

**ID Requerimientos relacionados:** RF-APR-002, RF-APR-010

#### **HU-006: Aprobar o rechazar solicitudes (Nivel 1)**
**Como** aprobador de Nivel 1
**Quiero** revisar el detalle de una solicitud y aprobarla o rechazarla
**Para** autorizar o denegar los viajes de mi equipo según políticas y presupuesto

**Criterios de aceptación:**
- [ ] Puedo acceder al detalle completo de la solicitud (todos los datos del viaje y presupuesto)
- [ ] Puedo aprobar la solicitud, generando una notificación al Aprobador Nivel 2 y cambiando el estado a "Pendiente de Aprobación Nivel 2"
- [ ] Puedo rechazar la solicitud, pero el sistema me obliga a ingresar un motivo de rechazo
- [ ] Al rechazar, el sistema notifica al solicitante y cambia el estado a "Rechazada"
- [ ] El sistema registra mi aprobación/rechazo en el historial con fecha, hora y observaciones

**ID Requerimientos relacionados:** RF-APR-003, RF-APR-004, RF-APR-005, RF-APR-009

#### **HU-007: Aprobar o rechazar solicitudes (Nivel 2)**
**Como** aprobador de Nivel 2
**Quiero** revisar solicitudes ya aprobadas en primer nivel y dar aprobación definitiva
**Para** autorizar o denegar viajes de mayor importe o alcance estratégico

**Criterios de aceptación:**
- [ ] Veo solo solicitudes que ya fueron aprobadas por el Aprobador Nivel 1
- [ ] Puedo ver el historial de aprobación previa (quién y cuándo aprobó en Nivel 1)
- [ ] Puedo aprobar definitivamente, cambiando el estado a "Aprobada" y notificando al solicitante y asistente de viaje
- [ ] Puedo rechazar en segunda instancia, ingresando obligatoriamente un motivo
- [ ] Al rechazar, el sistema notifica al solicitante y al Aprobador Nivel 1
- [ ] El sistema registra mi decisión en el historial

**ID Requerimientos relacionados:** RF-APR-003, RF-APR-006, RF-APR-007, RF-APR-009

#### **HU-008: Delegar aprobaciones temporalmente**
**Como** aprobador (Nivel 1 o Nivel 2)
**Quiero** delegar mis aprobaciones a otro usuario autorizado durante un período específico
**Para** asegurar continuidad en el proceso cuando esté ausente (vacaciones, enfermedad)

**Criterios de aceptación:**
- [ ] Puedo seleccionar un usuario autorizado como delegado temporal
- [ ] Debo especificar fecha de inicio y fecha de fin de la delegación
- [ ] Durante el período de delegación, las solicitudes pendientes se asignan automáticamente al delegado
- [ ] El delegado recibe notificaciones de solicitudes pendientes como si fuera el aprobador original
- [ ] Puedo visualizar y cancelar delegaciones activas antes de su fecha de fin
- [ ] El sistema registra todas las delegaciones en el historial de auditoría

**ID Requerimientos relacionados:** RF-APR-008

#### **HU-009: Recibir recordatorios de aprobaciones pendientes**
**Como** aprobador
**Quiero** recibir recordatorios automáticos por correo electrónico de solicitudes pendientes por más tiempo del establecido
**Para** no olvidar aprobar solicitudes y evitar retrasos en los viajes de mi equipo

**Criterios de aceptación:**
- [ ] Si tengo solicitudes pendientes por más de 48 horas, recibo un correo recordatorio
- [ ] El correo incluye un listado de todas las solicitudes pendientes con datos resumidos
- [ ] El correo incluye un enlace directo al sistema para acceder rápidamente
- [ ] Los recordatorios se envían diariamente hasta que se atienda la solicitud

**ID Requerimientos relacionados:** RF-APR-010

### 5.3 Módulo: Gestión de Cotización y Pasajes

#### **HU-010: Recibir solicitudes aprobadas para cotización**
**Como** asistente de viaje
**Quiero** recibir notificaciones de solicitudes aprobadas que requieren gestión de pasajes
**Para** iniciar el proceso de cotización con agencias

**Criterios de aceptación:**
- [ ] Recibo una notificación por correo cuando una solicitud con transporte aéreo es aprobada definitivamente (Nivel 2)
- [ ] Puedo visualizar un listado de solicitudes aprobadas pendientes de cotización
- [ ] Puedo filtrar por fecha de viaje, destino y solicitante
- [ ] Cada solicitud muestra los datos del viaje necesarios para cotizar (origen, destino, fechas, clase solicitada)

**ID Requerimientos relacionados:** RF-COT-001, RF-COT-002

#### **HU-011: Cargar opciones de pasajes mediante plantilla Excel**
**Como** asistente de viaje
**Quiero** cargar múltiples opciones de pasajes aéreos de forma masiva mediante una plantilla Excel
**Para** agilizar el registro de cotizaciones recibidas de las agencias

**Criterios de aceptación:**
- [ ] El sistema proporciona una plantilla Excel predefinida con las columnas requeridas (aerolínea, vuelo, clase, fecha/hora salida, fecha/hora llegada, origen, destino, tarifa neta, impuestos, tarifa total, moneda)
- [ ] Puedo descargar la plantilla, completarla fuera del sistema y cargarla desde mi computadora
- [ ] El sistema valida que la plantilla cumpla con el formato esperado y los tipos de datos
- [ ] Si hay errores en la plantilla, el sistema muestra un mensaje detallado indicando las filas/columnas con problemas
- [ ] Si la validación es exitosa, el sistema carga todas las opciones y me muestra un resumen de opciones registradas
- [ ] El sistema asocia automáticamente las opciones a la solicitud correspondiente

**ID Requerimientos relacionados:** RF-COT-003, RF-COT-004

#### **HU-012: Registrar opciones de pasajes manualmente**
**Como** asistente de viaje
**Quiero** registrar opciones de pasaje de forma manual campo por campo
**Para** cotizaciones individuales o cuando no puedo usar la carga masiva

**Criterios de aceptación:**
- [ ] El sistema muestra un formulario con todos los campos de un pasaje aéreo
- [ ] Puedo ingresar datos: aerolínea, número de vuelo, clase, fechas/horas, origen/destino, tarifas
- [ ] El sistema calcula automáticamente la tarifa total sumando tarifa neta + impuestos
- [ ] Puedo registrar múltiples opciones para la misma solicitud
- [ ] Puedo editar o eliminar opciones antes de notificar al solicitante

**ID Requerimientos relacionados:** RF-COT-005

#### **HU-013: Notificar al solicitante las opciones disponibles**
**Como** asistente de viaje
**Quiero** notificar al solicitante una vez que he cargado todas las opciones de pasajes
**Para** que pueda revisar y seleccionar la opción de su preferencia

**Criterios de aceptación:**
- [ ] Una vez cargadas las opciones, puedo seleccionar la opción "Notificar al solicitante"
- [ ] El sistema envía automáticamente un correo al solicitante indicando que tiene opciones disponibles
- [ ] El correo incluye un enlace directo a la pantalla de selección de pasajes
- [ ] El estado de la solicitud cambia a "Pendiente de Selección de Pasaje"

**ID Requerimientos relacionados:** RF-COT-006

#### **HU-014: Visualizar y seleccionar opciones de pasajes**
**Como** empleado solicitante
**Quiero** visualizar todas las opciones de pasajes cotizadas y seleccionar la de mi preferencia
**Para** confirmar mi itinerario de viaje

**Criterios de aceptación:**
- [ ] Puedo visualizar todas las opciones de pasajes con información completa: aerolínea, número de vuelo, horarios, escalas, duración total, precio
- [ ] Las opciones se muestran en formato comparativo fácil de leer (ej. tarjetas o tabla)
- [ ] Puedo ordenar las opciones por precio, duración o aerolínea
- [ ] Puedo seleccionar una opción haciendo clic en un botón "Seleccionar"
- [ ] El sistema me solicita confirmación antes de confirmar la selección
- [ ] Una vez seleccionada, el sistema notifica al asistente de viaje
- [ ] El estado cambia a "Pasaje Seleccionado - Pendiente de Compra"

**ID Requerimientos relacionados:** RF-COT-007, RF-COT-008

#### **HU-015: Registrar comprobante de compra de pasaje**
**Como** asistente de viaje
**Quiero** registrar el comprobante de compra del pasaje una vez adquirido
**Para** tener trazabilidad del gasto y documentación respaldatoria

**Criterios de aceptación:**
- [ ] Puedo ingresar datos del comprobante: tipo (Factura/Boleta), número, fecha emisión, RUC del proveedor, razón social, importe neto, IGV, importe total
- [ ] Si es Factura, el sistema calcula automáticamente el IGV al 18% cuando ingreso el importe neto
- [ ] Puedo adjuntar el archivo PDF del comprobante (máximo 5 MB)
- [ ] El sistema valida que el archivo sea PDF y no exceda el tamaño máximo
- [ ] Una vez registrado, el estado de la solicitud cambia a "Pasaje Comprado"
- [ ] El solicitante recibe notificación de que su pasaje fue adquirido

**ID Requerimientos relacionados:** RF-COT-009, RF-COT-010, RF-COT-012

#### **HU-016: Registrar información de pasaje terrestre**
**Como** asistente de viaje
**Quiero** registrar información de pasajes terrestres para solicitudes con este tipo de transporte
**Para** documentar el viaje por carretera y sus costos

**Criterios de aceptación:**
- [ ] Para solicitudes con transporte terrestre, puedo ingresar: empresa de transporte, tipo de servicio, distancia (km), duración, fecha/hora salida, origen/destino
- [ ] Puedo registrar el número de comprobante e importe del pasaje
- [ ] Puedo adjuntar el comprobante en PDF
- [ ] El sistema registra esta información asociada a la solicitud
- [ ] El estado cambia a "Pasaje Terrestre Registrado"

**ID Requerimientos relacionados:** RF-COT-011, RF-COT-012

### 5.4 Módulo: Rendición de Gastos

#### **HU-017: Iniciar rendición de gastos**
**Como** empleado
**Quiero** iniciar el proceso de rendición una vez finalizado mi viaje
**Para** registrar todos los comprobantes de gasto y obtener el reembolso correspondiente

**Criterios de aceptación:**
- [ ] Solo puedo iniciar rendición de solicitudes en estado "Aprobada" o "Pasaje Comprado/Registrado"
- [ ] Al iniciar, el estado cambia a "En Rendición"
- [ ] El sistema muestra un formulario para registrar comprobantes de gasto
- [ ] Puedo ver el presupuesto aprobado por concepto como referencia

**ID Requerimientos relacionados:** RF-REN-001

#### **HU-018: Registrar comprobantes de gasto**
**Como** empleado
**Quiero** registrar cada comprobante de gasto que generé durante el viaje (facturas, boletas)
**Para** justificar mis gastos y recibir el reembolso

**Criterios de aceptación:**
- [ ] Puedo agregar múltiples comprobantes, uno por uno
- [ ] Para cada comprobante ingreso: tipo (Factura/Boleta), número, RUC/DNI del emisor, razón social/nombre, fecha emisión, concepto de gasto (alojamiento, alimentación, transporte local, otros)
- [ ] Ingreso importe neto, IGV e importe total; si es Factura, el sistema calcula automáticamente el IGV al 18%
- [ ] Puedo adjuntar el archivo PDF o imagen (JPG/PNG) del comprobante físico (máximo 5 MB por archivo)
- [ ] El sistema valida que el archivo no exceda el tamaño máximo
- [ ] Puedo editar o eliminar comprobantes mientras la rendición esté en estado "En Rendición"

**ID Requerimientos relacionados:** RF-REN-002, RF-REN-003, RF-REN-004, RF-REN-009

#### **HU-019: Validar límites de gastos y justificar excesos**
**Como** empleado
**Quiero** que el sistema valide automáticamente si mis gastos exceden los límites corporativos
**Para** cumplir con las políticas de viáticos o justificar excepciones cuando sean necesarias

**Criterios de aceptación:**
- [ ] Al registrar un comprobante, el sistema valida automáticamente si el gasto excede el límite configurado para ese concepto (ej. alojamiento: S/. 350/noche)
- [ ] Si excede el límite, el sistema muestra una alerta y me solicita obligatoriamente ingresar una justificación textual del exceso
- [ ] No puedo guardar el comprobante sin ingresar la justificación cuando hay exceso
- [ ] La justificación queda registrada asociada al comprobante para revisión del operador de liquidación

**ID Requerimientos relacionados:** RF-REN-005, RF-REN-006

#### **HU-020: Visualizar cálculo de total gastado y diferencia con anticipo**
**Como** empleado
**Quiero** visualizar el total de gastos registrados y la diferencia con el anticipo recibido (si aplica)
**Para** saber si debo devolver saldo o me corresponde reembolso adicional

**Criterios de aceptación:**
- [ ] El sistema calcula y muestra en tiempo real el total de gastos sumando todos los comprobantes registrados
- [ ] Si mi solicitud fue con anticipo, el sistema muestra: Anticipo recibido, Total gastado, Diferencia (a favor o en contra)
- [ ] Si la diferencia es positiva (gasté más del anticipo), veo "Reembolso a recibir: S/. XXX"
- [ ] Si la diferencia es negativa (gasté menos del anticipo), veo "Saldo a devolver: S/. XXX"
- [ ] Esta información se actualiza dinámicamente al agregar/editar/eliminar comprobantes

**ID Requerimientos relacionados:** RF-REN-007, RF-REN-008

#### **HU-021: Enviar rendición a liquidación**
**Como** empleado
**Quiero** enviar mi rendición al área de contabilidad una vez registrados todos los comprobantes
**Para** que revisen, aprueben y procesen el reembolso

**Criterios de aceptación:**
- [ ] El sistema valida que haya registrado al menos un comprobante antes de permitir el envío
- [ ] Puedo revisar un resumen completo de la rendición antes de enviar (todos los comprobantes y montos)
- [ ] Al enviar, el estado cambia a "Pendiente de Liquidación"
- [ ] El sistema envía automáticamente una notificación por correo al operador de liquidación asignado
- [ ] Una vez enviada, no puedo editar ni eliminar comprobantes (solo el operador puede devolver para correcciones)
- [ ] Recibo una confirmación en pantalla del envío exitoso

**ID Requerimientos relacionados:** RF-REN-010, RF-REN-011, RF-REN-012

### 5.5 Módulo: Integración con SAP FI

#### **HU-022: Generar documentos contables en SAP automáticamente**
**Como** operador de liquidación
**Quiero** que el sistema genere automáticamente los documentos contables en SAP al ejecutar el visado
**Para** no tener que registrar manualmente cada transacción en SAP y evitar errores

**Criterios de aceptación:**
- [ ] Al ejecutar el proceso de visado de una rendición, el sistema genera automáticamente los documentos contables necesarios en SAP FI
- [ ] Para solicitudes con anticipo, se genera documento de anticipo (cuenta 1103010541 ANTICIPO FUNCIONARIOS)
- [ ] Se generan documentos de gasto por cada concepto (alojamiento, alimentación, transporte, etc.) con sus cuentas contables correspondientes
- [ ] Si hay anticipo, se genera documento de compensación que descuenta el anticipo del total de gastos
- [ ] Se genera documento de reembolso (si el empleado gastó más que el anticipo) o descuento (si gastó menos)
- [ ] Cada documento incluye: centro de costo, división, importe, moneda, indicador CME
- [ ] El sistema valida disponibilidad presupuestaria en SAP antes de generar los documentos

**ID Requerimientos relacionados:** RF-SAP-001, RF-SAP-002, RF-SAP-003, RF-SAP-004, RF-SAP-005, RF-SAP-009

#### **HU-023: Registrar número de documento SAP y trazabilidad**
**Como** operador de liquidación
**Quiero** que el sistema registre automáticamente los números de documento SAP generados
**Para** mantener trazabilidad completa entre el sistema de viajes y SAP

**Criterios de aceptación:**
- [ ] Una vez confirmada la contabilización en SAP, el sistema registra automáticamente el número de documento SAP generado
- [ ] Se registra la fecha de contabilización SAP
- [ ] Estos datos quedan asociados permanentemente a la liquidación
- [ ] Puedo consultar los números de documento SAP desde el detalle de la liquidación
- [ ] El sistema registra un log detallado de cada transacción con SAP: fecha/hora, tipo de documento, datos enviados, respuesta de SAP

**ID Requerimientos relacionados:** RF-SAP-007, RF-SAP-010

#### **HU-024: Reprocesar documentos SAP rechazados**
**Como** operador de liquidación
**Quiero** corregir datos y reenviar documentos contables que fueron rechazados por SAP
**Para** resolver errores y completar la contabilización sin perder información

**Criterios de aceptación:**
- [ ] Si SAP rechaza un documento (ej. error en cuenta o centro de costo), el sistema me notifica del error con el mensaje de SAP
- [ ] Puedo acceder a la liquidación y editar los datos contables (cuenta, centro de costo, división)
- [ ] Puedo seleccionar la opción "Reprocesar en SAP"
- [ ] El sistema reenvía el documento corregido a SAP
- [ ] Si el reenvío es exitoso, se registra el nuevo número de documento SAP
- [ ] Todo el proceso de rechazo y reproceso queda registrado en el log de auditoría

**ID Requerimientos relacionados:** RF-SAP-008, RF-SAP-010

### 5.6 Módulo: Generación de Archivos Bancarios

#### **HU-025: Seleccionar liquidaciones y generar archivo bancario**
**Como** operador de liquidación
**Quiero** seleccionar múltiples liquidaciones y generar un archivo bancario para remesa de pagos
**Para** agrupar reembolsos en un solo lote y ejecutar pagos masivos a empleados

**Criterios de aceptación:**
- [ ] Puedo visualizar todas las liquidaciones contabilizadas en SAP que están pendientes de pago
- [ ] Puedo seleccionar múltiples liquidaciones mediante checkboxes
- [ ] El sistema agrupa los pagos por número de referencia, sumando importes de liquidaciones del mismo empleado para generar un único pago
- [ ] El sistema valida que cada empleado tenga registrada al menos una cuenta bancaria activa
- [ ] Si un empleado tiene múltiples cuentas, puedo seleccionar en cuál depositar
- [ ] Puedo elegir el formato del archivo: BCP o Scotiabank
- [ ] El sistema genera el archivo SCT en formato de texto (.txt) según el estándar del banco seleccionado
- [ ] El archivo incluye: tipo de registro, número de cuenta destino, importe, moneda, referencia (número de liquidación)

**ID Requerimientos relacionados:** RF-BAN-001, RF-BAN-002, RF-BAN-003, RF-BAN-004, RF-BAN-005, RF-BAN-006, RF-BAN-007

#### **HU-026: Descargar y confirmar ejecución de remesa bancaria**
**Como** operador de liquidación
**Quiero** descargar el archivo bancario generado y confirmar su ejecución en el banco
**Para** completar el proceso de pago a empleados

**Criterios de aceptación:**
- [ ] Una vez generado el archivo, puedo descargarlo en formato .txt desde el sistema
- [ ] El sistema registra la fecha y hora de generación del archivo, así como mi usuario
- [ ] Puedo subir el archivo al portal del banco y ejecutar la remesa
- [ ] Una vez ejecutada la remesa en el banco, puedo volver al sistema y confirmar la ejecución
- [ ] Al confirmar, ingreso la fecha de pago efectivo
- [ ] El estado de todas las liquidaciones incluidas en la remesa cambia a "Pagada"
- [ ] Se notifica por correo a cada empleado que su reembolso fue procesado

**ID Requerimientos relacionados:** RF-BAN-008, RF-BAN-009, RF-BAN-010

#### **HU-027: Anular archivo bancario generado**
**Como** operador de liquidación
**Quiero** anular un archivo bancario generado si detecto errores antes de subirlo al banco
**Para** corregir los errores y regenerar el archivo correctamente

**Criterios de aceptación:**
- [ ] Puedo seleccionar un archivo bancario generado que aún no se haya confirmado como ejecutado
- [ ] Puedo anular el archivo, ingresando un motivo de anulación
- [ ] Al anular, las liquidaciones incluidas vuelven a estado "Pendiente de Pago" (disponibles para incluir en un nuevo archivo)
- [ ] El archivo anulado queda registrado en el historial con estado "Anulado" para auditoría
- [ ] Puedo regenerar un nuevo archivo con las correcciones necesarias

**ID Requerimientos relacionados:** RF-BAN-011

### 5.7 Módulo: Liquidación y Cierre

#### **HU-028: Visualizar rendiciones pendientes de liquidación**
**Como** operador de liquidación
**Quiero** visualizar todas las rendiciones pendientes de liquidación
**Para** priorizarlas y procesarlas oportunamente

**Criterios de aceptación:**
- [ ] Veo un listado de todas las rendiciones en estado "Pendiente de Liquidación"
- [ ] Cada rendición muestra: solicitante, destino, fecha de viaje, total gastado, anticipo, diferencia, fecha de envío
- [ ] Puedo filtrar por fecha, solicitante, centro de costo y monto
- [ ] Puedo ordenar por antigüedad o monto
- [ ] El sistema indica visualmente rendiciones con más de X días pendientes (alerta de prioridad)

**ID Requerimientos relacionados:** RF-LIQ-001

#### **HU-029: Revisar comprobantes y solicitar correcciones**
**Como** operador de liquidación
**Quiero** revisar todos los comprobantes de una rendición y solicitar correcciones si detecto errores
**Para** asegurar que la documentación esté completa y correcta antes de contabilizar

**Criterios de aceptación:**
- [ ] Puedo acceder al detalle de cada comprobante registrado en la rendición
- [ ] Puedo visualizar los archivos PDF adjuntos de cada comprobante
- [ ] Puedo ver las justificaciones de excesos de límites
- [ ] Si detecto errores o falta documentación, puedo seleccionar "Devolver para corrección"
- [ ] Debo ingresar obligatoriamente las observaciones detallando qué debe corregirse
- [ ] Al devolver, el estado cambia a "En Corrección" y el empleado recibe notificación con las observaciones
- [ ] El empleado puede corregir y reenviar; yo recibo notificación de reenvío

**ID Requerimientos relacionados:** RF-LIQ-002, RF-LIQ-003, RF-LIQ-004

#### **HU-030: Ejecutar proceso de visado y liquidación**
**Como** operador de liquidación
**Quiero** ejecutar el proceso de visado una vez validados todos los comprobantes
**Para** generar la contabilización definitiva en SAP y habilitar el pago al empleado

**Criterios de aceptación:**
- [ ] Solo puedo ejecutar el visado en rendiciones completamente validadas (sin observaciones pendientes)
- [ ] Al ejecutar el visado, el sistema: genera automáticamente todos los documentos contables en SAP (anticipos, gastos, compensaciones, reembolsos/descuentos), registra números de documento SAP y fechas de contabilización, cambia el estado a "Liquidada y Visada"
- [ ] El sistema calcula el importe líquido a pagar: Total Gastado - Anticipo Recibido = Líquido a Pagar/Descontar
- [ ] Se genera automáticamente un PDF resumen de liquidación con todos los datos
- [ ] El empleado recibe notificación de que su rendición fue liquidada
- [ ] Si hay errores en la contabilización SAP, el sistema me notifica y no cambia el estado (puedo corregir y reintentar)

**ID Requerimientos relacionados:** RF-LIQ-005, RF-LIQ-006, RF-SAP-001 a RF-SAP-007

#### **HU-031: Descargar resumen de liquidación**
**Como** empleado u operador de liquidación
**Quiero** descargar un PDF resumen de la liquidación
**Para** tener un documento oficial de referencia y archivo

**Criterios de aceptación:**
- [ ] Una vez liquidada una rendición, puedo descargar un PDF resumen
- [ ] El PDF incluye: datos del solicitante, datos del viaje (origen, destino, fechas), detalle de gastos por concepto con comprobantes, anticipo recibido (si aplica), total gastado, líquido a pagar/descontar, números de documentos SAP, fecha de visado, firma digital del operador
- [ ] El PDF tiene formato profesional con logo corporativo
- [ ] Puedo descargar el PDF cuantas veces sea necesario

**ID Requerimientos relacionados:** RF-LIQ-007, RF-LIQ-008

#### **HU-032: Consultar histórico de liquidaciones**
**Como** empleado, operador o auditor
**Quiero** consultar el histórico completo de liquidaciones procesadas
**Para** hacer seguimiento, análisis o auditorías

**Criterios de aceptación:**
- [ ] Puedo visualizar todas las liquidaciones procesadas (según mis permisos: mis liquidaciones como empleado, todas como operador/auditor)
- [ ] Puedo filtrar por fecha, estado, empleado, centro de costo
- [ ] Puedo acceder al detalle completo de cada liquidación
- [ ] Puedo exportar el listado a Excel
- [ ] Como auditor, tengo acceso de solo lectura a todas las liquidaciones

**ID Requerimientos relacionados:** RF-LIQ-009

#### **HU-033: Reversar liquidación en casos excepcionales**
**Como** administrador o supervisor de contabilidad
**Quiero** reversar una liquidación ya visada en casos excepcionales
**Para** corregir errores críticos detectados después del visado

**Criterios de aceptación:**
- [ ] Solo usuarios con permisos especiales (administrador, supervisor) pueden reversar liquidaciones
- [ ] Puedo seleccionar una liquidación en estado "Liquidada y Visada" o "Pagada"
- [ ] Debo ingresar obligatoriamente el motivo detallado de la reversión
- [ ] El sistema me solicita confirmación adicional (doble confirmación)
- [ ] Al confirmar, el sistema genera automáticamente documentos de reversión en SAP
- [ ] El estado de la liquidación cambia a "Reversada - Pendiente de Corrección"
- [ ] Si la liquidación ya fue pagada, el sistema alerta que debe gestionarse la devolución del pago
- [ ] Toda la operación queda registrada en el log de auditoría

**ID Requerimientos relacionados:** RF-LIQ-010

### 5.8 Módulo: Reportes y Dashboards

#### **HU-034: Visualizar dashboard de indicadores de gestión**
**Como** gerente o aprobador de nivel 2
**Quiero** visualizar un dashboard con indicadores clave de gestión de gastos de viaje
**Para** monitorear el comportamiento de los gastos y tomar decisiones estratégicas

**Criterios de aceptación:**
- [ ] El dashboard muestra indicadores clave: total de solicitudes del mes, total de gastos autorizados, promedio de días en aprobación, distribución de solicitudes por estado (gráfico de torta), top 10 destinos más visitados, top 10 solicitantes con mayor gasto total
- [ ] Puedo seleccionar un rango de fechas para filtrar los indicadores
- [ ] Puedo filtrar por centro de costo o área
- [ ] Los gráficos son interactivos (puedo hacer clic para ver detalle)
- [ ] El dashboard se actualiza automáticamente con datos en tiempo real

**ID Requerimientos relacionados:** RF-REP-001

#### **HU-035: Generar reporte de solicitudes por período**
**Como** auditor u operador
**Quiero** generar un reporte Excel con todas las solicitudes en un rango de fechas
**Para** análisis detallado fuera del sistema

**Criterios de aceptación:**
- [ ] Puedo seleccionar fecha de inicio y fecha de fin
- [ ] Puedo filtrar adicionalmente por estado, centro de costo o solicitante
- [ ] El sistema genera un archivo Excel con columnas: solicitante, destino, fecha viaje, monto estimado, monto real, estado, aprobador nivel 1, aprobador nivel 2, fechas de aprobación, fecha de liquidación
- [ ] Puedo descargar el archivo Excel generado
- [ ] El reporte incluye totales al final

**ID Requerimientos relacionados:** RF-REP-002, RF-REP-008

#### **HU-036: Generar reporte de gastos por centro de costo**
**Como** gerente o controlador financiero
**Quiero** generar un reporte consolidado de gastos por centro de costo y concepto
**Para** analizar la distribución de gastos de viaje por área y concepto

**Criterios de aceptación:**
- [ ] Puedo seleccionar uno o múltiples centros de costo
- [ ] Puedo seleccionar el período (mes/año)
- [ ] El reporte muestra gastos agrupados por centro de costo y subagrupados por concepto (alojamiento, alimentación, transporte, otros)
- [ ] Incluye totales por centro de costo y totales generales
- [ ] Incluye comparativo con el año anterior (mismo período)
- [ ] Puedo exportar a Excel

**ID Requerimientos relacionados:** RF-REP-003, RF-REP-008

#### **HU-037: Generar reporte de liquidaciones pendientes**
**Como** operador o supervisor de contabilidad
**Quiero** generar un reporte de rendiciones pendientes de liquidación con más de X días
**Para** identificar cuellos de botella y priorizar procesamiento

**Criterios de aceptación:**
- [ ] Puedo configurar el número de días de antigüedad (ej. más de 7 días)
- [ ] El reporte lista todas las rendiciones pendientes que excedan ese plazo
- [ ] Incluye: solicitante, destino, fecha de viaje, fecha de envío a liquidación, días pendientes, monto total
- [ ] Los registros se ordenan por antigüedad (más antiguos primero)
- [ ] El sistema alerta visualmente los casos más críticos (ej. más de 15 días en rojo)
- [ ] Puedo exportar a Excel

**ID Requerimientos relacionados:** RF-REP-004

#### **HU-038: Monitorear documentos en proceso en tiempo real**
**Como** operador o supervisor
**Quiero** visualizar un monitor en tiempo real de documentos en cada etapa del proceso
**Para** identificar rápidamente dónde hay retrasos o acumulación

**Criterios de aceptación:**
- [ ] El sistema muestra una pantalla tipo "tablero" con columnas por etapa: Solicitud → Aprobación → Cotización → Rendición → Liquidación → Pago
- [ ] En cada columna veo la cantidad de documentos en esa etapa
- [ ] Uso códigos de colores según antigüedad: verde (reciente), amarillo (moderado), rojo (crítico)
- [ ] Puedo hacer clic en cada columna para ver el listado de documentos en esa etapa
- [ ] El tablero se actualiza automáticamente cada X minutos (configurable)

**ID Requerimientos relacionados:** RF-REP-010

### 5.9 Módulo: Administración y Configuración

#### **HU-039: Gestionar usuarios del sistema**
**Como** administrador del sistema
**Quiero** crear, modificar y desactivar usuarios
**Para** controlar el acceso al sistema según altas, bajas y cambios en el personal

**Criterios de aceptación:**
- [ ] Puedo crear un usuario nuevo ingresando: nombre completo, correo electrónico, número de documento, centro de costo, área, cargo, usuario de acceso, contraseña inicial
- [ ] Puedo asignar uno o más roles al usuario (Empleado, Asistente, Aprobador Nivel 1, Aprobador Nivel 2, Operador Liquidación, Auditor, Administrador)
- [ ] Puedo editar datos de usuarios existentes
- [ ] Puedo desactivar usuarios (no eliminar, para mantener trazabilidad histórica)
- [ ] Los usuarios desactivados no pueden acceder al sistema
- [ ] Puedo reactivar usuarios previamente desactivados
- [ ] El sistema registra todas las operaciones en el log de auditoría

**ID Requerimientos relacionados:** RF-ADM-001, RF-ADM-002

#### **HU-040: Configurar flujos de aprobación por centro de costo**
**Como** administrador del sistema
**Quiero** configurar quiénes son los aprobadores Nivel 1 y Nivel 2 para cada centro de costo
**Para** asegurar que las solicitudes se enruten automáticamente a los aprobadores correctos

**Criterios de aceptación:**
- [ ] Puedo seleccionar un centro de costo
- [ ] Puedo asignar uno o múltiples usuarios como Aprobadores Nivel 1 para ese centro de costo
- [ ] Puedo asignar uno o múltiples usuarios como Aprobadores Nivel 2
- [ ] Puedo definir si la aprobación es en serie (secuencial) o en paralelo (cualquiera puede aprobar)
- [ ] Puedo modificar estas configuraciones en cualquier momento
- [ ] Los cambios aplican solo para solicitudes nuevas (no afectan solicitudes en proceso)

**ID Requerimientos relacionados:** RF-ADM-003

#### **HU-041: Mantener catálogos maestros del sistema**
**Como** administrador del sistema
**Quiero** mantener los catálogos maestros (monedas, tipos de gasto, aerolíneas, centros de costo, cuentas SAP, etc.)
**Para** que el sistema cuente con información actualizada y correcta

**Criterios de aceptación:**
- [ ] Puedo acceder a un módulo de administración de maestros con las siguientes opciones: Monedas (código ISO, símbolo, tipo de cambio), Tipos de Gasto (conceptos con cuenta contable SAP asociada), Límites de Gastos (máximos por concepto), Aerolíneas (código IATA, nombre), Empresas de Transporte Terrestre (RUC, razón social, tipo), Centros de Costo (código SAP, descripción, área, responsable), Cuentas Contables SAP (código, descripción, tipo)
- [ ] Para cada catálogo puedo: agregar nuevos registros, editar registros existentes, desactivar registros (no eliminar), buscar y filtrar registros
- [ ] Todos los cambios quedan registrados en auditoría

**ID Requerimientos relacionados:** RF-ADM-004, RF-ADM-005, RF-ADM-006, RF-ADM-007, RF-ADM-008, RF-ADM-009, RF-ADM-010

#### **HU-042: Configurar parámetros globales del sistema**
**Como** administrador del sistema
**Quiero** configurar parámetros globales que afectan el comportamiento del sistema
**Para** adaptar el sistema a las políticas corporativas y necesidades operativas

**Criterios de aceptación:**
- [ ] Puedo configurar: días de recordatorio para aprobaciones pendientes (ej. 2 días), días de antigüedad para alertas de rendición pendiente (ej. 7 días), tamaño máximo de archivos adjuntos (ej. 5 MB), formato de archivos bancarios por banco (BCP, Scotiabank), tasa de IGV (ej. 18%)
- [ ] Cada parámetro tiene una descripción clara de su propósito
- [ ] Puedo modificar los valores y guardar los cambios
- [ ] Los cambios aplican inmediatamente en todo el sistema
- [ ] El sistema valida que los valores ingresados sean coherentes (ej. porcentajes entre 0-100, días mayor a 0)

**ID Requerimientos relacionados:** RF-ADM-011

#### **HU-043: Gestionar cuentas bancarias de empleados**
**Como** empleado o administrador
**Quiero** registrar y mantener actualizadas mis cuentas bancarias personales
**Para** que los reembolsos se depositen correctamente

**Criterios de aceptación:**
- [ ] Como empleado, puedo acceder a "Mis Cuentas Bancarias" y agregar una o más cuentas
- [ ] Para cada cuenta ingreso: banco, número de cuenta, tipo de cuenta (ahorros/corriente), moneda (Soles/Dólares)
- [ ] Puedo marcar una cuenta como "preferida" (por defecto para reembolsos)
- [ ] Puedo desactivar cuentas que ya no uso
- [ ] El administrador puede ver y editar cuentas de cualquier empleado
- [ ] Al generar archivos bancarios, el sistema usa la cuenta activa preferida o permite seleccionar

**ID Requerimientos relacionados:** RF-ADM-013, RF-BAN-003, RF-BAN-004

#### **HU-044: Consultar log de auditoría del sistema**
**Como** administrador o auditor
**Quiero** consultar el log de auditoría con todas las acciones críticas realizadas por usuarios
**Para** realizar auditorías de seguridad y rastrear operaciones

**Criterios de aceptación:**
- [ ] Puedo acceder al módulo de auditoría
- [ ] El log registra: login de usuarios, creación/modificación de solicitudes, aprobaciones/rechazos, liquidaciones, modificación de configuraciones, desactivación de usuarios, reversiones, cada registro incluye: fecha/hora, usuario, acción realizada, IP de origen, datos modificados (antes/después si aplica)
- [ ] Puedo filtrar por rango de fechas, usuario, tipo de acción
- [ ] Puedo buscar por texto libre (ej. número de solicitud)
- [ ] Puedo exportar el log a Excel
- [ ] El log es de solo lectura (no se puede editar ni eliminar registros)

**ID Requerimientos relacionados:** RF-ADM-012
