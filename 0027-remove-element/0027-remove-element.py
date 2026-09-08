class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0
        count = 0
        for i in range (len(nums)):
            if (nums[i] != val):
                nums[p] = nums[i]
                count += 1
                p += 1
        return count