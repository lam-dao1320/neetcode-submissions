class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # return sorted(s.lower()) == sorted(t.lower())

        dict = {}
        for i in range(len(s)):
            c1 = s[i].lower()
            if dict.get(c1):
                dict[c1] += 1
            else:
                dict[c1] = 1

            c2 = t[i].lower()
            if dict.get(c2):
                dict[c2] -= 1
            else:
                dict[c2] = -1
            
        result = set(dict.values())

        return len(result) == 1 and 0 in result
        