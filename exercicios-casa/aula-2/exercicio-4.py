# A creche possui 8 alunos, e a cozinheira reservou as seguintes frutas para serem
# servidas no lanche da tarde:

# 1 dúzia de laranjas
# 2 dúzias de bananas
# 1⁄2 dúzia de maçãs

# Cada aluno comeu 4 frutas no total. Dois alunos levaram para casa as frutas que
# sobraram. Quantas frutas cada um deles levou para casa? (vai dar um trabalhinho, mas
# você consegue)

alunos = 8
laranjas = 12
bananas = 24
macas = 6

frutasNoTotal = laranjas + bananas + macas
frutasComidas = alunos * 4
frutasQueSobraram = frutasNoTotal - frutasComidas
cadaAlunoLevou = frutasQueSobraram / 2

print(frutasNoTotal)
print(frutasComidas)
print(frutasQueSobraram)
print('Cada aluno levou:',cadaAlunoLevou,'frutas cada')

#--------------------------------------------------------------------------------#

# Segunda opção

alunos = 8
laranjas = 12
bananas = 24
macas = 6

frutasNoTotal = laranjas + bananas + macas
divisao = (frutasNoTotal - alunos * 4) / 2

print(divisao)
