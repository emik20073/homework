import string
a = "x-E"
ascii_str = string.ascii_letters
start, end = a.split("-")
result = ascii_str[ascii_str.index(start):ascii_str.index(end) + 1]
print(result)