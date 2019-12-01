from math import sqrt
import sys
def dist(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def dist2(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2
def ptseg(a, b, c):
    # find distance from c to line segment a b
    ab_dist = dist2(a, b)
    t = ((c[0] - a[0]) * (b[0] - a[0]) + (c[1] - a[1]) * (b[1] - a[1])) / ab_dist
    t = max(0, min(1, t))
    ans = dist(c, (a[0] + t*(b[0] - a[0]), a[1] + t*(b[1] - a[1])))
    return ans

T = int(input())
for t in range(T):
    N = int(input())
    npts = [[int(w) for w in input().split(" ")] for _ in range(N)]
    nseg = [[npts[i], npts[i + 1]] for i in range(len(npts) - 1)] + [[npts[-1], npts[0]]]
    M = int(input())
    mpts = [[int(w) for w in input().split(" ")] for _ in range(M)]
    mseg = [[mpts[i], mpts[i + 1]] for i in range(len(mpts) - 1)] + [[mpts[-1], mpts[0]]]
    mindist = float("inf")
    for i in range(len(npts)):
        d = min([ptseg(x[0], x[1], npts[i]) for x in mseg])
        mindist = min(mindist, d)
    for i in range(len(mpts)):
        d = min([ptseg(x[0], x[1], mpts[i]) for x in nseg])
        mindist = min(mindist, d)

    print(mindist/2)
