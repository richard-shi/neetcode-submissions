class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validate Rows
        for row in board:
            seen = [x for x in row if x != '.']
            if len(seen) != len(set(seen)):
                return False

        # Validate Cols
        for colnum in range(len(board[0])):
            col = [board[rownum][colnum] for rownum in range(len(board))]
            seen = [x for x in col if x != '.']
            if len(seen) != len(set(seen)):
                return False

        # Validate 3x3 boxes
        boxes = [set() for _ in range(9)]
        for rownum in range(len(board)):
            for colnum in range(len(board[0])):
                box_index = (rownum // 3) * 3 + (colnum // 3)
                num = board[rownum][colnum]
                if num == '.':
                    continue
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)
        
        return True