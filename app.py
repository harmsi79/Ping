import os
import time


def ping(host):
    response = os.system("ping -c 1 " + host)
    if response == 0:
        return True
    else:
        return False


def main():
    # Zielhostliste definieren
    hosts = ["192.168.212.211", "192.168.212.226", "192.168.212.2"]

    # Protokolldatei öffnen
    with open("ping-aussetzer.log", "a") as logfile:
        # Alle Zielhosts pingen
        while True:
            for host in hosts:
                # Ping-Ergebnis prüfen
                if not ping(host):
                    # Aussetzerprotokollierung
                    logfile.write(f"{time.strftime('%d.%m.%Y %H:%M:%S')}: {host} ist nicht erreichbar\n")


if __name__ == "__main__":
    main()