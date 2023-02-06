from sympy import symbols, simplify, InverseLaplaceTransform, exp

def closed_loop_tf(k, L, R):
    s = symbols('s')
    GP = 1 / (L * s + R)
    GC = k
    M = (GP * GC) / (1 + GP * GC)
    M = simplify(M)
    return M

def unit_step_response(M, t):
    s = symbols('s')
    return InverseLaplaceTransform(M, t, s, plane='s').doit().subs(s, 0)

k = symbols('k')
L = 10
R = 100
t = symbols('t')
M = closed_loop_tf(k, L, R)
print("Closed loop transfer function:")
print(M)

step_response = unit_step_response(M, t)
print("Unit step response of the closed loop transfer function:")
print(step_response)
