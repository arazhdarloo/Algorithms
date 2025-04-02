nums = [1,1,2]
expectedNums = []

nums.sort()

lastNumber = ''
for num in nums:
    if(num != lastNumber):
        expectedNums.append(num)
        lastNumber = num
    else:
        pass
        
print(expectedNums)