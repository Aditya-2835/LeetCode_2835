class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def multiply(set1: set, set2: set) -> set:
            return {s1 + s2 for s1 in set1 for s2 in set2}

        stack = []
        cur_set = set() 
        operand_stack = [set()]

        for char in expression:
            if char.isalpha():
                if not operand_stack[-1]:
                    operand_stack[-1] = {char}
                else:
                    operand_stack[-1] = multiply(operand_stack[-1], {char})

            elif char == ',':
                cur_set.update(operand_stack.pop())
                operand_stack.append(set())

            elif char == '{':
                stack.append((cur_set, operand_stack))
                cur_set = set()
                operand_stack = [set()]

            elif char == '}':
                cur_set.update(operand_stack.pop())
                inner_res = cur_set

                prev_cur_set, operand_stack = stack.pop()
                cur_set = prev_cur_set

                if not operand_stack[-1]:
                    operand_stack[-1] = inner_res
                else:
                    operand_stack[-1] = multiply(operand_stack[-1], inner_res)

        cur_set.update(operand_stack.pop())
        return sorted(list(cur_set))