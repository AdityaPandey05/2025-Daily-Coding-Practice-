class Solution:
    def singleNum(self, arr):
        total_xor = 0
        for i in arr:
            total_xor ^= i

        setbitpos = ("0"*(32-len(bin(total_xor)[2:]))+bin(total_xor)[2:]).index('1')
        num1 = 0
        num2 = 0
        for i in arr:
            if ("0"*(32-len(bin(i)[2:]))+bin(i)[2:])[setbitpos] == '1':
                num1 ^= i
            else:
                num2 ^= i
        return sorted([num1, num2])
