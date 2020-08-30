n = int(input('Enter your number:'))
def sum_to(n):
    num = 0
    for i in range(0,n+1):
        num = num + i
    return num
var = sum_to(n)
print(var)