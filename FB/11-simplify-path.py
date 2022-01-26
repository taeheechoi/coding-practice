https://leetcode.com/problems/simplify-path/
# Example 1:

# Input: path = "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory name.
# Example 2:

# Input: path = "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
# Example 3:

# Input: path = "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.



class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        print(path) # "/home/" ['', 'home', '']
        skip = [".", "..", ""]
        result = []
        for p in path:
            if p not in skip:
                result.append(p)
            if p == '..' and result:
                result.pop() # "/a/./b/../../c/" -> "/c"
        print(result)
        return "/" + "/".join(result)
        
        