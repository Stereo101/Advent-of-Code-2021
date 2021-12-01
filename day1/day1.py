from advent import Session

aoc = Session(2021,1)

lines = []
with aoc.fp() as f:
    lines = [int(line.strip()) for line in f.readlines()]

silver = sum(lines[i] > lines[i-1] for i in range(1,len(lines)))
gold = sum(lines[i] > lines[i-3] for i in range(3,len(lines)))

aoc.solution(1,silver)
aoc.solution(2,gold)
