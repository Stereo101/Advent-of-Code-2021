from advent import *

def step(grid,parity):
    to_iterate = set()
    new_grid = set()
    for p in grid:
        for x,y in sqr_itr(1):
            to_iterate.add((p[0]+x,p[1]+y))

    for point in to_iterate:
        c = iea[get_n(grid,point,parity)]
        if (c == "#") == parity:
            new_grid.add(point)
    return new_grid, parity ^ (iea[0] == "#")

def sqr_itr(size):
    for y in range(-size,size+1):
        for x in range(-size,size+1):
            yield x,y

def get_n(grid,point,parity):
    v = 0
    for x,y in sqr_itr(1):
        v = v*2 + (((point[0]+x,point[1]+y) in grid) ^ parity)
    return v

aoc = Session(2021,20)

grid = set()
with aoc.fp() as f:
    iea,lines = f.read().strip().split("\n\n")
    lines = lines.split("\n")

for x,y in iterate2d(lines):
    if lines[y][x] == "#":
        grid.add((x,y))


parity = False
grid,parity = step(grid,parity)
grid,parity = step(grid,parity)
silver = len(grid)
for _ in range(50-2):
    grid,parity = step(grid,parity)
gold = len(grid)

aoc.solution(1,silver)
aoc.solution(2,gold)
