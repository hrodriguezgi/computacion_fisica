"""
Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones
de python básicas.

Utilice el archivo `data.csv` para resolver las preguntas.

"""


def pregunta_01():
    
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    # escribo todo mi codigo aqui
    with open ("data.csv") as archivo:
        contenido = archivo.readlines()

    suma = 0 
    for entry in contenido:
        partes = entry.split('\t')
        suma += int(partes[1])
    print (suma) 
  
    # codigo con mi respuesta
    return 
    


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
    with open("data.csv") as archivo:
        contenido = archivo.readlines()
    letras = {}

    for line in contenido: 
        letra = line.split('\t')[0]
        if letra in letras.keys():
            letras[letra] += 1
        else:
            letras[letra] = 1

    ol = sorted(letras.items())

    print("[")
    for letra, count in ol:
        print(f'    ("{letra}",{count})')
    print("]")

    return 


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
    with open("data.csv") as archivo:
        contenido = archivo.readlines()
    sumas = {}
    for line in contenido: 
        letra = line.split('\t')
        sumas[letra[0]] = sumas.get(letra[0],0) + int(letra[1])
    ol2 = list(sorted(sumas.items()))
    print("[")
    for letra, count in ol2:
        print(f'    ("{letra}",{count})')
    print("]")

    return


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
    with open("data.csv") as archivo:
        contenido = archivo.readlines()

    letras = {}
    for line in contenido: 
        letra = line.split('\t')[2]
        meses = letra.split("-")[1]
        if meses in letras.keys():
            letras[meses] += 1
        else:
            letras[meses] = 1
    ol = sorted(letras.items())
    print("[")
    for letra, count in ol:
        print(f'    ("{letra}",{count})')
    print("]")
    return


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

    """
    with open("data.csv") as archivo:
        contenido = archivo.readlines()
    letras = {"A":[], "B":[], "C":[], "D":[], "E":[]}

    for line in contenido: 
        letra = line.split('\t')[0]
        number = line.split('\t')[1]
        letras[letra].append(int(number))

    minmax = {"A":[], "B":[], "C":[], "D":[], "E":[]}
    for clave, lista in letras.items():
        letra = clave 
        maximo = max(lista)
        minmax[letra].append(int(maximo))
        minimo = min(lista) 
        minmax[letra].append(int(minimo))

    minmaxs = minmax.items()

    print("[")
    for cosas in minmaxs:
        minmaxss = (cosas[0], *cosas[1])
        print (f'   {minmaxss}')
    print("]")
    return


def pregunta_06():
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
    with open("data.csv") as archivo:
        contenido = archivo.readlines()

    iamsodone = []
    ishouldquitmyjob = []
    splitmywritst = {}


    for line in contenido: 
        whydiditakethisclass = line.split('\t')[4]
        iamsodone.append(whydiditakethisclass.split(","))
    for cosas in iamsodone:
        for cosa in cosas:
            ishouldquitmyjob.append(cosa.replace("\n",""))
    for elemento in ishouldquitmyjob:
        key, valor = elemento.split(':')
        valor = int(valor)
        if key in splitmywritst:
            splitmywritst[key].append(valor)
        else:
            splitmywritst[key] = [valor]

    idontlikethis = sorted(splitmywritst.items())

    wrongmajor = {"aaa":[],"bbb":[],"ccc":[],"ddd":[],"eee":[],"fff":[],"ggg":[],"hhh":[],"iii": [],"jjj":[]}
    for key, lista in idontlikethis:
        letra = str(key)
        minimo = min(lista) 
        wrongmajor[letra].append(int(minimo))
        maximo = max(lista)
        wrongmajor[letra].append(int(maximo))
        

    boniceseller = wrongmajor.items()
    print("[")
    for cosas in boniceseller:
        boniceseller = (cosas[0], *cosas[1])
        print (f'   {boniceseller}')
    print("]")
    return


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
    with open("data.csv") as archivo:
        content = archivo.readlines()

    anxiousbeing = {}    
    hatredconsumedme = []

    for entry in content: 
        parts = entry.split('\t')
        hatredconsumedme.append(parts)

    for vaina in hatredconsumedme:
        key, value = int(vaina[1]), vaina[0]
        if key not in anxiousbeing:
            anxiousbeing[key] = []
        anxiousbeing[key].append(value)

    print("[")
    for element in sorted(anxiousbeing.items()):
        print(f'    {element},')
    print("]")
    return


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
    with open("data.csv") as archivo:
        content = archivo.readlines()
    questioninglife = {}
    whybother = []

    for entry in content: 
        parts = entry.split('\t')
        whybother.append(parts)


    for vaina in whybother:
        key, value = int(vaina[1]), vaina[0]
        if key not in questioninglife:
            questioninglife[key] = []
        if value not in questioninglife[key]:
            questioninglife[key].append(value)

    print("[")
    for element in sorted(questioninglife.items()):
        order = sorted(element[1])
        lista = (element[0], order)
        print(f'    {lista}')
    print("]")
    return


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
    with open("data.csv") as archivo:
        content = archivo.readlines()
    ricardoShillyShally = {}
    whyyyy = []
    chocoaventuras = []
    numeros = []
    for entry in content: 
        parts = entry.split('\t')[4]
        whyyyy.append(parts.split(","))
        
            
    for thing in whyyyy:
        for element in thing:
            chocoaventuras.append(element.replace("\n", ""))

    for vaina in chocoaventuras:
        key, value = vaina.split(":")
        if key not in ricardoShillyShally:
            ricardoShillyShally[key] = 1
        else: 
            ricardoShillyShally[key] += 1
                    
    print("{")
    for key in sorted(ricardoShillyShally):
        print(f'    "{key}": {ricardoShillyShally[key]},')
    print("}")
    return


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
    my_dic = {}
    with open("data.csv") as archivo:
        content = archivo.readlines()

    sobelo_list = []
    new_thingy = []
    cosiaco = []
    for entry in content: 
        parts = entry.split('\t')
        sobelo_list.append(parts)
            
    for thing in sobelo_list:
        thing[4] = thing[4].replace("\n", "")
        tupla = (thing[0], len(thing[3].split(",")), len(thing[4].split(",")))
        cosiaco.append(tupla)        
        
    print("[")
    for vaina in cosiaco:
        print(f'    {vaina},')
    print("]")
    return


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
    with open("data.csv") as archivo:
        content = archivo.readlines()
    iwanttosleep = {}
    mycathasabetterlife= []
    cosito = []
    i=0
    for entry in content: 
        parts = entry.split('\t')   
        mycathasabetterlife.append(parts[3].split(","))
        cosito.append(int(parts[1]))
    for element in mycathasabetterlife:
        for vaina in element:
            if vaina in iwanttosleep:
                iwanttosleep[vaina] = iwanttosleep[vaina] + cosito[i]
            else: 
                iwanttosleep[vaina] = cosito[i]
        i += 1
    livelovelaugh=(dict(sorted(iwanttosleep.items())))
    print("{")
    for element in livelovelaugh:
        print(f'    "{element}": {livelovelaugh[element]},')
    print("}")
        
    return


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
    fucklife = {}
    iwouldratherdie = []
    killmenow = []
    whatdididoinlife = []
    codingisntmything = []
    with open("data.csv") as archivo:
        content = archivo.readlines()


    for entry in content: 
        parts = entry.split('\t')
        iwouldratherdie.append(parts[4])
        codingisntmything.append(parts[0])
        
    for knives in iwouldratherdie:
        knives = knives.replace('\n', '').split(",")
        fuuuuuuck = []
        for elements in knives:
            fuuuuuuck.append(elements.split(":"))
        killmenow.append(fuuuuuuck)

    for mkada in killmenow:
        value = 0
        for chbda in mkada:
            value += int(chbda[1])
        whatdididoinlife.append(value)
    i = 0
    for element in codingisntmything:
        if element not in fucklife:
            fucklife[element] = whatdididoinlife[i]
        else: 
            fucklife[element] += whatdididoinlife[i]    
        i += 1
    print("[")
    for cosito in dict(sorted(fucklife.items())):
        print(f"    '{cosito}' : {dict(sorted(fucklife.items()))[cosito]}")
    print("]")
    return
pregunta_01()
pregunta_02()
pregunta_03()
pregunta_04()
pregunta_05()
pregunta_06()
pregunta_07()
pregunta_08()
pregunta_09()
pregunta_10()
pregunta_11()
pregunta_12()