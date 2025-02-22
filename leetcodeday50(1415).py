class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy = []
        chars = ['a', 'b', 'c']

        def backtrack(path):
            if len(path) == n:
                happy.append("".join(path))
                return
            for c in chars:
                if not path or path[-1] != c:
                    backtrack(path + [c])

        backtrack([])
        return "" if k > len(happy) else happy[k - 1]