import random

class Solution:
    #quicksort partition using lomuto method
    def partition(self, array, low, high):
        #find the pivot 
        pivot = random.randint(low,high) #find random index

        #move pivot to the end
        array[high], array[pivot] = array[pivot], array[high]
        pivot_value = array[high][1]


        i = low
        for j in range(low, high):
            if array[j][1] > pivot_value:
                array[i], array[j] = array[j], array[i]
                i +=1
            
        
        array[i], array[high] = array[high], array[i]

        return i

    def quickselect(self, array, low, high, k): #returning the keys with the top kth frequencies
        if low == high:
            return array[low]
        pi = self.partition(array, low, high)
        if k == pi:
            return
        elif k<pi:
            self.quickselect(array, low, pi-1, k)
        else:
            self.quickselect(array, pi+1, high, k)


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        dct = collections.Counter(nums) #key-value (num-freq)
        count_array = list(dct.items()) #convert it into array

        n = len(count_array) 
        self.quickselect(count_array, 0, n-1, k-1)

        return [count[0] for count in count_array[:k]] 
        