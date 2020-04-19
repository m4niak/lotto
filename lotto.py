import random

class Lotek:
    randNumber = 0
    def randNumber(self):
        tempNumber = []
        oneNumber = random.randint(1, 49)
        tempNumber.append(oneNumber)
        twoNumber = random.randint(1, 49)
        tempNumber.append(twoNumber )
        threeNumber = random.randint(1, 49)
        tempNumber.append(threeNumber )
        fourNumber = random.randint(1, 49)
        tempNumber.append(fourNumber )
        fiveNumber = random.randint(1, 49)
        tempNumber.append(fiveNumber )
        sixNumber = random.randint(1, 49)
        tempNumber.append(sixNumber )
        tempNumber.sort()
        self.randNumber = tempNumber

program = Lotek()
program.randNumber()

print(program.randNumber)