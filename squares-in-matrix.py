class Solution:
    def __init__(self):
        pass

    @staticmethod
    def count_squares(m, n):
        size = m * n
        minimum = m if m < n else n
        maximum = max(m, n)
        num_squares = size
        for i in range(2, minimum + 1):
            row_squares = 1 + minimum - i
            col_squares = 1 + maximum - i
            num_squares += row_squares * col_squares
        return num_squares


if __name__ == '__main__':
    print(Solution.count_squares(2, 2))
    print(Solution.count_squares(4, 3))
