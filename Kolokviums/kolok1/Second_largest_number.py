# def sec_largest_number():
#   arr = list(map(int, input().split()))
#   arr.sort()
#   return arr[-2]
# print(sec_largest_number())

numbers=input("Enter the numbers: ").split()
max1=0;max2=0
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]<numbers[j]:
            temp =numbers[i]
            numbers[i]=numbers[j]
            numbers[j] = temp
print(numbers)
print(numbers[1])