from advent import Session

aoc = Session(2021,4)
silver = None
gold = None

def parse(line):
    return [int(p) for p in line.strip().split()]


class Bingo:
    def __init__(self,rows):
        self.row_counts = [0] * len(rows[0])
        self.col_counts = [0] * len(rows)
        self.finished = False
        self.unmarked_sum = 0

        self.height = len(rows)
        self.width = len(rows[0])

        self.d = {}  
        for x in range(len(rows[0])):
            for y in range(len(rows)):
                self.d[rows[y][x]] = (x,y)
                self.unmarked_sum += rows[y][x]

    def mark(self,n):
        if n in self.d:
            self.unmarked_sum -= n

            row,col = self.d[n]
            self.row_counts[col] += 1
            self.col_counts[row] += 1

            if self.row_counts[col] == self.height:
                self.finished = True
            if self.col_counts[row] == self.width:
                self.finished = True

cards = []
with aoc.fp() as f:
    sequence = [int(x) for x in f.readline().split(",")]
    f.readline()
    cards = []
    for group in f.read().split("\n\n"):
        rows = [parse(line.strip()) for line in group.split("\n") if line != ""]
        cards.append(Bingo(rows))


for call in sequence:
    next_cards = []
    for b in cards:
        b.mark(call)
        if b.finished:
            if silver is None:
                silver = b.unmarked_sum*call
            gold = b.unmarked_sum*call
        else:
            next_cards.append(b)
    cards = next_cards
    if len(cards) == 0:
        break

aoc.solution(1,silver)
aoc.solution(2,gold)
