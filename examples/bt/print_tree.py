# . . Binary Search Tree
# . .               70
#          55                95     
#     13         68      80       102  
soln = []
def solution(root) :
    if not root:
        return 
    
    if not (root.l and root.r):
        soln.append(root.v)
        print(soln)
        soln.pop()
        # all_paths.add(soln) 
    soln.append(root.v)
    solution(root.l)
    
    solution(root.r)
    soln.pop()
    

    return 




