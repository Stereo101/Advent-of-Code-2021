from advent import *

aoc = Session(2021,20)
silver = None
gold = None

def parse(line):
    return [int(x) for x in line.split(",")]

grid = {}
with aoc.fp() as f:
    iea,lines = f.read().strip().split("\n\n")
    lines = lines.split("\n")

for x,y in iterate2d(lines):
    if lines[y][x] == "#":
        grid[(x,y)] = "#"

def step(grid,parity):
    to_iterate = set()
    new_grid = {}
    for p in grid.keys():
        for x,y in sqr_itr(2):
            to_iterate.add((p[0]+x,p[1]+y))

    for point in to_iterate:
        c = iea[get_n(grid,point,parity)]
        if (c == "#") == parity:
            new_grid[point] = c
    return new_grid, parity ^ (iea[0] == "#")

def sqr_itr(size):
    for y in range(-size,size+1):
        for x in range(-size,size+1):
            yield x,y

def get_n(grid,point,parity):
    default_char = "#" if parity else "."
    v = 0
    for x,y in sqr_itr(1):
        v *= 2
        if grid.get((point[0]+x,point[1]+y),default_char) == "#":
            v += 1
    return v

parity = False
grid,parity = step(grid,parity)
grid,parity = step(grid,parity)
silver = sum(v == "#" for v in grid.values())
for _ in range(50-2):
    print(2+_)
    grid,parity = step(grid,parity)
    input()
gold = sum(v == "#" for v in grid.values())


aoc.solution(1,silver)
aoc.solution(2,gold)
