def shorten(long_string):
    abbreviation = ""
    letters = long_string.split()
    for l in letters:
        short_big = l[0].upper()
        abbreviation += short_big
    return abbreviation

shortened = shorten("Don't repeat yourself")
print(shortened)

shortened = shorten("Read the fine manual")
print(shortened)

shortened = shorten("All terrain armoured transport")
print(shortened)
