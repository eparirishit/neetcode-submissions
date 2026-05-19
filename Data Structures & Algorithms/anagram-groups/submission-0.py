class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Pre-sort every string once so we don't repeat the sorting work
        sorted_strs = ["".join(sorted(s)) for s in strs]
        
        anagrams = []
        visited = set()
        
        for i in range(len(strs)):
            if i in visited: # Track visited indices instead of strings
                continue
                
            visited.add(i)
            current_group = [strs[i]]
            
            # Look ahead for any matches using pre-sorted list
            for j in range(i + 1, len(strs)):
                if sorted_strs[i] == sorted_strs[j]:
                    current_group.append(strs[j])
                    visited.add(j) # Mark 'j' as visited so the outer loop skips it later
                    
            anagrams.append(current_group)
            
        return anagrams