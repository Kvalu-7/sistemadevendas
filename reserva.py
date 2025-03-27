# parte1:login
# parte2:coleta de dados do cliente
# parte3:reserva da viagem
# parte4:pagamento
# parte5:nota fiscal

import os


#     LOGIN

loginEm = 'SENAC'
senhaEm = 'SENAC'
# loginM = "ROOT"
# senhaM = "ROOT"
tent = 0
validador = 0


#listas

entradadia=[]
saidadia=[]
horaentrada=[]
horasaida=[]
produtos={
    '1.Solteiro simples':200.00,
    '2.Solteiro simples,com café,almoço e jantar incluso':480.00,
    '3.solteiro suite, all inclusiv':590.00,
    '4.casal simples':380.00,
    '5.casal simples,com café,almoço e jantar incluso-':680.00,
    '6.casal suite, all inclusiv':980.00,
}
nomeres=[]
contato=[]
cpf=[]
valor=[]
dias=[]
totval=[]

def cabecalho():
    linha()
    print('                         -INHOUSE-')
    linha()

def espacoduplo():
    print('\n'*2)

def espacosimples():
    print('')

def linha():
    print(20*'===')

def linhasp():
    print('=======================')

def limpatela():
    os.system('cls')

def fimt():
    print('\n'*10)

def produt():
    cabecalho()
    for item in produtos:
        print(item, '  R$ ',produtos[item])
    print('\n')




#def quarto():
        # print(' 1.Solteiro simples,sem café,almoço e jantar incluso-  R$00,00 ')
        # print(' 2.Solteiro simples,com café,almoço e jantar incluso-  R$00,00')
        # print(' 3.solteiro suite, all inclusiv-  R$00,00')
        # print(' 4.casal simples,sem café,almoço e jantar incluso-  R$00,00')
        # print(' 5.casal simples,com café,almoço e jantar incluso-  R$00,00')
        # print(' 6.casal suite, all inclusiv-  R$00,00')    


# parte3: reserva da viagem
def voltar():
    pass


def logar():
    tent=1
    validador=0
    while validador < 6:
        import os
        os.system('cls')
        print(' \n '*3)
        tent
        cabecalho()
        linha()
        print('OBSERVAÇOES')
        linhasp()
        print('               ENTRE EM CONTATO PARA REGISTRAS-SE ')
        print('                   CONOSCO. (88) 9 8596-4587')
        linha()
        print(" TENTATIVAS FALHAS: ",tent)
        linha()
        print(' '*5,'| LOGIN |')
        linha()
        logEn=str(input('ACESSE SEU LOGIN:  ')).upper()
        linha()
        senEn=str(input('ACESSE SUA SENHA:  ')).upper()
        linha()

           #  validar
        if loginEm == logEn and senhaEm == senEn: 
            usuario()
            #reserva()
            quarto()
            comanda_final()
            #logar()
            break
            
        # else:
        #     tent = tent + 1

        # if tent==3:
        #         import os
        #         os.system('cls')
        #         linha()
        #         print('     ACESSO NEGADO!!    ')
        #         linha()
        #         if loginEm != logEn:
        #             print('    MOTIVO (1) LOGIN INCORRETO!!    ')
        #             linha()
        #         if senhaEm != senEn:
        #             print('    MOTIVO (2) SENHA INCORRETA!!    ')
        #             linha()
        #             print("\n" * 6)
        #             print("         TENTAR NOVAMENTE??   ")
        #             new=str(input("  ")).lower()
        #             if new =="sim":
        #                 logar()
        #             else:
        #                logar()
    


def cabviagem():
    limpatela()
    linha()
    cabecalho()
    linha()
    print(18*' ','---DADOS DA VIAGEM---')
    linha()

def reserva():
    cabviagem()
    print('   SELECIONE A DATA ')
    linhasp()
    espacosimples()
    print('-CHECK IN-')
    print('   *DATA DE ENTRADA:' )
    entradadia.append(str(input('')))
    print('   *HORA DE ENTRADA:' )
    horaentrada.append(str(input('')))
    linhasp()
    espacosimples()
    print('   *DATA DE SAIDA:' )
    saidadia.append(str(input('')))
    espacosimples()
    print('   *HORA DE SAIDA:' )
    horasaida.append(str(input('')))
    espacosimples()




    # fimt()
    # linha()
    # print('ENTRADA:')
    # print(entradadia,horaentrada)
    # linhasp()
    # print('SAIDA:')
    # print(saidadia,horasaida)
    # linhasp()

def quarto():
    cabviagem()
    print('   ---SELECIONE O QUARTO--- ')
    linhasp()
    espacosimples()
    print('-COMBOS-')
    produt()
    linhasp()
    print('DIGITE O VALOR DO PACOTE ESCOLHIDO: ')
    valores=float(input('   '))
    valor.append(valores)
    print('DIGITE A QUANTIDADE DE DIAS: ')
    diasu=float(input('   '))
    dias.append(diasu)
    total=valores*diasu
    totval.append(total)
    linha()
    print("   SUA ESTADIA FICARA EM:")
    print('   ',totval)
    linha()
    fimt()






def usuario():
    cabviagem()
    print('   DADOS DO HOSPEDE:')
    linhasp()
    espacosimples()
    print('DADOS')
    print('   NOME DO RESPONSAVEL:' )
    nome=str(input('   '))
    nomeres.append(nome)
    print('   CONTATO:' )
    cont=str(input('   '))
    contato.append(cont)
    #linhasp()
    #espacosimples()
    print('   CPF:' )
    cpfr=str(input('   '))
    cpf.append(cpfr)
    #espacosimples()
    # print('   *HORA DE SAIDA:' )
    # horasaida=str(input(''))
    espacosimples()


def comanda_final():
    os.system('cls')
    print("     --- COMANDA ---   ")
    cabecalho()
    print('   RESERVA SELECIONADA: ')
    linha()
    print('IDENTIFICAÇÃO:  ',nomeres)
    print('CONTATO:  ',contato)
    print('CPF:  ',cpf)
    linha()
    linha()
    print('VALOR FINAL:')
    linha()
    print('QUANTIDADE DE DIAS:')
    print('      DIAS: ',dias)
    linhasp()
    print('VALOR DO QUARTO:')
    print('      R$: ',valor)
    linha()
    print('VALOR FINAL:') 
    print('      R$: ',totval)
    linha()
    
    


    fimt()
 





logar()

