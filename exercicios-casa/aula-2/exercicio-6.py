#Exercício 6
#Mencione o tipo de dado (string, inteiro ou float). Contém pegadinhas:

#a) “Mariana”                = STRING
#b) “@queroserprogramadora”  = STRING
#c) 36.7                     = FLOAT
#d) 287656453                = INTEIRO
#e) “verdadeiro”             = STRING
#f) 1.72                     = FLOAT
#g) “456789”                 = STRING

a = "Mariana"
b = "@queroserprogramadora"
c = 36.7
d = 287656453
e = "verdadeiro"
f = 1.72
g = "456789"

# validar valores
respostaA = isinstance(a, str)
respostaB = isinstance(b, str)
respostaC = isinstance(c, float)
respostaD = isinstance(d, int)
respostaE = isinstance(e, str)
respostaF = isinstance(f, float)
respostaG = isinstance(g, str)

# Respostas validadas
print("A resposta A é string? ", respostaA)
print("A resposta B é string? ", respostaB)
print("A resposta C é float? ", respostaC)
print("A resposta D é inteiro? ", respostaD)
print("A resposta E é string? ", respostaE)
print("A resposta F é float? ", respostaF)
print("A resposta G é string? ", respostaG)
