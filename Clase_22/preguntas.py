"""
Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones
de python básicas.

Utilice el archivo `data.csv` para resolver las preguntas.

"""


import csv


def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214

    """
    # escribo todo mi codigo aqui
    # codigo con mi respuesta

    total = 0
    with open("data.csv", "r") as archivo:
        for linea in archivo:
           
            valores = linea.strip().split("\t")
            # Convertir el primer valor a entero y sumarlo al total
            try:
                total += int(valores[1])
            except ValueError:
                print(f"Error al convertir el valor '{valores[1]}' a entero en la línea: {linea}")
            
    return total
resultado = pregunta_01()
print( resultado)

 

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
    cualquier = []
    with open("data.csv", "r") as archivo:
        cualquier= archivo.readlines()
        diccionario={}
    for line in cualquier:
        letra= line[0]
        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1
    resultado = list(diccionario.items())
    resultado.sort()
    return resultado
resultado2 = pregunta_02()
print(resultado2)




def pregunta_03():
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
    suma_por_letra = {}
    with open("data.csv", "r") as archivo:
        for partes in archivo:
            letra = partes.split('\t')[0]
            numero = int(partes.split('\t')[1])

            if letra in suma_por_letra:
                suma_por_letra[letra] += numero
            else:
                suma_por_letra[letra] = numero
    resultado_ordenado = sorted(suma_por_letra.items())
    return resultado_ordenado
resultado03=pregunta_03()
print( resultado03)
   

def pregunta_04():
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
    meses = {}
    with open("data.csv", "r") as archivo:
        for linea in archivo:
            campos = linea.split()
            fecha = campos[2]
            mes = fecha[5:7]
            if mes in meses:
                meses[mes] += 1
            else:
                meses[mes] = 1
    resultado4 = list(meses.items())
    resultado4.sort()
    return resultado4
 
resultado4 = pregunta_04()
print(resultado4)
    


def pregunta_05():
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

    
    return
    """
    resultados = {}
    with open("data.csv", 'r') as archivo:
        for linea in archivo:
            campos = linea.split("\t") 
            letra, valor = campos[0], int(campos[1])

            if letra not in resultados:
                resultados[letra] = []

            resultados[letra].append(valor)

        resultado5 = list(resultados.items())
        resultado5.sort()
        return [(letra, min(valores), max(valores)) for letra, valores in resultados.items()]
resultado5 = pregunta_05()
print( resultado5)


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

    
    return
    """
def pregunta_06():
    diccionario_valores = {}
    with open('data.csv', 'r') as file:
        lineas = file.readlines()
        for linea in lineas:  
            columnas = linea.split('\t') 
            elementos_columna_5 = columnas[4].split(',')  
            for elemento in elementos_columna_5:
                clave, valor = elemento.split(':')
                valor = int(valor)
                if clave in diccionario_valores:
                    diccionario_valores[clave].append(valor)
                else:
                    diccionario_valores[clave] = [valor]

    
    diccionario_extremos = {clave: (min(valores), max(valores)) for clave, valores in diccionario_valores.items()}

    return diccionario_extremos


valores_extremos = pregunta_06
print(valores_extremos)



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


return
"""
def pregunta_07():
    asociaciones = {}
    with open('data.csv', 'r') as file:
        lineas = file.readlines()
        for linea in lineas:  
            columnas = linea.split('\t')  
            letra_columna_1 = columnas[0]
            valor_columna_2 = columnas[1]
            if valor_columna_2 not in asociaciones:
                asociaciones[valor_columna_2] = []
            asociaciones[valor_columna_2].append(letra_columna_1)
    
    lista_tuplas = [(valor, letras) for valor, letras in asociaciones.items()]
    
    return lista_tuplas
resultado07 = pregunta_07
print(resultado07)


def pregunta_08():
    
    """Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
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

    
    return"""

    diccionario = {}
    with open('data.csv', 'r') as file:
        lineas = file.readlines()
        for linea in lineas:  
            columnas = linea.split('\t') 
            valor_columna_2 = columnas[1]
            letra_columna_1 = columnas[0]
            if valor_columna_2 not in diccionario:
                diccionario[valor_columna_2] = set()
            diccionario[valor_columna_2].add(letra_columna_1)
    
    lista_tuplas = [(valor, sorted(list(letras))) for valor, letras in diccionario.items()]
    
    return lista_tuplas


resultado08 = pregunta_08
print(resultado08)


def pregunta_09():
    
    """Retorne un diccionario que contenga la cantidad de registros en que aparece cada
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

    
    return"""


    conteo_claves = {}
    with open('data.csv', 'r') as file:
        lineas = file.readlines()
        for linea in lineas: 
            columnas = linea.split('\t')  
            elementos_columna_5 = columnas[4].split(',')  
            for elemento in elementos_columna_5:
                clave = elemento.split(':')[0] 
                if clave in conteo_claves:
                    conteo_claves[clave] += 1
                else:
                    conteo_claves[clave] = 1
    return conteo_claves

conteo_resultado = pregunta_09
print(conteo_resultado)


def pregunta_10():
    
    """Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
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
    with open('data.csv','r') as file:
        Q = file.readlines()
        for linea in Q:  
            columnas = linea.split('\t')
            letra_columna_1 = columnas[0]
            elementos_columna_4 = columnas[3].split(',')
            elementos_columna_5 = columnas[4].split(',')
            resultado.append((letra_columna_1, len(elementos_columna_4), len(elementos_columna_5)))
    return resultado
respuesta10=pregunta_10
print(respuesta10)


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



return

"""
def pregunta_11():
    diccionario = {}
    with open('data.csv', 'r') as file:
        lineas = file.readlines()
        for linea in lineas:  
            columnas = linea.split('\t')  
            valor_columna_2 = int(columnas[1])
            letras_columna_4 = columnas[3].split(',') 
            for letra in letras_columna_4:
                if letra in diccionario:
                    diccionario[letra] += valor_columna_2
                else:
                    diccionario[letra] = valor_columna_2

    
    diccionario_ordenado = dict(sorted(diccionario.items()))

    return diccionario_ordenado


diccionario_resultado = pregunta_11
print(diccionario_resultado)


    
"""Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
los valores de la columna 5 sobre todo el archivo.

Rta/
{
    'A': 177,
    'B': 187,
    'C': 114,
    'D': 136,
    'E': 324
}


return
"""       
def pregunta_12():
    diccionario = {}
    with open('data.csv', 'r') as file:
            lineas = file.readlines()
            for linea in lineas: 
                columnas = linea.split('\t')  
                letra_columna_1 = columnas[0]
                elementos_columna_5 = columnas[4].split(',') 
                suma_valores = sum(int(elemento.split(':')[1]) for elemento in elementos_columna_5 if ':' in elemento)
                if letra_columna_1 in diccionario:
                    diccionario[letra_columna_1] += suma_valores
                else:
                    diccionario[letra_columna_1] = suma_valores 
            return diccionario

diccionario_resultado12 = pregunta_12
print(diccionario_resultado12)

