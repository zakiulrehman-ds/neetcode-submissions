class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # create empty buckets whare index = frequency count
        freq = [[] for i in range(len(nums) + 1)]
        #count occurrences of each number
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        #put numbers into their frequency buckets
        #if number 3 apears 4 times, put 3 into freq[4]
        for num, frequency in count.items():
            freq[frequency].append(num)

        res = []
        #iterate backwards from the highest frequency to the lowest
        for i in range(len(freq) -1,0,-1):
            for num in freq[i]:
                res.append(num)
                #Once we collected exactly k items, return the result immediately
                if len(res) == k:
                    return res