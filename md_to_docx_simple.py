#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script simple para convertir markdown a DOCX usando pypandoc.
No procesa diagramas Mermaid (se mostrarán como bloques de código).
"""
import sys
from pathlib import Path
import pypandoc

def convert_md_to_docx_simple(input_md, output_docx):
    """Convierte markdown a DOCX usando pypandoc"""
    input_path = Path(input_md)
    output_path = Path(output_docx)
    
    if not input_path.exists():
        print(f"Error: El archivo {input_path} no existe")
        sys.exit(1)
    
    print(f"Convirtiendo {input_path.name} a DOCX...")
    print("Nota: Los diagramas Mermaid se mostrarán como bloques de código")
    
    try:
        # Convertir usando pypandoc
        pypandoc.convert_file(
            str(input_path),
            'docx',
            outputfile=str(output_path),
            extra_args=[
                '--toc',  # Tabla de contenidos
                '--toc-depth=3',  # Profundidad del TOC
                '--highlight-style=tango',  # Estilo de resaltado de código
            ]
        )
        
        print(f"\n✓ Conversión exitosa:")
        print(f"  {output_path.absolute()}")
        print(f"  Tamaño: {output_path.stat().st_size:,} bytes")
        
    except Exception as e:
        print(f"Error durante la conversión: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python md_to_docx_simple.py <archivo.md> <salida.docx>")
        sys.exit(1)
    
    input_md = sys.argv[1]
    output_docx = sys.argv[2]
    
    convert_md_to_docx_simple(input_md, output_docx)
