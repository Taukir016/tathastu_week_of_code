https://www.linkedin.com/in/mohammad-taukir-ansari-734008179

n = int(input("Enter the value of N:"))

print("\n")

for i in range(n):
    print("* " * (n - i) + "    " * i + " *" * (n - i))
    
for i in range(2,n + 1):
    print("* " * i + "    " * (n - i) + " *" * i)
© 2020 GitHub, Inc.
