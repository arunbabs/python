lst = list(map(int,input("Enter list elements:").split()))
lst = list(set(lst))
lst.sort()

print("Second largest element:",lst[-2])

