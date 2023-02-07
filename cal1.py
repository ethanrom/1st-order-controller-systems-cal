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
    K = limit(num / den, s, 0)
    return (1 - K) / R

def transient_response(step_response, t, steady_state_error):
    return step_response - steady_state_error

k = symbols('k')
P = 0.25
Q = 100
R = 1
t = symbols('t')

M = closed_loop_tf(k, P, Q, R)
print("Closed loop transfer function:")
print(M)
print("")

step_response = unit_step_response(M, t)
print("Unit step response of the closed loop transfer function:")
print(step_response)
print("")

ss_error = steady_state_error(M, R)
print("Steady state error:")
print(ss_error)
print("")

transient = transient_response(step_response, t, ss_error)
print("Transient response:")
print(transient)
print("")
