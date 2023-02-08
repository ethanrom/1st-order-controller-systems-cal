from sympy import symbols, simplify, InverseLaplaceTransform, exp, numer, denom, Eq, limit

def closed_loop_tf(k, P, Q, R):
    s = symbols('s')
    GP = P / (Q * s + R)
    GC = k
    M = (GP * GC) / (1 + GP * GC)
    M = simplify(M)
    return M

def unit_step_response(M, t):
    s = symbols('s')
    return InverseLaplaceTransform(M, t, s, plane='s').doit().subs(s, 0)

def steady_state_error(M, R):
    s = symbols('s')
    num, den = numer(M), denom(M)
    return R / (den.subs(s, 0))

def transient_response(step_response, t, steady_state_error):
    return step_response - steady_state_error

k = symbols('k')
P = float(input("Enter value for P: "))
Q = float(input("Enter value for Q: "))
R = float(input("Enter value for R: "))
t = symbols('t')

M = closed_loop_tf(k, P, Q, R)
print("\nClosed loop transfer function:")
print(M)

step_response = unit_step_response(M, t)
print("\nUnit step response of the closed loop transfer function:")
print(step_response)

ss_error = steady_state_error(M, R)
print("\nSteady state error:")
print(ss_error)

transient = transient_response(step_response, t, ss_error)
print("\nTransient response:")
print(transient)
