# Time complexity: O(n^2) because of the two for loops
# Space complexity: O(1) no auxilary data structure

def CheckDuplicateBrute(nums)-> bool:
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

print("1",CheckDuplicateBrute([1,4,89,45,2,3,7,45]))

def CheckDuplicateSort(nums)-> bool:
    nums.sort() # does not return any value
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

print("2",CheckDuplicateSort([1,4,89,45,2,3,7,45]))


def CheckDuplicateHashMap(nums)-> bool:
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = [1]
        else:
            return True
    return False

print("3",CheckDuplicateHashMap([0,1,2,3,4,5,4]))
print("4",CheckDuplicateHashMap([0,1,2,3,4,5]))
print("5",CheckDuplicateHashMap([0]))
print("6",CheckDuplicateHashMap([]))

def CheckDuplicateNegationTechnique(nums)-> bool:
    for i in range(0,len(nums)):
        if nums[abs(nums[i])] >=  0:
            nums[abs(nums[i])] = -nums[abs(nums[i])]
            print(nums,i)
        else:
            print("Duplicate exists: ",nums[i])
            return True
            
    return False

print("7",CheckDuplicateNegationTechnique([3,2,1,2,2,3]))
print("8",CheckDuplicateNegationTechnique([1,2,3,4,0]))