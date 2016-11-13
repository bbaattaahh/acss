import unittest

from ChooseFinalCandidates import ChooseFinalCandidates
from Rectangle import Rectangle


class TestChooseFinalCandidates(unittest.TestCase):
    def test_final_candidates_no_candidates(self):
        # given
        candidates = []
        tolerance = 5
        expected_candidates = []

        # when
        choose_final_candidates = ChooseFinalCandidates(candidates, tolerance)
        actual_candidates = choose_final_candidates.final_candidates

        # that
        self.assertEqual(actual_candidates, expected_candidates)

    def test_final_candidates_two_candidates(self):
        # given
        asparagus_candidate1 = Rectangle(0, 0, 100, 10, -1)
        asparagus_candidate2 = Rectangle(1, 1, 100, 10, 0)
        asparagus_candidate3 = Rectangle(1, 10, 100, 10, 0)
        candidates = [asparagus_candidate1, asparagus_candidate2, asparagus_candidate3]
        tolerance = 5
        expected_candidates = [asparagus_candidate2, asparagus_candidate3]

        # when
        choose_final_candidates = ChooseFinalCandidates(candidates, tolerance)
        actual_candidates = choose_final_candidates.final_candidates

        # that
        self.assertEqual(actual_candidates, expected_candidates)

    def test_final_candidates_three_candidates(self):
        # given
        asparagus_candidate1_1 = Rectangle(0, 0, 100, 10, -1)
        asparagus_candidate1_2 = Rectangle(1, 1, 100, 10, 0)
        asparagus_candidate1_3 = Rectangle(1, 2, 100, 10, 1)
        asparagus_candidate2_1 = Rectangle(1, 10, 100, 10, 5)
        asparagus_candidate2_2 = Rectangle(1, 12, 100, 10, 6)
        asparagus_candidate3_1 = Rectangle(1, 22, 100, 10, 15)
        candidates = [asparagus_candidate1_1,
                      asparagus_candidate1_2,
                      asparagus_candidate1_3,
                      asparagus_candidate2_1,
                      asparagus_candidate2_2,
                      asparagus_candidate3_1]
        tolerance = 5

        expected_candidates = [asparagus_candidate1_2, asparagus_candidate2_2, asparagus_candidate3_1]

        # when
        choose_final_candidates = ChooseFinalCandidates(candidates, tolerance)
        actual_candidates = choose_final_candidates.final_candidates

        # that
        self.assertEqual(actual_candidates, expected_candidates)

    def test_get_groups_single_group(self):
        # given
        asparagus_candidate1 = Rectangle(0,0,100,10,-1)
        asparagus_candidate2 = Rectangle(1,1,100,10,0)
        candidates = [asparagus_candidate1, asparagus_candidate2]
        tolerance = 5
        expected_groups = [[asparagus_candidate1, asparagus_candidate2]]

        # when
        choose_final_candidates = ChooseFinalCandidates(candidates, tolerance)
        actual_groups = choose_final_candidates.get_groups()

        # that
        self.assertEqual(actual_groups, expected_groups)

    def test_get_groups_two_groups(self):
        # given
        asparagus_candidate1 = Rectangle(0, 0, 100, 10, -1)
        asparagus_candidate2 = Rectangle(1, 1, 100, 10, 0)
        asparagus_candidate3 = Rectangle(1, 10, 100, 10, 0)
        candidates = [asparagus_candidate1, asparagus_candidate2, asparagus_candidate3]
        tolerance = 5
        expected_groups = [[asparagus_candidate1, asparagus_candidate2],
                           [asparagus_candidate3]]

        # when
        choose_final_candidates = ChooseFinalCandidates(candidates, tolerance)
        actual_groups = choose_final_candidates.get_groups()

        # that
        self.assertEqual(actual_groups, expected_groups)

if __name__ == '__main__':
    unittest.main()