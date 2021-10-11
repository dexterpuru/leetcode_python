class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        i, j = 0, 0
        maxi = 0
        while j<len(s):
            if s[j] in count:
                count[s[j]]+=1
            else:
                count[s[j]]=1
            while count[s[j]]>1:
                count[s[i]]-=1
                i+=1
            maxi = max(maxi,j-i+1)
            j+=1
        return maxi