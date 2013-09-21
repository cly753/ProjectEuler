def fromBack(value):
    temp = 0
    while value:
        temp = temp * 10 + value % 10
        value = value // 10
    return temp
        
palindromic = 0

for i in range(999, 1, -1):
    for j in range(999, 1, -1):
        toCheck = i * j
        if toCheck == fromBack(toCheck):
            palindromic = max(palindromic, toCheck)

print(palindromic)
