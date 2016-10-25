class Solution(object):
    def isValid(self, x, y, xmax, ymax, board):
        if (x >= 0 and y >= 0 and y < ymax and x < xmax and board[x][y] != 'X' and board[x][y] != '1'):
            return True
        return False;

    def bfs(self, x, y, board, val, xmax, ymax):
        if (self.isValid(x, y, xmax, ymax, board) == False):
            return board
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        p = [x, y]
        board[x][y] = val;
        q = [p]
        while (len(q) != 0):
            p = q[0]
            del q[0]
            x1 = p[0];
            y1 = p[1];

            for i in range(4):
                if (self.isValid(x1 + dx[i], y1 + dy[i], xmax, ymax, board) == True):
                    board[x1 + dx[i]][y1 + dy[i]] = val;
                    p = [x1 + dx[i], y1 + dy[i]]
                    q.append(p)

        return board;

    def solve(self, board):
        if (board == None or len(board) == 0):
            return;

        nrow = len(board);

        ncol = len(board[0]);

        i = 0
        i1 = nrow - 1
        for j in range(ncol):

            if (board[i][j] == 'O'):
                board = self.bfs(i, j, board, '1', nrow, ncol)

            if (board[i1][j] == 'O'):
                board = self.bfs(i1, j, board, '1', nrow, ncol)

        j = 0
        j1 = ncol - 1
        for i in range(1, nrow - 1):
            if (board[i][j] == 'O'):
                board = self.bfs(i, j, board, '1', nrow, ncol)

            if (board[i][j1] == 'O'):
                board = self.bfs(i, j1, board, '1', nrow, ncol)

        for i in range(1, nrow - 1):
            for j in range(1, ncol - 1):
                if (board[i][j] == 'O'):
                    board = self.bfs(i, j, board, 'X', nrow, ncol)

        for i in range(nrow):
            for j in range(ncol):
                if (board[i][j] == '1'):
                    board[i][j] = 'O'




