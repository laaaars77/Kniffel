from unittest.mock import patch
from Kniffel import Kniffel


class TestKniffel:

    def test_ThrowDice(self):
        game = Kniffel()
        with patch('Kniffel.randint') as mock_throw:
            mock_throw.return_value = 3
            throw = [1, None, 2, None, None]
            result = game._ThrowDice(throw)
            assert result == [1, 3, 2, 3, 3]

    def test_ApplyStrategy(self):
        game = Kniffel()
        # Test case where most common is 2
        throw = [1, 2, 2, 3, 2]
        result = game._ApplyStrategy(throw)
        assert result == [None, 2, 2, None, 2]

        # Test case where most common is 1
        throw = [1, 1, 2, 3, 4]
        result = game._ApplyStrategy(throw)
        assert result == [1, 1, None, None, None]

        # Test tie: if multiple max, index takes the first
        throw = [1, 2, 1, 2]
        result = game._ApplyStrategy(throw)
        assert result == [1, None, 1, None]

    def test_PlayKniffel(self):
        k = Kniffel(numThrow=2, numDice=3)  # Small for testing
        with (
            patch.object(k, '_ThrowDice') as mock_throw_dice,
            patch.object(k, '_ApplyStrategy') as mock_apply
        ):
            # Simulate throws
            mock_throw_dice.side_effect = [
                [1, 2, 3],  # First throw
                [1, 1, 1]   # Final throw
            ]
            mock_apply.return_value = [1, None, None]  # After first throw, keep 1
            result = k._PlayKniffel()
            assert result == True  # All same

            # Another case: not all same
            mock_throw_dice.side_effect = [
                [1, 2, 3],
                [1, 1, 2]
            ]
            result = k._PlayKniffel()
            assert result == False
