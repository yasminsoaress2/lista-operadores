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
#Pede duas palavras  (só que agora strings) ao usuário
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
#É uma questão que pede para calcular quantos salários mínimos a pessoa ganha
salario_minimo = float(input("Digite o valor do salário mínimo: "))
salario_pessoa = float(input("Digite o valor do seu salário: "))

quantidade = salario_pessoa / salario_minimo
print("Você ganha", quantidade, "salários mínimos")


#Questão 4:
#Pede para criar um algoritmo que leia o peso de uma pessoa (em kg) e calcular o peso da pessoa e se ela aumentar seu peso em 12%
peso_kg = float(input("Digite seu peso em kg: "))

#Aqui vai converter o peso para gramas
peso_gramas = peso_kg * 1000

#Calcula o novo peso com o aumento de 12%
novo_peso_gramas = peso_gramas + (peso_gramas * 0.12)

print("Seu peso em gramas é:", peso_gramas)
print("Se você engordar 12%, seu novo peso em gramas será:", novo_peso_gramas)

#Questão 5:
#Completar a tabela com os valores resultantes de avaliação do operador AND para cada uma das combinações de valores
#Obs: Ao invés de fazer a tabela, resolvi testar aqui mesmo os resultados 
print(False and False)
print(False and True)
print(True and False)
print(True and True)

#Questão 6:
#Mostrar o resultado de todas as combinações do operador AND
print("O resultado da operação False and False é", False and False)
print("O resultado da operação False and True é", False and True)
print("O resultado da operação True and False é", True and False)
print("O resultado da operação True and True é", True and True)

#Questão 7:
#Mostrar em como a expressão w = x * y < z / x or x / y > z * x and z * y < x seria avaliada pelo python

#Seguindo as regras de prioridade, primeiro o python iria resolver as contas que aparece (* e /)
#Depois ele faz as comparações (<,>,==) para poder ver as partes que são verdadeiras e falsas
#Em seguida ele vai resolver o AND porque ele exige que as duas partes sejam verdadeiras
#E por último ele vai resolver o or porque precisa que uma das partes seja verdadeira para ser true
w = (x * y < z / x) or ((x / y > z * x) and (z * y < x)) 

#Questão 8:
#Fazer um programa que receba os valores de x, y e z e mostre o resultado da questão anterior
# Programa para calcular a expressão w = x*y < z/x or x/y > z*x and z*y < x

x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))
z = float(input("Digite o valor de z: "))

w = (x * y < z / x) or ((x / y > z * x) and (z * y < x))

print("O resultado da expressão é:", w)

