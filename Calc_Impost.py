####### Calculo para imposto de cada cidade diferente #######

valor = float(input("Insira o valor do produto bruto\n"))
destino = str(input("Insira o destino\nMG-SP-RJ-MS\n"))

print(f"O valor bruto do produto em R$: {valor} com", end=" ")

if destino == "MG":
        print(f"7% de imposto fica {valor + valor * 7/100}")

elif destino == "SP":
    print(f"12% de imposto fica {valor + valor * 12/100}")

elif destino == "RJ":
    print(f"15% de imposto fica {valor + valor * 15/100}")
else:
    print(f"8% de imposto fica {valor + valor * 8/100}")
