# import getpass
# senha=getpass.getpass('senha: ')
# print(senha)


def validar_senha(senha):

    # Falha 1: Não verifica se a senha é vazia
    if len(senha) == 0:
        return "A senha não pode ser vazia."

    # Falha 2: Permite senhas com apenas caracteres repetidos
    if len(set(senha)) == 1:
        return "A senha não pode conter apenas um único caractere repetido."

    # Falha 3: Verifica se a senha tem pelo menos 8 caracteres, mas não verifica se é uma sequência
    if len(senha) < 8:
        return "A senha deve ter pelo menos 8 caracteres."

    # Falha 4: Verifica se há pelo menos um número, mas não garante que não seja uma sequência
    if not any(char.isdigit() for char in senha):
        return "A senha deve conter pelo menos um número."

    # Falha 5: Verifica se há pelo menos uma letra minúscula e uma maiúscula, mas não garante que não sejam sequenciais
    if not any(char.islower() for char in senha) or not any(char.isupper() for char in senha):
        return "A senha deve conter pelo menos uma letra minúscula e uma letra maiúscula."

    # Falha 6: Não verifica se a senha contém caracteres especiais
    if not any(char in "!@#$%^&*()-_+=<>?" for char in senha):
        return "A senha deve conter pelo menos um caractere especial."

    # Falha 7: Não verifica se a senha contém sequências de caracteres (ex: "1234", "abcd")
    for i in range(len(senha) - 3):
        if senha[i:i+4].isdigit() or senha[i:i+4].isalpha():
            return "A senha não pode conter sequências de caracteres."

    return "Senha válida!"

senha = input("Digite a senha para validação: ")
resultado = validar_senha(senha)
print(resultado)
