# s1 = {'a','b','c','d','e','sdf'}
# print(s1)
# print(len(s1))
# print('c' in s1)
# s2 = set("PrepBytes")
# print(s2)
#
# st = "PythonnnopN"
# print(list(st))
# print(set(st))
#
# s3 = {}
# print(type(s3))
#
# s4 = set()
# print(type(s4))

s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
s3 = {1,2}
s4 = {1,2,3,4,5,6,7}
print(s1.union(s2))
print(s1|s2)

print(s1.intersection(s2))
print(s1&s2)

print(s1.difference(s2))
print(s1-s2)

print(s3.issubset(s4))
print(s3<=s1)
print(s4.issuperset(s1))
print(s4>=s1)
