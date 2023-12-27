# Escreva um programa que pergunte  a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia  e R$0,15 por quilometros rodados.

dias_alugados = int(input("Por quanto dias o carro foi alugado? "))
km_percorridos = float(input("Informe a quilometragem percorrida com o carro: "))
preco_total = (0.15 * km_percorridos) + (60 * dias_alugados)
print("O valor total do aluguel do carro é de R${:.2f}.".format(preco_total))