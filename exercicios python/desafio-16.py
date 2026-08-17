#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.
#ex: Digite um numero: 6.127
#O numero 6.127 tem a parte inteira 6.

num = float(input('Digite um numero real:'))
print('o numero {} tem a parte inteira {}'.format(num, int(num)))