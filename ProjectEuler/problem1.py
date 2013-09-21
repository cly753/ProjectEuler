a = 0
for b in range(0, 1000):
    if b % 3 == 0 or b % 5 == 0:
        a += b

print(a)
