#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo.
#calcule e mostre o comprimento da hipotenusa.

Co = int(input('Digite o comprimento do cateto oposto:'))
Ca = int(input('Digite o comprimento do cateto adjacente:'))

from math import hypot

hi = hypot(Co, Ca)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))