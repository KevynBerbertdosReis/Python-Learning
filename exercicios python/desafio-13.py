salario = int(input('Qual é o salário do funcionário?:'))
aumento = salario * 15 / 100
novo_salario = salario + aumento
print('O funcionário que ganhava R$ {}, com o aumento de 15%, passará a ganhar R$ {}'.format(salario, novo_salario))