x=input("Enter 1st number")
y=input("Enter 2nd number")
z=input("Enter 3rd number")

if (x>=y) and (num >= z):
	largest=x
elif (y>=x) and (x>=z):
	largest=y
else:
	largest=z

print(" The largest number is ", largest)
