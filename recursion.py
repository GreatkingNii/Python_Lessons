def recursion(k):
    if (k>0):
        result=k+recursion(k-1)
        print(result)
    else:
        result=0
    return result

print('The recursive values are: ')
recursion(6)