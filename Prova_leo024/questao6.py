# Função para verificar se o CPF é par ou ímpar
def verificar_cpf(cpf):
    # Remover os pontos e o traço do CPF
    cpf_numeros = cpf.replace('.', '').replace('-', '')
    
    # Verificar se o CPF contém exatamente 11 dígitos
    if len(cpf_numeros) != 11 or not cpf_numeros.isdigit():
        return "CPF inválido. Certifique-se de que o CPF tenha 11 dígitos."

    # Somar todos os dígitos do CPF
    soma_cpf = sum(int(digito) for digito in cpf_numeros)

    # Verificar se a soma é par ou ímpar
    if soma_cpf % 2 == 0:
        return f"A soma dos números do CPF ({soma_cpf}) é PAR."
    else:
        return f"A soma dos números do CPF ({soma_cpf}) é ÍMPAR."

# Solicitar o CPF do usuário
cpf = input("Digite o CPF no formato 999.999.999-99: ")

# Exibir o resultado
print(verificar_cpf(cpf))
