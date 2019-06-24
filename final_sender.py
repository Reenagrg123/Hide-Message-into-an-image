# import image_slicer
# import scipy
# from matplotlib import pyplot as plt
import cv2
# from PIL import ImageDraw, ImageFont
# #from scipy.misc import imsave
# from scipy import ndimage
# from scipy import misc
# import scipy.misc
import numpy as np
# import random
# import sys
# from image_slicer import join
# from dateutil.utils import today 
# from PIL import Image

#**********************************************************************#


def inRangeAndEmpty(posx,posy,board,N):
    return (posx < N and posx >= 0 and posy < N and posy >= 0 and board[posx][posy] == 0)

def getAccessibility(x,y,moves,board,N):
    accessibility = 0
    for i in range(8):
        if inRangeAndEmpty(x+moves[i][0],y+moves[i][1],board,N): 
            accessibility += 1
    return accessibility

def getNextMoves(move,moves,board,N):
    positionx = move[0]
    positiony = move[1]
    accessibility = 8
    for i in range(8):
        newx = positionx + moves[i][0]
        newy = positiony + moves[i][1]
        newacc = getAccessibility(newx,newy,moves,board,N)
        if inRangeAndEmpty(newx,newy,board,N) and newacc < accessibility:
            move[0] = newx
            move[1] = newy
            accessibility = newacc
    return



def ifSolution(Board,N):
    for i in range(N):
        for j in range(N):
            if Board[i][j] == 0:
                return False
    return True

#***************************************************************************#
            

N =8
positionx = 0
positiony = 0
x = positionx
y = positiony
moveNumber = 2
move = [positionx,positiony]
moves = [[2,1],[2,-1],[1,2],[1,-2],[-1,2],[-1,-2],[-2,1],[-2,-1]]
Board = np.zeros([N,N])
Board[positionx][positiony] = 1
L = []

for i in range(N*N):
    move[0] = positionx
    move[1] = positiony
    getNextMoves(move,moves,Board,N)
    positionx = move[0]
    positiony = move[1]
    Board[positionx][positiony] = moveNumber
    moveNumber += 1
Board[positionx][positiony] -= 1


sol = ifSolution(Board,N)
if sol:

    k = 1
    while k <= N*N:
        for i in range(N):
            for j in range(N):
                if Board[i][j] == k:
                    L.append([i,j])  
                    k += 1
#     print(Board)
else:
    moves = [[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
    Board = np.zeros([N,N])
    positionx = x
    positiony = y
    Board[positionx][positiony] = 1
    L = []
    moveNumber = 2 
    move = [positionx,positiony] 
  
    for i in range(N*N):
        move[0] = positionx
        move[1] = positiony
        getNextMoves(move,moves,Board,N)
        positionx = move[0]
        positiony = move[1]
        Board[positionx][positiony] = moveNumber
        moveNumber += 1
    Board[positionx][positiony] -= 1

 
    sol = ifSolution(Board,N)
    if sol:
     
        k = 1
        while k <= N*N:
            for i in range(N):
                for j in range(N):
                    if Board[i][j] == k:
                        L.append([i,j])
                        k += 1
#         print(Board)
if len(L) == 0:
    print("Didn't find a solution.")
print("Knights' positions: ", L)


#***************************************************************#

"""The n queens puzzle."""


size = 8
solutions = 0
listfinal=[]

def solve():
    positions = [-1] * size
    put_queen(positions, 0)
    print("Found", solutions, "solutions.")


def put_queen(positions, target_row):
    global solutions
    if target_row ==  size:
        show_full_board(positions)
        solutions += 1
    else:    
        for column in range( size):  
            if  check_place(positions, target_row, column):
                positions[target_row] = column
                put_queen(positions, target_row + 1)
    

def check_place(positions, ocuppied_rows, column):
    for i in range(ocuppied_rows):
        if positions[i] == column or \
            positions[i] - i == column - ocuppied_rows or \
            positions[i] + i == column + ocuppied_rows:
            return False
    return True


def show_full_board(positions):
    global listfinal
    list1=[]
    for row in range( size):

        for column in range( size):
            if positions[row] == column:
                list1.append(positions[row])
      
    listfinal.append(list1)
  


solve()
print("Queen Solutions are: ",listfinal)


#**************************************************************#




img=cv2.imread("sender_images\j3.jpg",0)
 

print("Actual size:")
print(img.shape)




try:    
  
   
    
    mystring=input("Enter ur message:")
    length=len(mystring)
    mystring=mystring.ljust(150-length)
   
    
    print("************************************")
    
   
    t=0
    z=0
    a=0
    b=4
    d=0
    x_inc=0
    y_inc=8
    count_tile=0
    for ii in range(0,20): 
        ar=[]
        kt_list=[]  
        new_kt_list=[]    
        for i in range (0,8):
            arr=[] 
            for j in range (x_inc,y_inc):
                 
                arr.append(img[i][j])
                    
            ar.append(arr)
            
    
        np.ndarray(shape=(8,8),dtype=int)
        file=np.asarray(ar)
        
        
        
        
      
        print("For each seg:")  
        for i in range(0,64,2):
            k=L[i][0]
            l=L[i][1]
        
            for x in range(0,8):
                for y in range(0,8):
                    if k==x and l==y:
                        kt_list.insert(len(kt_list),file[k][l])
                        break
        print(t,"kt_list:",kt_list)
        t=t+1;
      
        binary_list1=[]
        binary_list2=[]
        binary_list3=[]
        binary_list4=[]
        m=0
        n=8
        while(m<32):
            for i in range(m,n):    
                bin_no=bin(kt_list[i])
                bin_no1=bin_no[2:]
                if len(bin_no1)<8:
                    bin_no1 = bin_no1.zfill(8)
                    
                row=[]
                for j in bin_no1:
                    row.append(j)
                if(m==0):    
                    binary_list1.append(row)
                elif(m==8):    
                    binary_list2.append(row) 
                elif(m==16):    
                    binary_list3.append(row) 
                elif(m==24):    
                    binary_list4.append(row)                
            
            m=m+8
            n=n+8
        print(binary_list1)
        print(binary_list2)
        print(binary_list3)
        print(binary_list4)
        count=0;   
        
        for ch in mystring[a:b]:
            count=count+1
            
        #*****queens iterations***#
        #applying first solution
                
            if(count==1):
                print(ch)
                sol_list=[]
                for i in range(0,8): 
                    c=listfinal[z][i]
                    
                    for j in range(0,8):
                        if(c!=7):
                            if(c==j):
                                sol_list.append(binary_list1[i][j])
                print("sol_list: ",sol_list)
                ints=ord(ch) 
                bins=bin(ints)
                mychar = bins[2:]
                if len(mychar)<7:
                    mychar = mychar.zfill(7)
                print("Mychar:",mychar) 
                for k in range(0,8):
                    if(listfinal[z][k]==7):
                        Q_pos=k
                        print("Q_pos:",Q_pos)
            
                        for i in range(0,8):
                            if(i<Q_pos):
                                j=binary_list1[i]
                                if(sol_list[i]==mychar[i]):
                                    for n,k in enumerate(j):
                                        if(n==7):
                                            j[n]='0'
                        
                                else:
                                    for n,k in enumerate(j):
                                        if(n==7):
                                            
                                            j[n]='1'
             
                            elif(i==Q_pos):
                                continue
                            else:
                                j=binary_list1[i]
            
                                if(sol_list[i-1]==mychar[i-1]):
                                    for n,k in enumerate(j):
                                        if(n==7):
                                            j[n]='0'
                        
                                else:
                                    for n,k in enumerate(j):
                                        if(n==7):
                                            j[n]='1'
                                                    
           
            
             
            elif(count==2):
                print(ch)
                sol_list=[]
                for i in range(0,8): 
                    c=listfinal[z][i]
                    for j in range(0,8):
                        if(c!=7):
                            if(c==j):
                                sol_list.append(binary_list2[i][j])
                print("sol_list: ",sol_list)
                ints=ord(ch) 
                bins=bin(ints)
                #print(len(bins))
                mychar = bins[2:]
                if len(mychar)<7:
                    mychar = mychar.zfill(7)
                print("Mychar:",mychar) 
                for k in range(0,8):
                    if(listfinal[z][k]==7):
                        Q_pos=k
                        print("Q_pos:",Q_pos)
            
                        for i in range(0,8):
                            if(i<Q_pos):
                                j=binary_list2[i]
                                if(sol_list[i]==mychar[i]):
                                    for n,k in enumerate(j):
                                        if(n==7):
                                            j[n]='0'
                        
                                else:
                                    for n,k in enumerate(j):
                                        if(n==7):
                                            
                                            j[n]='1'
             
                            elif(i==Q_pos):
                                continue
                            else:
                                j=binary_list2[i]
            
                                if(sol_list[i-1]==mychar[i-1]):
                                    for n,k in enumerate(j):
                                        if(n==7):
                                            j[n]='0'
                        
                                else:
                                    for n,k in enumerate(j):
                                        if(n==7):
                                            j[n]='1'
                                                    
             
            
            
            elif(count==3):
                print(ch)
                sol_list=[]
                for i in range(0,8): 
                    c=listfinal[z][i]
                    for j in range(0,8):
                        if(c!=7):
                            if(c==j):
                                sol_list.append(binary_list3[i][j])
                print("sol_list3: ",sol_list)
                ints=ord(ch) 
                
                bins=bin(ints)
                mychar = bins[2:]
                if len(mychar)<7:
                    mychar = mychar.zfill(7)
                print("Mychar:",mychar) 
                for k in range(0,8):
                    if(listfinal[z][k]==7):
                        Q_pos=k
                        print("Q_pos:",Q_pos)
            
                        for i in range(0,8):
                            if(i<Q_pos):
                                j=binary_list3[i]
                                if(sol_list[i]==mychar[i]):
                                    for n,k in enumerate(j):
                                        if(n==7):
                                            j[n]='0'
                        
                                else:
                                    for n,k in enumerate(j):
                                        if(n==7):
                                            
                                            j[n]='1'
             
                            elif(i==Q_pos):
                                continue
                            else:
                                j=binary_list3[i]
            
                                if(sol_list[i-1]==mychar[i-1]):
                                    for n,k in enumerate(j):
                                        if(n==7):
                                            j[n]='0'
                        
                                else:
                                    for n,k in enumerate(j):
                                        if(n==7):
                                            j[n]='1'
                                                    
           
            
            elif(count==4):
                print(ch)
                sol_list=[]
                for i in range(0,8): 
                    c=listfinal[z][i]
                    for j in range(0,8):
                        if(c!=7):
                            if(c==j):
                                sol_list.append(binary_list4[i][j])
                print("sol_list4: ",sol_list)
                ints=ord(ch) 
                bins=bin(ints)
                mychar = bins[2:]
                if len(mychar)<7:
                    mychar = mychar.zfill(7)
                print("Mychar:",mychar) 
                for k in range(0,8):
                    if(listfinal[z][k]==7):
                        Q_pos=k
                        print("Q_pos:",Q_pos)
            
                        for i in range(0,8):
                            if(i<Q_pos):
                                j=binary_list4[i]
                                if(sol_list[i]==mychar[i]): 
                                    for n,k in enumerate(j):
                                        if(n==7):
                                            j[n]='0'
                        
                                else:
                                    for n,k in enumerate(j):
                                        if(n==7):
                                            
                                            j[n]='1'
             
                            elif(i==Q_pos):
                                continue
                            else:
                                j=binary_list4[i]
            
                                if(sol_list[i-1]==mychar[i-1]):
                                    for n,k in enumerate(j):
                                        if(n==7):
                                            j[n]='0'
                        
                                else:
                                    for n,k in enumerate(j):
                                        if(n==7):
                                            j[n]='1'
                                                    
    
                    
                
            #backtracking
        print("updated............")

        
        new_binary_list1=[]
        new_binary_list2=[]
        new_binary_list3=[]
        new_binary_list4=[]
        for i in range(0,8):
            str1=''.join(binary_list1[i])
            new_binary_list1.append(int(str1,2))
            str1=''.join(binary_list2[i])
            new_binary_list2.append(int(str1,2))
            str1=''.join(binary_list3[i])
            new_binary_list3.append(int(str1,2))
            str1=''.join(binary_list4[i])
            new_binary_list4.append(int(str1,2))
            
        new_kt_list=[]
        new_kt_list=new_binary_list1+new_binary_list2+new_binary_list3+new_binary_list4
        print("new kt_list:",new_kt_list)
        w=0 
        k=0
        l=0
        print("segment matrix before changes: ",file) 
        #print('new_ktlist:',new_kt_list)
        for i in range(0,64,2):
            k=L[i][0]
            l=L[i][1]
           
            for x in range(0,8):
                for y in range(0,8):
                    if x==k and y==l:
                        file[k,l]=new_kt_list[w]
                       
                        w=w+1
                        break
               
       
        for i in range (0,8):
       
            for j in range (0,8): #traverses through width of the image
                img[i][j+x_inc]=file[i][j]
                
         
        print("segment matrix after changes: ",file)     
              
        #alternationg queens sol
        z=z+2
        a=a+4
        b=b+4
        x_inc=x_inc+8
        y_inc=y_inc+8
             
 
    print("done...")        
        
except Exception:
    print(Exception.Message)  
    

print('*******************')    

cv2.imwrite("receiver_images\j33.bmp",img) 

               
                
