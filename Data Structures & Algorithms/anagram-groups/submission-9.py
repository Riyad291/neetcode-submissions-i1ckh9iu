class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq = {}
        for s in strs:
            key = tuple(sorted(s))

            if key not in freq:
                freq[key] = []

            freq[key].append(s)
        return list(freq.values())
       