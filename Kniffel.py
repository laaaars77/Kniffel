from random import randint


class Kniffel:
    def __init__(self, numThrow: int = 3, numDice: int = 5, diceType: int = 6) -> None:
        self._numThrow = numThrow
        self._numDice = numDice
        self._diceType = diceType

    def RunSimulation(self, N: int) -> float:
        numKniffel = 0
        for i in range(N):
            isKniffel = self._PlayKniffel()
            if isKniffel:
                numKniffel += 1
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
                throw[i] = self._ThrowDie()
        return throw

    @staticmethod
    def _ThrowDie() -> int:
        return randint(1, 6)

    def _ApplyStrategy(self, throw: list[int]) -> list[int | None]:
        """
        Strategy: Keep the most common die and set the rest to None.
        """
        counter = [0] * self._diceType
        for die in throw:
            counter[die - 1] += 1
        argmax = counter.index(max(counter))
        return [die if argmax else None for die in throw]