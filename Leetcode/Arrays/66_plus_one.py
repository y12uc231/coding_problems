class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[len(digits) - 1] += 1
        dig = [1]
        p = range(0, len(digits), 1)
        p.reverse()
        for i in p:
            if digits[i] / 10 == 0:
                return digits
            if digits[i] / 10 == 1 and i > 0:
                digits[i - 1] += 1
                digits[i] = 0
            if digits[i] / 10 == 1 and i == 0:
                digits[i] = 0
                dig.extend(digits)
                return dig
