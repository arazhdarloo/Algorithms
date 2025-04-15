number = int(input("enter your number: "))
output = 1

for n in range(1, number + 1):
    output *= n
    
print(output)