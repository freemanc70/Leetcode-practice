class solution(object):
    def boardCount(self, board):
        '''
        type board: List[List[str]]
        rtype: int
        '''
        if not board or not board[0]:
            return 0
        
        count = 0
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                count += int(board[i][j] == 'X' and \
                            (i == 0 or board[i-1][j] != 'X') and \
                            (j == 0 or board[i][j-1] != 'X'))
        return count
        
        
if __name__ == '__main__':
    
    result = solution().boardCount([['X','.','.'], ['X','.','.'],['.','.','X']])
    print result
