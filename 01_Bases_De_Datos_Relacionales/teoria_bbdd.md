# Lección 1: Teoría de Bases de Datos Relacionales
## Certificado IFCD0112 - Preparación Examen

### 1. Conceptos Básicos

**Dato vs. Información**: Un dato es un hecho aislado (ej. "25"), mientras que la información es el dato procesado y con contexto (ej. "25 grados centígrados").
**Sistema Gestor de Bases de Datos (SGBD/DBMS)**: Software que permite definir, crear, mantener y controlar el acceso a la base de datos.
**Base de Datos Relacional**: Tipo de BD que almacena datos en tablas relacionadas entre sí. Basada en el álgebra relacional (E.F. Codd).

### 2. El Modelo Relacional

**Estructura**:
*   **Tabla (Relación)**: Conjunto de datos organizados en filas y columnas.
*   **Registro (Tupla/Fila)**: Representa una instancia única de un objeto (ej. un alumno concreto).
*   **Campo (Atributo/Columna)**: Característica o propiedad de la entidad (ej. nombre, edad).

**Claves (Keys)**:
*   **Clave Primaria (Primary Key - PK)**: Identificador único de cada fila. No puede ser NULL y debe ser única.
*   **Clave Candidata**: Cualquier columna que podría ser PK.
*   **Clave Foránea (Foreign Key - FK)**: Columna que crea una relación entre dos tablas, apuntando a la PK de otra tabla.
*   **Clave Compuesta**: PK formada por dos o más columnas.

### 3. Relaciones entre Tablas (Cardinalidad)

*   **1:1 (Uno a Uno)**: Un registro de la Tabla A se relaciona con uno de la Tabla B. (Ej. Persona - DNI).
*   **1:N (Uno a Muchos)**: Un registro de A, se relaciona con varios de B. (Ej. Cliente - Pedidos). *Es la más común*.
*   **N:M (Muchos a Muchos)**: Varios registros de A se relacionan con varios de B. (Ej. Alumno - Asignaturas). *Requiere una tabla intermedia (pivote)*.

### 4. Integridad de Datos

*   **Integridad de Entidad**: La PK identifica unívocamente cada fila.
*   **Integridad Referencial**: Una FK debe coincidir con una PK existente o ser NULL. Evita registros "huérfanos".
*   **Integridad de Dominio**: Los valores en una columna deben ajustarse al tipo de dato y restricciones definidas.

### 5. Normalización

Proceso para organizar los datos y reducir la redundancia.
*   **1FN (Primera Forma Normal)**: 
    *   Eliminar grupos repetitivos.
    *   Todos los atributos deben ser atómicos (indivisibles).
*   **2FN (Segunda Forma Normal)**: 
    *   Estar en 1FN.
    *   Todo atributo no clave debe depender de *toda* la Clave Primaria (eliminar dependencias parciales).
*   **3FN (Tercera Forma Normal)**: 
    *   Estar en 2FN.
    *   No deben existir dependencias transitivas (un atributo no clave no debe depender de otro atributo no clave).

### 6. Introducción a SQL

*   **DDL (Data Definition Language)**: Estructura. `CREATE`, `ALTER`, `DROP`.
*   **DML (Data Manipulation Language)**: Datos. `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
