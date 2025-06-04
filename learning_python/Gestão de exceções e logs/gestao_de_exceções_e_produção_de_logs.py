''' 
Exceções = Erro -> fim do programa 

---> Sempre é necessário controlar o fluxo do programa em caso de erro seguindo um caminho diferente!

'''

print ('Início 1')
lista = [1,2,3]

try: #pode ocorrer erro
    print (lista[10])

except: #executado em caso de erro
    print('Falha ao acessar, linha não encontrada')
    
print ('Fim')



print ('Início 2')
lista = [1,2,3]

try: #pode ocorrer erro
    print (lista[10])

except Exception as error: #mostra o tipo de erro na mensagem (Exception == error)
    print ('Falha ao acessar, linha não encontrada. Mensagem de erro: ' + str(error))
    
print ('Fim')



print ('Início 3')
lista = [1,2,3]

try: #pode ocorrer erro
    print (lista[10])

except: #executado em caso de erro
    print('Falha ao acessar, linha não encontrada')

finally: #sempre executado, com ou sem erro -> ótimo para desalocar os recursos
    del lista
    print('Lista excluída!')
    
print ('Fim')



print ('Início 4')
lista = [1,2,3]

try: #pode ocorrer erro
    print (lista[2])

except: #executado em caso de erro
    print('Falha ao acessar, linha não encontrada')

else: #executado somente se não houver erro 
    print('Não houve erro')
    
print ('Fim')

# Tudo junto!

print ('Início com tudo junto!')
lista = [10,14,20]
print (lista)

try: #pode ocorrer erro
    numero = (int(input('Escreva o numero para acessar uma posição na lista: ')) - 1)
    print ('O número na posição escolhida é: %i' % (lista[numero]))

except Exception as error: #executado em caso de erro
    print('Falha ao acessar, posição não encontrada. Mensagem de erro: ' + str(error))

else: #executado somente se não houver erro 
    print('Não houve nenhum erro!')

finally: #executado com erro ou sem!
    del lista
    print ('Lista deletada!')
    
print ('Fim')

#tratamentos pra erros específicos:


print ('Início erro 1')
lista = [1,2,3]

try: #vai ocorrer dois erros
    print (lista[10])
    divisao = 10 / 0

except IndexError as erro1: #executa caso o erro do tipo index error ocorrer
    print ('Falha ao acessar, linha não encontrada. Mensagem de erro: ' + str(erro1))
    
except ZeroDivisionError as erro2: #executa caso o erro do tipo divisão por zero ocorrer
    print ('Não é possível a divisão por zero. Mensagem de erro: ' + str(erro2))

#executa a primeira linha de erro!

print ('Fim')

# Gerando as próprias exceções


print ('Inicio 5')

def numero_positivo (numero):
    if numero < 0:
        raise ValueError ('O número não pode ser negativo!') #esse passa a ser o nome do erro
    print (numero)

try:
    numero_positivo(-1)
except ValueError as erro1:
    print ('O erro é: ' + str(erro1))
except Exception as erro_qualquer:
    print ('O erro é: ' + str(erro_qualquer))


print ('Inicio 6')

def numero_positivo (numero):
    assert (numero >= 0)
    print (numero)

try:
    numero_positivo(-1)
except AssertionError as erro1:
    print ('O erro é: ' + str(erro1))
except Exception as erro_qualquer:
    print ('O erro é: ' + str(erro_qualquer))



# Introdução a logs!
'''
São mensagens que o programa escreve para contar o  que está acontecendo!

Levels: Debug, Info, Warning (padrão), Error, Critical

Podem ser salvadas em disco ou tela

handler = destino das mensagens do log
'''

caminho = "Colocar o caminho para o log"

def custom_logger (level, message):
    import logging # biblioteca para gerar logs
    logger = logging.getLogger(__name__) #nome
    if not (len(logger.handlers)): # Se o logger ainda não tem nenhum handler, então adicione os handlers.
        logging.basicConfig(level=logging.INFO) #info ou superiores
        c_handler = logging.StreamHandler() #envia logs para o terminal
        f_handler = logging.FileHandler(caminho) #caminho para a criação do log
        format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') #formato do log
        c_handler.setFormatter(format) #coloca o formato no terminal
        f_handler.setFormatter(format) #coloca o formato no arquivo log
        logger.addHandler(c_handler) # conecta as saídas para onde os logs serão enviados
        logger.addHandler(f_handler) # conecta as saídas para onde os logs serão enviados

# parte que registra as mensagens 
    if level == 'debug':
        logger.debug(message) #envia a mensagem com o nível correspondente 
    elif level == 'info':
        logger.info(message)
    elif level == 'warning':
        logger.warning(message)
    elif level == 'error':
        logger.error(message)
    else:
        logger.critical(message)


custom_logger ('info','Inicio do programa!')

lista = [1,2,3]

try:
    print (lista[10])
except:
    custom_logger ('error','Indice incorreto!')

custom_logger ('info','Final do programa!')
    