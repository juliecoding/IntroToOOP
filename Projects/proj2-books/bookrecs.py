

# Read the book data into a list of (author,title) tuples. Do this at the module/file level.
books = [] 
fileReader = open('booklist.txt', 'r')
for line in fileReader:
    books.append(tuple(line.strip().split(',')))
print(books)
fileReader.close()


# Read the ratings data into a dictionary keyed by each name (converted to lower case). 
# The value for each key is a list of the ratings for that reader, preserving the original order. 
# Do this also at the module level so the data is available when the functions mentioned below are called. 
ratings = {}
fileReader = open('ratings.txt', 'r')

while True:
    name = fileReader.readline().strip().lower()
    if not name:
        break
    scores = fileReader.readline().split()
    intScores = []

    for score in scores:
        intScores.append(int(score))

    ratings[name] = intScores

print(ratings)



# Write a function dotprod(x,y) 
def dotprod(x, y):
    total = 0

    for i in range(len(x)):
        total += x[i] * y[i]
    
    return total
#print(dotprod([5, 0, -3], [5, 1, 3])) #5 * 5 + 0 * 1 + -3 * 3 = 16


# Compute affinity scores for each user.  Store it in a data structure at the module level. 
affinityScores = {}

def computeAffinityScores():
    for name1 in ratings:
        for name2 in ratings:
            if name1 != name2:
                score = dotprod(ratings[name1], ratings[name2])
                if score > 0:
                    affinityScores[name1] = affinityScores.get(name1, {})
                    affinityScores[name1][name2] = score

computeAffinityScores()
print(affinityScores)

# Write the friends function, which returns a sorted list of the names of the two readers with the highest 
# affinity scores compared to the reader in question. Use the sorted function for all sorting in this program. 
def friends(name):
    pass

# Write recommend by calling friends and then getting the recommended books from the two friends obtained. 
def reccomend(name):
    pass

def report():
    pass

#All of the above should execute when the module is loaded or imported, 
# so you need to make sure you have computed the friends and affinity scores at the module level, independent of main. 
# Your main function only prints the full report, as previously shown.
def main():
    """Prints reccomendations for all readers """
    with open('recomendations.txt', 'w') as rec_file:
        print(report(), file=rec_file)

if __name__ == '__main__':
    main()
