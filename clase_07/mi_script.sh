#!/bin/bash

# Completar este archivo para que realice las siguientes actividades:
# 1. Descargar el fichero laboratorio_7.tgz
#curl -L -o laboratorio_7.tgz https://....
tar -xzf laboratorio_7.tgz # generaba una carpeta llamada labotario_7

# 2. Imprimir el contenido del archivo1.txt
cat laboratorio_7/archivo1.txt

# 3. Buscar la palabra 'registro' en archivo2.txt
grep registro laboratorio_7/archivo2.txt

# 4. Crear una variable local llamada 'LOCAL_VAR' con el valor de 'amarillo azul rojo'
LOCAL_VAR=(amarillo azul rojo)

# 5. Agregar el valor 'verde' en la posición 3, e imprimir la variable con todos los valores.
LOCAL_VAR[3]=verde

echo -n El valor de la variable LOCAL_VAR es: 
echo ${LOCAL_VAR[*]}