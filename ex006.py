#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

aluno = input ("Informe o nome do aluno: ")
n1 = float(input ("Informe a primeira nota: "))
n2 = float (input ("Informe a segunda nota: "))
media = (n1 + n2) / 2
print ("A média de {} é: {}".format(aluno,media))