#User function Template for python3

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        st = []
        for e in x:
            if e in '([{':
                st.append(e)
            else:
                if not st or st.pop()+e not in ["()", "[]", "{}"]:
                    return False
        return len(st) == 0
        # code here
