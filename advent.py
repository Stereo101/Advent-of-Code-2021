import requests
import os

#Utility script to download input quickly or use a local copy if already downloaded

#set this to your aoc session cookie from browser dev tools
AOC_SESSION = os.environ["AOC_SESSION"]


def adj4(x,y,grid):
    for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
        ex = dx+x
        ey = dy+y
        if ex >= 0 and ex < len(grid[0]) and ey >= 0 and ey < len(grid):
            yield ex,ey

def adj8(x,y,grid):
    for dx,dy in ((-1,0),(1,0),(-1,1),(1,-1),(0,-1),(0,1),(-1,-1),(1,1)):
        ex = dx+x
        ey = dy+y
        if ex >= 0 and ex < len(grid[0]) and ey >= 0 and ey < len(grid):
            yield ex,ey

def iterate2d(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            yield x,y

def show2d(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            print(grid[y][x],end="")
        print()
    print()

class Session(requests.Session):
    def __init__(self, year: int, day: int) -> None:
        super().__init__()
        self.year = year
        self.day = day
        self.cookies = requests.cookies.cookiejar_from_dict({'session': AOC_SESSION})

    @property
    def url(self) -> str:
        return f'https://adventofcode.com/{self.year}/day/{self.day}'

    @property
    def fname(self) -> str:
        return f"day{self.day}.input"

    def problem(self) -> str:
        return self.get(f'{self.url}/input').text

    def fp(self,BIGBOY=False):
        if(not os.path.exists(self.fname)):
            with open(self.fname,"w") as f:
                f.write(self.problem())
        if(BIGBOY):
            return open("bigboy.txt")
        return open(self.fname,"r")
        
    def check_solved(self,level,answer):
        if level == 1:
            if os.path.exists("silver.flag"):
                expected = open("silver.flag","r").read()
                if str(answer) == expected:
                    print("Silver Solved! <matched silver.flag>",answer)
                else:
                    print(f"Silver didn't match flag. ans given:'{answer}' != flag:'{expected}'")
                return True
            return False
        elif level == 2:
            if os.path.exists("gold.flag"):
                expected = open("gold.flag","r").read()
                if str(answer) == expected:
                    print("Gold Solved! <matched gold.flag>",answer)
                else:
                    print(f"Gold didn't match flag. ans given:'{answer}' != flag:'{expected}'")
                return True
            return False
        return False

    def make_flag(self,level,answer):
        if level == 1:
            print("Silver solved!",answer)
            fp = open("silver.flag","w").write(str(answer))
        elif level == 2:
            print("Gold solved!",answer)
            fp = open("gold.flag","w").write(str(answer))


    def solution(self, level: int, answer) -> None:
        if answer is None:
            print(f"Skipping submission of level {level}, since the answer was None.")
            return
        elif level not in [1,2]:
            print(f"level must be either 1 (silver) or 2 (gold), instead got '{level}'")
            return
        elif self.check_solved(level,answer):
            return

        print(f"submitting... '{answer}'")
        r = self.post(f'{self.url}/answer', data={
            'level': level,
            'answer': answer
        })
        if 'That\'s the right answer!' in r.text:
            self.make_flag(level,answer)
            return
        lines = r.text.splitlines()
        for line in lines:
            if '<article>' in line:
                raise RuntimeError(line)
        raise RuntimeError(r.text)
