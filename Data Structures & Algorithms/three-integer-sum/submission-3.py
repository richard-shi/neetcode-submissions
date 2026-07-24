class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        sorted_nums = sorted(nums)        

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            print(f"{i} {r} {l}")

            while l < r:
                lr_sum = sorted_nums[l] + sorted_nums[r]
                if lr_sum < -sorted_nums[i]:
                    l += 1
                elif lr_sum > -sorted_nums[i]:
                    r -= 1
                else:
                    triplets.add((sorted_nums[i], sorted_nums[l], sorted_nums[r]))
                    l += 1
                    r -= 1

        return [list(triplet) for triplet in triplets]

















        