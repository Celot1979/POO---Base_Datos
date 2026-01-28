def dividir_numeros():
    while True:
        try:
            A = int(input("Introduce el número (Dividendo): "))
            B = int(input("Introduce el número (Divisor): "))
            print("El resultado de la división es: ", A/B)
            # Si todo va bien, rompe el bucle con break
            break
            
        except ValueError:
            print("Introduce solo números")
            # Maneja que no sean números
            
            
        except ZeroDivisionError:
            print("No se puede dividir entre cero")
            

# Ejecución
print("--- Iniciando Calculadora Segura ---")
dividir_numeros()
