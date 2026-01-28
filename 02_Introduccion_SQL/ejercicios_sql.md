# Lección 2: Ejercicios de SQL
## Práctica de Escritura de Código (DDL y DML)

Para estos ejercicios, usaremos el esquema que diseñamos en la lección anterior (Clientes, Productos y Pedidos).

### Ejercicio 1: Crear Tablas (DDL)

Escribe la sentencia SQL completa para crear la tabla **CLIENTES**. 
*   **Requisitos**:
    *   `ID_Cliente`: Entero, Clave Primaria, Autoincremental.
    *   `Nombre`: Texto (max 100 letras), Obligatorio.
    *   `Ciudad`: Texto (max 50 letras).

> **Tu Respuesta (Escribe el código SQL abajo):**
> ```sql
 CREATE TABLE CLIENTES (
    ID_Cliente INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Ciudad VARCHAR(50)
 ); ✅ **CORRECTO**
> 
> ```

Escribe la sentencia SQL para crear la tabla **PEDIDOS**.
*   **Requisitos**:
    *   `ID_Pedido`: Entero, PK.
    *   `Fecha`: Tipo Fecha.
    *   `ID_Cliente`: Entero (Debe ser FK que apunte a la tabla CLIENTES).

> **Tu Respuesta:**
> ```sql
CREATE TABLE pedidos(
    ID_Pedido INT,
    fecha DATE, -- ❌ CORRECCIÓN: El tipo es DATE, no DATA
    ID_Cliente INT,

    PRIMARY KEY (ID_Pedido),
    FOREIGN KEY (ID_Cliente) REFERENCES CLIENTES(ID_Cliente) -- ✅ CORRECTO
);
> 
> ```

---

### Ejercicio 2: Insertar Datos (INSERT)

Escribe el SQL para insertar a estos dos clientes en la tabla `CLIENTES`:
1.  Nombre: "Empresa A", Ciudad: "Gijón"
2.  Nombre: "Juan Pérez", Ciudad: "Oviedo"

> **Tu Respuesta:**
> ```sql
-- ✅ CORRECTO. (Nota: En SQL estándar es mejor usar comillas simples ' ')
INSERT INTO Clientes(Nombre,Ciudad) VALUES
('Empresa A', 'Gijon'),
('Juan Pérez', 'Oviedo');
> 
> ```

---

### Ejercicio 3: Consultar Datos (SELECT)

1.  Escribe una consulta para obtener **todos** los datos de todos los clientes.
> **Tu Respuesta:**
> ```sql
> SELECT FROM * clientes; ❌ **MAL ORDEN**. Correcto: SELECT * FROM clientes;
> ```

2.  Escribe una consulta para obtener solo el **Nombre** de los clientes que sean de **'Gijón'**.
> **Tu Respuesta:**
> ```sql
SELECT Nombre FROM clientes WHERE ciudad = 'Gijón'; ✅ **CORRECTO**
> 
> ```

---

### Soluciones (Intenta hacerlo antes de mirar)

#### Ejercicio 1
```sql
CREATE TABLE CLIENTES (
    ID_Cliente INT AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Ciudad VARCHAR(50),
    PRIMARY KEY (ID_Cliente)
);

CREATE TABLE PEDIDOS (
    ID_Pedido INT,
    Fecha DATE,
    ID_Cliente INT,
    PRIMARY KEY (ID_Pedido),
    FOREIGN KEY (ID_Cliente) REFERENCES CLIENTES(ID_Cliente)
);
```

#### Ejercicio 2
```sql
INSERT INTO CLIENTES (Nombre, Ciudad) VALUES 
('Empresa A', 'Gijón'),
('Juan Pérez', 'Oviedo');
```

#### Ejercicio 3
1. `SELECT * FROM CLIENTES;`
2. `SELECT Nombre FROM CLIENTES WHERE Ciudad = 'Gijón';`
