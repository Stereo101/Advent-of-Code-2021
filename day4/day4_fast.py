from advent import Session

aoc = Session(2021,4)
silver = None
gold = None

def winning_turn(rows,lookup):
    minimum = float("INF")
    for y in range(len(rows)):
        minimum = min(minimum,max(lookup[e] for e in rows[y]))
    for x in range(len(rows[0])):
        minimum = min(minimum,max(lookup[e] for e in (rows[i][x] for i in range(len(rows)))))
    return minimum
            
def unmarked_sum(rows,turn,lookup):
    r = 0
    for row in rows:
        r += sum(e for e in row if lookup[e] > turn)
    return r

def parse(line):
    return [int(p) for p in line.strip().split()]

lowest_win = float("INF")
silver = None

highest_win = float("-INF")
gold = None

with aoc.fp() as f:
    sequence = [int(x) for x in f.readline().split(",")]
    lookup = {e:i for i,e in enumerate(sequence)}

    f.readline()

    for group in f.read().split("\n\n"):
        rows = [parse(line.strip()) for line in group.split("\n") if line != ""]
        wt = winning_turn(rows,lookup) 
        if wt < lowest_win:
            lowest_win = wt
            silver = sequence[wt]*unmarked_sum(rows,wt,lookup)
        elif wt > highest_win:
            highest_win = wt
            gold = sequence[wt]*unmarked_sum(rows,wt,lookup)

aoc.solution(1,silver)
aoc.solution(2,gold)
