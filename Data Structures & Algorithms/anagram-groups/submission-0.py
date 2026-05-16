class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagr_map = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagr_map[sorted_s].append(s)

        return list(anagr_map.values())