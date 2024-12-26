class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        t1 = [0]*26
        t2 = [0]*26
        if len(s1)>len(s2): return False
        for i in s1:
            t1[ord(i)-ord('a')]+=1
        for i in range(len(s1)):
            t2[ord(s2[i])-ord('a')]+=1
        if t1 == t2:
            return True
        for i in range(len(s2)-len(s1)):
            t2[ord(s2[i])-ord('a')]-=1
            t2[ord(s2[i+len(s1)])-ord('a')]+=1
            if t1 == t2:
                return True
        return False