import time
import matplotlib.pyplot as plt

# Function to calculate Fibonacci numbers iteratively
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Measure execution time for each input size and plot it
def plot_execution_times_iterative(n):
    times_iterative = []
    for i in range(1, n + 1):
        start_time = time.perf_counter_ns()
        fibonacci_iterative(i)
        end_time = time.perf_counter_ns()
        times_iterative.append(end_time - start_time)

    # Plot
    plt.plot(range(1, n + 1), times_iterative, 'o-', color='b')
    plt.title("Tiempo de ejecución decreciente (Fibonacci Iterativo)")
    plt.xlabel("Tamaño entrada (N)")
    plt.ylabel("Tiempo (ns)")
    plt.yscale('log')  # Escala logarítmica para ver mejor los tiempos si crecen rápido
    plt.grid(True)
    plt.show()

# Main function to ask for user input and plot the graph
def main():
    n = int(input("Ingresa el número de términos de Fibonacci (n): "))
    plot_execution_times_iterative(n)

# Run the main function
if __name__ == "__main__":
    main()
