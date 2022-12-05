from dataclasses import dataclass

@dataclass
class Elf:

    id: int
    calories: list

    def getTotalCalories(self):
        self.totalcalories = sum(self.calories)

    def __repr__(self):
        return f"Elf {self.id} has {self.calories} totaling: {self.totalcalories}"
    
    def __lt__(self, obj):
        return ((self.totalcalories) < (obj.totalcalories))

    def __gt__(self, obj):
        return ((self.totalcalories) > (obj.totalcalories))

    def __le__(self, obj):
        return ((self.totalcalories) <= (obj.totalcalories))

    def __ge__(self, obj):
        return ((self.totalcalories) >= (obj.totalcalories))

    def __eq__(self, obj):
        return (self.totalcalories == obj.totalcalories)



if __name__ == "__main__":
    elves = list()
    elfid = 1
    with open("Problem1_input.txt", 'r') as infile:
        currentElfCals = []
        for line in infile.readlines():
            if len(line) == 1:
                elves.append(Elf(elfid, currentElfCals))
                elfid += 1
                currentElfCals = []
            else:
                currentElfCals.append(int(line.strip()))
    
    
    for elf in elves:
        elf.getTotalCalories()
        #if elf.totalcalories > highestcalories.totalcalories:
        #   highestcalories = elf
    
    highestcalories = sorted(elves, reverse=True)[0]

    print(repr(highestcalories))

    top3Elves = sorted(elves, reverse=True)[0:3]
    for elf in top3Elves:
        print(repr(elf))

    print(sum([x.totalcalories for x in top3Elves]))

    