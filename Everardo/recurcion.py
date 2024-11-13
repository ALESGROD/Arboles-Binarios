import time
import matplotlib.pyplot as plt

# Función recursiva para calcular Fibonacci
def fibonacci_recursivo(n, caminos):
    if n == 0:
        caminos.append((n, 0))
        return 0
    elif n == 1:
        caminos.append((n, 1))
        return 1
    else:
        resultado = fibonacci_recursivo(n-1, caminos) + fibonacci_recursivo(n-2, caminos)
        caminos.append((n, resultado))
        return resultado

# Ingresar el valor de n
n = int(input("Ingresa el número para calcular Fibonacci: "))

# Inicializamos la lista de caminos tomados
caminos = []

# Medir el tiempo de ejecución
start_time = time.time()
resultado_recursivo = fibonacci_recursivo(n, caminos)
end_time = time.time()

print(f"Fibonacci({n}) es {resultado_recursivo}")
for paso in caminos:
    print(f"Fibonacci({paso[0]}) es {paso[1]}")

# Tiempo total de ejecución
tiempo_recursivo = end_time - start_time
print(f"Tiempo total para el método recursivo: {tiempo_recursivo} segundos")

# Gráfica de los caminos tomados
x_vals = [paso[0] for paso in caminos]
y_vals = [paso[1] for paso in caminos]
plt.plot(x_vals, y_vals, marker='o', color='red')
plt.xlabel('Número Fibonacci')
plt.ylabel('Valor calculado')
plt.title('Caminos tomados por la recursión en Fibonacci')
plt.show()

# Gráfica de tiempo de ejecución
plt.bar(['Recursivo'], [tiempo_recursivo], color='green')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title(f'Tiempo de ejecución para Fibonacci({n}) con método recursivo')
plt.show()