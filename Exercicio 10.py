print("Este programa calcula o desconto de imposto de renda")

salario_bruto = float(input("Digite o salario bruto: "))

if salario_bruto <= 1903.98:
    print("Salario bruto: " +str(salario_bruto))
    print("Desconto: ISENTO")
    print("Salario liquido: " +str(salario_bruto))

elif 1903.98 < salario_bruto <= 2826.65:
    imposto = 7.5 / 100
    deducao = 142.80
    
    valor_imposto = (salario_bruto * imposto) - deducao
    
    print("Salario bruto: " +str(salario_bruto))
    print("Desconto: " +str(valor_imposto))
    print("Salario liquido: " +str(salario_bruto - valor_imposto))
    
elif 2826.65 < salario_bruto <= 3751.05:
    imposto = 15 / 100
    deducao = 548.82
    
    valor_imposto = (salario_bruto * imposto) - deducao
    
    print("Salario bruto: " +str(salario_bruto))
    print("Desconto: " +str(valor_imposto))
    print("Salario liquido: " +str(salario_bruto - valor_imposto))
    
elif 3751.05 < salario_bruto <= 4664.68:
    imposto = 22.5 / 100
    deducao = 636.13
    
    valor_imposto = (salario_bruto * imposto) - deducao
    
    print("Salario bruto: " +str(salario_bruto))
    print("Desconto: " +str(valor_imposto))
    print("Salario liquido: " +str(salario_bruto - valor_imposto))
    
elif salario_bruto > 4664.68:
    imposto = 27.5 / 100
    deducao = 869.36
    
    valor_imposto = (salario_bruto * imposto) - deducao
    
    print("Salario bruto: " +str(salario_bruto))
    print("Desconto: " +str(valor_imposto))
    print("Salario liquido: " +str(salario_bruto - valor_imposto))