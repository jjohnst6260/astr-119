# python exceptions allow you to deal with unexpected results

try:
	print(a)    # this will give an exception, a not defined
except:
	print("a is not defined")

# there are specific errors to help with certain cases

try:
	print(a)     # gives exceptiobn
except NameError:
	print("a is still not defined!")
except:
	print("Something else went wrong.")

# this will break the program - a is not defined

print(a)
