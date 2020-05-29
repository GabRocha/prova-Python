def calculo(numA, numB):    #Função que seleciona a opção digitada pelo usuario e faz a operação
    if opcao == 1:          #Caso o usuario escolha a opção de somar
        print("Você selecionou a opção somar\n"
              "Resultado {} + {} = {}".format(numA, numB, numA + numB))

    elif opcao == 2:        #Caso o usuario escolha a opção de subtrair
        print("Você selecionou a opção Subtrair\n"
              "Resultado {} - {} = {}".format(numA, numB, numA - numB))

    elif opcao == 3:        #Caso o usuario escolha a opção de multiplicar
        print("Você selecionou a opção Subtrair\n"
              "Resultado {} x {} = {}".format(numA, numB, numA * numB))

    elif opcao == 4:        #Caso o usuario escolha a opção de divisão
        if numB == 0:       #Caso o usuario tente dividir por zero
            print("Não existe divisão por 0 \"Zero\","
                  " por favor insira outro numero!")

        else:               #Se nao ele faz a conta normal
            print("Você selecionou a opção divisão\n"
                  "Resultado {} / {} = {}".format(numA, numB, numA / numB))



while True:                 #Estrutura de repetição para o usuario fazer quantas contas ele quiser
    #num1 = float(input("Digite o primeiro numero: "))   #Recebe o primeiro numero
    #num2 = float(input("Digite o segundo numero: "))    #Recebe o sugundo numero
    #Coloquei para receber os numeros dentro do else,pois caso o usuario deseje sair,
    # ele nao tem que digitar o numero é só selecianar a opção sair(5)
    opcao = int(input("Calculando\n Selecione uma das opções para seguir\n"
                          "1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão\n5- Sair\n"
                          "Didite aqui: ")) #Recebe a opção que o usuario deseja ou sair
    if opcao == 5:
        break

    elif 0 > opcao > 5:     #
        print("Escolha uma das opções!!!")

    else:
        num1 = float(input("Digite o primeiro numero: "))  # Recebe o primeiro numero
        num2 = float(input("Digite o segundo numero: "))  # Recebe o sugundo numero
        calculo(num1, num2)



