
def calcular_media(notas, nome):
    if nome in notas:
        media = sum(notas[nome]) / len(notas[nome])
        return media


    else:
        return 0


notas = {}

for i in range(3):
    nome = input('nome:')
    nota1 = float(input('primeira nota'))
    nota2 = float(input('segunda nota'))

    notas[nome] = [nota1, nota2]

print(notas)

nome = input('digite o nome da um aluno:')
media = calcular_media(notas, nome)

print('Media do aluno:', media)
