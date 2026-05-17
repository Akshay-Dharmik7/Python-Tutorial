setdata = {1, 2, 6, 4, 5, 6}

print(setdata)

#1) add():
setdata.add('a') #element
print(setdata)

#2)  remove()
setdata.remove(2) #element
print(setdata)

# setdata.remove(3) #element
# print(setdata)

#3) discard()
setdata.discard(4) #element
print(setdata)

setdata.discard(3) #element
print(setdata)

# 4) pop()
setdata.pop() #no parameter
print(setdata)

# 5) copy():
copy2 = setdata.copy()
print(copy2)

#6)  clear()
setdata.clear()
print(setdata)

