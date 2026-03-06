# 🔍 Guía de Debugging - Módulo de Rendiciones

## Problema Reportado
"No me deja registrar gastos"

## ✅ Mejoras Implementadas

Se agregaron mejoras de validación y feedback visual para facilitar la identificación de problemas:

### 1. **Alertas de Validación**
- ⚠️ **Paso 3:** Mensaje de error si faltan campos requeridos
- ⚠️ **Paso 5:** Advertencia si el formulario es inválido antes de guardar

### 2. **Botón Guardar Mejorado**
- Ahora se deshabilita visualmente si el formulario es inválido
- Muestra mensaje claro: "Revisa que todos los campos obligatorios estén completos"

### 3. **Logging de Consola**
- Se agregó `console.log('Guardando rendición:', this.rendicionForm.value)` para ver exactamente qué se está enviando

---

## 🐛 Cómo Debuguear el Problema

### Paso 1: Verificar Campos Requeridos

Los siguientes campos SON OBLIGATORIOS para guardar un gasto:

| Campo | Validación | Ejemplo |
|-------|-----------|---------|
| **Solicitud de Viaje** | Required | SOL-2024-001 |
| **Categoría del Gasto** | Required | ALIMENTACION, TRANSPORTE, etc. |
| **Fecha** | Required | 05/03/2026 |
| **Monto** | Required, min(0.01) | 150.00 |
| **Concepto** | Required, maxLength(200) | "Almuerzo con cliente" |

❌ **Campos Opcionales (no bloquean el guardado):**
- Proveedor
- Folio
- RUC
- Justificación

---

### Paso 2: Abrir Consola del Navegador

1. **Presiona F12** en el navegador
2. Ve a la pestaña **Console**
3. Intenta registrar un gasto
4. Busca mensajes de error en rojo

**Errores Comunes:**
```
❌ Error: Cannot read property 'value' of undefined
   → El formulario no se inicializó correctamente

❌ Error: Cannot read property 'subscribe' of undefined
   → El servicio RendicionService no está inyectado

❌ Error: Invalid Date
   → Problema con la conversión de fecha del Document AI
```

---

### Paso 3: Verificar Estado del Formulario

En la **Consola del Navegador**, ejecuta:

```javascript
// Ver si el formulario es válido
angular.ng.getComponent($0).rendicionForm.valid

// Ver errores específicos
angular.ng.getComponent($0).rendicionForm.errors

// Ver valores del formulario
angular.ng.getComponent($0).rendicionForm.value

// Ver qué campos están inválidos
Object.keys(angular.ng.getComponent($0).rendicionForm.controls).forEach(key => {
  const control = angular.ng.getComponent($0).rendicionForm.get(key);
  if (control.invalid) {
    console.log(`❌ ${key}:`, control.errors);
  }
});
```

---

### Paso 4: Verificar Proceso del Wizard

Revisa que el flujo sea correcto:

1. ✅ **Paso 1 - Captura:** ¿Se cargó la imagen/PDF correctamente?
2. ✅ **Paso 2 - Preview:** ¿Se muestra la vista previa?
3. ✅ **Paso 3 - Datos:** ¿Se autocompletaron los campos?
4. ✅ **Paso 4 - Resumen:** ¿Se muestran los conceptos?
5. ✅ **Paso 5 - Confirmar:** ¿El botón "Guardar Gasto" está habilitado?

---

## 🔧 Soluciones a Problemas Comunes

### Problema 1: Botón "Guardar Gasto" Deshabilitado

**Causa:** El formulario no es válido.

**Solución:**
1. Vuelve al **Paso 3**
2. Verifica que TODOS los campos requeridos estén completos:
   - Solicitud de Viaje (seleccionada)
   - Categoría del Gasto (seleccionada)
   - Fecha (válida)
   - Monto (mayor a 0)
   - Concepto (no vacío, máx. 200 caracteres)

---

### Problema 2: Campos No Se Autocompletar

**Causa:** Error en Document AI Service o imagen no procesada.

**Solución:**
1. Verifica en la consola si aparece:
   ```
   [Document AI] Iniciando extracción de: comprobante.jpg
   [Document AI] Extracción completada: {...}
   ```

2. Si NO aparece, revisa que:
   - La imagen se haya capturado correctamente
   - El archivo no sea muy pesado (máx. 5MB)
   - El formato sea válido (JPG, PNG, PDF)

**Workaround:** Completa los campos manualmente en el Paso 3.

---

### Problema 3: Error al Guardar

**Causa:** Problema con el servicio `RendicionService.create()`.

**Solución:**
1. Verifica en la consola el mensaje:
   ```
   Guardando rendición: {solicitudId: "...", categoria: "...", ...}
   ```

2. Si aparece un error después, revisa:
   - ¿El empleadoId está correctamente configurado? (Por defecto: 'EMP-001')
   - ¿La estructura de datos coincide con el modelo `Rendicion`?

**Código del método guardar():**
```typescript
const rendicionData = {
  ...this.rendicionForm.value,
  empleadoId: 'EMP-001', // ← Verificar esto
  estado: EstadoRendicion.PENDIENTE
};
```

---

### Problema 4: Fecha Inválida

**Causa:** Error al convertir fecha del Document AI (formato DD/MM/YYYY).

**Solución:**
1. Verifica en la consola si el Document AI devolvió:
   ```
   fecha: "05/03/2026"
   ```

2. Si la fecha tiene formato incorrecto, complétala manualmente en el Paso 3.

3. Si el problema persiste, modifica temporalmente el método `autocompletarFormulario()`:
   ```typescript
   if (datos.fecha) {
     try {
       const [day, month, year] = datos.fecha.split('/');
       updates.fecha = new Date(`${year}-${month}-${day}`);
     } catch (error) {
       console.error('Error parseando fecha:', error);
       updates.fecha = new Date(); // Usar fecha actual como fallback
     }
   }
   ```

---

### Problema 5: Error 404 - Solicitudes No Cargan

**Causa:** El servicio `SolicitudService.getSolicitudes()` no encuentra datos.

**Solución:**
1. Verifica que existan solicitudes en estado **APROBADO_N1** o **APROBADO_N2**
2. Si no hay solicitudes, crea una primero en el módulo de Solicitudes

**Código de verificación:**
```typescript
loadSolicitudes(): void {
  this.solicitudService.getSolicitudes().subscribe({
    next: (solicitudes: Solicitud[]) => {
      const aprobadas = solicitudes.filter((s: Solicitud) => 
        s.estado === 'APROBADO_N1' || s.estado === 'APROBADO_N2'
      );
      console.log('Solicitudes aprobadas encontradas:', aprobadas.length);
      this.solicitudes.set(aprobadas);
    }
  });
}
```

---

## 🧪 Prueba Paso a Paso

Sigue este checklist para validar el flujo completo:

### ✅ Checklist de Prueba

- [ ] **Iniciar formulario:** Ir a `/rendiciones/formulario`
- [ ] **Paso 1:** Capturar o subir una imagen de comprobante
  - [ ] ¿Se muestra el archivo cargado?
  - [ ] ¿El botón "Siguiente" se habilitó?
- [ ] **Paso 2:** Confirmar preview
  - [ ] ¿Se ve la imagen?
  - [ ] ¿Los botones de rotación funcionan?
  - [ ] Click en "Confirmar y Extraer Datos"
- [ ] **Paso 3:** Verificar datos extraídos
  - [ ] ¿Apareció el spinner "Procesando comprobante"?
  - [ ] ¿Se autocompletaron los campos?
  - [ ] ¿El mensaje muestra confianza del Document AI?
  - [ ] Completar campos faltantes:
    - [ ] Solicitud de Viaje
    - [ ] Categoría
    - [ ] Fecha
    - [ ] Monto > 0
    - [ ] Concepto (no vacío)
  - [ ] Click en "Siguiente"
- [ ] **Paso 4:** Revisar resumen
  - [ ] ¿Se muestran los conceptos (Alojamiento, Alimentación, etc.)?
  - [ ] ¿Las barras de progreso se ven correctas?
  - [ ] Click en "Continuar"
- [ ] **Paso 5:** Confirmar y guardar
  - [ ] ¿Se muestran los datos de resumen?
  - [ ] ¿El botón "Guardar Gasto" está HABILITADO?
  - [ ] Click en "Guardar Gasto"
  - [ ] ¿Aparece el spinner "Guardando comprobante"?
  - [ ] ¿Aparece el mensaje "¡Gasto Registrado!"?

---

## 📊 Logs Esperados en Consola

### Flujo Normal (Sin Errores)

```
[Document AI] Iniciando extracción de: comprobante.jpg (245.67 KB)
[Document AI] Extracción completada: {proveedor: "Restaurant Central", monto: 150.50, confidence: 92%}
Guardando rendición: {
  solicitudId: "SOL-2024-001",
  categoria: "ALIMENTACION",
  concepto: "Almuerzo ejecutivo con cliente",
  fecha: "2026-03-05T00:00:00.000Z",
  monto: 150.5,
  moneda: "PEN",
  proveedor: "Restaurant Central",
  folio: "F001-00012345",
  ruc: "20512345678",
  justificacion: ""
}
✓ Rendición creada exitosamente: REN-1234567890
```

---

## 🚀 Próximos Pasos

Si el problema persiste después de seguir esta guía:

1. **Exporta los logs de la consola:**
   - Click derecho en la consola → "Save as..."
   - Guarda como `rendiciones_error_log.txt`

2. **Toma capturas de pantalla:**
   - Paso donde falla
   - Mensajes de error
   - Estado del formulario

3. **Comparte información:**
   - Versión del navegador
   - Sistema operativo
   - Pasos exactos para reproducir el error

---

## 📝 Notas Técnicas

### Estructura del Modelo `Rendicion`

```typescript
interface Rendicion {
  id: string;                    // Auto-generado
  solicitudId: string;           // REQUERIDO
  empleadoId: string;            // Auto: 'EMP-001'
  fecha: Date;                   // REQUERIDO
  categoria: CategoriaGasto;     // REQUERIDO
  concepto: string;              // REQUERIDO
  monto: number;                 // REQUERIDO > 0
  moneda: 'PEN' | 'USD';         // Default: 'PEN'
  comprobante?: string;          // Opcional
  estado: EstadoRendicion;       // Auto: PENDIENTE
  proveedor?: string;            // Opcional
  folio?: string;                // Opcional
  ruc?: string;                  // Opcional
  justificacion?: string;        // Opcional
}
```

### Validaciones del Formulario

```typescript
this.rendicionForm = this.fb.group({
  solicitudId: ['', Validators.required],
  categoria: ['', Validators.required],
  concepto: ['', [Validators.required, Validators.maxLength(200)]],
  fecha: [new Date(), Validators.required],
  monto: [0, [Validators.required, Validators.min(0.01)]],
  moneda: ['PEN'],
  proveedor: [''],
  folio: [''],
  ruc: [''],
  justificacion: ['']
});
```

---

**Última actualización:** 2026-03-05  
**Build:** ✅ Compilación exitosa (203.32 kB)
