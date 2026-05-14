class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stk = []
        brckt_map = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in brckt_map:
                if stk and stk[-1] == brckt_map[ch]:
                    stk.pop()
                else:
                    return False # we got a mismatch ORr stack is empty when it shouldn't be
            else:
                stk.append(ch)

        return len(stk) == 0