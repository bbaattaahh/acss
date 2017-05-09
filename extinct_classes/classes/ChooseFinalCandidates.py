import numpy as np


class ChooseFinalCandidates:
    def __init__(self,
                 candidates,
                 tolerance):

        self.candidates = candidates
        self.tolerance = tolerance
        self.final_candidates = self.get_final_candidates()

    def get_final_candidates(self):
        final_candidates = []
        candidates_of_one_asparagus = self.get_groups()

        for group in candidates_of_one_asparagus:
            center_candidate = self.get_center_candidate_from_group(group)
            final_candidates.append(center_candidate)

        return final_candidates

    def get_groups(self):
        groups = []
        for candidate in self.candidates:
            unsaved = True

            for group in groups:
                if self.is_it_fit_to_group(candidate, group):
                    group.append(candidate)
                    unsaved = False
                    break

            if unsaved:
                groups.append([candidate])

        return groups

    def is_it_fit_to_group(self, candidate, group):
        for group_member in group:
            if self.euclidean_distance(candidate.top_left_corner(), group_member.top_left_corner()) < self.tolerance:
                return True

        return False

    @staticmethod
    def euclidean_distance(point1, point2):
        a = np.array(point1)
        b = np.array(point2)
        distance = np.linalg.norm(a - b)
        return distance

    @staticmethod
    def get_center_candidate_from_group(group):
        n = len(group)
        center = n // 2
        return group[center]
