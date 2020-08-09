class Solution:
    @staticmethod
    def isValid(string):
        valid_pair = {'(': ')',
                      '{': '}',
                      '[': ']'}

        if len(string) == 0:
            return True

        for i in range(len(string)):
            current_bracket = string[i]
            if current_bracket in valid_pair:
                closing_bracket = valid_pair[current_bracket]
                index_first_closing_bracket = string.find(closing_bracket)
                if index_first_closing_bracket == -1:
                    return False
                else:
                    string = string.replace(current_bracket, '', 1)
                    string = string.replace(closing_bracket, '', 1)
                    return Solution().isValid(string)

            else:
                return False


if __name__ == '__main__':
    print(Solution().isValid('([{}])()'))
    print(Solution().isValid('({[)]'))
    print(Solution().isValid('()(){(())'))
    print(Solution().isValid('[()]{}'))
