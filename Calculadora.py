def suma(x, y):
    print(f"La suma es: {x + y}")

def resta(x, y):
    print(f"La resta es: {x - y}")

def multi(x, y):
    print(f"La multiplicación es: {x * y}")

def div(x, y):
    if y == 0:
        print("Error: No se puede dividir por 0.")
    else:
        print(f"La división es: {x / y}")

while True:
    print("\nBienvenido a tu calculadora de confianza\n")
    print("¿Qué deseas realizar?")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    response = int(input("Escribe la opción: "))

    if response == 5:
        print("¡Gracias por usar la calculadora!")
        break  # Sale del bucle

    # Solo pide los números si la opción es válida
    if response in [1, 2, 3, 4]:
        a = int(input("Escribe un número: "))
        b = int(input("Escribe otro número: "))

        if response == 1:
            suma(a, b)
        elif response == 2:
            resta(a, b)
        elif response == 3:
            multi(a, b)
        elif response == 4:
            div(a, b)
    else:
        print("Opción no válida. Inténtalo de nuevo.")