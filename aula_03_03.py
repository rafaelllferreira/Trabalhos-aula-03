#
Nome = input("Informe o nome: ")
sexo = input("Informe o sexo (m ou f): ")
Idade = int(input("Informe a idade: "))

if (Idade >= 18) and (sexo == "m"):
    certificado = int(input("informe o certificado de reservista"))
    print("Você é maior de idade")
if (Idade >= 18):
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
