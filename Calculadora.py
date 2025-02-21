def mostrar_menu():
    print("\n Bienvenido a tu calculadora de confianza \n")
    print("\n Menú ")
    print("1. Calcular IMC")
    print("2. Ver tabla de clasificación")
    print("3. Salir")

def calcular_imc():
    peso = float (input("ingresa tu peso en kg: "))
    altura = float (input("ingresa tu altura en metros"))

    if peso <= 0 or altura <= 0:
        print(" ¡ERROR! Peso y altura deben ser mayores a 0.")  
        return 
   
    imc = peso / (altura ** 2)
    print(f"\n Tu IMC es : {imc:.2f}")

    if imc < 18.5:
        print("Estás en una categoria de peso bajo :(")
    elif 18.5 <= imc < 24.9:
        print("Estás en una categoria de peso normal :D")
    elif 25 <= imc < 29.9:
        print("Estás en una categoria de sobrepeso :[")
    else:
        print("Estás en un rango de obesidad D:")

def mostrar_menu():
    print("\n Bienvenido a tu calculadora de confianza \n")
    print("\n Menú ")
    print("1. Calcular IMC")
    print("2. Ver tabla de clasificación")
    print("3. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
         calcular_imc()
    elif opcion == "2":
        print("Mostrando tabla de clasificación")
    elif opcion == "3":
        print("¡Chaoooo!")
        break
    else:
        print(" Opción no válida. Inténtalo de nuevo.")
