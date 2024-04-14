import math

# definição de f(x)
def f(x):
    return x / math.exp(x) - 0.2 * x**2 + 17

# Método secante com o quociente de definição
def secante(f, x0, x1, epsilon, max_iter):
    iteracoes = 0
    while iteracoes < max_iter:
        f_x0 = f(x0)
        f_x1 = f(x1)
        x2 = (x0 * f_x1 - x1 * f_x0) / (f_x1 - f_x0)
        if abs(x2 - x1) < epsilon:
            return x2, iteracoes
        x0 = x1
        x1 = x2
        iteracoes += 1
    return None, iteracoes

# Intervalos, precisão e iteração
intervalos = [(-3, -2), (9, 10)]
epsilon = 1.0e-20
max_iter = 67

# Iterações para cada intervalo
for intervalo in intervalos:
    print(f"Iterações para o intervalo {intervalo}:")
    raiz, iteracoes = secante(f, intervalo[0], intervalo[1], epsilon, max_iter)
    if raiz is not None:
        print(f"Raiz encontrada: {raiz}")
        print(f'Número de iterações: {iteracoes}')
    else:
        print("Não foi possível encontrar a raiz com a precisão especificada.")
