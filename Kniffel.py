class Kniffel:
    def __init__(self):
        pass

    def RunSimulation(self, N: int) -> float:
        numKniffel = 0
        for i in range(N):
            isKniffel = self._SimulateTurn()
            if isKniffel:
                numKniffel += 1
        return numKniffel / N

    def _SimulateTurn(self) -> bool:
        pass