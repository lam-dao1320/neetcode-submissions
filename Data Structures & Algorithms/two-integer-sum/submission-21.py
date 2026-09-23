class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            if indices.get(n):
                indices[n].append(i)
            else:
                indices[n] = [i]

        for i, n in enumerate(nums):
            diff = target - n
            if indices.get(diff):
                index = indices[diff].copy()
                if i in indices[diff] and len(index) > 1:
                    index.remove(i)

                if i != index[0]:
                    return [i, index[0]]
        return []