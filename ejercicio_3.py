# EJERCICIO NO. 3 validador_contraseñas.py
# Programa que valida si una contraseña es segura
# Autor: Alain Pineda
# Fecha: 03/10/2025

import re  # para trabajar con expresiones regulares

def validar_contraseña(contra):
    """
    Vamos a revisar si una contraseña cumple con los criterios:
    - Al menos 8 caracteres
    - Al menos una mayúscula
    - Al menos una minúscula
    - Al menos un número
    - Al menos un carácter especial (@$!%*?&#)
    
    Devuelve si es válida y qué le falta si no lo es.
    """
    errores = []  # aquí guardamos lo que le falta
    
    # Revisamos cada criterio
    if len(contra) < 8:
        errores.append("mínimo 8 caracteres")
    if not re.search(r'[A-Z]', contra):
        errores.append("al menos una letra mayúscula")
    if not re.search(r'[a-z]', contra):
        errores.append("al menos una letra minúscula")
    if not re.search(r'\d', contra):
        errores.append("al menos un número")
    if not re.search(r'[@$!%*?&#]', contra):
        errores.append("al menos un carácter especial (@$!%*?&#)")
    
    if errores:
        return f"Inválida. Le falta: {', '.join(errores)}"
    else:
        return "Válida"

# Casos de prueba
contraseñas = [
    "Segura123!",
    "contrasena",
    "MAYUSCULA123!",
    "P@ssw0rd"
]

for c in contraseñas:
    resultado = validar_contraseña(c)
    print(f"{c} → {resultado}")
