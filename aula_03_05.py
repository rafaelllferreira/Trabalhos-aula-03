#
nome = input("Nome do doador: ")
idade = int(input("Idade: "))
peso = int(input("peso: "))
hrs = int(input("Quantidade de horas dormidas nas últimas 24hrs: "))

if (idade >= 16 and idade <= 69) and (peso >= 50) and (hrs >= 6):
    print("Pode doar")
else:
    print("Não pode doar")