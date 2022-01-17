from doctest import FAIL_FAST


x = True and True   # True
y = True and False  # True
z = False and True  # True
v = False and False # False

c = True or True    # True
a = True or False   # False
b = False or True   # False
e = False or False  # False
h = True and False or True # True

print(x, y, z, v, c, a ,b, e, h)