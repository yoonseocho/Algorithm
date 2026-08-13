class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        l, r = 0, n-1
        start = -1
        
        # start 찾기
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                start = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        # end 찾기
        l, r = 0, n-1
        end = -1
        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                end = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return [start, end]