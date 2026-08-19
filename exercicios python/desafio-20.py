#o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

Alunos = ['João', 'Naiara', 'Pedro', 'Maria']
import random 
random.shuffle(Alunos)
print('A ordem de apresentação será: {}'.format(Alunos))