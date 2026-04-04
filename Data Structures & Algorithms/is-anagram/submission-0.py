class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check the length
        if len(s) != len(t): 
            return False
        anagram = collections.Counter(s)
        for i in t:
            if anagram[i] <=0: 
               return False
            anagram[i] -=1
        return True

        