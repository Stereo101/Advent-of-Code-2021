import requests
import os

#Utility script to download input quickly or use a local copy if already downloaded

#set this to your aoc session cookie from browser dev tools
AOC_SESSION = os.environ["AOC_SESSION"]



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
        
    def check_solved(self,level):
        if level == 1 and os.path.exists("silver.flag"):
            return os.path.exists("silver.flag")
        elif level == 2 and os.path.exists("gold.flag"):
            return os.path.exists("gold.flag")
        return False

    def make_flag(self,level,answer):
        if level == 1:
            fp = open("silver.flag","w").write(str(answer))
        elif level == 2:
            fp = open("gold.flag","w").write(str(answer))


    def solution(self, level: int, answer) -> None:
        if answer is None:
            print(f"Skipping submission of level {level}, since the answer was None.")
            return
        elif level not in [1,2]:
            print(f"level must be either 1 (silver) or 2 (gold), instead got '{level}'")
            return
        elif self.check_solved(level):
            print(f"Level {level} is already solved.")
            return

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
