def anagrams(word, words):
    letters = list(word)
    mainDict = makeLetterCountDictionary(letters)
    anas = []
    for word in words:
        comparisonDict = makeLetterCountDictionary(list(word))
        if (compareTwoThings(mainDict, comparisonDict)):
            anas.append(word)
    return anas

def compareTwoThings(a, b):
    for letter in b:
        if not letter in a:
            return False
        if a[letter] != b[letter]:
            return False
    return True

def makeLetterCountDictionary(letterList):
    letterDictionary = {'test': 1, 'test2': 2}
    tester = 'test'
    for letter in letterList:
        if (letter in letterDictionary):
            letterDictionary[letter] += 1
        else:
            letterDictionary[letter] = 1
    return letterDictionary

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
