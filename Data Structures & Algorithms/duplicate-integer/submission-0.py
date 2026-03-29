class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)
        print( unique, nums)
        return len(unique) != len(nums)