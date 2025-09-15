a = [4,2,0,0,7,0,5,3]
for i in a:
    if i == 0:
        a.remove(0)
        a.append(0)
print(a)
