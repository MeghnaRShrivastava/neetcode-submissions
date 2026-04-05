class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #its 1-indexed
        left, right = 0, len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left +=1
            else:
                right -=1
            

        