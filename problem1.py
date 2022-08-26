class Solution:
    totalSum = 0
    def romanToInt(self, s: str) -> int:
        totalSum = 0
        romanNums = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        skip = False
        for i in range(len(s)):
            print(s[i])
            if not skip:
                if s[i] == "I" or s[i] == "X" or s[i] == "C":
                    try:
                        if romanNums[s[i]] < romanNums[s[i+1]]:
                            totalSum += romanNums[s[i+1]] - romanNums[s[i]]
                            skip = True
                        else:
                            totalSum += romanNums[s[i]]
                    except IndexError:
                        totalSum += romanNums[s[i]]
                else:
                    totalSum += romanNums[s[i]]
            else:
                skip = False
        return totalSum



