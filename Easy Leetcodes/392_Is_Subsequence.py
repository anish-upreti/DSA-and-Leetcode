class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # # one way to solve
        # s1 = list(s)
        # t1 = list(t)
        # r = []

        # for i in s:
        #     if i in t1:
        #         r.append(i)
        #         t1.remove(i)
        # r1 ="".join(r)
        # if r1==s:
        #     return True
        # else:
        #     return False

        # ***********************************************   

        # Another way to solve
        
        if len(s) == 0: return True
        if len(s) > len(t): return False

        i = 0
        for letter in t:
            if s[i] == letter:
                i += 1
            if i == len(s):
                return True
        return False


