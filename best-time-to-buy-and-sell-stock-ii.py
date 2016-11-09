class solution(object):
    '''
    type prices: list[int]
    rtype: int
    '''
    
    def maxProfit(self, prices):
        
        profit = 0
        for i in xrange(len(prices) - 1):
            profit += max(0, prices[i+1] - prices[i])
            
        return profit


if __name__ =='__main__':
    
    result = solution().maxProfit([3,5,66,3,4,5,45])
    print result
