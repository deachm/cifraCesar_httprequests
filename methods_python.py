from flask import Flask
import requests
import json
import random


def cifra_cesar(mensagem,chave):
    print("Este é o software da Cifra de César!")

    status = "" #string chamada no final do programa

    while (status != "Sair"): #o programa continua rodando até que no final o usuário digite "Sair"
        print("\n")

    #as variáveis a seguir armazenam os atributos utilizados nas operações e comparações
        operacao = 1
        direcao = 'D'
        while operacao!=1 and operacao!=2:
            operacao = 1

        if operacao==1:
                operacao_frase='Criptografar'
        elif operacao==2:
                operacao_frase='Decriptografar'

        frase = mensagem.upper()
        while direcao != 'D' and direcao != 'E':
            direcao = (input(f'digite D para criptografar para a Direita e E para a Esquerda: ')) #a variável direção será usada antes dos ifs de operacao para escolher a direcao da criptografia


        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,'!?\"()#"
        alfabetoMinusculo = "abcdefghijklmnopqrstuvwxyz1234567890.,'!?\"()#"
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
                    while indiceParaTrocar > 45:
                        indiceParaTrocar -= 46

                elif (operacao == 2): 
                    indiceParaTrocar = indiceAlfabeto - chave #subtrai o indice da letra encontrada com a chave
                    #ajusta o indice para que fique um número entre 0 e 25, caso a subtração seja negativa 
                    while indiceParaTrocar < 0:
                        indiceParaTrocar += 46
            
            else:

                if (operacao == 1): 
                    indiceParaTrocar = indiceAlfabeto - chave #subtrai o indice da letra encontrada com a chave
                    #ajusta o indice para que fique um número entre 0 e 25, caso a subtração seja negativa 
                    while indiceParaTrocar < 0:
                        indiceParaTrocar += 46

                if (operacao == 2): 
                    indiceParaTrocar = indiceAlfabeto + chave #soma a chave com o indice da letra encontrada
                    #ajusta o indice para que fique um número entre 0 e 25, caso a soma resulte em um número maior
                    while indiceParaTrocar > 45:
                        indiceParaTrocar -= 46         

            #verifica se a letra é maiuscula ou minuscula e realiza a adição da letra trocada na variavel final
            if (letraMaiuscula): fraseAlterada += alfabeto[indiceParaTrocar]
            else: fraseAlterada += alfabetoMinusculo[indiceParaTrocar] 

        print (f"A frase com o método {operacao_frase} fica: {fraseAlterada}")

        #verfifica se o usuário quer realizar outra operação. Se sim, repete todo este bloco, se não, fecha o app
        status = 'Sair'
        if (status == "Sair"): print("Fechando app...")
        return fraseAlterada


app = Flask(__name__)

#
@app.route("/getCifra", methods=["GET"])
def index():
    chave = random.randint(1,46)
    requisicao = requests.get('https://dog-api.kinduff.com/api/facts')
    cifra = json.loads(requisicao.content)
    cifra_str = cifra['facts']
    print (cifra_str [0])
    cifra_criptografa = cifra_cesar(cifra_str[0],chave)
    return {
        'cifra criptografada': cifra_criptografa, 
        'chave para decriptografar': chave}

    
if __name__=="__main__":
    app.run(debug=True)


