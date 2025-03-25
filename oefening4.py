target = int(input("input target"))
nums = list(map(int, input("lijst").split(",")))
def countTargetPairs(nums, target):
    
    TrPairs = 0
    for getal in range(len(nums)):
        for fofo in range( getal +1, len(nums)):
            if gatal != fofo:
                if nums[getal] + nums[fofo] < target:
                    TrPairs += 1
    return TrPairs


print(countTargetPairs(nums, target))

