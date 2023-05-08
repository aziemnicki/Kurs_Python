import time
import math
import os
'''
source = 'raport+=1'
raport = 0
czas = time.time()
for i in range(100000):
    exec(source)
stop = time.time()
czas_bez_comp = stop - czas

# kod do wykonania, ścieżka dostępu dająca info o błędzie,
sourceComp = compile(source, 'internal variable source', 'exec')
czas = time.time()
for i in range(100000):  # co ma sie wykonać z programem wywoływanym tą metodą
    exec(sourceComp)
stop = time.time()
czas_comp = stop - czas

print(czas_bez_comp)
print(czas_comp)
print(czas_bez_comp/czas_comp)

formuly = [
    "abs(x**3 - x**0.5)",
    "abs(math.sin(x) * x**2)"
]
argumenty = []
for i in range(1000000):
    argumenty.append(i/10)

for i in formuly:
    rezultaty = []
    print(i)
    start = time.time()
    for x in argumenty:
        rezultaty.append(eval(i))
    print(f'min - {min(rezultaty)} max - {max(rezultaty)}')
    stop = time.time()
    print(f'czas - {stop - start}')

argumenty = []
for i in range(1000000):
    argumenty.append(i/10)

for i in formuly:
    rezultaty = []
    print(i)
    start = time.time()
    formula_comp = compile(i, 'inter. var.', 'eval')  # kompilacja formuły
    for x in argumenty:
        rezultaty.append(eval(formula_comp))
    print(f'min - {min(rezultaty)} max - {max(rezultaty)}')
    stop = time.time()
    print(f'czas - {stop - start}')
'''


def show(how_many, char='*', *args, **kwargs):
    print(char*how_many)
    print(args)
    print(kwargs)


# args-wiele argumentów dodawanych, kwargs-nazwa+argument
def zakupy(jakie, sklepy, *args, **kwargs):
    print(jakie, sklepy)
    print(args)
    print(kwargs)


show(10)
show(15)
show(30)

show(10, '-')
show(15, '+')
zakupy('V', 'pies', 'pióro', 'szkielet', sklep='aldi', marka='adidas')
produkty = ['chleb', 'ser', 'jajka']
parametry = {'cena': 'niska', 'czas': 'potem'}

zakupy("kup mi", 'wódke', *produkty, **parametry)


def kalk(eff, *args):
    pow = sum(args)
    ilosc = eff*pow
    print(f'Potrzeba {ilosc} litrów farby')


kalk(5, 32, 17, 15, 8)
pokoje = [24, 51, 15, 30]
kalk(2.58, *pokoje)


def log_it(*args):
    path = r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\argumenty.txt'

    with open(path, 'a') as file:  # musi być 'a', bez tego nie można otworzyć pliku
        for a in args:
            file.write(a)
            file.write(' ')
        file.write('\n')


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')
