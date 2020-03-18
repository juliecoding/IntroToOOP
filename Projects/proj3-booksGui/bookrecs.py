from functools import reduce
from operator import mul, itemgetter
from heapq import nlargest
from io import StringIO

# Read the book data into a list of (author,title) tuples. Do this at the module/file level.
books = []
fileReader = open('booklist.txt', 'r')
for line in fileReader:
    books.append(tuple(line.strip().split(',')))
# print(books)
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

# print(ratings)



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
# print(affinityScores)

# Write the friends function, which returns a sorted list of the names of the two readers with the highest
# affinity scores compared to the reader in question. Use the sorted function for all sorting in this program.
def friends(name, nfriends=2):
    '''
        Returns an alphabetized list of the closest friends in reading taste
    '''
    results = affinityScores[name]
    top_n = [name for name,_ in nlargest(nfriends,results.items(),key=itemgetter(1))[:nfriends]]
    return sorted(top_n)

def recommend(name, nfriends=2):
    '''
        Returns an alphabetized list of books recommended by top friends (alphabetized by author's last name)
    '''
    def aut_title(book):    # Sort key
        aut = book[0].split()
        return (aut[-1],aut[0],book[1])

    read1 = {i for i in range(len(books)) if ratings[name][i] != 0}        # Books name has read
    recs = set()
    for name2 in friends(name, nfriends):
        liked2 = {i for i in range(len(books)) if ratings[name2][i] > 1}    # Books name2 liked
        recs |= liked2 - read1
    good_books = [books[i] for i in recs]
    return sorted(good_books,key=aut_title)

def report():
    s = StringIO()
    for name in sorted(affinityScores.keys()):
        print(name+':',friends(name),file=s)
        for b in recommend(name):
            print('\t',b,file=s)
        print(file=s)
    return s.getvalue()

#All of the above should execute when the module is loaded or imported,
# so you need to make sure you have computed the friends and affinity scores at the module level, independent of main.
# Your main function only prints the full report, as previously shown.
def main():
    """Prints reccomendations for all readers """
    with open('recomendations.txt', 'w') as rec_file:
        print(report(), file=rec_file)


if __name__ == '__main__':
    main()
