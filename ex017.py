# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

aluno1 = input("Digite o nome do aluno: ")
aluno2 = input("Digite o nome do aluno: ")
aluno3 = input("Digite o nome do aluno: ")
aluno4 = input("Digite o nome do aluno: ")
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
print("O aluno escolhido para apagar o quadro é {}!".format(random.choice(lista_alunos)))
