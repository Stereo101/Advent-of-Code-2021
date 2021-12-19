from advent import *
import itertools
import math
import ast

aoc = Session(2021,18)

with aoc.fp() as f:
    s = f.readlines()
    lines = [line.strip() for line in s]

#Node class to allow int* essentially.
class node:
    def __init__(self,n):
        self.n = n
    def __repr__(self):
        return str(self.n)

#Convert nested list of ints, to nested list of nodes
def nodify(L,offset=0):
    if offset >= len(L):
        return

    a = L[offset]
    if type(a) == type([]):
        nodify(a)
    else:
        L[offset] = node(a)

    nodify(L,offset+1)

"""Basic overview::
In order traverse the list
Keep track of the last_leaf node visited
Find first explode target (l,r)
Increase the last_leaf by l
Continue Traversal
Increase next leaf by r
"""
def snail_explode(snail,last_leaf=None,to_add=None,depth=1):
    a = snail[0]
    b = snail[1]
    a_is_list = type(a) == type([])
    b_is_list = type(b) == type([])

    if simple_pair(a):
        l,r = a
        if to_add is not None:
            l.n += to_add.n
            return last_leaf,to_add,True

        elif depth >= 4 and to_add is None:
            if last_leaf is not None:
                last_leaf.n += l.n
            snail[0] = node(0)
            to_add = r
        else:
            last_leaf = r

    elif a_is_list:
        last_leaf,to_add,done = snail_explode(a,last_leaf=last_leaf,
                                                to_add=to_add,
                                                depth=depth+1)
        if done:
            return last_leaf,to_add,done
    else:
        if to_add is not None:
            a.n += to_add.n
            return last_leaf,to_add,True
        else:
            last_leaf = a

    if simple_pair(b):
        l,r = b
        if to_add is not None:
            l.n += to_add.n
            return last_leaf,to_add,True
        elif depth >= 4 and to_add is None:
            if last_leaf is not None:
                last_leaf.n += l.n
            snail[1] = node(0)
            to_add = r
        else:
            last_leaf = r
    elif b_is_list:
        last_leaf,to_add,done = snail_explode(b,last_leaf=last_leaf,
                                                to_add=to_add,
                                                depth=depth+1)
        if done:
            return last_leaf,to_add,done
    else:
        if to_add is not None:
            b.n += to_add.n
            return last_leaf,to_add,True
        else:
            last_leaf = b

    return last_leaf,to_add,False

def simple_pair(snail):
    if type(snail) == type([]):
        a,b = snail
        return (type(a) != type([])) and (type(b) != type([]))
    return False

def snail_split(snail):
    a,b = snail
    a_is = type(a) == type([])
    b_is = type(b) == type([])

    if not a_is:
        if a.n >= 10:
            snail[0] = [node(a.n//2),node(math.ceil(a.n/2))]
            return True

    if a_is and snail_split(a):
        return True

    if not b_is:
        if b.n >= 10:
            snail[1] = [node(b.n//2),node(math.ceil(b.n/2))]
            return True
    
    elif b_is and snail_split(b):
        return True
    return False

def snail_reduce(snail):
    while True:
        _,_,done = snail_explode(snail)
        if done:
            continue
        if snail_split(snail):
            continue
        break

def snail_add(s1,s2):
    v = [s1,s2]
    snail_reduce(v)
    return v

def magnitude(snail):
    if type(snail) == type(node(0)):
        return snail.n
    return magnitude(snail[0])*3 + magnitude(snail[1])*2

result = None
for line in lines:
    snail = ast.literal_eval(line)
    nodify(snail)
    if result is None:
        result = snail
    else:
        result = snail_add(result,snail)

silver = magnitude(result)

m = float("-INF")
for a,b in itertools.combinations(lines,2):
    s_a = ast.literal_eval(a)
    nodify(s_a)
    s_b = ast.literal_eval(b)
    nodify(s_b)
    c = snail_add(s_a,s_b)
    m = max(m,magnitude(c))
    s_a = ast.literal_eval(a)
    nodify(s_a)
    s_b = ast.literal_eval(b)
    nodify(s_b)
    c = snail_add(s_b,s_a)
    m = max(m,magnitude(c))
gold = m

aoc.solution(1,silver)
aoc.solution(2,gold)
