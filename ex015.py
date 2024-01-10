# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retânguo, calcule e mostre o comprimento da hipotenusa.

import math

cateto_oposto = int(input("Insira o valor do cateto oposto: "))
cateto_adjacente = int(input("Insira o valor do cateto adjacente: "))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print("O comprimento da hipotenusa desse triângulo é {}.".format(hipotenusa))