# Fatura do cartão

# Se vier até 200.00 vc paga tudo
# se vier ate 399.00 vc paga a maior parte
# se vier mais de 399.00 voce fica devendo a maior parte

fatura = float(input('Qual valor da fatura? '))

if fatura <= 200.00:
    print('Você paga tudo.')
elif fatura <= 399.00:
    print('Será pago a maior parte')
else:
    print('Você fica devendo a maior parte.')