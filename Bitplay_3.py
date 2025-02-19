#Swapping values
def swap_1(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"Swapped values: a = {a}, b = {b}")
def swap_2(a, b):
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    print(f"Swapped values: a = {a}, b = {b}")
def swap_3(a, b):
    a = a + b
    b = a - b
    a = a - b
    print(f"Swapped values: a = {a}, b = {b}")
a, b = 10, 12
swap_1(a, b)
swap_2(a, b)
swap_3(a, b)
#Division but complicated
def divide(divident, divisor):
    sign = (-1 if(divident < 0) ^ (divisor < 0) else 1)
    divident = abs(divident)
    divisor = abs(divisor)
    quotient = 0
    temp = 0
    for i in range(31, -1, -1):
        if temp + (divisor << i) <= divident:
            temp += divisor << i
            quotient |= 1 << i
    if sign == -1:
        quotient = -quotient
    return quotient
a = int(input("Enter a for a / b: "))
b = int(input("Enter b for a / b: "))
result = divide(a, b)
print(f"a / b = {result}")
print(f"OR YOU COULD a / b AND get the same result: {a / b}")