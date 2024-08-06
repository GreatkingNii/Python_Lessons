# a=0
# b=1
# count=1
# n=20
# next_numb=b

# while count < n:
   
#     count+=1
#     a,b=b,next_numb
#     next_numb=a+b
#     print(next_numb, end=" ,")   

# class car:
#     def __init__(self,make,model,year,status):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.status=status
#     def display_info(self):
#         return(self.make, self.model, self.year, self.status)
    
# car1=car('Honda', 'Civic','2017','Good Condition')
# car2=car('Mercedez Benz','Maybach','2024','Left Rear damage')

# print(car1.make, car1.year)
# print(car2.make, car2.year)


class account:
    def __init__(self, account_holder, account_type, balance=0):
        self.Account_holder = account_holder
        self.account_type = account_type
        self._balance = balance 

    def deposit(self,amount):
        if amount > 0:
            self._balance +=amount
    
    def withdraw(self,amount):
        if amount <= self._balance:
            self._balance -=amount
        else:
            print('Insufficient funds')

    def balance_inquiry(self):
        return self._balance


acc1=account('Razak Nii Nartey', 'Current Account',900000)
acc1.deposit(7000)
print(acc1.Account_holder, acc1.account_type, acc1._balance)


# def swaplist(newlist):

#     size=len(newlist)
#     temp=newlist[0]
#     newlist[0]=newlist[size -1]
#     #newlist[size-1]=temp

#     return newlist

# newlist=[1,2,3,4,5]
# print(swaplist(newlist))