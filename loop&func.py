numbers=[1,2,3,4,5,6,7,8,9,10]

def value(step):
    if step  not in [0,1]:
        print('out of scope')
    else:
        for x in numbers:
            if x%2==step:
                print (x)
value(4)