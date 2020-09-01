class Solution:
    """You are given a hash table where the key is a course code,
     and the value is a list of all the course codes that are prerequisites for the key.
     Return a valid ordering in which we can complete the courses.
     If no such ordering exists, return NULL."""

    @staticmethod
    def courses_to_take(course_to_prereqs):
        # Pre processing or trying to find the last class in the dictionary of courses
        lastClass = None
        only_pre_reqs = []
        for values in course_to_prereqs.values():
            for val in values:
                if val not in only_pre_reqs:
                    only_pre_reqs.append(val)

        for key in course_to_prereqs.keys():
            if key not in only_pre_reqs:
                lastClass = key
                break

        stack = [lastClass]
        visited = []
        path = []
        paths = []
        while stack:
            popped_item = stack.pop()
            path.append(popped_item)
            for pre_req in course_to_prereqs[popped_item]:
                # visited nodes
                if pre_req in visited:
                    visited.remove(pre_req)
                    visited.append(pre_req)
                else:
                    visited.append(pre_req)

                # checking if the leaf node
                if len(course_to_prereqs[pre_req]) == 0:
                    path.append(pre_req)
                    paths.append(path[:])
                    while len(path) != 0 and len(visited) != 0 and path[-1] == visited[-1]:
                        visited.pop()
                        path.pop()

                stack.append(pre_req)

        # Check which path is bigger
        courses_order = []
        for l in paths:
            if len(l) > len(courses_order):
                courses_order = l

        return courses_order


if __name__ == '__main__':
    courses = {
        'CSC300': ['CSC100', 'CSC200'],
        'CSC200': ['CSC100'],
        'CSC100': []
    }
    print(Solution().courses_to_take(courses))
    # ['CSC100', 'CSC200', 'CSC300']
