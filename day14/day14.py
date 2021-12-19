from advent import *

aoc = Session(2021,14)

with aoc.fp() as f:
    seed,rules = f.read().split("\n\n")
    seed = seed.strip()
    rules = [rule.strip().split(" -> ") for rule in rules.strip().split("\n")]

rule_d = {k:v for k,v in rules}
seed_d = {}
offset = {}

for i in range(len(seed)-1):
    pair = seed[i:i+2]
    seed_d[pair] = seed_d.get(pair,0) + 1

    #second item in pair always double counted
    offset[pair[1]] = offset.get(pair[1],0)-1

#except for the last item
offset[seed[-1]] = offset.get(seed[-1],0)+1

def insert(seed_d,rule_d,offset):
    new_seed_d = {}
    for pattern,count in seed_d.items():
        if pattern in rule_d:
            next_p = pattern[0] + rule_d[pattern]
            next_pp = rule_d[pattern] + pattern[1]
            new_seed_d[next_p] = new_seed_d.get(next_p,0) + count
            new_seed_d[next_pp] = new_seed_d.get(next_pp,0) + count

            #middle char is now double counted, correct via offset
            offset[rule_d[pattern]] = offset.get(rule_d[pattern],0) - count
        else:
            new_seed_d[pattern] = count
    return new_seed_d

def most_least_diff(seed_d,offsets):
    counts = {}
    for p,count in seed_d.items():
        for c in p:
            counts[c] = counts.get(c,0) + count

    most,least = 0,float("inf")
    most_e,least_e = None,None

    for k,v in offset.items():
        counts[k] += v

    for k,v in counts.items():
        if v > most:
            most_e,most = k,v
        if v < least:
            least_e,least = k,v
    return most-least

for _ in range(10):
    seed_d = insert(seed_d,rule_d,offset)
silver = most_least_diff(seed_d,offset)

for _ in range(40-10):
    seed_d = insert(seed_d,rule_d,offset)
gold = most_least_diff(seed_d,offset)

aoc.solution(1,silver)
aoc.solution(2,gold)
