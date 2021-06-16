import random
import string
import os

def clear():
    os.system('color a')
    os.system('cls')
clear()
print('Password generator')

L = int(input('\nHvor mange ord skal din adgangs kode være på: '))

små = string.ascii_lowercase
store = string.ascii_uppercase
tal = string.digits
symboler = string.punctuation

alle = små + store + tal + symboler

rando = random.sample(alle,L)

adgangskode = "".join(rando)

clear()
print('\n-----------------------------')

print('\nAdgangskode: ' + adgangskode)

print('\n-----------------------------')