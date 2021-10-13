# Time complexity:- O(n)
# Space complexity:- O(1) No use of any auxilary data structure


def UnorderedSearch(nums,target)-> bool:
    for i in range(len(nums)):
        if target == nums[i]:
            return True

    return False

nums = [1,84,87,0,45,36,700,89,46,2,9,14,65]
print(UnorderedSearch(nums,2))
print(UnorderedSearch(nums,100))
