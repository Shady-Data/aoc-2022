from dataclasses import dataclass

@dataclass
class Guide:
    filepath: str
    decoder = {
        'A': 'Rock',
        'B': 'Paper',
        'C': 'Scissors',
        'X': 'Rock',
        'Y': 'Paper',
        'Z': 'Scissors'
    }
    fixeddecoder = {
        'A': 'Rock',
        'B': 'Paper',
        'C': 'Scissors',
        'X': 'Lose',
        'Y': 'Draw',
        'Z': 'Win'        
    }

    def ingestguide(self):
        with open(self.filepath, 'r') as infile:
            self.decodedguide = []
            for line in infile.readlines():
                self.decodedguide.append((self.decoder[line.split(' ')[0].strip()], self.decoder[line.split(' ')[1].strip()]))

    def fixedingestguide(self):
        with open(self.filepath, 'r') as infile:
            self.decodedguide = []
            for line in infile.readlines():
                self.decodedguide.append((self.fixeddecoder[line.split(' ')[0].strip()], self.fixeddecoder[line.split(' ')[1].strip()]))

    def getprediction(self, gameEntryNum: int):
        if gameEntryNum > len(self.decodedguide):
            return None
        return RPS(self.decodedguide[gameEntryNum - 1][0], self.decodedguide[gameEntryNum - 1][1]).outcome()

    def scoreAllPredictions(self):
        score = 0
        for entry in self.decodedguide:
            score += RPS(entry[0], entry[1]).outcome()
        return score

    

@dataclass
class RPS:
    scoring = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3,
        "Lose" : 0,
        "Draw" : 3,
        "Win": 6
    }
    opponent: str
    desiredoutcome: str
    # selection: str

    def getSelectionforDesiredOutcome(self):
        if self.desiredoutcome == 'Draw':
            return self.opponent
        elif self.desiredoutcome == 'Lose':
            if self.opponent == 'Rock':
                return 'Scissors'
            if self.opponent == 'Scissors':
                return 'Paper'
            if self.opponent == 'Paper':
                return 'Rock'
        elif self.desiredoutcome == 'Win':
            if self.opponent == 'Rock':
                return 'Paper'
            if self.opponent == 'Scissors':
                return 'Rock'
            if self.opponent == 'Paper':
                return 'Scissors'


    def outcome(self):
        selection = self.getSelectionforDesiredOutcome()
        if self.opponent == selection:
            return self.scoring[selection] + self.scoring['Draw']
        elif (self.opponent == 'Rock' and selection == 'Scissors') or (self.opponent == 'Scissors' and selection == 'Paper') or (self.opponent == 'Paper' and selection == 'Rock'):
            return self.scoring[selection] + self.scoring['Lose']
        elif (self.opponent == 'Rock' and selection == 'Paper') or (self.opponent == 'Scissors' and selection == 'Rock') or (self.opponent == 'Paper' and selection == 'Scissors'):
            return self.scoring[selection] + self.scoring['Win']

if __name__ == '__main__':
    StrategeyGuide = Guide("Problem2_input.txt")
    StrategeyGuide.fixedingestguide()
    print(StrategeyGuide.scoreAllPredictions())