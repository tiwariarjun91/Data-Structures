def generate(numRows):
    dir1 ={}
    dir1[0] = [0,1,0]
        
        
    for i in range(1,numRows+1):
        dir1[i] = [0]
        j = 0
        arr = dir1.get(i-1)
        while j+1 <= len(dir1[i-1])-1:
            dir1[i].append(arr[j]+arr[j+1])
            j = j + 1
            
        dir1[i].append(0)
                
                
    print(dir1)



generate(5)