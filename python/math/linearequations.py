import sys

def solve_linear_equation(lineal_equation,variable='x'):
    tmp = lineal_equation.replace("=","-(") + ")"
    grouped_equation = eval(tmp.replace(variable,'1j'))
    return -grouped_equation.real/grouped_equation.imag

if len(sys.argv) > 1:
    linear_equation=sys.argv[1]
    print("linear equation: " + linear_equation)
    print("x=" + str(solve_linear_equation(linear_equation))) 
else:
    print('	please type the linear equation to solve')