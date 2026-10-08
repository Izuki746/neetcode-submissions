class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        newS = sorted(s)
        newT = sorted(t)
        if len(newS) > len(newT):
            return False
        if len(newT) > len(newS):
            return False

        for i in range(len(newS)):
            if newS[i]==newT[i]:
                continue
            else:
                return False
        return True