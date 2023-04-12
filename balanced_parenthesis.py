class Solution:
	# @param A : string
	# @return an integer
    def solve(self, A):
        stack = []
        for ch in A:
            if ch == "{" or ch == "[" or ch == "(" or len(stack) == 0:
                stack.append(ch)
            else:
                if ch == "}" and stack[-1] == "{":
                    stack.pop()
               
                if ch == "]" and stack[-1] == "[":
                    stack.pop()

                if ch == ")" and stack[-1] == "(":
                    stack.pop()

        if len(stack) != 0:
            return 0
        else:
            return 1

sol=Solution()
print(sol.solve("{[]}()"))
