class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_seen = {n:False for n in nums}
        longest_seq_length = 0

        for n in nums:
            if nums_seen[n]:
                continue

            if (n - 1) not in nums_seen: # Beginning of seq
                current = n
                current_streak = 0
                while current in nums_seen:
                    nums_seen[current] = True
                    current += 1
                    current_streak += 1
                longest_seq_length = max(longest_seq_length, current_streak)
        
        return longest_seq_length