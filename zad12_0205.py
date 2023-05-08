import itertools


def TODO1():
    clients = {
        "INFO": 0.5,
        "DATA": 0.2,
        "SOFT": 0.2,
        "INTER": 0.1,
        "OMEGA": 0.0
    }

    myClient = input("Enter clienťs name: ")
    # myClient  = ("Enter clienťs name: ")
    totalCost = 7200
    try:
        ratio = float(input('Enter new ratio: '))
        print("The default % ratio for {} is {} and new ratio is {}".format(myClient, clients[myClient], ratio))
        print('The cost for {} is {}'.format(myClient, totalCost * ratio))
        print('New ratio in comparison {}'.format(clients[myClient] / ratio))
    except KeyError as e:
        print('Wrong client, {} not in list'.format(myClient, [c for c in clients.keys()], e))
    except ZeroDivisionError as e:
        print("Can't divide by new ratio- zero, Detail: ".format(e))
    except ValueError as e:
        print(f'Problem with value, must be a number. Detail: {e} ')
    except Exception as e:
        print("Sorry we have an error...\nDetails:\n{}".format(e))
    # else:
    # finally:
    #     print("Calculation finished")

    print('###' * 20)


def TODO2():
    import requests
    import os
    import shutil


    def save_url_to_file(url, file_path):
        r = requests.get(url, stream=True)
        with open(file_path, "wb") as f:
            f.write(r.content)


    url = 'http://www.mobilo24.eu/spis/'
    dir = r'C:\Users\Andrzej\Desktop\kurs Python'
    tmpfile = 'download.tmp'
    file = 'spis.html'

    tmpfile_path = os.path.join(dir, tmpfile)
    file_path = os.path.join(dir, file)
    try:
        if os.path.exists(tmpfile_path):
            print('Usuwanie {}'.format(tmpfile))
            os.remove(tmpfile_path)
        save_url_to_file(url, tmpfile_path)
        shutil.copy(tmpfile_path, file_path)

    except requests.exceptions.ConnectionError as rqe:
        print(f'Wrong URL address {rqe}')
    except PermissionError as pe:
        print(f'File {pe} read only')
    except FileNotFoundError as fnf:
        print(f"File {fnf} not found in this dir")
    except Exception as e:
        print("Sorry we had an error\nDetail:\n".format(e))
    else:
        print(f"Succesfully downloaded {file}")
    finally:
        if os.path.exists(tmpfile_path):
            os.remove(tmpfile_path)
            print('Usuwanie {}'.format(tmpfile))
        print('DONE')

def TODO3():
    def process(netto, brutto):
        if netto>=brutto:
            raise Exception('Netto should be lower than brutto')
        else:
            print('Process invoice: netto={} brutto={}'.format(netto,brutto))
    def EndOfMonth():
        netto = 1250
        brutto = 1000
        try:
            process(netto, brutto)
        except ValueError as e:
            print('The value on invoice are incorrect {}'.format(e))
            raise ValueError ('Error processing invoice') from e
        except Exception as e:
            print('Error processing invoice {}'.format(e))
    EndOfMonth()

def TODO4():
    import datetime as dt

    class Trip:
        def __init__(self, symbol, title, start, end):
            self.symbol = symbol
            self.title = title
            self.start = start
            self.end = end

        def check_data(self):
            if len(self.title) == 0:
                raise Exception("Title is empty!")
            if self.start > self.end:
                raise ValueError("Start date is later than end date!")

        @classmethod
        def publish_offer(cls, trips):
            list_of_err = []
            for trip in trips:
                try:
                    trip.check_data()
                except ValueError as e:
                        list_of_err.append(f'{trip.symbol}: {e}')
                except Exception as e:
                        list_of_err.append(f'{trip.symbol}: {e}')
            if len(list_of_err) > 0:
                raise Exception(f"The list of trips has errors: {list_of_err}")
            else:
                print("the offer will be published...")

    trips = [
        Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
        Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 5, 12), dt.date(2023, 5, 22)),
        Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
    ]

    try:
        print('Start checking trips...')
        Trip.publish_offer(trips)
        print('DONE')
    except Exception as e:
        print(f'ERRORS: {e}')
        print('CANNOT PUBLISH OFFER')

def TODO5():
    import datetime as dt
    netto = 1250
    brutto = 10000
    assert netto<=brutto,    'Netto<brutto'

    orderDate = dt.date(2022,11,13)
    deliverydate = dt.date(2022,10,18)
    assert orderDate <= deliverydate,   'Order < delivery'

def TODO6():
    import datetime as dt

    class Trip:
        def __init__(self, symbol, title, start, end):
            self.symbol = symbol
            self.title = title
            self.start = start
            self.end = end

        def check_data(self):
            # assert len(self.title) == 0, "Title is empty!"
            # assert self.start > self.end, "Start date is later than end date!"
            if len(self.title) == 0:
                raise TripNameException('Title is empty')
            if self.start > self.end:
                raise TripDateException('Start date to far')


        @classmethod
        def publish_offer(cls, trips):
            list_of_err = []
            for trip in trips:
                try:
                    trip.check_data()
                # except ValueError as e:
                #     list_of_err.append(f'{trip.symbol}: {e}')
                except TripNameException as e:
                    list_of_err.append(f'{trip.symbol}: {str(e)}')
                except TripDateException as e:
                    list_of_err.append(f'{trip.symbol}: {str(e)}')
            #assert len(list_of_err) > 0, f"The list of trips has errors: {list_of_err}"
            if len(list_of_err) > 0:
                raise  TripException('This is list of errors', list_of_err)
            else:
                print("the offer will be published...")

    class TripException(Exception):
        def __init__(self,text, descrition):
            super().__init__(text)
            self.description = descrition

        def __str__(self):
            return '{}, descriptions: {}'.format(super().__str__(), self.description)

    class TripNameException(TripException):
        def __init__(self, text):
            super().__init__(text, 'Name of trip is missing')

    class TripDateException(TripException):
        def __init__(self,text):
            super().__init__(text, 'Date of trip is missing')



    trips = [
        Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
        Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 5, 12), dt.date(2023, 5, 22)),
        Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
    ]

    try:
        print('Start checking trips...')
        Trip.publish_offer(trips)
        print('DONE')
    except Exception as e:
        print(f'ERRORS: {e}')
        print('CANNOT PUBLISH OFFER')

def TODO7():
    class BITex(Exception):
        def __init__(self, text, area):
            super().__init__(text)
            self.area = area

        def __str__(self):
            return '{}, area {}'.format(super().__str__(),self.area)

    class BITsecEX(BITex):
        pass

    class BITdataForEX(BITex):
        pass


    try:

        raise BITex('file format is wrong', 'Financial data')
    except BITex as e:
        print(f'App error: {e}, area: {e.area}')

    try:

        raise BITex('file format is wrong', 'Personal data')

    except BITsecEX as e:
        print(f'App security error {e}')
    except BITdataForEX as e:
        print(f"App data format error {e}")
    except BITex as e:
        print(f'Application error {e}')
    except Exception as e:
        print(f'General error {e}')

def TODO8():
    import datetime as dt
    import sys
    start = dt.datetime.now()
    print(f'Exec started at: {start}')
    dates = [dt.date(2000,1,1) + dt.timedelta(days = i) for i in range(2500000)]
    print(f'Size od dates is {sys.getsizeof(dates)}')
    for d in dates:
        pass
    class MillionDays:
        def __init__(self, year, month, day, maxdays):
            self.date = dt.date(year, month, day)
            self.maxdays = maxdays

        # def __next__(self):
        #     if self.maxdays <= 0:
        #         raise StopIteration()
        #     ret = self.date
        #     self.date += dt.timedelta(days=1)
        #     self.maxdays -= 1
        #     return ret

        def __getitem__(self, item):
            if item <= self.maxdays:
                return self.date + dt.timedelta(days= item)
            else:
                raise StopIteration

        # def __iter__(self):
        #     return self

    md = MillionDays(2000, 1, 1, 25000)
    print(f'Size od dates is {sys.getsizeof(md)}')
    #print(md[0], md[1])
    it = iter(md)
    print(next(it))
    print(next(it))

    # for i in range(2500000):
    #     next(md)

    for d in md:
        print(d)


    stop = dt.datetime.now()
    print(f'Total time {stop-start}')


def TODO9():
    import time

    class Combinations:
        def __init__(self, products, promotions, customers):
            self.products = products
            self.promotions = promotions
            self.customers = customers
        #     self.curr_product = 0
        #     self.curr_promotion = 0
        #     self.curr_customer = 0
        #
        # def __next__(self):
        #     if self.curr_customer >= len(self.customers):
        #         self.curr_customer = 0
        #         self.curr_promotion += 1
        #     if self.curr_promotion >= len(self.promotions):
        #         self.curr_promotion = 0
        #         self.curr_product +=1
        #     if self.curr_product >= len(self.products):
        #         self.curr_product = 0
        #         raise StopIteration
        #
        #     item_to_return = [self.products[self.curr_product], self.promotions[self.curr_promotion],
        #                       self.customers[self.curr_customer]]
        #     self.curr_customer += 1
        #     return item_to_return

        def __getitem__(self, item):
            if item >= len(self.products) * len(self.promotions) * len(self.customers):
                raise StopIteration
            else:
                pos_products = item // (len(self.promotions)* len(self.customers))
                item = item % (len(self.promotions) * len(self.customers))
                pos_promotions = item // len(self.customers)
                item = item % len(self.customers)
                pos_customers = item
            return print(f'{self.products[pos_products]},- {self.promotions[pos_promotions]},{self.customers[pos_customers]}')

        # def __iter__(self):
        #     return self

    products = ["Product {}".format(i) for i in range(1, 50)]
    print(products)

    promotions = ["Promotion {}".format(i) for i in range(1, 30)]
    print(promotions)

    customers = ['Customer {}'.format(i) for i in range(1, 60)]
    print(customers)

    combinations = Combinations(products, promotions, customers)
    # for i in range(len(promotions) * len(products) * len(customers)):
    #     print(combinations[i])

    # for c in combinations:
    #     # here an analysis will be done - currently, just nothing happens :)
    #     pass
    combinations_iter = iter(combinations)
    print(next(combinations_iter))
    print(next(combinations_iter))

    for c in combinations_iter:
        print(c)


def TODO10():
        atuple = (1,2,3,4)
        for x in atuple:
            print(x)

        it = iter(atuple)
        print(next(it))
        print(next(it))
        print(next(it))

        alist = [1,2,3,4,5]

        for i in alist:
            print(i)

        it = iter(alist)
        print(next(it))
        print(next(it))
        print(next(it))

        aset = {1,2,(3,4), 'element', 5,6}
        for i in aset:
            print(i)
        it = iter(aset)
        with open(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\argumenty.txt', 'r' ) as file:
            while True:
                try: print(next(file))
                except StopIteration:
                    break

def TODO11():
    import csv

    with open(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\data.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        # for row in csvreader:
        #     print('|'.join(row))
        # print(next(csvreader))
        # print(next(csvreader))
        # print(next(csvreader))
        while True:
            try:
                print(next(csvreader))
            except StopIteration:
                break


def TODO12():

    import datetime as dt

    def Million(year, month, day, maxdays):
        date = dt.date(year, month, day)

        for i in range(maxdays):
            yield(date + dt.timedelta(days=i))

    for d in Million(2000, 1, 1, 10):
        print(d)
    print('***'*20)
    def Getnum():
        yield (22)
        yield (4)
        yield (10)
    r = Getnum()
    print(next(r))
    print(next(r))
    #print(next(r))
def TODO13():
    def Combination(products, promotions, customers):
        for prod in products:
            for prom in promotions:
                for cust in customers:
                    yield ("{} - {} - {}".format(prod, prom, cust) )


    products = ["Product {}".format(i) for i in range(1, 4)]
    promotions = ["Promotion {}".format(i) for i in range(1, 2)]
    customers = ['Customer {}'.format(i) for i in range(1, 5)]

    for c in Combination(products, promotions, customers):
        print(c)

def TODO14():
    file = open(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\data.txt', 'r')
    records = []
    # for line in file:
    #     if line.startswith('ACTION'):
    #         print(line.replace('\n',' '))

    # for line in file:
    #     if ':' in line:
    #         type, action = line.rstrip('\n').split(':', 1)
    #         record = (type, action)
    #         records.append(record)
    #
    # file.close()
    # print(records)
    def get_records(path):          #GENERATOR, nei wczytuje całego pliku, odczytuje po linijce za każdym razem, 1 open i 1 close
        print('__opening--')
        file = open(path)

        for line in file:
            if ':' in line:
                type, action = line.rstrip('\n').split(':', 1)
                record = (type, action)
                yield record            #strumień danych wczytyany z dysku jeden po drugim, funkcja zamraża następne pobranie danych

        print('__closing__')
    for record in get_records(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\data.txt'):
        print(f'The type is {record[0]} and action is {record[1]}')

def TODO15():
    import random           #GENERATOR losowych 3 liczb z zakresu 1-100 bez zapisu wszystkich możliwości, SI
    def gen_rand_sum(num_values, assert_sum):
        trial = 0
        numbers = list(range(num_values))
        while True:
            trial +=1
            for i in range(num_values):
                numbers[i] = (random.randrange(1, 101))
            if numbers[0]+numbers[1]+numbers[2] == assert_sum:
                yield (trial, numbers)
                trial = 0

    for i in range(10):
        (number_of_trial, numbers) = next(gen_rand_sum(3, 100))
        print(number_of_trial,numbers)

def TODO16():
    import os

    path = r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt'
    search = 'data'
    file_ext = '.txt'

    for dir_name, subdir, filesnames in os.walk(path):  # przechodzi przez wszystkie pliki w katalogu
        # print(dir_name, subdir, filesname)
        for filename in filesnames:  # sprawdza każdy plik
            if filename.endswith(file_ext):
                full_name = os.path.join(dir_name, filename)  # Łaczy ścieżką z nazwą pliku
                for line in open(full_name):  # W pliku sprawdza każdą linijkę
                    if search in line:
                        print(filename)

    def gen_files(base_dir, file_ext):
        for dir_name, subdir, filesnames in os.walk(base_dir):  # przechodzi przez wszystkie pliki w katalogu
            # print(dir_name, subdir, filesname)
            for filename in filesnames:  # sprawdza każdy plik
                if filename.endswith(file_ext):
                    full_name = os.path.join(dir_name, filename)  # Łaczy ścieżką z nazwą pliku
                    yield full_name     #generator zwraca nazwy plików
                    # for line in open(full_name):  # W pliku sprawdza każdą linijkę
                    #     if search in line:
                    #         print(filename)

    def grep_files(search_str, files):
        for file in files:
            with open(file) as text:
                if search_str in text.read():
                    yield file

    files_gen = gen_files(path, file_ext)
    for file in grep_files(search, files_gen):
        print(file)

def TODO17():
    import os
    import requests

    def gen_getfiles(dir):
        for d in os.listdir(dir):
            yield os.path.join(dir, d)

    def gen_getlines(filename):
        with open(filename, 'r') as f:
            for line in f.readlines():
                if line.endswith('\n'):
                    yield line.rstrip('\n')

    def gen_webpage(url):
        try:
            response = requests.get(url)
            return response.status_code == 200
            return True
        except:
            return False

    try:
        os.mkdir(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\links_to_check')
    except:
        pass

    with open(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\links_to_check\pl.txt', 'w') as f:
        f.write('http://www.wykop.pl/\n')
        f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
        f.write('http://www.demotywatory.pl')

    with open(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\links_to_check\com.txt', 'w') as f:
        f.write('http://www.realpython.com/\n')
        f.write('http://www.nonexistenturl.com/\n')
        f.write('http://www.stackoverflow.com')

    for file in gen_getfiles(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\links_to_check'):
        for line in gen_getlines(file):
            status = gen_webpage(line)
            print(f'Plik- {file}, adres www- {line}, status-{status}')


def TODO18():
    import itertools as it

    # mylist = ['a', 'b', 'c', 'd']
    # for combination in it.combinations_with_replacement(mylist, 3):
    #     print(combination)

    money = [20, 20, 20, 20, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1, 1, 1]
    results = []

    for i in range(1, 101):
        for combination in it.combinations(money, i):
            if sum(combination) == 100:
               results.append(combination)
    results = set(results)

    for result in results:
        print(result)

    money = [50, 20, 10, 5]

    for i in range(1, 101):
        for combination in it.combinations_with_replacement(money, i):
            if sum(combination) == 100:
                print(combination)

def TODO19():
    import itertools as it
    import math
    notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

    for i in range(50):
        for combination in it.permutations(notes, 4):
            print(combination)

    V= math.factorial(len(notes))/(math.factorial(len(notes)-4))
    print(V)

    for i in range(50):
        for combination in it.combinations_with_replacement(notes, 4):
            print(combination)

    V = len(notes)**4
    print(V)

def TODO20():
    import itertools as it
    filepath =  r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\data.txt'
    data = []

    with open(filepath) as file:
        for line in file:
            elements = line.rstrip('\n').split(':')
            d = {'type': elements[0],  'action': elements[1]}
            data.append(d)
    print(data)

    data = sorted(data, key=lambda x:x['type'])

    for key, elements in it.groupby(data, key=lambda x:x['type']):
        print(f'This key is {key} and the group num is {len(list(elements))}')

def TODO21():
    import os
    import itertools as it

    def scantree(path):
        for obj in os.scandir(path):
            if obj.is_dir():
                yield obj
                yield from scantree(obj.path)
            else:
                yield obj

    listing = scantree(r'C:\Users\Andrzej\Desktop\kurs Python')


    for l in listing:
        print('DIR ' if l.is_dir() else 'FILE', l.path)

    listing = scantree(r'C:\Users\Andrzej\Desktop\SPIKE Essensials')
    listing = sorted(listing, key=lambda x: x.is_dir())
    for is_dir, elements in it.groupby(listing, key=lambda x: x.is_dir()):
        print('DIR' if is_dir else 'file', len(list(elements)))

def TODO22():
    import itertools as it
    import operator

    data = [1, 2, 3, 4, 15, 6, 2]
    result = it.accumulate(data, operator.mul)          #łączy kolejne numery w liscie operatorem...
    for each in result:
        print(each)
    print()

    for i in it.count(10,3):                    #iteruje po 1 arg i zwiększa o tyle ile drugi arg
        print(i)
        if i > 25:
            break
    months = ['Jan', 'Feb','March', 'April', 'May','June' , 'july','August']
    # for m in it.cycle(months):                  #zapętla i powtarza w kółko dane
    #     print(m)

    color_basic = ['red', 'blue', 'yell']
    color_mix = ['green', 'orange']

    result = it.chain(color_mix, color_basic)       #łączy listy
    for each in result:
        print(each)
    cars = ['Ford', 'Open', "audi", 'mercedes']
    selection = [True, False, False, True]

    result = it.compress(cars, selection)           #łączy, wyświetla tylko obiekty gdzie jest True
    for each in result:
        print(each)

    result = it.dropwhile(lambda x: x<4, data)      #Odrzuca wartosci z listy poza warunkiem
    for each in result:
        print(each)

    result = it.filterfalse(lambda x:x<5, data)     #tak jak wyżej ale sprawdza do końca listę
    for each in result:
        print(each)

    result = it.islice(months, 6,8)                 #wyświetla tylko wybrane elementy
    for each in result:
        print(each)

    spades = ['Heart', 'Tiles', 'Clover', 'Pike']
    fig = ['Ace', 'King', 'Queen', 'Jack', '10', '9']
    result = it.product(spades, fig)    #iloczyn kartezjański zbiorow
    for each in result:
        print(each)

    for i in it.repeat('tell me why', 5):           #powtarza nawias, można określić ile razy
        print(i)

    data = [(1,2), (5,10), (15,20)]
    result = it.starmap(operator.mul, data)         #łączy elementy z tuple
    for each in result:
        print(each)

    data = [1, 2, 3, 4, 15, 6, 2]
    result = it.takewhile(lambda x:x<5, data)       #zostawia elementy z warunku
    for each in result:
        print(each)

    cars1 , cars2 = it.tee(cars)                    #tworzy dwa wspólne iteratory
    for each in cars1:
        print(each)
    print('----'*10)
    for each in cars2:
        print(each)

    plan = ['busy','busy', 'busy', 'busy', 'free','free']
    result = it.zip_longest(months, plan, fillvalue='chill')    #łączy listy o różnej długości, dodaje brakujące elementy
    for each in result:
        print(each)

def TODO23():
    import itertools as it
    def get_factors(x):

        ret_list = []
        for i in range(1, x):
            if x % i == 0:
                ret_list.append(i)
        return ret_list

    candidate_list = list(range(1,10001))
    filtered_list = list(it.filterfalse(lambda x: x!=sum(get_factors(x)), candidate_list))
    for l in filtered_list:
        print(f'Liczba idealna to {l}', get_factors(l))

    def check_if_has_dividers(x):

        for i in range(2, x):
            if x % i == 0:
                return True
        else:
            return False

    # # not optimal:
    # prime_numbers = list(it.filterfalse(lambda x: check_if_has_dividers(x), range(1, 10000)))
    # print(prime_numbers)
    #
    # print(prime_numbers[:10])

    prime_numbers = it.islice(it.filterfalse(lambda x: check_if_has_dividers(x), range(10000000)), 100)
    print(list(prime_numbers))



if __name__ == '__main__':
    #TODO1()
    #TODO2()
    #TODO3()
    #TODO4()
    #TODO5()
    #TODO6()
    #TODO7()
    #TODO8()
    #TODO9()
    #TODO10()
    #TODO11()
    #TODO12()
    #TODO13()
    #TODO14()
    #TODO15()
    #TODO16()
    #TODO17()
    #TODO18()
    #TODO19()
    #TODO20()
    #TODO21()
    #TODO22()
    TODO23()