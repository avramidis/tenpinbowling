import numpy

def getScore(rolls):
    
    #print(rolls)
    score = rolls[0]
    # print(score)
    score += rolls[1]
    # print(score)
    for i in range(2, len(rolls)):
        
        score += rolls[i]

        # Calculate strike
        if rolls[i-2] == 10:
            score += rolls[i]
            score += rolls[i-1]

        # Calculate spare
        # if rolls[i-2] + rolls[i-1] == 10:
        #     score += rolls[i]

        # print(score)

    return score