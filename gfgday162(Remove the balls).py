class Solution:
  def findLength(self, color, radius):
        
    n=len(color)
    stack=[]
    ans=0
    for i in range(n):
        if (not stack) or color[i]!=stack[-1][0]:
            stack.append((color[i],radius[i]))
        else:
            if radius[i]!=stack[-1][1]:
                stack.append((color[i],radius[i]))
            else:
                stack.pop()
                ans+=2
    return n-ans
