# Função para calcular a média
def calcular_media(notas):
    return sum(notas) / len(notas)

# Lista para armazenar as notas
notas = []

# Solicitando as 4 notas
for i in range(4):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

# Calcula a média inicial
media = calcular_media(notas)
print(f"Média inicial: {media:.2f}")

# Verifica se foi aprovado na média inicial
if media >= 7:
    print("APROVADO")
else:
    # Caso contrário, solicita a nota da prova final
    nota_final = float(input("Digite a nota da prova final: "))
    notas.append(nota_final)

    # Recalcula a média incluindo a nota da prova final
    nova_media = calcular_media(notas)
    print(f"Nova média: {nova_media:.2f}")

    # Verifica a nova média
    if nova_media >= 5:
        print("APROVADO")
    else:
        print("REPROVADO")
