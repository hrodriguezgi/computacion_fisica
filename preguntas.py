"""
Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones
de python básicas.
#MATENME
Utilice el archivo `data.csv` para resolver las preguntas.

"""
#Trabajo hecho por Sary Alejandra Garcia Sierra y José Tomas Doria Causil
#hola 
with open('data.csv') as file:
    data = file.readlines()

#Pregunta num 1
def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    # escribo todo mi codigo aqui
    # codigo con mi respuesta
    total = 0
    for line in data: 
        total = total + int(line.split('\t')[1])
    # codigo con mi respuesta
    return(total)
#print(pregunta_01())

#Pregunta num 2
def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    diccionario = {}
    for line in data:
        letra = line[0]
        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1
    orden = sorted(diccionario.items())
    return(orden)
#print(pregunta_02())

#Pregunta num 3
def pregunta_03():
    
    suma_por_letra = {}


    for partes in data:
        letra = partes.split('\t')[0]
        numero = int(partes.split('\t')[1])

        if letra in suma_por_letra:
            suma_por_letra[letra] += numero
        else:
            suma_por_letra[letra] = numero
    #print(resultado_ordenado)
    resultado_ordenado = sorted(suma_por_letra.items())
    return resultado_ordenado

#print(pregunta_03())

"""
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ] 
    """

    
#Pregunta num 4
def pregunta_04():
    diccionario = {}
    for line in data:
        letra = line.split('-')[1]
        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1
    orden = sorted(diccionario.items())
    return(orden)

#print(pregunta_04())
"""
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    

#Pregunta num 5
def pregunta_05():
    mayores_menores = {}

    for partes in data:
        letra = partes.split('\t')[0]
        numero = int(partes.split('\t')[1])
  

        if letra in mayores_menores :
            mayores_menores[letra]['max'] = max(mayores_menores[letra]['max'], numero)
            mayores_menores[letra]['min'] = min(mayores_menores[letra]['min'], numero)
        else:
            mayores_menores[letra] = {'max': numero, 'min': numero} 
    resultado = [(letra, valores['max'], valores['min']) for letra, valores in mayores_menores.items()]
    return(sorted(resultado))
#print(pregunta_05())
"""
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """


#Pregunta num 6
def pregunta_06():
    diccionario = {}

    for line in data:
        columnas = line.strip().split('\t')
        if len(columnas) < 5:
            continue  
        elementos = columnas[4].split(',') 
        for elemento in elementos:
            try:
                clave, valor = elemento.split(':')  
                valor = int(valor) 
                if clave in diccionario:
                    diccionario[clave].append(valor)
                else:
                    diccionario[clave] = [valor]
            except ValueError:
                print(f"Error en el formato del elemento: {elemento}")
                continue  
    resultado = []
    for clave, valores in diccionario.items():
        min_valor = min(valores)
        max_valor = max(valores)
        resultado.append((clave, min_valor, max_valor))

    resultado_ordenado = sorted(resultado)
    return(resultado_ordenado)
#print(pregunta_06())
"""
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """


#Pregunta num 7
def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
 

    diccionario = {}
    for line in data:
        partes = line.split('\t')
        letra = partes[0]
        valor = int(partes[1])
        if valor in diccionario:
            diccionario[valor].append(letra)
        else:
            diccionario[valor] = [letra]
    resultado = [(valor, letras) for valor, letras in diccionario.items()]
    return (sorted(resultado))
#print(pregunta_07())

#Pregunta num 8
def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open('data.csv') as file:
        linea = file.readlines()

    diccionario = {}
    for line in linea:
        partes = line.split('\t')
        letra = partes[0]
        valor = int(partes[1])
        if valor in diccionario:
            diccionario[valor].add(letra)
        else:
            diccionario[valor] = {letra}
    resultado = [(valor, sorted(list(letras))) for valor, letras in diccionario.items()]
    return(sorted(resultado))
    
#print(pregunta_08())

#Pregunta num 9
def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    diccionario = {}
    for line in data:
        valores = line.split('\t')[4].split(',')
        for valor in valores:
            clave = valor.split(':')[0]
            if clave in diccionario:
                diccionario[clave] += 1
            else:
                diccionario[clave] = 1

    orden = dict(sorted(diccionario.items()))
    return(orden)
#print(pregunta_09())


#Pregunta num 10
def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    resultado = []
    for line in data:
        partes = line.split('\t')
        letra = partes[0]
        col4 = len(partes[3].split(','))
        col5 = len(partes[4].split(','))
        resultado.append((letra, col4, col5))

    return(resultado)
#print(pregunta_10())
    

#Pregunta num 11
def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    sum = {}

    for line in data:
        col = line.strip().split('\t') 
        value = int(col[1]) 
        letras = col[3].split(',') 

        for letra in letras:
            if letra in sum:
                sum[letra] += value
            else:
                sum[letra] = value
    orden_sumas = dict(sorted(sum.items()))

    return(orden_sumas)
#print(pregunta_11())
#Esto no cargaaaa

#Pregunta num 12
def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    diccionario = {}
    for line in data:
        partes = line.split('\t')
        letra = partes[0]
        valores = partes[4].split(',')
        suma = sum(int(valor.split(':')[1]) for valor in valores)
        if letra in diccionario:
            diccionario[letra] += suma
        else:
            diccionario[letra] = suma
    orden = dict(sorted(diccionario.items()))
    return(orden)

#print(pregunta_12())
