
Exercício 1:

def eq_seg_grau(a, b, c):
    delta = (b ** 2) - (4 * a * c)

    raiz1 = (-b + (delta) ** 0.5) / (2 * a)
    raiz2 = (-b - (delta) ** 0.5) / (2 * a)
    return raiz1, raiz2 

def ano_bissexto(ano):
    return ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 
-------------------------------------------------------------
-------------------------------------------------------------

Exercício 2:

def calcula_salário(valor_hora, num_hora):
    irpf = 0.275
    valorbruto = valor_hora * num_hora
    salario_liquido = valorbruto * (1 - irpf)
    return salario_liquido
 
