import sympy

def equation(a, b, c):

    x = sympy.symbols('x')

    equation = sympy.Eq(a * x**2 + b * x + c, 0)
    solutions = sympy.solve(equation, x)
    
    return solutions