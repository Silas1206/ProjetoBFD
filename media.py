nome=input("Qual o seu nome: ")
n1=float(input("diga sua primeira nota: "))
n2=float(input("diga sua segunda nota: "))

media=(n1 + n2)/2

if media>=7:
    print(f"aluno {nome}, sua média é {media} e você foi Aprovado!")
elif media>=4:
    print(f"aluno {nome}, sua média é {media} e você está de Recuperação!")
else:
    print(f"aluno {nome}, sua média é {media} e você está de Reprovado!")



