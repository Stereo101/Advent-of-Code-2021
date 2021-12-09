from advent import Session
import itertools
import math

aoc = Session(2021,8)

def parse(line):
    p1,p2 = line.split(" | ")
    return [p1.split(),p2.split()]

with aoc.fp() as f:
    lines = [parse(x) for x in f.readlines()]

valid = {"abcefg":"0",
        "cf":"1",
        "acdeg":"2",
        "acdfg":"3",
        "bcdf":"4",
        "abdfg":"5",
        "abdefg":"6",
        "acf":"7",
        "abcdefg":"8",
        "abcdfg":"9"}

def replace(x,pattern):
    default = "abcdefg"
    out = [pattern[default.index(c)] for c in x]
    out.sort()
    return "".join(out)

def perm_gen(examples):
    mapping = {}
    for c in "abcdefg":
        mapping[c] = set(list("abcdefg"))

    tells = {   2:set(list("cf")),
                3:set(list("acf")),
                4:set(list("bcdf"))}

    for ex in examples:
        if len(ex) in tells:
            for k,v in mapping.items():
                if k not in ex:
                    mapping[k] = v.difference(tells[len(ex)])

    yield from rec_perm_gen("abcdefg",mapping)

def rec_perm_gen(s,mapping,used=set()):
    if s == "":
        yield ""
        return 
    x = s[0]
    for c in mapping[x]:
        if c in used:
            continue
        for tail in rec_perm_gen(s[1:],mapping,used=used | set(c)):
            yield c + tail

silver,gold = 0,0
for p1,p2 in lines:
    examples = set(p1) | set(p2)
    valid_count = 0
    lowest_gold = float("INF")
    lowest_silver = None
    lowest_pattern = None

    for pattern in perm_gen(examples):
        if not any(replace(ex,pattern) not in valid for ex in examples):
            digits = [valid[replace(e,pattern)] for e in p2]
            gold_sum = int("".join(digits))
            if gold_sum < lowest_gold:
                lowest_gold = gold_sum
                lowest_silver = sum(digits.count(x) for x in "1478")
            valid_count += 1
            break

    if valid_count >= 1:
        gold += lowest_gold
        silver += lowest_silver
    else:
        print("No solution!!!!")
        input()

aoc.solution(1,silver)
aoc.solution(2,gold)
