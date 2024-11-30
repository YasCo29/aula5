#Exercício 1: Escreva um programa que use a função range() para gerar os números pares de 2 a 20 e, em seguida,imprima cada número.

Lista = list(range(2,21,2))
print(Lista)


#Exercício 2: Escreva um programa que use a função range() para gerar os múltiplos de 5 em 5 até 50, em seguida, calcule e imprima a soma desses 
#múltiplos.

Lista1 = list(range(5,51,5))
print(Lista1)
soma = sum(Lista1)
print(soma)


#Exercício 1: Crie uma lista chamada pessoas que contenha os números inteiros de pessoa1 a pessoa5 e imprima-a na tela.

pessoas = ['pessoa1', 'pessoa2', 'pessoa3', 'pessoa4', 'pessoa5']
print(pessoas)


#Exercício 2: Acesse e imprima o terceiro elemento da lista numeros.
lista2 = [1,2,3,4,5]
print(lista2[2])

#Exercício 3: Adicione o número 9 à lista numeros e imprima a lista atualizada.
lista = [1,2,3,4,5,6,7,8]
lista.append(9)
print(lista)

#Exercício 4: Remova o número 5 da lista numeros e imprima a lista resultante.
lista = [1,2,3,4,5,6,7,8,9,10]
lista.remove(5)
print(lista)

#Exercício 5: Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista numeros e imprima o 
#resultado.

carros= ['onix', 'voyage', 'yaris']
numeros = [1,2,3]
print(numeros, carros)



#mercado

lista_produtos = ['macarrão', 'feijão', 'uva', 'sal']

lista_valores = [2.50,5.00,10.00,5.00]

meus_valores = []
carrinho = []

print('escolha seus produtos:')
print(lista_produtos)

produto1= int(input('digite o produto:'))
produto2= int(input('digite o produto:'))
produto3= int(input('digite o produto:'))

carrinho += (lista_produtos[produto1],lista_produtos[produto2],lista_produtos[produto3])
meus_valores += (lista_valores[produto1],lista_valores[produto2],lista_valores[produto3])
print('seus produtos', carrinho)
print('valores', meus_valores)
soma = sum(meus_valores)
print('==============TOTAL===============')
print('R$', soma)


#dicionario

pessoa = {
    'nome': 'Maria',
     'idade': 25,
    'CPF':123456789,
    'RG': 12345678,
    }

nome_pessoa= pessoa['nome']
print(nome_pessoa)

print(pessoa)



#condicionais - condição
idade = int(input('Digite sua idade'))
#if 10 > 2:
  #  print('10 é maior')
#else:
   # print('10 é menor)
    
if idade == 20:
   print('Voce tem 20 anos')
else:
   print('voce tem mais ou menos de 20 anos')
    
#Random
   
   import random

print('SISTEMA DA MEGA SENA')

numero_da_sorte1 = random.randrange(1,2)
numero_da_sorte2 = random.randrange(1,2)
numero_da_sorte3 = random.randrange(1,2)
numero_da_sorte4 = random.randrange(1,2)
numero_da_sorte5 = random.randrange(1,2)
numero_da_sorte6 = random.randrange(1,2)

lista_sorteada = [numero_da_sorte1,numero_da_sorte2, numero_da_sorte3, numero_da_sorte4,numero_da_sorte5, numero_da_sorte6]


meu_chute1 = int(input('nº 1'))
meu_chute2 = int(input('nº 2'))
meu_chute3 = int(input('nº 3'))
meu_chute4 = int(input('nº 4'))
meu_chute5 = int(input('nº 5'))
meu_chute6 = int(input('nº 6'))

meus_chutes =  [meu_chute1, meu_chute2, meu_chute3, meu_chute4, meu_chute5, meu_chute6]


if meus_chutes in lista_sorteada:
    print('VOCÊ É O MILINÁRIO DA MEGA DA VIRADA')
else:
    print('Não foi dessa vez')


print(f'''
n°1{numero_da_sorte1}
n°2{numero_da_sorte2}
n°3{numero_da_sorte3}
n°4{numero_da_sorte4}
n°5{numero_da_sorte5}
n°6{numero_da_sorte3}
''')

import random

print('SISTEMA DA MEGA SENA')

numero_da_sorte1 = random.randint(1,60)
print(numero_da_sorte1)
numero_da_sorte2 = random.randint(1,60)
print(numero_da_sorte2)
numero_da_sorte3 = random.randint(1,60)
print(numero_da_sorte3)
numero_da_sorte4 = random.randint(1,60)
print(numero_da_sorte4)
numero_da_sorte5 = random.randint(1,60)
print(numero_da_sorte5)
numero_da_sorte6 = random.randint(1,60)
print(numero_da_sorte6)

lista_sorteada = []

lista_sorteada.append(numero_da_sorte1)
lista_sorteada.append(numero_da_sorte2)
lista_sorteada.append(numero_da_sorte3)
lista_sorteada.append(numero_da_sorte4)
lista_sorteada.append(numero_da_sorte5)
lista_sorteada.append(numero_da_sorte6)
                      


meu_chute1 = int(input('nº 1'))
meu_chute2 = int(input('nº 2'))
meu_chute3 = int(input('nº 3'))
meu_chute4 = int(input('nº 4'))
meu_chute5 = int(input('nº 5'))
meu_chute6 = int(input('nº 6'))




if meu_chute1 and meu_chute2 and meu_chute3 and meu_chute4 and meu_chute5 and meu_chute6 in lista_sorteada:
    print('VOCÊ É O MILINÁRIO DA MEGA DA VIRADA')
elif meu_chute1 or meu_chute2 or meu_chute1 or meu_chute2 or meu_chute3 or meu_chute4 or meu_chute5 or meu_chute6    in lista_sorteada:
    print('Você ganhou R$ 50k') 
else:
    print('Não foi dessa vez')













