from sokszog import Sokszog

class Haromszog(Sokszog):
    def __init__(self, csomopontok):
        self._Sokszog__oldalak = 3
        self.setCsomopontok(csomopontok)
