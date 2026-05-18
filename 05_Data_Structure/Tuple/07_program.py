tupledata1 = ( 5, 7, 5, 9, 2, 6, 5, 8)
tupledata2 = ( 'a', 'z', 'b', 'o', 'e')

# 1) filter():
print(tuple(filter(lambda x: x > 5, tupledata1)))