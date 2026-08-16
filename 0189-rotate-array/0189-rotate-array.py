class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        rotated_nums = nums[-k:] + nums[:-k]

        nums[:] = rotated_nums