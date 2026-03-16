# Network Socket Programming (C & Python)

Zbiór implementacji komunikacji sieciowej w architekturze Klient-Serwer, demonstrujący obsługę stosu protokołów TCP/IP na poziomie niskopoziomowym (POSIX Sockets) oraz wysokopoziomowym (Python).

##  Funkcjonalności
* **Multi-threaded Server (Python):** Obsługa wielu klientów jednocześnie przy użyciu biblioteki `threading`.
* **Low-level C Sockets:** Implementacja serwera i klienta z wykorzystaniem biblioteki `sys/socket.h`.
* **Zarządzanie połączeniem:** Obsługa mechanizmów `bind`, `listen`, `accept` oraz bezpieczne zamykanie deskryptorów plików.
* **Endianness Handling:** Wykorzystanie `htons` do poprawnej konwersji kolejności bajtów (Network Byte Order).

##  Struktura
* `client.c` / `server.c` – Niskopoziomowa komunikacja w standardzie POSIX.
* `app_client.py` / `app_server.py` – Wielowątkowy system wymiany komunikatów z obsługą komend sterujących (`!exit`, `!shutdown`).

##  Czego się nauczyłem?
* Zarządzania gniazdami i opcjami socketów (`SO_REUSEADDR`).
* Synchronizacji wątków w środowisku sieciowym.
* Projektowania prostych protokołów tekstowych do sterowania zdalnymi procesami.
