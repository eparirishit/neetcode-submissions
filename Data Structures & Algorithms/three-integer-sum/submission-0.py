class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        n = len(nums)

        for i in range(n - 2):
            # Skip the repeated values for 'a'
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            two_pairs = self.twoPair(-nums[i], (i + 1), nums)
            for pair in two_pairs:
                triplets.append([nums[i]] + pair)
        return triplets

    

    def twoPair(self, target: int, start: int, nums: List[int]) -> List[List[int]]:
        l, r = start, len(nums) - 1
        pairs = []
        while l < r:
            pair_sum = nums[l] + nums[r]
            if pair_sum == target:
                pairs.append([nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif pair_sum < target:
                l += 1
            else:
                r -= 1
        return pairs