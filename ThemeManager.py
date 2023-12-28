import json
import os

from Theme import Theme

class ThemeManager:

    def __init__(self):
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), 
            os.path.dirname(__file__)
        ))

        __themes__ = os.path.join(__location__, "themes")

        files = []
        w = os.walk(__themes__)

        for (dirpath, dirnames, filenames) in w:
            files.extend(filenames)
            break

        self.themes = []
        for file in files:
            with open(os.path.join(__themes__, file), "r") as read_file:
                data = json.load(read_file)

                name: str = file.split(".")[0]
                pattern: str = data["pattern"]
                colors: list = data["colors"]

                wait: float = data["wait"] if "wait" in data else None
                speed: float = data["speed"] if "speed" in data else None
                steps: int = data["steps"] if "steps" in data else None

                self.themes.append(Theme(name, pattern, colors, wait, speed, steps))


        for theme in self.themes:
            print(theme)
