import pandas as pd

def limpiar_usuarios_lms(df):
    """
    Limpia y normaliza el reporte de usuarios del LMS
    """

    # Filtrar solo usuarios activos
    # df = df[df["Activo"] == "Sí"]

    # Filtrar solo de El Salvador
    df = df[df["País"] == "El Salvador"].copy()

    # Extraer código de empleado del usuario (es10065 → 10065)
    df["Código empleado"] = df["Usuario"].str.extract(r'(\d+)')
    df["Código empleado"] = pd.to_numeric(df["Código empleado"], errors='coerce')

    # Selección de columnas
    df_limpio = df[[
        "Código empleado",
        "Usuario",
        "Nombre y apellido",
        "Email",
        "Teléfono",
        "Activo",
        "País",
        "Sucursales El Salvador",
        "Departamento El Salvador"
    ]].copy()

    return df_limpio

def limpiar_empleados(df):
    """
    Limpia la base de empleados
    """

    # Hacer copia para evitar SettingWithCopyWarning
    df = df.copy()
    
    # Normalizar código
    df["Cod. Empleado"] = pd.to_numeric(df["Cod. Empleado"], errors='coerce')

    # Separar nombre y apellido
    nombres = df["Apellidos y nombres"].str.split(", ", expand=True)
    df["Apellido"] = nombres[0].str.strip()
    df["Nombre"] = nombres[1].str.strip()

    # Limpiar teléfono
    df["Teléfono"] = df["Teléfono móvil"].str.replace("-", "", regex=False).str.strip()
    df["Teléfono"] = "503" + df["Teléfono"]
    
    # Crear username del LMS
    df["Usuario"] = "es" + df["Cod. Empleado"].astype(str)

    UNIDADES = [
        "Ferretería",
        "Tornillería",
        "Herramientas",
        "Eléctrico",
        "Administración Sucursales",
        "Automotriz",
        "Pinturas",
        "Fontanería",
        "Industrial"
    ]
    
    # Filtrar solo empleados de las unidades relevantes
    df = df[df["Unidad"].isin(UNIDADES)].copy()

    # Filtro especial para Gerencias
    PLAZAS_GERENCIAS = [
        "Gerente de Sucursal",
        "Subgerente de Sucursal",
        "Coordinador(a) de Sucursal",
        "District Manager"
    ]
    
    # Separar en dos grupos
    df_admin = df[df["Unidad"] == "Administración Sucursales"].copy()
    df_otros = df[df["Unidad"] != "Administración Sucursales"].copy()
    
    # Filtrar SOLO dentro de administración
    df_admin = df_admin[
        df_admin["Plaza"].str.startswith(tuple(PLAZAS_GERENCIAS), na=False)
    ]

    # Unir nuevamente
    df = pd.concat([df_otros, df_admin], ignore_index=True)

    # Seleccionar columnas
    df_limpio = df[[
        "Cod. Empleado",
        "Usuario",
        "Apellido",
        "Nombre",
        "Correo electrónico interno",
        "Teléfono",
        "Fecha de inicio de contrato",
        "Fecha de nacimiento",
        "Centro de trabajo",
        "Estado",
        "Unidad",
        "Plaza",
        "Fecha de retiro"
    ]].copy()
    
    return df_limpio