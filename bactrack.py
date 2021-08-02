def repetitions(DNA):
    a = 1
    maxi = 1
    for i in range(len(DNA)-1):
        if DNA[i] == DNA[i+1]:
           a = a+1
           if a > maxi :
                maxi = a
        else:
             a = 1
    return maxi   
     

DNA = input()
print(repetitions(DNA))