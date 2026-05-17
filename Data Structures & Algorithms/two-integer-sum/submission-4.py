class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Pair each number with its original index: [[num, original_index], ...]
        sorted_nums = sorted([[num, i] for i, num in enumerate(nums)])
        
        l, r = 0, len(nums) - 1
        
        while l < r:
            t_sum = sorted_nums[l][0] + sorted_nums[r][0]
            
            if t_sum == target:
                # Return the stored original indices
                return [min(sorted_nums[l][1], sorted_nums[r][1]), 
                        max(sorted_nums[l][1], sorted_nums[r][1])]
            elif t_sum < target:
                l += 1
            else:
                r -= 1