num=int(input("Enter a number:"))
temp=num
order=len(str(num))
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10
    if sum == num:
        print(num,"Is an Armstrong number")
    else:
        print(num,"Is not an Armstrong number")
