import pandas as pd

def comparar_datasets(df_emp, df_usr):
    """
    Compara empleados vs usuarios LMS y genera:
    - nuevos usuarios
    - usuarios a eliminar
    - usuarios a modificar
    """

    # Renombrar columnas para hacer match
    df_emp = df_emp.rename(columns={
        "Cod. Empleado": "codigo"
    })

    df_usr = df_usr.rename(columns={
        "Código empleado": "codigo"
    })

    # Asegurar que el tipo sea numérico para comparar
    df_emp["codigo"] = pd.to_numeric(df_emp["codigo"], errors="coerce")
    df_usr["codigo"] = pd.to_numeric(df_usr["codigo"], errors="coerce")

    # USUARIOS A CREAR
    nuevos = df_emp[~df_emp["codigo"].isin(df_usr["codigo"])].copy()

    # USUARIOS A ELIMINAR
    eliminar = df_usr[~df_usr["codigo"].isin(df_emp["codigo"])].copy()

    # USUARIOS EN COMÚN
    df_merge = df_emp.merge(
        df_usr,
        on="codigo",
        how="inner",
        suffixes=("_emp", "_usr")
    )

    # Normalización para comparación
    def normalizar_texto(s):
        return s.astype(str).str.strip().str.lower()

    # Email
    df_merge["email_diff"] = (
        normalizar_texto(df_merge["Correo electrónico interno"]) !=
        normalizar_texto(df_merge["Email"])
    )

    # Teléfono
    df_merge["tel_diff"] = (
        normalizar_texto(df_merge["Teléfono_emp"]) !=
        normalizar_texto(df_merge["Teléfono_usr"])
    )

    # Unidad vs Departamento
    df_merge["unidad_diff"] = (
        normalizar_texto(df_merge["Unidad"]) !=
        normalizar_texto(df_merge["Departamento El Salvador"])
    )

    # Centro de trabajo vs Sucursal
    df_merge["centro_diff"] = (
        normalizar_texto(df_merge["Centro de trabajo"]) !=
        normalizar_texto(df_merge["Sucursales El Salvador"])
    )

    # Filtrar las modificaciones
    cambios = df_merge[
        df_merge[
            ["email_diff", "tel_diff", "unidad_diff", "centro_diff"]
        ].any(axis=1)
    ].copy()

    # COLUMNAS FINALES MODIFICADOS
    modificados = cambios[[
        "codigo",
        "Usuario_emp",
        "Correo electrónico interno",
        "Email",
        "Teléfono_emp",
        "Teléfono_usr",
        "Unidad",
        "Departamento El Salvador",
        "Centro de trabajo",
        "Sucursales El Salvador",
        "email_diff",
        "tel_diff",
        "unidad_diff",
        "centro_diff"
    ]].copy()

    # Renombrar para claridad
    modificados.rename(columns={
        "Usuario_emp": "Usuario",
        "Correo electrónico interno": "Email_empleado",
        "Email": "Email_LMS",
        "Teléfono_emp": "Telefono_empleado",
        "Teléfono_usr": "Telefono_LMS"
    }, inplace=True)

    return nuevos, eliminar, modificados