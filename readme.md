# PASOS PARA CONFIGURAR EL PROYECTO

* 1. En la raiz del proyecto crear el entorno virtual ejecutando el comando: virtualenv env
* 2. Para activar el entorno creado, en un terminal bash ejecutamos el siguiente comando: source env/bin/activate(Mac)
* 3. Necesitamos instalar una serie de librerias definidas en el archivo **requerimiento.txt** :
    * 3.1 Dentro del entorno virtual, ejecutar el siguiente comando: pip install -r **requerimiento.txt**
    * 3.2 En caso de querer actualizar las versiones del archivo ejecutamos el siguiente comando: pip install -U -r **requerimiento.txt**

> **IMPORTANTE:** Debemos asegurarnos que el Python Interpreter con el que estamos trabajando, sea el del virtualenv que hemos creado.
