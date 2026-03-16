#!/usr/bin/python3
# -*- coding: utf-8 -*-

#----------|--------------------|--------------------|----------
#Biblioteki
import socket as s  #sieć
import threading    #wątki
import os           #system/shell
import platform     #platforma systemowa

#----------|--------------------|--------------------|----------
#Zmienne
ip_address = '127.0.0.1'    #adres ip serwera
port = 81                   #port serwera
buffer = 1024               #buffer wiadomości w bitach
kodowanie = 'utf-8'         #kodowanie wiadomości
command = ''

#----------|--------------------|--------------------|----------
#Funkcje / Klasy
def client(connection, address):
    global command

    print(f"Nowe połączenie od {address}")

    connected_client = True
    while connected_client:
        msg = connection.recv(buffer).decode(kodowanie)
        if msg == '!exit':
            print(f"Adres:{address} się rozłączył")
            connected_client = False

        elif msg == '!shutdown':
            print(f"Adres:{address} się rozłączył")
            command = '!shutdown'
            connected_client = False

        elif msg:
            print(f"Adres:{address}> {msg}")

    connection.close()
    print(f"Aktualnie połączenia : {threading.active_count() - 2}")
    return

        

def server():
    while True:
        global connection, address

        if command == '!shutdown':
            break

        else:
            connection, address = server_side.accept()
            multi_connection = threading.Thread(target=client, args=(connection, address))
            multi_connection.start()
            print(f"Aktywne połączenia : {threading.active_count() - 1}")

    return

#----------|--------------------|--------------------|----------
#System
if(platform.system() == 'Linux'):
    system_operacyjny = 'clear'

elif(platform.system() == 'Windows'):
    system_operacyjny = 'cls'

#----------|--------------------|--------------------|----------
#Program
server_side = s.socket(s.AF_INET, s.SOCK_STREAM)    #zmienna która jest konstruktorem socketu aby działał
ip_and_port = (ip_address, port)                    #zmienna która jest połączeniem dwóch innych zmiennych
server_side.bind(ip_and_port)                       #Utworzenie serwera na podstawie adresu ip oraz portu
server_side.listen()                                #Nasłuchiwanie połączeń w sieći

os.system(system_operacyjny)
print("--------------------")
print(f"[ip] {ip_address}")
print(f"[port] {port}")
print(f"[buffer] {buffer}")
print(f"[os] {platform.system()}")
print("--------------------")

server()