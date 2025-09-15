lst = [1]
i = 0
a = 0
while i < len(lst):
    a += lst[i]
    i += 2
if lst:
    b = a * lst[-1]
else:
    b = 0
print(b)