st = "Prep Bytes"
print(st[0])
print(st[-10])
print(st[1])
print(st[-9])

print(st[0:6])
print(st[2:7])
print(st[0:4])
print(st[5:])
print(st[:7])
print(st[:])
print(st[5:] + st[:4])
print(st[-6:2])
print(st[-6:-2])
print(st[-6:8])

print(st[0:7:3])
print(st[:8:2])
print(st[0::5])
print(st[::-1])
print(st[6:8:-1])

st = list(st)
st[7] = 'Z'
print(st)
st1="".join(map(str, st))
print(st1)














