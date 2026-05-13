class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        len_nb = len(numbers)
        p1, p2 = 0, len_nb - 1
        while p1 < p2:
            current_sum = numbers[p1] + numbers[p2]
            
            if current_sum == target:
                # Problem asks for 1-indexed array
                return [p1 + 1, p2 + 1]
            
            elif current_sum < target:
                # Sum is too small, we need a larger value
                # So move the left pointer to the right
                p1 += 1
            else:
                # Sum is too large, we need a smaller value
                # So move the right pointer to the left
                p2 -= 1