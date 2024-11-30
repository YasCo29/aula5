# 1 - Peça para o usuário digitar um número, verifique se um número é positivo, negativo ou zero.

numero = int(input('digite um número:'))

if numero > 0:
    print('positivo')
    
elif numero < 0:
          print('negativo')
else:
    print('zero')



# 2-Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com base na idade.

idade = int(input('digite sua idade:'))
if idade >= 16:
    print('pode votar')
else:
    print('não pode votar')
    
# 3*Declara uma variável com um número qualquer, determine se um número é par ou ímpar.

numero1 = int(input('digite um número:'))

if numero1 % 2 == 0:
    print(' o numero é par')
else:
    print(' o numero  é impar')
    
# 4- Usuário vai digitar 3 números, para criar um triângulo, verifique se um triângulo é equilátero, isósceles ou escaleno:

# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

lado1 = int(input('lado'))
lado2 = int(input('lado'))
lado3 = int(input('lado'))

if lado1 != lado2 != lado3 != lado1:
    print('esse triangulo é escaleno')
    
elif lado1 == lado2 == lado3 :
    print('esse triangulo é equilátero ') 

else:
    print('esse triangulo é isósceles ')



# 5- Determine se um número é múltiplo de 5 e 7.
print('Mutiplo de 5 e 7')
numero = int(input('digite um número:'))

if numero % 5 == 0 and numero % 7 == 0: 
    print(' é mutiplo de 5 e 7')
else:
    print(' não é mutiplo de 5 e 7')
    

# 6 -Verifique se um número é positivo e maior que 10
numero = int(input('digite um número:'))

if numero > 10:
    print('positivo e maior que 10')
    
elif numero < 10:
          print('negativo')
else:
    print('zero')



# 7 - Verifique se um número é divisível por 3 ou 5.

print('Divisivel de 3 e 5')
numero = int(input('digite um número:'))

if numero % 3 == 0 or numero % 5 == 0: 
    print(' é divisivel de 3 e 5')
else:
    print(' não é divisivel de 3 e 5')
    




