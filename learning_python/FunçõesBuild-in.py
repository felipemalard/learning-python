# Funções Matemáticas:

# valor absuloto
num1 = 10
num2 = -20
valor = abs(num1) + abs(num2)
print (valor)

# maior e menor valor
lista = [-10,-20,90,80,-6,70]
maior_valor = max(lista)
print (maior_valor)

lista = [-10,-20,90,80,-6,70]
menor_valor = min(lista)
print (menor_valor)

# potência
x = 10
y = 2
valor = pow(x,y)
print (valor)

# raiz quadrada
import math
print (math.sqrt(25))

# arredondadar
print (round(2.623478236,1))
from math import floor, ceil
print (floor(2.623478236))
print (ceil(2.623478236))

# cociente e resto da divisão
print (divmod(10,2))

# caractere para números
numero = 70
print (chr(numero))

numero = 'F'
print (ord(numero))

# Funções para texto:
texto = 'olá, eu sou o FELIPE, gosto MUITO DE JOG@R BOL@ e tenis'
print(texto.capitalize)
print(texto.lower)
print(texto.upper)
print(texto.swapcase)
print(texto.title)
print (texto.center(30,'-'))
print(texto.rjust(30))
print(texto.ljust(30))
print(texto.count('e'))
print(texto.find('o'))
print(texto.replace('@','a'))
print(texto.split(','))

#Funções para lista

lista = [10,6,5,2,8,3,6,32,65,23]
lista_ordenada = lista.sort()
print(lista)
lista_decrescente = lista.sort(reverse=True)
print(lista)
lista1 = [['Carro', 'R$1000'], ['Moto', 'R$5000']]
for produto, valor in lista1:
    print(produto, valor)
elementos = dict.fromkeys(lista,10)
print(elementos)

# Funções data e hora
import datetime

data_completa = datetime.datetime.now()

print ('Data: ',data_completa.date())
print ('Hora Complete: ',data_completa.time())
print ('Dia: ',data_completa.day)
print ('Mês: ',data_completa.month)
print ('Ano: ',data_completa.year)
print ('Hora: ',data_completa.hour)
print ('Minutos: ',data_completa.minute)
print ('Segundos: ',data_completa.second)

print(datetime.date(day=5,month=3,year=2000))
print(datetime.time(20,46,20))
print(datetime.datetime(2000,3,13,20,7,54))

atual = datetime.datetime.now()
strg = atual.strftime('%y/%m/%d %H/%M/%S')
print (strg)

from datetime import datetime
data_txt = input('Digite a data no formato (dia/mês/ano): ')
data_obj = datetime.strptime(data_txt, '%d/%m/%Y')
print (data_obj)