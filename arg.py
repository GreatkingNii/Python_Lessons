def average(*arg):
    sum = 0
    length=len(arg)
    for numbers in arg:
        sum=sum+numbers
    return sum/length
        
print(average(4,4,53,2,5,))