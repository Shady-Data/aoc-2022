from dataclasses import dataclass
from itertools import zip_longest
import re

@dataclass
class Crates:
    filepath: str
    cratesStack: dict
    movelist: list
    countmoves = 0

    def Importfile(self):
        temp = []
        with open(self.filepath, 'r') as infile:
            for line in infile.readlines():
                if line.startswith('move'):
                    self.movelist.append(line)
                elif line.startswith('['):
                    temp.append(line)
        self.parseStartingStack(temp)

    def parseStartingStack(self, filelines: list):
        for line in filelines:
            for x in range(8):
                self.cratesStack[x+1].append(line[x*4:((x+1)*4)-1])
            self.cratesStack[9].append(line[32:-1])
        
        for key in self.cratesStack:
            while "   " in self.cratesStack[key]:
                self.cratesStack[key].remove("   ")
            self.cratesStack[key].reverse()

    def printCratesStacks(self):
        allstacks = zip_longest(self.cratesStack[1], self.cratesStack[2], self.cratesStack[3], self.cratesStack[4], self.cratesStack[5], self.cratesStack[6], self.cratesStack[7], self.cratesStack[8], self.cratesStack[9], fillvalue='   ')
        temp = []
        for stack in allstacks:
            temp.append(" ".join(stack))
        while len(temp) > 0:
            print(temp.pop())
        print(" 1   2   3   4   5   6   7   8   9 ")

    def printTopCratesLine(self):
        for stack in self.cratesStack:
            print(self.cratesStack[stack][-1][1], end="")
        print()


    def moveCrates(self):
        for line in self.movelist:
            if len(line) == 19:
                self.move9000(int(line[5]), int(line[12]), int(line[17]))
            elif len(line) == 20:
                self.move9000(int(line[5:7]), int(line[13]), int(line[18]))
            self.countmoves += 1

    def moveCratesv2(self):
        for line in self.movelist:
            if len(line) == 19:
                self.move9001(int(line[5]), int(line[12]), int(line[17]))
            elif len(line) == 20:
                self.move9001(int(line[5:7]), int(line[13]), int(line[18]))
            self.countmoves += 1

    def move9000(self, amount: int, fromStack: int, toStack: int):
        if amount > len(self.cratesStack[fromStack]):
            for _ in range(len(self.cratesStack[fromStack])):
                validation = re.match(r"\[[A-Z]\]", self.cratesStack[fromStack].pop())
                while not validation:
                    validation = re.match(r"\[[A-Z]\]", self.cratesStack[fromStack].pop())
                self.cratesStack[toStack].append(validation.string)
        else:
            for _ in range(amount):
                validation = re.match(r"\[[A-Z]\]", self.cratesStack[fromStack].pop())
                while not validation:
                    validation = re.match(r"\[[A-Z]\]", self.cratesStack[fromStack].pop())
                self.cratesStack[toStack].append(validation.string)

    def move9001(self, amount: int, fromStack: int, toStack: int):
        tempstack = self.cratesStack[fromStack][:-amount]
        crates = self.cratesStack[fromStack][-amount:]
        self.cratesStack[toStack].extend(crates)
        self.cratesStack[fromStack] = tempstack

if __name__ == "__main__":
    tempdict = {stack: [] for stack in range(1, 10)}
    templist = []
    cargo = Crates("Problem5_input.txt", tempdict, templist)
    cargo.Importfile()
    cargo.printCratesStacks()
    print("\tStarting Moves")
    print(f"{len(cargo.movelist)} Moves to complete")
    cargo.moveCratesv2()
    print(f"\t{cargo.countmoves} Moves completed!")
    cargo.printCratesStacks()
    # print(cargo.cratesStack)
    cargo.printTopCratesLine()
