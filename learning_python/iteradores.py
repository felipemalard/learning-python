# Iteradores = percorre objetos 

lista = [1,2,3,4]
iterador = iter(lista) #percorre por todos os números da lista
print (next(iterador))
print (next(iterador))
print (next(iterador))
print (next(iterador))

#-------------------------------------------------------------

# outra forma
for item in lista:
    print (item)

#-------------------------------------------------------------

# Criando o próprio objeto iterável

class ColecaoNumeros:
    def __init__(self, numero_max):
        self.max = numero_max #recebe o número máximo pelo construtor 

    def __iter__ (self): #torna o objeto iterável (sendo possível a utilização do for ou iter)
        self.numero_atual = 0 #incia o contador para começar do início 
        return self
    
    def __next__ (self):
        if self.numero_atual <= self.max: # enquanto o número atual (0) for menor ou igual ao máximo
            retorno = self.numero_atual
            self.numero_atual += 1
            return retorno
        else:
            raise StopIteration
        
colecao = ColecaoNumeros(6)

x = iter(colecao)
print (next(x))
print (next(x))
print (next(x))
print (next(x))
print (next(x))
print (next(x))
print (next(x))

#-------------------------------------------------------------

for item in colecao:
    print (item)

#-------------------------------------------------------------

# Funções iteráveis - Generators 
# yield -> parecido com o return mas não encerra a função 

def numeros ():
    yield 1
    yield 2
    yield 3
    yield 4

for item in numeros():
    print (item)

#-------------------------------------------------------------

# Enumerate -> enumerar objetos em uma lista (indice com seu respectivo valor)

lista = ['a','b','c','d']

for item in enumerate(lista):
    print (item)

for indice, valor in enumerate(lista):
    print (indice)
    print (valor)

#-------------------------------------------------------------

# Unpacking -> desempacotar elementos de uma coleção

produtos = [['carro','200000'],['geladeira','9000']]

for produto, valor in produtos:
    print (produto,valor)

def gen1():
    yield [1,5]
    yield [5,9]

for x,y in gen1():
    print (x,y)

#-------------------------------------------------------------

def gen1():
    yield 1
    yield 2
    yield 3

def gen2 ():
    for i in gen1():
        yield i,'a'
        yield i,'b'
        yield i,'c'

for x,y in gen2():
    print (x,y)

#-------------------------------------------------------------

# join -> junta elementos

texto1 = 'olá'
print ('$'.join(texto1))

lista = ['a','b','c']
print ('   '.join(lista))

letras = '-'.join([str(i) for i in range(10)])
print (letras)

def anos ():
    for i in range (2020,2030):
        yield str(i)

print ('-'.join(anos()))

#-------------------------------------------------------------

#Tratando erros

lista = [1,2,3]
iterador = iter(lista)

while True:
    try:
        print (next(iterador))
    except StopIteration:
        break

