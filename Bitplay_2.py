#Check if same
def check_if_same(num1, num2):
    result1 = num1 ^ num2
    if result1 != 0:
        print(f"{num1} and {num2} are not the same")
    else:
        print(f"{num1} and {num2} are the same")
input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
check_if_same(input1, input2)
#One odd occurring (XOR)
def xor_odd(arr):
    result2 = 0
    for num in arr:
        result2 ^= num
    return result2
arr_size = int(input("Enter size of array: "))
arr = []
for i in range(0, arr_size):
    input3 = int(input("Enter number: "))
    arr.append(input3)
result3 = xor_odd(arr)
if result3 != 0:
    print(f"The number that occurred an odd number of times is {result3}")
else:
    print("All numbers occurred evenly")
#Two odd occurring numbers
def two_odd(arr, size):
    xor = arr[0]
    x = 0
    y = 0
    set_bit = 0
    for i in range(0, size):
        xor ^= arr[i]
    set_bit = xor & ~(xor - 1)
    for i in range(size):
        if (arr[i] & set_bit):
            x ^= arr[i]
        else:
            y ^= arr[i]
    print(f"The two odd elements are: {x} and {y}")
arr_size1 = int(input("Enter size of array: "))
arr1 = []
for i in range(0, arr_size1):
    input4 = int(input("Enter number: "))
    arr1.append(input4)
two_odd(arr1, arr_size1)