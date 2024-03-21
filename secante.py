import math

# definição de f(x)
def f(x):
    return x / math.exp(x) - 0.2 * x**2 + 17

# Método secante com o quociente
def secante_quociente(f, x0, x1, epsilon, max_iter):
    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        x2 = (x0 * f_x1 - x1 * f_x0) / (f_x1 - f_x0)
        if abs(x2 - x1) < epsilon:
            return x2
        x0 = x1
        x1 = x2
    return None

# Intervalos, precisão e iteração
intervalos = [(-3, -2), (9, 10)]
epsilon = 1e-14
max_iter = 1000

# Iterações para cada intervalo
for intervalo in intervalos:
    print(f"Iterações para o intervalo {intervalo}:")
    raiz_encontrada = secante_quociente(f, intervalo[0], intervalo[1], epsilon, max_iter)
    if raiz_encontrada is not None:
        print(f"Raiz encontrada: {raiz_encontrada}")
    else:
        print("Não foi possível encontrar a raiz com a precisão especificada.")
