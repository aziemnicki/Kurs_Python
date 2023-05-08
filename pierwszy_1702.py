moja ='10'
moja2 = moja
print(moja, moja2)
print(type(moja), type(moja2))
print(moja is moja2)
print(id(moja), id(moja2))
moja2 = moja+'!!'

moja2 = moja2[:-2] # ta sama zmienna ale bez 2 ostatnich znaków

print(moja, moja2)
print(moja == moja2)
print(type(moja), type(moja2))
print(moja is moja2)
print(id(moja), id(moja2))

lista = [2,4,6]
lista.append(8)
lista2 = lista      #zmiana jednego el. zmienia poprzednią listę, ta sama komórka pamięci
lista3 = lista.copy()   #tworzy kopię listy jako nowy element
lista3.append(20)
print(lista, id(lista), lista2,  id(lista2), lista3, id(lista3))

