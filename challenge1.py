# El objetivo de este desafío es programar una versión simplificada del popular juego de adivinación de palabras, "Wordle", utilizando Python.

# Funcionamiento del Juego:
# En Wordle, el jugador tiene un número limitado de intentos para adivinar una palabra secreta. Con cada intento, 
# el juego proporciona retroalimentación sobre qué letras están correctas y en la posición correcta, 
# qué letras están en la palabra pero en una posición incorrecta, y qué letras no están en la palabra.

# Requisitos Específicos:
# - El jugador tiene un número limitado de 5 intentos para adivinar la palabra.
# - Después de cada intento, el programa debe retornar las letras según las instrucciones de:
#     - Si las letras existen en la palabra a encontrar y sus posiciones coinciden: encerrar en corchetes `[]` y agregar al resultado
#     - Si las letras existen en la palabra a encontrar pero sus posiciones no coinciden: encerrar en paréntesis `()` y agregar al resultado
#     - Si no se cumple ninguna de las anteriores, agregar la letra a la lista vacía sin modificaciones
# - Asegurarse de que las entradas del usuario sean válidas (por ejemplo, de la longitud correcta).
# - Incluir un contador de intentos restantes.

# Tecnologías a utilizar:
# - Python
# - Se valora el uso de librerías adicionales