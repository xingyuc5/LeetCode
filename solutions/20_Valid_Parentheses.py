class Solution:
    def isValid(self, s: str) -> bool:

        # Use a list to serve as stack
        mapping = {"(": ")", "[": "]", "{": "}"}

        stack = []
        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                if stack == []:
                    return False
                if mapping[stack[-1]] == c:
                    stack.pop()
                else:
                    return False

        if stack == []:
            return True
        return False
