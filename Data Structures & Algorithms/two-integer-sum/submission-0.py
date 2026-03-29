class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain = {}
        ans = []
        for pos, num in enumerate(nums):
            # print( num, pos)
            if (target - num ) in remain:
                print( target - num, pos)
                ans =  [ remain[target - num] , pos ]
            else:
                remain[num] = pos
                print(target-num)
        return ans