class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def backtract(open_c,close_c,path):
            if len(path)==2*n:
                res.append("".join(path))
                return

            if open_c<n:
                path.append("(")
                backtract(open_c+1,close_c,path)
                path.pop()

            if close_c<open_c:
                path.append(")")
                backtract(open_c,close_c+1,path)
                path.pop()

        backtract(0,0,[])
        return res