Money = float(input('Quanto dinheiro você tem na carteira? R$: '))
conversao_dolar = Money / 5.13530
print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(Money, conversao_dolar))