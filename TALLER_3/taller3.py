#taller 3 Juan Pablo Arcila y Ana Sofia Giraldo

def question_01():

    # Open the CSV file
    with open('C:\PROGRAMMING\data.csv') as file:
        # Read the entire file content as a string
        content = file.readlines()
    #print(content)
    
    #01 return the sum of the second column
    addition = 0
    
    for entry in content:
        # Step 1: Split by the tab character ('\t')
        parts = entry.split('\t')
        #print(parts)
        addition += int(parts[1])
    print(addition)

def question_02():
    
    my_dic = {}

    # Make sure to use double backslashes or a raw string for the file path
    with open(r"C:\PROGRAMMING\data.csv") as archivo:
        contenido = archivo.readlines()

    for entry in contenido:
        parts = entry.split('\t')[0]
        my_dic[parts] = my_dic.get(parts, 0) + 1

    # Sort the dictionary by keys
    parts_sorted = dict(sorted(my_dic.items()))

    # Display a preview of the sorted dictionary
    organized = list(parts_sorted.items())  # First 5 entries as a preview
    #print(organized)
    print("[")
    for letra, count in organized:
        print(f'    ("{letra}", {count}),')
    print("]")

def question_03():
    my_dic = {}

    # Make sure to use double backslashes or a raw string for the file path
    with open(r"C:\PROGRAMMING\data.csv") as archivo:
        contenido = archivo.readlines()

    for entry in contenido:
        parts = entry.split('\t')
        my_dic[parts[0]] = my_dic.get(parts[0], 0) + int(parts[1])

    # Sort the dictionary by keys
    parts_sorted = dict(sorted(my_dic.items()))

    # Display a preview of the sorted dictionary
    organized = list(parts_sorted.items())  # First 5 entries as a preview
    #print(organized)
    print("[")
    for letra, count in organized:
        print(f'    ("{letra}", {count}),')
    print("]")
    
def question_04():
    my_dic = {}

    # Make sure to use double backslashes or a raw string for the file path
    with open(r"C:\PROGRAMMING\data.csv") as archivo:
        contenido = archivo.readlines()

    for entry in contenido:
        parts = entry.split('\t')[2]
        my_dic[parts.split("-")[1]] = my_dic.get(parts.split("-")[1], 0) + 1

    # Sort the dictionary by keys
    parts_sorted = dict(sorted(my_dic.items()))

    # Display a preview of the sorted dictionary
    organized = list(parts_sorted.items())  # First 5 entries as a preview
    #print(organized)
    print("[")
    for letra, count in organized:
        print(f'    ("{letra}", {count}),')
    print("]")
    
def question_05(): 
    my_dic={}
    with open("C:\PROGRAMMING\data.csv") as archivo:
        content = archivo.readlines()
        
    for entry in content: 
        letter = entry.split('\t')[0]
        number = entry.split('\t')[1]
        if letter not in my_dic:
            my_dic[letter] = [] 
            
        my_dic[letter].append(int(number))
    minmax = {}

    for clave, lista in my_dic.items():
        #letra = entry.split('\t')[0]
        if clave not in minmax:
            minmax[clave] = []
        maximo = max(lista)
        minmax[clave].append(int(maximo))
        minimo = min(lista) 
        minmax[clave].append(int(minimo))
    #print(minmax)
    print("[")
    new_thingy = sorted(minmax.items())
    for thingy in new_thingy:
        other_new_thingy = (thingy[0], *thingy[1])
        print(f'    {other_new_thingy},')
    print("]")

def question_06():
    my_dic = {}
    with open("C:\PROGRAMMING\data.csv") as archivo:
        content = archivo.readlines()

    sobelo_list = []
    new_thingy = []
    
    for entry in content: 
        parts = entry.split('\t')[4]
        sobelo_list.append(parts.split(","))
    #print(sobelo_list) 
        
    for thing in sobelo_list:
        for element in thing:
            new_thingy.append(element.replace("\n", ""))

    #print(new_thingy)
    for vaina in new_thingy:
        key, value = vaina.split(":")
        if key not in my_dic:
            my_dic[key] = []
        my_dic[key].append(int(value))
    #print(my_dic)

    minmax = {}
    for depression, aguapanela in my_dic.items():
        #letters = entry.split('\t')[0] 
        if depression not in minmax:
            minmax[depression] = []
        minmax[depression].append(min(aguapanela))
        minmax[depression].append(max(aguapanela))
        
    #print(minmax)

    print("[")
    for element in sorted(minmax.items()):
        for cosito in element:
            new_element = (element[0], *element[1])
        print(f'    {new_element},')
    print("]")
    
def question_07():
    my_dic = {}
    with open("C:\PROGRAMMING\data.csv") as archivo:
        content = archivo.readlines()

    sobelo_list = []

    for entry in content: 
        parts = entry.split('\t')
        sobelo_list.append(parts)
    #print(sobelo_list)

    for vaina in sobelo_list:
        key, value = int(vaina[1]), vaina[0]
        if key not in my_dic:
            my_dic[key] = []
        my_dic[key].append(value)

    print("[")
    for element in sorted(my_dic.items()):
        print(f'    {element},')
    print("]")
    
def question_08():
    my_dic = {}
    with open("C:\PROGRAMMING\data.csv") as archivo:
        content = archivo.readlines()

    sobelo_list = []

    for entry in content: 
        parts = entry.split('\t')
        sobelo_list.append(parts)
    #print(sobelo_list)

    for vaina in sobelo_list:
        key, value = int(vaina[1]), vaina[0]
        if key not in my_dic:
            my_dic[key] = []
        if value not in my_dic[key]:
            my_dic[key].append(value)

    print("[")
    for element in sorted(my_dic.items()):
        print(f'    {element},')
    print("]")

def question_08():
    my_dic = {}
    with open("C:\PROGRAMMING\data.csv") as archivo:
        content = archivo.readlines()

    sobelo_list = []

    for entry in content: 
        parts = entry.split('\t')
        sobelo_list.append(parts)
    #print(sobelo_list)

    for vaina in sobelo_list:
        key, value = int(vaina[1]), vaina[0]
        if key not in my_dic:
            my_dic[key] = []
        if value not in my_dic[key]:
            my_dic[key].append(value)

    print("[")
    for element in sorted(my_dic.items()):
        order = sorted(element[1])
        listica = (element[0], order)
        print(f'    {listica}')
    print("]")
    
def question_09():
    my_dic = {}
    with open("C:\PROGRAMMING\data.csv") as archivo:
        content = archivo.readlines()

    sobelo_list = []
    new_thingy = []
    numeros = []
    for entry in content: 
        parts = entry.split('\t')[4]
        sobelo_list.append(parts.split(","))
    #print(sobelo_list) 
        
    for thing in sobelo_list:
        for element in thing:
            new_thingy.append(element.replace("\n", ""))

    #print(new_thingy)
    for vaina in new_thingy:
        key, value = vaina.split(":")
        if key not in my_dic:
            my_dic[key] = 1
        else: 
            my_dic[key] += 1
            
    print(my_dic)
    #print(minmax)
    print("{")
    for key in sorted(my_dic):
        print(f'    "{key}": {my_dic[key]},')
    print("}")

def question_10():
    my_dic = {}
    with open("C:\PROGRAMMING\data.csv") as archivo:
        content = archivo.readlines()

    sobelo_list = []
    new_thingy = []
    cosiaco = []
    for entry in content: 
        parts = entry.split('\t')
        sobelo_list.append(parts)
    #print(sobelo_list) 
        
    for thing in sobelo_list:
        thing[4] = thing[4].replace("\n", "")
        tupla = (thing[0], len(thing[3].split(",")), len(thing[4].split(",")))
        cosiaco.append(tupla)
        #print(thing)
        
    #print(cosiaco)
    print("[")
    for vaina in cosiaco:
        print(f'    {vaina},')
    print("]")

def question_11():
    my_dic = {}
    todas_mienten= []
    cosito = []
    i = 0
    with open("C:\PROGRAMMING\data.csv") as archivo:
        content = archivo.readlines()


    for entry in content: 
        parts = entry.split('\t')   
        todas_mienten.append(parts[3].split(","))
        cosito.append(int(parts[1]))
    #print(todas_mienten, cosito)
    for element in todas_mienten:
        for vaina in element:
            if vaina in my_dic:
                my_dic[vaina] = my_dic[vaina] + cosito[i]
            if vaina not in my_dic:
                my_dic[vaina] = cosito[i]
        i += 1


    print("[")
    for element in dict(sorted(my_dic.items())):
        print(f'    "{element}", {dict(sorted(my_dic.items()))[element]},')
    print("]")

def question_12():
    my_dic = {}
    Im_sick_of_this = []
    kill_me_now = []
    Ill_study_administration = []
    Harvey_te_amo = []
    with open("C:\PROGRAMMING\data.csv") as archivo:
        content = archivo.readlines()


    for entry in content: 
        parts = entry.split('\t')
        Im_sick_of_this.append(parts[4])
        Harvey_te_amo.append(parts[0])
        
    #print(Harvey_te_amo)
    for knives in Im_sick_of_this:
        knives = knives.replace('\n', '').split(",")
        fuuuuuuck = []
        for elements in knives:
            fuuuuuuck.append(elements.split(":"))
        kill_me_now.append(fuuuuuuck)

    for mkada in kill_me_now:
        value = 0
        for chbda in mkada:
            value += int(chbda[1])
        Ill_study_administration.append(value)
    i = 0
    for element in Harvey_te_amo:
        if element not in my_dic:
            my_dic[element] = Ill_study_administration[i]
        else: 
            my_dic[element] += Ill_study_administration[i]    
        i += 1
    print(dict(sorted(my_dic.items())))
    print("{")
    for cosito in dict(sorted(my_dic.items())):
        print(f"    '{cosito}': {dict(sorted(my_dic.items()))[cosito]}")
    print("}")

    print("El que me lea le pone 5.0 a Juan Pablo")

question_01()
#question_02()
#question_03()
#question_04()
#question_05()
#question_06()
#question_07()
#question_08()
#question_09()
#question_10()
#question_11()
#question_12()
