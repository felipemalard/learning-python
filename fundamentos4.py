#funções

# utilizando def
def print_soma (x,y):
    print (x + y)
print_soma (1,2)

def subtrai (num1, num2):
    valor = num1 - num2
    return valor #pode ser guradado em variável
operacao = subtrai(10,3) # 10 passa a ser igual a num1 e 3 passa a ser igual a num2
print (operacao)

# lambda (+ simples)
subtracao = lambda num1, num2:num1-num2
#                  parametros| return
print (subtracao(10,3))

# def + lambda
def multiplicacao (y):
    return lambda x : x * y

valor = multiplicacao(2) #transforma a função em lambda
resultado = valor (10)
print (resultado)

# Recursiva

def contar (n):
    if n > 5: #quando parar
        return
    print (n)
    contar (n+1) # chama a própria função dentro dela mesma

contar(1)

# Vai -> Volta
def fatorial (num):
    if (num == 1):
            return 1
    return num * (fatorial(num-1)) #só vai saber o resultado se descobrir fatorial (num - 1)
print (fatorial(5))

'''fatorial(5)
= 5 * fatorial(4)
         = 4 * fatorial(3)
                  = 3 * fatorial(2)
                           = 2 * fatorial(1)
                                    = 1   ← aqui para
'''

#aninhamento de funções

def pai ():
    def filho ():
        print ('Eu sou a função filho')
    filho()
pai()

#decoradores


def meu_decorator(func): #func = função original que ta sendo decorada
    def decorador():
        print("Antes da função")
        func() # <----- função entra aqui
        print("Depois da função")
    return decorador

@meu_decorator #função que modifica outra função [diga_ola = meu_decorator (diga_ola)]
def diga_ola():
    print("Olá!")
diga_ola()



def DeixaMaiusculo (func):
    def inner_func (texto):
        return func(texto).upper()
    return inner_func

def ColocaParentese (func):
    def inner_func (texto):
        return '(' + func(texto) + ')'
    return inner_func

@DeixaMaiusculo
@ColocaParentese
def formata_string (texto):
    return texto

print (formata_string('Olá eu sou o felipe!'))




