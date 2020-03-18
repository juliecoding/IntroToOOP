booklist = []
ratings = {}
scores = {}
friendlies = {}
recommendations = {}

def readInBooklist(filename):
    with open(filename, 'r') as file:
        for line in file.readlines():
            booklist.append(tuple(line.strip().split(',')))
    return booklist

def readInRatings(filename):
    with open(filename, 'r') as file:
        while True:
            r = file.readline().strip().lower()
            if not r:
                break
            scores = list(map(lambda x: int(x), file.readline().split()))
            ratings[r] = scores
    return ratings

def dotprod(x, y):
    return x * y

def computeAffinity(baseUser, comparedUser):
    prods = []
    for i, score in enumerate(ratings[baseUser]):
        prods.append(ratings[baseUser][i] * ratings[comparedUser][i])
    return sum(prods)

def getScores(ratings):
    for r in ratings:
        for r2 in ratings:
            if r == r2:
                break
            first = r if r < r2 else r2
            second = r if r > r2 else r2
            if (first, second) in scores:
                break
            scores[(first, second)] = computeAffinity(first, second)
    return scores

def friends(name):
    names = ratings.keys()
    if name in friendlies:
        return friendlies[name]
    bffs = []
    for n in names:
        if n == name:
            continue
        if len(bffs) < 2 and n not in bffs:
            bffs.append(n)
        else:
            f1 = n if n < name else name
            s1 = n if n > name else name
            for (ind, bff) in enumerate(bffs):
                f2 = bff if bff < name else name
                s2 = bff if bff > name else name
                if scores[(f1, s1)] > scores[(f2, s2)] and n not in bffs:
                    bffs[ind] = n
    friendlies[name] = sorted(bffs)
    return friendlies[name]

def getRecommendations(name):
    recs = []
    amigos = friendlies[name] if name in friendlies else friends(name)
    for amigo in amigos:
        rats = ratings[amigo]
        for (ind, book) in enumerate(rats):
            if (rats[ind] == 3 or rats[ind] == 5):
                if (ratings[name][ind] == 0):
                    if (name not in recommendations):
                        recommendations[name] = []
                    if (booklist[ind] not in recs):
                        recs.append(booklist[ind])
    recommendations[name] = sorted(recs, key = lambda tup: (tup[0].split()[-1], tup[0].split()[0], tup[1]))
    return recommendations[name]

def recommend(name):
    return recommendations[name] if name in recommendations else getRecommendations(name)

def report():
    stringOfDoom = ''
    for r in ratings:
        recommend(r)
    stringOfDoom += str(recommendations)
    return stringOfDoom


readInBooklist('booklist.txt')
readInRatings('ratings.txt')
getScores(ratings)

def main():
    with open('recommendations.txt', 'w') as rec_file:
        print(report(), file=rec_file)




if __name__ == "__main__":
    main()