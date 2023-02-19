import numpy as np
import control as ctrl
import matplotlib.pyplot as plt

def routh_array(den):
    r = [[],[]]
    for i in range(len(den)):
        r[i%2].append(den[i])

    i=0
    while True:

        if len(r[i])>len(r[i+1]) and r[i][len(r[i])-1]!=0:
            r[i+1].append(0)
        if r[i][len(r[i])-1] == 0:
            r[i].pop()
        if len(r[i])>1:
            r.append([])
        if r[i+1][0]==0:
            den= [a + b for a, b in zip(den + [0], [0]+den)]
            return routh_array(den)
        for j in range(len(r[i])-1):
            r[i+2].append((r[i+1][0]*r[i][j+1] - r[i][0]*r[i+1][j+1])/r[i+1][0])
        if len(r[i])==1:
            break
        i += 1
    return r

def check_stability(den):
    if den[len(den)-2]==0 and den[len(den)-1]==0:
        print('System Unstable due to multiple poles at origin!')
        return False
    flag = 0
    row_array = routh_array(den)
    for i in range(len(row_array)-1):
        if row_array[i][0]*row_array[i+1][0]<0:
            flag = 1
    if flag ==0:
        print('Stable')
        return True
    else :
        print('Unstable')
        return False

# Example polynomial coefficients
num = [1]
den = [1, 5, 4, -1]

# Check the stability of the system defined by the polynomial coefficients
result = check_stability(den)

# Confirm by plotting pole-zero graph on s-plane
p, z = ctrl.pzmap(ctrl.TransferFunction(num, den), plot = True, title="Pole-Zero Plot" )
plt.show()  
