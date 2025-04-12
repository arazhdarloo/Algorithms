number = int(input("enter your number: "))
rev = 0

while(number != 0):
    out = number % 10
    rev = (rev * 10) + out
    number = number // 10

print(rev)