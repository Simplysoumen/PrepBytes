l = ['a','b',4,'c','d','e',1,5,1]

#Slicing
print(l[-4:-1])
print(type(l))
print(l[2::2])
print(l[::2])
print(l[::-2])
print(l[7:0:-3])

#in and not in operation
print('b' in l)
print('b' not in l)
print('z' in l)

# + *
l = l+['k',6,'l',5.6]
print(l)

print(l*2)

#print(len(l))
#print(min(l))
#print(max(l))

l1=['a',1,['bb','ccd','abcde'],3,['bdc','pqr']]
print(len(l1))
print(len(l1[2]))
print(len(l1[4]))
print(len(l1[4][0]))
print(l1[4][1])
print(l1[2][2])
print(l1[2][2][2])
print(l1[2][-2])


l2 = ['a','b',1,2,'aca']
l2[2] = 'abcd'
print(l2)
l2[-1] = 100
print(l2)
print(l2[1:4])
l2[1:4]=[1000]
print(l2)
del l2[0]
print(l2)

l2=l2+[1,2]
print(l2)
l2=[1,2]+l2
print(l2)

l2.append('abcd')
print(l2)

l2.insert(2,'efgh')
print(l2)

l2.remove('efgh')
print(l2)

print(l2.pop(2))
print(l2)
