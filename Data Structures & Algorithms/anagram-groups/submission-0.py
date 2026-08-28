class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping charCount to list of Anagrams
            #create a list of 26 zeros, one for each letter (a-z)
        for s in strs:
            # Create a list of 26 zeros, one for each letter (a-z)
            count = [0] * 26 
            for char in s:
                # ord(char) gets the ASCII number of the letter
                # ord('a') is 97. If char is 'b' (98), 98 - 97 = index 1
                count[ord(char) - ord('a')] += 1
                
            # Convert the list to a tuple because Python lists cannot be dictionary keys
            # A tuple like (1, 0, 1, 0...) represents the letter blueprint
            res[tuple(count)].append(s)
            
        return list(res.values())
