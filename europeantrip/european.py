def distance (p1, p2):
    return (p1[1] - p2[1])**2 + (p1[0] - p2[0])**2

points = [[0, 0], [1, 0], [0, 1]]

geometric_mediod = min(map(lambda p1:(p1,sum(map(lambda p2:distance(p1,p2),points))),points), key = lambda x:x[1])[0]
print(geometric_mediod)
