print("Este programa verifica qual é a pessoa mais nova de acordo com a idade de duas pessoas")

ano = int(input("Digite o ano atual: "))
nome_1 = input("Pirmeira pessoa, digite seu nome: ")
idade_1 = int(input("Digite a sua idade: "))

nome_2 = input("Segunda pessoa, digite seu nome: ")
idade_2 = int(input("Digite sua idade: "))

if idade_1 > idade_2:
    print(nome_2 +" é mais novo e nasceu em " +str(ano - idade_2))
    
elif idade_1 == idade_2:
    print(nome_1 +" e " +nome_2 +" tem a mesma idade e nasceram em " +str(ano - idade_1))
    
else:
    print(nome_1 +" é mais novo e nasceu em " +str(ano - idade_1))