"""
Button class helper script
makes live buttons a thing
add new elif statement every time you make a new live button
"""

def buttAction(buttnumber):
    '''finds which button was pressed and does some action for that button'''
    if buttnumber == 0:
        '''NEW GAME button was pressed'''
        print "new game!" # standin for reset game state
    elif buttnumber == 1:
        '''PAUSE button was pressed'''
        print "game paused" # standin for pause game... only needed if we count time
