### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite o seu nome: ")

# verificando se o nome do usuario é um erro?
#print(nome_usuario.isdigit)

try:
    nome = input("Digite seu nome: ")

    # Verifica se o nome está vazio
    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio.")
        exit()
    # Verifica se há números no nome
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")
        exit()
    else:
        print("Nome válido:", nome)
except ValueError as e:
    print(e)
    exit()

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

try:
    salario = float(input("Digite seu salario: "))

    if salario < 0:
        print("Digite um valor positivo para salario.")
except ValueError:
    print("Valor invalido para salario. Por favor, digite o valor do seu salario: ")
    exit()
    
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

try:
    valor_bonus = float(input("Digite o valor de seu bonus: "))
    if valor_bonus < 0:
        print("Digite um valor positivo para seu bonus.")
except ValueError:
    print("Valor inválido para o bonus. Por favor, digite seu bonus: ")
    exit()

# 4) Calcule o valor do bônus final
bonus = 1000 + salario * valor_bonus
print(bonus)

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"{nome_usuario}, seu salario atual é R$ {salario:.2f} e seu bonus é de R$ {bonus:.2f}")
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?