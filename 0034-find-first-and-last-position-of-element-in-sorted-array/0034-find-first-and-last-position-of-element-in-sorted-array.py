class Solution:

    def bin_search(self, nums, target, find_first):
        l = 0
        r = len(nums) - 1
        ans = -1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                ans = mid

                if find_first:
                    r = mid - 1
                else:
                    l = mid + 1

            elif nums[mid] < target:
                l = mid + 1

            else:
                r = mid - 1

        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        first = self.bin_search(nums, target, True)
        last = self.bin_search(nums, target, False)

        return [first, last]