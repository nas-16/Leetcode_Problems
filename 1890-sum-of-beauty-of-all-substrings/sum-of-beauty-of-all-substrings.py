class Solution(object):
    def beautySum(self, s):
        total = 0
        for i in range(len(s)):
            freq = [0]*26
            max_freq = 0
            for j in range(i,len(s)):
                index = ord(s[j]) - ord('a')
                freq[index] += 1
                max_freq = max(freq[index],max_freq)
                min_freq = min(f for f in freq if f>0 )
                total += max_freq - min_freq
        return total

        