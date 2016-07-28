__author__ = 'Yaicky'

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        tmp = int(a,2) + int(b,2)
        tmp = bin(tmp)[2:]
        return tmp