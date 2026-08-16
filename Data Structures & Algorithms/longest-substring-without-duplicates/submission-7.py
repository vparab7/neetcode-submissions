class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # low = high = 0
        # string = set()
        # longest = 0
        # while high < len(s):
        #     while s[high] in string:
        #         string.remove(s[low])
        #         low+=1
        #     string.add(s[high])
        #     high += 1 
        #     longest = max (longest, len(string))

        # return longest

        last_seen = {}
        low = 0
        longest = 0

        for high, char in enumerate(s):
            if char in last_seen:
                low = max(low, last_seen[char] + 1)

            last_seen[char] = high
            longest = max(longest, high - low + 1)

        return longest
                