class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            sortedS = ''.join(sorted(s))
            if result.get(sortedS):
                result[sortedS].append(s)
            else:
                result[sortedS] = [s]

        # print(result)
        return list(result.values())
            
