    def is_bst_satisfied(self):
      leftMin = float('-inf')
      rightMax = float('inf')
      def helper(node, left, right) -> bool:

        if node is None:
          return True

        val = node.data
        if val <= left or val >= right:
          return False

        if helper(node.right, val, right) is False:
          return False
        return helper(node.left, left, val) is not False

      return helper(self.root, leftMin, rightMax)