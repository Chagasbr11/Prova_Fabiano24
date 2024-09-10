# Código para ler 10 números inteiros e calcular a soma dos quadrados

# Inicializando o vetor 'a' com 10 números inteiros
a = []

# Loop para inserir os números no vetor
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    a.append(numero)

# Calculando a soma dos quadrados dos elementos do vetor
soma_quadrados = sum([num ** 2 for num in a])

# Mostrando o resultado
print(f"A soma dos quadrados dos elementos do vetor é: {soma_quadrados}")
