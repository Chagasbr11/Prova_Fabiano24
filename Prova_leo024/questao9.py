def fibonacci_sequence(N):
    # Lista para armazenar a sequência de Fibonacci
    fibonacci = [0, 1]
    
    # Gera a sequência até o N-ésimo número
    for i in range(2, N):
        next_number = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(next_number)
    
    # Retorna os N primeiros números da sequência
    return fibonacci[:N]

# Número de termos da sequência desejado
N = 7  # Exemplo: altere este valor para qualquer outro N

# Gera e exibe a sequência de Fibonacci
resultado = fibonacci_sequence(N)
print(f"A sequência de Fibonacci com {N} termos é: {', '.join(map(str, resultado))}")
