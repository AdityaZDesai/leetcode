class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        test cases::::

        Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

        """
        #have the current character
    	#have the current character counter
        # once the string is complied, then iterate through the string and replace input array, returns the len of the string.  
        #THIS A STUPID AND DISGUSTING PROBLEM WTFFFF

        current_char = "3"
        char_counter = 1
        s = ""
        prev_char = chars[0] 
        for i in range(1, len(chars)): 
            print(prev_char, char_counter, chars[i])
            if chars[i] == prev_char:
                char_counter += 1
            else:
                if char_counter == 1:
                    s += prev_char
                    prev_char = chars[i]
                    char_counter = 1

                else:
                    s += prev_char + str(char_counter)
                    prev_char = chars[i]
                    char_counter = 1
        if char_counter == 1:
            s += prev_char
        else:
            s += prev_char + str(char_counter)
            prev_char = chars[i]
            char_counter = 1
        for index, char in enumerate(s):
            if len(chars) > index:
                chars[index] = char
            else:
                chars.append(char)

        return len(s), chars, s 
sol = Solution()
print(sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
        