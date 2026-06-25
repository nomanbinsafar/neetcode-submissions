class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq=defaultdict(list)
        
        for string in strs:
            vec=[0]*26
            for ch in string:
                vec[ord(ch)-ord('a')]+=1
            freq[tuple(vec)].append(string)
        return list(freq.values())

        
            
        