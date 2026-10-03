import os
from sqlalchemy import create_engine

def cargar_datos(tablas: dict, db_filename: str = "hospital.db"):
    print("\n--- [FASE 3: CARGA E IDEMPOTENCIA] ---")

    data_dir = os.path.join(os.getcwd(), "data")
    os.makedirs(data_dir, exist_ok=True)

    engine = create_engine(f"sqlite:///{os.path.join(data_dir, db_filename)}")

    # if_exists="replace" hace la carga idempotente: re-ejecutar no duplica filas
    for nombre, df in tablas.items():
        df.to_sql(name=nombre, con=engine, if_exists="replace", index=False)
        print(f" -> Tabla '{nombre}' cargada: {len(df)} registros")

    print(f"Carga finalizada. Base de datos en: data/{db_filename}")