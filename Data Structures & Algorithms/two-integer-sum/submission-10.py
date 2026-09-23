class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            j = target - i
            try:
                if i == j:
                    new_nums = nums.copy()
                    new_nums.remove(i)
                    index_j = new_nums.index(j) + 1
                else:
                    index_j = nums.index(j)
                return [nums.index(i), index_j]
                break
            except:
                pass