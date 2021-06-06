# Pedir um número para o usuário e validar se é par ou impar
# mensagem: se é par ou impar

numero = int(input('Informe um número: '))

if(numero % 2 == 0):
    print('Este número é par.')
else:
    print('Este número é ímpar.')