import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Función para cargar datasets
def cargar_datos(file_path):
    return pd.read_csv(file_path)

# Función para entrenar modelos
def entrenar_modelos(X_train, y_train):
    # Modelo 1: Regresión Logística
    logreg = LogisticRegression(max_iter=1000)
    logreg.fit(X_train, y_train)
    
    # Modelo 2: Random Forest con pesos balanceados
    rf = RandomForestClassifier(class_weight='balanced', random_state=42)
    rf.fit(X_train, y_train)
    
    return logreg, rf

# Función para evaluar modelos
def evaluar_modelos(modelo, X_test, y_test):
    y_pred = modelo.predict(X_test)
    return classification_report(y_test, y_pred, zero_division=0)

# Ruta a los datos procesados
red_wine_path = r'C:\Users\BS\Downloads\wine_quality\data\processed\winequality-red-clean.csv'
white_wine_path = r'C:\Users\BS\Downloads\wine_quality\data\processed\winequality-white-clean.csv'

# Cargar datos
df_red = cargar_datos(red_wine_path)
df_white = cargar_datos(white_wine_path)

# Separar características y etiquetas
X_red = df_red.drop('quality', axis=1)
y_red = df_red['quality']
X_white = df_white.drop('quality', axis=1)
y_white = df_white['quality']

# Dividir datos en entrenamiento y prueba
X_train_red, X_test_red, y_train_red, y_test_red = train_test_split(X_red, y_red, test_size=0.3, random_state=42)
X_train_white, X_test_white, y_train_white, y_test_white = train_test_split(X_white, y_white, test_size=0.3, random_state=42)

# Entrenar modelos
logreg_red, rf_red = entrenar_modelos(X_train_red, y_train_red)
logreg_white, rf_white = entrenar_modelos(X_train_white, y_train_white)

# Evaluar modelos con zero_division=0 para evitar advertencias
print("Evaluación de Regresión Logística (Vino Tinto):")
print(evaluar_modelos(logreg_red, X_test_red, y_test_red))

print("Evaluación de Random Forest (Vino Tinto):")
print(evaluar_modelos(rf_red, X_test_red, y_test_red))

print("Evaluación de Regresión Logística (Vino Blanco):")
print(evaluar_modelos(logreg_white, X_test_white, y_test_white))

print("Evaluación de Random Forest (Vino Blanco):")
print(evaluar_modelos(rf_white, X_test_white, y_test_white))
