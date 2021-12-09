from advent import Session

aoc = Session(2021,9)

with aoc.fp() as f:
    grid = [[int(x) for x in line.strip()] for line in f.readlines()]

def iterate_2d(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            yield (x,y)

def neighbors(x,y,grid):
    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
        ex,ey = x+dx,y+dy
        if ex >= 0 and ex < len(grid[0]) and ey >= 0 and ey < len(grid):
            yield (ex,ey)
            
def is_lowpoint(x,y,grid):
    v = grid[y][x]
    return all(v < grid[ey][ex] for ex,ey in neighbors(x,y,grid))

def floodfill(x,y,grid):
    used_points = {(x,y)}
    queue = [(x,y)]
    nine_count = 0
    while queue:
        ex,ey = queue.pop()
        for p in neighbors(ex,ey,grid):
            if p in used_points:
                continue
            used_points.add(p)

            if grid[p[1]][p[0]] == 9:
                nine_count += 1
            else:
                queue.append(p)
    return len(used_points) - nine_count
   
lowpoints = [(x,y) for x,y in iterate_2d(grid) if is_lowpoint(x,y,grid)]
silver = sum(1 + grid[y][x] for x,y in lowpoints)

basins = [floodfill(p[0],p[1],grid) for p in lowpoints]
basins.sort(reverse=True)
gold = basins[0] * basins[1] * basins[2]

aoc.solution(1,silver)
aoc.solution(2,gold)
