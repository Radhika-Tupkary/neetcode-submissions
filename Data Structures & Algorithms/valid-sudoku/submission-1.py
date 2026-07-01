class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                # k = (i//3) * 3 + j//3
                if i < 3:
                    if j < 3:
                        k= 0
                    elif j < 6:
                        k = 1
                    else:
                        k = 2
                elif i < 6:
                    if j < 3:
                        k= 3
                    elif j < 6:
                        k = 4
                    else:
                        k = 5
                else:
                    if j < 3:
                        k = 6
                    elif j < 6:
                        k = 7
                    else:
                        k = 8


                if (board[i][j] in rows[i]) or (board[i][j] in cols[j]) or (board[i][j] in squares[k]):
                    return False

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[k].add(board[i][j])

        print(rows)
        print(cols)
        print(squares)

        return True

        