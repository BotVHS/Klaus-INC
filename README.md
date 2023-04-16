# Klaus INC. 
Esta script en Python es una herramienta para realizar ataques a correos electrónicos a través de peticiones a diferentes APIs de verificación de correo electrónico. Su objetivo es enviar una cantidad específica de peticiones a la dirección de correo electrónico proporcionada.

# Requerimientos
Este script requiere la instalación de Python 3 y las bibliotecas `requests` y `argparse`.
Puede instalar estas bibliotecas utilizando el siguiente comando en su terminal:

```pip install requests argparse```

# Como usar
El script se puede ejecutar desde la línea de comandos con los siguientes argumentos opcionales:

- Uso: 
    ```bash email_bomber.py [-h] [email] [cantidad]
    ```

Realizar peticiones a la API de Verificación de correo

Argumentos Posicionales:
    `email`     -  Correo electrónico al que se enviarán las peticiones
    `cantidad`  -  Cantidad de peticiones que se desean realizar

Argumentos Opcionales:
    `-h` `--help`  -  Muestra el mensaje de ayuda

Si no se especifica el correo electrónico y la cantidad de peticiones a través de los argumentos, el script le solicitará esta información durante la ejecución.

# Ejemplo de Uso

```python email_bomber.py ejemplo@gmail.com 5```
Este comando enviará 5 peticiones al correo electrónico ejemplo@gmail.com utilizando API's. Si no se especifican los argumentos, el script solicitará la información necesaria durante la ejecución.
