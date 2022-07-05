import os

os.system('cls')

""""Instruções
Faça seu próprio jogo "Escolha sua própria aventura". 
Use condicionais como if, else, e elifdeclarações para estabelecer a lógica e o caminho da história em seu programa. 
"""


# Coding // codificação
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Bem-vindo à Ilha do Tesouro.")
print("Sua missão é encontrar o tesouro.\n")

opc = str(input('Você está em uma encruzilhada. Onde você quer ir?  Digite "esquerda" ou "direita".\n>> ')).lower()

if opc != 'esquerda':
    os.system('cls')
    print('\nVocê caiu em um buraco. Fim de jogo. :D\n')
else:
    opc = str(input('\nVocê veio a um lago. Há uma ilha no meio do lago. Digite "esperar" para esperar por um barco. Digite "nadar" para nadar.\n>> ')).lower()
    if opc != 'esperar':
        os.system('cls')
        print('\nVocê tá sendo atacado(a) pelo Ex-empresário do Luva de Pedreiro. Fim de jogo.\n')
    else:
        os.system('cls')
        opc = str(input('\nVocê chega ileso à ilha. Há uma casa com 3 portas. Uma vermelha, uma amarela e uma azul. Qual cor você escolhe? \n>> '))
        os.system('cls')
        if opc == 'vermelha':
            print("""                /^._
  ,___,--~~~~--' /'~
  `~--~\ )___,)/'    Te peguei!
      (/\\_  (/\\_""")
            print('\nVocê está sendo comido(a) por lobo-cinzento. Fim de jogo.\n')

        elif opc == 'azul':
            os.system('cls')
            print("""\n    ,.   (   .      )        .      "
   ("     )  )'     ,'        )  . (`     '`
 .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
 _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '""")
            print('\nVocê está sendo queimado(a) pelo fogo do Meteoro que acabou de cair :D. Fim de jogo\n')
            
        elif opc == 'amarela':
            os.system('cls')
            print("""                                                     ..::''''::..
                                           .:::.   .;''        ``;.
   ....                                    :::::  ::    ::  ::    ::
 ,;' .;:                ()  ..:            `:::' ::     ::  ::     ::
 ::.      ..:,:;.,:;.    .   ::   .::::.    `:'  :: .:' ::  :: `:. ::
  '''::,   ::  ::  ::  `::   ::  ;:   .::    :   ::  :          :  ::
,:';  ::;  ::  ::  ::   ::   ::  ::,::''.    .    :: `:.      .:' ::
`:,,,,;;' ,;; ,;;, ;;, ,;;, ,;;, `:,,,,:'   :;:    `;..``::::''..;'
                                                     ``::,,,,::''

""")
            print('\nParabéns! Você venceu o jogo.  \o/\n')
            print('\nNa história, nosso luvinha sempre sairá vencedor, você também por chegar até aqui. ^=^\n')
