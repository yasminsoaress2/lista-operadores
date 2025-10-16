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