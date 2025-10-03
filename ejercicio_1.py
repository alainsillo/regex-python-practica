# EJERCICIO NO.1 validador_correos.py
# Este programa checa si una cadena es un correo válido
# Autor: Alain Pineda
# Fecha: 03/10/2025

import re  # traemos la librería de expresiones regulares

def validar_correo(correo):
    """
    Función para checar correos
    
    Reglas para que sea válido:
    - Tiene que tener una @
    - Debe haber algo antes y después de la @
    - Terminar con .com, .mx o .org
    
    Devuelve "Válido" o "Inválido"
    """
    patron = r'^[\w\.-]+@[\w\.-]+\.(com|mx|org)$'  # patrón que cumple las reglas
    if re.match(patron, correo):
        return "Válido"
    else:
        return "Inválido"

# --- Probando unos correos ---
correos_prueba = [
    "usuario@ejemplo.com",       # debería pasar
    "nombre.apellido@dominio.mx",# también válido
    "usuarioejemplo.com",        # le falta la @, inválido
    "@ejemplo.com"               # no hay nada antes de @, inválido
]

# checamos cada uno y vemos qué sale
for correo in correos_prueba:
    resultado = validar_correo(correo)
    print(f"{correo} → {resultado}")
