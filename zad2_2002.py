import os
import urllib.request 
#path = r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\przyklad.txt'
path = r'C:\Users\Andrzej\Desktop\Praca Inżynierska\uwagi do pracy, wnioski i wstęp.txt'

def plik(sciezka):
    with open(path, 'r') as file:      #utworzenie i otwarcie pliku
        text = file.read()      #odczytanie słów w pliku
              #rozdzielenie słów
        ilosc = len(text.split())       #zliczanie ilości słów w pliku
        return ilosc

if os.path.isfile(path):
    slowa = plik(path)
    print(f'W pliku znajduje się ', slowa, ' słów.')
    

os.path.isfile(path) and print(f'W pliku znajduje się ', plik(path), ' słów.')

price = 123
bonus = 23
bonusGranted = True
price = price if bonusGranted== False else  price-bonus
print(price)

rating = 5
print("VG") if rating ==5 else print('G')  if rating == 4   else print('W')

today = 'pon'
print('pomagam mamie') if today == 'pon' else print('masz w domu pranie') if today == 'sr' or today== 'czw' else print('mam 2 zebrania') if today =='pt' else print('na lekcję ganiam') if today =='sob' else print('możemy')




data_dir = r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt'
strony = [
    {'nazwa': 'Forbot', 'url': 'https://forbot.pl/blog/'},
    {'nazwa': 'Udemy', 'url': 'https://www.udemy.com/?deal_code=&utm_term=Homepage&utm_content=Textlink&utm_campaign=Rakuten-default&ranMID=39197&ranEAID=UGrHaPSUfM0&ranSiteID=UGrHaPSUfM0-EBsxEdHss_LknEvbHR3E8A&LSNPUBID=UGrHaPSUfM0&utm_source=aff-campaign&utm_medium=udemyads'},
    {'nazwa': 'YT', 'url': 'https://www.youtube.com'},
    {'nazwa': 'PP', 'url': 'https://www.put.poznan.pl'}] 
'''
strony = [
    { 'nazwa': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
    { 'nazwa': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },
    { 'nazwa': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]
'''
for strona in strony:
    try:
        pliki = "{}.html".format(strona['nazwa'])
        path = os.path.join(data_dir, pliki)
        
        print("Processing: {}  => {} ...".format(strona["url"], pliki))
        urllib.request.urlretrieve (strona["url"], path)    
        print("DONE")
    except:
        print(f"Failure while downloading web {strona['nazwa']}")
        break
else: 
    print('Pobrano strony')