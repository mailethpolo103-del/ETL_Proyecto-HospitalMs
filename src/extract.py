import kagglehub
import pandas as pd
import os

def extraer_datos() -> dict:
    """
    Descarga el dataset de Kaggle y lee todos los archivos CSV encontrados,
    retornando un diccionario de DataFrames {nombre_tabla: df}.
    """
    print("\n--- [FASE 1: EXTRACCIÓN] ---")
    print("Descargando dataset relacional desde Kaggle...")
    
    try:
        folder_path = kagglehub.dataset_download("kanakbaghel/hospital-management-dataset")
        print(f"Ruta de descarga local: {folder_path}")
        
        tablas = {}
        for archivo in os.listdir(folder_path):
            if archivo.endswith(".csv"):
                nombre_tabla = archivo.replace(".csv", "")
                ruta_csv = os.path.join(folder_path, archivo)
                df = pd.read_csv(ruta_csv)
                tablas[nombre_tabla] = df
                print(f" -> Tabla '{nombre_tabla}' cargada: {len(df)} registros, {len(df.columns)} columnas.")
        
        return tablas
        
    except Exception as e:
        print(f"Error crítico en la extracción: {e}")
        raise e