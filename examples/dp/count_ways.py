m,n=2,3  # This should be made global 
mem = {} # dictionary

def countways(x,y):
  # base case - 1
  if x==m-1 and y==n-1:
    return 1 
		
  key = str(x)+ "_" + str(y)
  a,b = 0,0
  

	# How to check key in a dictionary
  if key in mem:
    return mem[key]
  
  if x+1<m and y<n:
    a = countways(x+1,y)
  

  if x<m and y+1<n:
    b = countways(x,y+1)
  mem[key] = a+b
  
  return(mem[key])

def countways2(x, y, m, n):
	# base case - 1
  if x==m-1 and y==n-1:
    return 1 
  
  if x>=m or y>=n:
    return 0
  
  key = str(x)+ "_" + str(y)
  
  if key in mem:
    return mem[key]

  mem[key] = countways2(x+1,y,m,n)+ countways2(x,y+1,m,n)
  return mem[key]