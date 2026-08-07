class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash_map = {}

        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1

        sorted_array = sorted(hash_map, key=hash_map.get, reverse=True)

        return sorted_array[:k]