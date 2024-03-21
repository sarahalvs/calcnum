import math

# definindo f(x)
def f(x):
    return x / math.exp(x) - 0.2 * x**2 + 17

# Método da Secante, pois ele é um método mais fácil de achar as raízes com essa precisão
def secante(f, x0, x1, epsilon, max_iter):
    iteracoes = 0
    while iteracoes < max_iter: #o número de iterações não pode passar do número máximo de iterações
        f_x0 = f(x0)
        f_x1 = f(x1)
        x2 = (x0 * f_x1 - x1 * f_x0) / (f_x1 - f_x0)
        if abs(x2 - x1) < epsilon:
            return x2, iteracoes
        x0, x1 = x1, x2
        iteracoes += 1
    return None, iteracoes

# precisão e iterações
epsilon = 1e-20
max_iter = 1000  #definindo um número max de iterações, p programa não entrar em loop infinito

# determinação dos intervalos
intervalos = [(-3, -2), (9, 10)]

# encontrando as raízes pelo método da secante
for intervalo in intervalos:
    print(f"\nIntervalo: {intervalo}")
    a, b = intervalo

    raiz, iteracoes = secante(f, a, b, epsilon, max_iter)
    if raiz is not None:
        print(f"Raiz encontrada: {raiz}")
        print(f'Número de iterações: {iteracoes}')
    else:
        print("Não foi possível encontrar a raiz com a precisão especificada.")
