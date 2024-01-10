# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome  dos quatro alunos e mostre a ordem sorteada.

import random

aluno1 = input("Digite o nome do aluno: ")
aluno2 = input("Digite o nome do aluno: ")
aluno3 = input("Digite o nome do aluno: ")
aluno4 = input("Digite o nome do aluno: ")
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista_alunos)
print("Os alunos citados apresentarão os trabalhos na seguinte ordem: ")
print(lista_alunos)
