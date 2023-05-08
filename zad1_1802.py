#operacje na zmiennych
a=b=c=10
print(a, id(a), b, id(b), c, id(c))
a=25
print(a, id(a), b, id(b), c, id(c))
a=b=c=[5, 10, 15]
print(a, id(a), b, id(b), c, id(c))
a.append(20)
print(a, id(a), b, id(b), c, id(c))

#zmienne mutable i immutable
x = 10
y = 10
print(id(x), id(y))
y+=1-1
print(id(x), id(y))
y+=124567890-1234567890
print(id(x), id(y))

#listy
days = ['mon','tue','wed','thu','fri','sat','sun']
workdays = days.copy()
workdays = workdays[:5]     #można tez .remove('sat')   .remove('sun')
print(days)
print(workdays)

#konwersja na typ logiczny True False
wybor = 1
opcje = ['load data', 'export data', 'analyze&predict']
def print_opcje(opcja):
    for i in range(len(opcja)):
        print("{} - {}".format(i+1, opcja[i]))      #między { } wstawiany jest i+1 oraz wartość tabeli opcje
    opcja = input("Wybierz jedną z opcji lub wciśnij enter")
    return opcja
        
while (wybor):
    wybor = print_opcje(opcje)
    if (wybor != ''):
        try:
            wybor_int = int(wybor)
        except:
            print('Należy podać liczbę')
        if wybor_int >0 and wybor_int < 4:
            print("{} - {}".format('Wybrano opcję', opcje[wybor_int-1]))
        else:
            print('Podano liczbe z poza zakresu, wybierz inną.')

    else:
        print('Do widzenia')
        break
    
    
