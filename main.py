from src.loaders import cargar_datos
from src.cleaners import limpiar_empleados, limpiar_usuarios_lms
from src.comparator import comparar_datasets
from src.exporter import exportar_resultados

def main():
    df_emp_raw, df_usr_raw = cargar_datos()

    df_emp = limpiar_empleados(df_emp_raw)
    df_usr = limpiar_usuarios_lms(df_usr_raw)

    nuevos, eliminar, modificados = comparar_datasets(df_emp, df_usr)

    exportar_resultados(nuevos, eliminar, modificados)

if __name__ == "__main__":
    main()