# run at https://leetcode.com/problems/two-sum/submissions/1682122163/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # define the hashmap
        hashmap = {}
        # iterate over nums and make a map of values to inices
        for i in range(len(nums)) :
            hashmap[nums[i]] = i
        # then iterate and check if complement is in map (but complement =/= target) and return indices
        for i in range(len(nums)) :
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap.get(complement)]