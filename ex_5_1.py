a = [0, 0]
b = [0, 0, 0]
a[0] = 2
a[1] = a[0] ** a[0]
a.append( a[0] + a[1] )
b[1 + 1] = a[0] - 1
b[a[0]-1] = 2*a[1] - 1
b[2+0*a[0]-a[1]] = b[0] + 1
for i in range(0,3):
 b[i] = b[i] + i
b[1] = 9
b = a
a[2] = 8
print(b)