class solution(object):
    def addStrings(self,num1,num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(num1[i]);
                i -= 1
            if j >= 0:
                carry += int(num2[j]);
                j -= 1
            result.append(str(carry % 10))
            carry = carry / 10
        
        return "".join(result[::-1])


if __name__ == '__main__':
    result = solution().addStrings('180','10')
    print result
