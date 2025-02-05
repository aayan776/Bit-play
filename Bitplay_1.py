#First_set_bit
def Find_first_set_bit(n):
    count = 0
    while n:
        if (n & 1 == 1):
            break
        count += 1
        print(count)
        n >>= 1
    return count
user1 = int(input("Enter a number: "))
result1 = Find_first_set_bit(user1)
print(f"First set bit of {user1} is {result1}")
#How many ones and zeroes
def find_binary(n):
    ones = 0
    zeroes = 0
    while n:
        if n & 1 == 1:
            ones += 1
        else:
            zeroes += 1
        n >>= 1
    print("")
    print(f"Number of ones = {ones}")
    print(f"Number of zeroes = {zeroes}")
user2 = int(input("Enter number: "))
find_binary(user2)
#nth bit set or not
def setornot(number, n):
    if number & (1 << (n - 1)):
        print("Set")
    else:
        print("Not set")
user3 = int(input("Enter number: "))
user4 = int(input("Enter bit: "))
setornot(user3, user4)