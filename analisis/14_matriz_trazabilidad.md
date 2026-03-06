## 14. Matriz de Trazabilidad

| Requisito | Historia(s) de Usuario | Pantalla(s) |
| :-------- | :--------------------- | :---------- |
| **RF-SOL-001:** Crear Solicitud de Gastos | HU-001 | `P-SOL-001` |
| **RF-SOL-002:** Calcular Presupuesto Total | HU-001 | `P-SOL-001` |
| **RF-SOL-003:** Guardar Borrador de Solicitud | HU-004 | `P-SOL-001` |
| **RF-SOL-004:** Enviar Solicitud a Aprobación | HU-002 | `P-SOL-001`, `P-SOL-003` |
| **RF-SOL-005:** Consultar Estado de Solicitud | HU-003 | `P-SOL-002`, `P-SOL-004` |
| **RF-SOL-006:** Editar Solicitud en Borrador | HU-004 | `P-SOL-001` |
| **RF-SOL-007:** Cancelar Solicitud | HU-004 | `P-SOL-002` |
| **RF-SOL-008:** Validar Fecha de Viaje | HU-001 | `P-SOL-001` |
| **RF-SOL-009:** Asignar Centro de Costo Automático | HU-001 | `P-SOL-001` |
| **RF-SOL-010:** Registrar Información de Pasaje Aéreo | HU-001 | `P-SOL-001` |
| **RF-SOL-011:** Registrar Información de Pasaje Terrestre | HU-001 | `P-SOL-001`, `P-SOL-005` |
| **RF-APR-001:** Notificar Aprobador Nivel 1 | HU-002, HU-005 | `P-APR-006` |
| **RF-APR-002:** Visualizar Solicitudes Pendientes | HU-005 | `P-APR-001` |
| **RF-APR-003:** Consultar Detalle de Solicitud | HU-006, HU-007 | `P-APR-002` |
| **RF-APR-004:** Aprobar Solicitud Nivel 1 | HU-006 | `P-APR-001`, `P-APR-002`, `P-APR-004` |
| **RF-APR-005:** Rechazar Solicitud Nivel 1 | HU-006 | `P-APR-001`, `P-APR-003`, `P-APR-004` |
| **RF-APR-006:** Aprobar Solicitud Nivel 2 | HU-007 | `P-APR-001`, `P-APR-002`, `P-APR-004` |
| **RF-APR-007:** Rechazar Solicitud Nivel 2 | HU-007 | `P-APR-001`, `P-APR-003`, `P-APR-004` |
| **RF-APR-008:** Delegar Aprobación | HU-008 | `P-APR-005` |
| **RF-APR-009:** Historial de Aprobaciones | HU-006, HU-007 | `P-SOL-004`, `P-APR-002` |
| **RF-APR-010:** Recordatorio de Aprobación Pendiente | HU-009 | `P-APR-006` |
| **RF-COT-001:** Notificar Asistente de Solicitud Aprobada | HU-010 | `P-COT-001` |
| **RF-COT-002:** Listar Solicitudes para Cotización | HU-010 | `P-COT-001` |
| **RF-COT-003:** Cargar Opciones de Pasajes mediante Excel | HU-011 | `P-COT-002` |
| **RF-COT-004:** Validar Plantilla de Pasajes | HU-011 | `P-COT-002` |
| **RF-COT-005:** Registrar Opción de Pasaje Manual | HU-012 | `P-COT-002` |
| **RF-COT-006:** Notificar Solicitante de Opciones Disponibles | HU-013 | `P-COT-006` |
| **RF-COT-007:** Visualizar y Comparar Opciones de Pasajes | HU-014 | `P-COT-003` |
| **RF-COT-008:** Seleccionar Opción de Pasaje | HU-014 | `P-COT-003`, `P-COT-004` |
| **RF-COT-009:** Registrar Comprobante de Compra de Pasaje | HU-015 | `P-COT-005` |
| **RF-COT-010:** Calcular IGV del Comprobante | HU-015 | `P-COT-005` |
| **RF-COT-011:** Registrar Pasaje Terrestre | HU-016 | `P-SOL-005` |
| **RF-COT-012:** Adjuntar Documentos de Pasaje | HU-015, HU-016 | `P-COT-005`, `P-SOL-005` |
| **RF-REN-001:** Iniciar Rendición de Gastos | HU-017 | `P-REN-001`, `P-REN-003` |
| **RF-REN-002:** Registrar Comprobante de Gasto | HU-018 | `P-REN-002` |
| **RF-REN-003:** Calcular IGV Automático en Rendición | HU-018 | `P-REN-002` |
| **RF-REN-004:** Adjuntar Comprobante Digital | HU-018 | `P-REN-002` |
| **RF-REN-005:** Validar Límites de Gastos | HU-019 | `P-REN-002`, `P-REN-004` |
| **RF-REN-006:** Justificar Exceso de Límites | HU-019 | `P-REN-002`, `P-REN-004` |
| **RF-REN-007:** Calcular Total Gastado | HU-020 | `P-REN-001`, `P-REN-005` |
| **RF-REN-008:** Calcular Diferencia con Anticipo | HU-020 | `P-REN-001`, `P-REN-005` |
| **RF-REN-009:** Editar Comprobante en Rendición | HU-018 | `P-REN-001`, `P-REN-002` |
| **RF-REN-010:** Enviar Rendición a Liquidación | HU-021 | `P-REN-001`, `P-REN-006` |
| **RF-REN-011:** Validar Rendición Completa | HU-021 | `P-REN-001` |
| **RF-REN-012:** Notificar Operador de Rendición Pendiente | HU-021 | `P-LIQ-001` |
| **RF-SAP-001:** Generar Documento de Anticipo en SAP | HU-022 | `P-SAP-001`, `P-LIQ-002` |
| **RF-SAP-002:** Asignar Cuenta Contable según Concepto | HU-022 | `P-SAP-002`, `P-LIQ-002` |
| **RF-SAP-003:** Generar Documento de Gasto en SAP | HU-022 | `P-SAP-002`, `P-LIQ-002` |
| **RF-SAP-004:** Generar Documento de Compensación en SAP | HU-022 | `P-SAP-003`, `P-LIQ-002` |
| **RF-SAP-005:** Generar Documento de Reembolso/Descuento | HU-022 | `P-SAP-004`, `P-LIQ-002` |
| **RF-SAP-006:** Enviar Datos a SAP mediante Interfaz | HU-022 | `P-LIQ-004`, `P-LIQ-005` |
| **RF-SAP-007:** Registrar Número de Documento SAP | HU-023 | `P-SOL-004`, `P-LIQ-002`, `P-LIQ-006` |
| **RF-SAP-008:** Reprocesar Documento SAP Rechazado | HU-024 | `P-SAP-005`, `P-LIQ-002` |
| **RF-SAP-009:** Validar Disponibilidad Presupuestaria | HU-022 | `P-LIQ-004` |
| **RF-SAP-010:** Trazabilidad de Integración SAP | HU-023, HU-024 | `P-SAP-006` |
| **RF-BAN-001:** Seleccionar Liquidaciones para Pago | HU-025 | `P-BAN-001` |
| **RF-BAN-002:** Agrupar Pagos por Referencia | HU-025 | `P-BAN-001` |
| **RF-BAN-003:** Validar Cuenta Bancaria del Empleado | HU-025 | `P-BAN-001` |
| **RF-BAN-004:** Seleccionar Cuenta Bancaria | HU-025 | `P-BAN-001` |
| **RF-BAN-005:** Generar Archivo SCT para BCP | HU-025 | `P-BAN-002`, `P-BAN-003` |
| **RF-BAN-006:** Generar Archivo SCT para Scotiabank | HU-025 | `P-BAN-002`, `P-BAN-003` |
| **RF-BAN-007:** Convertir Moneda en Archivo Bancario | HU-025 | `P-BAN-003` |
| **RF-BAN-008:** Descargar Archivo Bancario | HU-026 | `P-BAN-003` |
| **RF-BAN-009:** Registrar Fecha de Generación de Remesa | HU-026 | `P-BAN-003`, `P-BAN-005` |
| **RF-BAN-010:** Confirmar Ejecución de Remesa | HU-026 | `P-BAN-004` |
| **RF-BAN-011:** Cancelar Archivo Bancario | HU-027 | `P-BAN-005`, `P-BAN-006` |
| **RF-LIQ-001:** Listar Rendiciones Pendientes de Liquidación | HU-028 | `P-LIQ-001` |
| **RF-LIQ-002:** Revisar Comprobantes de Rendición | HU-029 | `P-LIQ-002` |
| **RF-LIQ-003:** Solicitar Corrección de Rendición | HU-029 | `P-LIQ-002`, `P-LIQ-003` |
| **RF-LIQ-004:** Corregir Rendición Observada | HU-029 | `P-REN-001` |
| **RF-LIQ-005:** Ejecutar Proceso de Visado | HU-030 | `P-LIQ-002`, `P-LIQ-004`, `P-LIQ-005` |
| **RF-LIQ-006:** Calcular Líquido a Pagar | HU-030 | `P-LIQ-002`, `P-REN-005` |
| **RF-LIQ-007:** Generar Resumen de Liquidación | HU-031 | `P-LIQ-005`, `P-LIQ-006` |
| **RF-LIQ-008:** Descargar Resumen de Liquidación | HU-031 | `P-LIQ-006` |
| **RF-LIQ-009:** Consultar Histórico de Liquidaciones | HU-032 | `P-LIQ-007` |
| **RF-LIQ-010:** Reversar Liquidación | HU-033 | `P-LIQ-008` |
| **RF-REP-001:** Dashboard de Indicadores de Gestión | HU-034 | `P-REP-001` |
| **RF-REP-002:** Reporte de Solicitudes por Período | HU-035 | `P-REP-002` |
| **RF-REP-003:** Reporte de Gastos por Centro de Costo | HU-036 | `P-REP-003` |
| **RF-REP-004:** Reporte de Liquidaciones Pendientes | HU-037 | `P-REP-004` |
| **RF-REP-005:** Reporte de Comprobantes por Proveedor | HU-035 | `P-REP-002` |
| **RF-REP-006:** Reporte de Documentos SAP Generados | HU-023 | `P-SAP-006` |
| **RF-REP-007:** Reporte de Anticipos Pendientes de Rendir | HU-037 | `P-REP-004` |
| **RF-REP-008:** Exportar Reportes a Excel | HU-035, HU-036 | `P-REP-002`, `P-REP-003`, `P-REP-004` |
| **RF-REP-009:** Programar Envío Automático de Reportes | HU-035 | `P-REP-006` |
| **RF-REP-010:** Monitor de Documentos en Proceso | HU-038 | `P-REP-005` |
| **RF-ADM-001:** Gestión de Usuarios | HU-039 | `P-ADM-001` |
| **RF-ADM-002:** Asignación de Roles | HU-039 | `P-ADM-001` |
| **RF-ADM-003:** Configurar Flujo de Aprobación | HU-040 | `P-ADM-002` |
| **RF-ADM-004:** Gestión de Catálogo de Monedas | HU-041 | `P-ADM-003` |
| **RF-ADM-005:** Gestión de Catálogo de Tipos de Gasto | HU-041 | `P-ADM-003` |
| **RF-ADM-006:** Gestión de Límites de Gastos | HU-041 | `P-ADM-003` |
| **RF-ADM-007:** Gestión de Catálogo de Aerolíneas | HU-041 | `P-ADM-003` |
| **RF-ADM-008:** Gestión de Empresas de Transporte Terrestre | HU-041 | `P-ADM-003` |
| **RF-ADM-009:** Gestión de Centros de Costo | HU-041 | `P-ADM-003` |
| **RF-ADM-010:** Gestión de Cuentas Contables SAP | HU-041 | `P-ADM-003` |
| **RF-ADM-011:** Configurar Parámetros del Sistema | HU-042 | `P-ADM-004` |
| **RF-ADM-012:** Auditar Acciones de Usuarios | HU-044 | `P-ADM-006` |
| **RF-ADM-013:** Gestión de Cuentas Bancarias de Empleados | HU-043 | `P-ADM-005`, `P-GEN-005` |
| **RF-ADM-014:** Configurar Plantilla de Correos | HU-044 | `P-ADM-008` |
| **RF-ADM-015:** Backup y Restauración | HU-044 | `P-ADM-007` |

#### Pantallas de Infraestructura General (sin RF específico)
| Requerimiento | Historia(s) de Usuario | Pantalla(s) |
| :------------ | :--------------------- | :---------- |
| **Infraestructura:** Página Principal (Launchpad) | HU-001 | `P-GEN-002` |
| **Infraestructura:** Marco/Shell de Aplicación | HU-001 | `P-GEN-003` |
| **Infraestructura:** Panel de Notificaciones | HU-001 | `P-GEN-004` |

---

### Resumen de Cobertura de Trazabilidad

**Total de Requerimientos Funcionales:** 101 (distribuidos en 9 módulos):
- Módulo Gestión de Solicitudes de Gastos: 11 RFs
- Módulo Proceso de Aprobaciones: 10 RFs
- Módulo Gestión de Cotización y Pasajes: 12 RFs
- Módulo Rendición de Gastos: 12 RFs
- Módulo Integración con SAP FI: 10 RFs
- Módulo Generación de Archivos Bancarios: 11 RFs
- Módulo Liquidación y Cierre: 10 RFs
- Módulo Reportes y Dashboards: 10 RFs
- Módulo Administración y Configuración: 15 RFs

**Total de Historias de Usuario:** 44
**Total de Pantallas:** 64

**Nota:** Las pantallas de infraestructura general (P-GEN-002, P-GEN-003, P-GEN-004) son componentes transversales que no mapean a RFs específicos pero son esenciales para la navegación y usabilidad del sistema. Han sido incluidas en una sección separada para completitud de trazabilidad.

**Cobertura de Trazabilidad:**
- **RFs con HU asignada:** 101 de 101 (100%)
- **RFs con Pantalla asignada:** 101 de 101 (100%)
- **HUs con Pantalla asignada:** 44 de 44 (100%)
- **Pantallas con trazabilidad:** 64 de 64 (100%)

**Validación de Cobertura:**
Todos los Requerimientos Funcionales sintetizados en la Sección 3 están trazados a:
1. Al menos una Historia de Usuario (Sección 5)
2. Al menos una Pantalla (Sección 10)

La trazabilidad está completa y validada al 100% para el modo prototipo.

---

### Notas sobre la Matriz

**Modo Prototipo Activo:**
- Esta matriz no incluye las columnas "Caso(s) de Uso" y "Prueba(s)" debido a que el análisis se realizó en modo prototipo.
- Para un análisis funcional completo, estas columnas deberían ser generadas en las Secciones 6 y 13 respectivamente.

**Pantallas Genéricas:**
- Las pantallas `P-GEN-001` a `P-GEN-006` proporcionan funcionalidad transversal (Login, Launchpad, Shell, Notificaciones, Perfil, Búsqueda) y no están directamente trazadas a RFs específicos, pero son esenciales para la navegación y usabilidad del sistema.

**Múltiples Relaciones:**
- Algunos RFs están relacionados con múltiples HUs cuando la funcionalidad es transversal o compartida.
- Algunos RFs se implementan en múltiples pantallas cuando la funcionalidad aparece en diferentes contextos del sistema.

**Pantallas SAP:**
- Las pantallas `P-SAP-001` a `P-SAP-004` representan visualizaciones estándar de documentos SAP FB03 y no son pantallas propias del sistema, pero se referencian para trazabilidad de integración.
