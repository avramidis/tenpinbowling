import numpy

def checkStrike(frame):
    if frame[0] == 10:
        return True
    else:
        return False

def checkSpare(frame):
    if frame[0] + frame[1] == 10 and frame[0] < 10:
        return True
    else:
        return False

def getScore(frames):
    
    print(frames)
    score = 0
    
    for i in range(0, 3):
        score += sum(frames[i])
        if checkStrike(frames[i]):
            score += sum(frames[i+1])
            if checkStrike(frames[i+1]):
                score += frames[i+2][0]

        print(frames[i])

        # Calculate strike
        # if rolls[i-2] == 10:
        #     score += rolls[i]
        #     score += rolls[i-1]

        # Calculate spare
        # if rolls[i-2] + rolls[i-1] == 10:
        #     score += rolls[i]

        # print(score)

    return score