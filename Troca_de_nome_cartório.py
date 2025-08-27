import random
import time
print('Olá, bem vindo ao sistema de troca de sobrenomes, somos do cartório ATB. Para fazer a troca de sobrenome no nosso cartório, digite seus dados aqui.')
nome = str(input('Digite seu nome completo').strip())
CPF = int(input('Digite seu CPF'))
mae = str(input('Digite o nome da sua mãe').strip())
rg = int(input('Digite seu RG'))
print('Bem-vindo(a) {}'.format(nome))
print('Analisando o nome {}'.format(nome))
anly = nome.split()
print('No seu nome completo existem {} sobrenomes, sendo eles {} '.format(len(anly[1:]),anly[1:]))
print('Quais deles você deseja alterar? Pedimos para que, se caso o nome anterior foi escrito de forma errada, repetir o processo.')
antname = str(input('Digite o sobrenome que deseja alterar de forma IDÊNTICA ao escrito anteriormente.'))

newname =  str(input('Digite o novo sobrenome que deseja inserir de forma CORRETA.'))

print('-=-' * 10)
print('LOADING...')
print('-=-' * 10)
time.sleep(5)
if antname in nome:
    print('Com as informações aferidas, segue informações com cunho de confirmação. \n NOME ANTERIOR: \033[1;30;46m {} \033[m \n PORTADOR(a) DO CPF: {} \n PORTADOR(a) do RG {} \n FILHO(a) de {} \n Seu novo nome será \033[0;30;42m {} \033[m \n DADOS GERADOS. PARA CONFIRMAÇÃO, CONTACTE O CARTÓRIO VIA OS MEIOS TELEFÔNICOS E APRESENTE O SEGUINTE PROTOCOLO: \n PROTOCOLO: {}'.format(nome, CPF, rg,mae, nome.replace(antname, newname), random.randint(1000,9999)))
else:
    print('O sobrenome não consta no nome anterior, por favor, refaça o processo.')

