class Solution:
    """ There are n people lined up, and each have a height represented as an integer.
     A murder has happened right in front of them, and only people who are taller than
     everyone in front of them are able to see what has happened. How many witnesses are there?
    Example:
    Input: [3, 6, 3, 4, 1]
    Output: 3
    Explanation: Only [6, 4, 1] were able to see in front of them."""

    @staticmethod
    def findTheWitnesses(heights):
        # First person can see because no one is blocking in front of him.
        numOfWitnesses = 1
        # First person also acts as a wall between the crime scene and remaining people on the list.
        heightOfWall = heights[-1]

        for i in (range(len(heights) - 1, 0, -1)):
            if heights[i] > heightOfWall:
                numOfWitnesses += 1
                heightOfWall = heights[i]  # new height for the wall

        return numOfWitnesses


if __name__ == '__main__':
    print(Solution().findTheWitnesses([3, 6, 3, 4, 1]))
    # 3
