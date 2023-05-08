
import math
import os

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
x=0
loty = ((a,b) for a in ports for b in ports)    #wszystkie loty każdy z każdym
for n in loty:
    print(n)
    x= x + 1
print(x)
x=0
loty = ((a,b) for a in ports for b in ports if a!=b)
for n in loty:
    print(n)
    x= x+1
print(x)

loty = [(a,b) for a in ports for b in ports if a<b]     #numer powtórzenia pętli a mniejszy niż b tzn bez powtórzeń
x=0
for n in loty:
    print(n)
    x= x+1
print(x)


var = 10
haslo = "Super silne hasło"
#źródło = 'var + 2'
źródło = '__import__("os").getcwd()'
globalne = globals().copy()         #funkcja globals to słownik więc trzeba skopiować
del globalne['haslo']
wynik = eval(źródło, globalne)
print(wynik)


#print(globals())




wzory = '2*x'

#wzory = 'math.sin(x)'

#wzory = '3*x**2+2*x-4'
'''
lista = []
wzor = input("wpisz wzór funkcji korzystając z argumentu x : ")
for i in range(100):
    lista.append(i*0.1)
   
for x in lista:
    wynik = eval(wzor)      #dla każdego x z listy 0.1, 0.2, 0.3... 9.9, 10 podstawia formułę wzoru podaną przez eval
    print(wynik)
'''
var = 10
source = '''            #definicja dowolnej funkcji w wielu linijkach 
vax = 0
for i in range(var):
    print('_'*i)
    vax+=1
'''

result = exec(source)   #uruchomienie programu ze zmiennej
print(result)           #funkcja exec nic nie zwraca
print(var)              #zmienna została podstawiona 


pliki_do_wykonania = [
    r'C:\Users\Andrzej\Desktop\kurs Python\exec1.py',
    r'C:\Users\Andrzej\Desktop\kurs Python\exec2.py'
]
print(os.path.basename(pliki_do_wykonania[0]))
print(os.path.basename(pliki_do_wykonania[1]))
for pos,i in list(enumerate(pliki_do_wykonania)):
    if os.path.isfile(i):
        with open(pliki_do_wykonania[pos], 'r') as file: 
            source = file.read()
            exec(source)
            