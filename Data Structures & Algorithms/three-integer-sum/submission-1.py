class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0: 
                break
            if i == 0 or nums[i-1]!=nums[i]: #condition to check that first value shouldn't be greater than zero and no duplicates
                self.twoSum(nums, i, res)
        return res


    def twoSum(self, nums, i:int, res: List[List[int]]):
        seen = set() #use set to store duplicate values.

        j = i+1
        while j<len(nums):
            complement = 0 - nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j+1<len(nums) and nums[j] == nums[j+1]: #increase the j pointer if consecutive j values
                    j +=1
            seen.add(nums[j])
            j +=1


        