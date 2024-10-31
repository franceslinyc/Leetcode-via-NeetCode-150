class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        empty_set = {}

        for i, n in enumerate(nums): 

            diff = target - n 

            if diff in empty_set:

                return [i, empty_set[diff]]

            empty_set[n] = i
