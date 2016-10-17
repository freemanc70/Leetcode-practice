class solution(object):
    def addBinary (self, a, b):
        result, temp, val = "", 0, 0
        for i in xrange(max(len(a),len(b))):
            val = temp
            if i < len(a):
                val += int(a[-(i+1)])
            if i < len(b):
                val += int(b[-(i+1)])
            temp, val = val / 2, val % 2
            result += str(val)
        if temp:
            result += str(temp)
        return (result[::-1])
    
if __name__ == '__main__':
    result = solution().addBinary('101', '1')
    print result
