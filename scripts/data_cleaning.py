import pandas as pd
from sklearn.preprocessing import StandardScaler

# Función para cargar datasets
def cargar_datasets(red_path, white_path, delimiter=';'):
    df_red = pd.read_csv(red_path, delimiter=delimiter)
    df_white = pd.read_csv(white_path, delimiter=delimiter)
    return df_red, df_white

# Función para detectar y eliminar valores nulos
def limpiar_valores_nulos(df):
    return df.dropna()

# Función para imputar valores nulos con la media (opcional)
def imputar_valores_nulos(df):
    return df.fillna(df.mean())

# Función para detectar outliers usando IQR
def detectar_outliers(df, columna):
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[columna] < (Q1 - 1.5 * IQR)) | (df[columna] > (Q3 + 1.5 * IQR))]
    return outliers

# Función para eliminar outliers
def eliminar_outliers(df, columna):
    outliers = detectar_outliers(df, columna)
    df_clean = df[~df.index.isin(outliers.index)]
    return df_clean

# Función para estandarizar los datos
def estandarizar_datos(df, columnas_numericas):
    scaler = StandardScaler()
    df_scaled = df.copy()
    df_scaled[columnas_numericas] = scaler.fit_transform(df[columnas_numericas])
    return df_scaled

# Función principal de limpieza
def limpiar_datos(red_path, white_path, red_output, white_output):
    # Cargar datasets
    df_red, df_white = cargar_datasets(red_path, white_path)
    
    # Limpiar valores nulos
    df_red_clean = limpiar_valores_nulos(df_red)
    df_white_clean = limpiar_valores_nulos(df_white)
    
    # Eliminar outliers en 'alcohol' (puedes elegir más columnas si es necesario)
    df_red_clean = eliminar_outliers(df_red_clean, 'alcohol')
    df_white_clean = eliminar_outliers(df_white_clean, 'alcohol')
    
    # Estandarizar columnas numéricas
    columnas_numericas = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 
                          'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']
    df_red_scaled = estandarizar_datos(df_red_clean, columnas_numericas)
    df_white_scaled = estandarizar_datos(df_white_clean, columnas_numericas)
    
    # Guardar datasets limpios
    df_red_scaled.to_csv(red_output, index=False)
    df_white_scaled.to_csv(white_output, index=False)
    print("Limpieza y estandarización completadas. Archivos guardados.")

# Ejecutar la limpieza (puedes cambiar las rutas según tu estructura)
if __name__ == "__main__":
    red_wine_path = r'C:\Users\BS\Downloads\wine_quality\data\raw\winequality-red.csv'
    white_wine_path = r'C:\Users\BS\Downloads\wine_quality\data\raw\winequality-white.csv'
    red_output_path = r'C:\Users\BS\Downloads\wine_quality\data\processed\winequality-red-clean.csv'
    white_output_path = r'C:\Users\BS\Downloads\wine_quality\data\processed\winequality-white-clean.csv'

    limpiar_datos(red_wine_path, white_wine_path, red_output_path, white_output_path)
