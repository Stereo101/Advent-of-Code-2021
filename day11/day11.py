from advent import Session
import multiprocessing

aoc = Session(2021,11)

def parse(line):
    return [int(x) for x in list(line)]

#with aoc.fp() as f:
with aoc.fp(BIGBOY=True) as f:
    grid = [parse(line.strip()) for line in f.readlines()]

def neighbors(x,y,grid):
    for dx,dy in ((-1,0),(1,0),(-1,1),(1,-1),(0,-1),(0,1),(-1,-1),(1,1)):
        ex = dx+x
        ey = dy+y
        if ex >= 0 and ex < len(grid[0]) and ey >= 0 and ey < len(grid):
            yield ex,ey

def iterate2d(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            yield x,y

def step(grid):
    to_flash = []
    for x,y in iterate2d(grid):
        grid[y][x] += 1
        if grid[y][x] == 10:
            to_flash.append((x,y))

    flashed = set()

    while to_flash:
        x,y = to_flash.pop()
        for nx,ny in neighbors(x,y,grid):
            grid[ny][nx] += 1
            if grid[ny][nx] == 10:
                to_flash.append((nx,ny))
        flashed.add((x,y))

    for x,y in flashed:
        grid[y][x] = 0

    return len(flashed)
                    
silver,steps = 0,0
total_octo = len(grid)*len(grid[0])

#while (v := step(grid)) != total_octo:
while True:
    v = step(grid)
    if v == total_octo:
        break
    silver += (v * (steps < 100))
    """
    print(steps,v)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            print(grid[y][x],end="")
        print()
    print()
    input()
    """
    steps += 1
gold = steps+1

aoc.solution(1,silver)
aoc.solution(2,gold)
