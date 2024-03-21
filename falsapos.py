import math

# definindo f(x)
def f(x):
    return x / math.exp(x) - 0.2 * x**2 + 17

# Método da falsa posição, parecido com o da bisseção
def falsa_posicao(a, b, epsilon, max_iter):
    iteracoes = 0
    if f(a) * f(b) > 0: #restrição do método
        print("Não é possível garantir a existência de raízes no intervalo fornecido.")
        return None, iteracoes
    while iteracoes < max_iter:
        xi = (a * abs(f(b)) + b * abs(f(a))) / (abs(f(b)) + abs(f(a)))
        if abs(f(xi)) < epsilon:
            return xi, iteracoes
        elif f(xi) * f(a) < 0:
            b = xi
        else:
            a = xi
        iteracoes += 1
    return None, iteracoes

# Intervalos, precisão e máximo de iterações
intervalos = [(-3, -2), (9, 10)]
epsilon = 1.0e-1
max_iter = 5

# encontrando as raízes de cada intervalo
for intervalo in intervalos:
    print(f"Intervalo: {intervalo}")
    a, b = intervalo
    raiz, iteracoes = falsa_posicao(a, b, epsilon, max_iter)
    if raiz is not None:
        print(f'Raiz encontrada: {raiz}')
        print(f'Número de iterações: {iteracoes}')
    else:
        print("Não foi possível encontrar a raiz com a precisão especificada.")
