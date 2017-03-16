from graphics import *
import math


def roundUp(x):
    return int(math.ceil(x / 100.0)) * 100


def getInputs():
    acceptedColours = ["red", "green", "blue", "orange", "magenta", "cyan"]
    validCheck = False
    while validCheck == False:
        validCheck = True
        ##Data Collection
        # Printing infomation to the user on how to use the program
        print("")
        print("*----------------------------------*")
        print("5 = 5x5")
        print("7 = 7x7")
        print("9 = 9x9")
        # Getting data from user to generate the grid of squares
        gridType = eval(input("Please enter the grid size of the window: "))
        colourOne = input("Please enter the first colour: ").lower()
        colourTwo = input("Please enter the second colour: ").lower()
        colourThree = input("Please enter the third colour: ").lower()

        ##Validation
        # If a vairable not valid, it will change the vairable used to check if the loop should repeat again "validCheck" to False.
        # Each colour will checked alongside an array of acceptable colours
        if colourOne in acceptedColours:
            print("Colour one is accepted:")
        else:
            print("Colour one is an invalid colour")
            validCheck = False
        if colourTwo in acceptedColours:
            print("Colour two is accepted:")
        else:
            print("Colour two is an invalid colour")
            validCheck = False
        if colourThree in acceptedColours:
            print("Colour three is accepted:")
        else:
            print("Color three is an invalid colour")
            validCheck = False
        # Is the value entered an accepted grid type?
        if gridType == 5 or gridType == 7 or gridType == 9:
            print("The grid size is valid")
        else:
            print("The grid size is not valid")
            validCheck = False

    return gridType, colourOne, colourTwo, colourThree


def main():
    # Getting inputs
    gridType, colourOne, colourTwo, colourThree = getInputs()
    # Setting up the window
    winSize = gridType * 100
    win = GraphWin("770117 Coursework", winSize, winSize)
    # Drawing Grid
    drawGrid(win, gridType, colourOne, colourTwo, colourThree)
    swapPatterns(win, gridType, colourOne, colourTwo, colourThree)


def drawGrid(win, gridType, colourOne, colourTwo, colourThree):
    # Scales the size of the windows to the size of the grid the user entered.
    colours = [colourOne, colourTwo, colourThree]
    colourCount = 0
    xShift = 0
    yShift = 0
    # If a pattern is not at the end of the window, this will be true.
    while yShift != gridType:
        # Assigning what patterns are drawn where.
        if xShift == 0 or yShift >= gridType - 2:
            drawLinedSquares(win, xShift, yShift, colours[colourCount])
        else:
            drawGrowingSquare(win, xShift, yShift, colours[colourCount])

        colourCount = colourCount + 1
        xShift = xShift + 1

        # If the most recent colour has been called, the value used to assign the colour changes back to 0 to allow the first colour to be assigned to the next pattern to be drawn.
        if colourCount == 3:
            colourCount = 0
        # If a pattern has reached the end of the window, the X coordinate is set to 0 again, and the Y coordinate is set down a level.
        if xShift == gridType:
            yShift = yShift + 1
            xShift = 0


def drawGrowingSquare(win, xPos, yPos, colour):
    xPos = xPos * 100
    yPos = yPos * 100
    # This pattern is effectively few squares overlapping. These squares are drawn bigger for each interation of the loop.
    for i in range(10):
        scale = i * 10
        box = Rectangle(Point(0 + xPos, 100 + yPos), (Point(100 - scale + xPos, 0 + scale + yPos)))
        if i % 2 == 0:
            box.setFill(colour)
        else:
            box.setFill("white")
        box.draw(win)


def drawLinedSquares(win, xPos, yPos, colour):
    xPos = xPos * 100
    yPos = yPos * 100
    movDown = 0

    for i in range(5):
        for i2 in range(11):
            scaleBox = i2 * 10
            # This could be done with a single if condition, but this would cause the side of the pattern to "leak" into patterns ajacent to it. These extra if statements cut off the squares to ensure they stay in a 100x100 area.
            if i2 == 10:
                box = Rectangle(Point(-5 + scaleBox + xPos, 0 + movDown + yPos),
                                Point(0 + scaleBox + xPos, 10 + movDown + yPos))
            elif i2 == 0:
                box = Rectangle(Point(0 + scaleBox + xPos, 0 + movDown + yPos),
                                Point(5 + scaleBox + xPos, 10 + movDown + yPos))
            else:
                box = Rectangle(Point(-5 + scaleBox + xPos, 0 + movDown + yPos),
                                Point(5 + scaleBox + xPos, 10 + movDown + yPos))
            # i mod 2 will generate a 1 for an odd number, or 0 at even. This allows me to setup the patterns colour scheme.
            if i2 % 2 == 0:
                box.setFill(colour)
            else:
                box.setFill("white")
            box.draw(win)
        movDown = movDown + 10

        for i3 in range(5):
            scaleLongBox = i3 * 20

            longBox = Rectangle(Point(0 + scaleLongBox + xPos, 0 + movDown + yPos),
                                Point(20 + scaleLongBox + xPos, 10 + movDown + yPos))
            longBox.draw(win)
        movDown = movDown + 10


def clearPattern(win, pointXOne, pointYOne):
    whiteRectangle = Rectangle(Point(pointXOne * 100, pointYOne * 100),
                               Point(pointXOne * 100 + 100, pointYOne * 100 + 100))
    whiteRectangle.setFill("white")
    whiteRectangle.draw(win)


def swapPatterns(win, gridType, colourOne, colourTwo, colourThree):
    # This will be used in our while loop. I don't want the program to end, so this will stay false.
    exitProgram = False
    ## Assigning the array
    # A 2D array makes sense, having one part dedicated to the X chord and the other element dedicated to the Y chord.
    if gridType == 5:
        pattern = [["s", "l", "l", "l", "l"], ["s", "l", "l", "l", "l"], ["s", "l", "l", "l", "l"],
                   ["s", "s", "s", "s", "s"], ["s", "s", "s", "s", "s"]]
        colourPattern = [[1, 2, 3, 1, 2], [3, 1, 2, 3, 1], [2, 3, 1, 2, 3], [1, 2, 3, 1, 2], [3, 1, 2, 3, 1]]
    elif gridType == 7:
        pattern = [["s", "l", "l", "l", "l", "l", "l"], ["s", "l", "l", "l", "l", "l", "l"],
                   ["s", "l", "l", "l", "l", "l", "l"], ["s", "l", "l", "l", "l", "l", "l"],
                   ["s", "l", "l", "l", "l", "l", "l"], ["s", "s", "s", "s", "s", "s", "s"],
                   ["s", "s", "s", "s", "s", "s", "s"]]
        colourPattern = [[1, 2, 3, 1, 2, 3, 1], [2, 3, 1, 2, 3, 1, 2], [3, 1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3, 1],
                         [2, 3, 1, 2, 3, 1, 2], [3, 1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3, 1]]
    elif gridType == 9:
        pattern = [["s", "l", "l", "l", "l", "l", "l", "l", "l"], ["s", "l", "l", "l", "l", "l", "l", "l", "l"],
                   ["s", "l", "l", "l", "l", "l", "l", "l", "l"], ["s", "l", "l", "l", "l", "l", "l", "l", "l"],
                   ["s", "l", "l", "l", "l", "l", "l", "l", "l"], ["s", "l", "l", "l", "l", "l", "l", "l", "l"],
                   ["s", "l", "l", "l", "l", "l", "l", "l", "l"], ["s", "s", "s", "s", "s", "s", "s", "s", "s"],
                   ["s", "s", "s", "s", "s", "s", "s", "s", "s"]]
        colourPattern = [[1, 2, 3, 1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3, 1, 2, 3],
                         [1, 2, 3, 1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3, 1, 2, 3],
                         [1, 2, 3, 1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3, 1, 2, 3]]

    while exitProgram == False:
        # Getting the first selected point and converting it to a single unit for the grid. (1 == 100)
        mousPos = win.getMouse()
        pointXOne = int(roundUp(mousPos.getX()) / 100 - 1)
        pointYOne = int(roundUp(mousPos.getY()) / 100 - 1)
        # Drawing a black box around the selected pattern
        selector = Rectangle(Point(pointXOne * 100 + 100, pointYOne * 100 + 100),
                             Point(pointXOne * 100, pointYOne * 100))
        selector.setWidth(5)
        selector.draw(win)
        # Getting the second point.
        mousPos = win.getMouse()
        pointXTwo = int(roundUp(mousPos.getX()) / 100 - 1)
        pointYTwo = int(roundUp(mousPos.getY()) / 100 - 1)
        # Removing the pattern selector after the mouse has been clicked again.
        selector.undraw()
        # Covering the existing pattern with a white pattern, so when overwritten the pattern will draw as indended.
        clearPattern(win, pointXOne, pointYOne)
        clearPattern(win, pointXTwo, pointYTwo)

        ## Swapping Shapes
        # Holding the first object in a varable.
        holder = pattern[pointYOne][pointXOne]
        # Swapping the second patch into the first space.
        pattern[pointYOne][pointXOne] = pattern[pointYTwo][pointXTwo]
        # Swapping the stored patch into the second space.
        pattern[pointYTwo][pointXTwo] = holder

        ## Swapping Colours
        # Holding the first object in a varable.
        colourHolder = colourPattern[pointYOne][pointXOne]
        colourPattern[pointYOne][pointXOne] = colourPattern[pointYTwo][pointXTwo]
        colourPattern[pointYTwo][pointXTwo] = colourHolder
        # Swapping the second colour into the first space.
        if colourPattern[pointYOne][pointXOne] == 1:
            pointOneColour = colourOne
        elif colourPattern[pointYOne][pointXOne] == 2:
            pointOneColour = colourTwo
        elif colourPattern[pointYOne][pointXOne] == 3:
            pointOneColour = colourThree
        # Swapping the stored colour into the second space.
        if colourPattern[pointYTwo][pointXTwo] == 1:
            pointTwoColour = colourOne
        elif colourPattern[pointYTwo][pointXTwo] == 2:
            pointTwoColour = colourTwo
        elif colourPattern[pointYTwo][pointXTwo] == 3:
            pointTwoColour = colourThree
        ## Drawing swapped Shapes
        if pattern[pointYOne][pointXOne] == "s":
            drawLinedSquares(win, pointXOne, pointYOne, pointOneColour)
        elif pattern[pointYOne][pointXOne] == "l":
            drawGrowingSquare(win, pointXOne, pointYOne, pointOneColour)

        if pattern[pointYTwo][pointXTwo] == "s":
            drawLinedSquares(win, pointXTwo, pointYTwo, pointTwoColour)
        elif pattern[pointYTwo][pointXTwo] == "l":
            drawGrowingSquare(win, pointXTwo, pointYTwo, pointTwoColour)


main()



# todo add comments and add optomisasion

