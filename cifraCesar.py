#Cifra de César: O programa a seguir é capaz de criptografar ou decriptografar uma determinada frase
#por meio de uma chave (inteiro) qualquer que o usuário digitar. Funciona para frases com espaços, mas sem 
#caracteres de acentuação, pontuação, números ou outros tipos de carcteres especiais.

print("Este é o software da Cifra de César!")

status = "" #string chamada no final do programa

while (status != "Sair"): #o programa continua rodando até que no final o usuário digite "Sair"
    print("\n")

#as variáveis a seguir armazenam os atributos utilizados nas operações e comparações
    operacao = 0
    direcao = 0
    while operacao!=1 and operacao!=2:
        operacao = int(input("Digite (1)Criptografar e (2)Decriptografar uma frase: "))

        if operacao==1:
            operacao_frase='Criptografar'
        elif operacao==2:
            operacao_frase='Decriptografar'

        frase = input(f"Digite a frase sobre a qual a operação {operacao_frase} será aplicada: ")
        chave = int(input(f"Digite a chave para {operacao_frase}: "))
        fraseAlterada = [] #armazena a string final com o método escolhido aplicado
        
        for letra in frase: #percorre a frase sobre a qual a operação será realizada

            asc2 = ord(letra)

            if ((asc2 >= 65 and asc2 <= 90) or (asc2 >= 97 and asc2 <= 122)): 
                if (operacao == 1): 
                    asc2 += chave
                    if(asc2 >= 122):
                        asc2 = 96 + asc2 - 122 
                elif (operacao == 2): 
                    asc2 -= chave
                    if(asc2 <= 65):
                        asc2 = 91 - (65 - asc2) 
                    if(asc2 <= 97 ):
                        asc2 = 123 - (97 - asc2)   
            print(asc2)       
            fraseAlterada.append(chr(asc2))
        fraseFeita = "".join(fraseAlterada)
    print (f"A frase com o método {operacao_frase} fica: {fraseFeita}")

    #verfifica se o usuário quer realizar outra operação. Se sim, repete todo este bloco, se não, fecha o app
    status = input ("Deseja realizar outra operação? Digite 'Sair' para fechar o aplicativo ou 'Continuar' para fazer outra operação. ")
    if (status == "Sair"): print("Fechando app...")
