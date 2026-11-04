n = int(input("Enter the number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter an element: "))
    numbers.append(num)

unique = list(set(numbers))

print("Original list:", numbers)
print("List after removing duplicates:", unique)
