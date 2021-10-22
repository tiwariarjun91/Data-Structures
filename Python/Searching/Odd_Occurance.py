def FindOddOccuringNumber(nums):
    X = 0
    for i in nums:
        X = X ^ i
    print("Number with Odd Occurance is ",X)

FindOddOccuringNumber([1,2,1,2,3,3,4,5,4,5,2])