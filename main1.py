'''program to check whether given number is perfect square or not'''
import math
n=int(input("enter number"))
root=math.sqrt(n)
if int(root+0.5)**2==n:
	print(n "Yes it is perfect square")
else:
	print(n "is not perfect square")