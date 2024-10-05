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
    with open("data.csv") as file:
        datos = file.readlines()
    
    totalA = 0
    for x in datos:
        totalA = totalA + int(x.split('\t')[1])
    return totalA


def pregunta_02(data):
    conteo_por_letra = {}
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
    with open(data, 'r') as archivo:
        lineas = archivo.readlines()
    for linea in lineas[0:]:
        valores = linea.strip().split(',')
        valores_nuevos = valores[0].strip().split('\t')
        letra = valores_nuevos[0] 
        if letra in conteo_por_letra:
            conteo_por_letra[letra] += 1
        else:
            conteo_por_letra[letra] = 1

        resultado_ordenado = sorted(conteo_por_letra.items())


    return resultado_ordenado


data = 'data.csv' 
resultado = pregunta_02(data)
print(resultado)


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
    with open("data.csv") as file:
        datos = file.readlines()
    
    totalA = 0
    totalB = 0
    totalC = 0
    totalD = 0
    totalE = 0
    
    Lista = [0,0,0,0,0]
    for x in datos:
        if x.split('\t')[0] == "A":
            totalA = totalA + int(x.split('\t')[1])
            Lista[0]=("A",totalA)
        elif x.split('\t')[0] == "B":
            totalB = totalB + int(x.split('\t')[1])
            Lista[1]=("B",totalB)
        elif x.split('\t')[0] == "C":
            totalC = totalC + int(x.split('\t')[1])
            Lista[2]=("C",totalC)
        elif x.split('\t')[0] == "D":
            totalD = totalD + int(x.split('\t')[1])
            Lista[3]=("B",totalD)
        else:
            totalE = totalE + int(x.split('\t')[1])
            Lista[4]=("E",totalE)
    print(Lista)
    return Lista



def pregunta_04(data): 
    conteo_por_mes = {}
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

    with open(data, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas[1:]: 
            columnas = linea.strip().split(",")
            columnas_nuevas = columnas[0].strip().split('\t')
            if  len(columnas_nuevas) >= 3: 
                    fecha = columnas_nuevas[2].strip()
                    if len(fecha) == 10 and fecha[4] == '-' and fecha[7] == '-':
                        mes=fecha[5:7]  
                        if mes in conteo_por_mes: 
                            conteo_por_mes[mes] += 1
                        else: 
                            conteo_por_mes[mes] = 1 
        resultado = dict(sorted(conteo_por_mes.items()))
    return resultado

data = 'data.csv'
resultado = pregunta_04(data)
print(resultado)


    



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
    with open("data.csv") as file:
        datos = file.readlines()

    Lista = []
    Lista_1 = []
    for x in datos:
        A = x.split('\t')[0]
        i=0
        for y in datos:
            if y.split('\t')[0] == A:
                n = int(y.split('\t')[1])
                Lista_1.append(n)
        
        max_value = max(Lista_1)
        min_value = min(Lista_1)
        if (A, max_value, min_value) not in Lista:
            Lista.append((A, max_value, min_value))
        Lista_1 = []
    Lista.sort()
    return Lista



def pregunta_06(data):
    valores_por_clave = {}
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
    with open(data, 'r') as archivo: 
        lineas = archivo.readlines()
        
        for linea in lineas[0:]: 
            
            columnas_nuevas = linea.strip().split('\t')
            
            
            if len(columnas_nuevas) >= 5: 
                columna_5 = columnas_nuevas[4].strip()
                pares = columna_5.split(',') 
                for par in pares: 
                    try: 
                        clave, valor = par.split(':') 
                        clave = clave.strip()  
                        valor = float(valor.strip())  
                        if clave not in valores_por_clave: 
                            valores_por_clave[clave] = [] 
                        valores_por_clave[clave].append(valor) 
                    except ValueError: 
                        continue  
         # Calcular el valor mínimo y máximo para cada clave 
    resultado_lista = []  
    for clave, valores in valores_por_clave.items(): 
        min_val = min(valores)
        max_val = max(valores)
        resultado_lista.append((clave, min_val, max_val))
        
    resultado_lista = sorted(resultado_lista) 
    return resultado_lista             
    
data = 'data.csv' 
resultado =  pregunta_06(data)
print(resultado)




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
    with open("data.csv") as file:
        datos = file.readlines()
    
    Lista_num=[]
    for z in datos:
        if int(z.split('\t')[1]) not in Lista_num:
            Lista_num.append(int(z.split('\t')[1]))
    Lista_num.sort()

    Lista_aux = []
    Lista_tupla = []
    for x in Lista_num:
        for y in datos:
                if x==int(y.split('\t')[1]):
                    Lista_aux.append(y.split('\t')[0])
        Lista_tupla.append((x, Lista_aux))
        Lista_aux = []

     
    return Lista_tupla

def pregunta_08(data): 
    
    asociaciones = {}
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
    #por qué no funcionaaaaaaaaaaaaaaaaa :/ 
    with open(data, 'r') as archivo: 
        lineas = archivo.readlines() 
    for linea in lineas[0:]:        
        columnas = linea.strip().split('\t')  
        letra_columna_1 = columnas[0].strip()  
        if len(columnas) >= 2:  #if valor_columna_2
            letra_columna_1 = columnas[0].strip()  
            valor_columna_2 = columnas[1].strip()
            
            if valor_columna_2 not in asociaciones: 
                    asociaciones[valor_columna_2] = set()
            asociaciones[valor_columna_2].add(letra_columna_1)
            lista_resultado = [] 
            for valor, letras in asociaciones.items(): 
                lista_resultado.append([valor, sorted(letras)]) 
            lista_resultado = sorted(lista_resultado, key=lambda x: x[0])
    return lista_resultado 
            
data = 'data.csv'  
resultado = pregunta_08(data)
print(resultado)

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
    with open("data.csv") as file:
        datos = file.readlines()
    

    Lista_keys=[]
    Lista_keys1=[]
    for z in datos:
        Lista_keys1.append(z.split('\t')[4])

    Lista_aux1=[]
    for x in Lista_keys1:
        Lista_aux1.extend(x.split(","))

    Lista_aux2=[]
    for y in Lista_aux1:
        Lista_aux2.extend(y.split("\t"))
        
    for x in Lista_aux2:
        if x[:3] not in Lista_keys:
            Lista_keys.append(x[:3])
    Lista_keys.sort()

    i=0
    dic = {}
    for x in Lista_keys:
        for y in Lista_aux2:
            if y[:3] == x:
                i = i+1
    dic[x] = i
    i=0

    return dic

def pregunta_10(data): 
    resultados = []
 #"""
  #  Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
   # cantidad de elementos de las columnas 4 y 5.

    #Rta/
    #[
     #   ("E", 3, 5),
      #  ("A", 3, 4),
       # ("B", 4, 4),
        #...
      #  ("C", 4, 3),
       # ("E", 2, 3),
        #("E", 3, 3),
    #]


    #"""

    with open(data, 'r') as archivo: 
        lineas = archivo.readlines()
        for linea in lineas[1:]: 
            columnas = linea.strip().split('\t')
            if len(columnas) >= 5: 
                letra_columna_1 = columnas[0].strip() 
                columna_4 = columnas[3].strip() 
                columna_5 = columnas[4].strip()
           
                cantidad_columna_4 = len(columna_4.split(',')) if columna_4 else 0 
                cantidad_columna_5 = len(columna_5.split(',')) if columna_5 else 0
        
            resultados.append([letra_columna_1, cantidad_columna_4, cantidad_columna_5])  
    return resultados
data = 'data.csv' 
resultado = pregunta_10(data)
print(resultado)

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
    with open("data.csv") as file:
        datos = file.readlines()

    Lista_Key = []
    for z in datos:
        Lista_Key.append(z.split('\t')[3])
    
    Lista_Key3 = []
    for x in Lista_Key:
        Lista_Key3.append(x.split(","))

    Lista_Key2 = []
    for x in Lista_Key:
        Lista_Key2.extend(x.split(","))

    List = []
    for x in Lista_Key2:
        if x not in List:
            List.append(x)
    List.sort()

    List_num = []
    for x in datos:
        List_num.append(int(x.split('\t')[1]))

    i=0
    dic_1 = {}
    for x in List:
        for j,y in enumerate(Lista_Key3):
            for z in y:
                if z == x:
                    i += List_num[j]
        dic_1[x] = i
        i=0

    print(dic_1)
        
    return dic_1


def pregunta_12(data):
    suma_por_clave = {}
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
    with open(data, 'r') as archivo: 
        
        lineas = archivo.readlines() 
        for linea in lineas [0:]: 
            columnas = linea.strip().split('\t')
         
            clave_columna_1 = columnas[0].strip() 
        
            valor_columna_5 = columnas[4].split(',')
            total=0
            for j in valor_columna_5:
                  valores=j.split(":")
                  total+=float(valores[1])                  
            if clave_columna_1 in suma_por_clave: 
                        suma_por_clave[clave_columna_1] += total 
            else: 
                    suma_por_clave[clave_columna_1] = total 
        
            ordenado = sorted(suma_por_clave.items())                          
    return ordenado
data = './data.csv' 
resultado = pregunta_12(data)
print(resultado)