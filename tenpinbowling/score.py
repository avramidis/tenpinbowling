def checkStrike(frame):
    """Checks if the frame is a strike.

    Checks if the frame is a strike by checking if the first element of frame equals to 10.

    Args:
        frame: A list with the two elements that indicate the pins hit by the player.

    Returns:
        A boolean value were true means that the frame is a strike and false
        when the frame is not a strike.

    Raises:
        TypeError: An error occurred accessing the frame object.
    """

    if len(frame)!=2 or (type(frame) is not type([])):
        raise TypeError("Input must be a list with two elements")

    if frame[0] == 10:
        return True
    else:
        return False

def checkSpare(frame):
    """Checks if the frame is a spare.

    Checks if the frame is a spare by checking if sum of the elements of frame
    is 10 and the value of the first element is not 10.

    Args:
        frame: A list with the two elements that indicate the pins hit by the player.

    Returns:
        A boolean value were true means that the frame is a spare and false
        when the frame is not a strike.

    Raises:
        TypeError: An error occurred accessing the frame object.
    """

    if len(frame)!=2 or (type(frame) is not type([])):
        raise TypeError("Input must be a list with two elements")

    if frame[0] + frame[1] == 10 and frame[0] < 10:
        return True
    else:
        return False

def getScore(frames, numFrames):
    """Calculates the score of a 10 pin bolwing game for one player.

    TODO: explain the rules for the calculation of the score.

    Args:
        frames: A list with lists with two elements that indicate the pins hit by the player
        at each throw of the ball.
        numFrame: The lenght of the game in frames.

    Returns:
        A scalar with the score.

    Raises:
        TypeError: An error occurred accessing the bigtable.Table object.
    """

    score = 0
    for i in range(0, numFrames):
        score += sum(frames[i])
        if checkStrike(frames[i]):
            score += sum(frames[i+1])
            if checkStrike(frames[i+1]):
                score += frames[i+2][0]

        if checkSpare(frames[i]):
            score += frames[i+1][0]
    return score