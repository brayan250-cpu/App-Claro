## 11. Diagramas de Navegación

### 11.1. Flujo de Navegación - Empleado/Solicitante

```mermaid
graph TD
    A[P-GEN-002: Launchpad] --> B{Seleccionar acción}
    B -->|Crear solicitud| C[P-SOL-001: Form Solicitud]
    B -->|Ver solicitudes| D[P-SOL-002: Listado Solicitudes]
    B -->|Rendir gastos| E[P-REN-003: Listado Rendiciones]
    
    C -->|Guardar borrador| C
    C -->|Enviar a aprobación| F[P-SOL-003: Confirmación Envío]
    F --> D
    
    D -->|Ver detalle| G[P-SOL-004: Detalle Solicitud]
    D -->|Editar borrador| C
    D -->|Cancelar| D
    G -->|Ver opciones pasajes<br/>si aprobada| H[P-COT-003: Opciones Pasajes]
    
    H -->|Seleccionar pasaje| I[P-COT-004: Confirmación Selección]
    I --> G
    
    G -->|Iniciar rendición<br/>si viaje finalizado| J[P-REN-001: Form Rendición]
    E -->|Crear rendición| J
    E -->|Ver detalle| K[P-LIQ-002: Detalle Rendición]
    
    J -->|Agregar comprobante| L[P-REN-002: Modal Comprobante]
    L -->|Excede límite| M[P-REN-004: Alerta Justificación]
    M --> L
    L --> J
    J -->|Ver resumen| N[P-REN-005: Resumen Rendición]
    J -->|Enviar a liquidación| O[P-REN-006: Confirmación Envío]
    O --> E
    
    K -->|Si observada| J
    K -->|Si liquidada| P[P-LIQ-006: PDF Resumen]
    
    G -->|Consultar histórico| Q[P-LIQ-007: Histórico]
```

### 11.2. Flujo de Navegación - Aprobador (Nivel 1 y Nivel 2)

```mermaid
graph TD
    A[P-GEN-002: Launchpad<br/>Badge pendientes] --> B[P-APR-001: Bandeja Aprobaciones]
    
    B -->|Seleccionar solicitud| C[P-APR-002: Detalle para Aprobación]
    
    C -->|Rechazar| D[P-APR-003: Modal Rechazo]
    D -->|Confirmar| E[P-APR-004: Confirmación]
    E --> B
    
    C -->|Aprobar| F[P-APR-004: Confirmación Aprobación]
    F --> B
    
    B -->|Filtrar/Buscar| B
    B -->|Sin pendientes| G[Mensaje: Sin datos]
    
    A -->|Configurar delegación| H[P-APR-005: Delegación]
    H --> A
    
    A -->|Ver mis solicitudes<br/>como empleado| I[P-SOL-002: Mis Solicitudes]
    I -->|Crear nueva| J[P-SOL-001: Form Solicitud]
    
    K[P-APR-006: Email Notificación] -.->|Link directo| B
```

### 11.3. Flujo de Navegación - Asistente de Viaje

```mermaid
graph TD
    A[P-GEN-002: Launchpad] --> B[P-COT-001: Solicitudes Pendientes Cotización]
    
    B -->|Iniciar cotización| C[P-COT-002: Cargar Pasajes]
    
    C -->|Descargar plantilla| D[Archivo Excel<br/>Template]
    D -.->|Llenar offline| E[Cargar plantilla]
    E --> C
    
    C -->|Registrar manual| C
    C -->|Validar datos| C
    C -->|Notificar solicitante| F[P-COT-006: Email Opciones]
    
    F -.->|Solicitante selecciona| G[Notificación interna<br/>Pasaje seleccionado]
    
    G --> H[P-COT-005: Registrar Comprobante Compra]
    H -->|Adjuntar PDF| H
    H -->|Guardar| I[Confirmación]
    I --> B
    
    A -->|Registrar pasaje terrestre| J[P-SOL-005: Form Pasaje Terrestre]
    J --> A
```

### 11.4. Flujo de Navegación - Operador de Liquidación

```mermaid
graph TD
    A[P-GEN-002: Launchpad<br/>Contador pendientes] --> B{Seleccionar acción}
    
    B -->|Liquidar rendiciones| C[P-LIQ-001: Rendiciones Pendientes]
    B -->|Generar archivo banco| D[P-BAN-001: Liquidaciones Pendientes Pago]
    B -->|Consultar histórico| E[P-LIQ-007: Histórico]
    
    C -->|Revisar rendición| F[P-LIQ-002: Detalle Rendición]
    
    F -->|Ver comprobante| G[Visualizador PDF]
    G --> F
    
    F -->|Devolver con observaciones| H[P-LIQ-003: Modal Devolución]
    H --> C
    
    F -->|Aprobar y visar| I[P-LIQ-004: Confirmación Visado]
    I -->|Confirmar| J{Integración SAP}
    
    J -->|Exitoso| K[P-LIQ-005: Resultado Exitoso]
    J -->|Error| L[P-SAP-005: Error SAP]
    
    K -->|Descargar resumen| M[P-LIQ-006: PDF]
    K --> C
    
    L -->|Reprocesar| F
    L --> C
    
    D -->|Seleccionar liquidaciones| D
    D -->|Generar archivo| N[P-BAN-002: Confirmación Generación]
    N --> O[P-BAN-003: Descarga Archivo]
    O --> D
    
    D -->|Confirmar remesa ejecutada| P[P-BAN-004: Confirmar Ejecución]
    P --> D
    
    A -->|Ver monitor proceso| Q[P-REP-005: Monitor Kanban]
    Q -->|Click en documento| F
    
    A -->|Consultar documentos SAP| R[P-SAP-006: Log Transacciones]
    
    S[Visualizar en SAP] --> T[P-SAP-001: Doc Anticipo]
    S --> U[P-SAP-002: Doc Gasto]
    S --> V[P-SAP-003: Doc Compensación]
    S --> W[P-SAP-004: Doc Reembolso]
```

### 11.5. Flujo de Navegación - Administrador del Sistema

```mermaid
graph TD
    A[P-GEN-002: Launchpad] --> B{Panel Administración}
    
    B -->|Gestionar usuarios| C[P-ADM-001: Gestión Usuarios]
    B -->|Flujos aprobación| D[P-ADM-002: Config Flujos]
    B -->|Catálogos maestros| E[P-ADM-003: Maestros]
    B -->|Parámetros sistema| F[P-ADM-004: Parámetros]
    B -->|Cuentas bancarias| G[P-ADM-005: Cuentas Bancarias]
    B -->|Log auditoría| H[P-ADM-006: Log Auditoría]
    B -->|Backup/Restore| I[P-ADM-007: Backup]
    B -->|Plantillas emails| J[P-ADM-008: Plantillas Correos]
    
    C -->|Crear usuario| K[Modal Crear Usuario]
    K -->|Guardar| C
    C -->|Editar| L[Modal Editar Usuario]
    L --> C
    C -->|Activar/Desactivar| C
    C -->|Resetear password| C
    
    D -->|Seleccionar Centro Costo| D
    D -->|Asignar aprobadores| D
    D -->|Configurar tipo aprobación| D
    
    E -->|Tab Monedas| E1[Catálogo Monedas]
    E -->|Tab Tipos Gasto| E2[Catálogo Tipos Gasto]
    E -->|Tab Aerolíneas| E3[Catálogo Aerolíneas]
    E -->|Tab Centros Costo| E4[Catálogo Centros]
    E1 & E2 & E3 & E4 -->|CRUD operations| E
    
    F -->|Editar parámetro| F
    F -->|Guardar cambios| M[Confirmación]
    M --> F
    
    G -->|Buscar empleado| G
    G -->|Agregar cuenta| N[Modal Cuenta]
    N --> G
    
    H -->|Aplicar filtros| H
    H -->|Ver detalle evento| O[Drill-down JSON]
    O --> H
    H -->|Exportar Excel| P[Descarga]
    
    I -->|Generar backup| Q[Proceso Backup]
    Q --> I
    I -->|Restaurar| R[Confirmación Restauración]
    R --> I
    
    J -->|Seleccionar plantilla| J
    J -->|Editar HTML| J
    J -->|Vista previa| J
    J -->|Enviar prueba| S[Modal Email Prueba]
    J -->|Guardar| T[Confirmación]
```

### 11.6. Flujo de Navegación - Reportes (Todos los Roles)

```mermaid
graph TD
    A[P-GEN-002: Launchpad] --> B[P-REP-001: Dashboard Principal]
    
    B -->|Ver indicadores| B
    B -->|Cambiar período| B
    B -->|Filtrar centro costo| B
    B -->|Click en gráfico| C[Drill-down Detalle]
    C --> B
    
    A -->|Generar reporte solicitudes| D[P-REP-002: Gen Reporte Solicitudes]
    D -->|Configurar criterios| D
    D -->|Vista previa| E[Tabla Previa]
    E --> D
    D -->|Generar| F[Descarga Excel]
    
    A -->|Reporte por Centro Costo| G[P-REP-003: Reporte Centros]
    G -->|Configurar| G
    G -->|Exportar| H[Excel/PDF]
    
    A -->|Rendiciones pendientes| I[P-REP-004: Reporte Pendientes]
    I -->|Filtrar antigüedad| I
    I -->|Exportar| J[Excel]
    I -->|Enviar recordatorio| K[Confirmación Email]
    
    A -->|Monitor proceso| L[P-REP-005: Monitor Kanban]
    L -->|Click columna| M[Listado Documentos]
    M -->|Ver detalle| N[Detalle Documento]
    N --> M
    
    D & G & I -->|Programar envío| O[P-REP-006: Programar Envío]
    O -->|Configurar frecuencia| O
    O -->|Guardar| P[Confirmación]
```

### 11.7. Flujo de Navegación Global - Búsqueda y Notificaciones

```mermaid
graph TD
    A[Cualquier pantalla] --> B{Acciones Globales Header}
    
    B -->|Click búsqueda| C[P-GEN-006: Búsqueda Global]
    C -->|Ingresar texto| D[Autocompletado]
    D --> C
    C -->|Seleccionar resultado| E[Navegación a pantalla específica]
    
    B -->|Click notificaciones| F[P-GEN-004: Panel Notificaciones]
    F -->|Ver detalle| G[Click en link acción]
    G --> E
    F -->|Marcar leídas| F
    F -->|Filtrar| F
    
    B -->|Click perfil dropdown| H{Opciones Usuario}
    H -->|Mi Perfil| I[P-GEN-005: Mi Perfil]
    H -->|Mis Cuentas| J[P-ADM-005: Mis Cuentas]
    H -->|Cambiar Contraseña| K[Modal Cambio Password]
    H -->|Cerrar Sesión| L[Logout]
    L --> M[P-GEN-001: Login]
    
    I -->|Editar datos| I
    I -->|Config notificaciones| I
    I -->|Guardar cambios| N[Confirmación]
    
    J -->|Agregar cuenta| O[Modal Nueva Cuenta]
    O --> J
    J -->|Editar| P[Modal Editar Cuenta]
    P --> J
    
    A -->|Click menú lateral| Q[P-GEN-003: Menú Navegación]
    Q -->|Seleccionar opción| R[Navegación a módulo]
    
    A -->|Click breadcrumb| S[Navegación hacia atrás]
```

### 11.8. Flujo Completo End-to-End - Ciclo de Vida de una Solicitud

```mermaid
graph TD
    Start[Inicio] --> A[EMPLEADO: P-SOL-001 Crear Solicitud]
    A -->|Enviar a aprobación| B[Sistema envía<br/>P-APR-006 Email]
    
    B --> C[APROBADOR NIV1: P-APR-001 Bandeja]
    C -->|Revisar| D[P-APR-002 Detalle]
    D -->|Aprobar| E[Notificación a Niv2]
    D -->|Rechazar| End1[Fin: Rechazada]
    
    E --> F[APROBADOR NIV2: P-APR-001 Bandeja]
    F -->|Revisar| G[P-APR-002 Detalle]
    G -->|Aprobar| H[Notificación a<br/>Asistente y Empleado]
    G -->|Rechazar| End1
    
    H -->|Si transporte aéreo| I[ASISTENTE: P-COT-001 Cotizar]
    I --> J[P-COT-002 Cargar Pasajes]
    J --> K[EMPLEADO: P-COT-003 Seleccionar]
    K --> L[ASISTENTE: P-COT-005 Registrar Compra]
    
    L --> M[EMPLEADO: Viaje realizado]
    H -->|Si sin pasaje| M
    
    M --> N[EMPLEADO: P-REN-001 Rendir Gastos]
    N -->|Agregar comprobantes| O[P-REN-002 Modal Comprobante]
    O --> N
    N -->|Enviar a liquidación| P[Sistema notifica<br/>Operador]
    
    P --> Q[OPERADOR: P-LIQ-001 Pendientes]
    Q -->|Revisar| R[P-LIQ-002 Detalle]
    R -->|Devolver con observaciones| S[EMPLEADO corrige]
    S --> N
    
    R -->|Visar| T[P-LIQ-004 Confirmar Visado]
    T --> U{Integración SAP}
    U -->|Error| V[P-SAP-005 Error]
    V -->|Corregir| R
    
    U -->|Éxito| W[Documentos SAP generados<br/>P-SAP-001 a P-SAP-004]
    W --> X[P-LIQ-005 Resultado Exitoso]
    X --> Y[P-LIQ-006 PDF Resumen]
    
    Y --> Z[OPERADOR: P-BAN-001 Generar Archivo]
    Z --> AA[P-BAN-003 Descargar SCT]
    AA --> AB[Upload a banco offline]
    AB --> AC[P-BAN-004 Confirmar Ejecución]
    
    AC --> End2[Fin: Reembolso Pagado]
```

### 11.9. Navegación por Módulos - Estructura Jerárquica

```mermaid
graph TD
    Root[P-GEN-002: Launchpad Principal] --> Mod1[Módulo Solicitudes]
    Root --> Mod2[Módulo Rendiciones]
    Root --> Mod3[Módulo Aprobaciones]
    Root --> Mod4[Módulo Cotizaciones]
    Root --> Mod5[Módulo Liquidación]
    Root --> Mod6[Módulo Reportes]
    Root --> Mod7[Módulo Administración]
    
    Mod1 --> M1P1[P-SOL-001: Crear/Editar]
    Mod1 --> M1P2[P-SOL-002: Listado]
    Mod1 --> M1P3[P-SOL-004: Detalle]
    Mod1 --> M1P4[P-SOL-005: Pasaje Terrestre]
    
    Mod2 --> M2P1[P-REN-003: Listado]
    Mod2 --> M2P2[P-REN-001: Crear/Editar]
    Mod2 --> M2P3[P-LIQ-007: Histórico]
    
    Mod3 --> M3P1[P-APR-001: Bandeja]
    Mod3 --> M3P2[P-APR-005: Delegaciones]
    
    Mod4 --> M4P1[P-COT-001: Pendientes]
    Mod4 --> M4P2[P-COT-002: Cargar Pasajes]
    
    Mod5 --> M5P1[P-LIQ-001: Pendientes Liquid]
    Mod5 --> M5P2[P-BAN-001: Gen Archivo Bancario]
    Mod5 --> M5P3[P-BAN-005: Historial Archivos]
    
    Mod6 --> M6P1[P-REP-001: Dashboard]
    Mod6 --> M6P2[P-REP-002: Rep Solicitudes]
    Mod6 --> M6P3[P-REP-003: Rep Centros Costo]
    Mod6 --> M6P4[P-REP-004: Rep Pendientes]
    Mod6 --> M6P5[P-REP-005: Monitor Proceso]
    
    Mod7 --> M7P1[P-ADM-001: Usuarios]
    Mod7 --> M7P2[P-ADM-002: Flujos Aprob]
    Mod7 --> M7P3[P-ADM-003: Maestros]
    Mod7 --> M7P4[P-ADM-004: Parámetros]
    Mod7 --> M7P5[P-ADM-005: Ctas Bancarias]
    Mod7 --> M7P6[P-ADM-006: Log Auditoría]
    Mod7 --> M7P7[P-ADM-007: Backup]
    Mod7 --> M7P8[P-ADM-008: Plantillas Email]
    
    style Root fill:#2E86AB
    style Mod1 fill:#A23B72
    style Mod2 fill:#F18F01
    style Mod3 fill:#C73E1D
    style Mod4 fill:#6A994E
    style Mod5 fill:#BC4B51
    style Mod6 fill:#8B8C89
    style Mod7 fill:#3D5A80
```
