import random


print('Digite o nome dos alunos para fazer o sorteio em ordem')
n1 = str(input('Digite a primeiro nome '))
n2 = str(input('Digite a segundo nome '))
n3 = str(input('Digite a terceiro nome '))
n4 = str(input('Digite a quarto nome '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(lista)