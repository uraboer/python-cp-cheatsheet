class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)

        if abs(S-T) > 1:
            return False

        return next(
            (
                s[i + 1 :] == t[i + 1 :]
                or s[i + 1 :] == t[i:]
                or s[i:] == t[i + 1 :]
                for i in range(min(S, T))
                if s[i] != t[i]
            ),
            abs(S - T) == 1,
        )