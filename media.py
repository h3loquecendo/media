nome = input("digite o nome do aluno: ")
nota_1 = float(input("digite a primeira nota: "))
nota_2 = float(input("digite a segunda nota: "))
nota_3 = float(input("digite a terceira nota: "))

media = (nota_1 + nota_2 + nota_3)/3

if media >= 7:
    print("aprovado!")
elif media > 4: 
    print("recuperação!")
else:
    print("reprovado!")
print(media)