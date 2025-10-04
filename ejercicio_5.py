# EJERCICIO NO. 5 analizador_fechas.py
# Programa que encuentra fechas en distintos formatos y las convierte a YYYY-MM-DD
# Autor: Alain Pineda
# Fecha: 03/10/2025

import re
from datetime import datetime

# Diccionario para meses en español abreviados y completos
meses = {
    'Ene': 'Jan', 'Feb': 'Feb', 'Mar': 'Mar', 'Abr': 'Apr', 'May': 'May', 'Jun': 'Jun',
    'Jul': 'Jul', 'Ago': 'Aug', 'Sep': 'Sep', 'Oct': 'Oct', 'Nov': 'Nov', 'Dic': 'Dec',
    'Enero': 'Jan', 'Febrero': 'Feb', 'Marzo': 'Mar', 'Abril': 'Apr', 'Mayo': 'May', 'Junio': 'Jun',
    'Julio': 'Jul', 'Agosto': 'Aug', 'Septiembre': 'Sep', 'Octubre': 'Oct', 'Noviembre': 'Nov', 'Diciembre': 'Dec'
}

def convertir_fecha(fecha):
    """
    Convierte diferentes formatos de fecha a YYYY-MM-DD
    """
    # reemplazamos meses en español por inglés si existen
    for es, en in meses.items():
        fecha = re.sub(fr'\b{es}\b', en, fecha, flags=re.IGNORECASE)
    
    formatos = [
        "%d/%m/%Y",
        "%Y-%m-%d",
        "%d-%b-%Y",
        "%B %d, %Y"
    ]
    
    for f in formatos:
        try:
            dt = datetime.strptime(fecha, f)
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            continue
    return "Formato desconocido"

# Texto de ejemplo
texto = "La reunión es el 15/03/2024. El proyecto inicia el 2024-04-20 y termina en Junio 30, 2024. La entrega final es 01-Jul-2024."

# patrones de fechas (simplificados)
patron = r'\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2}|\d{2}-[A-Za-z]{3}-\d{4}|[A-Za-z]+ \d{1,2}, \d{4}'

fechas = re.findall(patron, texto)

print("Fechas encontradas y convertidas:")
for f in fechas:
    estandar = convertir_fecha(f)
    print(f"- Formato original: {f} → Estándar: {estandar}")
