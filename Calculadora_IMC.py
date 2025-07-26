# Calculadora de IMC

#Esta calculadora de IMC (Índice de Masa Corporal) está diseñada para:
# -Capturar y validar datos del usuario
# -Calcular el IMC utilizando operadores aritméticos
# -Clasificar el resultado según rangos definidos
# -Permitir múltiples cálculos sin reiniciar el programa


# Esta función (def calcular_imc) contiene todo el proceso del cálculo del IMC
# La función calcular_imc() contiene todo el proceso principal. 
# Se encarga de validar los datos, calcular el IMC, y mostrar el resultado.

def calcular_imc():
    # Dentro de while True, se solicita al usuario que ingrese peso y estatura
    # Se validan los siguientes aspectos:
    # - Que los campos no estén vacíos
    # - Que la estatura contenga un punto decimal (formato entero.decimal a dos dígitos)
    # - Que ambos valores sean positivos

    while True: 
        try:
            # Captura de datos del usuario
            peso= input("Ingresa el peso en kilogramos: ")
            estatura = input("Ingresa la estatura en metros (usa punto decimal, ej: 1.56): ")

            # Validación: campos vacíos
            if not peso or not estatura:
                raise ValueError("No se deben dejar campos vacíos.")

            # Validación: la estatura debe contener un punto decimal (ej. "1.56")
            if "." not in estatura:
                raise ValueError("La estatura debe tener punto decimal, por ejemplo: 1.56")

            # Conversión de entradas a tipo float
            Peso = float(peso)
            Estatura = float(estatura)

            # Validación: valores numéricos mayores a cero
            # Mediante raise ValueError lanza un error si el peso o la estatura son menores o iguales a cero
            if Peso <= 0 or Estatura <= 0:
                raise ValueError("El peso y la estatura deben ser mayores a cero.")

            # Si todo está bien, sale del bucle
            break

        # Manejo de errores
        except ValueError as e:
            print(f"\nFavor de validar los datos de entrada en peso y estatura. {e}\n")

    # Cálculo del IMC usando operador aritmético
    IMC = Peso / (Estatura ** 2)

    # Clasificación según el valor del IMC
    if IMC < 18.5:
        clasificacion = "peso bajo"
    elif 18.5 <= IMC <= 24.99:
        clasificacion = "peso normal"
    elif 25.0 <= IMC <= 29.99:
        clasificacion = "sobrepeso"
    elif 30.0 <= IMC <= 34.99:
        clasificacion = "obesidad leve"
    elif 35.0 <= IMC <= 39.99:
        clasificacion = "obesidad media"
    else:
        clasificacion = "obesidad mórbida"

    # Salida de datos completa
    print("\nResultados:")
    print(f"Peso ingresado: {Peso} kg")                              # Mostrar peso original
    print(f"Estatura ingresada: {Estatura} m")                       # Mostrar estatura original
    print(f"Operación realizada: {Peso} / ({Estatura} * {Estatura})")  # Mostrar fórmula usada
    print(f"Tu IMC es {IMC:.2f}, por lo cual tienes {clasificacion}.\n")  # Mostrar resultado y clasificación

# Bucle principal: permite repetir el cálculo si el usuario así lo desea
while True:
    calcular_imc()  # Llamamos a la función para realizar todo el proceso

    # Preguntar si el usuario quiere hacer otro cálculo
    repetir = input("¿Deseas calcular otro IMC? (s/n): ").strip().lower()
    if repetir != "s":
        print("Gracias por usar la calculadora de IMC.")
        break  # Finaliza el programa si la respuesta no es "s"