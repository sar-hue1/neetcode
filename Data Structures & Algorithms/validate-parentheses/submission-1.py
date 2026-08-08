class Solution:
    def isValid(self, s: str) -> bool:
        stack_ = []

        for ch in s:

            if ch == "(" or ch == "[" or ch == "{":
                stack_.append(ch)

            else:
                if not stack_:
                    return False

                top = stack_.pop()

                if ch == ')' and top != '(':
                    return False

                if ch == ']' and top != '[':
                    return False

                if ch == '}' and top != '{':
                    return False

        return len(stack_) == 0
