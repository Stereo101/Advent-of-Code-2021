from advent import *
import itertools

aoc = Session(2021,19)
silver = None
gold = None

def parse(line):
    return [int(x) for x in line.split()]

with aoc.fp() as f:
    s = f.read().strip()
    scanners_raw = s.split("\n\n")
    scanners = [lines.split("\n")[1:] for lines in scanners_raw]
    for i in range(len(scanners)):
        scanners[i] = [[int(x) for x in line.split(",")] for line in scanners[i]]

        
def calc_all_deltas(scanner):
    out = set()
    for a,b in itertools.combinations(scanner,2):
        delta = (a[0]-b[0],a[1]-b[1],a[2]-b[2])
        for way in all_ways(delta):
            out.add(way)
    return set(out)

def calc_deltas(scanner):
    out = set()
    for a,b in itertools.combinations(scanner,2):
        delta = (a[0]-b[0],a[1]-b[1],a[2]-b[2])
        out.add(delta)
    return set(out)


def aligned(delta_a,delta_b):
    return len(delta_a & delta_b) >= 12

def shift_align(scanner_a,scanner_b):
    possible_shifts = []

    for a in scanner_a:
        for b in scanner_b:
            shift = (a[0]-b[0],a[1]-b[1],a[2]-b[2])
            possible_shifts.append(shift)
    a_set = set(tuple(e) for e in scanner_a)
    for shift in possible_shifts:
        b_set = set(pw_add(b,shift) for b in scanner_b)
        if len(b_set & a_set) >= 12:
            return shift
    return None

def pw_add(a,b):
    return (a[0]+b[0],a[1]+b[1],a[2]+b[2])
    

"""Shoutout to stack overflow"""
def roll(v):
    return (v[0],v[2],-v[1])
def turn(v):
    return (-v[1],v[0],v[2])
def all_ways(v):
    for cycle in range(2):
        for step in range(3):
            v = roll(v)
            yield v
            for i in range(3):
                v = turn(v)
                yield v
        v = roll(turn(roll(v)))

def iterate_scanner(scanner):
    sat_itr = [all_ways(v) for v in scanner]
    for _ in range(24):
        out = [next(itr) for itr in sat_itr]
        yield out

deltas = [calc_all_deltas(scanner) for scanner in scanners]

graph = {}
for a,b in itertools.combinations(range(len(scanners)),2):
    overlap = deltas[a] & deltas[b]
    if len(overlap) >= 12:
        graph[a] = graph.get(a,set()) | set([b])
        graph[b] = graph.get(b,set()) | set([a])

        print(a,b,len(overlap))

for k,v in graph.items():
    print(k,v)

fixed = set([0])
frontier = [0]
seen = set([0])


beacon_set = set(tuple(e) for e in scanners[0])

dists = [None] * len(scanners)
dists[0] = (0,0,0)
while frontier:
    e = frontier.pop()
    neighbors = graph.get(e,set())
    #print("working on",e,"neighbors:",neighbors)
    this_delta = calc_deltas(scanners[e])

    for n in neighbors:
        if n in fixed:
            continue
            
        n_scanner = scanners[n]
        
        #Shift all satelites until
        for scan_rot in iterate_scanner(n_scanner):
            n_delta = calc_deltas(scan_rot)
            if aligned(this_delta,n_delta):
                scanners[n] = scan_rot
                shift_amt = shift_align(scanners[e],scanners[n])
                dists[n] = shift_amt
                print("aligned",n,"from",e,"shift",shift_amt,"@",dists[n])
                scanners[n] = [pw_add(shift_amt,p) for p in scanners[n]]
                for p in scanners[n]:
                    beacon_set.add(p)
                fixed.add(n)
                if n not in seen:
                    frontier.append(n)
                    seen.add(n)
                break

for i,d in enumerate(dists):
    print(i,d)
gold = float("-INF")
for a,b in itertools.combinations(dists,2):
    manhat = abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2])
    gold = max(gold,manhat)
silver = len(beacon_set)
print(silver)
print(gold)
input()

aoc.solution(1,silver)
aoc.solution(2,gold)
