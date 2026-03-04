num= int(input("Enter a number:"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
        if sum==num:
            print(num,"Is a perfect number")
        else:
            print(num,"Is not a perfect number")
