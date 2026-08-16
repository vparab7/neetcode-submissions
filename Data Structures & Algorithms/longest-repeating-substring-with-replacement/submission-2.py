class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low = high = 0
        occurance = dict()
        max_occ = 0
        longest = 0
        while high < len(s):
            occurance[s[high]] = occurance.get(s[high],0) + 1
            max_occ = max(max_occ,occurance[s[high]])
            while high - low + 1 - max_occ > k: 
                occurance[s[low]] = occurance[s[low]] - 1
                low+=1
            longest = max(longest,high-low+1)
            high +=1

        return longest
# if we comment 
# #occurance[s[low]] = occurance[s[low]] - 1, 
# then this will fail 
# ex -> "AABABBA"
