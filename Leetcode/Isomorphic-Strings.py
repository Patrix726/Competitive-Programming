from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        equivalentChars = defaultdict(str)
        mapped = set()
        for s_, t_ in zip(s, t):
            if not equivalentChars[s_]:
                if t_ in mapped:
                    return False
                equivalentChars[s_] = t_
                mapped.add(t_)
            elif equivalentChars[s_] != t_:
                return False
        return True
