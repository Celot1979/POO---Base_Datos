# ⚔️ Desafío Práctico: Sistema de Notificaciones Polimórfico

## Objetivo
Implementar un sistema que pueda enviar mensajes por diferentes canales (Email, SMS, App) sin que el código principal sepa qué tipo de notificador está usando.

## Enunciado
1. Define una clase base llamada `Notificador` con un método `enviar(mensaje)` que no haga nada (o lance `NotImplementedError`).
2. Crea tres clases hijas:
   - `EmailNotificador`: Al enviar, imprime "Enviando EMAIL: [mensaje]".
   - `SMSNotificador`: Al enviar, imprime "Enviando SMS: [mensaje]".
   - `PushNotificador`: Al enviar, imprime "Enviando PUSH: [mensaje]".
3. Crea una lista llamada `canales` que contenga una instancia de cada uno.
4. Recorre la lista y usa el polimorfismo para enviar el mensaje "Hola, examen 2026!" por todos los medios.

## Pista
Tu bucle principal debería verse así de simple:
```python
for canal in canales:
    canal.enviar("Hola...")
```

---

## Solución Propuesta (¡Inténtalo primero!)

```python
class Notificador:
    def enviar(self, mensaje):
        raise NotImplementedError("Debes implementar este método")

class EmailNotificador(Notificador):
    def enviar(self, mensaje):
        print(f"📧 Enviando EMAIL: {mensaje}")

class SMSNotificador(Notificador):
    def enviar(self, mensaje):
        print(f"📱 Enviando SMS: {mensaje}")

class PushNotificador(Notificador):
    def enviar(self, mensaje):
        print(f"🔔 Enviando PUSH: {mensaje}")

# Código Cliente
canales = [EmailNotificador(), SMSNotificador(), PushNotificador()]

for canal in canales:
    canal.enviar("¡Recordatorio: Examen el 03/02/2026!")
```
