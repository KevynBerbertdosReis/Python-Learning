diasA = int(input('Quantos dias o carro foi alugado?:'))
kmR = int(input('Quantos km foram rodados?:'))
print('O total a pagar é de R${:.2f}'.format(diasA * 60 + kmR * 0.15))