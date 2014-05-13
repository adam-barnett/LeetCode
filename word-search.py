"""
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.
For example,
Given board =
[["ABCE"],["SFCS"],["ADEE"]]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
Problem found here:
http://oj.leetcode.com/problems/word-search/
"""



class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if len(board) == 0:
            return False
        explored = {}
        for y in xrange(len(board)):
            for x in xrange(len(board[y])):
                if board[y][x] == word[0]:
                    if self.depthSearch(board, word[1:], explored, (x,y)):
                        return True
        return False
    
    def depthSearch(self, board, word, explored, (x,y)):
        explored[(x,y)] = True
        if len(word) == 0:
            return True
        if y != 0 and board[y-1][x] == word[0] and (x,y-1) not in explored:
            if self.depthSearch(board, word[1:], explored, (x, y-1)):
                return True
        if x != 0 and board[y][x-1] == word[0] and (x-1,y) not in explored:
            if self.depthSearch(board, word[1:], explored, (x-1, y)):
                return True
        if y + 1 < len(board) and board[y+1][x] == word[0] and (x,y+1) not in explored:
            if self.depthSearch(board, word[1:], explored, (x, y+1)):
                return True
        if x + 1 < len(board[y]) and board[y][x+1] == word[0] and (x+1,y) not in explored:
            if self.depthSearch(board, word[1:], explored, (x+1, y)):
                return True
        del explored[(x,y)]


#test
sol = Solution()
board = []
word = 'word'
print 'for the board', board, 'and the word:', word,
print 'my method returns', sol.exist(board, word)
board.append(list(word))
print 'for the board', board, 'and the word:', word,
print 'my method returns', sol.exist(board, word)
board = [['w','r','d','o'],['o','r','r','w'],['r','d','r','w']]
print 'for the board', board, 'and the word:', word,
print 'my method returns', sol.exist(board, word)
board[0][0] = 'r'
print 'for the board', board, 'and the word:', word,
print 'my method returns', sol.exist(board, word)
