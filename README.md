# Network Socket Programming (C & Python)

A collection of network communication implementations in a Client-Server architecture, demonstrating low-level TCP/IP stack handling (POSIX Sockets) and high-level implementations in Python.

---
```
### 1. Overview
The project showcases bidirectional communication between processes using both compiled and interpreted languages.
It covers the full lifecycle of a network connection, from socket creation to secure descriptor termination.
```
---
```
### 2. Key Features
- Multi-threaded Server (Python): Concurrent handling of multiple client connections using the threading library.
- Low-level C Sockets: Implementation of basic networking primitives using sys/socket.h.
- Connection Management: Robust implementation of bind, listen, and accept mechanisms.
- Endianness Handling: Correct use of htons to ensure Network Byte Order compatibility across different architectures.
- Protocol Design: Implementation of custom control commands such as !exit and !shutdown to manage remote processes.
```
---
```
### 3. Technical Implementation

Python Implementation:
- Socket Type: AF_INET (IPv4), SOCK_STREAM (TCP).
- Threading: Each new connection triggers a separate thread to maintain server responsiveness.
- Buffering: Default 1024-bit message buffer using UTF-8 encoding.

C Implementation:
- API: POSIX Sockets.
- Options: Utilization of SO_REUSEADDR to allow immediate socket rebinding after server restarts.
- Data Flow: Implementation of read/write and send/recv calls for synchronous data exchange.
```
---
```
### 4. Project Structure
- server.c / client.c: Low-level POSIX-compliant source files for C implementations.
- app_server.py / app_client.py: High-level Python scripts for multi-threaded communication.
- default.h: Common header file used for C type definitions (e.g., i32, i64).
```
---
---
```
### 5. Learning Outcomes
- Advanced understanding of the Berkeley sockets API.
- Thread synchronization in a network environment.
- Handling of file descriptors and system-level error reporting (perror).
- Practical experience with cross-platform differences in networking and system shells.
```
---
Created by Demichu5
