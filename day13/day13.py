from advent import *

aoc = Session(2021,13)

with aoc.fp() as f:
    dots,fold = f.read().split("\n\n")
    dots = [l.strip().split(",") for l in dots.split("\n")]
    dots = [(int(a),int(b)) for a,b in dots]
    fold = [l.strip().split(" ")[-1] for l in fold.split("\n") if l != ""]
    fold = [(d,int(dist)) for d,dist in (l.split("=") for l in fold)]


grid = set(dots)

def fold_on(grid,d,dist):
    if d == "x":
        f = lambda x,y: ((2*dist-x),y)
    else:
        f = lambda x,y: (x,(2*dist-y))

    for x,y in list(grid):
        grid.add(f(x,y))
        
    mx,my = 0,0 
    for x,y in list(grid):
        if ((d == "x") and x > dist) or (d == "y") and y > dist:
            grid.remove((x,y))
        else:
            mx = max(x,mx)
            my = max(y,my)
    return mx,my

def show_d(grid,mx,my):
    for y in range(my+1):
        for x in range(mx+1):
            if (x,y) in grid:
                print("#",end="")
            else:
                print(".",end="")
        print()
    print()

for d,dist in fold:
    mx,my = fold_on(grid,d,dist)
show_d(grid,mx,my)

silver = len(grid)
gold = None


aoc.solution(1,silver)
aoc.solution(2,gold)
