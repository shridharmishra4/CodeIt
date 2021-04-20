# . . Binary Search Tree
# . .               70
#          55                95     
#     13         68      80       102  
# Perform inoder traversal
count = 1
def solution(root,k) :
    global count
    
    if not root:
        return -1
     
    # if left tree returns -1, then no solution exists in the # left_tree
    left_tree = solution(root.l,k)
    
    # if solution exists in the left sub-tree
    # then return, otherwise continue on the processing
    if left_tree != -1:
        return left_tree
    
    
    if count == k:
        return root.v
    count += 1

    right_tree = solution(root.r, k)

    return right_tree


    

    

