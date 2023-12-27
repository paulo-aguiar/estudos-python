#Faça um programa que leia um número qualquer e mostre na tela a sua tabuada.

n = int(input("Digite o número que você quer calcular a tabuada:  "))
for i in range(11):
  res = n * i
  print("{} * {} = {}".format(n, i, res))
  i += 1
  
