#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

angulo = int(input('Digite um angulo qualquer:'))
from math import sin, cos, tan

seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)
print('O angulo de {} tem o SENO de {:.2f}, o COSSENO de {:.2f} e a TANGENTE de {:.2f}'.format(angulo, seno, cosseno, tangente))