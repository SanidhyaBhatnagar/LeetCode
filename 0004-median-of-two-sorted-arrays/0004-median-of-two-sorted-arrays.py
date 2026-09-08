class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge( nums1, nums2):
            i = 0
            j = 0
            result = []

            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    result.append(nums1[i])
                    i += 1
                else:
                    result.append(nums2[j])
                    j += 1    

            while i < len(nums1):
                result.append(nums1[i])
                i +=1

            while j < len(nums2):
                result.append(nums2[j])
                j += 1

            return result

        mergearr = merge(nums1, nums2)
        if (len(mergearr) % 2 == 1):
            n = len(mergearr)//2
            return(mergearr[n])
        else:
            n = len(mergearr)
            median = (mergearr[n//2 - 1]+ mergearr[n//2])/2
            return median
              