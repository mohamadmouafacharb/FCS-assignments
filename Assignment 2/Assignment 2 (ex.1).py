list1 = [54, 76, 2, 4, 98, 100]
list1.sort()
print(list1)

int1 = int(input("Enter the first integer: "))
int2 = int(input("Enter the second integer: "))

if int1 > int2:
    temp=int1
    int1=int2
    int2=temp
print("value within the range:")
for value in list1:
    if int1 <= value <= int2:
        print(value)  