import sqlite3
import os

# Nombre de la base de datos
DB_NAME = "taller_sql.db"

# Borramos la BD si existe para empezar limpio cada vez
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

print("--- TALLER DE SQL: CONSTRUYENDO LA BASE DE DATOS ---")
conexion = sqlite3.connect(DB_NAME)
cursor = conexion.cursor()

# ==========================================
# EJERCICIO 1: CREACIÓN DE TABLAS (DDL)
# ==========================================
print("\n1. Creando Tablas...")

# TAREA: Define aquí la sentencia SQL para crear la tabla CLIENTES
# - ID_Cliente (Entero, Primary Key)
# - Nombre (Texto, Not Null)
# - Ciudad (Texto)
sql_crear_clientes = """
CREATE TABLE CLIENTES (
    ID_Cliente INTEGER PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Ciudad VARCHAR(50)
);
"""

try:
    cursor.execute(sql_crear_clientes)
    print("✅ Tabla CLIENTES creada.")
except Exception as e:
    print(f"❌ Error creando CLIENTES: {e}")

# ==========================================
# EJERCICIO 2: INSERTAR DATOS (DML)
# ==========================================
print("\n2. Insertando Datos...")

# TAREA: Inserta un cliente: "Empresa A" de "Gijón"
sql_insertar_1 = """
INSERT INTO CLIENTES(Nombre, Ciudad) VALUES ('Empresa A', 'Gijón');
"""

# TAREA EXTRA: INSERTAR MÁS DATOS
# En SQL, para insertar varios a la vez se separan por comas:
sql_insertar_varios = """
INSERT INTO CLIENTES (Nombre, Ciudad) VALUES 
    ('Empresa B', 'Avilés'),
    ('Empresa C', 'Sevilla'),
    ('Empresa D', 'Sevilla'),
    ('Empresa E', 'Vigo');
"""

try:
    cursor.execute(sql_insertar_1)
    cursor.execute(sql_insertar_varios) # <-- DESCOMENTADO PARA QUE FUNCIONE
    print("✅ Clientes insertados.")
except Exception as e:
    print(f"❌ Error insertando: {e}")

# ==========================================
# EJERCICIO 3: CONSULTAS (SELECT)
# ==========================================
print("\n3. Consultando Datos...")

# TAREA 1: Selecciona TODO de la tabla CLIENTES
sql_select_todos = "SELECT * FROM CLIENTES"

print(f"Ejecutando: {sql_select_todos}")
cursor.execute(sql_select_todos)
resultados = cursor.fetchall()

print("--- Todos los Clientes ---")
for fila in resultados:
    print(fila)

# TAREA 2: CONSULTA CON FILTRO (WHERE)
# Instrucciones: Selecciona solo los clientes de una ciudad específica.
sql_where = """
SELECT Ciudad From Clientes WHERE Ciudad = "Sevilla";
"""

print("\n--- Resultados del Filtro (Pendiente) ---")
cursor.execute(sql_where)      # <-- DESCOMENTAR CUANDO ESTÉ LISTO EL WHERE
resultados_filtro = cursor.fetchall()
for fila in resultados_filtro:
    print(fila)

# Cierre
conexion.commit()
conexion.close()
