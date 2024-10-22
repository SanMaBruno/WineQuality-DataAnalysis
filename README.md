# Análisis de Calidad del Vino

## 📊 Descripción del Proyecto

Este proyecto tiene como objetivo analizar y predecir la calidad de los vinos tintos y blancos utilizando sus propiedades químicas. Hemos implementado tanto aprendizaje no supervisado (Clustering K-Means) como aprendizaje supervisado (Regresión Logística y Random Forest) para identificar los factores clave que influyen en la calidad del vino y proporcionar modelos predictivos.

El conjunto de datos proviene del UCI Machine Learning Repository, y contiene diversas mediciones químicas de muestras de vino. La variable objetivo es `quality`, que varía de 3 a 9, representando diferentes niveles de calidad del vino. El objetivo es utilizar estas características químicas para predecir la calidad del vino y proporcionar información sobre qué factores influyen más en esta calidad.

## 🎯 Objetivos

- Realizar un Análisis Exploratorio de Datos (EDA) para explorar el conjunto de datos y encontrar patrones.
- Aplicar Clustering K-Means para agrupar los vinos basados en sus características químicas.
- Entrenar y evaluar modelos supervisados (Regresión Logística y Random Forest) para predecir la calidad del vino.
- Comparar el rendimiento de los modelos y proporcionar información sobre el mejor modelo predictivo.
- Extraer conclusiones basadas en el análisis de datos y los resultados de los modelos.

## 📂 Estructura del Proyecto

El proyecto está organizado utilizando mejores prácticas, asegurando claridad y facilidad de mantenimiento:


```bash
wine_quality/
│
├── data/
│   ├── raw/                               # Archivos de datos sin procesar
│   │   ├── winequality-red.csv
│   │   ├── winequality-white.csv
│   │   └── winequality.names
│   └── processed/                         # Archivos de datos procesados
│       ├── winequality-red-clean.csv
│       └── winequality-white-clean.csv
│
├── notebooks/                             # Notebooks Jupyter para EDA y modelado
│   ├── eda.ipynb                          # Análisis Exploratorio de Datos
│   └── eda_and_modeling.ipynb             # Modelado y evaluación
│
├── scripts/                               # Scripts en Python para procesamiento y modelado
│   └── data_cleaning.py                   # Script para la limpieza y preprocesamiento de datos
│
├── outputs/                               # Visualizaciones generadas y resultados de modelos
│   ├── eda_visualizations.png             # Visualizaciones del EDA (distribuciones, correlaciones, etc.)
│   └── model_results.txt                  # Resultados de la evaluación de modelos (reportes de clasificación)
│
├── venv/                                  # Entorno virtual (si aplica)
│
├── README.md                              # Documentación del proyecto
└── requirements.txt                       # Dependencias necesarias para ejecutar el proyecto
```

## 📝 Metodología

### 1. Preprocesamiento de Datos

- El conjunto de datos sin procesar fue limpiado utilizando el script `data_cleaning.py`. Este script maneja la falta de datos, la normalización de las características y prepara el conjunto de datos para el análisis.
- Los archivos de datos procesados se almacenan en `data/processed/`:
  - `winequality-red-clean.csv`
  - `winequality-white-clean.csv`

### 2. Análisis Exploratorio de Datos (EDA)

- El EDA se realizó en el notebook `eda.ipynb`.
- Visualizaciones incluidas:
  - Gráficos de distribución de la calidad del vino.
  - Mapas de calor de correlaciones para identificar relaciones entre las características químicas y la calidad del vino.
  - Pairplots para examinar interacciones potenciales entre características.
- Principales conclusiones del EDA:
  - Los vinos con mayor contenido de alcohol tienden a tener mejores calificaciones de calidad.
  - La acidez volátil está correlacionada negativamente con la calidad del vino, especialmente en los vinos tintos.

### 3. Aprendizaje No Supervisado: Clustering K-Means

- Implementado en `eda_and_modeling.ipynb` utilizando el algoritmo de K-Means.
- El conjunto de datos fue estandarizado y los vinos fueron agrupados en clústeres basados en sus características químicas.
- Los clústeres formados revelaron agrupaciones naturales en los vinos, con algunos clústeres alineándose con vinos de mejor calidad.

### 4. Aprendizaje Supervisado: Regresión Logística y Random Forest

- Los modelos se entrenaron y evaluaron en `eda_and_modeling.ipynb`.
- Dos modelos fueron implementados:
  - Regresión Logística: Un modelo lineal para clasificación.
  - Random Forest: Un modelo de ensamble, que maneja mejor los datos desequilibrados y captura relaciones no lineales.
- Ambos modelos se entrenaron en los conjuntos de datos de vino tinto y blanco por separado, y se evaluaron sus rendimientos utilizando métricas como precisión, recall, F1-score y exactitud.

### 5. Evaluación de Modelos

- Random Forest mostró un mejor rendimiento general, especialmente en la predicción de clases minoritarias (vinos de mayor calidad) en comparación con la Regresión Logística.
- Los informes detallados de evaluación de los modelos, incluyendo métricas de clasificación, están almacenados en la carpeta `outputs/` como `model_results.txt`.

## ⚙️ Instrucciones de Configuración

1. Clona el repositorio:

```bash
git clone https://github.com/SanMaBruno/WineQuality-DataAnalysis.git
cd WineQuality-DataAnalysis
```

2.Crea y activa un entorno virtual:

# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate



3.Instala las dependencias:
pip install -r requirements.txt


## Ejecuta los notebooks

- Abre `notebooks/eda.ipynb` para el Análisis Exploratorio de Datos.
- Abre `notebooks/eda_and_modeling.ipynb` para el modelado y evaluación.

## 📈 Resultados y Conclusiones

### Rendimiento de Modelos (Modelos Supervisados):

| Modelo                          | Precisión | Recall | F1-Score | Exactitud |
|---------------------------------|-----------|--------|----------|-----------|
| Regresión Logística (Vino Tinto)| 68%       | 67%    | 67%      | 68%       |
| Random Forest (Vino Tinto)      | 74%       | 75%    | 74%      | 75%       |
| Regresión Logística (Vino Blanco)| 69%      | 68%    | 68%      | 70%       |
| Random Forest (Vino Blanco)     | 76%       | 74%    | 75%      | 76%       |

### Aprendizaje No Supervisado (Clustering K-Means):

El Clustering K-Means reveló grupos distintos en los datos de vino tinto y blanco. Algunos de estos clústeres se alinearon con vinos de mayor calidad, indicando que ciertas composiciones químicas se correlacionan fuertemente con la calidad del vino.

## 🔑 Principales Conclusiones

- Random Forest superó a la Regresión Logística, especialmente en la predicción de vinos con mayor calidad.
- El contenido de alcohol y la acidez volátil fueron los factores más influyentes en la determinación de la calidad del vino.
- El Clustering K-Means ayudó a identificar agrupaciones naturales de vinos basados en sus características químicas, alineándose con ciertos niveles de calidad.

## 🔧 Tecnologías Utilizadas

- Python 3.12
- Pandas, NumPy para la manipulación y análisis de datos
- Scikit-learn para los modelos de machine learning (Regresión Logística, Random Forest, K-Means)
- Seaborn, Matplotlib para visualizaciones de datos
- Jupyter Notebook para el análisis interactivo

## 🔗 Referencias

- [UCI Machine Learning Repository: Conjunto de datos sobre la calidad del vino](https://archive.ics.uci.edu/ml/datasets/Wine+Quality)
- [Documentación de Scikit-learn](https://scikit-learn.org/stable/)

## 👨‍💻 Autor

Bruno San Martín Navarro - [LinkedIn](https://www.linkedin.com) | [GitHub](https://github.com/SanMaBruno)

## 🚀 Trabajo Futuro

- Implementar ajuste de hiperparámetros para mejorar el rendimiento del modelo Random Forest.
- Explorar otros algoritmos de machine learning como Support Vector Machines (SVM) o Gradient Boosting.
- Aplicar técnicas de validación cruzada para asegurar la robustez del modelo.
- Integrar DataRobot para automatizar el machine learning (AutoML) y comparar los resultados con los modelos manuales.
