s=input("Enter a string:")
print("original string:",s)
char=s[0]
s=s.replace(char,'$')
s=char+s[1:]
print(s)

