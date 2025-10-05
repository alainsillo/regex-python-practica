# EJERCICIO NO.1 validador_correos.py 
# Este programa lee un archivo de correos y dice cuántos son válidos e inválidos
# Autor: Alain Pineda
# Fecha: 04/10/2025

import re
import matplotlib.pyplot as plt  # Librería para graficar

# Expresión regular
patron = r'^\d+\.\s*[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

validos = 0
invalidos = 0

# Leer archivo
with open("correos.txt", "r", encoding="utf-8") as f:
    for linea in f:
        correo = linea.strip()
        if correo:
            if re.match(patron, correo):
                validos += 1
            else:
                invalidos += 1

# Imprimir resultados
print(f"Correos válidos: {validos}")
print(f"Correos inválidos: {invalidos}")

# Gráfica de pastel sencilla
labels = ['Válidos', 'Inválidos']
sizes = [validos, invalidos]
colors = ['#FFC0CB', '#FFB6C1']  # Dos tonos de rosa

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Correos válidos e inválidos')
plt.show()
