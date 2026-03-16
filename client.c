#include <stdio.h>
#include <stdlib.h>
#include "deafult.h"

// Network
#include <sys/socket.h>
#include <netinet/in.h>


int createSocket_test(i32 adressIP, i16 portNumber) {
    struct sockaddr_in serverAddress;

    // CREATE SOCKET
    i64 priv_socketClient = socket(AF_INET, SOCK_STREAM, 0);
    i64 priv_status = 0;

    if (priv_socketClient < 0) {
        perror("ERROR:      Socket creation failed!");
        exit(EXIT_FAILURE);
    }

    // BIND IP, PORT
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_port = htons(portNumber);
    serverAddress.sin_addr.s_addr = adressIP;
    serverAddress.sin_zero[8] = '\0';


    priv_status = connect(priv_socketClient, (struct sockaddr*)&serverAddress, sizeof(serverAddress));
    if (priv_status < 0) {
        perror("ERROR:      Couldn't connect with the server");
        exit(EXIT_FAILURE);
    }
    
    return priv_socketClient;
}

int main() {

    char *message = "Hello World from client!";
    char buffer[1024];

    i64 socketMain = createSocket_test(0, 4444);

    write(socketMain, message, 25);
    read(socketMain, buffer, 1024);
    printf("Message from server: %s \n", buffer);
    close(socketMain);

    return 0;
}