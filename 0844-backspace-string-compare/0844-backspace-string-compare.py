class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            res=[]
            for char in string:
                if char!='#':
                    res.append(char)
                elif res:
                    res.pop()
            return "".join(res)

        return build(s)==build(t)