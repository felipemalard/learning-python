# Uma classe com suas propriedades e métodos
# self = instância da classe 

class Pessoa:
    def __init__(self): # inicialização
        pass

class Pessoa:
    def __init__(self, cadastro_nome):
        self.cadastro_nome = cadastro_nome #cadastro_nome é uma propriedade da classe
        print ('Cadastro realizado com sucesso, o seu nome é %s' %(cadastro_nome))

cadastrar = Pessoa('João')
cadastrar.cadastro_nome #sempre resgatar uma variável assim

# Contagem do número de pessoas + uso detalhado do self

class Num_Pessoas:
    num_pessoas = 0
    def __init__(self, nome):
        self.nome = nome #sempre ter o self (instância da classe)
        Num_Pessoas.num_pessoas += 1
    def print_nome (self):
        print ('O seu nome é: %s' %(self.nome)) #sempre utilizar o self !!!!!!!!!! (regata o atributo da classe)

Pessoa1 = Num_Pessoas('Rodrigo')
Pessoa2 = Num_Pessoas('João')
print (Num_Pessoas.num_pessoas)

Pessoa1.print_nome()

# Herança = classe pai com atributos e métodos e classes filhas herdam coisas da classe pai

class Area:
    def __init__(self, medida1, medida2):
        self.medida1 = medida1
        self.medida2 = medida2
        self.area = (medida1 * medida2)
    def print_area (self):
        print ('A área do quadrado é: %s' % (self.area))

class Quadrado (Area): #Está herdando os atributos da classe Area
    pass

area_quadrado = Quadrado(10,10)
area_quadrado.print_area()

#Override = mesmo após a definição de parâmetros a classe pode ser sobrescrita

class Pai:
    def __init__(self):
        print ('Sou a classe pai')

class Filha (Pai):
    def __init__(self): #cria o seu próprio parâmetro
        print ('Sou a classe filha')

pai = Pai()
filha = Filha() #sobreposição dos métodos da classe pai!


# A partir do novo def __init__ a classe cria o seu próprio parâmetro
# Agora para resgatar os atributos da classe Pai novamente:

class FormaGeometrica:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

class Quadrado (FormaGeometrica):
    def __init__(self, altura, largura, atributo_quadrado):
        FormaGeometrica.__init__(self,altura,largura) # Resgate dos atributos da classe Pai (FormaGeometrica)
        self.atributo_quadrado = atributo_quadrado

quadrado = Quadrado (100,200, 'quadrado')

print (quadrado.altura)
print (quadrado.largura)
print (quadrado.atributo_quadrado)

# Nova forma de calcular a área:

class FormaGeometrica:
    def __init__(self,altura,largura):
        self.altura = altura
        self.largura = largura
    def calcula_area (self): #lembra que sempre recebe o self da função
        pass

class Quadrado (FormaGeometrica):
    def calcula_area(self):
        return self.altura * self.largura
    
quadrado = Quadrado(10,20)

print (quadrado.calcula_area())

# Herança múltipla

class Base1:
    def __init__(self, atributo1):
        self.atributo1 = atributo1
    def print_atributo1 (self):
        print ('O atributo 1 é: %s' %(self.atributo1))

class Base2:
    def __init__(self, atributo2):
        self.atributo2 = atributo2
    def print_atributo2 (self):
        print ('O atributo 2 é: %s' %(self.atributo2))

class MinhaClasse (Base1, Base2):
    def __init__(self):
        Base1.__init__(self,10)
        Base2.__init__(self,20)

var = MinhaClasse()
print(var.atributo1)
print(var.atributo2)
var.print_atributo1()
var.print_atributo2()

# Modificadores de Acesso
# __ = não pode ser acessado fora da classe   
# _ = pertence apenas a própria classe a para quem a herdar

# ex: self.__segredo ou self._segredo

class Base:
    def __base__privada (self):
        print ('Pertenço somente a base')
    
    def _baseprotegida (self):
        print ('Pertenço a base e a quem me herdar')

class Filha (Base):
    def acessa_protegida (self):
        self._baseprotegida()

filha = Filha()
filha.acessa_protegida() 

# outro exemplo:

class Veiculo:
    def __init__(self):
        self.__marcha = 1
    
    def aumenta_marcha(self):
        self.__marcha += 1
        self.__marcha = min(self.__marcha, 5) # menor valor entre marcha e 5 !!

    def diminui_marcha(self):
        self.__marcha -= 1
        self.__marcha = max(self.__marcha, 1) # maior valor entre marcha e 1 !!

    def marcha_atual (self):
        return self.__marcha
    
carro = Veiculo()
print (carro.marcha_atual())
carro.aumenta_marcha()
carro.aumenta_marcha()
carro.aumenta_marcha()
carro.aumenta_marcha()
carro.aumenta_marcha() # não executa
print (carro.marcha_atual())
carro.diminui_marcha()
carro.diminui_marcha()
print (carro.marcha_atual())

# Property

class Pessoa:
    def __init__(self,nome):
        self.__nome = nome #PRIVADO
    
    def get_nome (self):
        return self.__nome
    
    nome = property(get_nome) #faz com que se possa ler (sempre com a função que retorna o self privado)
    
pessoa = Pessoa('Maria')
print (pessoa.get_nome())
# print (pessoa.nome) #nao vou poder pq está privado
# utilizar o property (ler atributos privados)

print (pessoa.nome)

# Alterar uma propriedade privada

class Pessoa:
    def __init__(self,nome):
        self.__nome = nome
    
    def get_nome (self):
        return self.__nome
    
    def altera_nome (self,nome):
        if len(nome) > 0:
            self.__nome = nome


    nome = property(get_nome, altera_nome) #vai alterar o nome privado
    
pessoa = Pessoa('Claudio')
print (pessoa.nome)
pessoa.nome = 'Marcos' 
print(pessoa.nome)

# fget, fset, fdel

class Pessoa:
    def __init__(self,nome):
        self.__nome = nome

    def get_nome (self):
        return self.__nome
    
    nome = property(fget = get_nome) #faz com que se possa ler (sempre com a função que retorna o self privado)
    
pessoa = Pessoa('Godofredo')
print (pessoa.nome)


class Pessoa:
    def __init__(self,nome):
        self.__nome = nome
    
    def altera_nome (self,nome):
        if len(nome) > 0:
            print ('Nome alterado')
            self.__nome = nome


    nome = property(fset = altera_nome) #vai alterar o nome privado (sem o fset nao teria como)
    
pessoa = Pessoa('Claudio')
pessoa.nome = 'Marcos' 

# Lendo e Alterando Privados com Decorators

class Natural:
    def __init__(self, numero):
        self.__numero = numero #PRIVADO
    
    @property #getter permite a leitura do número privado! (Como você vai ler)
    def numero (self):
        return self.__numero #aqui você pode fazer qualquer coisa
    
    @numero.setter #setter permite a modificação do valor do argumento privado
    def numero (self,value): #o value é para dizer que valor
        if value >= 0:
            self.__numero = value

numero_atual = Natural(10) #getter
print (numero_atual.numero)

numero_atual.numero = 20 #setter (Modifica)
print (numero_atual.numero)

# Cópia por Valor e Referência

# Valor (valores primitivos)
numero1 = 50
numero2 = numero1 #cópia
numero2 = 20
print (numero1)

# Referência (classes e listas) -> compartilham um local de memória
lista1 = [1,2,3]
lista2 = lista1 #cópia
lista2.append (10)
print (lista1)
print (lista2) #compartilham a mesma memória

class Classe:
    def __init__(self):
        self.num = 10

classe1 = Classe()
classe2 = classe1 #cópia 
classe2.num = 90
print (classe1.num)
print (classe2.num)

# função copy permite que a cópia seja por valor!


from copy import copy

lista1 = [1,2,3]
lista2 = copy(lista1) #cópia por valor agora
lista2.append (10)
print (lista1)
print (lista2) # não compartilham a mesma memória!


class Classe:
    def __init__(self):
        self.num = 10

classe1 = Classe()
classe2 = copy(classe1) #cópia por valor!

print (classe1 is classe2)

# Deletando objetos

numero = 10
del numero #deleta a variável

arr = [1,2,3]
print (arr)
del arr [0]
print (arr)

class Teste:
    def __init__(self):
        self.lista = [1,2,3]
    def __del__ (self):
        print ('Fui deletado!')

teste = Teste()
del teste

#Utilizando o property

class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
    
    def get_nome (self): # posso usar o @property + função
        print ('Pegando nome')
        return self.__nome
    
    def set_nome (self,nome): # @nome.setter
        print ('Setando nome')
        self.__nome = nome
    
    def del_nome (self): # @nome.deleter
        print ('Deletando nome')
        del self.__nome
    
    nome = property(get_nome, set_nome, del_nome)

instancia = Pessoa ('Larissa')
instancia.set_nome('João')
print (instancia.nome)
del instancia.nome

# Testando objetos

e_inteiro = isinstance(5, str)
print (e_inteiro)

class Base:
    def __init__ (self):
        pass
classe = Base()
e_base = isinstance(classe,Base)
print (e_base)


def soma (num1,num2):
    if isinstance(num1, (int,float)) and isinstance(num2, (int,float)):
        return num1 + num2
    else:
        return None
print (soma (1,34.5))
print (soma (True,'Texto'))

# With 

class Lista():
    def __init__(self):
        pass

    def __enter__ (self):
        print ('Memória Iniciada')
        self.lista = [i for i in range (0,11)]
        return self.lista
    
    def __exit__ (self,*args, **kwargs):
        print ('Memória Liberada')
        del self.lista

with Lista() as temp_lista:
    for i in temp_lista:
        print (i)

print ('Aqui o objeto já não existe mais!')

# Utilizando o ADD ou SUB ou Lt (menor que) ou Gt (maior que)




class MeuNumero:
    def __init__(self,numero):
        self.numero = numero

    def __add__ (self,outro):
        return self.numero + outro.numero
    
num1 = MeuNumero(10)
num2 = MeuNumero(20)

print (num1 + num2)


class MeuNumero:
    def __init__(self,numero):
        self.numero = numero

    def __sub__ (self,outro):
        return self.numero - outro.numero
    
num1 = MeuNumero(10)
num2 = MeuNumero(20)

print (num1 - num2)




class Veiculos:
    def __init__ (self,peso,potencia):
        self.peso = peso
        self.potencia = potencia

    def __lt__ (self,outro):
        return self.potencia < outro.potencia
    
    def __gt__ (self,outro):
        return self.potencia > outro.potencia

class Moto (Veiculos):
    def __init__(self, peso, potencia):
        Veiculos.__init__(self,peso,potencia)

class Onibus (Veiculos):
    def __init__(self, peso, potencia):
        Veiculos.__init__(self,peso,potencia)

moto = Moto(200,400)
onibus = Onibus(2000,900)

print (moto > onibus)
print (moto < onibus)