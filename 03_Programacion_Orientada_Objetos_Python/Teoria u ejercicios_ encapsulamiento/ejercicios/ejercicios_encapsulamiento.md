# Desafío Práctico: Encapsulamiento y Protección de Datos
## Certificado IFCD0112

### Ejercicio 1: La Cuenta Corriente Segura
Crea una clase `CuentaSegura`.
1.  **Atributo Privado**: `__saldo` (empieza en 2000).
2.  **Getter `@property`**: `saldo` -> devuelve el valor.
3.  **Setter `@saldo.setter`**: `saldo` -> **NO PERMITAS CAMBIARLO DIRECTAMENTE**. Si alguien intenta `c.saldo = 5000`, imprime "Error: No puedes manipular el saldo manualmente, usa depositar()".
4.  **Método** `depositar(cantidad)`: Suma dinero (solo si cantidad > 0).
5.  **Método** `retirar(cantidad)`: Resta dinero (solo si hay fondos y cantidad > 0).

---

### Ejercicio 2: Registro de Usuario
Crea una clase `Usuario`.
1.  **Atributos**: `nombre` (publico) y `_edad` (protegido).
2.  Usa `@property` para la `edad`.
3.  En el setter de `edad`, valida que el usuario tenga entre 18 y 100 años. Si no, imprime "Edad no válida" y no guardes el cambio.
4.  **Prueba**:
    *   Crea un usuario con 25 años -> Imprime su edad.
    *   Intenta cambiar la edad a 12 -> Verifica que no cambie.
    *   Intenta cambiar la edad a 45 -> Verifica que sí cambie.
