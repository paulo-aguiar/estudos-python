#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input("Informe um valor em metros: "))
centimetro = (m / 100)
milimetro = (m / 1000)
print("O valor em metros informado, corresponde a {} centímetros e a {} milímetros.".format(centimetro,milimetro))
