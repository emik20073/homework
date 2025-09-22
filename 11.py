import string

def hashtag(name):
    for a in string.punctuation:
        name = name.replace(a, "")
    b = name.split()
    c = "#"
    for i in b:
        c += i.capitalize()
        if len(c) > 140:
            c = c[:140]
    return c
print(hashtag("i like python community!"))