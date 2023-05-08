def Buyme(what):
    print("a new car", what)

def left(*args):
    print('PLACEHOLDER - turning left with', *args)

def right(*args):
    print('PLACEHOLDER - turning right with', *args)

def start(*args):
    print('PLACEHOLDER - starting with', *args)

def stop(*args):
    print('PLACEHOLDER - stopping with', *args)

instructions = [start, left, right, stop]
dish = 'pizza'
for inst in instructions:
    inst(dish)


def double(x):
    return 2 * x


def square(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2
number = 8
transformations = [double, square, div2, negative]
tmp_return_value = number
for transform in transformations:
    tmp_return_value = transform(tmp_return_value)
    print(tmp_return_value)

# __________________________________________________________
def Cook(activity,obj):
    activity(obj)

def generate_values(name, x_table):
    value_list = []
    for i in x_table:
        value_list.append(name(i))
    return value_list


x_table = list(range(11))

print(generate_values(double, x_table))
print(generate_values(square, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))

# _________________________________________________________

def Create(kind = '+'):
    source = '''
def f(*args):       #definicja nowej funckji z parametrami dynamicznmi
    result = 0
    for a in args:
        result {}= a    #przesłanie dowolnego znaku za pomocą format
    return result   
''' .format(kind)
    exec(source, globals())     #uruchonienie funkcji w środowisku globalnym
    return f                    #zwrócenie nowej funkcji

f_add = Create('+')
print(f_add(1,2,3,4,5,6,7,8,9))
f_sub = Create('-')
print(f_sub(50,40,30))

from datetime import datetime
start = datetime(2019, 1, 1, 0, 0, 0)
end  = datetime.now()

def funkcje(span):
    if span == 'm':
        sec = 60
    elif span == 'h':
        sec = 3600
    elif span == 'd':
        sec = 86400

    source = '''
def f(start, end):
    duration = end - start
    dur_in_s = duration.total_seconds()
    return divmod(dur_in_s, {})[0]
    '''.format(sec)
    exec (source, globals())
    return f


f_minutes = funkcje('m')
f_hours = funkcje('h')
f_days = funkcje('d')

print(f_minutes(start, end))
print(f_hours(start, end))
print(f_days(start, end))

# ________WRAPPER _________________________________________
import datetime
#import functools                    #moduł do dekorowania funkcji

#log_file_path = r"C:\Users\Andrzej\Desktop\kurs Python\pliki txt\function_logi.txt"
def CreateLogFile(log_file_path):       #przekazanie ścieżki do różnych plików jako parametr wrappera
    def CreateWrapper(func):            #funkcja śledząca inną funkcję
        def function(*args, **kwargs):  #przekazanie parametrów nowej funkcji
            file = open(log_file_path, 'a')
            file.write('-'*20 + '\n')
            file.write((f'Function "{func.__name__}" started at {datetime.datetime.now().isoformat()}'))
            file.write(('Used arguments: '))
            file.write(' '.join('{}'.format(x) for x in args))
            file.write('\n')
            file.write(' '.join('{}={}'.format(k,v) for k,v in kwargs.items()))
            file.write('\n')
            result = func(*args, **kwargs)
            file.write(f'Returned {result} \n')
            file.close()
            return result
        return function
    return CreateWrapper

@CreateLogFile(r"C:\Users\Andrzej\Desktop\kurs Python\pliki txt\function_logi.txt")      #dekorator, zmienia nowe funkcję w funkcję obudowane wrapperem powyżej
def Change(employ, new_salary, bonus=False):
    print(f'Changing salary for {employ} to {new_salary} as a bonus {bonus} ')
    return new_salary

@CreateLogFile(r"C:\Users\Andrzej\Desktop\kurs Python\pliki txt\position_logi.txt")      #dekorator, zmienia nowe funkcję w funkcję obudowane wrapperem powyżej
def ChangePos(employ, new_position):
    print(f'Changing position for {employ} to {new_position}  ')
    return new_position
#print(Change('Andrzej', 6000, True))


#Change = CreateWrapper(Change)

print(Change('Andrzej', 10000, bonus=True))
print(Change('Andrzej', 10000, True))
print(ChangePos('Andrzej', 'CEO'))

print("_"*30)

import time
import functools

def wrapper_time(a_func):
    def wrapped_func(*args, **kwargs):
        start_time = time.time()
        v = a_func(*args, **kwargs)
        stop_time = time.time()
        print(f'Funkcion "{a_func.__name__}" done in time {stop_time-start_time}.')
        return v
    return wrapped_func

#@wrapper_time
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v

wrapped_seq = wrapper_time(get_sequence)
print(wrapped_seq(24))                      #wywołuje jednorazowo wrapper
#print(get_sequence(20))                    #wywołuje rekurencyjnie wrappera na tej samej funkcji