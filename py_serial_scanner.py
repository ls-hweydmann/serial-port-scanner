# Hubert Weydmann
#
#   skrypt próbuje otworzyć każdy z portów COM w zakresie COM1-COM99,
#   następnie wypisuje te, które można otworzyć
#   po sekundzie powtarza całą operację
#   i tak do końca świata
#   albo do chwili zamknięcia terminala

import serial as s
import time
from os import system
#system('mode con: cols=27 lines=20')

STARTCOM = 1    # tu można zmieniać zakres skanowania,
ENDCOM = 99     # ale raczej nie ma potrzeby


p = 'COM{}'
pr = '*   - {}                *'
ports = []
print('\n\n')
for i in range(STARTCOM, ENDCOM + 1):
    ports.append(p.format(i))

while True:
    system("cls")
    print("***************************")
    print("*                         *")
    print("*   Dostępne porty COM:   *")
    print("*                         *")
    for port in ports:
        try:
            ser = s.Serial()
            ser.port = port
            ser.open()
            ser.close()
            print(pr.format(port))
        except s.serialutil.SerialException:
            pass
    print("*                         *")
    print("***************************")
    print("\nodświeżam co 1s...\n")

    time.sleep(1)
