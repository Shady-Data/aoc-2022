# Groups of 3
# the badge is the only item type carried by all three Elves. That is, if a group's badge is item type B, then all three Elves will have item type B somewhere in their rucksack, and at most two of the Elves will be carrying any other item type.
# The only way to tell which item type is the right one is by finding the one item type that is common between all three Elves in each group.

from dataclasses import dataclass
from queue import Queue
import string

lower_priorities = zip(string.ascii_lowercase, range(1,27))
upper_priorities = zip(string.ascii_uppercase, range(27,53))
Priorities = {i[0]: i[1] for i in lower_priorities}
Priorities.update({i[0]: i[1] for i in upper_priorities})


@dataclass
class Rucksack:
    compartment: str
    amount: int

    def splitcompartments(self):
        return ("".join([c for c in self.compartment[0:self.amount // 2]]), "".join([c for c in self.compartment[self.amount  // 2:]]))

    def itemInBothCompartments(self):
        compartment1 = self.splitcompartments()[0]
        compartment2 = self.splitcompartments()[1]
        return [x for x in compartment1 if x in compartment2][0]

    def __repr__(self):
        return f"Rucksack containing {self.compartment} has {self.amount} items with {self.splitcompartments()[0]} in one compartment and {self.splitcompartments()[1]}. Found Item {self.itemInBothCompartments()} in both."

@dataclass
class ElfGroup:
    Elf1Ruck: Rucksack
    Elf2Ruck: Rucksack
    Elf3Ruck: Rucksack
    badge: str
    badgepriority: int

    def __repr__(self):
        return f"Group badge {self.badge}: has a Priroty of {self.badgepriority} found in {self.Elf1Ruck.compartment}, {self.Elf2Ruck.compartment}, and {self.Elf3Ruck.compartment}"

def getcommonitemforgroup(group: list):
    if len(group) == 3:
        for c in string.ascii_letters:
            if c in group[0].compartment and c in group[1].compartment and c in group[2].compartment:
                return c
        print(f"\n\nNo common item found in: \n\t{group[0].compartment}, \n\t{group[1].compartment}, \n\t{group[2].compartment}")
        return

    print(f"\n\nIncorrect number in group: got {len(group)} instead of 3....How did this even get hit???\n")
    return 

def prepareGrouping(r1: Rucksack, r2: Rucksack, r3: Rucksack):
    badge = getcommonitemforgroup([r1, r2, r3])
    bpriority = Priorities[badge]
    return ElfGroup(r1, r2, r3, badge, bpriority)


if __name__ == "__main__":
    rucksacks = Queue(maxsize=3)
    elfGroups = []
    with open("Problem3_input.txt", 'r') as infile:
        for line in infile.readlines():
            rucksacks.put(Rucksack(line.strip(), len(line.strip())))
            if rucksacks.full():
                elfGroups.append(prepareGrouping(rucksacks.get(), rucksacks.get(), rucksacks.get()))


    # for ruck in rucksacks:
    #     print(repr(ruck))
    # print(", ".join([str(Priorities[r.itemInBothCompartments()]) for r in rucksacks]))
    # print(f"\n\nSum of all priorities of items in error is {sum([Priorities[r.itemInBothCompartments()] for r in rucksacks])}\n")

    # find groups of 3 for

    for group in elfGroups:
        print(repr(group))

    print(f"\n\nSum of all priorities of items in groups is {sum([g.badgepriority for g in elfGroups])}\n")