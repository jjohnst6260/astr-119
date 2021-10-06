import numpy as np

x = 1.0
y = 2.0

# exponents and logs

print(np.exp(x))		# print e^x

print(np.log(x))		# print lnx

print(np.log10(x))		# print log base 10 of x

print(np.log2(x))		# print log base 2 of x

# min-max-misc

print(np.fabs(x))		# prints absolute value as a floar

print(np.fmin(x,y))		# prints the minimum of x and y

print(np.fmax(x,y))		# prints the maximum of x and y

# populate arrays

n=100								# defines an integer
z=np.arange(n, dtype=float)			# forms an array [0.0, n-1]
z *= 2.0*np.pi/float(n-1)			# dedlares z = [0, 2pi]
sin_z = np.sin(z)

# interpolation

print(np.interp(0.75, z, sin_z))	# interpolates sin(0.75)

print(np.sin(0.75))