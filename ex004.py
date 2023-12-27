#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor

n1 = int(input ("Digitei um número: "))
antecessor = (n1 - 1)
sucessor = (n1 + 1)
print ("O antecessor de {} é {} , e o sucessor é {}".format(n1, antecessor,sucessor))
