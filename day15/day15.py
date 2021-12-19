from advent import *
import heapq

aoc = Session(2021,15)
silver = None
gold = None

def parse(line):
    return [int(x) for x in list(line)]

with aoc.fp() as f:
    s = f.readlines()
    lines = [parse(line.strip()) for line in s if line != ""]

def get_risk(x,y,grid):
    adjust = (x // len(grid[0])) + (y // len(grid))
    fx,fy = x%len(grid[0]),y%len(grid)
    v = ((grid[fy][fx]-1+adjust) % 9) + 1
    return v

def bfs(grid,start,end,tiled=1):
    h = []
    heapq.heappush(h,(0,start))
    dist = {}
    
    while h:
        v,current = heapq.heappop(h)
        x,y = current
        
        if v > dist.get(current,float("INF")):
            continue
        elif current == end:
            return dist[end]

        for nx,ny in adj4(x,y,grid,tiled=tiled):
            ev = v + get_risk(nx,ny,grid)
            if ev < dist.get((nx,ny),float("INF")):
                dist[(nx,ny)] = ev
                heapq.heappush(h,(ev,(nx,ny)))
                
    return dist[end]
        
silver = bfs(lines,(0,0),(len(lines[0])-1,len(lines)-1))
gold = bfs(lines,(0,0),((len(lines[0])*5)-1,(len(lines)*5)-1),tiled=5)



aoc.solution(1,silver)
aoc.solution(2,gold)
