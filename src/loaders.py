import pandas as pd
import os

# Configuración de rutas
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_PATH = os.path.join(BASE_PATH, "data", "raw")

# Funciones internas
def _leer_archivo(ruta):
    """
    Detecta automáticamente el tipo de archivo y lo carga
    """
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

    if ruta.endswith(".xlsx") or ruta.endswith(".xls"):
        return pd.read_excel(ruta)

    elif ruta.endswith(".csv"):
        return pd.read_csv(ruta)

    else:
        raise ValueError(f"Formato no soportado: {ruta}")

# Función principal
def cargar_datos(
    archivo_empleados="empleados.xlsx",
    archivo_usuarios="usuarios.xlsx"
):
    """
    Carga los datasets de empleados y usuarios LMS

    Retorna:
    - df_empleados_raw
    - df_usuarios_raw
    """

    ruta_empleados = os.path.join(RAW_PATH, archivo_empleados)
    ruta_usuarios = os.path.join(RAW_PATH, archivo_usuarios)

    # Leer archivos
    df_empleados = _leer_archivo(ruta_empleados)
    df_usuarios = _leer_archivo(ruta_usuarios)

    # Validación
    if df_empleados.empty:
        raise ValueError("El archivo de empleados está vacío")

    if df_usuarios.empty:
        raise ValueError("El archivo de usuarios está vacío")

    return df_empleados, df_usuarios