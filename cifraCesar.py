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
    while direcao != 'D' and direcao != 'E':
        direcao = (input(f'digite D para criptografar para a Direita e E para a Esquerda: ')) #a variável direção será usada antes dos ifs de operacao para escolher a direcao da criptografia


    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfabetoMinusculo = "abcdefghijklmnopqrstuvwxyz"
    fraseAlterada = "" #armazena a string final com o método escolhido aplicado

    for indice in range (0, len(frase)): #percorre a frase sobre a qual a operação será realizada

        if (frase[indice] == " "): #se encontrar um caractere de espaço, insere-o na variavel final e pula todos os passos após o "continue"
            fraseAlterada += " "
            continue

        indiceAlfabeto = 0 #utilizado para acessar as posições dos alfabetos minusculo e maiusculo

        while (frase[indice] != alfabeto[indiceAlfabeto] and frase[indice] != alfabetoMinusculo[indiceAlfabeto]): #quando encontra a letra da frase correspondente nos alfabetos, a variável indiceAlfabeto armazena sua posição
            indiceAlfabeto += 1

        #verifica se a letra atual da frase é maiuscula ou minuscula
        if (frase[indice] == alfabeto[indiceAlfabeto]): letraMaiuscula = True
        else: letraMaiuscula = False 

        if direcao == 'D':

            #verfifica qual tipo de operação o usuário quer realizar  
            if (operacao == 1): 
                indiceParaTrocar = indiceAlfabeto + chave #soma a chave com o indice da letra encontrada
                #ajusta o indice para que fique um número entre 0 e 25, caso a soma resulte em um número maior
                while indiceParaTrocar > 25:
                    indiceParaTrocar -= 26

            elif (operacao == 2): 
                indiceParaTrocar = indiceAlfabeto - chave #subtrai o indice da letra encontrada com a chave
                #ajusta o indice para que fique um número entre 0 e 25, caso a subtração seja negativa 
                while indiceParaTrocar < 0:
                    indiceParaTrocar += 26
        
        else:

            if (operacao == 1): 
                indiceParaTrocar = indiceAlfabeto - chave #subtrai o indice da letra encontrada com a chave
                #ajusta o indice para que fique um número entre 0 e 25, caso a subtração seja negativa 
                while indiceParaTrocar < 0:
                    indiceParaTrocar += 26 

            if (operacao == 2): 
                indiceParaTrocar = indiceAlfabeto + chave #soma a chave com o indice da letra encontrada
                #ajusta o indice para que fique um número entre 0 e 25, caso a soma resulte em um número maior
                while indiceParaTrocar > 25:
                    indiceParaTrocar -= 26          

        #verifica se a letra é maiuscula ou minuscula e realiza a adição da letra trocada na variavel final
        if (letraMaiuscula): fraseAlterada += alfabeto[indiceParaTrocar]
        else: fraseAlterada += alfabetoMinusculo[indiceParaTrocar] 

    print (f"A frase com o método {operacao_frase} fica: {fraseAlterada}")

    #verfifica se o usuário quer realizar outra operação. Se sim, repete todo este bloco, se não, fecha o app
    status = input ("Deseja realizar outra operação? Digite 'Sair' para fechar o aplicativo ou 'Continuar' para fazer outra operação. ")
    if (status == "Sair"): print("Fechando app...")
