class Theme:
    def __init__(self, name: str, pattern: str, colors: list, wait: float, speed: float, steps: int):
        self.name = name
        self.pattern = pattern
        self.colors = colors

        self.wait = wait if wait != None else 0.3
        self.speed = speed if speed != None else 1.0
        self.steps = steps if steps != None else 20
        

    def __str__(self):
        return self.name + ": " + self.pattern + ", " + str(self.colors)