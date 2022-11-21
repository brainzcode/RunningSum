a = [1, 2, 3, 8, 5, -5, 4, -6]
result = []
s = 0
for item in a:
    s += item
    if item < 0:
        print(result)
        break

    else:
        result.append(s)