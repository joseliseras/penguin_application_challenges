def obtener_fila_verificada(palabra_a_encontrar, palabra_ingresada):
    cantidad_de_palabras_a_encontrar = 5

    letras_verificadas = []

    for posicion in range(cantidad_de_palabras_a_encontrar):
        
        las_letras_son_iguales = palabra_a_encontrar[posicion] == palabra_ingresada[posicion]
        la_letra_existe_en_palabra = palabra_ingresada[posicion] in palabra_a_encontrar

        if las_letras_son_iguales:
            letras_verificadas.append("[" +palabra_ingresada[posicion] + "]")

        elif la_letra_existe_en_palabra:
            letras_verificadas.append("(" +palabra_ingresada[posicion] + ")")

        else:
            letras_verificadas.append(palabra_ingresada[posicion])

    return letras_verificadas


palabra_a_encontrar = "arbol"
intentos = 5
cantidad_de_letras = 5

letras_verificadas = []

print ("bienvenidos al Juego")
print("""INSTRUCIONES:
      1. Encuentra una palabra de 5 letras
      2. Si la letra corresponde a la posicion corresta se marca entre[]
      3. Si la letra existe en la palabra pero no se encuentra en la posicion corresta se marca entre ()
      4. si la letra no se encuentra en la palabra no se marca
      5. Tenes 5 intentos""")


while intentos > 0:
    print(f"Te quedan {intentos} intentos")
    palabra_ingresada = input (f"Ingrese una palabra: ")
    intentos = intentos - 1
    
    
    if (len(palabra_ingresada)) != cantidad_de_letras:
        print("La palabra ingresasda no contiene la cantidad de letras correctas")
        print("Ingrese una palabra ", cantidad_de_letras, "letras")
        intentos = intentos + 1
        continue
        

    else:
        linea_verificada = obtener_fila_verificada (palabra_a_encontrar, palabra_ingresada)
        letras_verificadas.append(linea_verificada)
    
    

    if palabra_ingresada == palabra_a_encontrar:
        print(linea_verificada)
        print("GANASTEEEEE")
        break


    print(linea_verificada)

print("No te quedan intentos")


