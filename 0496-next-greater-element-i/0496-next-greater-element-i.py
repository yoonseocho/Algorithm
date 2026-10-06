class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        memo = {}
        stk = []

        for num in nums2:
            while stk and stk[-1] < num:
                memo[stk.pop()] = num
            stk.append(num)
        
        answer = []
        for num in nums1:
            if num in memo:
                answer.append(memo[num])
            else:
                answer.append(-1)
        
        return answer