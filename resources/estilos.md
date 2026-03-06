# 🎨 Guía de Estilo — CLARO Perú

> Colores y tipografía basados en la identidad visual de CLARO para https://www.claro.com.pe/personas/

## 🖌️ Colores

### **Colores de Fondo (Background Colours)**

| Color          | HEX       | RGB                | Uso                                    |
| :------------- | :-------- | :----------------- | :------------------------------------- |
| Blanco         | `#FFFFFF` | `rgb(255,255,255)` | Fondo principal del sitio              |
| Rojo CLARO     | `#E30613` | `rgb(227,6,19)`    | **Barra de navegación principal, botones destacados, elementos corporativos** |
| Negro          | `#000000` | `rgb(0,0,0)`       | Fondos especiales, footer              |
| Gris oscuro    | `#1A1A1A` | `rgb(26,26,26)`    | Fondos de overlay, modales             |
| Gris claro     | `#F5F5F5` | `rgb(245,245,245)` | Cards, hover states                    |
| Gris medio     | `#E8E8E8` | `rgb(232,232,232)` | Dividers, backgrounds secundarios      |

---

### **Colores de Texto (Text Colours)**

| Color            | HEX       | RGB                | Uso                                    |
| :--------------- | :-------- | :----------------- | :------------------------------------- |
| Negro principal  | `#212121` | `rgb(33,33,33)`    | Texto principal body, navegación       |
| Blanco           | `#FFFFFF` | `rgb(255,255,255)` | Texto sobre fondos rojos/oscuros, menú navegación |
| Rojo CLARO       | `#E30613` | `rgb(227,6,19)`    | Textos destacados, llamadas a la acción, links |
| Gris oscuro      | `#424242` | `rgb(66,66,66)`    | Texto secundario                       |
| Gris medio       | `#757575` | `rgb(117,117,117)` | Labels, hints, texto terciario         |
| Azul enlace      | `#0066CC` | `rgb(0,102,204)`   | Enlaces secundarios, informativos      |

---

## ✍️ Tipografía (Typography)

**Fuente principal:** `'Helvetica Neue', Helvetica, Arial, sans-serif`

**Fuentes complementarias:**
- `Roboto, sans-serif` (para Material Design components)
- `'Open Sans', sans-serif` (fallback alternativo)

### Jerarquía tipográfica

| Elemento                       | Tamaño | Peso           | Color       | Uso                                   |
| :----------------------------- | :----- | :------------- | :---------- | :------------------------------------ |
| **Encabezado principal (H1)**  | 32px   | 700 (Bold)     | `#212121`   | Títulos principales                   |
| **Encabezado secundario (H2)** | 24px   | 600 (Semibold) | `#212121`   | Títulos de sección                    |
| **Encabezado terciario (H3)**  | 20px   | 600 (Semibold) | `#424242`   | Subtítulos                            |
| **Texto principal (Body)**     | 16px   | 400 (Normal)   | `#212121`   | Contenido general                     |
| **Texto secundario (Body Small)** | 14px | 400 (Normal)  | `#424242`   | Texto secundario                      |
| **Texto destacado**            | 16px   | 700 (Bold)     | `#212121`   | Información importante, énfasis       |
| **Enlaces navegación**         | 16px   | 500 (Medium)   | `#FFFFFF`   | Enlaces del menú principal sobre fondo rojo |
| **Texto botones**              | 16px   | 600 (Semibold) | `#FFFFFF`   | Texto en botones primarios            |
| **Caption/Hints**              | 12px   | 400 (Normal)   | `#757575`   | Anotaciones, hints, información auxiliar |

### Notas de implementación

- La fuente **Helvetica Neue** es una tipografía sans-serif moderna que aporta limpieza y profesionalismo. Si no está disponible, usar **Helvetica** o **Arial** como fallback.
- El **color rojo corporativo (#E30613)** es el elemento visual más distintivo de CLARO y debe usarse para:
  - Barra de navegación principal
  - Botones de acción primarios (FloatingActionButton, CTAs)
  - Elementos de énfasis corporativo
  - Headers y secciones destacadas
  - Enlaces y llamadas a la acción
- Los textos sobre fondo rojo deben ser siempre **blancos (#FFFFFF)** para máximo contraste y accesibilidad.
- El texto del body utiliza un negro suave (#212121) en lugar de negro puro (#000000) para mejor legibilidad y menos fatiga visual.
- La tipografía mantiene un tamaño base de **16px** para mejor experiencia de usuario y accesibilidad web (WCAG).
- Para componentes de Angular Material, usar **Roboto** como fuente complementaria ya que es la tipografía estándar de Material Design.
- Mantener jerarquía visual clara: H1 (32px) > H2 (24px) > H3 (20px) > Body (16px) > Small (14px) > Caption (12px).