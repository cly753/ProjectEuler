a = 1
b = 1
result = 0
for c in range(0, 100):
    a, b = b, a + b
    if a > 4000000:
        break
    if a % 2 == 0:
        result += a
print(result)
