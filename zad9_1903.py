def double(x):
    return x*2

x = 10
x = double(x)
print(x)

x = 10
f = lambda x: x * 2
print(f(x))


def power(x,y):
    return x ** y

x = 5
y = 3
print(power(x,y))

f = lambda x,y: x ** y
print(f(x,y))

lista = [1, 2, 3, 4, 5, 11, 14, 15 , 21, 20]

def nieparzysta(x):
    return x % 2 != 0

print(nieparzysta(5), nieparzysta(6))

filtr = list(filter(nieparzysta, lista))
print(filtr)

filtr = list(filter(lambda x: x % 2 != 0, lista))
print(filtr)

print(list(filter(lambda x: x % 2 != 0, lista)))        #lambda tworzy funkjcję anonimową, do prostych obliczeń

def generate(n):
    return lambda x: n * x


mul_2 = generate(2)
mul_5 = generate(5)
print(mul_2(13), mul_5(8))

text_list = ['x','xxx','xxxxx','xxxxxxx','']
f = lambda x: len(x)
txt = 'wyrażenie'
print(f(txt))

print(list(map(f, text_list)))
print(list(map(lambda x: len(x), text_list)))

car_01 = {
'carBrand' : 'Seat ',
'carModel' : 'Ibiza',
'carIsAirBagOK' : True,
'carIsPaintingOK' : True,
'carIsMechanicOK' : True
}
car_02 = {
'carBrand' : 'Opel ',
'carModel' : 'Corsa',
'carIsAirBagOK' : False,
'carIsPaintingOK' : True,
'carIsMechanicOK' : False
}

def IsCarDamaged (aCar) :
    return not (aCar['carIsAirBagOK'] and ['carIsPaintingOK'] and ['carIsMechanicOK'])

print(IsCarDamaged(car_01), IsCarDamaged(car_02))

cars = [car_01, car_02]
for c in cars:
    print(f"Is {c['carBrand']} {c['carModel']} damaged? = {IsCarDamaged(c)}")



brandOnSale = "Renault"

import csv          #do odczytania i zapisu pliku csv
import types        # do definiowania funkcji dla klasy


def export(path, header, data):             #funkcja statyczna obok klasy
    with open(path, mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(data)

def exportfile(cls, path):                  #funkcja dynamiczna obok klasy
    with open(path, mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand', 'model', 'IsOnSale'])
        for c in cls.list_of_cars:
            writer.writerow([c.brand, c.model, c.IsOnSale])

def exportinstance(self, path):             #funkcja zewnętrzna dla każdej instancji
    with open(path, mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand', 'model', 'IsOnSale'])
        writer.writerow([self.brand, self.model, self.IsOnSale])

class Car(object):
    number_of_cars = 0
    list_of_cars = []
    def __init__(self, brand, model, airbag, painting, mechanic, accessories):
        self.brand = brand
        self.model = model
        self.airbag = airbag
        self.painting = painting
        self.mechanic = mechanic
        #self.__sale = sale
        Car.number_of_cars += 1
        Car.list_of_cars.append(self)
        self.accessories = accessories

    def damaged(self):
        return not (self.airbag and self.painting and self.mechanic)

    def getinfo(self):
        print(' --' * 10)
        print(" {} {} ".format(self.brand, self.model).upper())
        print("Air Bag- ok — {}".format (self.airbag) )
        print("Painting -ok- {}".format(self.painting))
        print('Mechanic - ok {}'.format(self.mechanic))
        #print('Is on sale - {}'.format(self.__sale))
        print(' --'*10)

    def __GetSale(self):
        return self.__sale

    def __SetSale(self, newSale):
        if self.brand == brandOnSale:
            self.__sale = newSale
            print(f'Changing status on sale to {newSale} for {self.brand}')
        else:
            print(f'Brand not on sale. Valid is {self.brand}')

    IsOnSale = property(__GetSale, __SetSale, None, 'if true car is on sale')           #właściwość klasy

    @classmethod
    def ReadTxtFromFile(cls, text):
        aNewCar = cls(*text.split(':'))
        return aNewCar

    @staticmethod
    def convertKM(KM):          #dla porządku funkcja należy do klasy
        return KM * 0.735       #może być w dowolnym miejscu zdefiniowana i wywołana

    @staticmethod
    def convertKW(KW):
        return KW * 1.36

    def __iadd__(self, other):
        if type(other) is list:
            accessories = self.accessories
            accessories.extend(other)
            return Car(self.brand, self.model, self.airbag, self.painting, self.mechanic, accessories)
        elif type(other) is str:
            accessories = self.accessories
            accessories.append(other)
            return Car(self.brand, self.model, self.airbag, self.painting, self.mechanic, accessories)
        else:
            raise Exception(f'Not logic type to car {type(other)}.')

    def __add__(self, other):
        if type(other) is Car:
            return (self, other)
        else:
            raise Exception('Addint type not implemented')

    def __str__(self):
        return f"brand {self.brand}, Model: {self.model}"

car7 = Car('Volvo', 'C50', False, True, True, [])


#
# lineOfText = 'Renault:Megane:True:True:True:False'
# car_05 = Car.ReadTxtFromFile(lineOfText)
# print(f'\n CAR NR 5 ')
# car_05.getinfo()

car_03 = Car('Renault', 'Megane', True, True, True, True)
car_04 = Car('Ford', 'Focus', True, False, True, False)
# print(car_03._Car__GetSale(), car_04._Car__GetSale())  #po ukryciu metody w klasie nie są dostępne do zmiany, tak nie robić
# car_03._Car__SetSale(True)        #ustawienie wartości sale przez funckcję
# car_04._Car__SetSale(False)

car_03.IsOnSale = True
car_04.IsOnSale = True      #ustawienie wartości sale przez właściwość klasy
#car_03.__sale = False
car_03.YearOfProduction=2010    #definicja nowego atrybutu

car6 = Car('Peugeot', '206', True, True, False, ['tires', 'lewarek', 'zapach'])
car6 += 'loud speaker bass system'
car6.getinfo()

setattr(car_03, 'taxi', True)   #definiowanie nowego atrybutu instancji
print(hasattr(car_03, 'taxi'))  #czy jest atrybut o tej nazwie
del car_03.YearOfProduction
delattr(car_03, 'taxi')         #dwa różne sposoby usuwania atrybutów, robią to samo


print(car_04.airbag, car_03.model, car_03.brand)
print(car_03.brand, car_03.model, car_03.damaged())
print(car_04.brand, car_04.model, car_04.damaged())

# car_04.getinfo()
# car_03.getinfo()
#
# print('Static------'*10)
# Car.Export_static = export
# #export(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\export.csv', ['Brand', 'Model', 'IsOnSale'], [car_03.brand, car_03.model, car_03.IsOnSale])
# Car.Export_static(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\export.csv', ['Brand', 'Model', 'IsOnSale'], [car_03.brand, car_03.model, car_03.IsOnSale])
#
# print('Class------'*10)
# #Car.ExportClass = exportfile
# Car.ExportClass = types.MethodType(exportfile, Car)
# Car.ExportClass(path=r"C:\Users\Andrzej\Desktop\kurs Python\pliki txt\exportfile.csv")
#
# print('Instance------'*10)
# car_03.ExportInstance = types.MethodType(exportinstance, car_03)
# car_03.ExportInstance(path=r"C:\Users\Andrzej\Desktop\kurs Python\pliki txt\exportinstance.csv")

car_pack = car6 + car7
print('car6 + car7= ', car_pack[0].brand, car_pack[1].brand)
print(car_pack)

print(car7)


class Truck(Car):
    def __init__(self,  brand, model, airbag, painting, mechanic, accessories, capacity):
        super().__init__(brand, model, airbag, painting, mechanic, accessories)     # odwołuje się do klasy Car, dziedziczenie
        self.capacity = capacity

    def GetInfo(self):
        super().getinfo()
        print(f'Capacity {self.capacity}')

truck1 = Truck('Ford', 'Transit', True, True, True, False, 1600)
truck2 = Truck('Renault', 'Traffic', True, False, True, False, 2000)
print(truck1.brand, truck1.model, truck1.capacity, truck2.brand, truck2.model, truck2.capacity)

truck1.GetInfo()
truck2.GetInfo()

