class Solution:
    def startStation(self, gas, cost):
        n = len(gas)
        sume = 0
        start = 0
        for i in range (2*n):
            ind = i % n
            sume = sume + gas[ind] - cost[ind]
            if sume < 0:
                sume = 0
                start = i + 1
            if (i - start == n):
                return start
        return -1
