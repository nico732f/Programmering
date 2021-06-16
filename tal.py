import os
import random
import keyboard

def clear():
    os.system('color a')
    os.system('cls')
def start():
    print('Du skal vælge et tal mellem 1 & 10')
    tal = random.randint(1,10)
    gæt = int(input('\nIndsæt dit gæt: '))


    if gæt == tal:
        print(f'\nDet rigtige tal [{tal}]')
        print(f'Dit gæt [{gæt}]')

        print('\nTillykke du vandt')
        while True:
            if keyboard.is_pressed('delete'):
                start()
    if gæt != tal:
        print(f'\nDet rigtige tal [{tal}]')
        print(f'Dit gæt [{gæt}]')

        print('\nDu tabte')
        while True:
            if keyboard.is_pressed('delete'):
                start()



start()









