#import image_slicer
#import scipy
#from matplotlib import pyplot as plt
import cv2
#from PIL import ImageDraw, ImageFont
#from scipy.misc import imsave
#from scipy import ndimage
#from scipy import misc
#import scipy.misc
import numpy as np
#import random
#import sys
#from image_slicer import join
#from dateutil.utils import today 
#import binascii


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

img=cv2.imread("receiver_images\j33.bmp",0)
 

print("Actual size:")
print(img.shape)


try:  
    
    t=0
    z=0
    a=0
    b=4
    d=0
    s=0
    str=''
    str_len=0
    final_list=[]
    final_char_list=[]
    x_inc=0
    y_inc=8
    #final_char_list=[]
    
    for ii in range(0,20): 
        ar=[]
        seg=[]
        for i in range (0,8):
            arr=[] 
            for j in range (x_inc,y_inc):
                arr.append(img[i][j])
            ar.append(arr)
        

        np.ndarray(shape=(8,8),dtype=int)
        file=np.asarray(ar)
        kt_list=[]
        seg=file
        
     
        print("seg matrix received is: ",seg)  
        print("For each seg:")  
        for i in range(0,64,2):
            k=L[i][0]
            l=L[i][1]
        
            for x in range(0,8):
                for y in range(0,8):
                    if k==x and l==y:
                        kt_list.insert(len(kt_list),seg[k][l])
                        break
        print(t,"kt_list:",kt_list)
        k=0
       
        t=t+1;
        
        binary_list1=[]
        binary_list2=[]
        binary_list3=[]
        binary_list4=[]
        m=0
        n=8
        while(m<32):
            for i in range(m,n):    
                bin_no=bin(int(kt_list[i]))
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
        print("binary list1:",binary_list1) 
        print("binary list2:",binary_list2)     
        print("binary list3:",binary_list3)     
        print("binary list4:",binary_list4)  
        
        
       
          
        
        for k in range(0,8):
            if(listfinal[z][k]==7):
                Q_pos=k
                print("Q_pos:",Q_pos)
                
                sol_list=[]
        
                for i in range(0,8): 
                        c=listfinal[z][i]
                                
                        for j in range(0,8):
                            if(c!=7):
                                if(c==j):
                                    sol_list.append(binary_list1[i][j])
                print("sol list",sol_list)    
                y=0
                char_list=[]
                for x in range(0,8): 
                    if x!=Q_pos:
                        if(binary_list1[x][7]==sol_list[y]):
                            char_list.append('0')
                        else:
                            char_list.append('1')
                        y=y+1
                final_char_list.append(''.join(char_list))
                
                sol_list=[]
        
                for i in range(0,8): 
                        c=listfinal[z][i]
                                
                        for j in range(0,8):
                            if(c!=7):
                                if(c==j):
                                    sol_list.append(binary_list2[i][j])
                print("sol list",sol_list,str)                    
                y=0
                char_list=[]
                for x in range(0,8): 
                    if x!=Q_pos:
                        if(binary_list2[x][7]==sol_list[y]):
                            char_list.append('0')
                        else:
                            char_list.append('1')
                        y=y+1
                final_char_list.append(''.join(char_list))
                
                sol_list=[]
        
                for i in range(0,8): 
                        c=listfinal[z][i]
                                
                        for j in range(0,8):
                            if(c!=7):
                                if(c==j):
                                    sol_list.append(binary_list3[i][j])
                print("sol list",sol_list,str)    
                y=0
                char_list=[]
                for x in range(0,8): 
                    if x!=Q_pos:
                        if(binary_list3[x][7]==sol_list[y]):
                            char_list.append('0')
                        else:
                            char_list.append('1')
                        y=y+1
                        
                final_char_list.append(''.join(char_list))
                
                sol_list=[]
        
                for i in range(0,8): 
                        c=listfinal[z][i]
                                
                        for j in range(0,8):
                            if(c!=7):
                                if(c==j):
                                    sol_list.append(binary_list4[i][j])
                print("sol list",sol_list,str)    
                y=0
                char_list=[]
                for x in range(0,8): 
                    if x!=Q_pos:
                        if(binary_list4[x][7]==sol_list[y]):
                            char_list.append('0')
                        else:
                            char_list.append('1')
                        y=y+1
                final_char_list.append(''.join(char_list))
                            
                 
                
              
                print("char for seg:", s, final_char_list)  
                #final_list.append(final_char_list)
                               
        #alternationg queens sol
        z=z+2
        a=a+4
        b=b+4
        s=s+1  
        x_inc=x_inc+8
        y_inc=y_inc+8
    print("********************************")
    print("final:",final_char_list)     
    for fin in final_char_list:
        str=str+chr(int(fin,2))   
        
except Exception:
    print(Exception.Message) 
    
print("string :",str)    
    