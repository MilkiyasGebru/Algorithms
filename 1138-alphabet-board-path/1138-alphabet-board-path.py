class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        words = {}
        stack = []
        for i in range(26):
            col = i%5
            row = i//5
            words[i] = (row,col)
        answer = 0
        cur_row,cur_col = (0,0)
        for character in target:
            row,col = words[ord(character)-ord("a")]
            if row == 5:
                stack.extend(["L" if cur_col > col else "R" for _ in range(abs(cur_col-col))])
                stack.extend(["D" for _ in range(abs(cur_row-row))])
            else:
                stack.extend(["U" if row < cur_row else "D" for _ in range(abs(cur_row-row))])
                stack.extend(["L" if cur_col > col else "R" for _ in range(abs(cur_col-col))])
            stack.append("!")
            cur_row,cur_col = row,col
        return "".join(stack)
            