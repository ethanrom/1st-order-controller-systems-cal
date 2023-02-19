import pandas as pd

def pad_with_zeros(array, length):
    return array + [0] * (length - len(array))

print("\n\n Routh's table \n\n")

order = int(input("Enter the order of the system: "))

equation = [int(input(f"Enter the coefficient of s^{i}: ")) for i in range(order, -1, -1)]

table = []
table.append(equation[::2])
table.append(pad_with_zeros(equation[1::2], len(table[0])))

for i in range(2, len(equation)):
    current_row = []
    for j in range(len(table[0]) - 1):
        if table[i-1][0] == 0:
            current_row.append("E")
        else:
            current_element = (table[i-1][0] * table[i-2][j+1] - table[i-2][0] * table[i-1][j+1]) / table[i-1][0]
            current_row.append(round(current_element, 2))
    current_row = pad_with_zeros(current_row, len(table[0]))
    table.append(current_row)

print(pd.DataFrame(table))
