# return sum of all nodes

def solution(root):

    if not root:
        return 0
    
    if not (root.l and root.r):
        return root.v 

    a = solution(root.l)
    b = solution(root.r)

    return a+b+ root.v
