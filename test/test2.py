i = [10, 2, 3, 4]
g = i[0]
for k in i[1:]:
    print("iteration: ", k)
    g = g * k
print(g)