import tools.pattern.ColorPatterns as plugin

class PatternManager:

    def __init__(self, path):
        print("returned plugins: " + str(plugin.loadPatterns(path)))
    