from advent import *
import itertools

aoc = Session(2021,21)

quantum_dice = {}
for rolls in itertools.product((1,2,3),repeat=3):
    dist = sum(rolls)
    quantum_dice[dist] = quantum_dice.get(dist,0) + 1

memo = {}
def dp(p1,p2,p1_spot,p2_spot,p1_turn=False):
    if (p1,p2,p1_spot,p2_spot,p1_turn) in memo:
        return memo[(p1,p2,p1_spot,p2_spot,p1_turn)]
    elif p1 >= 21:
        return 1
    elif p2 >= 21:
        return 0

    result = 0
    for dist,weight in quantum_dice.items():
        if p1_turn:
            new_p1_spot = (p1_spot+dist) % 10
            new_p1 = p1 + new_p1_spot + 1
            result += weight*dp(new_p1,p2,new_p1_spot,p2_spot,not p1_turn)
        else:
            new_p2_spot = (p2_spot+dist) % 10
            new_p2 = p2 + new_p2_spot + 1
            result += weight*dp(p1,new_p2,p1_spot,new_p2_spot,not p1_turn)

    memo[(p1,p2,p1_spot,p2_spot,p1_turn)] = result
    return result



        
p1_spot,p2_spot = 7,6

p1_wins = dp(0,0,p1_spot,p2_spot,p1_turn=True)
p2_wins = dp(0,0,p2_spot,p1_spot,p1_turn=False)
gold = max(p1_wins,p2_wins)

turn = True
roll_count = 0
p1,p2 = 0,0
while p2 < 1000 and p1 < 1000:
    total_roll = 0
    
    total_roll += (roll_count % 100)+1
    roll_count += 1

    total_roll += (roll_count % 100)+1
    roll_count += 1

    total_roll += (roll_count % 100)+1
    roll_count += 1

    if turn:
        p1_spot = (total_roll + p1_spot) % 10
        p1 += p1_spot + 1
    else:
        p2_spot = (total_roll + p2_spot) % 10
        p2 += p2_spot + 1

    turn = not turn
silver = min(p1,p2) * roll_count

aoc.solution(1,silver)
aoc.solution(2,gold)
