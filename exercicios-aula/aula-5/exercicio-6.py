# Mais condições
## elif

## Menos de 12 anos = criança
## menos de 18 anos = adolescente
## menos de 60 anos = adulto


idade = int(input('Qual sua idade? '))

if idade < 12:
    print('Você é uma criança.')
elif idade < 18:
    print('Você é um adolescente.')
elif idade < 60:
    print('Você é um adulto.')
else:
    print('Você é idoso.')