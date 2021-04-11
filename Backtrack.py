
def repetitions(DNA):
    a =0
    b =0
    c =0
    d =0
    
    AUX = ["A","C","G","T"]
    if len(DNA) == 0:
        print('something else')
        return 1
    if len(DNA) > 0 :
        for i in range(len(DNA)):
            if DNA[i] == AUX[0] :
                a = a+1
            if DNA[i] == AUX[1]:
                b = b+1
            if DNA[i] == AUX[2]:
                c = c+1
            if DNA[i] == AUX[3]:
                d = d+1
    return max(a,b,c,d)        

DNA = input()
print(repetitions(DNA))
        