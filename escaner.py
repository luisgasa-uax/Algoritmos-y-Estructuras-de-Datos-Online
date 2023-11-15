# -*- coding: utf-8 -*-

# https://proyectoa.com/script-sencillo-para-escanear-rango-ip-con-python-en-windows-y-linux/

import os
import platform
import socket
import json  # para serializar objetos
from datetime import datetime


def escribir_objeto_a_archivo(objeto, nombre_archivo):
    # Convertir el objeto a una cadena de texto JSON
    objeto_serializado = json.dumps(objeto, indent=4)

    # Escribir el objeto serializado en un archivo
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(objeto_serializado)


def get_fecha_actual_formateada():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def guardar_lista_en_archivo(lista, nombre_archivo):
    with open(nombre_archivo, 'a') as archivo:
        for elemento in lista:
            archivo.write(str(elemento) + '\n')


def escanear_puertos(ip, puerto_inicio, puerto_fin):
    for puerto in range(puerto_inicio, puerto_fin + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # Timeout de 1 segundo
        ips_puertos = {}
        try:
            s.connect((ip, puerto))
            print(f"El puerto {puerto} está abierto.")
            ips_puertos[puerto] = 'abierto'
            guardar_lista_en_archivo(ips_puertos, 'ips_puertos.csv')
        except socket.error:
            # print(f"El puerto {puerto} está cerrado o filtrado.")
            pass
        finally:
            s.close()


def validar_rangos(rango_inicial, rango_final):
    if rango_inicial < 0:
        return False
    if rango_inicial > 255:
        return False
    if rango_final < 0:
        return False
    if rango_final > 255:
        return False
    if rango_final < rango_inicial:
        return False
    return True


def comando_ping():
    so = platform.platform()
    comando = ''
    if 'Windows' in so:
        comando = 'ping -n 1 -w 10 '
    if 'Linux' in so:
        comando = 'ping -c 1 '
    if 'Darwin' in so:  # MacOS
        comando = 'ping -c 1 '
    return comando


# red = input("Dime la red: ")
red = ''
if red == "":
    red = "192.168.1"
red = "192.168.248"  # comentario de una línea

listaIP = []
listaEquiposOnline = []

'''
Comentario
de 
párrafo
'''

'''
rangoInicial = int(input("Dame el rango inicial: "))
rangoFinal =  int(input("Dame el rango final: "))
'''
rangoInicial = 184
rangoFinal = 184

if not validar_rangos(rangoInicial, rangoFinal):
    print("ande vas!!!???")
else:
    # listaIP = []
    for i in range(rangoInicial, rangoFinal + 1):
        unaIP = red + '.' + str(i)
        # print(unaIP)
        listaIP.append(unaIP)

if len(listaIP) != 0:
    comando = comando_ping()
    for ip in listaIP:
        comando_completo = comando + ip + ' 1> nul'  # redirigimos la salida de pantalla al vacío
        # print( comando_completo )
        respuesta = os.system(comando_completo)
        if respuesta == 0:
            listaEquiposOnline.append(ip)

print('IPs que han respondido')
print(listaEquiposOnline)

print(get_fecha_actual_formateada())
escribir_objeto_a_archivo(listaEquiposOnline, 'equipos_online_' + get_fecha_actual_formateada())
guardar_lista_en_archivo(listaEquiposOnline, 'equipos_online_csv' + get_fecha_actual_formateada())

for ip in listaEquiposOnline:
    escanear_puertos(ip, 1, 50)