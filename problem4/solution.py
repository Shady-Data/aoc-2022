from dataclasses import dataclass

# Every section has a unique ID number, and each Elf is assigned a range of section IDs.
@dataclass
class CleaningSections:
    Elf1: str
    Elf2: str

    def fullyoverlap(self):
        sections1 = [x for x in range(int(self.Elf1.split('-')[0]), int(self.Elf1.split('-')[1]) + 1)] # break each elf's assigned sections into a list of integers to compare
        sections2 = [x for x in range(int(self.Elf2.split('-')[0]), int(self.Elf2.split('-')[1]) + 1)]
        if len(sections1) == len(sections2) or len(sections1) < len(sections2):  # find with list is longer to pass into the Boolean overlap check, if they are of equeal length, then the order passed into the function doesn't matter
            return self.overlap(sections1, sections2)
        elif len(sections1) > len(sections2): # Flip the order of the sections if Elf 1's list of sections is longer than Elf 2's list
            return self.overlap(sections2, sections1)

    def overlap(self, shortlist: list, longlist: list):
        for item in shortlist: # for each entry in the short list of section ids
            if item not in longlist: # if any item from the short list is outside of the longer list of section ids
                return False # Then both lists dont overlap completely
        return True # otherwise, if the iteration of the shortlist completes without hitting outside of the longer list, then they overlap

    def anyoverlap(self):
        sections1 = [x for x in range(int(self.Elf1.split('-')[0]), int(self.Elf1.split('-')[1]) + 1)] # break each elf's assigned sections into a list of integers to compare
        sections2 = [x for x in range(int(self.Elf2.split('-')[0]), int(self.Elf2.split('-')[1]) + 1)]
        if len(sections1) == len(sections2) or len(sections1) < len(sections2):  # find with list is longer to pass into the Boolean overlap check, if they are of equeal length, then the order passed into the function doesn't matter
            return self.checkoverlap(sections1, sections2)
        elif len(sections1) > len(sections2): # Flip the order of the sections if Elf 1's list of sections is longer than Elf 2's list
            return self.checkoverlap(sections2, sections1)

    def checkoverlap(self, shortlist: list, longlist: list):
        for item in shortlist: # for each entry in the short list of section ids
            if item in longlist: # if any item from the short list is in the longer list of section ids
                return True # Then both lists have an overlapping section
        return False # otherwise, if the iteration of the shortlist completes without hitting any of the longer list, then they don't overlap

if __name__ == '__main__':
    cleaningassignments = []
    with open('Problem4_input.txt', 'r') as infile:
        for line in infile.readlines():
            cleaningassignments.append(CleaningSections(line.split(',')[0].strip(), line.split(',')[1].strip()))

    fullyoverlapping = 0
    for assgn in cleaningassignments:
        if assgn.fullyoverlap():
            fullyoverlapping += 1

    print(f"{fullyoverlapping} assignements were found to be completely overlapping!")

    anyoverlapping = 0
    for assgn in cleaningassignments:
        if assgn.anyoverlap():
            anyoverlapping += 1

    print(f"\n{anyoverlapping} assignements were found to be completely overlapping!")