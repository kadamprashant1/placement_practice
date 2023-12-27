def eucledian_dist(point1,point2):
    return sum((x-y)**2 for x,y in zip(point1,point2)) ** 0.5
def mahattan_dist(point1, point2):
    return sum(abs(x -y) for x,y in zip(point1,point2))
def minkowski_dist(point1, point2,p):
    return sum(abs(x-y)**p for x,y in zip(point1,point2))
