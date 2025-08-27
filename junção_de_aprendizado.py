

nome = str(input('Digite seu nome completo')).strip()
print('Analisando vários componentes do nome {}'.format(nome))
list = nome.split() #Separação das palavras para ver ordem dos nomes
newname = nome.upper() # Transformação de nome para identificação do programa
print('Seu nome completo é {} e tem {} letras'.format(nome,len(nome)-1))
print ('Seu primeiro nome é {} e seu último nome é {}'.format(list[0],list[len(list) - 1]))

print('Seu primeiro nome é {} e tem {} letras'.format(list[0],len(list[0])))
print ('No seu nome completo aparece {} vezes a letra o e {} vezes a letra p'.format(newname.count('O'), newname.count('P') ))
print('No seu nome tem o sobrenome Silva? {}'.format("SILVA" in newname) )

