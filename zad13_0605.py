import time
#
# try:
#     with open(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\file.txt', 'w+') as file:
#         file.writelines('SUCCES')
# except OSError as e:
#     print(f'Error opening file {e.filename}, details: {e.strerror}')

def TODO1():
    class time_measure:

        def __init__(self):
            pass

        def __enter__(self):
            print('entering...')
            self.__start = time.time()      #ukryta zmienna - __start
            return self

        def  __exit__(self, exc_type, exc_val, exc_tb):
            print('exiting...')
            self.__stop = time.time()
            self.__diff = self.__stop - self.__start
            print(f'Execution time {self.__diff}')

    with time_measure() as my_timer:
        time.sleep(3)

    class HtmlCM:

        def __init__(self):
            pass

        def __enter__(self):
            print("""<TABLE>
     <TR>
         <TH>Number</TH><TH>Description</TH>
     </TR>""")
        def __exit__(self, exc_type, exc_val, exc_tb):
            print('</TABLE>')

    with HtmlCM() as HTML:
        print(""" <TR>
         <TD>1</TD><TD>Say hello!</TD)
     </TR>
     <TR>
         <TD>2</TD><TD>Say good bye!</TD)
     </TR>""")

def TODO2():
    import os

    class ini_file:

        def __init__(self, path):
            self.path = path
            self.param = {}
            self.read_from_disc()

        def read_from_disc(self):
            if os.path.isfile(self.path):
                with open(self.path) as file:
                    for line in file:
                        parts = line.replace('\n', '').split('=')
                        self.param[parts[0]] = parts[1]

        def read_param(self, key):
            if key in self.param:
                return self.param[key]
            else:
                return None

        def write_param(self, key, value):
            self.param[key] = value

        def save_on_disc(self):
            with open(self.path, 'w') as file:
                for key, value in self.param.items():
                    line = '{}={}\n'.format(key, value)
                    file.writelines(line)

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            print('exitinig...')
            print(f'exec_type={exc_type}')
            print(f'exec_val={exc_val}')
            print(f'exec_tb={exc_tb}')
            if exc_type ==OSError:
                return False
            else: True


    ini = ini_file(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\my.ini')
    ini.write_param('version', 1)
    ini.write_param('level', 'advanced')
    ini.save_on_disc()

    ini2 = ini_file(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\my.ini')
    print(ini2.param)
    print(ini2.read_param('version'))
    print(ini2.read_param('level'))

    with ini_file(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\my.ini') as ini3:
        print(ini3.param)
        print(ini3.read_param('version'))
        print(ini3.read_param('level'))

    with ini_file(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\my.ini') as myini:
        myini.write_param('mode', 'strict')
        myini.write_param('loglevel', 'light')
        myini.save_on_disc()
        #print(10/0)

def TODO3():
    import os
    import zipfile
    import requests

    class FileFromWeb:

        def __init__(self, url, tmp_file):
            self.url = url
            self.tmp_file = tmp_file

        def __enter__(self):
            response = requests.get(self.url)
            with open(self.tmp_file, 'wb') as file:
                file.write(response.content)
                return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type == FileNotFoundError or exc_type == KeyError:
                print('No file in archive / incorrect dir')
                return True
            else: return False

    with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip',r'C:\Users\Andrzej\Downloads\euroxref.zip') as my_zip:
        with zipfile.ZipFile(my_zip.tmp_file, 'r') as z:
            a_file = z.namelist()[0]
            print(a_file)
            os.chdir(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt')
            z.extract(a_file, '.', None)

def TODO4():

    class Door:

        def __init__(self, where):
            self.where = where

        def open(self):
            print(f'Opening doors to {self.where}')

        def close(self):
            print(f'closing door to {self.where}')
    from contextlib import contextmanager

    @contextmanager
    def Closee(obj):
        yield obj
        obj.close()

    with Closee(Door('next room')) as door:
        door.open()
        print(f'the door is to the {door.where}')

    from urllib.request import urlopen
    from contextlib import closing, suppress, redirect_stdout

    # with closing(urlopen('http://www.kursyonline24.eu')) as page:
    #     for line in page:
    #         print(line)

    import os

    with suppress(FileNotFoundError):
        os.remove(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\syf.txt')

    f = open(r'C:\Users\Andrzej\Desktop\kurs Python\pliki txt\data.txt', 'w')
    with redirect_stdout(f):            #nei wyświetla nic na ekranie i od razu zapisuje w pliku to co zwraca terminal
        print('Hello')
        d = Door('Exit')
        d.open()
        d.close()

def TODO5():
    import os
    import zipfile
    import requests
    import contextlib

    class FileFromWeb:

        def __init__(self, url, tmp_file):
            self.url = url
            self.tmp_file = tmp_file

        def download_file(self):
            response = requests.get(self.url)
            with open(self.tmp_file, 'wb') as f:
                f.write(response.content)
            return self

        def close(self):
            #if os.path.isfile(self.tmp_file):
            os.remove(self.tmp_file)

    with contextlib.suppress(FileNotFoundError):
        with contextlib.closing(FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', r'C:\Users\Andrzej\Downloads\euroxref.zip')) as f:
            f.download_file()

            with zipfile.ZipFile(f.tmp_file, 'r') as z:
                a_file = z.namelist()[0]
                print(a_file)
                os.chdir(r'C:\Users\Andrzej\Downloads')
                z.extract(a_file, '.', None)

            os.remove(f.tmp_file)


if __name__ == '__main__':
    #TODO1()
    #TODO2()
    #TODO3()
    #TODO4()
    TODO5()
