largura = float(input("Insira a largura da parede\n"))
altura = float(input("Insira a altura da parede\n"))

area = altura * largura
litros_tinta = area /2

print(f"A parede tem {largura} x {altura} tem sua area total: {area}")
print(f"Serão necessários {litros_tinta} litros de tintas para pinta-lá")