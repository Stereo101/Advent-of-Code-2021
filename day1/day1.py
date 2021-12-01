from advent import Session

aoc = Session(2021,1)
silver = None
gold = None

lines = []
with aoc.fp() as f:
    lines = [line.strip() for line in f.readlines()]

for line in lines:
    print(line)

aoc.solution(1,silver)
aoc.solution(2,gold)
