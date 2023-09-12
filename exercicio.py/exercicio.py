while True:
    nome = input ('Digite seu nome: ')
    
    # Verificando Se o Usuario Digitou apenas Letras
    if nome.isalpha():
        break
    else:
        print ('Por favor só digite Letras')

# Verificando se o nome tem a quantidade certa de caracter
    if len (nome) >=3: 
      break

    else: 
        print ('Por favor, digite pelo menos 3 letras')

# Verificando se o nome no contem espaço
if ' ' in nome :
    print (f'{nome} tem espaço')

else:
    print (f'{nome} nao tem espaço')





# Verificando a Idade

while True:
 idade = input('Digite sua idade: ')

# Verificando se a idade é um numero
 if idade.isdigit():
    break
 else:
     print ('Por favor digite a idade correta!')
    

# Convertendo a idade para um valor inteiro
idade = int (idade)

# Conferindo se a idade é permitida
if idade <= 17 or idade >= 71 :
     print ('Você nao tem idade para usar esse site')
     exit()

else:
    print (f'Seu nome é {nome} e a Sua idade é {idade} ')


    
 
 

