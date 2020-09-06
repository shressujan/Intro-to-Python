class Solution:
    """You are given an array of intervals - that is, an array of tuples (start, end).
     The array may not be sorted, and could contain overlapping intervals.
     Return another array where the overlapping intervals are merged."""
    @staticmethod
    def merge(intervals):

        sorted_intervals = sorted(intervals, key=lambda tup: tup[0], reverse=True)
        print(sorted_intervals)
        deleting_tuple = []
        for i in range(len(sorted_intervals) - 1):
            if sorted_intervals[i][0] > sorted_intervals[i + 1][0] and sorted_intervals[i][1] < sorted_intervals[i + 1][1]:
                deleting_tuple.append((sorted_intervals[i][0], sorted_intervals[i][1]))

        for i in deleting_tuple:
            sorted_intervals.remove(i)

        return sorted(sorted_intervals, key=lambda tup: tup[0])


if __name__ == '__main__':
    print(Solution().merge([(1, 3), (5, 8), (4, 10), (11, 20), (21, 25), (12, 17)]))
    # [(1, 3), (4, 10), (11, 20), (21, 25)]
