from advent import Session

aoc = Session(2021,3)

with aoc.fp() as f:
    lines = [int(line.strip(),2) for line in f.readlines()]

def mcb(arr,mask,lcb=False):
    return mask if (sum(e&mask==mask for e in arr) >= len(arr)/2)^lcb else 0

def filter_mcb(arr,bitwidth,lcb=False):
    mask = 1 << (bitwidth-1) 
    while len(arr) > 1:
        bit = mcb(arr,mask,lcb)
        arr = [e for e in arr if (e&mask) == bit]
        mask >>= 1
    return arr[0]

def get_bitwidth(arr):
    m = max(arr)
    mask,result = 1,0
    while mask < m:
        mask <<= 1
        result += 1
    return result

print(len(lines),"loaded")
bitwidth = get_bitwidth(lines)
silver = sum(mcb(lines,1 << i) for i in range(bitwidth))
silver *= ((1 << (bitwidth))-1) ^ silver
gold = filter_mcb(lines,bitwidth) * filter_mcb(lines,bitwidth,lcb=True)
print(silver,gold)

aoc.solution(1,silver)
aoc.solution(2,gold)
