x = '321-'
if x == 0:
    print x
x = str(x)
isNeg = False

if x[0:1] == '-' or x[len(x)-2:len(x)-1]:
    isNeg = True
    x.replace('-', '')

mystr = ''
for i in range(len(x) - 1, -1, -1):
    if i == (len(x) - 1) and x[i] == '0':
        pass
    else:
        mystr += x[i]

mystr = int(mystr)
if isNeg:
    mystr * (-1)

print mystr
