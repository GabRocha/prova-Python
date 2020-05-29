#Exercicio 01
def fatorial(fator):                                    #Criando função do vetorial
    listanum = range(1, fator)                          #lista de numeros para fazer o calculo do vetor


    if fator == 0:                                      #if caso o usuario digite 0 e o fatorial de 0 é 1!
       return 1                                         #retorna 1

    else:                                               #else para fazer o calculo do veto
        for num in listanum:
            fator *= num                                #Calculo do fatorial

        return fator                                    #retorna o valor do calculo

def checarnegativo(positivo):                           #Criando a funação para fazer checagem se o numero digitado e positivo ou negatico
    if num1 < 0:
        print("Digite apenas numeros positivos!!!!")    #quando o numero e negativo retorna essa mensagem

    else:                                               #caso seja positivo chama a função fatorial para calcular o vetor
        print("O fatorial de {}! = {}".format(num1, fatorial(num1)))

num1 = int(input("Digite um numero para descobrir se fatorial: ")) #varialvel que quardo o valor do numero digitado pelo usuario
checarnegativo(num1)                                    #chama a função que checa se o numero é negativo ou positivo