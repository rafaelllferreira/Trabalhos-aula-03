#
Nome = (input("Nome do aluno: "))
n1 = float(input("Informe a nota do 1° bimestre: "))
n2 = float(input("Informe a nota do 2° bimestre: "))
n3 = float(input("Informe a nota do 3° bimestre: "))
n4 = float(input("Informe a nota do 4° bimestre: "))
media = (n1+n2+n3+n4)/4
if media >= 7:
    print(f"Aluno(a) {Nome} aprovado com média {media}")
elif media >= 3:
    print(f"Aluno(a) {Nome} recuperação com media {media}")
else:
    print(f"Aluno(a) {Nome} reprovado com media {media}")