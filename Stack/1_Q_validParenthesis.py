class Solution:
    def isvalid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack

# Driver code
if __name__ == "__main__":
    sol = Solution()

    test_strings = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}",
        "{[()]}",
        "{[({})]}",
        "{[()]",
    ]

    for test in test_strings:
        result = sol.isvalid(test)
        print(f"Input: {test}, Valid: {result}")
