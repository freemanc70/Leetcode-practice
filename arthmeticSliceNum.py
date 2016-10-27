class solution(object):
    def arthmeticSliceNum(self, num):
        """
        type num: List[int]
        rtype: int
        
        """
        result, i = 0, 0
        while i < len(num)-2:
            start = i
            while i <len(num)-2 and num[i] + num[i+2] == 2*num[i+1]:
                result += i - start + 1
                i += 1
            i += 1
        return result
        
        



if __name__ == '__main__':
    result = solution().arthmeticSliceNum([1,2,3,4,5])
    print result
