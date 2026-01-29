"""
TALLER SQL 2: ESTRUCTURA DESDE CERO
-----------------------------------
Objetivo: Crear una estructura modular separando la lógica de la base de datos.
Este archivo actuará como nuestro "Módulo de Base de Datos" (Modelo/Infraestructura).

PASOS:
1. Importar librería sqlite3
2. Definir nombre de la BB.DD.
3. Crear función para conectar
4. Crear tablas
...
"""
# ¡TODO TUYO! Empieza importando y definiendo la conexión...
import sqlite3
import os
# ==========================================
# 3. TABLA TIENDA
# ==========================================
DB_Name = "TIENDA.db"
# Esto es para si la base de datos ya existe la borre.
if os.path.exists(DB_Name):
    os.remove(DB_Name)

conexion = sqlite3.connect(DB_Name)
cursor = conexion.cursor()

Tabla_Clientes = """
CREATE TABLE CLIENTES (
    ID_Cliente INTEGER PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Email VARCHAR(100),
    Ciudad VARCHAR(50)
);
"""
try:
    cursor.execute(Tabla_Clientes)
except Exception as e:
     print(f"❌ Error creando CLIENTES: {e}")

# ==========================================
# 3. TABLA PEDIDOS 
# ==========================================

DB_Name_Pedidos = "PEDIDOS.db"

Tabla_Pedidos= """
CREATE TABLE PEDIDOS (
    ID_Pedido INTEGER PRIMARY KEY,
    Fecha DATE,
    ID_Cliente INT,
    
    FOREIGN KEY ( ID_Cliente) REFERENCES CLIENTES(ID_Cliente )
    
);
"""

try:
    cursor.execute(Tabla_Pedidos)
except Exception as e:
     print(f"❌ Error creando CLIENTES: {e}")

# ==========================================
# 3. TABLA PRODUCTOS
# ==========================================
# Reto Final DDL: ID_Producto (PK), Nombre, Precio (REAL/FLOAT), Stock (INTEGER)
Tabla_Productos = """
     CREATE TABLE PRODUCTOS(
        ID_Producto INTEGER PRIMARY KEY,
        Nombre VARCHAR (50),
        Precio FLOAT,
        Stock INTEGER
     );

"""
cursor.execute(Tabla_Productos)

# ==========================================
# 4. INSERTAR DATOS
# ==========================================
# Misión 1: Insertar 3 Clientes (Recuerda: Nombre, Email, Ciudad)
sql_insertar_clientes = """
INSERT INTO CLIENTES (Nombre, Email, Ciudad) VALUES
    ('Daniel', 'daniel@email.com', 'Avilés'),
    ('Sandra', 'sandra@email.com', 'Oviedo'),
    ('Rafaela', 'rafaela@email.com', 'Cudillero');
"""
cursor.execute(sql_insertar_clientes)

# Misión 2: Insertar 3 Productos (Nombre, Precio, Stock)
sql_insertar_productos = """
INSERT INTO PRODUCTOS (Nombre, Precio, Stock) VALUES
    ('Plátano', 1.25, 600),
    ('Sandia', 8.0, 300),
    ('Manzanas', 2.58, 500);
"""
cursor.execute(sql_insertar_productos)

# Misión 3: Insertar 2 Pedidos (Fecha, ID_Cliente)
# ¡OJO! El ID_Cliente tiene que existir en la tabla de arriba (ej. 1, 2 o 3)
# Formato Fecha: 'YYYY-MM-DD' (ej. '2024-01-30')
sql_insertar_pedidos = """
INSERT INTO PEDIDOS(Fecha, ID_Cliente) VALUES
    ('2021-03-21', 1),
    ('2025-02-21', 3);
"""
cursor.execute(sql_insertar_pedidos)


# ==========================================
# 5. CONSULTAS (SELECT)
# ==========================================
print("\n--- CONSULTAS ---")

# Misión 1: Listar todos los productos que tengan un stock menor a 600
sql_stock_bajo = """

    SELECT Nombre FROM PRODUCTOS WHERE Stock < 600;
"""
cursor.execute(sql_stock_bajo)
resultados = cursor.fetchall()
for fila in resultados:
    print(f"Producto bajo stock: {fila}")


# Misión 2: Obtener los pedidos del Cliente con ID 1
sql_pedidos_cliente = """
SELECT * FROM PEDIDOS WHERE ID_Cliente = 1;
"""
cursor.execute(sql_pedidos_cliente)
resultados = cursor.fetchall()
for fila in resultados:
   print(f"Pedido del cliente 1: {fila}")


conexion.commit()
print("¡Base de Datos generada con éxito!")
# print("Datos insertados correctamente") # <-- Descomentar al final
conexion.close()