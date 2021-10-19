def FirstRepeatedElement(nums):
    dic = {}
    max = 0
    maxtimes = 0
    for i in range(len(nums)-1,-1,-1):
        if nums[i] not in dic:
            dic[nums[i]] = 1
        else:
            max = nums[i]
            dic[nums[i]] += 1
            maxtimes = dic[nums[i]]
    print("First repeated ",max," ",maxtimes," times")
            
FirstRepeatedElement([1,1,1,1,3,2,1,2,3])