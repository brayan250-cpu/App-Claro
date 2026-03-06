# DISEÑO TÉCNICO - Sistema de Gestión de Viajes CLARO

**Proyecto:** CRM Comercial - Gestión de Viajes y Gastos Corporativos  
**Cliente:** América Móvil Perú S.A.C. (CLARO)  
**Fecha:** 3 de Marzo de 2026  
**Versión:** 1.0 - Prototipo

---

## 1. RESUMEN EJECUTIVO

### 1.1 Objetivo del Prototipo

Desarrollar un prototipo funcional frontend del Sistema de Gestión de Viajes CLARO que demuestre:
- Flujo completo de solicitud → aprobación → cotización → rendición → liquidación
- Experiencia de usuario moderna y eficiente
- Arquitectura escalable basada en Angular 17+
- Integración simulada con SAP FI y bancos

### 1.2 Alcance del Prototipo

**Incluye:**
- 64 pantallas funcionales implementadas
- 9 módulos principales con navegación completa
- 9 roles de usuario con permisos diferenciados
- Mock de servicios backend (in-memory)
- Persistencia local con LocalStorage
- Simulación de integraciones SAP y bancos
- Responsive design (desktop-first)

**Excluye:**
- Backend real y APIs productivas
- Base de datos persistente
- Autenticación real (SSO/LDAP)
- Integración real con SAP FI
- Integración real con bancos
- Web Speech API (opcional fase avanzada)

---

## 2. STACK TECNOLÓGICO

### 2.1 Frontend Core

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Angular** | 17.3+ | Framework principal SPA |
| **TypeScript** | 5.4+ | Lenguaje de desarrollo |
| **RxJS** | 7.8+ | Programación reactiva |
| **Angular Material** | 17+ (Material 3) | Componentes UI |
| **Angular CDK** | 17+ | Utilidades de UI |

### 2.2 Estado y Datos

| Tecnología | Propósito |
|------------|-----------|
| **Angular Signals** | Gestión de estado reactivo |
| **LocalStorage API** | Persistencia local de datos |
| **IndexedDB** (opcional) | Almacenamiento de archivos adjuntos |

### 2.3 Routing y Estructura

| Tecnología | Propósito |
|------------|-----------|
| **Standalone Components** | Modularidad sin NgModules |
| **Route Guards** | Control de acceso por rol |
| **Lazy Loading** | Carga diferida de módulos |

### 2.4 Desarrollo y Tooling

| Herramienta | Versión | Propósito |
|-------------|---------|-----------|
| **Angular CLI** | 17+ | Scaffolding y build |
| **ESLint** | 8+ | Linting TypeScript |
| **Prettier** | 3+ | Formateo de código |
| **Karma + Jasmine** | Latest | Testing unitario |

### 2.5 Justificación del Stack

**Angular 17+ con Signals:**
- Rendimiento superior vs Change Detection tradicional
- Sintaxis más limpia y menos boilerplate
- Mejor experiencia de desarrollo
- Alineado con el futuro de Angular

**Standalone Components:**
- Eliminación de NgModules verboso
- Mejora en tree-shaking y bundle size
- Más fácil de mantener y testear

**Material 3:**
- Diseño moderno y profesional
- Componentes accesibles (a11y)
- Consistencia visual
- Ampliamente adoptado en enterprise

**LocalStorage + Signals:**
- No requiere backend para prototipo
- Persistencia entre sesiones
- Suficiente para scope del prototipo
- Reactivo y performante

---

## 3. ARQUITECTURA DE LA APLICACIÓN

### 3.1 Patrón Arquitectónico

**Smart + Presentational Components**

```
┌─────────────────────────────────────────────┐
│          Feature Modules (Lazy)             │
│  ┌────────────────────────────────────┐     │
│  │  Smart Components (Pages)          │     │
│  │  - Lógica de negocio               │     │
│  │  - Gestión de estado (Signals)     │     │
│  │  - Llamadas a servicios            │     │
│  └────────────────┬───────────────────┘     │
│                   │                          │
│  ┌────────────────▼───────────────────┐     │
│  │  Presentational Components         │     │
│  │  - UI pura (inputs/outputs)        │     │
│  │  - Sin lógica de negocio           │     │
│  │  - Reutilizables                   │     │
│  └────────────────┬───────────────────┘     │
└───────────────────┼─────────────────────────┘
                    │
       ┌────────────▼────────────┐
       │   Shared Components      │
       │   - Button, Card, Modal  │
       │   - Table, Form Controls │
       └────────────┬─────────────┘
                    │
       ┌────────────▼────────────┐
       │   Core Services          │
       │   - Auth, Storage        │
       │   - HTTP Interceptors    │
       └────────────┬─────────────┘
                    │
       ┌────────────▼────────────┐
       │   Data Layer             │
       │   - Stores (Signals)     │
       │   - Mock Services        │
       │   - Adapters             │
       └──────────────────────────┘
```

### 3.2 Estructura de Carpetas

```
src/
├── app/
│   ├── core/                          # Singleton services
│   │   ├── auth/
│   │   │   ├── auth.service.ts        # Mock authentication
│   │   │   ├── role.guard.ts          # Route guards por rol
│   │   │   └── auth.interceptor.ts    # HTTP interceptor (mock)
│   │   ├── storage/
│   │   │   ├── storage.service.ts     # LocalStorage wrapper
│   │   │   └── cache.service.ts       # Cache in-memory
│   │   ├── navigation/
│   │   │   └── breadcrumb.service.ts  # Migas de pan
│   │   └── notification/
│   │       └── toast.service.ts       # SnackBar notifications
│   │
│   ├── shared/                         # Shared components/utilities
│   │   ├── components/
│   │   │   ├── confirm-dialog/        # MatDialog confirmación
│   │   │   ├── empty-state/           # Estado vacío
│   │   │   ├── loading-spinner/       # Spinner
│   │   │   ├── data-table/            # Tabla reutilizable
│   │   │   ├── file-upload/           # Upload de archivos
│   │   │   ├── currency-input/        # Input moneda
│   │   │   └── date-range-picker/     # Rango de fechas
│   │   ├── pipes/
│   │   │   ├── currency-format.pipe.ts
│   │   │   ├── relative-date.pipe.ts
│   │   │   └── estado-solicitud.pipe.ts
│   │   ├── directives/
│   │   │   ├── permission.directive.ts # v-if por rol
│   │   │   └── auto-focus.directive.ts
│   │   ├── models/
│   │   │   └── interfaces.ts          # Tipos globales
│   │   └── validators/
│   │       └── custom-validators.ts   # Validadores formularios
│   │
│   ├── layout/                         # Shell application
│   │   ├── main-layout/
│   │   │   ├── main-layout.component.ts
│   │   │   ├── header/                # Header con búsqueda
│   │   │   ├── sidebar/               # Menú lateral
│   │   │   └── footer/                # Footer (opcional)
│   │   └── auth-layout/
│   │       └── auth-layout.component.ts # Layout login
│   │
│   ├── features/                       # Feature modules (lazy)
│   │   ├── auth/
│   │   │   ├── login/
│   │   │   │   └── login.component.ts
│   │   │   └── auth.routes.ts
│   │   │
│   │   ├── dashboard/
│   │   │   ├── dashboard-page/
│   │   │   │   └── dashboard-page.component.ts
│   │   │   ├── components/
│   │   │   │   ├── dashboard-card.component.ts
│   │   │   │   ├── quick-stats.component.ts
│   │   │   │   └── recent-activities.component.ts
│   │   │   └── dashboard.routes.ts
│   │   │
│   │   ├── solicitudes/                # Módulo Solicitudes
│   │   │   ├── pages/
│   │   │   │   ├── solicitud-create/
│   │   │   │   ├── solicitud-list/
│   │   │   │   └── solicitud-detail/
│   │   │   ├── components/
│   │   │   │   ├── solicitud-form/
│   │   │   │   ├── presupuesto-table/
│   │   │   │   └── pasaje-info-form/
│   │   │   ├── services/
│   │   │   │   └── solicitud.service.ts
│   │   │   ├── store/
│   │   │   │   └── solicitud.store.ts  # Signal-based store
│   │   │   └── solicitudes.routes.ts
│   │   │
│   │   ├── aprobaciones/               # Módulo Aprobaciones
│   │   │   ├── pages/
│   │   │   │   ├── bandeja-aprobaciones/
│   │   │   │   └── delegacion/
│   │   │   ├── components/
│   │   │   │   ├── aprobacion-card/
│   │   │   │   └── historial-aprobaciones/
│   │   │   ├── services/
│   │   │   │   └── aprobacion.service.ts
│   │   │   └── aprobaciones.routes.ts
│   │   │
│   │   ├── cotizaciones/               # Módulo Cotización Pasajes
│   │   │   ├── pages/
│   │   │   │   ├── cotizacion-list/
│   │   │   │   └── cargar-pasajes/
│   │   │   ├── components/
│   │   │   │   ├── pasaje-table/
│   │   │   │   └── excel-upload/
│   │   │   └── cotizaciones.routes.ts
│   │   │
│   │   ├── rendiciones/                # Módulo Rendición
│   │   │   ├── pages/
│   │   │   │   ├── rendicion-create/
│   │   │   │   └── rendicion-list/
│   │   │   ├── components/
│   │   │   │   ├── comprobante-form/
│   │   │   │   └── resumen-gastos/
│   │   │   └── rendiciones.routes.ts
│   │   │
│   │   ├── liquidacion/                # Módulo Liquidación
│   │   │   ├── pages/
│   │   │   │   ├── liquidacion-list/
│   │   │   │   ├── visado/
│   │   │   │   └── archivo-bancario/
│   │   │   └── liquidacion.routes.ts
│   │   │
│   │   ├── reportes/                   # Módulo Reportes
│   │   │   ├── pages/
│   │   │   │   ├── dashboard-reportes/
│   │   │   │   └── listado-reportes/
│   │   │   └── reportes.routes.ts
│   │   │
│   │   └── admin/                      # Módulo Administración
│   │       ├── pages/
│   │       │   ├── usuarios/
│   │       │   ├── catalogos/
│   │       │   └── configuracion/
│   │       └── admin.routes.ts
│   │
│   ├── assets/                         # Static assets
│   │   ├── mocks/                      # Datos mock JSON
│   │   │   ├── usuarios.json
│   │   │   ├── solicitudes.json
│   │   │   ├── catalogos.json
│   │   │   └── README.md              # Documentación mocks
│   │   ├── images/
│   │   └── styles/
│   │
│   ├── app.config.ts                   # App configuration
│   ├── app.routes.ts                   # Root routes
│   └── app.component.ts                # Root component
│
├── environments/
│   ├── environment.ts                  # Dev environment
│   └── environment.prod.ts             # Prod environment
│
├── index.html
├── main.ts
└── styles.scss                         # Global styles
```

### 3.3 Organización por Feature

Cada feature module sigue el patrón:
- **pages/**: Smart components (páginas completas)
- **components/**: Presentational components (piezas UI)
- **services/**: Lógica de negocio y llamadas HTTP mock
- **store/**: Estado reactivo con Signals
- **models/**: Tipos e interfaces específicos del módulo
- **[feature].routes.ts**: Definición de rutas lazy

---

## 4. MODELO DE DATOS

### 4.1 Entidades Principales

#### **Solicitud (Expense Request)**
```typescript
interface Solicitud {
  id: string;                          // UUID
  numero: string;                      // SOL-2026-0001
  empleado: EmpleadoRef;               // Referencia empleado
  origen: string;
  destino: string;
  fechaInicio: Date;
  fechaFin: Date;
  motivoViaje: string;
  tipoTransporte: 'AEREO' | 'TERRESTRE';
  modalidad: 'CON_ANTICIPO' | 'SIN_ANTICIPO';
  presupuesto: PresupuestoDetalle;
  informacionPasaje?: PasajeInfo;
  estado: EstadoSolicitud;
  centroCosto: CentroCostoRef;
  historialAprobaciones: HistorialAprobacion[];
  fechaCreacion: Date;
  fechaActualizacion: Date;
  createdBy: string;
}

type EstadoSolicitud =
  | 'BORRADOR'
  | 'PENDIENTE_APROBACION_N1'
  | 'PENDIENTE_APROBACION_N2'
  | 'APROBADA'
  | 'RECHAZADA'
  | 'EN_RENDICION'
  | 'LIQUIDADA'
  | 'CANCELADA';

interface PresupuestoDetalle {
  alojamiento: number;
  alimentacion: number;
  transporteLocal: number;
  otrosGastos: number;
  total: number;                       // Calculado
  moneda: 'PEN' | 'USD';
}

interface PasajeInfo {
  tipo: 'AEREO' | 'TERRESTRE';
  aerea?: {
    aerolinea: string;
    numeroVuelo: string;
    clase: 'ECONOMICA' | 'EJECUTIVA';
    fechaHoraSalida: Date;
    fechaHoraLlegada: Date;
  };
  terrestre?: {
    empresaTransporte: string;
    distancia: number;
    duracion: number;
    ruta: string;
  };
}
```

#### **Aprobación (Approval)**
```typescript
interface HistorialAprobacion {
  id: string;
  solicitudId: string;
  nivel: 1 | 2;
  aprobador: EmpleadoRef;
  accion: 'APROBAR' | 'RECHAZAR';
  motivo?: string;                     // Obligatorio si rechaza
  fecha: Date;
}

interface Delegacion {
  id: string;
  aprobadorOriginal: EmpleadoRef;
  aprobadorDelegado: EmpleadoRef;
  nivel: 1 | 2;
  fechaInicio: Date;
  fechaFin: Date;
  activa: boolean;
}
```

#### **Cotización (Quotation)**
```typescript
interface Cotizacion {
  id: string;
  solicitudId: string;
  opciones: OpcionPasaje[];
  opcionSeleccionada?: string;        // ID opción
  estado: 'PENDIENTE' | 'SELECCIONADA' | 'COMPRADA';
  fechaCotizacion: Date;
}

interface OpcionPasaje {
  id: string;
  aerolinea: string;
  numeroVuelo: string;
  clase: 'ECONOMICA' | 'EJECUTIVA';
  fechaHoraSalida: Date;
  fechaHoraLlegada: Date;
  origen: string;
  destino: string;
  tarifaNeta: number;
  impuestos: number;
  tarifaTotal: number;
  moneda: 'PEN' | 'USD';
  escalas?: number;
}

interface ComprobantePasaje {
  id: string;
  cotizacionId: string;
  tipoDocumento: 'FACTURA' | 'BOLETA';
  numeroDocumento: string;
  fechaEmision: Date;
  rucProveedor: string;
  razonSocial: string;
  importeNeto: number;
  igv: number;
  importeTotal: number;
  archivoAdjunto: File | string;      // Base64 or URL
}
```

#### **Rendición (Expense Report)**
```typescript
interface Rendicion {
  id: string;
  numero: string;                      // REN-2026-0001
  solicitudId: string;
  comprobantes: Comprobante[];
  totalGastado: number;
  anticipoRecibido: number;
  diferencia: number;                  // Calculado
  estado: EstadoRendicion;
  observaciones?: string;
  fechaCreacion: Date;
  fechaEnvio?: Date;
}

type EstadoRendicion =
  | 'EN_RENDICION'
  | 'PENDIENTE_LIQUIDACION'
  | 'EN_CORRECCION'
  | 'LIQUIDADA';

interface Comprobante {
  id: string;
  tipoDocumento: 'FACTURA' | 'BOLETA';
  numeroDocumento: string;
  rucDni: string;
  razonSocialNombre: string;
  fechaEmision: Date;
  conceptoGasto: ConceptoGasto;
  importeNeto: number;
  igv: number;
  importeTotal: number;
  moneda: 'PEN' | 'USD';
  archivoAdjunto: string;              // Base64 or Blob URL
  justificacionExceso?: string;        // Si excede límite
}

type ConceptoGasto =
  | 'ALOJAMIENTO'
  | 'ALIMENTACION'
  | 'TRANSPORTE_LOCAL'
  | 'OTROS';
```

#### **Liquidación (Settlement)**
```typescript
interface Liquidacion {
  id: string;
  numero: string;                      // LIQ-2026-0001
  rendicionId: string;
  solicitudId: string;
  empleado: EmpleadoRef;
  totalGastado: number;
  anticipoRecibido: number;
  liquidoAPagar: number;               // Puede ser negativo (descuento)
  documentosSAP: DocumentoSAP[];
  estado: EstadoLiquidacion;
  operadorLiquidacion: EmpleadoRef;
  fechaVisado?: Date;
  archivoBancario?: ArchivoBancario;
  fechaLiquidacion: Date;
}

type EstadoLiquidacion =
  | 'PENDIENTE_REVISION'
  | 'VISADA'
  | 'ARCHIVO_GENERADO'
  | 'PAGADA';

interface DocumentoSAP {
  id: string;
  tipoDocumento:
    | 'ANTICIPO'
    | 'GASTO'
    | 'COMPENSACION'
    | 'REEMBOLSO'
    | 'DESCUENTO';
  numeroDocumentoSAP: string;          // Generado por SAP mock
  cuentaContable: string;
  centroCosto: string;
  division: string;
  importe: number;
  moneda: 'PEN' | 'USD';
  indicadorCME?: string;
  fechaContabilizacion: Date;
  estado: 'PENDIENTE' | 'CONTABILIZADO' | 'ERROR';
  mensajeError?: string;
}

interface ArchivoBancario {
  id: string;
  formato: 'SCT_BCP' | 'SCT_SCOTIABANK';
  numeroRemesa: string;
  liquidaciones: string[];             // IDs liquidaciones
  totalPagos: number;
  cantidadPagos: number;
  archivoTXT: Blob;
  fechaGeneracion: Date;
  generadoPor: string;
  estado: 'GENERADO' | 'EJECUTADO' | 'CANCELADO';
  fechaEjecucion?: Date;
}
```

#### **Referencias y Catálogos**
```typescript
interface EmpleadoRef {
  id: string;
  nombreCompleto: string;
  email: string;
  documento: string;
  centroCosto: CentroCostoRef;
  area: string;
  cargo: string;
  roles: Rol[];
  cuentasBancarias?: CuentaBancaria[];
}

type Rol =
  | 'EMPLEADO'
  | 'ASISTENTE'
  | 'APROBADOR_N1'
  | 'APROBADOR_N2'
  | 'OPERADOR_LIQUIDACION'
  | 'AUDITOR'
  | 'ADMINISTRADOR';

interface CuentaBancaria {
  id: string;
  banco: 'BCP' | 'SCOTIABANK' | 'INTERBANK';
  numeroCuenta: string;
  tipoCuenta: 'AHORROS' | 'CORRIENTE';
  moneda: 'PEN' | 'USD';
  activa: boolean;
}

interface CentroCostoRef {
  codigo: string;
  descripcion: string;
  area: string;
  responsable: string;
}

interface Moneda {
  codigo: 'PEN' | 'USD';
  simbolo: string;
  descripcion: string;
}

interface TipoGasto {
  id: string;
  nombre: string;
  cuentaContableSAP: string;
  limiteMaximo?: number;
  moneda: 'PEN' | 'USD';
}

interface Aerolinea {
  codigo: string;                      // IATA code
  nombre: string;
  pais: string;
}

interface EmpresaTransporte {
  ruc: string;
  razonSocial: string;
  tipoServicio: 'OMNIBUS' | 'VAN' | 'TAXI';
}
```

### 4.2 Persistencia

**LocalStorage Schema:**
```typescript
interface LocalStorageSchema {
  'claro-viajes:auth': {
    user: EmpleadoRef | null;
    token: string | null;
    expires: number;
  };
  'claro-viajes:solicitudes': Solicitud[];
  'claro-viajes:aprobaciones': HistorialAprobacion[];
  'claro-viajes:cotizaciones': Cotizacion[];
  'claro-viajes:rendiciones': Rendicion[];
  'claro-viajes:liquidaciones': Liquidacion[];
  'claro-viajes:catalogos': {
    empleados: EmpleadoRef[];
    centrosCosto: CentroCostoRef[];
    aerolineas: Aerolinea[];
    empresasTransporte: EmpresaTransporte[];
    tiposGasto: TipoGasto[];
  };
}
```

---

## 5. GESTIÓN DE ESTADO

### 5.1 Patrón Signal-Based Store

**Store Base Pattern:**
```typescript
// solicitud.store.ts
import { Injectable, signal, computed } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class SolicitudStore {
  // State
  private _solicitudes = signal<Solicitud[]>([]);
  private _loading = signal<boolean>(false);
  private _error = signal<string | null>(null);

  // Selectors (computed)
  solicitudes = this._solicitudes.asReadonly();
  loading = this._loading.asReadonly();
  error = this._error.asReadonly();

  // Computed selectors
  solicitudesByEstado = computed(() => {
    const items = this._solicitudes();
    return {
      borradores: items.filter(s => s.estado === 'BORRADOR'),
      pendientes: items.filter(s =>
        s.estado === 'PENDIENTE_APROBACION_N1' ||
        s.estado === 'PENDIENTE_APROBACION_N2'
      ),
      aprobadas: items.filter(s => s.estado === 'APROBADA'),
      // ... más filtros
    };
  });

  totalSolicitudes = computed(() => this._solicitudes().length);

  // Actions
  loadSolicitudes(empleadoId: string): void {
    this._loading.set(true);
    this._error.set(null);

    // Simular async call
    setTimeout(() => {
      const data = this.solicitudService.getByEmpleado(empleadoId);
      this._solicitudes.set(data);
      this._loading.set(false);
    }, 500);
  }

  addSolicitud(solicitud: Solicitud): void {
    const current = this._solicitudes();
    this._solicitudes.set([...current, solicitud]);
    this.storageService.save('solicitudes', this._solicitudes());
  }

  updateSolicitud(id: string, changes: Partial<Solicitud>): void {
    const current = this._solicitudes();
    const updated = current.map(s =>
      s.id === id ? { ...s, ...changes } : s
    );
    this._solicitudes.set(updated);
    this.storageService.save('solicitudes', updated);
  }

  deleteSolicitud(id: string): void {
    const current = this._solicitudes();
    const filtered = current.filter(s => s.id !== id);
    this._solicitudes.set(filtered);
    this.storageService.save('solicitudes', filtered);
  }

  constructor(
    private solicitudService: SolicitudService,
    private storageService: StorageService
  ) {}
}
```

### 5.2 Stores Principales

| Store | Responsabilidad |
|-------|----------------|
| **AuthStore** | Usuario autenticado, roles, permisos |
| **SolicitudStore** | Solicitudes de viaje |
| **AprobacionStore** | Aprobaciones pendientes/historial |
| **CotizacionStore** | Cotizaciones de pasajes |
| **RendicionStore** | Rendiciones de gastos |
| **LiquidacionStore** | Liquidaciones y archivos bancarios |
| **CatalogosStore** | Datos maestros (read-only) |
| **UIStore** | Estado UI (sidebar, breadcrumb, loading global) |

---

## 6. SERVICIOS

### 6.1 Servicios de Datos (Mock)

**Patrón Service:**
```typescript
// solicitud.service.ts
import { Injectable } from '@angular/core';
import { Observable, of, delay } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class SolicitudService {
  private mockData: Solicitud[] = [];

  constructor(private storageService: StorageService) {
    this.loadFromStorage();
  }

  getAll(): Observable<Solicitud[]> {
    return of([...this.mockData]).pipe(delay(400));
  }

  getById(id: string): Observable<Solicitud | undefined> {
    const found = this.mockData.find(s => s.id === id);
    return of(found).pipe(delay(300));
  }

  getByEmpleado(empleadoId: string): Observable<Solicitud[]> {
    const filtered = this.mockData.filter(
      s => s.empleado.id === empleadoId
    );
    return of(filtered).pipe(delay(400));
  }

  create(solicitud: Omit<Solicitud, 'id'>): Observable<Solicitud> {
    const newSolicitud: Solicitud = {
      ...solicitud,
      id: this.generateId(),
      numero: this.generateNumero(),
      fechaCreacion: new Date(),
      fechaActualizacion: new Date(),
    };

    this.mockData.push(newSolicitud);
    this.saveToStorage();

    return of(newSolicitud).pipe(delay(500));
  }

  update(
    id: string,
    changes: Partial<Solicitud>
  ): Observable<Solicitud | null> {
    const index = this.mockData.findIndex(s => s.id === id);

    if (index === -1) {
      return of(null).pipe(delay(200));
    }

    this.mockData[index] = {
      ...this.mockData[index],
      ...changes,
      fechaActualizacion: new Date(),
    };

    this.saveToStorage();

    return of(this.mockData[index]).pipe(delay(400));
  }

  delete(id: string): Observable<boolean> {
    const index = this.mockData.findIndex(s => s.id === id);

    if (index === -1) {
      return of(false).pipe(delay(200));
    }

    this.mockData.splice(index, 1);
    this.saveToStorage();

    return of(true).pipe(delay(300));
  }

  // Acciones específicas
  enviarAAprobacion(id: string): Observable<Solicitud | null> {
    return this.update(id, {
      estado: 'PENDIENTE_APROBACION_N1',
    });
  }

  cancelar(id: string, motivo: string): Observable<Solicitud | null> {
    return this.update(id, {
      estado: 'CANCELADA',
      motivoCancelacion: motivo,
    });
  }

  // Helper methods
  private generateId(): string {
    return `SOL-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
  }

  private generateNumero(): string {
    const year = new Date().getFullYear();
    const count = this.mockData.length + 1;
    return `SOL-${year}-${count.toString().padStart(4, '0')}`;
  }

  private loadFromStorage(): void {
    this.mockData = this.storageService.get('solicitudes') || [];
  }

  private saveToStorage(): void {
    this.storageService.save('solicitudes', this.mockData);
  }
}
```

### 6.2 Servicios Core

| Servicio | Responsabilidad |
|----------|----------------|
| **AuthService** | Mock authentication, session management |
| **StorageService** | Wrapper LocalStorage con tipado |
| **ToastService** | Notificaciones MatSnackBar |
| **DialogService** | Wrapper MatDialog para confirmaciones |
| **FileService** | Upload/download archivos, conversión Base64 |
| **ExcelService** | Parseo plantillas Excel (cotizaciones) |
| **PDFService** | Generación PDFs (resumen liquidación) |
| **ValidationService** | Validaciones de negocio centralizadas |

### 6.3 Servicios de Simulación

| Servicio | Responsabilidad |
|----------|----------------|
| **SAPSimulatorService** | Mock integración SAP FI |
| **BankSimulatorService** | Mock generación archivos SCT |
| **EmailSimulatorService** | Mock envío notificaciones email |

---

## 7. ROUTING Y NAVEGACIÓN

### 7.1 Estructura de Rutas

```typescript
// app.routes.ts
export const routes: Routes = [
  {
    path: '',
    redirectTo: '/dashboard',
    pathMatch: 'full',
  },
  {
    path: 'login',
    loadComponent: () =>
      import('./features/auth/login/login.component'),
    title: 'Iniciar Sesión',
  },
  {
    path: '',
    component: MainLayoutComponent,
    canActivate: [authGuard],
    children: [
      {
        path: 'dashboard',
        loadComponent: () =>
          import('./features/dashboard/dashboard-page.component'),
        title: 'Dashboard',
      },
      {
        path: 'solicitudes',
        loadChildren: () =>
          import('./features/solicitudes/solicitudes.routes'),
        canActivate: [roleGuard(['EMPLEADO', 'ASISTENTE', 'ADMINISTRADOR'])],
      },
      {
        path: 'aprobaciones',
        loadChildren: () =>
          import('./features/aprobaciones/aprobaciones.routes'),
        canActivate: [roleGuard(['APROBADOR_N1', 'APROBADOR_N2'])],
      },
      {
        path: 'cotizaciones',
        loadChildren: () =>
          import('./features/cotizaciones/cotizaciones.routes'),
        canActivate: [roleGuard(['ASISTENTE'])],
      },
      {
        path: 'rendiciones',
        loadChildren: () =>
          import('./features/rendiciones/rendiciones.routes'),
        canActivate: [roleGuard(['EMPLEADO'])],
      },
      {
        path: 'liquidaciones',
        loadChildren: () =>
          import('./features/liquidacion/liquidacion.routes'),
        canActivate: [roleGuard(['OPERADOR_LIQUIDACION'])],
      },
      {
        path: 'reportes',
        loadChildren: () =>
          import('./features/reportes/reportes.routes'),
        canActivate: [authGuard], // Todos los roles
      },
      {
        path: 'admin',
        loadChildren: () =>
          import('./features/admin/admin.routes'),
        canActivate: [roleGuard(['ADMINISTRADOR'])],
      },
    ],
  },
  {
    path: '**',
    loadComponent: () =>
      import('./shared/components/not-found/not-found.component'),
    title: '404 - Página no encontrada',
  },
];
```

### 7.2 Guards

**Role Guard:**
```typescript
// role.guard.ts
export const roleGuard = (allowedRoles: Rol[]) => {
  return (): boolean => {
    const authStore = inject(AuthStore);
    const router = inject(Router);

    const user = authStore.currentUser();

    if (!user) {
      router.navigate(['/login']);
      return false;
    }

    const hasRole = user.roles.some(role =>
      allowedRoles.includes(role)
    );

    if (!hasRole) {
      router.navigate(['/dashboard']);
      return false;
    }

    return true;
  };
};
```

---

## 8. COMPONENTES CLAVE

### 8.1 Smart Components (Pages)

| Componente | Ruta | Responsabilidad |
|------------|------|----------------|
| **DashboardPageComponent** | `/dashboard` | Dashboard principal con métricas |
| **SolicitudCreateComponent** | `/solicitudes/crear` | Formulario solicitud nueva |
| **SolicitudListComponent** | `/solicitudes` | Listado mis solicitudes |
| **SolicitudDetailComponent** | `/solicitudes/:id` | Detalle y edición solicitud |
| **BandejaAprobacionComponent** | `/aprobaciones` | Bandeja aprobaciones pendientes |
| **CotizacionListComponent** | `/cotizaciones` | Solicitudes pendientes cotización |
| **CargarPasajesComponent** | `/cotizaciones/:id/cargar` | Upload Excel pasajes |
| **RendicionCreateComponent** | `/rendiciones/crear/:solicitudId` | Crear rendición |
| **LiquidacionListComponent** | `/liquidaciones` | Rendiciones pendientes liquidación |
| **VisadoComponent** | `/liquidaciones/:id/visado` | Proceso de visado |

### 8.2 Presentational Components (Shared)

| Componente | Uso |
|------------|-----|
| **DataTableComponent** | Tablas reutilizables con sort/filter/pagination |
| **FormCardComponent** | Card container para formularios |
| **StatusChipComponent** | Chips de estado con colores |
| **UserAvatarComponent** | Avatar usuario con iniciales |
| **FileUploadComponent** | Drag & drop upload archivos |
| **CurrencyInputComponent** | Input con formato moneda |
| **DateRangePickerComponent** | Selector rango fechas |
| **ConfirmDialogComponent** | Dialog confirmación acciones |
| **EmptyStateComponent** | Estado vacío ilustrado |
| **LoadingSpinnerComponent** | Spinner global |

---

## 9. INTEGRACIÓN MOCK

### 9.1 SAP FI Simulator

```typescript
// sap-simulator.service.ts
@Injectable({ providedIn: 'root' })
export class SAPSimulatorService {
  generarDocumentoAnticipo(
    solicitud: Solicitud
  ): Observable<DocumentoSAP> {
    // Simular latencia
    return of({
      id: this.generateId(),
      tipoDocumento: 'ANTICIPO',
      numeroDocumentoSAP: `PE02-${this.generateSAPDocNumber()}`,
      cuentaContable: '1103010541', // ANTICIPO FUNCIONARIOS
      centroCosto: solicitud.centroCosto.codigo,
      division: '1000',
      importe: solicitud.presupuesto.total,
      moneda: solicitud.presupuesto.moneda,
      indicadorCME: 'X',
      fechaContabilizacion: new Date(),
      estado: 'CONTABILIZADO',
    } as DocumentoSAP).pipe(delay(1500));
  }

  generarDocumentosGasto(
    rendicion: Rendicion
  ): Observable<DocumentoSAP[]> {
    const docs: DocumentoSAP[] = rendicion.comprobantes.map(comp => ({
      id: this.generateId(),
      tipoDocumento: 'GASTO',
      numeroDocumentoSAP: `PE03-${this.generateSAPDocNumber()}`,
      cuentaContable: this.getCuentaByConcepto(comp.conceptoGasto),
      centroCosto: rendicion.solicitud.centroCosto.codigo,
      division: '1000',
      importe: comp.importeTotal,
      moneda: comp.moneda,
      fechaContabilizacion: new Date(),
      estado: 'CONTABILIZADO',
    }));

    return of(docs).pipe(delay(2000));
  }

  validarDisponibilidadPresupuestaria(
    centroCosto: string,
    monto: number
  ): Observable<boolean> {
    // Simular validación (siempre OK en prototipo)
    return of(true).pipe(delay(800));
  }

  private getCuentaByConcepto(concepto: ConceptoGasto): string {
    const mapping: Record<ConceptoGasto, string> = {
      ALOJAMIENTO: '4610130154',
      ALIMENTACION: '4610130154',
      TRANSPORTE_LOCAL: '4610130154',
      OTROS: '1103013002', // COSTOS A COMPROBAR
    };
    return mapping[concepto];
  }

  private generateSAPDocNumber(): string {
    return Math.floor(1000000000 + Math.random() * 9000000000).toString();
  }

  private generateId(): string {
    return `DOC-SAP-${Date.now()}`;
  }
}
```

### 9.2 Bank File Generator

```typescript
// bank-simulator.service.ts
@Injectable({ providedIn: 'root' })
export class BankSimulatorService {
  generarArchivoSCT(
    liquidaciones: Liquidacion[],
    banco: 'BCP' | 'SCOTIABANK'
  ): Observable<ArchivoBancario> {
    const content = banco === 'BCP'
      ? this.generateBCPFormat(liquidaciones)
      : this.generateScotiabankFormat(liquidaciones);

    const blob = new Blob([content], { type: 'text/plain' });

    const archivo: ArchivoBancario = {
      id: this.generateId(),
      formato: banco === 'BCP' ? 'SCT_BCP' : 'SCT_SCOTIABANK',
      numeroRemesa: this.generateRemesaNumber(banco),
      liquidaciones: liquidaciones.map(l => l.id),
      totalPagos: liquidaciones.reduce((sum, l) => sum + l.liquidoAPagar, 0),
      cantidadPagos: liquidaciones.length,
      archivoTXT: blob,
      fechaGeneracion: new Date(),
      generadoPor: 'OPERADOR',
      estado: 'GENERADO',
    };

    return of(archivo).pipe(delay(1000));
  }

  private generateBCPFormat(liquidaciones: Liquidacion[]): string {
    let content = '';

    // Header
    content += '0001|'; // Tipo registro
    content += 'CLARO|'; // Empresa
    content += new Date().toISOString().split('T')[0] + '|';
    content += liquidaciones.length.toString() + '\n';

    // Detalle
    liquidaciones.forEach((liq, index) => {
      content += '0002|'; // Tipo registro detalle
      content += (index + 1).toString().padStart(6, '0') + '|';
      content += liq.empleado.cuentasBancarias![0].numeroCuenta + '|';
      content += liq.liquidoAPagar.toFixed(2) + '|';
      content += liq.numero + '\n';
    });

    return content;
  }

  private generateScotiabankFormat(liquidaciones: Liquidacion[]): string {
    // Similar pero con formato Scotiabank
    return `Scotiabank format - ${liquidaciones.length} pagos`;
  }

  private generateRemesaNumber(banco: string): string {
    const prefix = banco === 'BCP' ? 'REM-BCP' : 'REM-SCO';
    const timestamp = Date.now().toString().slice(-6);
    return `${prefix}-${timestamp}`;
  }

  private generateId(): string {
    return `ARCHIVO-${Date.now()}`;
  }
}
```

---

## 10. DISEÑO UI/UX

### 10.1 Paleta de Colores (Material 3)

**Branding CLARO:**
```scss
// styles/theme.scss
$claro-primary: (
  50: #e3f2fd,
  100: #bbdefb,
  200: #90caf9,
  300: #64b5f6,
  400: #42a5f5,
  500: #e30613,  // Rojo CLARO principal
  600: #cd0512,
  700: #b70410,
  800: #a1040e,
  900: #8b030c,
  contrast: (
    50: rgba(black, 0.87),
    100: rgba(black, 0.87),
    200: rgba(black, 0.87),
    300: rgba(black, 0.87),
    400: rgba(black, 0.87),
    500: white,
    600: white,
    700: white,
    800: white,
    900: white,
  )
);

$claro-accent: (
  500: #00a19c,  // Verde/turquesa secundario
);

$claro-warn: (
  500: #f44336,   // Rojo material warn
);
```

### 10.2 Tipografía

```scss
// styles/typography.scss
$custom-typography: mat.define-typography-config(
  $font-family: '"Roboto", "Helvetica Neue", Arial, sans-serif',
  $headline-1: mat.define-typography-level(32px, 40px, 700),
  $headline-2: mat.define-typography-level(28px, 36px, 600),
  $headline-3: mat.define-typography-level(24px, 32px, 600),
  $headline-4: mat.define-typography-level(20px, 28px, 600),
  $headline-5: mat.define-typography-level(18px, 24px, 600),
  $body-1: mat.define-typography-level(16px, 24px, 400),
  $body-2: mat.define-typography-level(14px, 20px, 400),
  $caption: mat.define-typography-level(12px, 16px, 400),
);
```

### 10.3 Layout Patterns

**Main Layout:**
- Header fixed: 64px height
- Sidebar collapsible: 240px / 64px
- Content area responsive
- Footer opcional

**Responsive Breakpoints:**
- Desktop: >= 1280px
- Tablet: 768px - 1279px
- Mobile: < 768px

---

## 11. TESTING

### 11.1 Testing Strategy

| Tipo | Scope | Herramientas |
|------|-------|-------------|
| **Unit Tests** | Servicios, Pipes, Utilidades | Jasmine + Karma |
| **Component Tests** | Componentes individuales | Angular Testing Library |
| **Integration Tests** | Flujos completos | Jasmine + Karma |
| **E2E Tests** (opcional) | User journeys críticos | Playwright |

### 11.2 Coverage Objetivo

- **Servicios:** >= 80%
- **Stores:** >= 80%
- **Pipes:** >= 90%
- **Components:** >= 60%

---

## 12. DESPLIEGUE Y BUILD

### 12.1 Build Configuration

**Development:**
```bash
ng serve --configuration=development
# http://localhost:4200
```

**Production:**
```bash
ng build --configuration=production
# dist/claro-viajes/
```

### 12.2 Optimizaciones Build

- **Tree-shaking**: Standalone components reducen bundle size
- **Lazy loading**: Módulos por feature
- **AOT compilation**: Ahead-of-time por defecto
- **Code splitting**: Chunks automáticos
- **Minification**: Terser para JS

### 12.3 Docker (opcional)

```dockerfile
# Dockerfile
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build --configuration=production

FROM nginx:alpine
COPY --from=build /app/dist/claro-viajes /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

---

## 13. SEGURIDAD

### 13.1 Consideraciones

**Mock Authentication:**
- Login simulado con credenciales hardcoded
- Session token en LocalStorage
- Auto-logout tras 1 hora inactividad

**Route Protection:**
- Guards por rol en todas las rutas protegidas
- Redirección a login si no autenticado
- Redirección a dashboard si rol no autorizado

**Input Validation:**
- Reactive Forms con validators
- Sanitización de inputs (Angular automático)
- Validación server-side simulada

**File Upload:**
- Validación tipo MIME
- Límite tamaño 5 MB
- Conversión a Base64 para persistencia

---

## 14. PERFORMANCE

### 14.1 Estrategias

**Change Detection:**
- OnPush por defecto en componentes presentacionales
- Signals evitan checks innecesarios

**Virtual Scrolling:**
- Para listas largas (>50 items)
- Angular CDK Virtual Scroll

**Image Optimization:**
- Lazy loading nativo (`loading="lazy"`)
- Formato WebP cuando sea posible

**Bundle Size:**
- Target: < 500 KB initial bundle
- Lazy loading agresivo por feature

---

## 15. PRÓXIMOS PASOS

### 15.1 Fase 1: Setup e Infraestructura
- Crear proyecto Angular 17+
- Configurar Material 3
- Implementar layout base
- Setup routing y guards
- Crear stores principales

### 15.2 Fase 2: Módulo Solicitudes
- Implementar CRUD solicitudes
- Formulario creación
- Listado y detalle
- Estados workflow

### 15.3 Fase 3: Módulo Aprobaciones
- Bandeja aprobaciones
- Acciones aprobar/rechazar
- Delegación
- Notificaciones mock

### 15.4 Fase 4: Módulos Complementarios
- Cotizaciones
- Rendiciones
- Liquidaciones
- Reportes

### 15.5 Fase 5: Polish y Demo
- Dashboard con métricas
- Refinamiento UI/UX
- Testing
- Documentación demo

---

## ANEXOS

### A. Convenciones de Código

**Naming:**
- Components: `PascalCase` + `Component` suffix
- Services: `PascalCase` + `Service` suffix
- Stores: `PascalCase` + `Store` suffix
- Interfaces: `PascalCase` (sin prefix `I`)
- Constants: `UPPER_SNAKE_CASE`

**File Structure:**
```
feature-name/
├── feature-name.component.ts
├── feature-name.component.html
├── feature-name.component.scss
└── feature-name.component.spec.ts
```

**Imports Order:**
1. Angular core
2. Angular Material
3. RxJS
4. Third party
5. App core
6. App shared
7. Relative imports

### B. Git Workflow

**Branches:**
- `main`: Production-ready
- `develop`: Integration branch
- `feature/*`: Nueva funcionalidad
- `fix/*`: Bugfixes

**Commit Convention:**
```
type(scope): subject

feat(solicitudes): add create form
fix(aprobaciones): correct status filter
docs(readme): update setup instructions
```

### C. Referencias

- [Angular 17 Documentation](https://angular.dev)
- [Angular Material 3](https://material.angular.io)
- [Angular Signals](https://angular.dev/guide/signals)
- [Angular Standalone Components](https://angular.dev/guide/components/importing)

---

**Documento generado:** 3 de Marzo de 2026  
**Versión:** 1.0  
**Estado:** Aprobado para implementación
