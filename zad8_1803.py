import os
from datetime import datetime as dt
import functools


def wrapper_log_file(logged_action, log_file_path):
    def WrapperToFile(func):
        def the_real_wrapper(path):
            with (open(log_file_path, 'a')) as file:
                file.write(f'Action {logged_action} executed on {path} on {dt.now().strftime("%Y-%m-%d %H:%M:%S")} \n')
            return func(path)
        return the_real_wrapper
    return WrapperToFile

@wrapper_log_file('FILE_CREATE', r"C:\Users\Andrzej\Desktop\kurs Python\pliki txt\file_create.txt")
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")

@wrapper_log_file('FILE_DELETE', r"C:\Users\Andrzej\Desktop\kurs Python\pliki txt\file_delete.txt")
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


# create_file(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\dummy_file.txt')
# delete_file(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\dummy_file.txt')
# create_file(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\dummy_file.txt')
# delete_file(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\dummy_file.txt')

import smtplib
import functools


def SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody):

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(user, password)
        server.sendmail(user, mailTo, message)
        server.close()
        print('mail sent')
        return True
    except:
        print("Error, mail not sent")
        return False


mailFrom = 'Your automation system'
mailTo = ['a-ziemnicki@wp.pl']
mailSubject = 'Email done'
mailBody = '''Szanowny Panie 

    Zwracam się z prośbą o ...

    Z wyrazami szacunku,
    Andrzej Ziemnicki, AIR, sem 1, RISA/L2, nr indeksu 144838
    '''
message = '''From:  {}
    Subject: {}

    {}
    '''.format(mailFrom, mailSubject, mailBody)

user = 'endi99pyra@gmail.com'
password = 'endi99awf'

#SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody)
SendInfo = functools.partial(SendInfoEmail, user, password, mailSubject='Execution')    #wywołanie funkcji z wcześniej zdefiniowanymi parametrami

SendInfo(mailFrom =mailFrom,mailTo= mailTo,mailBody= mailBody)
import time
import functools

@functools.lru_cache()
def silnia(n):
    time.sleep(0.1)
    if n==1:
        return 1
    else:
        return n*silnia(n-1)
start = time.time()

for i in range(1,18):
    print(f'{i}! = {silnia(i)}')
stop = time.time()
print(f'Czas wynosi: {stop-start}')
print(silnia.cache_info())

@functools.lru_cache(maxsize=100)
def fib(n):
    if n < 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result
start_time = time.time()
for i in range(1,100):
    print(f'Ciąg Fibbonaciego {i}= {fib(i)} z czasem {time.time()-start_time}')
stop_time = time.time()
print(f"Czas całkowity wynosi {stop_time-start_time}")
#print(fib.cache_info())
