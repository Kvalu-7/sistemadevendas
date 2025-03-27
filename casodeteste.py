#pagina de login

def classificar_cpf(possiveis_ent):
    if len(possiveis_ent[0])==11 and [numero[8] for numero in possiveis_ent] == "6":
        return "CPF válido"
    elif len(possiveis_ent[0])==11 and [numero[8] for numero in possiveis_ent] != "6":
        return "CPF não é do estado de MG"
    elif len(possiveis_ent)!=11:
        return"ERRO!Quantidade de números insuficientes"

possiveis=["12344577632","3215556667","33344422266"]


for ent in possiveis:
    print(ent,classificar_cpf(ent))