import os
os.system("cls")

def linha():
    print("__"*40)

def ml():
    print("=="*40)

def f_pag():
    print("Qual seria a forma de pagamento?")
    print(" Pix \n Dinheiro \n Cartão")

def cartão():  
    return " Débito \n ou \n Crédito"

def msg_final():
    print("\nPedido efetuado com sucesso!")
    print("Agradecemos pela sua preferência!")


produtos={
    "Alcatra":30.99,
    "Acém":19.50,
    "Contrafilé":37.98,
    "Picanha":70.10,
    "Carne moida":17.99
}
ml()
ml()
print("                OLÁ! \n BEM-VINDO A LOJA VIRTUAL DO AÇOUGUE VITÓRIA")
ml()
ml()
print(" Segue abaixo nossas ofertas do dia:")
ml()
for item in produtos:
    print(f"{item}:R${produtos[item]}")

total=0

while True:
    
    linha()
    pedido=str(input("Adicione seu(s) pedido(s) ou digite 'sair' para finalizar compra: ")).capitalize()
    linha()
    if pedido=="Sair":
        ml()
        print(f"O valor total da sua compra  foi de: R$ {total:.2f}")
        ml()
        break

    elif pedido in produtos:
        total+=produtos[pedido]
        print(f"O valor da sua compra até o momento corresponde a R$ {total:.2f}")    

    else:
        print("Item não encontrado")    

ml()
f_pag()
ml()

print("Forma de pagamento: ")
pagamento=str(input('  ')).capitalize()

if pagamento=="Pix":
    print("CHAVE: 154789526")
    ml()
    msg_final()
    ml()
elif pagamento=="Dinheiro":
    print("OK")
    ml()
    msg_final()
    ml()
elif pagamento=="Cartão":
    print(cartão())
    tipopag_cartao=str(input("\n ")).capitalize()
    ml()
    msg_final()
    ml()


