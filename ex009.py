# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta , pinta uma área de 2m².

largura = float(input("Qual a largura da parede? "))
altura  = float(input("Qual a altura da parede? "))

area_parede = largura * altura 
litros_tinta = area_parede / 2

print("A área a ser pintada dessa parede é de {} m².\nVocê irá precisar de {} litros de tinta para pintá-la.".format(area_parede, litros_tinta)) 