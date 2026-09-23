class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        dict = {}
        for i in range(len(s)):
            c = s[i].lower()
            if dict.get(c):
                dict[c] += 1
            else:
                dict[c] = 1
        for i in range(len(t)):
            c = t[i].lower()
            if dict.get(c):
                dict[c] -= 1
            
        
        print(set(dict.values()))
        return len(set(dict.values())) == 1 and 0 in set(dict.values())
        