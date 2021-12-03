from advent import Session
import numpy as np

aoc = Session(2021,2)

fp = aoc.fp()

lines = [(a,int(b)) for a,b in (line.split() for line in fp.readlines())]
A = np.zeros(3,dtype=int)
p = {"up":-1,"down":1,"forward":0}
for d,dist in lines:
    A += (dist*(not p[d]), dist*p[d], dist*A[1]*(not p[d]))

silver,gold = A[0]*A[1], A[0]*A[2]

aoc.solution(1,silver)
aoc.solution(2,gold)
