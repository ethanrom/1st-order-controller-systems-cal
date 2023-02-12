from sympy import symbols, simplify, InverseLaplaceTransform, exp, numer, denom, Eq, limit
import tkinter as tk
from tkinter import messagebox

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

def show_result():
    try:
        k = symbols('k')
        P = float(p_entry.get())
        Q = float(q_entry.get())
        R = float(r_entry.get())
        t = symbols('t')

        M = closed_loop_tf(k, P, Q, R)
        result = "\nClosed loop transfer function:\n" + str(M) + "\n\nUnit step response of the closed loop transfer function:\n" + str(unit_step_response(M, t)) + "\n\nSteady state error:\n" + str(steady_state_error(M, R)) + "\n\nTransient response:\n" + str(transient_response(unit_step_response(M, t), t, steady_state_error(M, R)))
        messagebox.showinfo("Results", result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Closed Loop Transfer Function Calculator")

p_label = tk.Label(root, text="Enter value for P:")
p_label.grid(row=0, column=0, padx=10, pady=10)
p_entry = tk.Entry(root)
p_entry.grid(row=0, column=1, padx=10, pady=10)

q_label = tk.Label(root, text="Enter value for Q:")
q_label.grid(row=1, column=0, padx=10, pady=10)
q_entry = tk.Entry(root)
q_entry.grid(row=1, column=1, padx=10, pady=10)

r_label = tk.Label(root, text="Enter value for R:")
r_label.grid(row=2, column=0, padx=10, pady=10)
r_entry = tk.Entry(root)
r_entry.grid(row=2, column=1, padx=10, pady=10)

def get_tf():
    P = float(p_entry.get())
    Q = float(q_entry.get())
    R = float(r_entry.get())
    t = symbols('t')
    k = symbols('k')
    M = closed_loop_tf(k, P, Q, R)
    step_response = unit_step_response(M, t)
    ss_error = steady_state_error(M, R)
    transient = transient_response(step_response, t, ss_error)
    result_label.config(text="Closed loop transfer function:\n" + str(M) +
                        "\n\nUnit step response:\n" + str(step_response) +
                        "\n\nSteady state error:\n" + str(ss_error) +
                        "\n\nTransient response:\n" + str(transient))

calculate_button = tk.Button(root, text="Calculate", command=get_tf)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", wraplength=300)
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
