# Recursive approach with step count
def fibonacci_recursive(n, steps=None):
    if steps is None:
        steps = [0]  # Initialize step counter as a list to allow mutation
    
    steps[0] += 1  # Increment step count with each call
    
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1, steps) + fibonacci_recursive(n - 2, steps)

# Iterative approach with step count
def fibonacci_iterative(n):
    steps = 0  # Step counter
    a, b = 0, 1
    
    for _ in range(n):
        steps += 1  # Increment step count for each loop iteration
        a, b = b, a + b
    
    return a, steps

# Testing the functions
n = int(input("Enter the Fibonacci term index: "))

# Recursive approach
steps_recursive = [0]
fib_recursive = fibonacci_recursive(n, steps_recursive)
print(f"Recursive Approach: Fibonacci({n}) = {fib_recursive}, Steps = {steps_recursive[0]}")

# Iterative approach
fib_iterative, steps_iterative = fibonacci_iterative(n)
print(f"Iterative Approach: Fibonacci({n}) = {fib_iterative}, Steps = {steps_iterative}")
