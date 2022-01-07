"""
题目4
rest1 = 3 > 4 and 4 > 3 or 1 == 3 and 'x' == 'x' or 3 > 3
结果是什么?-True
"""
# ((False) and (True)) = False
# False or False = False
# False and True = False--其实这里可以不看了，因为and前面有个False
# False or False = False
print(3 > 4 and 4 > 3 or 1 == 3 and 'x' == 'x' or 3 > 3)
