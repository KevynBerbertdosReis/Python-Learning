Prod = float(input('Digite o preço do produto: R$:'))
Desc = Prod * 5 / 100
valorF = Prod - Desc
print('O valor do produto com o desconto de 5%, fica no valor de R$:{:.2f}'.format(valorF))