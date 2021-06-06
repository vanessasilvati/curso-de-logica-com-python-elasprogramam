# calcular a raiz quadrada do número informado 
# pelo usuário e adicionar a mensagem informando 
# a raiz quadrada do número x é y.

import math
numero = int(input('Informe um número: '))
raiz = int(math.sqrt(numero))

print('A raiz quadrada de {} é {}.'.format(numero,raiz))
