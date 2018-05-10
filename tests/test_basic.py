import unittest
import sys
sys.path.append('..')
import tenpinbowling.score

class TestScoreMethod(unittest.TestCase):
    
    def test_simple_getScore(self):
        frames = [[4, 3], [5, 4], [4, 4]]
        score = tenpinbowling.score.getScore(frames,3)
        self.assertEqual(24, score)

    def test_strike_getScore(self):
        frames = [[10], [6, 3], [3, 2]]
        score = tenpinbowling.score.getScore(frames,3)
        self.assertEqual(33, score)

        frames = [[6, 3], [10], [5, 4]]
        score = tenpinbowling.score.getScore(frames,3)
        self.assertEqual(37, score)

        frames = [[10], [10], [4, 5]]
        score = tenpinbowling.score.getScore(frames,3)
        self.assertEqual(52, score)

        frames = [[3, 3], [4, 5], [10, 10, 10]]
        score = tenpinbowling.score.getScore(frames,3)
        self.assertEqual(45, score)

        frames = [[10], [10], [10, 10, 10]]
        score = tenpinbowling.score.getScore(frames,3)
        self.assertEqual(90, score)

    def test_spare_getScore(self):
        frames = [[4, 6], [6, 3], [3, 2]]
        score = tenpinbowling.score.getScore(frames,3)
        self.assertEqual(30, score)

        frames = [[4, 6], [6, 3], [4, 6, 5]]
        score = tenpinbowling.score.getScore(frames,3)
        self.assertEqual(40, score)
        
if __name__ == '__main__':
    unittest.main()