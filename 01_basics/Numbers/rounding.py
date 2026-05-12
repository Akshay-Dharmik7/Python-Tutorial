import math

#1. abs()
print("-----abs()-------")
print(abs(2-10))

#2. rounding Numbers
# 2.1 round()
print("---- round()-------")
print(round(2.3))
print(round(2.5))
print(round(2.7))
print(round(5.4464356))
print(round(5.4464356, 2))

# 2.2 math.floor() - nearest min/lowest value
print("------floor()-------")
print(math.floor(2.3))
print(math.floor(2.5))
print(math.floor(2.7))

# 2.3 math.ceil() - nearest max/greater value
print("------- ceil()-----")
print(math.ceil(2.3))
print(math.ceil(2.5))
print(math.ceil(2.7))

# 2.4 math.trunc()
print("------ trunc() ------")
print(math.trunc(2.555))
print(int(2.555))

# Diff between trunc() and int()
# ---- int() ------
# -when we are not using math module then use int() only.
# - difficult to understand what actually we are doing when we use int() on string, it looks like we are converting string into integer/number

# ------ trunc() -----------
# - When we are using math module then ue trunc().
#  -  In case of trunc() easy to understand by just reading the operation comparwe to int().

