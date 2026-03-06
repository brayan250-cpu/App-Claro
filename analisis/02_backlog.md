# BACKLOG DE IMPLEMENTACIÓN - Sistema de Gestión de Viajes CLARO

**Proyecto:** CRM Comercial - Gestión de Viajes y Gastos Corporativos  
**Cliente:** América Móvil Perú S.A.C. (CLARO)  
**Fecha:** 3 de Marzo de 2026  
**Versión:** 1.0 - Prototipo

---

## 1. ESTRATEGIA DE IMPLEMENTACIÓN

### 1.1 Enfoque Incremental

El prototipo se desarrollará en **6 FASES INCREMENTALES**, donde cada fase entrega valor funcional y se puede demo

strar de forma independiente.

**Principios:**
- ✅ Entregar funcionalidad completa por módulo
- ✅ Priorizar flujos críticos (happy path)
- ✅ Validar con stakeholders al final de cada fase
- ✅ Iterar basado en feedback

### 1.2 Definición de Tareas

Cada tarea incluye:
- **ID**: Identificador único
- **Historia de Usuario**: Referencia a HU del análisis funcional
- **Descripción**: Qué se implementa
- **Estimación**: Story points (escala Fibonacci: 1, 2, 3, 5, 8, 13)
- **Prioridad**: Alta / Media / Baja
- **Criterios de Aceptación**: Validación técnica

### 1.3 Estimaciones Totales

| Fase | Story Points | Días Estimados | Prioridad |
|------|-------------|----------------|-----------|
| FASE 0: Setup | 21 | 3-4 días | 🔴 Critical |
| FASE 1: Autenticación y Layout | 34 | 5-6 días | 🔴 Critical |
| FASE 2: Módulo Solicitudes | 55 | 8-10 días | 🔴 Critical |
| FASE 3: Módulo Aprobaciones | 34 | 5-6 días | 🟠 High |
| FASE 4: Cotizaciones y Pasajes | 42 | 6-7 días | 🟠 High |
| FASE 5: Rendiciones y Liquidación | 55 | 8-10 días | 🟠 High |
| FASE 6: Reportes y Admin | 34 | 5-6 días | 🟡 Medium |
| **TOTAL** | **275 SP** | **40-49 días** | - |

---

## 2. FASE 0: SETUP E INFRAESTRUCTURA

**Objetivo:** Configurar proyecto Angular y estructura base  
**Duración estimada:** 3-4 días  
**Story Points:** 21  
**Prioridad:** 🔴 Critical

### Tareas

| ID | Descripción | Estimación | Prioridad |
|----|-------------|------------|-----------|
| **F0-T001** | Crear proyecto Angular 17+ con CLI | 2 | Alta |
| **F0-T002** | Configurar Angular Material 3 con tema CLARO | 3 | Alta |
| **F0-T003** | Configurar ESLint + Prettier | 1 | Media |
| **F0-T004** | Crear estructura de carpetas (core, shared, features, layout) | 2 | Alta |
| **F0-T005** | Implementar StorageService (LocalStorage wrapper) | 3 | Alta |
| **F0-T006** | Crear modelos TypeScript (interfaces.ts) | 5 | Alta |
| **F0-T007** | Setup routing principal (app.routes.ts) | 2 | Alta |
| **F0-T008** | Generar datos mock JSON (usuarios, catálogos) | 3 | Media |

**Criterios de Aceptación Fase 0:**
- [x] Proyecto Angular 17+ creado y ejecutándose en `localhost:4200`
- [x] Material 3 configurado con paleta CLARO (rojo #e30613)
- [x] Estructura de carpetas según diseño técnico
- [x] Modelos de datos implementados
- [x] StorageService funcional con persistencia
- [x] Datos mock cargados en `/assets/mocks/`

---

## 3. FASE 1: AUTENTICACIÓN Y LAYOUT

**Objetivo:** Implementar shell de aplicación y autenticación mock  
**Duración estimada:** 5-6 días  
**Story Points:** 34  
**Prioridad:** 🔴 Critical

### Historias de Usuario Cubiertas

- **Infraestructura:** Login, Launchpad, Shell, Notificaciones

### Tareas

| ID | Descripción | HU | Estimación | Prioridad |
|----|-------------|----|------------|-----------|
| **F1-T001** | Implementar AuthService (mock login/logout) | - | 5 | Alta |
| **F1-T002** | Crear AuthStore con Signals | - | 3 | Alta |
| **F1-T003** | Implementar authGuard y roleGuard | - | 5 | Alta |
| **F1-T004** | Pantalla de Login (P-GEN-001) | - | 5 | Alta |
| **F1-T005** | MainLayoutComponent con header + sidebar | - | 8 | Alta |
| **F1-T006** | HeaderComponent (búsqueda, notificaciones, perfil) | - | 5 | Alta |
| **F1-T007** | SidebarComponent (menú navegación multinivel) | - | 5 | Media |
| **F1-T008** | ToastService (MatSnackBar wrapper) | - | 2 | Media |
| **F1-T009** | ConfirmDialogComponent reutilizable | - | 3 | Media |

**Criterios de Aceptación Fase 1:**
- [x] Usuario puede hacer login con credenciales mock
- [x] Session persiste en LocalStorage
- [x] Header muestra usuario logueado, notificaciones y menú perfil
- [x] Sidebar muestra opciones según rol del usuario
- [x] Guards protegen rutas por autenticación y rol
- [x] Notificaciones toast funcionan correctamente
- [x] Dialog de confirmación reutilizable

**Pantallas Implementadas:**
- P-GEN-001: Login
- P-GEN-002: Launchpad (dashboard básico)
- P-GEN-003: Shell/Container
- P-GEN-004: Notificaciones (panel)

---

## 4. FASE 2: MÓDULO SOLICITUDES DE VIAJE

**Objetivo:** CRUD completo de solicitudes con workflow de estados  
**Duración estimada:** 8-10 días  
**Story Points:** 55  
**Prioridad:** 🔴 Critical

### Historias de Usuario Cubiertas

- HU-001: Crear solicitud de gastos de viaje
- HU-002: Enviar solicitud a aprobación
- HU-003: Consultar estado de mis solicitudes
- HU-004: Editar o cancelar solicitud en borrador

### Tareas

| ID | Descripción | HU | Estimación | Prioridad |
|----|-------------|----|------------|-----------|
| **F2-T001** | Crear SolicitudService (mock API) | HU-001 | 5 | Alta |
| **F2-T002** | Crear SolicitudStore con Signals | HU-001 | 5 | Alta |
| **F2-T003** | Pantalla: Listado de Solicitudes (P-SOL-002) | HU-003 | 8 | Alta |
| **F2-T004** | Componente: DataTable reutilizable con filtros | HU-003 | 5 | Alta |
| **F2-T005** | Pantalla: Crear Nueva Solicitud (P-SOL-001) | HU-001 | 13 | Alta |
| **F2-T006** | Componente: Formulario datos básicos viaje | HU-001 | 5 | Alta |
| **F2-T007** | Componente: PresupuestoTableComponent (desglose) | HU-001 | 5 | Media |
| **F2-T008** | Componente: PasajeInfoFormComponent (aéreo/terrestre) | HU-001 | 5 | Media |
| **F2-T009** | Implementar validaciones formulario | HU-001 | 3 | Alta |
| **F2-T010** | Pantalla: Detalle Solicitud (P-SOL-003) | HU-003 | 8 | Alta |
| **F2-T011** | Componente: StatusChipComponent (estados) | HU-003 | 2 | Media |
| **F2-T012** | Componente: Historial de Estados (timeline) | HU-003 | 5 | Media |
| **F2-T013** | Acción: Enviar a Aprobación (validaciones) | HU-002 | 3 | Alta |
| **F2-T014** | Acción: Guardar como Borrador | HU-001 | 2 | Alta |
| **F2-T015** | Acción: Cancelar Solicitud (con motivo) | HU-004 | 3 | Media |
| **F2-T016** | Acción: Editar Solicitud Borrador | HU-004 | 3 | Media |
| **F2-T017** | Pipe: EstadoSolicitudPipe (traducción estados) | - | 1 | Baja |
| **F2-T018** | Empty State para listado vacío | HU-003 | 2 | Baja |

**Criterios de Aceptación Fase 2:**
- [x] Empleado puede crear solicitud con todos los campos requeridos
- [x] Sistema calcula automáticamente presupuesto total
- [x] Sistema asigna centro de costo según empleado
- [x] Puede guardar borrador sin enviar a aprobación
- [x] Validaciones impiden enviar solicitud incompleta
- [x] Al enviar, estado cambia a "Pendiente Aprobación N1"
- [x] Listado muestra todas las solicitudes del empleado
- [x] Puede filtrar por estado
- [x] Detalle muestra info completa y historial de estados
- [x] Puede cancelar solicitud en borrador o pendiente
- [x] Puede editar solicitud en borrador

**Pantallas Implementadas:**
- P-SOL-001: Formulario Solicitud
- P-SOL-002: Listado Mis Solicitudes
- P-SOL-003: Detalle Solicitud
- P-SOL-004: Historial Estados
- P-SOL-005: Formulario Pasaje Terrestre

---

## 5. FASE 3: MÓDULO APROBACIONES

**Objetivo:** Gestión de aprobaciones multinivel con delegación  
**Duración estimada:** 5-6 días  
**Story Points:** 34  
**Prioridad:** 🟠 High

### Historias de Usuario Cubiertas

- HU-005: Visualizar solicitudes pendientes de aprobación
- HU-006: Aprobar o rechazar solicitudes (Nivel 1)
- HU-007: Aprobar o rechazar solicitudes (Nivel 2)
- HU-008: Delegar aprobaciones temporalmente
- HU-009: Recibir recordatorios de aprobaciones pendientes

### Tareas

| ID | Descripción | HU | Estimación | Prioridad |
|----|-------------|----|------------|-----------|
| **F3-T001** | Crear AprobacionService (mock API) | HU-005 | 3 | Alta |
| **F3-T002** | Crear AprobacionStore con Signals | HU-005 | 3 | Alta |
| **F3-T003** | Pantalla: Bandeja de Aprobaciones (P-APR-001) | HU-005 | 8 | Alta |
| **F3-T004** | Componente: AprobacionCardComponent | HU-005 | 5 | Alta |
| **F3-T005** | Pantalla: Detalle para Aprobar (P-APR-002) | HU-006,007 | 5 | Alta |
| **F3-T006** | Componente: Historial Aprobaciones Previas | HU-007 | 3 | Media |
| **F3-T007** | Dialog: Aprobar Solicitud (P-APR-004) | HU-006,007 | 3 | Alta |
| **F3-T008** | Dialog: Rechazar Solicitud con motivo (P-APR-003) | HU-006,007 | 3 | Alta |
| **F3-T009** | Pantalla: Delegación de Aprobaciones (P-APR-005) | HU-008 | 5 | Media |
| **F3-T010** | Lógica: Workflow aprobación 2 niveles | HU-006,007 | 5 | Alta |
| **F3-T011** | Mock EmailService (notificaciones) | HU-002,009 | 2 | Media |
| **F3-T012** | Indicador visual solicitudes +48h pendientes | HU-009 | 2 | Baja |

**Criterios de Aceptación Fase 3:**
- [x] Aprobador ve bandeja de solicitudes pendientes según su nivel
- [x] Puede filtrar y ordenar por antigüedad, solicitante, monto
- [x] Alertas visuales para solicitudes con +48h pendientes
- [x] Detalle muestra toda la info de la solicitud
- [x] Puede aprobar con un clic (confirmación)
- [x] Puede rechazar ingresando motivo obligatorio
- [x] Al aprobar N1 → solicitud pasa a N2
- [x] Al aprobar N2 → solicitud queda APROBADA
- [x] Al rechazar (cualquier nivel) → solicitud RECHAZADA
- [x] Puede delegar aprobaciones especificando fechas
- [x] Mock de email se dispara en aprobación/rechazo

**Pantallas Implementadas:**
- P-APR-001: Bandeja Aprobaciones
- P-APR-002: Detalle Solicitud para Aprobar
- P-APR-003: Modal Rechazo
- P-APR-004: Modal Aprobación
- P-APR-005: Delegación
- P-APR-006: Centro de Notificaciones

---

## 6. FASE 4: COTIZACIONES Y PASAJES

**Objetivo:** Gestión de cotización, carga y selección de pasajes  
**Duración estimada:** 6-7 días  
**Story Points:** 42  
**Prioridad:** 🟠 High

### Historias de Usuario Cubiertas

- HU-010: Ver solicitudes aprobadas pendientes de cotización
- HU-011: Cargar opciones de pasajes mediante Excel
- HU-012: Validar plantilla Excel de pasajes
- HU-013: Registrar pasajes manualmente
- HU-014: Notificar al solicitante opciones disponibles
- HU-015: Seleccionar pasaje preferido
- HU-016: Registrar comprobante de compra

### Tareas

| ID | Descripción | HU | Estimación | Prioridad |
|----|-------------|----|------------|-----------|
| **F4-T001** | Crear CotizacionService (mock API) | HU-010 | 3 | Alta |
| **F4-T002** | Crear CotizacionStore con Signals | HU-010 | 3 | Alta |
| **F4-T003** | Pantalla: Solicitudes Pendientes Cotización (P-COT-001) | HU-010 | 5 | Alta |
| **F4-T004** | Pantalla: Cargar Pasajes (P-COT-002) | HU-011 | 8 | Alta |
| **F4-T005** | Componente: FileUploadComponent (Excel) | HU-011 | 5 | Alta |
| **F4-T006** | ExcelService: Parsear plantilla pasajes | HU-012 | 8 | Alta |
| **F4-T007** | Validaciones: Formato, datos obligatorios, fechas | HU-012 | 5 | Alta |
| **F4-T008** | Pantalla: Registro Manual Pasaje (P-COT-003) | HU-013 | 5 | Media |
| **F4-T009** | Pantalla: Visualizar Opciones (Solicitante) (P-COT-004) | HU-015 | 5 | Alta |
| **F4-T010** | Componente: PasajeTableComponent (comparación) | HU-015 | 3 | Media |
| **F4-T011** | Acción: Seleccionar Opción Pasaje | HU-015 | 2 | Alta |
| **F4-T012** | Pantalla: Registrar Comprobante Compra (P-COT-005) | HU-016 | 5 | Alta |
| **F4-T013** | Mock: Notificación email opciones disponibles | HU-014 | 1 | Baja |
| **F4-T014** | Pantalla: Pasajes Terrestres (P-COT-006) | HU-013 | 3 | Media |

**Criterios de Aceptación Fase 4:**
- [x] Asistente ve solicitudes aprobadas pendientes cotización
- [x] Puede cargar Excel con múltiples opciones de pasajes
- [x] Sistema valida formato y datos del Excel
- [x] Muestra errores de validación claramente
- [x] Puede registrar pasajes de forma manual (alternativa)
- [x] Solicitante recibe notificación mock de opciones disponibles
- [x] Solicitante puede ver y comparar opciones
- [x] Puede seleccionar un pasaje
- [x] Asistente puede registrar comprobante de compra
- [x] Soporta pasajes aéreos y terrestres

**Pantallas Implementadas:**
- P-COT-001: Listado Solicitudes Pendientes Cotización
- P-COT-002: Cargar Pasajes via Excel
- P-COT-003: Registro Manual Pasaje Aéreo
- P-COT-004: Selección de Pasaje (Empleado)
- P-COT-005: Registro Comprobante Compra
- P-COT-006: Pasajes Terrestres

---

## 7. FASE 5: RENDICIONES Y LIQUIDACIÓN

**Objetivo:** Registro de rendiciones y proceso de liquidación SAP  
**Duración estimada:** 8-10 días  
**Story Points:** 55  
**Prioridad:** 🟠 High

### Historias de Usuario Cubiertas

#### Rendiciones (HU-017 a HU-021)
- HU-017: Iniciar rendición de gastos
- HU-018: Registrar comprobantes de gasto
- HU-019: Adjuntar documentos sustentatorios
- HU-020: Validar límites de gastos y justificar excesos
- HU-021: Enviar rendición a liquidación

#### Liquidación (HU-028 a HU-033)
- HU-028: Visualizar rendiciones pendientes de liquidación
- HU-029: Revisar comprobantes y adjuntos
- HU-030: Solicitar correcciones al empleado
- HU-031: Ejecutar proceso de visado
- HU-032: Generar archivo bancario para pagos
- HU-033: Confirmar ejecución de remesa

### Tareas

| ID | Descripción | HU | Estimación | Prioridad |
|----|-------------|----|------------|-----------|
| **F5-T001** | Crear RendicionService (mock API) | HU-017 | 3 | Alta |
| **F5-T002** | Crear RendicionStore con Signals | HU-017 | 3 | Alta |
| **F5-T003** | Pantalla: Mis Rendiciones (P-REN-001) | HU-017 | 5 | Alta |
| **F5-T004** | Pantalla: Crear Rendición (P-REN-002) | HU-018 | 8 | Alta |
| **F5-T005** | Componente: ComprobanteFormComponent | HU-018 | 5 | Alta |
| **F5-T006** | Componente: FileUploadComponent (PDF/IMG) | HU-019 | 3 | Alta |
| **F5-T007** | Cálculo automático IGV (18%) | HU-018 | 2 | Alta |
| **F5-T008** | Validación límites por concepto | HU-020 | 3 | Alta |
| **F5-T009** | Campo justificación exceso (condicional) | HU-020 | 2 | Media |
| **F5-T010** | Componente: ResumenGastosComponent | HU-021 | 3 | Media |
| **F5-T011** | Cálculo diferencia vs anticipo | HU-021 | 2 | Alta |
| **F5-T012** | Acción: Enviar a Liquidación | HU-021 | 2 | Alta |
| **F5-T013** | Crear LiquidacionService (mock API) | HU-028 | 3 | Alta |
| **F5-T014** | Crear LiquidacionStore con Signals | HU-028 | 3 | Alta |
| **F5-T015** | Pantalla: Rendiciones Pendientes Liquidación (P-LIQ-001) | HU-028 | 5 | Alta |
| **F5-T016** | Pantalla: Revisar Rendición (P-LIQ-002) | HU-029 | 5 | Alta |
| **F5-T017** | Acción: Solicitar Corrección (con observaciones) | HU-030 | 3 | Media |
| **F5-T018** | Pantalla: Proceso de Visado (P-LIQ-003) | HU-031 | 8 | Alta |
| **F5-T019** | SAPSimulatorService (mock contabilización) | HU-031 | 8 | Alta |
| **F5-T020** | Generación documentos SAP mock | HU-031 | 5 | Alta |
| **F5-T021** | Pantalla: Archivo Bancario (P-ARB-001) | HU-032 | 5 | Alta |
| **F5-T022** | BankSimulatorService (formato SCT) | HU-032 | 5 | Alta |
| **F5-T023** | Generación archivo TXT BCP/Scotiabank | HU-032 | 5 | Alta |
| **F5-T024** | Download archivo bancario | HU-032 | 2 | Media |
| **F5-T025** | Acción: Confirmar Remesa Ejecutada | HU-033 | 2 | Baja |

**Criterios de Aceptación Fase 5:**

**Rendiciones:**
- [x] Empleado puede iniciar rendición de solicitud aprobada
- [x] Puede registrar múltiples comprobantes (facturas/boletas)
- [x] Sistema calcula IGV automáticamente para facturas
- [x] Puede adjuntar PDF/imagen de cada comprobante
- [x] Sistema valida límites configurados por concepto
- [x] Si excede límite, solicita justificación obligatoria
- [x] Calcula total gastado automáticamente
- [x] Calcula diferencia vs anticipo (si aplica)
- [x] Puede enviar rendición completa a liquidación

**Liquidación:**
- [x] Operador ve rendiciones pendientes de revisar
- [x] Puede acceder a todos los comprobantes y adjuntos
- [x] Puede solicitar corrección con observaciones
- [x] Empleado recibe notificación y puede corregir
- [x] Ejecuta visado que genera docs SAP mock
- [x] Muestra números de documentos SAP generados
- [x] Puede seleccionar múltiples liquidaciones para archivo bancario
- [x] Genera archivo SCT en formato BCP o Scotiabank
- [x] Puede descargar archivo TXT generado
- [x] Puede confirmar que remesa fue ejecutada

**Pantallas Implementadas:**
- P-REN-001: Listado Mis Rendiciones
- P-REN-002: Crear/Editar Rendición
- P-REN-003: Detalle Rendición
- P-REN-004: Resumen Gastos
- P-LIQ-001: Rendiciones Pendientes Liquidación
- P-LIQ-002: Revisar Rendición (Detalle)
- P-LIQ-003: Proceso Visado
- P-LIQ-004: Resumen Liquidación
- P-ARB-001: Generar Archivo Bancario
- P-ARB-002: Histórico Remesas

---

## 8. FASE 6: REPORTES Y ADMINISTRACIÓN

**Objetivo:** Dashboard, reportes y gestión de datos maestros  
**Duración estimada:** 5-6 días  
**Story Points:** 34  
**Prioridad:** 🟡 Medium

### Historias de Usuario Cubiertas

#### Reportes (HU-034 a HU-038)
- HU-034: Dashboard con indicadores de gestión
- HU-035: Generar reporte de solicitudes por período
- HU-036: Reporte de gastos por centro de costo
- HU-037: Exportar reportes a Excel
- HU-038: Monitor de documentos en proceso

#### Administración (HU-039 a HU-044)
- HU-039: Gestión de usuarios
- HU-040: Asignar roles y permisos
- HU-041: Mantener catálogos maestros
- HU-042: Configurar flujos de aprobación
- HU-043: Gestión de cuentas bancarias
- HU-044: Auditar acciones de usuarios

### Tareas

| ID | Descripción | HU | Estimación | Prioridad |
|----|-------------|----|------------|-----------|
| **F6-T001** | Pantalla: Dashboard Principal (P-GEN-002) | HU-034 | 8 | Alta |
| **F6-T002** | Componente: DashboardCardComponent | HU-034 | 3 | Media |
| **F6-T003** | Componente: QuickStatsComponent (métricas) | HU-034 | 5 | Media |
| **F6-T004** | Pantalla: Reportes (P-REP-001) | HU-035,036 | 5 | Media |
| **F6-T005** | Componente: DateRangePickerComponent | HU-035 | 3 | Media |
| **F6-T006** | ExcelService: Exportar reportes | HU-037 | 5 | Media |
| **F6-T007** | Pantalla: Monitor Documentos (P-REP-003) | HU-038 | 5 | Baja |
| **F6-T008** | Pantalla: Gestión Usuarios (P-ADM-001) | HU-039 | 5 | Alta |
| **F6-T009** | CRUD usuarios completo | HU-039,040 | 5 | Alta |
| **F6-T010** | Pantalla: Gestión Roles (P-ADM-002) | HU-040 | 3 | Media |
| **F6-T011** | Pantalla: Gestión Catálogos (P-ADM-003) | HU-041 | 5 | Media |
| **F6-T012** | Pantalla: Configuración Flujos (P-ADM-004) | HU-042 | 5 | Media |
| **F6-T013** | Pantalla: Cuentas Bancarias (P-ADM-005) | HU-043 | 3 | Media |
| **F6-T014** | Pantalla: Log de Auditoría (P-ADM-006) | HU-044 | 2 | Baja |

**Criterios de Aceptación Fase 6:**

**Reportes:**
- [x] Dashboard muestra métricas clave: total solicitudes, gastos, promedios
- [x] Gráficos visuales (torta, barras) para distribución
- [x] Puede generar reporte de solicitudes con filtros
- [x] Puede generar reporte de gastos por centro de costo
- [x] Todos los reportes se pueden exportar a Excel
- [x] Monitor muestra documentos en cada etapa con colores

**Administración:**
- [x] Admin puede crear/editar/desactivar usuarios
- [x] Puede asignar múltiples roles a un usuario
- [x] Puede configurar aprobadores por centro de costo
- [x] Puede mantener catálogos maestros (CRUD básico)
- [x] Empleado puede gestionar sus propias cuentas bancarias
- [x] Log de auditoría registra acciones críticas

**Pantallas Implementadas:**
- P-GEN-002: Dashboard (actualizado con métricas)
- P-REP-001: Listado Reportes
- P-REP-002: Generador Reportes
- P-REP-003: Monitor de Documentos
- P-ADM-001: Gestión Usuarios
- P-ADM-002: Gestión Roles
- P-ADM-003: Gestión Catálogos
- P-ADM-004: Configuración Flujos
- P-ADM-005: Cuentas Bancarias
- P-ADM-006: Log Auditoría

---

## 9. DEPENDENCIAS Y BLOQUEANTES

### 9.1 Dependencias entre Fases

```
FASE 0 (Setup)
    ↓
FASE 1 (Autenticación y Layout)
    ↓
    ├─→ FASE 2 (Solicitudes) ──────────┐
    │       ↓                           │
    │   FASE 3 (Aprobaciones)           │
    │       ↓                           │
    │   FASE 4 (Cotizaciones)           │
    │       ↓                           ↓
    │   FASE 5 (Rendiciones + Liquidación)
    │                                   │
    └─→ FASE 6 (Reportes + Admin) ←────┘
```

**Notas:**
- FASE 1 es crítica y bloquea todo lo demás
- FASE 2 debe completarse antes de FASE 3,4,5
- FASE 6 puede desarrollarse en paralelo parcial a partir de FASE 3

### 9.2 Bloqueantes Identificados

| Bloqueante | Impacto | Mitigación |
|------------|---------|------------|
| Falta de definición colores corporativos | FASE 0-1 | Usar paleta provisional Material |
| Plantilla Excel pasajes no disponible | FASE 4 | Crear plantilla mock |
| Especificación formato SCT bancos | FASE 5 | Generar formato simplificado mock |
| Datos SAP reales | FASE 5 | Simulador completo con lógica mock |

---

## 10. CRITERIOS DE FINALIZACIÓN

### 10.1 Definición de "Done"

Una tarea se considera completa cuando:
- ✅ Código implementado y funcional
- ✅ Sin errores de compilación ni linting
- ✅ Commits realizados con mensaje descriptivo
- ✅ Probado manualmente (happy path)
- ✅ Integrado en la rama `develop`
- ✅ Pantallas responsive (desktop/tablet mínimo)

### 10.2 Definición de "Fase Completa"

Una fase se considera completa cuando:
- ✅ Todas las tareas marcadas como Done
- ✅ Todas las HUs de la fase implementadas
- ✅ Criterios de aceptación de fase cumplidos
- ✅ Demo funcional preparada
- ✅ Sin errores críticos ni bloqueantes

### 10.3 Definición de "Prototipo Completo"

El prototipo se considera completo cuando:
- ✅ Las 6 fases finalizadas
- ✅ 64 pantallas implementadas
- ✅ Flujo E2E funcional: Solicitud → Aprobación → Cotización → Rendición → Liquidación
- ✅ Persistencia LocalStorage funcionando
- ✅ Mock de integraciones SAP y bancos operativo
- ✅ Responsive funcional
- ✅ Demo presentable a stakeholders

---

## 11. GESTIÓN DE RIESGOS

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Cambios de alcance mid-proyecto | Alta | Alto | Congelar scope tras aprobación PASO 4 |
| Complejidad Excel parsing FASE 4 | Media | Medio | Librería SheetJS ya probada |
| Performance con muchos datos | Baja | Medio | Virtual scrolling desde FASE 2 |
| Formato SCT bancos incorrecto | Media | Bajo | Es mock, validar lógica no formato real |
| Retrasos en feedback stakeholders | Media | Alto | Demos programadas al final de cada fase |

---

## 12. MÉTRICAS Y SEGUIMIENTO

### 12.1 Burn Down Chart

Actualizar diariamente:
- Story Points completados vs restantes
- Proyección de finalización

### 12.2 KPIs del Proyecto

| Métrica | Objetivo |
|---------|----------|
| **Velocity** | 40-50 SP por semana |
| **Errores críticos** | 0 al final de cada fase |
| **Coverage tests** | >= 70% servicios y stores |
| **Pantallas completas** | 64/64 implementadas |
| **HUs implementadas** | 44/44 completadas |

---

## 13. PRIORIZACIÓN DE HISTORIAS DE USUARIO

### 13.1 Matriz de Priorización (MoSCoW)

#### **MUST HAVE** (Críticas para MVP)
- HU-001 a HU-004: Solicitudes CRUD
- HU-005 a HU-007: Aprobaciones básicas
- HU-017 a HU-021: Rendiciones
- HU-028 a HU-031: Liquidación core

#### **SHOULD HAVE** (Importantes pero no bloqueantes)
- HU-010 a HU-016: Cotizaciones
- HU-032 a HU-033: Archivos bancarios
- HU-034 a HU-036: Reportes básicos

#### **COULD HAVE** (Opcionales value-add)
- HU-008 a HU-009: Delegación y recordatorios
- HU-037 a HU-038: Reportes avanzados
- HU-041 a HU-044: Admin avanzado

#### **WON'T HAVE** (Fuera de scope prototipo)
- Integración real SAP
- Autenticación SSO/LDAP
- Web Speech API
- Tests E2E automatizados completos

---

## 14. PRÓXIMOS PASOS INMEDIATOS

### 14.1 Iniciar FASE 0

**Comando:**
```bash
ng new claro-viajes --standalone --routing --style=scss
cd claro-viajes
ng add @angular/material
```

**Primeras tareas:**
1. **F0-T001**: Crear proyecto Angular 17+
2. **F0-T002**: Configurar Material 3
3. **F0-T004**: Crear estructura de carpetas

**Duración estimada:** 1 día

### 14.2 Checkpoint Fase 0

Validar con stakeholder:
- ✅ Proyecto ejecutándose correctamente
- ✅ Estructura de carpetas aprobada
- ✅ Paleta de colores CLARO visible

---

## ANEXOS

### A. Glosario de Prioridades

- **🔴 Critical**: Bloqueante, debe completarse antes de continuar
- **🟠 High**: Importante para flujo principal
- **🟡 Medium**: Value-add pero no bloqueante
- **🟢 Low**: Nice to have, puede postergarse

### B. Story Points (Fibonacci Scale)

- **1 punto**: Task trivial (< 1 hora)
- **2 puntos**: Task simple (1-2 horas)
- **3 puntos**: Task estándar (2-4 horas)
- **5 puntos**: Task compleja (4-8 horas)
- **8 puntos**: Task muy compleja (1-2 días)
- **13 puntos**: Epic (debe dividirse)

### C. Referencias

- [Análisis Funcional](./Analisis_Funcional_CRM_Viajes_CLARO.md)
- [Diseño Técnico](./01_technical_design.md)
- [Historias de Usuario](./05_historias_usuario.md)
- [Matriz de Trazabilidad](./14_matriz_trazabilidad.md)

---

**Documento generado:** 3 de Marzo de 2026  
**Versión:** 1.0  
**Estado:** Aprobado para ejecución  
**Próximo hito:** Iniciar FASE 0
