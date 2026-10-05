class Solution(object):
    def romanToInt(self, s):
        dicti = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and dicti[s[i]] < dicti[s[i+1]]:
                total -= dicti[s[i]]
            else:
                total += dicti[s[i]]
        return total

#забыла подгрузить эту задачу