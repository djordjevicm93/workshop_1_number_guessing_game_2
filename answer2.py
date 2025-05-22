def singulars_and_plurals(nouns):
    singulars = list()
    plurals = list()
    for w in nouns:
        if w.endswith("s"):
            plurals.append(w)
        else:
            singulars.append(w)
    answer = dict(singulars = singulars, plurals = plurals)
    return answer

words = ["tomato", "tomatoes", "potato", "potatoes", "cars", "unicorns", "horse", "cow"]
result = singulars_and_plurals(words)
print(result)
