def is_palindrome(text):
    a = ''.join(b.lower() for b in text if b.isalnum())
    return a == a[::-1]
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")