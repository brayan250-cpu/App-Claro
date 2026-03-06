#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script simple para combinar archivos markdown numerados en un solo archivo.
Uso: python combinar_markdown.py carpeta_analisis salida.md
"""
import sys
import re
from pathlib import Path

def collect_md_files(dir_path):
    """Recolecta archivos .md numerados (01_*.md, 02_*.md, etc.)"""
    pattern = re.compile(r"^(\d+)_.*\.md$", re.IGNORECASE)
    candidates = []
    
    for p in dir_path.iterdir():
        if not p.is_file() or p.name == 'debug.md':
            continue
        m = pattern.match(p.name)
        if m:
            num = int(m.group(1))
            candidates.append((num, p.name, p))
    
    candidates.sort(key=lambda t: (t[0], t[1]))
    return [c[2] for c in candidates]

def combine_markdown(input_dir, output_file):
    """Combina múltiples archivos markdown en uno solo"""
    input_path = Path(input_dir)
    output_path = Path(output_file)
    
    if not input_path.is_dir():
        print(f"Error: {input_path} no es una carpeta válida")
        sys.exit(1)
    
    files = collect_md_files(input_path)
    
    if not files:
        print(f"Error: No se encontraron archivos .md válidos en {input_path}")
        print("Se buscan archivos con formato: 01_nombre.md, 02_nombre.md, etc.")
        sys.exit(1)
    
    print(f"Archivos encontrados ({len(files)}):")
    for f in files:
        print(f"  - {f.name}")
    
    # Combinar contenido
    parts = []
    parts.append("# ANÁLISIS FUNCIONAL - Sistema de Gestión de Viajes CLARO\n")
    parts.append("## CRM Comercial - Prototipo\n\n")
    parts.append(f"**Fecha de generación:** 03 de Marzo de 2026\n\n")
    parts.append("---\n\n")
    
    for f in files:
        print(f"Procesando: {f.name}...")
        content = f.read_text(encoding='utf-8')
        
        # Limpiar el contenido
        content = content.strip()
        
        # Agregar separador entre secciones
        parts.append(content)
        parts.append("\n\n---\n\n")
    
    # Escribir archivo combinado
    combined_content = "\n".join(parts)
    output_path.write_text(combined_content, encoding='utf-8')
    
    print(f"\n✓ Archivo combinado generado exitosamente:")
    print(f"  {output_path.absolute()}")
    print(f"  Tamaño: {output_path.stat().st_size:,} bytes")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python combinar_markdown.py <carpeta_input> <archivo_output.md>")
        print("Ejemplo: python combinar_markdown.py analisis Analisis_Funcional_Completo.md")
        sys.exit(1)
    
    input_dir = sys.argv[1]
    output_file = sys.argv[2]
    
    combine_markdown(input_dir, output_file)
