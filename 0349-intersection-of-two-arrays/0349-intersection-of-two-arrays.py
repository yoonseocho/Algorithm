class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list(set(nums1)).sort()
        list(set(nums2)).sort()

        answer = []

        for num1 in nums1:
            if num1 in nums2:
                answer.append(num1)
        
        return list(set(answer))