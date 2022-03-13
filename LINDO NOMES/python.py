print('crie um programa que leia o nome completo de uma pessoa e mostre'
      '\nO nome com todas as letras maiusculas e minusculas.'
      '\nQuantas letras ao todo sem considerar espaços'
      '\nQuantas letras tem o primeiro nome.')
print()
nome = str(input('Qual o seu nome completo? ')).strip()
print('analisando seu nome..')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
