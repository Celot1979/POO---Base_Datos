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
-- ESCRIBE TU CÓDIGO AQUÍ (borra esto)
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
"""

try:
    cursor.execute(sql_insertar_1)
    print("✅ Cliente 1 insertado.")
except Exception as e:
    print(f"❌ Error insertando: {e}")

# ==========================================
# EJERCICIO 3: CONSULTAS (SELECT)
# ==========================================
print("\n3. Consultando Datos...")

# TAREA: Selecciona TODO de la tabla CLIENTES
sql_select_todos = "SELECT * FROM CLIENTES" # Te regalo esta de ejemplo

print(f"Ejecutando: {sql_select_todos}")
cursor.execute(sql_select_todos)
resultados = cursor.fetchall()

print("--- Resultados ---")
for fila in resultados:
    print(fila)

# Cierre
conexion.commit()
conexion.close()
