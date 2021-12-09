from advent import Session
import math

aoc = Session(2021,7)

with aoc.fp() as f:
    crabs = [int(x) for x in f.read().split(",")]
    
def gradient_f(f,x,dx,A):
    result = 0
    for e in A:
        result += f(x+dx,e)/dx - f(x,e)/dx
    return result
    
def descent(f,A):
    alpha = 0.0001
    tolerance = .0000000001
    x = A[len(A)//2]
    dx = .1

    diff = float("INF")
    step = 0
    while diff > tolerance:
        g = gradient_f(f,x,dx,A)
        diff = -alpha * g
        x += diff
        #print(f"{step=} {x=} {g=} {diff=}")
        step += 1
    return x
        
crabs.sort()

s1 = crabs[len(crabs)//2]
s2 = s1+1

#gradient descent
g1 = math.floor(descent(lambda a,b: abs(a-b)*(1+abs(a-b))//2,crabs))
g2 = g1+1

silver = min(sum(abs(e-v) for e in crabs) for v in (s1,s2))
gold = min(sum((abs(e-v)*(abs(e-v)+1))//2 for e in crabs) for v in (g1,g2))
"""
#brute force
silver,gold = float("INF"),float("INF")
silver = min(silver,sum(abs(e-align) for e in crabs))
for align in range(crabs[0],crabs[1]):
    gold = min(gold,sum((abs(e-align)*(abs(e-align)+1))//2 for e in crabs))
"""
aoc.solution(1,silver)
aoc.solution(2,gold)
