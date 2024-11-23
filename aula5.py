# # por padrão o input e um texto
# numero1 = input ('digite um numero')
# numero2 = input ('digite um numero')
# soma = numero1+numero2
# print(soma)

# #Formas de juntar (concatenação):
# nome= input ('digite seu nome')
# print('seja bem vindo (a)', nome)
# print('seja bem vindo (a)'+ nome)
# print(f'seja bem vindo (a) {nome}')
# print('seja bem vindo (a) {} ' . format (nome))
# print('seja bem vindo (a)  %s ' % (nome))


# 1 Imprima uma mensagem de boas-vindas na tela.

print('seja bem vindo (a)')

# 2 Declare uma variável booleana verdadeiro com o valor True e imprima seu tipo
verdadeiro =  True
falso = False
tipo = type(verdadeiro)
print (tipo)



# 3 Imprima o resultado da multiplicação de dois números decimais de sua escolha

print(6.3*8.7)

# 4 Imprima o resultado da divisão de dois números inteiros de sua escolha.
print(14/8)

# 5 Imprima o resultado da subtração de dois números inteiros de sua escolha
print(10-5)

# 6 Imprima o resultado da divisão inteira de dois números inteiros de sua escolha.
print(16/4)

# 7 Imprima o resultado da multiplicação de 4 números decimais de sua escolha
print(5*8*7*6)

# 8 Declare uma variável numero e atribua um número inteiro. Em seguida,  imprima o dobro desse número

N1= 45

print(N1*2)
# 9 Crie uma calculadora de soma com as ferramentas que vc já  conhece(Use apenas input, print e variavel)
N1 = input ('digite o primeiro numero')
N2= input ('digite o segundo numero')

resultado = int(N1)+int(N2)

print("total:", resultado)

# 10 Crie um sistema de cadastro com as estruturas que vc já  conhece(Use apenas input, print e variavel)
print('seja bem vindo (a)! Por gentileza, preencha os dados abaixo:')
nome= input('Nome Completo:')
data= input('data de nascimento:')
cpf= input('CPF:')
rg=  input('RG:')
endereço =input(' endereço:')
email =input(' e-mail:')

print('Cadastro finalizado!')

