# Time complexity:- O(n) Worst case if we need to scan the complete array
# Space complexity:- O(1) Did not use any auxilary data

def OrderedSearch(nums,target) -> bool:
    for i in range(len(nums)):
        if target == nums[i]:
            return True
        elif target < nums[i]:
            return False

nums = [1,2,3,4,5,7,8,9,10,11]
print(OrderedSearch(nums,6))
print(OrderedSearch(nums,5))