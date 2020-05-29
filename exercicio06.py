def temperatura(celsius):           #função para fazer a conversão de fahrenheit para celsius
    return (celsius - 32)/1.8       #Cálculo


fahre = float(input(("Digite uma temperatura em fahrenheit: ")))    #Recebe a temperatura
tempCelsius = temperatura(fahre)    #Chama a função
print("{}°F = {}°C".format(fahre, round(tempCelsius))) #Mostra na tela a temperatura em fahrenheit depois em celsius
