class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        answer = []

        for num1 in nums1:
            if num1 in nums2:
                answer.append(num1)
        
        return list(set(answer))