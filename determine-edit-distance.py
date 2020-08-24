class Solution:
    """Given two strings, determine the edit distance between them.
    The edit distance is defined as the minimum number of edits (insertion, deletion, or substitution)
    needed to change one string to the other. For example, "biting" and "sitting" have an edit distance
    of 2 (substitute b for s, and insert a t)."""

    @staticmethod
    def distance(s1, s2):
        edits = 0
        # Base case
        if len(s1) == 0:
            return len(s2)
        if len(s2) == 0:
            return len(s1)

        remaining1 = -1
        remaining2 = -1
        first1 = -1
        first2 = -1
        last1 = -1
        last2 = -1

        if len(s1) > 1:
            first1 = s1[0]
            last1 = s1[-1]
        else:
            remaining1 = s1[0]

        if len(s2) > 1:
            first2 = s2[0]
            last2 = s2[-1]
        else:
            remaining2 = s2[0]

        if first1 != -1 and first2 != -1:
            if first1 != first2:
                edits += 1
            s1 = s1[1:]
            s2 = s2[1:]

        if first1 != -1 and first2 != -1:
            if last1 != last2:
                edits += 1
            s1 = s1[:-1]
            s2 = s2[:-1]

        if remaining1 != -1 and remaining2 != -1:
            if remaining1 != remaining2:
                edits += 1
            s1 = ''
            s2 = ''

        if remaining1 != -1 and remaining2 == -1:
            if remaining1 != first2:
                edits += 1
            if remaining1 != last2:
                edits += 1
            s1 = ''

        if remaining1 == -1 and remaining2 != -1:
            if remaining2 != first1:
                edits += 1
            if remaining2 != last1:
                edits += 1
            s2 = ''

        return edits + Solution().distance(s1, s2)


if __name__ == '__main__':
    print(Solution().distance('biting', 'sitting'))
