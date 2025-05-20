# Fundamentos da estrutura IF

if (True):
    print ("Isso vai ser executado")
if (False):
    print ("Isso não vai ser executado")

if (True):
    pass

valor1 = 10
valor2 = 10
sao_iguais = (valor1 == valor2)
if (sao_iguais): #se não for igual não vai executar nada
    print ("São iguais")

valor1 = 10
valor2 = 10
if (valor1 == valor2): #não precisa ter uma variável
    print ("São iguais")

#uso do else
numero = 10
if (numero >= 11):
    print ("O numero é maior ou igual a 11")
else: #else só é executado se o if não for
    print ("O numero é menor que 11")

primeira_vez = input("É a primeira vez que você está usando? (sim/nao): ").strip().lower()
if (primeira_vez == (("sim").strip().lower())):
    print ("OI")
else:
    print ("Olá") #se eu colocar outra coisa como falar que ta errado? -> else

#Aninhando Ifs

numero = 11
if (numero > 0):
    print ("O numero é maior que zero")
    if (numero > 10):
        print ("O numero é maior que dez")

#Uso do elif (sempre entre o If e o Else)
primeira_vez = input("É a primeira vez que você está usando? (sim/nao): ").strip().lower()
if (primeira_vez == (("sim").strip().lower())):
    print ("OI")
elif (primeira_vez == (("sim").strip().lower())):
    print ("Olá") 
else:
    print ("Incorreto")

#podem ter varios elif!

#formas praticas
numero = 9
numero = "PAR" if numero % 2 == 0 else "IMPAR" #forma de linha única
print (numero)

numero= 1
numero = "Um" if numero == 1 else "Dois" if numero == 2 else "Três"
#só funciona com if e else, if e else
conta = input ("Digite o seu saldo: ")
devo = input ("Digite o quanto você está devendo: ")
conta = int(conta) - int(devo)
saldo_final= "Você não está devendo. " if conta >= 0 else "Você está devendo. "
print (saldo_final, "O seu saldo é:", conta)

#exercícios

cpf_usuario = input ("Digite o seu CPF: ")
senha_usuario = input ("Digite uma senha: ")
print ("Informações salvas, faça o login")
senha = input ("Digite a senha para logar: ")
if senha == senha_usuario:
    print ("O seu cpf é:", cpf_usuario)
else:
    print ("Senha não cadastrada.")

idade = 10
idade = "Bebê" if idade <= 3 else "Criança" if idade <= 13 else "Adulto" if idade <= 65 else "Idoso"

numero1 = input("Digite o primeiro numero: ")
numero2 = input("Digite o segundo numero: ")
operações = input("Digite a operação: ")
if (operações) == "soma":
    print (int(numero1) + int(numero2))
    if (operações) == "subtração":
        print (int(numero1) - int(numero2))
        if (operações) == "multiplicação":
            print (int(numero1) * int(numero2))
elif (operações) == "divisão":
    print (int(numero1) / int(numero2))
else:
    print("Isso não é uma operação matemática.")

#while (loops)

numero = 10
while (numero > 0):
    print (numero)
    numero -= 1
#vai funcionar até a condição ser satisfeita
print ("FIM")

#SOMAR
soma = 0
numeros_lidos = 0
while (numeros_lidos < 5):
    num_str = input("Digite um valor: ")
    num_lido = float(num_str)
    soma = soma + num_lido #soma começa inicialmente como 0
    numeros_lidos += 1 
print ("Soma é %.2f" % (soma))

# break 
num_atual = 0
while (True):
    if (num_atual == 5): 
        break
    print(num_atual)
    num_atual += 1
print ("Encerrou")

# continue é tipo um próximo (nao contar)
num_atual = 0
while (num_atual < 10):
    num_atual += 1 
    if (num_atual == 7):
        continue
    print (num_atual)
print ("Encerrou!")

#Uso do For

#For = codigo varias vezes

produtos = ['iphone', 'notebook', 'tablet']
for produto in produtos:
    print (produto)
 #para cada produto na minha lista produtos
 #o valor da variável produto é igual a todos da lista individualmente


for x in range(10):
    print (x)

for x in range(5,20,5):
    print (x)

for x in range (1,4):
    for y in range (1,11):
        print ("%d X %d = %d" % (x,y,x*y))