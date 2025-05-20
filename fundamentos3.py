# list
array = [] #lista vazia
array = list([])

array = [10,2,3]
print (array)
array.append(2) #adicionar a lista (sempre por último)
print (array)
array.insert(2,'Oi') #adicionar na posição do índice indicado
print (array)
array.remove(10) #remover elemento
print (array)
array.pop(1) #remover pelo índice
print (array)
print (len(array), "elementos")
array.clear()
print (array)

array = [1,10,90,1,10,8,7,1,10,1,1]
print (1 in array)
repeticoes = array.count(1) #quantas repetições tal elemento teve
print (repeticoes)
pos = array.index(8)
print (pos)

array = [3,4,5]
x, y, z = array
print(x)
print(y)
print(z)

cores = ["amarelo","azul","vermelho"]
for x in cores:
    print (x) #elementos agora na variavel x

cores = ["amarelo","azul","vermelho"]
for i in range(0,len(cores)):
    print (cores[i])

lista = [[1,2,3],[4,5,6]] #varias listas em uma
lista1 = lista[0]
lista2 = lista[1]
print (lista1)
print (lista2)
primeiro_elemento_da_lista1 = lista1[0]
print (primeiro_elemento_da_lista1)

#set
lista = set({})
lista = {1}
lista.add (5)
print (lista)

set1 = {1,2,3}
set2 = {4,5,6}
set_unido = set1.union(set2) #unir set1 com set2
print (set_unido)

#tuple
lista = tuple(())
lista = ()
lista = ("chocolate", "bom bom", "leite")
print (lista)

tupla = tuple((6,7,8,9,10,6,6))
print (tupla.count(6))

#dictionaries

lista = {"Maria":10, "Felipe":9, "Fernando": "Indefinido"}
print (lista)
print (lista["Maria"])
lista["Maria"] = 30
print (lista)
lista.update({"Felipe":19})
print (lista)
lista.popitem()
print (lista)

lista = {"Maria":10, "Felipe":9, "Fernando": "Indefinido"}
chaves = lista.keys()
valores = lista.values()
for item in chaves:
    print (item)
print ("----------------")
for item in valores:
    print (item)

dados = {'ana': {'sexo':'feminino'}}
print (dados)

#list comprehensions

lista = [x for x in range(0,10)]
print (lista)

lista = [x for x in range(0,11) if x % 2 ==0]
print (lista)

lista = [1,5,9]
lista1 = [x for x in range (0,11) if x not in lista]
print (lista1)