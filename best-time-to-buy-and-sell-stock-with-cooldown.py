class solution(object):
    def maxProfit(self, prices):
        '''
        type prices: list[int]
        rtype: int
        '''
        
        size = len(prices)
        if size < 2:
            return 0
        
        buys, sells = [None]*size, [None]*size
        sells[0], sells[1] = 0, max(0, prices[1] - prices[0])
        buys[0], buys[1] = -prices[0], max(-prices[0],-prices[1])
        
        for i in xrange(2,size):
            sells[i] = max(sells[i-1], buys[i-1] + prices[i])
            buys[i] = max(buys[i-1], sells[i-2] - prices[i])
            
        return sells[-1]
        
if __name__ == '__main__':
    result = solution().maxProfit([1,2,3,0,2])
    print result
