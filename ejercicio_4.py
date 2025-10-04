# EJERCICIO NO. 4 extractor_urls.py
# Programa que encuentra URLs en un texto y separa protocolo, dominio y ruta
# Autor: Alain Pineda
# Fecha: 03/10/2025

import re

def extraer_urls(texto):
    """
    Esta Función  busca URLs y separa:
    - Protocolo (http, https)
    - Dominio
    - Ruta (opcional)
    
    Soporta:
    - http://ejemplo.com
    - https://www.ejemplo.com/pagina
    - www.ejemplo.com
    """
    # Patrón para URLs con o sin protocolo
    patron = r'(https?://)?(www\.)?([\w\-]+\.[\w\-]+)(/[\w\-/]*)?'
    
    matches = re.findall(patron, texto)
    urls = []
    
    for m in matches:
        protocolo = m[0][:-3] if m[0] else ""  # quitamos los :// del protocolo
        dominio = m[1] + m[2] if m[1] else m[2]
        ruta = m[3] if m[3] else ""
        urls.append({
            "url": protocolo + "://" + dominio + ruta if protocolo else dominio + ruta,
            "protocolo": protocolo if protocolo else "N/A",
            "dominio": dominio,
            "ruta": ruta if ruta else "N/A"
        })
    return urls

# Texto de ejemplo
texto = "Visita https://www.google.com o http://github.com/usuario. También puedes ir a www.python.org para más info."

# extraemos las URLs
urls_encontradas = extraer_urls(texto)

# mostramos resultado
for i, u in enumerate(urls_encontradas, start=1):
    print(f"URL {i}: {u['url']}")
    print(f"  Protocolo: {u['protocolo']}")
    print(f"  Dominio: {u['dominio']}")
    print(f"  Ruta: {u['ruta']}\n")
