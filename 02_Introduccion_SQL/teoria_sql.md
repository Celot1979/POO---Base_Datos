# Lección 2: Introducción a SQL (DDL y DML Básico)
## Certificado IFCD0112 - Preparación Examen

SQL (*Structured Query Language*) es el lenguaje estándar para hablar con bases de datos relacionales.

### 1. Tipos de Datos Comunes (MySQL/Standard)

Al crear una tabla, debemos decir qué tipo de dato guardará cada columna:

*   **INT / INTEGER**: Números enteros (ej. edad, cantidad, ID).
*   **VARCHAR(n)**: Texto de longitud variable hasta *n* caracteres (ej. nombre, dirección).
*   **DECIMAL(p, s)**: Números exactos con decimales. *p* = total dígitos, *s* = decimales (ej. precios).
*   **DATE**: Fechas (AAAA-MM-DD).
*   **BOOLEAN**: Verdadero/Falso (a veces se usa TINYINT(1)).

### 2. DDL - Data Definition Language (Estructura)

Comandos para definir el esqueleto de la base de datos.

#### CREATE TABLE
Crea una nueva tabla.
```sql
CREATE TABLE NombreTabla (
    Columna1 TipoDato RESTRICCIONES,
    Columna2 TipoDato,
    ...
    PRIMARY KEY (Columna1),
    FOREIGN KEY (Columna2) REFERENCES OtraTabla(SuPK)
);
```

**Restricciones comunes:**
*   `NOT NULL`: Obligatorio, no puede estar vacío.
*   `UNIQUE`: No se puede repetir en toda la columna.
*   `AUTO_INCREMENT` (MySQL): El número sube solo (1, 2, 3...) ideal para IDs.

#### DROP TABLE
Elimina una tabla **y todos sus datos** (¡Cuidado!).
```sql
DROP TABLE NombreTabla;
```

### 3. DML - Data Manipulation Language (Datos)

#### INSERT (Insertar datos)
```sql
-- Insertar especificando columnas (Recomendado)
INSERT INTO Clientes (Nombre, Ciudad) VALUES ('Ana', 'Gijón');

-- Insertar varias filas a la vez
INSERT INTO Clientes (Nombre, Ciudad) VALUES 
('Pedro', 'Oviedo'),
('Luis', 'Avilés');
```

#### SELECT (Consultar datos)
La orden más usada.
```sql
SELECT Columna1, Columna2 FROM NombreTabla WHERE Condición;
```

**Ejemplos:**
*   `SELECT * FROM Clientes;` (Trae todo).
*   `SELECT Nombre FROM Clientes WHERE Ciudad = 'Gijón';` (Filtra por ciudad).

### Resumen Visual

| Concepto | Comando SQL | Ejemplo 'Humano' |
| :--- | :--- | :--- |
| **Crear Estructura** | `CREATE TABLE` | "Construir una estantería nueva" |
| **Borrar Estructura** | `DROP TABLE` | "Tirar la estantería a la basura" |
| **Meter Datos** | `INSERT INTO` | "Poner un libro en la estantería" |
| **Leer Datos** | `SELECT` | "Buscar un libro en la estantería"|
