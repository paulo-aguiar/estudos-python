# Faça um agoritmo que leia o preço  de um produto e mostre seu novo preço, com 5% de desconto.

preco_produto = float(input("Qual o preço do produto desejado? R$"))
preco_final = preco_produto - (preco_produto * 5) / 100
print("Seu produto terá 5% de desconto, com o preço final de R${:.2f}.".format(preco_final))