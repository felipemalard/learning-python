print ("Olá")

# comentário normal

''' esse é um comentário
de multiplas linhas
teste'''

print ("Pera", "Uva", "Beterraba", sep = " - ") #separar itens
print ("Pera", "Uva", "Beterraba", end = " fim ") #no final (terminar)
print ("\n Eu quero quebrar \n a linha desse texto") #mudar de linha
print ("Pera", "Uva", "Beterraba", sep = "\n") #um texto em cada lina

#Trabalhar com variáveis com o .format
print ("A pontuação do {} foi de {} pontos".format("Fernando", "10"))

''' Variável'''
_felipe = 20 # _felipe é diferente de felipe!
print (_felipe)

texto = "olá isso é um texto"
print (texto)

#Tipo booleano muito usado
var = True
print (var)
var = False 
print (var)

#Tipo nenhum
var = None
print (var)
var = 10
print (var)

#Formatação 
nome = "Fernando"
texto_formatado = "O nome dele é %s" % (nome)
print (texto_formatado)

# utilizando outras formatações 
nome = "Felipe"
idade = 19
altura = 1.71
texto = "O meu nome é %s, tenho %d anos e tenho %.2f metros de altura" % (nome, idade, altura) # %.2f (apenas duas casas)
print (texto)

valor = True
print ("O valor é %s" % (valor))
print ("O valor é %d" % (valor)) # 1 é True e 0 é False

dia , mes , ano = 31, 1, 2006 #forma mais minimalista
print ("Eu nasci no dia %d/%d/%d" % (dia, mes, ano))

# Operações aritméticos

num1, num2, num3 = 10, 16, 50
media = (num1 + num2 + num3)/3 # Cuidado com a ordem de prioridade
print ("A média é %.2f" % (media))

# Operadores Lógicos 

#AND
resultado1 = True and False
print (resultado1) # todos tem que ser verdadeiro! 
resultado2 = True and True
print (resultado2)

#exemplo de aplicação
clima_bom = True
disposicao = True
print ("Vou ao mercado?", clima_bom and disposicao) #aplicação com o and

#OR
resultado = True or False
print (resultado)  #apenas uma precisa ser verdadeiro 

#NOT
resultado = True
print (not resultado) #falso resultado

porta_aberta = False
tenho_chave = True
print ("Estou trancado?", not porta_aberta and not tenho_chave)

# Type

texto = "Oi" #str
numero = 2 #int
decimal = 1.5 #float
booleano = True #bool

print (type(texto)) 
print (type(numero)) 
print (type(decimal))
print (type(booleano))

# Casting (transformar dados de um tipo para outro)

texto1 = "2" #string
texto2 = "1.5" #string
numero1 = int(texto1) # Converter para inteiro 
numero2 = float(texto2) # Converter para decimal

num = 21.56765
inteiro = int(num)
print ("A parte inteira de %f é %d" % (num, inteiro))

numero = 123
texto = str(numero)
digitos = len(texto) # Para usar o len transformar o numero em string
print ("O numero %d tem %s digitos" % (numero, digitos))

saldo = 0
variavel = bool(saldo)
print ("O seu saldo está zerado?", not variavel)

# Input

meu_nome = input("Qual o seu nome? ")
print ("Eu me chamo %s" % (meu_nome))

entrada_usuario = input ("Digite 1 para verdadeiro ou 0 para falso: ") # Lembrar que numeros aqui são strings!!
valor_inteiro = int(entrada_usuario) #Transforma o 1 ou 0 em numeros (string -> numero)
valor_logico = bool(valor_inteiro) #Transforma em um valor lógico
print ("Você escolheu: %s" % (valor_logico))
print ("ou ainda, você escolheu: %d" % (valor_inteiro))


print("Vamos dividir numeros agora?")
numero1 = input("Escreva um numero: ")
valor1 = float(numero1)
numero2 = input ("Escreva outro numero: ")
valor2 = float(numero2)
print("Escolha o primeiro numero", valor1, "Escolha o segundo numero", valor2)
print ("A divisão entre eles é: ", valor1 / valor2)

#Atenção
# numero = numero + 1 -> numero += 1

num = 10
booleana = (num == 20) #comparando num com o numero 
print (booleana)

num = 10
booleana = (num != 20) #se são diferentes
print (booleana)

digitar = input('Digite a senha: ')
senha = 543 #tomar cuidado com isso! se é string, inteiro (tudo isso interfere)
senha1 = (int(digitar) == senha)
print (senha1)

#lembrar que começa no zero
texto = 'abcdegf'
texto = texto[:4] + texto [5:] #abcd + gf
print (texto)

texto = "exemplo"
texto1 = texto[2:4] #nesse caso o ultimo deve ser um a mais
print (texto1)

texto = input("Digite o texto: ")
print (texto[:-1]) #tira um caractere

texto = "Programação"
print("a" in texto) #in é para se está contido

texto = input("Digite: ")
print ("O texto tem uma vogal?: ", bool(texto in "a" or "e" or "i" or "o" or "u"))

texto = "Programação"
print("s" not in texto) #not in é o contrario
print (len(texto)) # len = tamanho do texto