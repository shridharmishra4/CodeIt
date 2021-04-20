
from examples.ds import TreeNode

# . . Binary Search Tree
# . .               70
#          55                95     
#     13         68      80       102  
root = TreeNode(70, TreeNode(55, TreeNode(13), TreeNode(68)), TreeNode(95, TreeNode(80), TreeNode(102)))

# -------------------------------------------------
# Done
# Prints the total number of way from source[0,0] in a grid to destination[m,n]
# Category : DP
# from examples import count_ways as cw
# print(cw.countways(0,0))
# print(cw.countways2(0,0,2,3))

# -------------------------------------------------
# Done
# Return the sum of all nodes in a tree
# Output : ?
# Category : Binary Tree
# from examples.bt import count_tree as ct
# print(ct.solution(root2))

# -------------------------------------------------

# Print all paths of the tree
# Done
# Output : {[70,55,13], [70,55,68], [70,95,80],[70,95,102]}
# Category : Binary Tree
# from examples.bt import print_tree as pt
# pt.solution(roo,t)

# -------------------------------------------------
# Not Done
# Return the kth smallest element in the bst
# Output : For k = 3, output = 68
# Category : Binary Tree
from examples.bt import kth_smallest as ks
print(ks.solution(root,5))