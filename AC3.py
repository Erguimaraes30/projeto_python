def determina_tipo_triangulo(a, b, c):
   
    if (a + b < c) or (a + c < b) or (b + c < a):
        return 'Nao é um triangulo'
    elif (a == b) and (a == c) :
        return 'Equilatero'
    elif (a==b) or (a==c) or (b==c):
        return'Isósceles'
    else:
        return 'Escaleno' 
    
def testa_triangulo():
    print(determina_tipo_triangulo(4,4,4))
    print(determina_tipo_triangulo(2,4,4))
    print(determina_tipo_triangulo(4,3,2))
    print(determina_tipo_triangulo(1,1,4))

testa_triangulo()

print("-" * 30)
print("-" * 30)

def dia_semana(d):
    if d == 1:
        return "Domingo"
    elif d == 2:
        return "Segunda-Feira"
    elif d == 3:
        return "Terça-Feira"
    elif d == 4:
        return "Quarta-Feira"
    elif d == 5:
        return "Quinta-Feira"
    elif d == 6:
        return "Sexta-Feira"
    elif d == 7:
        return "Sábado"
    else:
        return "string vazia"

def teste_semana():
    print(dia_semana(1))
    print(dia_semana(2))
    print(dia_semana(3))
    print(dia_semana(4))
    print(dia_semana(5))
    print(dia_semana(6))
    print(dia_semana(7))
    print(dia_semana(8))

teste_semana()
    
print("-" * 30)
print("-" * 30)

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Dividir por zero não é válido."

def calcular():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (Soma, Subtração, Multiplicação, Divisão): ")

    if operacao == "soma":
        resultado = soma(num1, num2)
    elif operacao == "subtração":
        resultado = subtracao(num1, num2)
    elif operacao == "multiplicação":
        resultado = multiplicacao(num1, num2)
    elif operacao == "divisão":
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida."

    print("Resultado:", resultado)

calcular()

print("-" * 30)
print("-" * 30)
