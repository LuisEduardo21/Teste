###### Pagamento de Formas diferentes #######


valor_produto = float(input("Insira o valor do produto\n"))

controle = int(input(f""""

Total a pagar pelo produto R$: {valor_produto}

Insira a forma de pagamento

[1] - Á Vista
[2] - Parcelado

"""))

if controle == 1:
    controle = int(input(""""
    [1] - Dinheiro ou Cheuqe com 10% de desconto
    [2] - Cartão com 5% de desconto
    
    """))
    if controle == 1:
        print(f"Com 10% de desconto, paga apenas R$: {valor_produto - valor_produto * 10/100}")
    elif controle == 2:
        print(f"Com 5% de desconto, paga apenas R$: {valor_produto - valor_produto * 5/100}")
elif controle == 2:
    controle = int(input(""""
    
    [1] - 2x No cartão sem juros
    [2] - 3x No cartão juros de 20%
    """))
    if controle == 1:
        print(f"Valor total a pagar {valor_produto}\nPagando mensalmente uma valor de {valor_produto/2:.2f}")
    elif controle == 2:
        print(f"Com 20% de juros o total a pagar é {valor_produto + valor_produto * 20/100}\nPagando mensalmente uma parcela de {valor_produto/3:.2f}")



