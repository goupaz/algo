class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res =0 
        for elem in nums:
            res= res^elem
        return res
    
    # x^x = 0
    # x^0 = x
    # Order does not matter in XOR operation
    #Since XOR of element by itself is zero, every element that appears twice will cancel each out and the remaining one wil be our answer
    # Time Complexity = O(n), Space Complexity = O(1)