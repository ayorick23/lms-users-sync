# ⚙️ LMS User Management Automation

Script de automatización en **Python** para el mantenimiento de usuarios en una plataforma **LMS**, que permite identificar de forma automática qué usuarios deben ser **creados, actualizados o eliminados**, a partir de la comparación entre la base de empleados y la base de usuarios del sistema.

El sistema genera reportes accionables y un registro detallado de cambios mediante logs, optimizando significativamente el tiempo de administración.

## 🚀 Descripción del proyecto

La administración manual de usuarios en plataformas LMS puede ser un proceso repetitivo, propenso a errores y altamente demandante en tiempo, especialmente cuando se manejan grandes volúmenes de colaboradores.

Este proyecto automatiza ese proceso mediante un script que:

1. Compara la base de empleados activa con la base de usuarios del LMS
2. Detecta diferencias entre ambos datasets
3. Clasifica los usuarios en tres categorías clave:
   - Usuarios a crear
   - Usuarios a eliminar
   - Usuarios a modificar

4. Genera reportes en Excel con acciones claras
5. Registra todas las operaciones mediante un sistema de logs

## 🧠 Problema que resuelve

Antes de esta solución:

- El mantenimiento de usuarios se realizaba manualmente
- Era difícil identificar diferencias entre bases de datos
- Existía riesgo de errores en la gestión de usuarios
- El proceso consumía una cantidad significativa de tiempo

Con este proyecto:

- La comparación de datos es automática
- Se generan listas claras de acciones a ejecutar
- Se reduce el riesgo de inconsistencias
- Se optimiza considerablemente el tiempo operativo

## ⚙️ Flujo del proceso

```text
Base de empleados        Base de usuarios LMS
        │                         │
        └──────────┬──────────────┘
                   ▼
        Comparación de datasets (Pandas)
                   ▼
        Clasificación de usuarios
                   ▼
   ┌──────────────┼──────────────┐
   ▼              ▼              ▼
Crear          Modificar       Eliminar
usuarios        usuarios       usuarios
   │              │              │
   └─────── Generación de reportes
                   ▼
              Sistema de logs
```

## 🛠️ Tecnologías utilizadas

- **Python**
- **Pandas**
- **Logging (Python logging module)**
- Procesamiento de archivos **Excel**

Este proyecto demuestra habilidades en **automatización de procesos, comparación de datasets y generación de reportes operativos**.

## 📁 Estructura del proyecto

```text
lms-user-management-automation
│
├── data/
│   ├── raw/
│   │   ├── empleados.xlsx
│   │   └── usuarios_lms.xlsx
│   │
│   └── output/
│       ├── usuarios_crear.xlsx
│       ├── usuarios_eliminar.xlsx
│       └── usuarios_modificar.xlsx
│
├── logs/
│   └── sync.log
│
├── src/
│   ├── loaders.py
│   ├── cleaners.py
│   ├── comparator.py
│   └── exporter.py
│
├── main.py
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md
```

## 🔍 Lógica de procesamiento

El sistema realiza una comparación estructurada entre dos fuentes de datos:

### 📥 Entrada

- Base de empleados (fuente oficial)
- Base de usuarios del LMS

### 🔄 Procesamiento

- Normalización de datos
- Comparación de registros
- Identificación de diferencias
- Clasificación de usuarios

### 📤 Salida

Se generan tres archivos principales:

- `usuarios_crear.xlsx`
- `usuarios_eliminar.xlsx`
- `usuarios_modificar.xlsx`

## ▶️ Ejecución

1. Colocar los archivos de entrada en la carpeta `raw/`

2. **Ejecutar el script:**

   ```bash
   python main.py
   ```

3. Revisar los resultados en la carpeta `output/`

## 📝 Sistema de Logs

El proyecto incluye un sistema de logging que permite monitorear y auditar el proceso.

El archivo de logs incluye:

- Usuarios detectados para creación
- Usuarios identificados para eliminación (colaboradores retirados)
- Cambios detectados en perfiles
- Eventos del proceso
- Posibles errores

Ubicación:

```text
logs/sync.log
```

## 📈 Impacto del proyecto

Este sistema permitió:

- Automatizar el mantenimiento de usuarios del LMS
- Reducir significativamente el tiempo de gestión manual
- Disminuir errores en la administración de usuarios
- Mejorar la trazabilidad de cambios mediante logs

## 🔧 Posibles mejoras futuras

- [ ] Integración directa con API del LMS
- [ ] Automatización completa (sin intervención manual)
- [ ] Validaciones avanzadas de calidad de datos
- [ ] Interfaz gráfica para usuarios no técnicos
- [ ] Programación periódica del proceso

## 👨‍💻 Autor

**Dereck Méndez**

Data Analyst | Business Intelligence | Python Automation

Especializado en la automatización de procesos operativos y análisis de datos para optimizar la toma de decisiones.
