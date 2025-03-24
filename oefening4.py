def countTargetPairs(self, nums, target):
        qzzzt = 0
        for j in range(1, len(nums)):
            for i in range(0, j):
                if nums[i]+nums[j] < target:
                    qzzzt+=1
        return qzzzt
