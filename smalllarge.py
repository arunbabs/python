n = int(input("Enter the number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter an element: "))
    numbers.append(num)

print("List:", numbers)
print("Largest element:", max(numbers))
print("Smallest element:", min(numbers))
