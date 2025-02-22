def calcular_imc():
    # Puede brindarme los datos de su peso y su altura del :)
    peso = float (input("ingresa tu peso en kg: "))
    altura = float (input("ingresa tu altura en metros"))

    # Validación de datos para evitar errores ;)
    if peso <= 0 or altura <= 0:
        print(" ¡ERROR! Peso y altura deben ser mayores a 0.")  
        return 
   
   # Cálculo del IMC
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

#Tabla de clasificación \(.u.)/
def mostrar_tabla():
    print("\n Tabla de clasificación del IMC:")
    print("Menos de 18.5  - Bajo peso")
    print("18.5 - 24.9    - Peso normal")
    print("25 - 29.9      - Sobrepeso")
    print("30 o más       - Obesidad")

#Menú interactivo :3
while True:
    print("\n Bienvenido a tu calculadora de confianza :D\n")
    print("\n Menú ")
    print("1. Calcular IMC")
    print("2. Ver tabla de clasificación")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
         calcular_imc()
    elif opcion == "2":
        mostrar_tabla()
    elif opcion == "3":
        print("¡Chaoooo!")
        break
    else:
        print(" Opción no válida. Inténtalo de nuevo.")