class Solution: 
    def chocolatePickup(self, mat): 
        # code here
        from functools import cache
        n = len(mat)
        end_step = 2 * n - 2
        
        @cache
        def solve(step=0, down1=0, down2=0):
            x1, y1 = down1, step - down1  # Robot 1
            x2, y2 = down2, step - down2  # Robot 2 aka return path
            if (not (0 <= x1 < n) or not (0 <= y1 < n)
                or not (0 <= x2 < n) or not (0 <= y2 < n)
                or mat[x1][y1] == -1 or mat[x2][y2] == -1
            ):
                return -1
            score = 0
            if step < end_step:
                # We haven't reached the final cell
                score = max(
                    solve(step + 1, down1, down2),
                    solve(step + 1, down1 + 1, down2),
                    solve(step + 1, down1, down2 + 1),
                    solve(step + 1, down1 + 1, down2 + 1)
                )
                if score == -1:
                    # No solution from this cell
                    return -1
            score += mat[x1][y1]
            if down1 != down2:
                # Second robot is in a different cell
                score += mat[x2][y2]
            return score
        
        score = solve()
        return score if score > -1 else 0
        