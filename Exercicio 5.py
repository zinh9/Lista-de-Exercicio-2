print("Este programa verifica se você foi aprovado, reprovado, ou recuperação com sua média de notas")

nome_aluno = input("Digite seu nome: ")
nota_1 = float(input("Digite sua primeira nota: "))
nota_2 = float(input("Digite sua segunda nota: "))

media = nota_1 + nota_2 / 2

if media == 0 or media < 5:
    print("Você esta reprovado com média: " +str(media) +" pontos")

elif media == 5 or media < 7:
    print("Você esta de recuperação com média: " +str(media) +" pontos")

elif media == 7 or media <= 10:
    print("Você esta aprovado com média: " +str(media) +" pontos")
