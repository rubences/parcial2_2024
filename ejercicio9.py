import math

# Define the function for which we want to find the root
def f(x):
    return x**3 - x - 2

# Bisection method
def bisection(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None
    iter_count = 0
    while (b - a) / 2.0 > tol:
        iter_count += 1
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            return midpoint, iter_count
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2.0, iter_count

# Secant method
def secant(x0, x1, tol):
    iter_count = 0
    while abs(x1 - x0) > tol:
        iter_count += 1
        x_temp = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x_temp
    return x1, iter_count

# Newton-Raphson method
def newton_raphson(x0, tol):
    def f_prime(x):
        return 3 * x**2 - 1

    iter_count = 0
    while True:
        iter_count += 1
        x1 = x0 - f(x0) / f_prime(x0)
        if abs(x1 - x0) < tol:
            return x1, iter_count
        x0 = x1

# Parameters
a = 1
b = 2
x0 = 1.5
tol = 1e-10

# Find roots using different methods
root_bisection, iter_bisection = bisection(a, b, tol)
root_secant, iter_secant = secant(a, b, tol)
root_newton_raphson, iter_newton_raphson = newton_raphson(x0, tol)

# Print results
print(f"Bisection method: root = {root_bisection}, iterations = {iter_bisection}")
print(f"Secant method: root = {root_secant}, iterations = {iter_secant}")
print(f"Newton-Raphson method: root = {root_newton_raphson}, iterations = {iter_newton_raphson}")