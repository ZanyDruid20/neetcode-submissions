class Solution:
    def isValid(self, s: str) -> bool:
        Result = []
        pairs = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in '([{':
                Result.append(c)
            elif c in pairs:
                if not Result:
                    return False
                top = Result.pop()
                if top != pairs[c]:
                    return False
        return not Result
