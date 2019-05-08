import numpy as np

global changematrix
def move(predtm,matrix,initial,final,nowx,nowy):
    if matrix[nowx,nowy]<0:
        if matrix[initial,final]>=abs(matrix[nowx,nowy]):
            matrix[initial,final]=matrix[initial,final]-abs(matrix[nowx,nowy])
            matrix[nowx,nowy]=0
        else:
            matrix[nowx,nowy]=matrix[nowx,nowy]+matrix[initial,final]
            matrix[initial,final]=0
    
    if matrix[initial,final]==0:
        return matrix
    
    elif nowx=rows-1:
        if matrix[nowx,nowy]<0:
            matrix=deposit(matrix,initial,final,nowx,nowy)
        return matrix
    
    else:
        maxdiff=0
        nextx=nowx
        nexty=nowy
        if nowx-1>=0:
            if predtm[nowx,nowy]-predtm[nowx-1,nowy]>maxdiff:
                maxdiff=predtm[nowx,nowy]-predtm[nowx-1,nowy]
                nextx=nowx-1
                nexty=nowy
        if nowx-1>=0 and nowy+1<cols:
            if predtm[nowx,nowy]-predtm[nowx-1,nowy+1]>maxdiff:
                maxdiff=predtm[nowx,nowy]-predtm[nowx-1,nowy+1]
                nextx=nowx-1
                nexty=nowy+1
        if nowy+1<cols:
            if predtm[nowx,nowy]-predtm[nowx,nowy+1]>maxdiff:
                maxdiff=predtm[nowx,nowy]-predtm[nowx,nowy+1]
                nextx=nowx
                nexty=nowy+1
        if nowx+1<rows and nowy+1<cols:
            if predtm[nowx,nowy]-predtm[nowx+1,nowy+1]>maxdiff:
                maxdiff=predtm[nowx,nowy]-predtm[nowx+1,nowy+1]
                nextx=nowx+1
                nexty=nowy+1
        if nowx+1<rows:
            if predtm[nowx,nowy]-predtm[nowx+1,nowy]>maxdiff:
                maxdiff=predtm[nowx,nowy]-predtm[nowx+1,nowy]
                nextx=nowx+1
                nexty=nowy
        if nowy-1>=0 and nowx+1<rows:
            if predtm[nowx,nowy]-predtm[nowx+1,nowy-1]>maxdiff:
                maxdiff=predtm[nowx,nowy]-predtm[nowx+1,nowy-1]
                nextx=nowx+1
                nexty=nowy-1
        if nowy-1>=0:
            if predtm[nowx,nowy]-predtm[nowx,nowy-1]>maxdiff:
                maxdiff=predtm[nowx,nowy]-predtm[nowx,nowy-1]
                nextx=nowx
                nexty=nowy-1
        if nowx-1>=0 and nowy-1>=0:
            if predtm[nowx,nowy]-predtm[nowx-1,nowy-1]>maxdiff:
                maxdiff=predtm[nowx,nowy]-predtm[nowx-1,nowy-1]
                nextx=nowx-1
                nexty=nowy-1
        move(predtm,matrix,initial,final,nextx,nexty)
        

        


def geospatial(predtm,matrix):
    (rows,cols)=matrix.shape
    for i in range(0,rows):
        for j in range(0,cols):
            if matrix[rows,cols]>0:
                move(predtm,matrix,i,j,i,j)
    
    