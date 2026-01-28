# Lección 1: Ejercicios de Bases de Datos Relacionales
## Preparación Examen 10 de Febrero

### Parte 1: Preguntas de Repaso (Simulacro Examen)

1.  **¿Cuál es la función principal de una Clave Primaria (PK)?**
    *   a) Relacionar dos tablas.
    *   b) Identificar de forma única cada registro en una tabla. ✅ **CORRECTO**
    *   c) Permitir valores nulos.
    *   d) Almacenar textos largos.

2.  **Si tenemos una relación N:M (Muchos a Muchos), ¿cómo la implementamos físicamente?**
    *   a) Poniendo la PK de una tabla en la otra.
    *   b) Creando una tercera tabla intermedia con las PK de ambas. ✅ **CORRECTO** (Efectivamente, tabla pivote)
    *   c) No se pueden implementar.
    *   d) Duplicando los datos en ambas tablas.

3.  **Para estar en Tercera Forma Normal (3FN), ¿qué condición se debe cumplir?**
    *   a) Eliminar dependencias transitivas. ✅ **CORRECTO** (Esta es la definición de 3FN).
    *   b) Eliminar grupos repetitivos. ❌ **INCORRECTO** (Esto es lo que se hace para llegar a la 1FN). 
    *   c) Eliminar dependencias parciales.
    *   d) Tener solo dos columnas.

4.  **¿Qué asegura la Integridad Referencial?**
    *   a) Que no haya datos duplicados.
    *   b) Que una FK siempre apunte a una PK válida o sea nula. ✅ **CORRECTO** 
    *   c) Que la base de datos sea rápida.
    *   d) Que todos los campos sean obligatorios.

---

### Parte 2: Ejercicios Prácticos

#### Ejercicio 1: Identificación de Relaciones
Determina la cardinalidad (1:1, 1:N, N:M) para los siguientes casos.
*Consejo: Pregúntate "¿Un [A] cuántos [B] puede tener?" y viceversa.*

1.  **Profesor** y **Departamento** (Un profesor pertenece a un solo departamento, un departamento tiene muchos profesores).
    > **Tu respuesta:** 1:N ✅ **CORRECTO**

2.  **Coche** y **Matrícula**.
    > **Tu respuesta:** 1:1 ✅ **CORRECTO**

3.  **Cliente** y **Producto** (En un contexto de compras históricas).
    > **Tu respuesta:** N:M ✅ **CORRECTO**

#### Ejercicio 2: Normalización (Guía Paso a Paso)

Vamos a normalizar esta tabla desnormalizada ("Gigante") de **PEDIDOS**:
`| ID_Pedido | Fecha | Cliente | Dirección_Cliente | Producto | Cantidad | Precio_Unitario |`

**Paso 1: Detectar el problema (¿Por qué está mal?)**
Imagina que el cliente "Juan" hace 100 pedidos. ¿Cuántas veces se repite su dirección en esta tabla? 100 veces. Eso es redundante y peligroso (si se muda, hay que cambiar 100 registros). 
Además, si un pedido tiene 3 productos, tendríamos que repetir la fecha y el cliente 3 veces (una por producto).

**Paso 2: Solución (Divide y vencerás)**
Vamos a separar los datos en cajitas (tablas) lógicas.

1.  **Datos del CLIENTE**: ¿Qué datos dependen SOLAMENTE del Cliente? (Sácalos a una tabla aparte).
    > *Tu propuesta (Tabla Clientes):*
    > *Campos:* ...

2.  **Datos del PRODUCTO**: ¿Qué datos son propios y fijos del producto?
    > *Tu propuesta (Tabla Productos):*
    > *Campos:* ...

3.  **Datos del PEDIDO (La Cabecera)**: ¿Qué datos son únicos del pedido en general (no cambian por producto)?
    > *Tu propuesta (Tabla Pedidos):*
    > *Campos:* ...

4.  **Datos del DETALLE (Las Líneas)**: ¿Qué queda? ¿Qué datos unen al pedido con el producto? (La cantidad comprada).
    > *Tu propuesta (Tabla Detalles):*
    > *Campos:* ...

---

### Soluciones (Para estudio personal)
🔻 *Despliega o baja solo cuando hayas intentado resolverlos* 🔻

**Parte 1**: 1-b, 2-b, 3-a, 4-b.

**Parte 2, Ejercicio 1**:
1.  **1:N** (Un Departamento tiene N Profesores, un Profesor tiene 1 Departamento).
2.  **1:1** (Un Coche tiene 1 Matrícula, una Matrícula es de 1 Coche).
3.  **N:M** (Un Cliente compra N Productos, un Producto es comprado por N Clientes).

**Parte 2, Ejercicio 2 (Propuesta)**:
*   Tabla **CLIENTES**: `ID_Cliente (PK)`, Nombre, Dirección.
*   Tabla **PRODUCTOS**: `ID_Producto (PK)`, Nombre, Precio_Unitario.
*   Tabla **PEDIDOS**: `ID_Pedido (PK)`, `ID_Cliente (FK)`, Fecha.
*   Tabla **DETALLE_PEDIDO**: `ID_Pedido (FK)`, `ID_Producto (FK)`, Cantidad. *(PK Compuesta)*
