import numpy as np

matrix_string = "89 1903 3\n18 3 1\n9 4 800"
m = []
rows = matrix_string.split('\n')
for row in rows:
    if len(row) == 1:
        m.append([row])
    else:
        m.append(list(map(int, row.split())))
npm = np.array(m).astype(int)

index = 2

print(npm[index - 1])
print(npm[:, index - 1])
