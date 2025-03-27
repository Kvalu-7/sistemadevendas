#atividade 1: Teste de idade inválida 

# def teste_idade_invalida(): 

#     idade = -5 

      
#     if idade < 0: 

#         return "Idade inválida" 

#     else: 

#         return "Idade válida" 
# assert teste_idade_invalida()=="Idade válida", "teste falhou,pq a idade é menor que zero"

#atividade 2: Teste de saldo insuficiente 

#Python 

# def teste_saldo_insuficiente(): 

#     saldo = 100 

#     saque = 150 

     

#     if saque > saldo: 

#         return "Saldo insuficiente" 

#     else: 

#         return "Saque realizado" 

# assert teste_saldo_insuficiente() == "Saldo realizado",'Seu saldo é inferior ao valor que você deseja sacar'       

# #atividade 3: Teste de email inválido 

# #Python 

# def teste_email_invalido(): 

#     email = "usuarioatividade.com" 

     

#     if "@" not in email: 

#         return "Email inv# álido" 

#     else: 

#         return "Email válido" 
# assert teste_email_invalido()=='Email válido','Erro de formatação de email'

#atividade 4: Teste de CPF inválido 

#Python 

# def teste_cpf_invalido(): 

#     cpf = "12345678900" 

     

#     if len(cpf) != 11: 

#         return "CPF inválido" 

#     else: 

#         return "CPF válido" 
# assert teste_cpf_invalido()=='CPF válido','Caracteres insuficientes'

#atividade 5: Teste de quantidade negativa 

# #Python 

# def teste_quantidade_negativa(): 

#     quantidade = -10 

     

#     if quantidade < 0: 

#         return "Quantidade inválida" 

#     else: 

#         return "Quantidade válida" 
# assert teste_quantidade_negativa()=='Quantidade válida','Erro!Número menor que zero'

# #atividade 6: Teste de nome vazio 

# #Python 

# def teste_nome_vazio(): 

#     nome = "" 

     

#     if not nome: 

#         return "Nome obrigatório" 

#     else: 

#         return "Nome válido" 
# assert teste_nome_vazio()=='Nome válido','Acesso negado!Área do nome vazio'

# #atividade 7: Teste de formato de telefone inválido 

# #Python 

# def teste_formato_telefone_invalido(): 

#     telefone = "12345" 

     

#     if len(telefone) != 10: 

#         return "Formato de telefone inválido" 

#     else: 

#         return "Telefone válido" 
# assert teste_formato_telefone_invalido()=='Telefone válido','Quantidade de dígitos insuficiente'

# # atividade 8: Teste de produto indisponível 

# Python 

# def teste_produto_indisponivel(): 

#     estoque_produto = 0 

     

#     if estoque_produto == 0: 

#         return "Produto indisponível" 

#     else: 

#         return "Produto disponível" 
# assert teste_produto_indisponivel()=='Produto disponível','não há produto em estoque'

# atividade 9: Teste de senha muito curta 

# Python 

# def teste_senha_muito_curta(): 

#     senha = "123" 

     

#     if len(senha) < 6: 

#         return "Senha muito curta" 

#     else: 

#         return "Senha válida" 
# assert teste_senha_muito_curta()=='Senha válida', 'ERRO!Quantidade de digitos insufientes'

# atividade 10: Teste de valor de desconto inválido 

# Python 

# def teste_desconto_invalido(): 

#     desconto = -10 

     

#     if desconto < 0 or desconto > 100: 

#         return "Desconto inválido" 

#     else: 

#         return "Desconto aplicado" 

# assert teste_desconto_invalido()=='Desconto aplicado','Erro na leitura do valor de desconto'