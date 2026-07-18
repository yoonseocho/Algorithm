class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1[:] = set(nums1)
        nums2[:] = set(nums2)

        if len(nums1) >= len(nums2):
            nums1_sub_nums2 = [n1 for n1 in nums1 if n1 not in nums2]
            return [n1 for n1 in nums1 if n1 not in nums1_sub_nums2]
        else:
            nums2_sub_nums1 = [n2 for n2 in nums2 if n2 not in nums1]
            return [n2 for n2 in nums2 if n2 not in nums2_sub_nums1]