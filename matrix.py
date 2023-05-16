def mat(mats1,mats2):
    row=len(mats1)
    col=len(mats2[0])
    result=[[0 for j in range (col)] for i in range(row)]
    for i in range(row):
        for j in range(col):
            result[i][j]=mats1[i][j]+mats2[i][j]
    return result

mats1=[[1,2,3],[4,5,6],[7,8,9]]
mats2=[[1,2,3],[4,5,6],[7,8,9]]
result=mat(mats1,mats2)
print(result)
