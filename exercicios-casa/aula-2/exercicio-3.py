# Crie dois problemas e escreva os respectivos códigos:
# a) Um problema que possa ser utilizado o operador de subtração.
# b) Um problema que possa ser utilizado o operador de multiplicação.

# a
## Pedro tem na conta R$4890,00 e precisa pagar o aluguel, que é R$1255,00 e também a conta de luz, que é R$365,00.
## Quanto ainda sobra para Pedrinho? 

disponivelNaConta = 4890.00
valorAluguel = 1255.00
contaDeLuz = 365.00

disponivelParaUso = disponivelNaConta - valorAluguel - contaDeLuz

print(disponivelParaUso)

#-------------------------------------------------------------------------------------------------------------------------#

# b

## Maria tem uma moto que consome 1 litro de gasolina a cada 27km. O tanque de sua moto cabem 15 litros de gasolina. Com um tanque cheio, quantos km no total a Maria consegue andar?

aCadaUmLitro = 27
capacidadeDoTanque = 15

autonomiaEmKm = aCadaUmLitro * capacidadeDoTanque

print(autonomiaEmKm)