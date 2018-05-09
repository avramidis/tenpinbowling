def checkStrike(frame):
    """Checks if the frame is a strike.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by big_table.  Silly things may happen if
    other_silly_variable is not None.

    Args:
        frame: A list with the two elements that indicate the pins hit by the player.

    Returns:
        A boolean value were true means that the frame is a strike and false
        when the frame is not a strike.

    Raises:
        TypeError: An error occurred accessing the bigtable.Table object.
    """

    if len(frame)!=2 or (type(frame) is not type([])):
        raise TypeError("Input must be a list with two elements")

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