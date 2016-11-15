class solution(object):
    def candy(self, ratings):
        '''
        type rating: list[int]
        rtype: list[int]
        '''
        
        candies = [1 for _ in xrange(len(ratings))]
        for i in xrange(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
            
        for i in reversed(xrange(1, len(ratings))):
            if ratings[i-1] > ratings[i] and candies[i-1] <=candies[i]:
                candies[i-1] = candies[i] + 1
    
        return sum(candies
        

if __name__ == "__main__":
    result = Solution().candy([1, 2, 3, 2, 3, 5, 2, 5])
    print result
