class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def rec(idx,path):
            result.append(path)
            for i in range(idx,len(nums)):
                rec(i+1,path+[nums[i]])
        result = []
        rec(0,[])
        return result
