from advent import Session

aoc = Session(2021,1)
silver = None
gold = None


lines = []
with aoc.fp() as f:
    lines = [int(line.strip()) for line in f.readlines()]

count = 0
last_line = lines[0]
for line in lines[1:]:
    if line > last_line:
        count += 1
    last_line = line

silver = count

window = lines[0] + lines[1] + lines[2]
count = 0
i=3
while i < len(lines):
    new_window = window - lines[i-3] + lines[i]
    if new_window > window:
        count += 1
    window = new_window
    i += 1
    
gold = count

aoc.solution(1,silver)
aoc.solution(2,gold)
