class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        self.count = 0

        def dfs(node):
            if node is None:
                return 0, 0

            suml, countl = dfs(node.left)
            sumr, countr = dfs(node.right)

            total_sum = suml + sumr + node.val
            total_count = countl + countr + 1

            avg = total_sum // total_count

            if avg == node.val:
                self.count += 1

            return total_sum, total_count

        dfs(root)

        return self.count