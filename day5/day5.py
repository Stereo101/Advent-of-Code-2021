from advent import Session

aoc = Session(2021,5)
silver = None
gold = None

def parse(line):
    a,b = line.split(" -> ")
    p1 = tuple(int(x) for x in a.split(","))
    p2 = tuple(int(x) for x in b.split(","))
    return (p1,p2)

def get_dir(a,b):
    return (b-a)//abs(b-a) if b-a else 0
     
with aoc.fp() as f:
    lines = [parse(line.strip()) for line in f.readlines()]

grid,diag = {},{}
for p1,p2 in lines:
        dx = get_dir(p1[0],p2[0])
        dy = get_dir(p1[1],p2[1])
        is_diag = (dx != 0) and (dy != 0)
        target = diag if is_diag else grid

        stop = (p2[0]+dx,p2[1]+dy)
        e = p1
        while e != stop:
            target[e] = target.get(e,0)+1
            e = (e[0]+dx,e[1]+dy)
           
silver = sum(v > 1 for v in grid.values())
for k,v in diag.items():
    grid[k] = grid.get(k,0) + v
gold = sum(v > 1 for v in grid.values())

aoc.solution(1,silver)
aoc.solution(2,gold)
