# Manejo de Python

# %%
help("str")

# %%
cadena = "hola mundo"
print(cadena[0:5])

# %%
# Toma desde la posición 2 hasta la posición 9 excluída
print(cadena[2:9])

# %%
# Toma el valor de la posición 2
print(cadena[2])

# %%
# Toma desde la posición 2 en adelante
print(cadena[2:])

# %%
# Toma desde el inicio hasta la posición 6 incluída
print(cadena[:7])

# %%
# Toma desde la posición -4 (cuento desde la última posición
# 4 caracteres) y tomo de ahi en adelante
# cadena = 'hola mundo'
# La posición -4 es la 'u'
print(cadena[-4:])

# %%
# Toma desde la posición inicial hasta la final
# saltando N caracteres
print("cadena original:\t\t\t", cadena)
print("cadena con slice:\t\t\t", cadena[1:9])
print("cadena con slice saltando 2 posiciones:\t", cadena[::2])
print("cadena con slice saltando 3 posiciones:\t", cadena[1:9:3])

# %%
curso = "curso.python.universidad.eia"

"""
variable[inicio:fin:salto]
rangos vacios --> depende de la posición

si esta derecha --> toma desde  0
si esta a la izquierda --> toma hasta el ultimo
"""
print("0. original                 : ", curso)  # Variable sin modificación
print("1. rangos vacios            : ", curso[::])  # Imprime la cadena normal
print("2. inicia desde             : ", curso[5:])  # Imprime desde la posición 5
print("3. hasta                    : ", curso[:-3])  # Imprime hasta la posición -3
print(
    "4. salteos                  : ", curso[::-2]
)  # Imprime la cadena con saltos de -2
print("5. invertir                 : ", curso[::-1])  # Imprime la cadena invertida
print(
    "6. segmento inverso         : ", curso[7:4:-1]
)  # Imprime un segmento de la cadena invertida

# ### 2.2 Métodos de los string

# %%
demo = "CuRsO PyThon UnIv3rSiD@D EIA"

print("00. variable original  : --> ", demo)
print("01. mayúsculas         : --> ", demo.upper())
print("02. minúsculas         : --> ", demo.lower())
print("03. inicia con         : --> ", demo.startswith("c"))
# concatenar operaciones(metodos) | concatenacion de operaciones finitas
print("04. inicia con         : --> ", demo.lower().startswith("c"))
print("05. capitalize         : --> ", demo.capitalize())
print("06. titulo             : --> ", demo.title())
print("07. centrado           : --> ", demo.center(50, "*"))
print("07. centrado           : --> ", demo.title().center(50, " "))  # centrando
print("08. rjust              : --> ", demo.rjust(50, "*"))
print("09. ljust              : --> ", demo.ljust(50, "*"))
print("10. zfill              : --> ", demo.zfill(50))
print("10. zfill              : --> ", "123".zfill(5))
print("11. remplazar          : --> ", demo.lower().replace("o", "@"))
print("11. remplazar          : --> ", demo.replace("o", "@"))
print("11. contar             : --> ", demo.count("o"))
print("12. contar             : --> ", demo.count("@"))
print("13. buscar             : --> ", demo.lower().find("python"))
print("13. buscar             : --> ", demo.lower().find("python--"))

# %%
help("str.find")

# %%
frase = "clase de hoy de python"
palabra = "de"

frase.find(palabra, 8)

# %%
print("14. longitud cadena    : --> ", len(demo))  # listas, tuplas, strings


espacios_izquierda = "          hola espacios izquierdos"
espacios_derecha = "hola espacios derechos            "
espacios_ambos = "            espacio central       "

print("15. lstrip             : --> ", espacios_izquierda.lstrip())
print("16. rstrip             : --> ", espacios_derecha.rstrip())
print("17. strip              : --> ", espacios_ambos.strip())

# %%
print("len espacios_ambos 1 : --> ", len(espacios_ambos))
print("len espacios_ambos 2 : --> ", len(espacios_ambos.strip()))

# %%
pi = 3.141618

print("18. len numero        : --> ", len(str(pi)))
print("19. es digito         : --> ", "234234".isdigit())
print("19. es digito         : --> ", "a1".isdigit())
print("19. es digito         : --> ", "1f".isdigit())

# %%
help("str.isdigit")

# %%
print("00. variable original : --> ", demo)
print("20. indice            : --> ", demo.index("o"))
print("20. indice            : --> ", demo.find("o"))

# %%
help("str.index")

# %%
help("str.find")

# %%
print("00. variable original : --> ", demo)
print("20. indice            : --> ", demo.find("@"))
print("20. indice            : --> ", demo.index("@"))
