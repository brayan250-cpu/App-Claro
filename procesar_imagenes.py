import base64
import sys
import os

def imagen_a_base64(ruta_imagen):
    """Convierte una imagen a base64"""
    try:
        with open(ruta_imagen, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python procesar_imagenes.py <ruta_imagen>")
        sys.exit(1)
    
    ruta = sys.argv[1]
    if not os.path.exists(ruta):
        print(f"Error: No se encontró el archivo {ruta}")
        sys.exit(1)
    
    base64_str = imagen_a_base64(ruta)
    print(base64_str)
