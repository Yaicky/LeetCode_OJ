__author__ = 'Yaicky'

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1)==0 or len(nums2)==0:
            return []
        else:
            nums1 = set(nums1)
            nums2 = set(nums2)
            tmp = nums1 & nums2
            return list(tmp)