class Character():
    """description of class"""
    WALLS = ["n", "e", "w", "s", "N", "E", "W", "S", "^", "<", "V", ">", "|", "-"]
    distance = 27
    directions = {"up": [0, -distance],
                 "down": [0, distance],
                 "left": [-distance, 0],
                 "right": [distance, 0]}
    direction = "right"
    position = [0, 0]

    def __init__(self, mazeCanvas):
        pass
