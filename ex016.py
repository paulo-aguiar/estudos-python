# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = int(input("Insira o ângulo que deseja calcular o seno, cosseno e tangente: "))
novo_angulo = math.radians(angulo)
seno = math.sin(novo_angulo)
cosseno = math.cos(novo_angulo)
tangente = math.tan(novo_angulo)
print("O ângulo inserido foi {}°, o seno é {:.4f}, o cosseno é  {:.4f}, e a tangente é {:.4f}!".format(angulo, seno, cosseno, tangente))