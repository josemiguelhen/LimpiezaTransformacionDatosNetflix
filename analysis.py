import pandas as pd

# Cargar el dataset limpio
df = pd.read_csv('netflix_cleaned.csv')

# ¿Cuántos valores nulos encuentras en los datos? ¿Los puedes eliminar?
print("Valores nulos por columna:")
print(df.isnull().sum())

# ¿Cuántos valores incompletos encuentras en los datos? ¿Los puedes reemplazar?
# (En este caso, ya se han eliminado valores nulos, pero se podrían reemplazar en vez de eliminarlos)

# ¿Puedes eliminar columnas que no te aportan información? ¿Cuáles son? ¿Por qué las eliminarías?
# Esto depende del análisis que se va a realizar. Un análisis típico podría considerar las columnas 
# 'director' o 'country' como menos importantes si se enfocara solo en la popularidad de los títulos, por ejemplo.

# ¿Qué tipo de dato es la columna “release_year”? ¿Lo puedes convertir a integer?
print("Tipo de dato de 'release_year':", df['release_year'].dtype)

# La columna “listed_in” contiene diferentes valores separados por coma, ¿Puedes crear una columna y quedarte con el primer valor?
print("Primeros 5 valores de 'main_genre':")
print(df['main_genre'].head())
