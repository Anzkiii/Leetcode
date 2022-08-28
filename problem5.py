class Solution:
    def longestCommonPrefix(self, strs: list):
        currentPrefix = []
        outputPrefix = []
        incrementValue = 0
        endStr = ""
        while incrementValue - 1 <= len(strs):
            try:
                currentPrefix = [strs[x][incrementValue] for x in range(len(strs))]
            except IndexError:
                currentPrefix = [""]
            if len(set(currentPrefix)) == 1:
                outputPrefix.append(currentPrefix)
                incrementValue += 1
            else:
                for i in range(len(outputPrefix)):
                    endStr += outputPrefix[i][0]
                    continue
                return endStr
        for i in range(len(outputPrefix)):
            endStr += outputPrefix[i][0]
            continue
        return endStr

print(Solution().longestCommonPrefix(["flower", "flower", "flower", "flower"]))

