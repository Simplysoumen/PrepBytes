IPL_team = {}
print(type(IPL_team))
IPL_team['Delhi'] = 'Rishabh'
IPL_team['Bengaluru'] = 'Virat','AB', 'Maxwell'
IPL_team[4] = 'Mumbai Indians'
print(IPL_team)

print(IPL_team['Bengaluru'][0])
print(IPL_team[4])

del IPL_team[4]
print(IPL_team)

numbers = {4:'d',3:'c',0:'a',2:'b',1:'g'}
print(numbers)
print(numbers[2])

#numbers.clear()
print(len(numbers))
print(numbers.get(4))
print(numbers.get(10,'Key is not present'))

#To get All the Keys and values in the form of tuples
print(numbers.items())

#To get all the keys
print(numbers.keys())

#To get all the values
print(numbers.values())

print(numbers.pop(2, 'Key is not present'))
print(numbers)

print(numbers.popitem())
print(numbers)
