from advent import Session

aoc = Session(2021,10)

with aoc.fp() as f:
    lines = [line.strip() for line in f.readlines()]

def first_illegal(line):
    pair = {")":"(","]":"[","}":"{",">":"<"}
    stack = []
    for c in line:
        if c not in pair:
            stack.append(c)
        elif not stack or stack[-1] != pair[c]:
            return {")":3,"]":57,"}":1197,">":25137}[c],[]
        else:
            stack.pop()
    return 0,[calc_score(stack)]

def calc_score(stack):
    score = 0
    for c in reversed(stack):
        score = score*5 + {"(":1,"[":2,"{":3,"<":4}[c]
    return score

silver = 0
scores = []
for corrupt_val,invalid_list in map(first_illegal,lines): 
    silver += corrupt_val
    scores += invalid_list

gold = sorted(scores)[len(scores)//2]

aoc.solution(1,silver)
aoc.solution(2,gold)
