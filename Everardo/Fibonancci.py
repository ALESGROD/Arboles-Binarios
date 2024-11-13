import matplotlib.pyplot as plt

def fibonacci(n):
    """
    Calcula los primeros n números de la secuencia de Fibonacci.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence

def graficar_fibonacci(n):
    """
    Calcula, imprime y grafica los primeros n números de la secuencia de Fibonacci.
    """
    fib_sequence = fibonacci(n)
    
    # Imprime los números de Fibonacci
    print(f"Los primeros {n} números de Fibonacci son: {fib_sequence}")
    
    # Grafica los números de Fibonacci
    plt.figure(figsize=(10, 6))
    plt.plot(fib_sequence, marker='o', color='b', linestyle='-', markersize=5)
    plt.title(f'Secuencia de Fibonacci - primeros {n} números')
    plt.xlabel('Índice')
    plt.ylabel('Valor de Fibonacci')
    plt.grid(True)
    plt.show()

# Ejemplo de uso
n = int(input("Ingrese la cantidad de números de Fibonacci que desea calcular: "))
graficar_fibonacci(n)