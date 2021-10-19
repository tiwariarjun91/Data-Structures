def FirstRepeatedCharacter(stri):
    count = [0 for _ in range(256)]
    for i in stri:
        if count[ord(i)] == 1:
            print("Repeated Character in ",stri,":- ",i)
            return
        else:
            count[ord(i)] +=1
    print("No repeated Character in ",stri) 
FirstRepeatedCharacter("bcdebfgha")
FirstRepeatedCharacter("abcdef")

