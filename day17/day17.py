from advent import *

aoc = Session(2021,17)
silver = None
gold = None

"""
def parse(line):
    retunr [int(x) for x in line.split()]

with aoc.fp() as f:
    lines = [parse(line.strip()) for line in f.readlines()]


for line in lines:
    print(line)
"""

#x=135..155, y=-102..-78

def inside_target(x,y):
    x_min = 135
    x_max = 155
    y_min = -102
    y_max = -78

    return x >= x_min and x <= x_max and y >= y_min and y <= y_max

def find_stop(dx,dy):
    x_min = 135
    x_max = 155
    y_min = -102
    y_max = -78

    steps = 1000
    x,y = 0,0
    y_max = float("-INF")
    for _ in range(steps):
        x += dx
        y += dy
        y_max = max(y_max,y)
        if inside_target(x,y):
            return True,y_max
        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1
        elif dx == 0:
            pass
        dy -= 1
        if y < y_min:
            break
    return False,y_max
        
"""
best_y = 0
total = 0
for dx in range(160):
    for dy in range(-105,500):
        t,y = find_stop(dx,dy)
        if t:
            total += 1
            best_y = max(best_y,y)
            print(dx,dy,best_y,total)

silver = best_y
gold = total
print(silver)
print(gold)
"""

x_min = 135
x_max = 155
y_min = -102
y_max = -78

y_hits = {}
x_hits = {}

valid_steps = set()
for i_dy in range(-200,500):
    steps,y = 0,0
    dy = i_dy
    for _ in range(1000):
        y += dy
        dy -= 1
        if (y >= y_min and y <= y_max):
            y_hits[steps] = y_hits.get(steps,set()) | set([i_dy])
            valid_steps.add(steps)
        steps += 1
        if y < y_min:
            break
    
x_stalled = {}
for i_dx in range(160):
    steps,x = 0,0
    dx = i_dx
    to_add = []
    for _ in range(1000):
        x += dx
        if (x >= x_min and x <= x_max):
            if dx == 0:
                x_stalled[steps] = x_stalled.get(steps,set()) | set([i_dx])
                valid_steps.add(steps)
                break
            else:
                to_add.append(steps)
        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1
        steps += 1
        if x > x_max:
            break
    if i_dx not in x_stalled.get(steps,set()):
        for s in to_add:
            x_hits[s] = x_hits.get(s,set()) | set([i_dx])
            valid_steps.add(s)

print(x_hits)
print(y_hits)
print(x_stalled)

total_ways = 0
for step in valid_steps:
    y_ways = y_hits.get(step,set())
    x_ways = x_hits.get(step,set())

    total_ways += sum(step >= x for x in x_stalled) * len(y_ways)
    total_ways += len(y_ways) * len(x_ways)

gold = total_ways
print(gold)


        
aoc.solution(1,silver)
aoc.solution(2,gold)
