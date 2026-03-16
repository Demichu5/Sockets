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
ip_address = '127.0.0.1'        #adres serwera
port = 81                       #port serwera
buffer = 1024                   #buffer wiadomości w bitach
kodowanie = 'utf-8'             #kodowanie wiadomości
#Zmienne-poboczne
MESSAGE_TO_SERVER = ''
MESSAGE_FROM_SERVER = ''

#----------|--------------------|--------------------|----------
#Funkcje / Klasy
def send(msg_to_server):
    MESSAGE_TO_SERVER = msg_to_server.encode(kodowanie)
    client_side.send(MESSAGE_TO_SERVER)

def recv(msg_from_server):
    MESSAGE_FROM_SERVER = msg_from_server.decode(kodowanie)
    print(f"[SERVER]> {msg_from_server}")

#----------|--------------------|--------------------|----------
#System
if(platform.system() == 'Linux'):
    system_operacyjny = 'clear'

elif(platform.system() == 'Windows'):
    system_operacyjny = 'cls'

#----------|--------------------|--------------------|----------
#Konfiguracja
ip_address = str(input("[IP]> "))
port = int(input("[Port]> "))

client_side = s.socket(s.AF_INET, s.SOCK_STREAM)    #zmienna która jest konstruktorem socketu aby działał
ip_and_port = (ip_address, port)                    #zmienna która jest połączeniem dwóch innych zmiennych
client_side.connect(ip_and_port)                    #połączenie do serwera

os.system(system_operacyjny)
print("--------------------")
print(f"[ip] {ip_address}")
print(f"[port] {port}")
print(f"[buffer] {buffer}")
print(f"[kodowanie] {kodowanie}")
print(f"[os] {platform.system()}")
print("--------------------")
print("Połączono z serwerem")

#----------|--------------------|--------------------|----------
#Pętla główna programu
while True:
    MESSAGE_TO_SERVER = ''              #Czyszczenie zmiennej
    MESSAGE_FROM_SERVER = ''            #Czyszczenie zmiennej

    command = str(input(">>> "))        #Czekanie na użytkownika
    if(command == '!exit')or(command == '!shutdown'):
        send(command)
        break

    else:
        send(command)

    try:
        recv()

    except:
        pass

client_side.close()