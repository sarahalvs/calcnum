import math

# f(x) e dps f'(x), pois precisamos derivar pra aplicar o método
def f(x):
    return x / math.exp(x) - 0.2 * x**2 + 17

def df(x):
    return (math.exp(x) - x * math.exp(x) - 0.4 * x * math.exp(2*x)) / math.exp(2*x)

# Método de Newton-Raphson
def newton_raphson(f, df, x0, epsilon, max_iter):
    x = x0
    iteracoes = 0
    for i in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < epsilon:
            return x_new, iteracoes
        x = x_new
        iteracoes += 1
    return None, iteracoes

# Intervalos e precisão
intervalos = [(-3, -2), (9, 10)]
epsilon = 1.0e-20
max_iter = 67

# Iterações para cada intervalo
for intervalo in intervalos:
    print(f"Iterações para o intervalo {intervalo}:")
    raiz_encontrada = None
    for x0 in intervalo:
        raiz, iteracoes = newton_raphson(f, df, x0, epsilon, max_iter) #parâmetros para a func
        if raiz is not None:
            raiz_encontrada = raiz
            break
    if raiz_encontrada is not None:
        print(f"Raiz encontrada: {raiz_encontrada}")
        print(f'Número de iterações: {iteracoes}')
    else:
        print("Não foi possível encontrar a raiz com a precisão especificada.")
