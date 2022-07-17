from ancii_art.logo_calculator import logo
from os import system


system('cls')


def soma(n1, n2):
  return n1 + n2


def subtracao(n1, n2):
  return n1 - n2 


def multiplicacao(n1, n2):
  return n1 * n2 


def divisao(n1, n2):
  return n1 / n2 
  

operadores = {
  '+': soma,
  '-': subtracao,
  '*': multiplicacao,
  '/': divisao
}

# calculator // calculadora 

"""
Obs: Os valores são sempre arredondados para o int mais próximo.
"""

def calculadora(): 
  print(logo)
  first_num = float(str(input("Qual é o primeiro número?: ")).replace(',', '.'))
  for operator in operadores:
    print(operator)

  the_start = True
  
  while the_start:
    you_operator = str(input("Escolha uma operação: "))
    you_operation = operadores[you_operator]

    last_num = float(str(input("Qual é o próximo número?: ").replace(',', '.')))

    result_of_the_operation = you_operation(first_num, last_num) 
 
    print(f"\n{round(first_num)} {you_operator} {round(last_num)} = {round(result_of_the_operation)}\n")
    
    if str(input(f"Digite 'y' para continuar calculando com {round(result_of_the_operation)} ou digite 'n' para iniciar um novo cálculo: " )) == 'y':
      first_num = result_of_the_operation
    
    # it's in an infinite loop // está em loop infinito ^^
    else:
      the_start = False
      system('cls')
      calculadora()


calculadora()















