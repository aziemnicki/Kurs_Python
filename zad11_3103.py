from datetime import date
from datetime import timedelta


class Memory:

    def __init__(self, lista):
        self.list_items = lista

    def __call__(self, item):
        self.list_items.append(item)


mem = Memory([])
mem.list_items.append('cukier')
mem('mleko')

print('List of items', mem.list_items)


class NoDuplicates:

    def __init__(self, listb):
        self.listb = listb
        self.func = listb

    def __call__(self, cake, add):
        no_dup_list = []
        for a in add:
            if a not in cake.additives:
                no_dup_list.append(a)
        self.func(cake, no_dup_list)

    # def __call__(self, items):
    #     self.new_items = []
    #
    #     for i in items:
    #         if i not in self.listb:
    #             self.listb.append(i)

my_no_dup_list = NoDuplicates([])
print(f'Instancja {my_no_dup_list.listb}')

# my_no_dup_list(['keyboard', 'mouse'])
# my_no_dup_list(['keyboard', 'mouse', 'pendrive'])
# my_no_dup_list(['charger', 'pendrive'])
# print(my_no_dup_list.listb)

import random

class Selected:

    list_selected = []

    def __init__(self, func):
        self.func = func

    def __call__(self, list):
        items_not_sel = [i for i in list if i not in Selected.list_selected]
        item = self.func(items_not_sel)
        Selected.list_selected.append(item)
        return item

cars = [ 'Opel ','Toyota' , 'Fiať ','Forď', 'Renaulť ', 'Mercedes',  'BMW' , 'Peugeoť , Porsche' , 'Audi'  , 'Mazda']

@Selected
def SelectedProm(list_of_cars):
    return random.choice(list_of_cars)

@Selected
def SelectedShow(list_of_cars):
    return random.choice(list_of_cars)

@Selected
def SelectedGifts(list_of_cars):
    return random.choice(list_of_cars)

#
# print('_______'*10)
# print('Promotion', SelectedProm(cars))
# print('Show', SelectedShow(cars))
# print('Free Gifts', SelectedGifts(cars))

print('_______'*10)

class Cake:
    '''
    Cake class for our bakery solution
    '''
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        '''
                __init__ takes all the parameters and saves them
                '''
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    def add_additives(self, additives):
        self.additives.extend(additives)

    @property
    def full_name(self):
        '''
                Just return the most important attributes of the object
                '''
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)

cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')

@NoDuplicates
def add_extra_additives(cake, additives):
    cake.add_additives(additives)

add_extra_additives(cake01, ['strawberries', 'sugar-flowers'])
cake01.show_info()

add_extra_additives(cake01, ['strawberries', 'sugar-flowers', 'chocolate', 'nuts'])
cake01.show_info()

class SpecialCake(Cake):
    def __init__(self, name, kind, taste, additives, filling, occasion, shape, ornaments, text):
        super().__init__(name, kind, taste, additives, filling)
        self.occasion = occasion
        self.shape = shape
        self.ornaments = ornaments
        self.text = text

    def show_info(self):
        super().show_info()
        print(f'Okazja {self.occasion}, Kształt {self.shape}, '
              f'Ozdoby {self.ornaments}, Tekst {self.text}.')

birthday = SpecialCake('tort', 'bezowy', 'truskawkowy', ['chuj'], 'krem', 'urodziny', 'romb', 'swieczki', 'sto lat')
wedding = SpecialCake('tort', 'ślubny', 'śmietankowy', ['orzechy'], ['krem', 'rum'], 'ślub', 'piętrowy', 'młoda para', 'love')
birthday.show_info()
wedding.show_info()
for cake in SpecialCake.bakery_offer:
    print(cake.full_name)
    cake.show_info()


class Promo():

    def __init__(self, name, discount, start_date, end_date, minimal_order):
        self.name = name
        self.discount = discount
        self.start_date = start_date
        self.end_date = end_date
        self.minimal_order = minimal_order

    @property
    def full_name(self):
        return "PROMO {0:s} {1:.0%}".format(self.name, self.discount)


cake = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')
cake.show_info()

promo10 = Promo("DISCOUNT - no additional conditions", 0.15, date.today(), date.today() + timedelta(days=14), 0)
print(promo10.full_name)


class PromoCake(Cake, Promo):

    def __init__(self, cake, promo):
        Cake.__init__(self, cake.name, cake.kind, cake.taste, cake.additives, cake.filling)
        Promo.__init__(self, promo.name, promo.discount, promo.start_date, promo.end_date, promo.minimal_order)


promo_cake = PromoCake(cake, promo10)
promo_cake.show_info()
print(promo_cake.full_name)
print(PromoCake.__mro__)
help(Cake)
help(Cake.full_name)