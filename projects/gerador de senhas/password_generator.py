from os import system
import random

system('cls')

# password-generator // gerador de senhas

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem-vindo ao Gerador de PyPassword!")
nr_letters = int(input("\n> Quantas letras você gostaria na sua senha?\n")) 
nr_symbols = int(input("> Quantos símbolos você gostaria?\n"))
nr_numbers = int(input("> Quantos números você gostaria?\n"))


my_password = new_password = '' 

#Nível Fácil - Ordem não aleatória (Posição Fixa):
#ex. 4 letras, 2 símbolos, 2 números = JduE&!91
for l in range(1, nr_letters + 1):
    my_password += random.choice(letters)

for n in range(1, nr_symbols + 1): 
    my_password += random.choice(symbols)

for n in range(1, nr_numbers + 1):
    my_password += random.choice(numbers)


#Nível Difícil - Ordem dos personagens randomizados:
#ex. 4 letras, 2 símbolos, 2 números = g^2jk8&P
opc = input('\n> Deseja uma senha Difícil? [S/N] S=sim/N=não:\n').upper()

if (opc in 'S'):
    my_password = random.sample(my_password, len(my_password))

    for info in my_password:
        new_password += info

    print('\n-> Aqui está sua senha: '+str(new_password)+'\n')

elif (opc in 'N'):
    print('\nAqui está sua senha -> '+str(my_password)+'\n')

else:
    print('\nOps! Opção inválida, tente mais uma vez.')