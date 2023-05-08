banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]

dict_nominal = {}
for k in banknotes_coins:
    dict_nominal[k] = 0

dict_nominal[100] += 1
dict_nominal[20] += 1
dict_nominal[5] += 1
dict_nominal[0.5] += 1
 
dict_nominal[50] += 1
dict_nominal[20] += 2
dict_nominal[5] += 1
dict_nominal[2] += 200000
 
dict_nominal[100] += 1
dict_nominal[50] += 1
dict_nominal[2] += 1

for d in sorted(dict_nominal.keys()):                   #sortowanie od najniższych do najwyższych nominałów
    print(f"Nominał: {d:6.2f} - ilość {dict_nominal[d]}")    #w {} jest format do 6 miejsc liczby oraz 2 po przecinku
    
 #  ZAGNIEŻDŻANIE LISTY i pętli
lista = list(range(5))
listb = list(range(5))
wynik = []

for a in lista:
    for b in listb:
         wynik.append((a,b))
print(wynik)
print(30*'*')
wynik = [(a,b) for a in lista for b in listb]               #wypisz wszystkie możliwe wartości tupletów 
print(wynik)
print(30*'_')
wynik=[(a,b) for a in lista for b in listb if a%2 ==0 and b%2 ==1]      #wypisz tuplety gdzie a- parzyste i b- nieparzyste
print(wynik)

wynik={a:b for a in lista for b in listb if a%2 ==0 and b%2 ==1}        #zagnieżdżanie słownika nadpisuje wartość w kluczu
print(wynik)

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

loty = [(a,b) for a in ports for b in ports]    #wszystkie loty każdy z każdym
print(loty)
print(len(loty))

loty = [(a,b) for a in ports for b in ports if a!=b]    #wszystkie loty oprócz sam do siebie
print(loty)
print(len(loty))

loty = [(a,b) for a in ports for b in ports if a<b]     #numer powtórzenia pętli a mniejszy niż b tzn bez powtórzeń
print(loty)
print(len(loty))


gen = ((a,b) for a in lista for b in listb if a%2 ==0 and b%2 ==1)      #tworzenie generatora
print(wynik)
print(next(gen))
print(next(gen))
for x in gen:           #po przejściu całego generatora nie można go odnowić, trzeba jeszcze raz wywołać
    print(x)

gen = ((a,b) for a in lista for b in listb if a%2 ==0 and b%2 ==1) 
while True:
    try:
        print(next(gen))
    except StopIteration:       #po zwróceniu błędu iteracji zatrzymuje pętlę
        print('stop')
        break