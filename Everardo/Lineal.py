import matplotlib.pyplot as plt

def fibonacci_iterativa(n):
    """
    Calcula los primeros n números de Fibonacci de forma iterativa.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        # Calcula el siguiente número como la suma de los dos anteriores
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence

def graficar_fibonacci_iterativa_log(n):
    """
    Calcula y grafica los primeros n números de Fibonacci de forma iterativa
    usando una escala logarítmica en el eje y para una apariencia diagonal.
    """
    # Calcula los primeros n números de Fibonacci de forma iterativa
    fibonacci_sequence = fibonacci_iterativa(n)
    
    # Imprime la secuencia calculada
    print(f"Los primeros {n} números de Fibonacci (iterativa) son: {fibonacci_sequence}")
    
    # Graficar la secuencia de Fibonacci con escala logarítmica en el eje y
    plt.figure(figsize=(10, 6))
    plt.plot(range(n), fibonacci_sequence, marker='o', color='b', linestyle='-', markersize=5)
    plt.yscale('log')  # Usar escala logarítmica en el eje y
    plt.title(f'Secuencia de Fibonacci (Iterativa) - primeros {n} números (Escala Logarítmica)')
    plt.xlabel('Índice')
    plt.ylabel('Valor de Fibonacci (escala log)')
    plt.grid(True, which="both", linestyle='--', linewidth=0.5)
    plt.show()

# Ejemplo de uso
n = int(input("Ingrese la cantidad de números de Fibonacci que desea calcular: "))
graficar_fibonacci_iterativa_log(n)