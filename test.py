def distance(row1, row2):
    distance = 0

    # fix this function so that it returns 
    # the sum of differences between the occurrences
    # of each word in row1 and row2.
    # you can assume that row1 and row2 are lists with equal length, containing numeric values.
    for i in range(len(row1)):
            distance += abs(row1[i] - row2[i]) 
    return distance

data = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 1, 0]
]

# dist = [[distance(sent1, sent2) for sent1 in data] for sent2 in data]
dist = []
for sent2 in data:
    row_distance = []
    for sent1 in data:
        row_distance.append(distance(sent1, sent2))
    dist.append(row_distance) 
# print nested list
print(dist)