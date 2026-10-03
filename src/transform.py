import pandas as pd

def _limpiar_tabla(nombre: str, df: pd.DataFrame) -> pd.DataFrame:
    df_clean = df.copy()

    # 1. Estandarizar nombres de columnas
    df_clean.columns = [c.strip().lower().replace(" ", "_") for c in df_clean.columns]

    # 2. Unicidad
    antes = len(df_clean)
    df_clean = df_clean.drop_duplicates()
    print(f" [{nombre}] duplicados eliminados: {antes - len(df_clean)}")

    # 3. Limpiar textos (sin convertir los nulos en el texto "nan")
    for col in df_clean.select_dtypes(include=["object"]).columns:
        df_clean[col] = df_clean[col].str.strip()

    # 4. Completitud
    print(f" [{nombre}] nulos totales: {int(df_clean.isnull().sum().sum())}")
    print(f" [{nombre}] registros finales: {len(df_clean)}")
    return df_clean

def transformar_datos(tablas: dict) -> dict:
    print("\n--- [FASE 2: TRANSFORMACION Y CALIDAD] ---")
    return {nombre: _limpiar_tabla(nombre, df) for nombre, df in tablas.items()}