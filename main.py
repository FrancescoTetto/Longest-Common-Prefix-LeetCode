class Solution(object):
    def longestCommonPrefix(self, strs):
        #Edge case: if the list is empty
        if not strs:
            return ""
        #This will be the first element
        prefix = strs[0]

        #Iterate the strs without first element
        for string in strs[1:]:
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                
                if not prefix:
                    return ""

        return prefix

solution = Solution()

print(solution.longestCommonPrefix(["flower","flow","flight"]))
