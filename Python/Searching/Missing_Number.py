# Time Complexity O(n^2)
# Space Complexity O(1) no auxilary data structure

def MissingNumberBruteForce(nums):
    for i in range(1,len(nums)+1):
        found = 0  #flags are good
        for j in range(0,len(nums)):
            if i == nums[j]:
                found = 1
        if found == 0:
            print("Missing number is ",i)

MissingNumberBruteForce([1,2,3,5,6,7,8])


# Time Complexity : O(n) lookup for Hashmap is O(1)
# Space Complexity : O(n) used auxillary data structure(Hashmap)
def MissingNumberHashMap(nums):
    dic = {}
    for i in nums:
        dic[i] = 0
    for i in range(1,len(nums)+1):
        if i not in dic:
            print("Missing Number is ", i)

MissingNumberHashMap([1,2,3,5,6,7,8])


#Time Complexity: O(n)
#Space Complexity : O(1)
def MissingNumberFormulae(nums):
    n = len(nums)
    sum = ((n+1) * (n+2))//2  # len is 7 but we need from 1 to 8 so it will be 8*9//2
    for i in nums:
        sum = sum - i
    print("Missing Number is ", sum)

MissingNumberFormulae([1,2,3,5,6,7,8])

def MissingNumberXOR(nums):
    X = 0
    for i in range(1,len(nums)+2): # length is 7 we need 1-8 hence 1-9 as 9 is excluded
        X = X ^ i
    for i in nums:
        X = X ^ i
    print("Missing Number is ", X)

MissingNumberXOR([1,2,3,5,6,7,8])