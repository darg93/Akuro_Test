Este repositorio cuenta con la solución propuesta por mi persona, para el taller-entrevista de la empresa Akuro SAS,
la solución se saba en un archivo para cada uno de los problemas propuesto de los cuales se tienen los siguientes comentarios y/o aclaraciones:

punto1.py:

Muestra la validación de una cadena específica de caracteres haciendo uso de tres validadores booleanos, uno para verificar si la primera letra es mayúscula o con ampersant, el otro para verificar si hay una separación por asteríscos, y la otra para verificar que el resto de cadena de caractéres seán minúsculas, guiónes bajos o guiónes medios. Esto se hace descartando los caracteres adicionales usando el código ASCII

punto2.entrada.json & punto2.py:

El archivo .json se encarga de dar la entrada en el formato indicado en el problema, mientras que el código python se encarga de leer la información del .json, convertirla a un formato de fecha y sumarle 22 días para luego imprimir el resultado en el formato de fecha indicado.

punto3.py:

Este código se encarga de realizar una lectura a la información de la API propuesta para extraer la información que contiene datos curiosos para gatos, y de la misma manera mostrarlos en pantalla.

punto4.py:

Este código contiene un controlador en Flask que permite realizar un webhook para mostrar en pantalla la información solicitada por el usuario. La forma de ejecutar este código es:

*Instalar Flask en la terminal de linux: https://flask.palletsprojects.com/en/1.1.x/installation/
*En la terminal inicilizar el servidor haciendo uso de los siguientes comandos:
    export FLASK_APP=punto4.py
    python3 -m flask run
*Abrir en el navegador cambiando las XXXXXX por el número entero de id y del monto especificamente
    127.0.0.1:5000/procesingEndpoint?id=XXXXXX&mount=XXXXXX

Automáticamente el sistema mostrará la información solicitada en formato json que es:
{"success":"OK", "total"=mount*id/4}


punto5.txt:

Muestra las definiciones cortas de los comandos solicitados


punto6.txt:

Muestra las diferentes frases que se pueden construir con el lenguaje propuesto


punto7.txt:

Muestra la explicación de cómo se podría incluir una imágen en el footer de un documento haciendo uso de Apps Script
