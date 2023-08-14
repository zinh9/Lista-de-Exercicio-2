print("Este programa verifica se o financiamento foi concedido ou negado")

salario = float(input("Digite o seu salario: "))
financiamento = float(input("Digite o financiamento pretendido: "))

if financiamento <= (salario * 5):
    print("Financiamento concedido")
else:
    print("Financiamento negado")

print("Obrigado por nos consultar")