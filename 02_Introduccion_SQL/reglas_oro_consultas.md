# Guía de Refuerzo: Las Reglas de Oro de las Consultas SQL

Hola. He analizado tus ejercicios y veo un patrón claro: **Tu lógica es buena (sabes qué pedir), pero tu "gramática" SQL te traiciona.**

Tiendes a usar el inglés o el lenguaje natural (como usar "AND" para listar cosas, o intercambiar "INTO" por "FROM"). SQL es muy rígido.

Aquí tienes las 3 Reglas de Oro para memorizar estas estructuras y no volver a fallar.

---

## Regla 1: El SELECT es una "Lista de la Compra"

Cuando vas al súper, no dices "Quiero manzanas Y peras Y uvas".
Haces una lista separada por comas: "Manzanas, peras, uvas".

**En SQL es igual:**
*   ❌ **MAL:** `SELECT Nombre AND Apellido FROM Clientes`
*   ✅ **BIEN:** `SELECT Nombre, Apellido FROM Clientes`

> **Truco:** El `AND` en SQL es SOLO para condiciones (FILTROS), nunca para columnas.
> *   "Donde sea de Gijón **Y** tenga más de 18 años" -> `WHERE Ciudad='Gijón' AND Edad > 18`.

---

## Regla 2: El Orden Sagrado (S-F-W)

Una consulta `SELECT` siempre sigue este orden. Tatuátelo en la mente: **S.F.W.**

1.  **S**ELECT (¿QUÉ columnas quiero?)
2.  **F**ROM   (¿De DÓNDE saco los datos? ¿De qué tabla?)
3.  **W**HERE  (¿CUÁLES filas quiero? ¿El filtro?)

*   ❌ **MAL:** `SELECT FROM Clientes *` (El FROM va después de decir qué quieres)
*   ✅ **BIEN:** `SELECT * FROM Clientes`

---

## Regla 3: INSERT "INTO" (DENTRO)

Piensa en una caja. Tú no insertas datos "DESDE" (FROM) la caja. Tú metes datos "DENTRO" (INTO) de la caja.

*   **SELECT** usa **FROM** (Cojo datos **DESDE** la tabla).
*   **INSERT** usa **INTO** (Meto datos **DENTRO** de la tabla).

*   ❌ **MAL:** `INSERT FROM Clientes ...`
*   ✅ **BIEN:** `INSERT INTO Clientes ...`

---

## Resumen Visual (Semáforo)

| Acción | Comando | Preposición Clave | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Leer** | SELECT | **FROM** (Desde) | `SELECT Nombre FROM Clientes` |
| **Escribir** | INSERT | **INTO** (Dentro) | `INSERT INTO Clientes...` |
| **Actualizar** | UPDATE | **SET** (Establecer) | `UPDATE Clientes SET ...` |
| **Borrar** | DELETE | **FROM** (Desde) | `DELETE FROM Clientes` |

