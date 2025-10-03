import re

def validar_correo(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.(com|mx|org)$'
    if re.match(patron, correo):
        return "Válido"
    else:
        return "Inválido"

correos = [
    "usuario@ejemplo.com",
    "nombre.apellido@dominio.mx",
    "usuarioejemplo.com",
    "@ejemplo.com"
]

for c in correos:
    print(f"{c} → {validar_correo(c)}")
