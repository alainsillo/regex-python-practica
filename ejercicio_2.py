# EJERCICIO NO. 2 extractor_telefonos.py
# Programa para encontrar todos los números de teléfono en un texto
# Autor: Alain Pineda
# Fecha: 03/10/2025

import re  # traemos la librería de expresiones regulares

def extraer_telefonos(texto):
    """
    Esto va a buscar números de teléfono mexicanos de 10 dígitos
    Soporta varios formatos:
    - 6461234567
    - 646-123-4567
    - 646 123 4567
    - (646) 123-4567
    """
    # patrón que reconoce todos los formatos mencionados
    patron = r'\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}'
    
    # buscamos todos los matchs y los devolvemos como lista
    telefonos = re.findall(patron, texto)
    return telefonos

# --- Ejemplo de texto ---
texto = "Contacta a Juan al 646-123-4567 o a María al (664) 987-6543. También puedes llamar al 5551234567."

# extraemos los teléfonos
telefonos_encontrados = extraer_telefonos(texto)
print("Teléfonos encontrados:", telefonos_encontrados)
