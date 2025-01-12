ranking = []
while True:
    try:
        height = int(input())
        ranking.append(height)
    except:
        break

sortedRanking = sorted(ranking, reverse=True)
print(sortedRanking[0])
print(sortedRanking[1])
print(sortedRanking[2])