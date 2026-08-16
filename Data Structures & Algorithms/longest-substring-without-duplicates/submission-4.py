class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low = high = 0
        string = set()
        longest = 0
        while high < len(s):
            while s[high] in string:
                string.remove(s[low])
                low+=1
                    #print("pop element is {}".format(poped_ele))
            string.add(s[high])
            #print("string is {}".format(string))
            high += 1 
            longest = max (longest, len(string))

        return longest
            