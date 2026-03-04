import math
num=int(input("Enter a number:"))
root=math.sqrt(num)
if root==int(root):
    print(num,"Is a perfect square")
else:
    print(num,"Is not a perfect square")
