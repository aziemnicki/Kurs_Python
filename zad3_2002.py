kolory = ["red", "orange", "green", "violet", "blue", "yellow"]
def colors(lista,ilosc):
    listb= lista.copy()
    return listb[:ilosc]

for i in range(1, len(kolory)+1):
    print(colors(kolory , i))
    
text = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli.'

print(text[10:text.index(')')+1])

workdays = [19, 21, 22, 20, 23]             #lista dni pracujących
months = ['I', 'II', 'III', 'IV', 'V']      #lista miesięcy

enum_days = list(enumerate(workdays))       #ponumerowana lista
enum_months = list(zip(months, workdays))   #połączona lista miesięcy i dni pracujących, składa się z 
                                            #dwóch zmiennych w każdej komórce
                                            
for m, d in enum_days:                      #pętla idzie po dwóch zmiennych naraz
    print('Pozycja', m, 'dni', d)
    
for pos, (m,d) in enumerate(zip(months, workdays)):     #w pętli wykonuje się najpierw numerowanie po zmiennej pos
    print('Pozycja', pos, 'miesiąc', m, 'dni', d)       #następnie pętla idzie przez 2 połączone zmienne naraz
    
    
projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for p ,(d, l) in zip(projects,(zip(dates, leaders))):   #można wielokrotnie pakować listy lub spakować wiele do jednej
    print( 'The leader of ', p, 'started on ', d, 'is ', l)
    
for n, (p,d, l) in enumerate( (zip(projects,dates, leaders))): #spakowana lista 3 parametrów, ponumerowana
    print(n+1,  ' - The leader of ', p, 'started on ', d, 'is ', l)
    
    
miesiace = dict(zip(months,workdays))
for key in miesiace:
    print(f"Klucz to {key} a wartość słownika to {miesiace[key]}")
    
for dane in miesiace.values():
    print(f'Wartosc danych słownika to {dane}')
