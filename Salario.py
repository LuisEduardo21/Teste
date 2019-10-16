######### O Programa e para calcular o porcentagem de aumento do salário #######



salario = int(input("Insira o salario que vai receber o reajuste: "))
porcentagem = int(input(f"Insira a % que vai ser analisadodo valor: {salario}"))
reajuste = salario * porcentagem/100

print(f"valor bruto {salario}")
print(f"{porcentagem}% do salario {salario} é {salario*porcentagem/100}")
print(f"O salario de {salario} com {porcentagem}%  de aumento é {salario + reajuste}")
print(f"O salario de {salario} com {porcentagem} % de desconto é {salario-reajuste}")