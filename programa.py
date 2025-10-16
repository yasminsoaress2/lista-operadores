#Lista de Exercícios - Operadores 
#Nome: Yasmin Soares

#Questão 1:
#Fazer um programa que solicite ao usuário dois números e mostre todos os resultados de possíveis de operações relacionais entre eles.
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print("Comparando a com b")
print("O valor da avaliação da expressão", a, ">", b, "é", a > b)
print("O valor da avaliação da expressão", a, "<", b, "é", a < b)
print("O valor da avaliação da expressão", a, ">=", b, "é", a >= b)
print("O valor da avaliação da expressão", a, "<=", b, "é", a <= b)
print("O valor da avaliação da expressão", a, "==", b, "é", a == b)
print("O valor da avaliação da expressão", a, "!=", b, "é", a != b)

print("Comparando b com a")
print("O valor da avaliação da expressão", b, ">", a, "é", b > a)
print("O valor da avaliação da expressão", b, "<", a, "é", b < a)
print("O valor da avaliação da expressão", b, ">=", a, "é", b >= a)
print("O valor da avaliação da expressão", b, "<=", a, "é", b <= a)
print("O valor da avaliação da expressão", b, "==", a, "é", b == a)
print("O valor da avaliação da expressão", b, "!=", a, "é", b != a)

#Questão 2:
#Um programa que faça o mesmo que o programa anterior, mas agora solicitando strings ao usuário
a = input("Digite a primeira palavra: ")
b = input("Digite a segunda palavra: ")

print("Comparando a com b")
print("O valor da avaliação da expressão", a, ">", b, "é", a > b)
print("O valor da avaliação da expressão", a, "<", b, "é", a < b)
print("O valor da avaliação da expressão", a, ">=", b, "é", a >= b)
print("O valor da avaliação da expressão", a, "<=", b, "é", a <= b)
print("O valor da avaliação da expressão", a, "==", b, "é", a == b)
print("O valor da avaliação da expressão", a, "!=", b, "é", a != b)

print("Comparando b com a")
print("O valor da avaliação da expressão", b, ">", a, "é", b > a)
print("O valor da avaliação da expressão", b, "<", a, "é", b < a)
print("O valor da avaliação da expressão", b, ">=", a, "é", b >= a)
print("O valor da avaliação da expressão", b, "<=", a, "é", b <= a)
print("O valor da avaliação da expressão", b, "==", a, "é", b == a)
print("O valor da avaliação da expressão", b, "!=", a, "é", b != a)

#Questão 3:
#Calcula o salário mínimo do usuário
salario_minimo = float(input("Digite o valor do salário mínimo: "))
salario_pessoa = float(input("Digite o valor do seu salário: "))

quantidade = salario_pessoa / salario_minimo
print("Você ganha", quantidade, "salários mínimos.")

#Questão 4:
#Algoritmo em python que calcula o peso, em gramas e pede um para calcular se a pessoa aumentar o peso em 12%
peso_kg = float(input("Digite seu peso em kg: "))

#Converte o peso para gramas
peso_gramas = peso_kg * 1000

#Com o aumento de 12%
novo_peso_gramas = peso_gramas + (peso_gramas * 0.12)

print("Seu peso em gramas é:", peso_gramas)
print("Se você engordar 12%, seu novo peso em gramas será:", novo_peso_gramas)

#Questão 5:
#Uma tabela com os valores resultantes de avaliação do operador AND para cada uma das combinações de valores dados
#Obs: Ao invés de fazer na tabela resolvi testar aqui no python mesmo 
print(False and False)
print(False and True)
print(True and False)
print(True and True)

#Questão 6:
#Um um programa que mostra o resultado do AND na tela para todas as combinações de valores vistas na questão anterior
print("O resultado da operação False and False é", False and False)
print("O resultado da operação False and True é", False and True)
print("O resultado da operação True and False é", True and False)
print("O resultado da operação True and True é", True and True)

#Questão 7:
#A questão pede em que ordem a expressão w = x * y < z / x or x / y > z * x and z * y < x seria avaliada pelo python
#Aí seguindo as regras de prioridade primeiro ele iria resolver as contas que aparecem (* e /)
#Depois ele iria fazer as comparações (<,>,==) para saber quais partes são verdadeiras e falsas
#Então em seguida iria resolver o and porque ele exige que as duas partes sejam verdadeiras
#E por último resolveria o or para que uma das partes seja verdadeira para ser true 
w = (x * y < z / x) or ((x / y > z * x) and (z * y < x)) #exemplo de como o python lê essa expressão

#Questão 8:
#Pede um programa que receba os valores de x, y e z e que mostre o resultado da expressão anterior
x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))
z = float(input("Digite o valor de z: "))

w = (x * y < z / x) or ((x / y > z * x) and (z * y < x))
print("O resultado da expressão é:", w)
