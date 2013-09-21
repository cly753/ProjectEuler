def prime(value):
    for a in range(2, (int)(value**0.5)+1):
        if not value % a:
            return 0
    return 1

ans = 0

for a in range(2, (int)(600851475143**0.5)+1):
    if 600851475143 % a == 0:
        if prime(a):
            ans = max(a, ans)
        b = 600851475143/a
        if prime(b):
            ans = max(b, ans)

print(ans)
