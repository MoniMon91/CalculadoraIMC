# CalculadoraIMC
## Proyecto UCamp para calcular el índice de masa corporal

### Para construir esta calculadora se hizo uso de los siguientes elementos clave de Python:
- def: Define una función para encapsular la lógica del cálculo del IMC.
- while: Permite repetir el ingreso de datos hasta que estos sean válidos o el usuario desee terminar.
- if: Evalúa condiciones para validar datos y clasificar el IMC.
- raise: Lanza errores personalizados cuando los datos no cumplen con los criterios requeridos. (para esta calculadora no se permiten campos vacíos)
- input: Captura datos del usuario (peso y estatura). (en este caso se encuentra dentro de un bucle while)
- print: Muestra los resultados y mensajes.
- float: Convierte cadenas a números reales para poder hacer operaciones.
- valores mayores a cero: Se exige que tanto el peso como la estatura sean mayores a 0 para ser válidos.
- ValueError: Tipo de error lanzado si los datos no cumplen las condiciones esperadas.
- variables: Se utilizan variables como Peso y Estatura para almacenar los datos ingresados.
- operación IMC: Se usa la fórmula IMC = peso / (estatura ** 2) para obtener el índice.
- break: Termina el bucle de entrada de datos si todo está correcto.
- except: Maneja errores generados por entradas inválidas.
- f-string: Muestra mensajes con variables formateadas de forma legible, como f"Tu IMC es {IMC:.2f}".
- {e}\n: Inserta el mensaje del error capturado seguido de un salto de línea.
- operador **: Eleva la estatura al cuadrado (potencia).
- elif: Evalúa condiciones múltiples en la clasificación del IMC.
- else: Maneja cualquier otra condición no cubierta por if/elif.
- \n: Salto de línea para mejorar la presentación del texto.
- .2f: Formatea números decimales a 2 cifras.
- repetir: Variable que guarda si el usuario quiere hacer otro cálculo. (Reiniciar la calculadora)
- .strip(): Limpia espacios en la entrada del usuario.
- .lower(): Convierte la entrada del usuario a minúsculas para evitar errores de formato.

