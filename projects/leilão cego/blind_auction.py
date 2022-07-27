from os import system
from logo_martelo import logo

system('cls')


# blind-auction // leilão cego

def encontrar_vencedor(var_dick):
    nome_vencedor = ''
    maior_lance = 0
    
    for key in var_dick:
      if var_dick[key] >= maior_lance:
        nome_vencedor = key
        maior_lance = var_dick[key]

    system('cls')
    print(f'\n>> The winner is {nome_vencedor} with a bid of ${maior_lance:.2f}.\n')
    # O vencedor é xx com um lance de $ xx 


print(logo)
print('Welcome to the secret ouction program.')

loopi = True
dick = {}

while loopi:
  name = input('What is your name?\n').capitalize()
  bid_price = float(input("What's your bid?: \n$"))

  # Adicione Nome e Lance em um dicionário como a chave e o valor.
  dick[name] = bid_price
  
  # Pergunte se há outros usuários que desejam dar lances
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  
  if other_bidders == 'no':      
    loopi = False
    encontrar_vencedor(dick) # Encontre o lance mais alto no dicionário e declare-o como o vencedor
    
  elif other_bidders == 'yes':
    system('cls')


