#Exercico 03
def mascara(doc):               #Função que retira ou coloca a mascara
    if forma == "a":            #Estrutura para colocar a mascara no RG
        print("RG: {}.{}.{}-{}".format(doc[0:2], doc[2:5], doc[5:8], doc[8])) #Retorna o RG com a mascara

    elif forma == "b":          #Estrutura para retirar a mascara
        list = ('.', ',', '-')  #lista com a pontuação há se retirada
        for pont in list:       #Vai checar a variavel e o replace vai substituir a pontuação por espaço vazio
            doc = doc.replace(pont, '')
        print("RG: ",doc)              #retor o rg sem a mascara

    else:                       #Caso o usuario não escolha uma das opções
        print("Escolha a opção A ou B")


                                #Pergunta ao usuario e guarda qual será a ação
forma = input("Escolha uma das opções a seguir para continuar.\nA. Para adicioanr mascara ao RG \nB. Para remover mascara do RG\nDigite aqui: ")
forma = forma.lower()           #Deixa o caracteries em minusculo caso o usuario digite em maiusculo
rg = input("Digite o numero do seu RG: ")#Usuario informa o RG

mascara(rg)                     #Chama a função



