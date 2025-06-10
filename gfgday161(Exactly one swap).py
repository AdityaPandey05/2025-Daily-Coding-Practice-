class Solution:
  def countStrings(self, s): 
         
    n = len(s)                  # Total length of the string
    freq = [0] * 26             # Frequency array for each letter a-z

    # Step 1: Count frequency of each character
    for item in s:
        freq[ord(item) - ord("a")] += 1

    # Step 2: Total unordered pairs (nC2 = n*(n-1)//2)
    ans = (n * (n - 1) // 2)    

    flag = False                # To check if any character repeats

    # Step 3: Subtract pairs that are of the same character
    for val in freq:
        if val > 1:
            ans -= (val * (val - 1) // 2)
            flag = True

    # Step 4: If any character repeated, add 1
    if flag:
        ans += 1

    return ans
    
