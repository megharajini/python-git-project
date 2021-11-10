n=int(input("enter the number"))
temp=n
while(n>0):
	r=n%10
	rev=rev*10+r
	n=n/10
if n==temp:
	print ("yes")
else:
	print("no")
