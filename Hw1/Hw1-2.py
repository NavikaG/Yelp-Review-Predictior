import numpy

pi=numpy.pi
n=100
total=0.0

for i in range (n+1):
	help=0.0
	help=((4.*i)+1.)*((4.*i)+3.)
	help=1/help
	total=help+total
	print("Sum:", 8*total)

total=8*total
print("total:", total)	 