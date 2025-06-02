# Bibliotecas empacotadas

import random

print ('O primeiro número aleatório é:', random.randrange(10,100)) #módulo + função

# importar apenas uma função específica

from random import randrange

print ('O segundo número aleatório é:', randrange(10,100))

# as = trocar o nome da função

from random import randrange as aleatorio

print ('O terceiro número aleatório é:', aleatorio(10,100))

# * é para importar todas as funções

from random import *

# dir = atributos, classes (tudo do módulo)

import random
print (dir(random))
print (random.__name__)
print (random.__file__) # utilizar para estudar os módulos
print (random.__doc__)

print (randrange.__doc__) # utilizar para saber o que cada função faz

# PIP

'''

-> pip list
-> pip install
-> pip uninstall

-> pip install módulo==versão

'''

# Criando os próprios módulos (módulo_teste.py)

import módulo_teste
print ( dir(módulo_teste) )
print (módulo_teste.pi)
módulo_teste.minha_função(10)
var = módulo_teste.Teste()

from módulo_teste import pi
print (pi)

print (módulo_teste.__doc__)

print (módulo_teste.Teste.__doc__)