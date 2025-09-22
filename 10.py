import keyword
import string
def a(name):
    if name.count("_") > 1:
        return False
    if not name:
        return False
    if name[0].isdigit():
        return False
    if name in keyword.kwlist:
        return False
    if any (c in string.punctuation and c != "_" for c in name):
        return False
    if any(c.isupper() for c in name):
        return False
    if any(c.isspace() for c in name):
        return False
    return True
print(a("__"))
print(a("Hello"))