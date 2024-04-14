import math

# definindo f(x)
def f(x):
    return x / math.exp(x) - 0.2 * x**2 + 17

# Método da bisseção
def bissecao(a, b, epsilon, max_iter):
    iteracoes = 0
    if f(a) * f(b) > 0:
        print("Não é possível garantir a existência de raízes no intervalo fornecido.")
        return None, iteracoes
    while (b - a) > epsilon and iteracoes < max_iter: #restrição do método + restrição p programa rodar
        c = (a + b) / 2
        if f(c) == 0:
            return c, iteracoes
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteracoes += 1
    return (a + b) / 2, iteracoes

# Determinando os intervalos, precisões e máximo de iteração
intervalos = [(-3, -2), (9, 10)]
epsilon = 1.0e-20
max_iter = 67

# encontrando as raízes em cada intervalo
for intervalo in intervalos:
    print(f"Intervalo: {intervalo}")
    a, b = intervalo
    raiz, iteracoes = bissecao(a, b, epsilon, max_iter)
    if raiz is not None:
        print(f"Raiz encontrada: {raiz} - Número de iterações: {iteracoes}")
    else:
        print("Não foi possível encontrar a raiz com a precisão especificada.")
