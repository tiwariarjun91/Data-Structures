# Time complexity: O(logn)
# Space complexity: O(1)

def BinarySearch(nums,target)-> bool:
    low = 0
    high = len(nums) - 1

    while(low<=high): # low and high can be at the same index.
        mid = low + (high-low)//2 # to avoid integer overloading, not present in python but a good programing practice
        if nums[mid] == target:
            return True
        elif nums[mid] < target: # < because here we are comparing the nums[mid] with external number else nums[mid]<=nums[low] as low and mid can be the same indexes
            low = mid +1
        else:
            high = mid -1
    return False

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(BinarySearch(nums,2))

def BinarySearch1(nums,target)-> bool:
    low = 0
    high = len(nums)-1
    while low<=high:
        mid = low + (high-low)//2
        if target < nums[mid]:
            high = mid -1
        elif target > nums[mid]:
            low = mid + 1
        else:
            return True
    return False

print(BinarySearch1(nums,2))

def BinarySearchRecursive(nums,target,low = 0,high = -1)-> bool:
    if high == -1:
        
        high = len(nums) - 1
    mid = low + (high-low)//2
    if nums[mid] == target:
        return True
    elif target > nums[mid]:
        return BinarySearchRecursive(nums,target,mid+1,high)
    else:
        return BinarySearchRecursive(nums,target,low,mid-1)
    
    return False

print(BinarySearchRecursive(nums,2,0,-1))
