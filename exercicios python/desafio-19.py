#um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

Alunos = ['João', 'Naiara', 'Pedro', 'Maria']
from random import choice
Escolhido = choice(Alunos)
print('O aluno escolhido foi o: {}'.format(Escolhido))
