##### Exercicio de aluguel de um carro ####

km_rodados = float(input("Insira a quantodades de Kms rodados\n"))

dias_alugados = int(input("Insira a quantidades de dias alugados\n"))


total_a_pagar = dias_alugados * 60 + km_rodados * 0.15



print(f"Total de Kms rodados {km_rodados}")
print(f"Total de dias alugados {dias_alugados}")
print(f"Total a pagar pelo uso do veiculo R$: {total_a_pagar}")