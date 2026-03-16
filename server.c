#include <stdio.h>
#include <stdlib.h>
#include "deafult.h"

// Network
#include <sys/socket.h>
#include <netinet/in.h>

int createSocket_test(i32 adressIP, i16 portNumber) {
    i64 priv_socketMain;
    i64 priv_socketClient;
    i64 priv_addressLenght;
    i64 priv_status;
    i64 priv_optionValue = 1;

    struct sockaddr_in serverAddress;
    struct sockaddr_in connectionAddress;

    priv_socketMain = socket(AF_INET, SOCK_STREAM, 0);
    if (priv_socketMain < 0) {
        perror("ERROR:      Socket creation failed!");
        exit(EXIT_FAILURE);
    }

    priv_status = setsockopt(priv_socketMain, SOL_SOCKET, SO_REUSEADDR, &priv_optionValue, sizeof(priv_optionValue));
    if (priv_status < 0) {
        perror("ERROR:      Couldn't set options!");
        exit(EXIT_FAILURE);
    }

    serverAddress.sin_family = AF_INET;
    serverAddress.sin_port = htons(portNumber);
    serverAddress.sin_addr.s_addr = adressIP;
    serverAddress.sin_zero[8] = '\0';

    priv_status = bind(priv_socketMain, (struct sockaddr*)&serverAddress, sizeof(struct sockaddr));
    if (priv_status < 0) {
        perror("ERROR:      Couldn't bind socket!");
        exit(EXIT_FAILURE);
    }

    priv_status = listen(priv_socketMain, 4);
    if (priv_status < 0) {
        perror("ERROR:      Couldn't listen for connections");
        exit(EXIT_FAILURE);
    }

    priv_addressLenght = sizeof(connectionAddress);
    priv_socketClient = accept(priv_socketMain, (struct sockaddr*)&connectionAddress, &priv_addressLenght);
    if (priv_socketClient < 0) {
        perror("ERROR:      Couldn't establish connection with client!");
        exit(EXIT_FAILURE);
    }

    return priv_socketMain, priv_socketClient;
}

int main() {

    i64 socketMain;
    i64 socketClient;

    socketMain, socketClient = createSocket_test(0, 4444);

    char buffer[1024];
    char *firstMessage = "Hello World from server!";

    

    read(socketClient, buffer, 1024);
    buffer[1024] = '\0';
    printf("Message from client: %s \n", buffer);
    send(socketClient, firstMessage, strlen(firstMessage), 0);

    close(socketClient);
    close(socketMain);
    return 0;
}