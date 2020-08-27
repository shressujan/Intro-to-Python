class Solution:
    """ You 2 integers n and m representing an n by m grid,
    determine the number of ways you can get from the top-left
    to the bottom-right of the matrix y going only right or down. """

    @staticmethod
    def num_ways(n, m):

        # Step 1
        node_to_edges = {}
        grid = []
        num = 0
        # Creating the grid for visibility
        for i in range(n):
            cols = []
            for j in range(m):
                num += 1
                cols.append(num)
            grid.append(cols)

        # Creating empty map
        for i in range(n):
            for j in range(m):
                node_to_edges[grid[i][j]] = []

        # Creating the map
        for i in range(n):
            for j in range(m):
                # last column and last row == last element in the grid
                if i == (n - 1) and j == (m - 1):
                    break
                # last column
                if j == (m - 1):
                    # Add down element
                    node_to_edges[grid[i][j]].append(grid[i + 1][j])
                    break
                # last row
                if i == (n - 1):
                    # Add right element
                    node_to_edges[grid[i][j]].append(grid[i][j + 1])
                    continue

                # Add right element
                node_to_edges[grid[i][j]].append(grid[i][j + 1])
                # Add down element
                node_to_edges[grid[i][j]].append(grid[i + 1][j])

        last_key = list(node_to_edges.keys())[-1]
        del node_to_edges[last_key]
        print(node_to_edges)

        # Step 2
        stack = [grid[0][0]]
        num_ways = 0
        visited = [grid[0][0]]
        destination = grid[n-1][m-1]
        print('Destination is', destination)
        path = []

        while stack:
            curr = stack.pop()
            path.append(curr)
            for node in node_to_edges[curr]:
                # if destination node found for current path, start with another prior possible path
                if node == destination:
                    num_ways += 1
                    while len(path) != 0 and visited[-1] == path[-1]:
                        visited.pop()
                        path.pop()
                    break

                stack.append(node)
                if node not in visited:
                    visited.append(node)

        return num_ways


if __name__ == '__main__':
    print('Total ways to get to the Destination is', Solution().num_ways(5, 5))
