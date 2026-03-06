Eres un desarrollador frontend experto. A continuación te detallo los ajustes y mejoras que debes implementar en la aplicación móvil de gestión de viajes. Lee cuidadosamente cada sección antes de comenzar.

MÓDULO 1 — TARJETAS DE SOLICITUDES (CARDS)
1.1 Rediseño visual de las tarjetas

Aplicar negrita a todos los títulos/etiquetas de los campos (ej: "Fecha de creación:", "Presupuesto total:").
Aumentar el interlineado entre etiqueta y valor para mejorar la legibilidad.
Alinear los valores numéricos y de fecha a la derecha de la tarjeta (como datos fijos de longitud conocida).
Usar formato de fecha numérico (ej: 06/03/2025) en lugar de texto (ej: "6 de marzo de 2025") para evitar variaciones de longitud según el mes.

1.2 Datos a mostrar en la tarjeta resumen
Mostrar únicamente estos campos esenciales:

Fecha de creación
Fecha de salida y retorno
Destino
Presupuesto total (importe estimado)
Motivo del viaje

Ocultar los campos: nombre del empleado (ya visible en el header de la app) y centro de costo (dato interno no relevante para el solicitante en la vista móvil).

MÓDULO 2 — DETALLE DE SOLICITUD DE VIAJE
2.1 Desglose de viáticos por concepto
La solicitud de viaje debe mostrar el presupuesto segmentado por los siguientes conceptos (NO mostrar solo "viaje" o "pasajes" como ítem único):
ConceptoDescripciónAlojamientoMonto estimado para hospedajeAlimentaciónMonto estimado para comidasTransporteMonto estimado para movilidadImpuestosCargos aplicablesOtros gastosMonto adicional (requiere justificación)
El sistema debe auto-calcular los montos por concepto en base al monto total ingresado y al tipo/duración del viaje.
2.2 Reglas de justificación en solicitud

Los conceptos Alojamiento, Alimentación, Transporte e Impuestos → NO requieren campo de justificación en la solicitud.
Solo el concepto "Otros gastos" requiere campo de justificación obligatorio, ya que el usuario ingresa ese monto manualmente.
El campo "Motivo del viaje" debe mantenerse (es el motivo general del desplazamiento, no una justificación de gasto).

2.3 Formato de importes

Todos los montos deben mostrarse con separador de miles (coma) y dos decimales.

Ejemplo correcto: 1,400.00
Ejemplo incorrecto: 1400 o 1400.0




MÓDULO 3 — RENDICIONES
3.1 Pantalla principal de rendiciones

Reemplazar la lista dispersa de gastos por tarjetas de solicitudes aprobadas, igual al diseño de las tarjetas de solicitudes.
Cada tarjeta debe mostrar: destino, fechas, monto planificado y monto ya rendido (progreso).
Al hacer clic en una tarjeta, el usuario entra al flujo de rendición de esa solicitud específica.

3.2 Flujo de registro de gastos (rendición)
Implementar el siguiente flujo secuencial al registrar un comprobante:
Paso 1 — Captura del documento

Botón principal: Tomar foto del comprobante.
Botón secundario: Subir archivo (PDF u otros formatos, para comprobantes digitales como constancias de Uber/taxi enviadas al correo).

Paso 2 — Previsualización del comprobante

Mostrar la imagen capturada o el archivo subido para que el usuario confirme que es legible.
Botón: "Confirmar" o "Volver a tomar".

Paso 3 — Campos autocompletados (Document AI)

Mostrar los campos extraídos automáticamente por el servicio de Document AI: fecha, importe, concepto, proveedor, folio, etc.
Mostrar todos los campos extraídos inicialmente; el feedback posterior definirá cuáles ocultar.
Para campos de texto libre (como justificación o descripción), incluir un botón de dictado por voz para facilitar la corrección sin escribir manualmente.
No incluir botón de audio en campos numéricos ni en campos como folio o número de documento.

Paso 4 — Resumen acumulado de viáticos

Debajo del formulario, mostrar un resumen visual de los viáticos rendidos vs. planificados por concepto:

Alojamiento   ████████░░  200 / 400
Alimentación  ████░░░░░░  100 / 250
Transporte    ██░░░░░░░░   50 / 120
Otros         ░░░░░░░░░░    0 / 80

Este resumen se actualiza en tiempo real con cada comprobante guardado.
Al hacer clic en un concepto (ej: "Alimentación"), debe abrirse la lista de comprobantes asociados con opción de descarga/previsualización.

Paso 5 — Confirmar y continuar

Después de guardar un comprobante, mostrar opciones:

"Registrar otro gasto"
"Finalizar rendición"



3.3 Reglas de justificación en rendición

En rendición, todos los conceptos pueden requerir justificación si el monto rendido supera el planificado.
La justificación de exceso de monto aplica de forma global (fuera del comprobante, al momento de enviar la rendición).
La justificación del comprobante individual es para sustentar el gasto puntual.


MÓDULO 4 — APROBACIONES
4.1 Vista del aprobador en detalle de solicitud

El aprobador no debe ver campos de gastos reales ni saldo disponible mientras la solicitud no tenga rendición asociada (mostrar solo presupuesto planificado).
Mostrar: datos de la solicitud, monto total, destino, fechas y motivo.

4.2 Listado de aprobaciones pendientes

Implementar filtros sobre la lista de aprobaciones: por empleado, monto, destino, fecha.
Agregar función de aprobación masiva: seleccionar múltiples solicitudes y aprobarlas en un solo paso.
La asignación de aprobadores debe consumirse desde el servicio existente en el backend (CAC/organigrama), que define niveles de aprobación según tipo de solicitud y destino. No hardcodear reglas.

4.3 Navegación entre solicitudes y rendiciones del aprobador

Evaluar reemplazar el swipe izquierda/derecha para cambiar entre "Solicitudes" y "Rendiciones" por una alternativa más clara: tabs superiores, lista desplegable (combobox) u otro control más explícito.
Proponer al menos una alternativa de navegación y mostrarla para feedback.

4.4 Roles mixtos (usuario que es también aprobador)

Un usuario puede tener simultáneamente el rol de solicitante y aprobador.
En el menú principal, mostrar ambas secciones condicionalmente según los roles asignados al usuario autenticado.
Nota: La implementación definitiva usará mosaicos (tiles) por aplicativo separado. Para el prototipo/mockup, mantener el menú lateral con las secciones diferenciadas por rol.


MÓDULO 5 — REPORTES DEL APROBADOR

El aprobador puede ver métricas de su equipo: viajes por empleado, gastos totales, promedio por viaje.
Evaluar si la presentación actual (tabla) es la más adecuada o proponer una vista alternativa más visual (tarjetas, gráficas simples).
Incluir filtros básicos: por empleado, por período, por monto.


CONSIDERACIONES GENERALES

Formato de fechas: Usar siempre formato numérico DD/MM/YYYY en toda la app.
Formato de importes: Separador de miles con coma, siempre dos decimales. Ej: 1,234.50.
Prioridad de implementación: Solicitudes → Rendiciones → Aprobaciones → Monitor. Las demás funcionalidades (gestión de pasajes, tickets) quedan fuera del alcance actual.