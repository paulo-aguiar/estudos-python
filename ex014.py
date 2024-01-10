# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import floor
num = float(input("Digite um número decimal qualquer: "))
num_floor = floor(num)
print("O número digitado {} tem seu número inteiro {}.".format(num, num_floor))
