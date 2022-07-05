
# Tip Calculator // Calculadora de gorjetas

"""Instructions
T: Se a conta foi de R$ 150,00, divida entre 5 pessoas, com 12% de gorjeta.

T: Cada pessoa deve pagar (150,00 / 5) * 1,12 = 33,6

T: Formate o resultado com 2 casas decimais = 33,60

T: Assim, a parte de todos na conta total é de $ 30,00 mais uma gorjeta de $ 3,60.

T: Dica: Existem 2 maneiras de arredondar um número.  Você pode ter que fazer alguma pesquisa no Google para resolver isso.💪
"""

"""Example Input
Welcome to the tip calculator!
What was the total bill? $124.56
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7
"""

"""Example Output
Each person should pay: $19.93
"""

# Coding // codificação
conta = float(input("What was the total bill? $"))
gorjeta = int(input("How much tip would you like to give? 10, 12, or 15? "))
qtd_pessoas = int(input("How many people to split the bill?"))

result = (gorjeta / 100 * conta + conta) / qtd_pessoas 

print(f"Each person should pay: ${result:.2f}")

