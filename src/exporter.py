import pandas as pd
import os

def exportar_resultados(nuevos, eliminar, modificar, ruta_salida="data/output"):
    """
    Exporta los resultados a archivos Excel
    """

    # Crear directorio si no existe
    os.makedirs(ruta_salida, exist_ok=True)

    nuevos.to_excel(
        f"{ruta_salida}/nuevos_usuarios.xlsx",
        index=False
    )

    eliminar.to_excel(
        f"{ruta_salida}/usuarios_eliminar.xlsx",
        index=False
    )

    modificar.to_excel(
        f"{ruta_salida}/usuarios_modificar.xlsx",
        index=False
    )