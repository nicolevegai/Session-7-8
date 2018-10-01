a = 5
b = 4
result = 0
pow = 1

for i in range (b):
    result = 0

    for j in range (a):
        result += pow
    pow = result

print (" the result of ", a, "**",b, "is: ", result)
