def dotprod

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

def frineds(name):
    pass

def recommned(name):
    pass

def report():
    pass

def main():