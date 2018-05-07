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
    score = 0
    for i in range(0, 3):
        score += sum(frames[i])
        if checkStrike(frames[i]):
            score += sum(frames[i+1])
            if checkStrike(frames[i+1]):
                score += frames[i+2][0]

        if checkSpare(frames[i]):
            score += frames[i+1][0]
    return score