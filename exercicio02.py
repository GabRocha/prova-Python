#Exercicio 02
def area(ladoa,ladob):                                      #Função que calcula a área
    return ((ladoa*ladob)/2)


print("Calculando a área de um losango")                    #Titulo da progrmação
lado1 = int(input("Digite o tamanho do lado menor: "))      #Recebe o valor do lado menor
lado2 = int(input("Digite o tamamho do lado maior: "))      #recebe o valor do lado maior
print("A área do seu losango é: ", area(lado1, lado2))      #Chama a função e mostra o resultado



