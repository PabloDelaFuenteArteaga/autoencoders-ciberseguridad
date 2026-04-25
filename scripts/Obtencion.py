import arff
import pandas as pd

# 1. Abrimos el archivo en modo lectura
with open('dataset_', 'r') as f:
    # 2. Cargamos el contenido usando liac-arff
    datos_dict = arff.load(f)
    
    # 3. Extraemos los nombres de las columnas (atributos)
    nombres_columnas = [attr[0] for attr in datos_dict['attributes']]
    
    # 4. Creamos el DataFrame de Pandas
    df = pd.DataFrame(datos_dict['data'], columns=nombres_columnas)

# Verificamos que todo esté en orden
print(f"Dataset cargado con {df.shape[0]} filas y {df.shape[1]} columnas.")
print(df.head())

# Exportamos a csv
df.to_csv("datos_ciber.csv", index=False)