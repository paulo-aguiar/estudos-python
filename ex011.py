# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Qual é seu salário atual? R$"))
novo_salario = salario + (salario * 15 / 100)
print("Seu salário atual é de R${:.2f}, mas você receberá 15% de aumento, então seu novo salário será R${:.2f}.".format(salario, novo_salario))