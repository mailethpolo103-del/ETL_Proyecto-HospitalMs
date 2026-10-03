from src.extract import extraer_datos
from src.transform import transformar_datos
from src.load import cargar_datos

def ejecutar_pipeline():
    """
    Orquestador Principal: Coordina sincronicamente la ejecucion del pipeline ETL.
    """
    print("==================================================================")
    print("   INICIANDO PIPELINE ETL DE EXTREMO A EXTREMO: HOSPITAL DATA")
    print("==================================================================")
    
    try:
        # 1. Fase de Extraccion
        df_raw = extraer_datos()
        
        # 2. Fase de Transformacion y Calidad
        df_clean = transformar_datos(df_raw)
        
        # 3. Fase de Carga e Idempotencia
        cargar_datos(df_clean)
        
        print("\n==================================================================")
        print("   PIPELINE FINALIZADO EXITOSAMENTE SIN ERRORES")
        print("==================================================================")
        
    except Exception as error:
        print(f"\n[ERROR CRITICO]: Fallo la ejecucion del pipeline. Detalle: {error}")

if __name__ == "__main__":
    ejecutar_pipeline()