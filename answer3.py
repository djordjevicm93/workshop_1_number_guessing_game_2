def check_palindrome(long_text):
    lower = long_text.lower()
    clean = ""
    for l in lower:
        if l.isalnum():
            clean += l
    if clean == clean[::-1]:
        return True
    else:
        return False

print(check_palindrome("Was it a car or a cat I saw?"))
print(check_palindrome("racecar"))
print(check_palindrome("hello"))
