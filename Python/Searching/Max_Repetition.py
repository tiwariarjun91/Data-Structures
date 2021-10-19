# Time Complexity :- O(n^2)
# Space Complexity :- O(1) no auxilary data structure

def Max_repetition_Brute_Force(nums):
    max = count = 0
    for i in range(0,len(nums)):
        count = 1
        for j in range(0,len(nums)):
            if nums[i] == nums[j]:
                count += 1
        if max < count:
            max = count
            maxNumber = nums[i]
    print("maximum repetition:-",maxNumber)

Max_repetition_Brute_Force([0,0,0,0,1,1,1,5,5,5,5,4,4,4,4,5,5,5,6,6])

def Max_repetition_Hash_Map(nums):  #Time complexity :- O(n), space complexity O(n)
    max = 0
    dic = {}
    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[nums[i]] = 1
        else:
            dic[nums[i]] += 1
        
        if max < dic[nums[i]]:
            max = dic[nums[i]]
            maxNumber = nums[i]
    print("maximum repetition:-",maxNumber)

Max_repetition_Hash_Map([0,0,0,0,1,1,1,5,5,5,5,4,4,4,4,5,5,5,6,6])




def Max_repetition_Efficient(nums):
    max = 0
    n = len(nums)
    for i in range(0,n):
        nums[nums[i]%n] += n
    
    for i in range(0,n):
        count = nums[nums[i]%n]//n # mod n is essential
        if max < count :
            max = count
            maxNum = nums[i]%n # mod n is essential
    print(maxNum,max)

Max_repetition_Efficient([0,0,0,0,1,1,5,6,6])