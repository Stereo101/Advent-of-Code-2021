from advent import Session

aoc = Session(2021,6)

with aoc.fp() as f:
    s = f.read().strip()
    line = [int(x) for x in s.split(",")]

size = max(line)+9
fish = [line.count(i) for i in range(size)]

def advance(arr,steps,offset=0):
    for day in range(offset,steps+offset):
        arr[(day+7)%size] += arr[day%size]
        arr[(day+9)%size] += arr[day%size]
        arr[day%size] = 0
    return sum(arr)

silver = advance(fish,80)
gold = advance(fish,256-80,offset=80)

aoc.solution(1,silver)
aoc.solution(2,gold)
