import numpy as np 

x = 1.0 	# define floats
y = 2.0

# exp and logs

print(np.exp(x))		# e^x
print(np.log(x))		# lnx
print(np.log10(x))		# log base 10
print(np.log2(x))		# log base 2

# min-max-misc

print(np.fabs(x))		# abs value as float
print(np.fmin(x,y))		# min of x,y as float
print(np.fmax(x,y))		# max of x,y as float


# populate arrays

n = 100 						# define an int
z = np.arange(n, dtype=float)	# get an array ]0.0, n-1]
z *= 2.0*np.pi/float(n-1)		# z = [0.0, 2pi] inclusive
sin_z = np.sin(z)				# get an array sinz

# interpolation

print(np.interp(0.75, z, sin_z))	# interpolate value  sine at 0.75
print(np.sin(0.75))		

# using n = 10000

n = 100000						# define an int
z = np.arange(n, dtype=float)	# get an array ]0.0, n-1]
z *= 2.0*np.pi/float(n-1)		# z = [0.0, 2pi] inclusive
sin_z = np.sin(z)