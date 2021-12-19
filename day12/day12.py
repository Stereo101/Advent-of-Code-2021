from advent import *

aoc = Session(2021,12)

with aoc.fp() as f:
    lines = [line.strip().split("-") for line in f.readlines()]

graph = {}
for a,b in lines:
    graph[a] = graph.get(a,set()) | set([b])
    graph[b] = graph.get(b,set()) | set([a])

def search(graph,current,seen=set(),double=False):
    if current == "end":
        return int(not double),int(double)

    seen.add(current)

    single_count,double_count = 0,0
    for edge in graph[current]:
        is_edge_clean = (edge not in seen) or (edge.upper() == edge)
        can_double = (not double) and (edge != "start") and (edge != "end")

        if is_edge_clean or can_double:
            s,d = search(graph,edge,seen=seen.copy(),double=((not is_edge_clean) or double))
            single_count += s
            double_count += d

    return single_count,double_count
    
silver,gold = search(graph,"start")
gold += silver

aoc.solution(1,silver)
aoc.solution(2,gold)
