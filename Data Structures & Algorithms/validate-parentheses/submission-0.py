class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        open_brackets = []
        for c in s:
            if c in brackets:
                open_brackets.append(c)
            else:
                if len(open_brackets) == 0:
                    return False

                last_open_bracket = open_brackets.pop()
                if c != brackets[last_open_bracket]:
                    return False
                
        return not bool(open_brackets)

        