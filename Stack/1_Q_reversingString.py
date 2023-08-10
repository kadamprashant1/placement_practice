class solution:
    def reverseString( self, s: str) -> str:
        stack =[]
        if not s:
            return stack
        for i in s:
            stack.append(i)
        ans =""
        while stack:
            ans +=stack.pop()

        return ans

if __name__ == "__main__":
    sol = solution()

    test_strings = [
        "hello",
        "world",
        "python",
        "openai",
    ]

    for test in test_strings:
        result = sol.reverseString(test)
        print(f"Input: {test}, Reversed: {result}")