class solution(object):
    """
    type num: str
    rtype: bool
    """
    
    def additiveNum(self, num):
        
        def addString(num1,num2):
            res, i, j, carry = [], len(num1) - 1, len(num2) - 1, 0
        
            while i >= 0 or j >= 0 or carry:
                if i >= 0:
                    carry += int(num1[i]);
                    i -= 1
                if j >= 0:
                    carry += int(num2[j]);
                    j -= 1
                res.append(str(carry % 10))
                carry = carry / 10
        
            return "".join(res[::-1])
        
        
        for i in xrange(1,len(num)):
            for j in xrange(i+1, len(num)):
                a1, a2 = num[0:i], num[i:j]
                if (len(a1) > 1 and a1[0] == '0') or (len(a2) > 1 and a2[0] == '0'):
                    continue
                
                sum = addString(a1, a2)
                cur = a1  + a2 + sum
                while len(cur) < len(num):
                    a1, a2, sum = a2, sum, addString(a2, sum)
                    cur += sum
                if cur == num:
                    return True
        
        return False
