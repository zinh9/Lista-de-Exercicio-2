print("Este programa lê um numero de três digitos e soma cada digito, e verifica se o resultado é divisivel por 16 e multiplo de 4 \n")

numero = int(input("Digite um numero de três digitos: "))

if 100 <= numero <= 999:
    digito_centena = numero // 100
    
    digito_dezena = numero % 100
    digito_dezena = digito_dezena // 10
    
    digito_unidade = numero % 10
    
    soma_digitos = digito_centena + digito_dezena + digito_unidade
    
    print("A soma de cada digito é igual a: " +str(soma_digitos))
    
    if soma_digitos % 16 == 0 and soma_digitos % 4 == 0:
        print("A soma dos digitos é divisivel por 16 e multiplo de 4")
    
    else:
        print("A soma dos digitos não é divisivel por 16 e multiplo de 4")
    
else:
    print("O dado não esta válido")