# Ejercicios de Refuerzo: SQL (DDL y DML)

Para asegurar conceptos, vamos a trabajar con un escenario nuevo: **Una Empresa**.
Necesitamos gestionar **DEPARTAMENTOS** y **EMPLEADOS**.

---

### Ejercicio 1: Crear Tablas (DDL)

1.  Crea la tabla **DEPARTAMENTOS**.
    *   `ID_Dep`: Entero, PK, Autoincremental.
    *   `Nombre`: Texto (max 50), Obligatorio.
    *   `Ubicacion`: Texto (max 50).

> **Tu Respuesta:**
> ```sql
CREATE TAble DEPARTAMENTOS(
    ID_Dep INT AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Ubicacion VARCHAR(50),

    PRIMARY KEY (ID_Dep) -- ❌ QUITAR LA COMA FINAL. El último elemento no lleva coma.
);
> 
> ```

2.  Crea la tabla **EMPLEADOS**.
    *   `ID_Emp`: Entero, PK.
    *   `Nombre`: Texto (max 100).
    *   `Salario`: Decimal (con 2 decimales).
    *   `Fecha_Alta`: Fecha.
    *   `ID_Dep`: Entero (FK que une con DEPARTAMENTOS).

> **Tu Respuesta:**
> ```sql
CREATE TABLE EMPLEADOS(
    ID_Emp INT PRIMARY KEY, -- ✅ CORRECCIÓN: La clave primaria es el ID del empleado, no el departamentos.
    Nombre VARCHAR(100),
    salario DECIMAL(10,2),
    Fecha_Alta DATE,
    ID_Dep INT, -- El tipo debe coincidir con la otra tabla
    FOREIGN KEY (ID_Dep) REFERENCES DEPARTAMENTOS(ID_Dep)
);
> 
> ```

---

### Ejercicio 2: Insertar Datos (INSERT)

1.  Inserta un departamento llamado "Ventas" en "Madrid".
2.  Inserta un empleado llamado "Laura" con un salario de 1500.50, fecha de alta hoy (2025-01-27) y que pertenezca al departamento anterior (asumimos ID 1).

> **Tu Respuesta:**
> ```sql
-- ❌ ERROR: Es 'INSERT INTO', no 'INSERT FROM'.
-- Además, si ID_Dep es automático, hay que especificar las columnas.
INSERT INTO DEPARTAMENTOS (Nombre, Ubicacion) VALUES ('Ventas', 'Madrid');

-- ❌ ERROR: Tabla 'empleado' (debe ser EMPLEADOS). Faltan columnas (ID_Emp).
INSERT INTO EMPLEADOS (ID_Emp, Nombre, Salario, Fecha_Alta, ID_Dep) 
VALUES (1, 'Laura', 1500.50, '2025-01-27', 1);
> 
> ```

---

### Ejercicio 3: Consultas (SELECT)

1.  Selecciona el **Nombre** y **Salario** de todos los empleados.
> **Tu Respuesta:**
> ```sql
SELECT Nombre, salario FROM EMPLEADOS; -- ❌ ERROR: Se separan con comas (,), no con 'and'.
> 
> ```

2.  Selecciona todos los datos de los empleados que ganen **más de 1200**.
> **Tu Respuesta:**
> ```sql
`SELECT * FROM EMPLEADOS WHERE Salario > 1200;
> 
> ```

---

### Soluciones (¡Inténtalo primero!)

<details>
<summary>Ver Soluciones</summary>

**Ejercicio 1**
```sql
CREATE TABLE DEPARTAMENTOS (
    ID_Dep INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Ubicacion VARCHAR(50)
);

CREATE TABLE EMPLEADOS (
    ID_Emp INT PRIMARY KEY,
    Nombre VARCHAR(100),
    Salario DECIMAL(10, 2),
    Fecha_Alta DATE,
    ID_Dep INT,
    FOREIGN KEY (ID_Dep) REFERENCES DEPARTAMENTOS(ID_Dep)
);
```

**Ejercicio 2**
```sql
INSERT INTO DEPARTAMENTOS (Nombre, Ubicacion) VALUES ('Ventas', 'Madrid');

INSERT INTO EMPLEADOS (ID_Emp, Nombre, Salario, Fecha_Alta, ID_Dep) 
VALUES (1, 'Laura', 1500.50, '2025-01-27', 1);
```

**Ejercicio 3**
1. `SELECT Nombre, Salario FROM EMPLEADOS;`
2. `SELECT * FROM EMPLEADOS WHERE Salario > 1200;`

</details>
