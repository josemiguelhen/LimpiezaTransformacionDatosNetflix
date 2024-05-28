import pandas as pd
import numpy as np

# Cargar el dataset
df = pd.read_csv('netflix1.csv')

# 1. Eliminar valores nulos
print("Valores nulos por columna antes de la limpieza:")
print(df.isnull().sum())

df.dropna(inplace=True)

print("Valores nulos por columna después de la limpieza:")
print(df.isnull().sum())

# 2. Reemplazar valores incompletos (en este caso, ya se eliminaron los nulos)

# 3. Convertir columnas a un tipo de datos específico
df['release_year'] = df['release_year'].astype(int)

# 4. Crear nuevas métricas o features a partir de columnas existentes
# Por ejemplo, podemos crear una columna 'main_genre' que contiene el primer género listado
df['main_genre'] = df['listed_in'].apply(lambda x: x.split(',')[0] if pd.notnull(x) else x)

# Mostrar el DataFrame después de la transformación
print("DataFrame después de la limpieza y transformación:")
print(df.head())

# Guardar el DataFrame limpio
df.to_csv('netflix_cleaned.csv', index=False)
