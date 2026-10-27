class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max = 0
        listN = []
        sortedN = list(set(sorted(nums)))
        sortedN.sort()
        if len(sortedN) > 0:
            listN.append(sortedN[0])
            max = 1

        for i in range(1, len(sortedN)):
            if len(listN) == 0:
                listN.append(sortedN[i-1])
            if sortedN[i] - sortedN[i-1] == 1:
                listN.append(sortedN[i])
                if len(listN) > max:
                    max = len(listN)
            else:
                listN = []

        return max