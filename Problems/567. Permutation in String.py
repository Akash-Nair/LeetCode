class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False

        # Frequency arrays for 26 lowercase letters
        freq1 = [0] * 26
        freq2 = [0] * 26

        for i in range(l1):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1

        if freq1 == freq2:
            return True

        for i in range(l1, l2):
            freq2[ord(s2[i]) - ord('a')] += 1
            freq2[ord(s2[i - l1]) - ord('a')] -= 1
            if freq1 == freq2:
                return True

        return False
