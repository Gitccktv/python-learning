numbers = [3, 8, 1, 9, 2, 7, 4, 6, 5]
max=min=numbers[0]
average=0
for i in numbers:
    if i>max:
        max=i
print(max)

for i in numbers:
    if i<min:
        min=i
print(min)

for i in numbers:
    average+=i
average/=len(numbers)
print(average)

numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

for i in numbers:
    if i%2==1:
        numbers.remove(i)
print(numbers)