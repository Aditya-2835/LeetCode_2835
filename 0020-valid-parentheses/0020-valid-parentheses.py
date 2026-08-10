class Solution:

  def isValid(self, s: str) -> bool:
    res = []

    for i in s:
      if i in ('(', '{', '['):
        res.append(i)
      else:
        if not res:
          return False

        top = res.pop()
        if (
            (i == ')' and top != '(')
            or (i == ']' and top != '[')
            or (i == '}' and top != '{')
        ):
          return False

    return len(res) == 0  