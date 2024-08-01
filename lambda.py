# def myfunc(n):
    
#     return lambda a:a**n
# square=myfunc() 
# print(square(5))



# numbers=(2,4,6,8,10,12,14,16,18,20)
# # for x in numbers:
# #     print(x)
# sqrnb = list(map(lambda x:x**2,numbers))

# print(sqrnb) # Using lambda to loop through the list of number.


def myfunc(n):
    return lambda x:x**n, numbers
squarenumb=myfunc(2)
print(7)