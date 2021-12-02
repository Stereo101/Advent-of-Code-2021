from advent import Session

aoc = Session(2021,2)
silver = None
gold = None

def parse(line):
    direction,dist = line.strip().split()
    return (direction,int(dist))

with aoc.fp() as f:
    lines = [parse(line) for line in f.readlines()]

horz,depth,aim,depth2 = 0,0,0,0
for direction,dist in lines:
    if direction == "forward":
        horz += dist
        depth2 += aim * dist
    elif direction == "down":
        depth += dist
        aim += dist
    elif direction == "up":
        depth -= dist
        aim -= dist

silver = horz*depth
gold = horz*depth2
print(silver,gold)

aoc.solution(1,silver)
aoc.solution(2,gold)
