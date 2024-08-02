import easyocr
import pandas as pd

# Paso 1: Extraer el texto de la imagen
reader = easyocr.Reader(['es'])
results = reader.readtext('imagen.png')

# Paso 2: Definir palabras clave que indican el inicio y fin de la tabla
start_keyword = 'categoria'
end_keyword = 'compañia'

# Paso 3: Procesar el texto para identificar la tabla y sus límites
inside_table = False
table_content = []

for (bbox, text, prob) in results:
    if start_keyword in text.lower():
        inside_table = True
        continue  # No incluir la palabra clave en la tabla

    if end_keyword in text.lower():
        inside_table = False
        break  # Terminar el bucle al encontrar la palabra clave

    if inside_table:
        table_content.append(text)

# Paso 4: Convertir el contenido de la tabla en un DataFrame
if table_content:
    max_len = max(len(row.split()) for row in table_content)  # Supone que cada fila está separada por espacios
    processed_table = [row.split() for row in table_content]
    for row in processed_table:
        while len(row) < max_len:
            row.append('')

    df = pd.DataFrame(processed_table)
    print(df)
else:
    print("No se encontró ninguna tabla entre 'categoria' y 'compañia'.")
