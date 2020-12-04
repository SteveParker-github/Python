class Character():
    """description of class"""

    distance = 27
    directions = {"up": [0, -distance],
                 "down": [0, distance],
                 "left": [-distance, 0],
                 "right": [distance, 0]}
    direction = "right"

    def __init__(self, mazeCanvas):
        pass
