n=int(input("enter the number="))
rev=0
temp=n
while n!=0:
    i=n%10
    rev=rev*10+i
    n=n//10
print(rev)
if rev==temp:
    print("the number is palindrone no") 
else:
    print("not palindrone")       