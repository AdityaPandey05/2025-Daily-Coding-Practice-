class Solution:
    def longestStringChain(self, words):
        # Code here
        words.sort(key=len)
        word_dict={}
        
        for word in words:
            word_dict[word]=1
            for i in range(len(word)):
                predecessor=word[:i]+word[i+1:]
                if predecessor in word_dict:
                    word_dict[word]=max(word_dict[word],word_dict[predecessor]+1)
        return max(word_dict.values())
