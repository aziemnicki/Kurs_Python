import pickle
import glob
import types

cake_01 = {
            'taste': 'vanilia',
            'glaze': 'chocolade',
            'text': 'Happy Brithday',
            'weight': 0.7}
cake_02 = {
            'taste': 'tee',
            'glaze': 'lemon',
            'text': 'Happy Python Coding',
            'weight': 1.3}


def show_cake_info(cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        cake['taste'], cake['glaze'], cake['text'], cake['weight']))


cakes = [cake_01, cake_02]
for c in cakes:
    show_cake_info(c)


def export_1_cake_to_html(obj, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        for c in obj.bakery_offer:
            content = template.format(c.name, c.kind, c.taste, c.additives, c.filling)
            f.write(content)


def export_cake_instance(self, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(self.name, self.kind, self.taste, self.additives, self.filling)
        f.write(content)


class Cake:

    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten, text):
        self.name = name
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.__gluten = gluten
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            print('Nie można ustawić tekstu na torcie')
        Cake.bakery_offer.append(self)

    def show_info(self):
        print(self.name.upper())
        print(f'Taste - {self.taste}')
        if len(self.additives) != 0:
            print(f'Dodatki {self.additives}')
        if len(self.filling) != 0:
            print(f'Nadzienie- {self.filling}')
        print(f"Czy ma gluten? {self.__gluten}")
        if len(self.__text) > 0:
            print(f'text na torcie {self.__text}')

    def set_filling(self, fil_name):
        self.filling = fil_name

    def add_add(self, dodatki):
        self.additives.append(dodatki)

    def __getTxt(self):
        return self.__text

    def __setTxt(self, newTXT):
        if self.kind == 'cake':
            self.__text = newTXT

    def saveFile(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def getFile(cls, path):
        with open(path, 'rb') as f:
            new_pickel = pickle.load(f)
            cls.bakery_offer.append(new_pickel)

            return new_pickel

    @staticmethod
    def get_bakery_files(path):
        return glob.glob(path + '\*.bakery')

    Text = property(__getTxt, __setTxt, None, 'wpisz nowy tekst na tort')


cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream', True, 'Happy Birthday')
cake2 = Cake('ciasto', 'placek', 'nie za słodki', ['lukier'], 'truskawka', True, '')

cake01.saveFile(r"C:\Users\Andrzej\Desktop\kurs Python\pliki txt\cake1.bakery")
cake2.saveFile(r"C:\Users\Andrzej\Desktop\kurs Python\pliki txt\cake2.bakery")
tort1 = Cake.getFile(r"C:\Users\Andrzej\Desktop\kurs Python\pliki txt\cake1.bakery")
tort2 = Cake.getFile(r"C:\Users\Andrzej\Desktop\kurs Python\pliki txt\cake2.bakery")


cake01.Text = 'Happy Birthday'
cake2.Text = 'sto lat'
for b in Cake.bakery_offer:
    print("{} - ({}) main taste: {} with additives of {}, filled with {}".format(
        b.name, b.kind, b.taste, b.additives, b.filling))
cake01.__gluten = False
cake2._Cake__gluten = False

cake01.show_info()
cake2.set_filling('śmietankowe')
cake2.add_add(['orzechy', 'kuleczki'])
cake2.show_info()

# print(isinstance(cake01,Cake))
# print(type(cake01) is Cake)
# print(vars(cake01), vars(Cake))
# print(dir(cake01), dir(Cake))
print(len(Cake.bakery_offer))
tort1.show_info()
print(Cake.get_bakery_files(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt'))

Cake.ExportCake = types.MethodType(export_1_cake_to_html, Cake)
Cake.ExportCake(path=r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\all_cakes.html')
for c in Cake.bakery_offer:
    c.ExportCakeInstance = types.MethodType(export_cake_instance, c)
    c.ExportCakeInstance(r"C:\Users\Andrzej\Desktop\kurs Python\pliki txt\{}.html".format(c.name))

