class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, val in enumerate(nums):
            hashmap[val] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement]!=i: #complement here is the key search in hashmap
                return [i, hashmap[complement]]
        