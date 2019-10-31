###### Emprestimo para uma casa em que o emprestimo não pode ultrapassar 30% do salário #######


casa = float(input("Insira o valor da casa\n"))
salario = float(input("Insira o salário do comprador\n"))
anos = int(input("Insira em quantos anos ele vai pagar\n"))

prestacao = casa / (anos * 12)


if prestacao > salario * 30/100:
    print("Emprestimo negado!!")

else:
    print("Emprestimo aceito")
