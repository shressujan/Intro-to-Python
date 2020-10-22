class Solution:
    """A look-and-say sequence is defined as the integer sequence beginning with a single
     digit in which the next term is obtained by describing the previous term."""
    def __init__(self):
        pass

    @staticmethod
    def look_and_say(n):
        start_str = str(1)
        print(start_str)
        start_str = str(11)
        print(start_str)
        for i in range(n):
            count = 1
            new_start_str = ''
            j = 0
            for j in range(len(start_str) - 1):
                if start_str[j] == start_str[j+1]:
                    count += 1
                else:
                    new_start_str += str(count) + start_str[j]
                    count = 1
            new_start_str += str(count) + start_str[j+1]
            start_str = new_start_str
            print(start_str)


if __name__ == '__main__':
    Solution().look_and_say(10)
