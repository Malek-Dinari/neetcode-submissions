class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a list of tuples: (number, original_index)
        # For [3, 2, 4], this creates [(3, 0), (2, 1), (4, 2)]
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        # Sort based on the nubmers -> [(2, 1), (3, 0), (4, 2)]
        inc_nums = sorted(indexed_nums)
        
        p1, p2 = 0, len(inc_nums) - 1

        while p1 < p2:
            # Check the sum of the numbers (that's index 0 of the tuple)
            curr_sum = inc_nums[p1][0] + inc_nums[p2][0]
            
            if curr_sum == target:
                # Return the original indices (index 1 or -1 of the tuple)
                return sorted([inc_nums[p1][1], inc_nums[p2][1]])
            elif curr_sum < target:
                p1 += 1
            else:
                p2 -= 1