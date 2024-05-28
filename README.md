
# Proyecto de Limpieza y Transformación de Datos de Netflix

## Descripción del Proyecto

Este proyecto tiene como objetivo demostrar la capacidad de lidiar con “datos sucios” realizando la limpieza y transformación de un dataset de Netflix. El proceso incluye la eliminación de valores nulos, reemplazo de valores incompletos, conversión de tipos de datos y creación de nuevas características.

## Requisitos Previos

- Python 3.8 o superior
- Anaconda (opcional, recomendado)
- Las siguientes bibliotecas de Python:
  - pandas
  - numpy

## Instalación

### Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/netflix_data_cleaning.git
cd netflix_data_cleaning
Crear y Activar un Entorno Virtual
Usando Conda:

bash
Copiar código
conda create -n netflix_env python=3.8
conda activate netflix_env
Instalar las Dependencias
bash
Copiar código
pip install pandas numpy
Uso
Ejecutar el Script de Limpieza de Datos
Asegúrate de que el archivo netflix1.csv esté en el mismo directorio que el script data_cleaning.py. Luego, ejecuta el siguiente comando:

bash
Copiar código
python data_cleaning.py
Esto cargará el dataset, realizará la limpieza y transformación, y guardará el resultado en un nuevo archivo netflix_cleaned.csv.

Estructura del Proyecto
bash
Copiar código
netflix_data_cleaning/
│
├── netflix1.csv             # Dataset original
├── netflix_cleaned.csv      # Dataset limpio y transformado
├── data_cleaning.py         # Script de limpieza y transformación de datos
└── README.md                # Documentación del proyecto
Preguntas de Guía
¿Cuántos valores nulos encuentras en los datos? ¿Los puedes eliminar?
Se eliminaron todos los valores nulos del dataset.
¿Cuántos valores incompletos encuentras en los datos? ¿Los puedes reemplazar?
Los valores incompletos se eliminaron en este proyecto.
¿Podés eliminar columnas que no te aportan información? ¿Cuáles son? ¿Por qué las eliminarías?
No se eliminaron columnas en este proyecto, pero esto depende del análisis que se quiera realizar.
¿Qué tipo de dato es la columna “release_year”? ¿Lo podes convertir a integer?
La columna release_year se convirtió a tipo integer.
La columna “listed_in” contiene diferentes valores separados por coma, ¿Puedes ccrear una columna y quedarte con el primer valor?
Se creó una nueva columna main_genre que contiene el primer valor de listed_in.
Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para cualquier mejora o corrección.

Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

Contacto
Autor: José Miguel Henríquez Arrau
Email: jose.miguelhen@gmail.com
GitHub: josemiguelhen