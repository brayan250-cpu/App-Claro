#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para completar el análisis de todas las imágenes extraídas
"""
import re
import os

def extraer_contenido_imagen(requisitos_content, img_num):
    """Extrae todo el contenido OCR relacionado con una imagen específica"""
    # Buscar todas las referencias a la imagen
    pattern = rf'img{img_num}#(ocr|diagram|table)\)_'
    matches = re.finditer(pattern, requisitos_content)
    
    contenidos = []
    for match in matches:
        # Extraer el contenido antes del patrón de origen
        end_pos = match.start()
        # Buscar hacia atrás hasta encontrar el inicio del contenido
        start_patterns = [
            r'\*\*RF-\d+\*\*:',
            r'\*\*RB-\d+\*\*:',
            r'\*\*DC-\d+\*\*:',
            r'\*\*UI-\d+\*\*:',
        ]
        
        start_pos = 0
        for i in range(end_pos - 1, max(0, end_pos - 2000), -1):
            for pattern in start_patterns:
                if re.match(pattern, requisitos_content[i:i+15]):
                    start_pos = i
                    break
            if start_pos > 0:
                break
        
        if start_pos == 0:
            start_pos = max(0, end_pos - 500)
        
        # Extraer el texto
        texto = requisitos_content[start_pos:end_pos].strip()
        # Limpiar el texto
        texto = re.sub(r'\*\*(RF|RB|DC|UI)-\d+\*\*:\s*', '', texto)
        
        if texto and len(texto) > 5:
            contenidos.append(texto)
    
    return contenidos

def clasificar_imagen(contenidos):
    """Clasifica el tipo de imagen basándose en su contenido"""
    texto_completo = ' '.join(contenidos).lower()
    
    if not contenidos or all(len(c) < 10 for c in contenidos):
        return "Interfaz", "Sin texto significativo reconocido"
    
    # Palabras clave para clasificación
    if any(kw in texto_completo for kw in ['moneda pen', 'fecha', 'documento', 'numero', 'sociedad', 'ejercicio']):
        if 'visualizar documento' in texto_completo or 'n° documento' in texto_completo:
            return "Pantalla SAP", "Documento contable"
    
    if any(kw in texto_completo for kw in ['solicitud de gasto', 'rendicion', 'centro de costes']):
        return "Formulario", "Gestión de gastos/viajes"
    
    if any(kw in texto_completo for kw in ['aerolinea', 'vuelo', 'pasaje', 'hora de salida', 'tarifa']):
        return "Tabla", "Información de pasajes"
    
    if any(kw in texto_completo for kw in ['reporte', 'dashboard', 'search engines', 'referring sites']):
        return "Dashboard", "Reporte de métricas"
    
    if any(kw in texto_completo for kw in ['aprobar', 'rechazar', 'reenviar', 'cerrar', 'guardar']):
        return "Botón/Acción", "Elemento de interfaz"
    
    if any(kw in texto_completo for kw in ['proveedor', 'ruc', 'factura', 'importe', 'igv']):
        return "Formulario", "Registro de comprobante"
    
    if len(contenidos) == 1 and len(contenidos[0]) < 50:
        return "Elemento UI", "Texto breve"
    
    return "Interfaz", "Contenido mixto"

def generar_markdown_imagen(img_num, contenidos):
    """Genera el markdown para una imagen"""
    tipo, subtipo = clasificar_imagen(contenidos)
    
    md = f"\n### Análisis de Imagen: img{img_num}\n\n"
    md += f"**Tipo:** {tipo} - {subtipo}\n\n"
    
    if not contenidos or all(len(c) < 10 for c in contenidos):
        md += "**Contenido OCR:** (Sin texto significativo reconocido)\n\n"
    else:
        md += "**Contenido OCR:**\n```\n"
        for contenido in contenidos[:5]:  # Limitar a 5 contenidos máximo
            if len(contenido) > 10:
                # Limpiar y limitar longitud
                contenido_limpio = contenido[:500] if len(contenido) > 500 else contenido
                md += f"{contenido_limpio}\n"
        md += "```\n\n"
    
    md += "---\n"
    return md

def main():
    # Leer el archivo requisitos.md
    with open('requisitos.md', 'r', encoding='utf-8') as f:
        requisitos_content = f.read()
    
    # Obtener lista de imágenes
    imagenes = []
    for filename in os.listdir('images'):
        if filename.endswith('.png'):
            img_num = filename.split('_img')[1].replace('.png', '')
            if img_num.isdigit():
                imagenes.append(int(img_num))
    
    imagenes.sort()
    
    print(f"Procesando {len(imagenes)} imágenes...")
    
    # Generar el contenido
    output = "# Análisis Completo de Imágenes - Gestión de Viajes CLARO\n\n"
    output += f"Este documento contiene el análisis de las {len(imagenes)} imágenes extraídas del documento fuente.\n\n"
    output += "---\n"
    
    # Procesar en lotes de 25
    for i in range(0, len(imagenes), 25):
        lote = imagenes[i:i+25]
        output += f"\n## LOTE {(i//25)+1}: Imágenes {lote[0]}-{lote[-1]}\n"
        
        for img_num in lote:
            contenidos = extraer_contenido_imagen(requisitos_content, img_num)
            output += generar_markdown_imagen(img_num, contenidos)
        
        print(f"  Lote {(i//25)+1} procesado ({len(lote)} imágenes)")
    
    # Resumen final
    output += "\n## RESUMEN COMPLETO\n\n"
    output += f"**Total de imágenes analizadas:** {len(imagenes)}\n\n"
    output += "**Archivo fuente:** requisitos.md\n\n"
    output += "Para análisis visual detallado (colores, posiciones, wireframes), configurar servidor MCP imageReader.\n\n"
    
    # Guardar
    with open('imagenes_completo.md', 'w', encoding='utf-8') as f:
        f.write(output)
    
    print(f"\n✓ Completado! Archivo generado: imagenes_completo.md")
    print(f"✓ Total de imágenes procesadas: {len(imagenes)}")

if __name__ == "__main__":
    main()
