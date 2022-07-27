import os 
import random

os.system('cls')

# rock-paper-scissors // pedra Papel Tesoura

"""Instruções

 Faça um jogo de pedra, papel e tesoura.

 Dentro do arquivo main.py, você encontrará a arte ASCII para os sinais de mão já salvos em uma variável correspondente: 
 pedra, papel e tesoura.  Isso tornará mais fácil imprimi-los no console.

 Comece o jogo perguntando ao jogador:

 "O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura."

 A partir daí, você precisará descobrir:

     Como você armazenará a entrada do usuário.
     Como você irá gerar uma escolha aleatória para o computador.
     Como você irá comparar a escolha do usuário e do computador para determinar o vencedor (ou um empate).
     E também como você dará feedback ao jogador.

 Você pode encontrar as regras "oficiais" do jogo no site da World Rock Paper Scissors Association.

"""

# Coding // codificação
humano = int(input( "O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n"))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

seqs =  [rock, paper, scissors]

pc = random.choice(seqs)

if (pc == rock) and (humano == 2): # PC = Pedra / HUMANO = Tesoura
    print(f'{pc} >> Pc Jogou Pedra \n\n{seqs[humano]} >> Humano Jogou Tesoura')
    print('\n>> PC vence o jogo :D\n')

elif (humano == 0) and (pc == scissors): # HUMANO = Pedra / PC = Tesoura
    print(f'{pc} >> Pc Jogou Tesoura\n\n{seqs[humano]} >> Humano Jogou Pedra')
    print('\n>> Parabéns humano! Você venceu o jogo \o/\n')

elif (pc == paper) and (humano == 0): # PC -> Papel / HUMANO -> Pedra
    print(f'{pc} >> Pc Jogou Papel\n\n{seqs[humano]} >> Humano Jogou Pedra')
    print('\n>> PC vence o jogo :D\n')

elif (humano == 1) and (pc == rock): # HUMANO = Papel / PC = Pedra
    print(f'{pc} >> Pc Jogou Pedra\n\n{seqs[humano]} >> Humano Jogou Papel')
    print('\n>> Parabéns humano! Você venceu o jogo \o/\n')

elif (pc == scissors) and (humano == 1): # PC -> Tesoura / HUMANO -> Papel
    print(f'{pc} >> Pc Jogou Tesoura \n\n{seqs[humano]} >> Humano Jogou Papel')
    print('\n>> PC vence o jogo :D\n')

elif (humano == 2) and (pc == paper): # HUMANO = Tesoura / PC = Papel
    print(f'{pc} >> Pc Jogou Papel\n\n{seqs[humano]} >> Humano Jogou Tesoura')
    print('\n>> Parabéns humano! Você venceu o jogo \o/\n')
elif (humano < 0) or (humano > 2):
    print('\n>> Ops! Jogada inválida amiguinho(a), tente mais uma vez :D\n')
else:
    jogada_iguais = ''
    if (humano == 0):
        jogada_iguais = 'Pedra'
    elif (humano == 1):
        jogada_iguais = 'Papel'
    elif (jogada_iguais == 2):
        jogada_iguais = 'Tesoura'

    print(f'{pc} >> Pc Jogou {jogada_iguais}\n\n{seqs[humano]} >> Humano Jogou {jogada_iguais}')
    print('\n>> Empatamos o jogo :)\n')
