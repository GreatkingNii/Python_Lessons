numbers=input(range(1,40))

def numb(step):
    if step == 1:
        for x in numbers:
            if x%2==1:
                print(x)
    elif step == 0:
        for x in numbers:
            if x%2==0:
                print(x)
    else:
        print('out of scope')
numb(0)