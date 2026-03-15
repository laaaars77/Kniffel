from random import randint


class Kniffel:
    def __init__(self, numThrow: int = 3, numDice: int = 5, diceType: int = 6) -> None:
        self._numThrow = numThrow
        self._numDice = numDice
        self._diceType = diceType
        self._numProgress = 10

    def RunSimulation(self, N: int) -> float:
        numKniffel = 0
        indexFilter = N // self._numProgress
        for i in range(N):
            isKniffel = self._PlayKniffel()
            if isKniffel:
                numKniffel += 1
            if i % indexFilter == 0:
                print(f"Progress: {i / N * 100:.0f}%")
        print("Simulation complete.")
        return numKniffel / N

    def _PlayKniffel(self) -> bool:
        throw = [None] * self._numDice
        for i in range(0, self._numThrow - 1):
            throw = self._ThrowDice(throw)
            throw = self._ApplyStrategy(throw)
        # final throw
        throw = self._ThrowDice(throw)
        return all(die == throw[0] for die in throw)

    def _ThrowDice(self, throw: list[int | None]) -> list[int]:
        """
        Determine dice result for every None entry in list.
        Entries that are not None are preserved.
        """
        for i in range(len(throw)):
            if throw[i] is None:
                throw[i] = randint(1, self._diceType)
        return throw

    def _ApplyStrategy(self, throw: list[int]) -> list[int | None]:
        """
        Strategy: Keep the most common die and set the rest to None.
        """
        counter = [0] * self._diceType
        for die in throw:
            counter[die - 1] += 1
        argmax = counter.index(max(counter))
        return [die if die - 1 == argmax else None for die in throw]


if __name__ == '__main__':
    nThrow = 3
    nDice = 5
    facets = 6
    game = Kniffel(numThrow=nThrow, numDice=nDice, diceType=facets)

    numSimulation = 1e6
    probKniffel = game.RunSimulation(int(numSimulation))
    print(
        f'The probability to get a Kniffel result with '
        f'{nThrow} throws and {nDice} dice with {facets} faces is: 🥁 🥁 🥁\n'
    )
    print(f'{probKniffel * 100}%')
