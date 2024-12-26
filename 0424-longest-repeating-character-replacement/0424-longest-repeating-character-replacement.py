class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = [0] * 26
        l,r = 0,0
        maxx = 0
        chars[ord(s[0])-ord('A')] = 1
        while r<len(s) and l<len(s):
            
            if max(chars) + k < (r-l+1):
                chars[ord(s[l])-ord('A')]-=1
                l+=1

            else:
                maxx = max(maxx,r-l+1)
                r+=1
                if (r<len(s)):
                    chars[ord(s[r])-ord('A')]+=1
        return maxx