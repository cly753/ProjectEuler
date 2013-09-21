def check(value):
    for a in range(2, (int)(value**0.5)+1):
        if not value % a:
            return 0
    return 1

up = 10001 * 10001 + 10001 + 1
count = 0
for a in range(2, up):
    if check(a):
        count += 1
    if count == 10001:
        print(a)
        break
