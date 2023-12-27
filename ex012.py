# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp_Celsisus = float(input("Insira a temperatura em graus Celsisus: "))
temp_Fahrenheit = (temp_Celsisus * 9 / 5) + 32
print("A temperatura {:.1f}ºC corresponde a {:.1f}ºF".format(temp_Celsisus,temp_Fahrenheit))