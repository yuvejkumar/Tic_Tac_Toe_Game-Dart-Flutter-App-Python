import sys
def Assign(matrix,value,pos):
    if pos==1:
        matrix[0][0]=value
    elif pos==2:
        matrix[0][1]=value
    elif pos==3:
        matrix[0][2]=value
    elif pos==4:
        matrix[1][0]=value
    elif pos==5:
        matrix[1][1]=value
    elif pos==6:
        matrix[1][2]=value
    elif pos==7:
        matrix[2][0]=value
    elif pos==8:
        matrix[2][1]=value
    elif pos==9:
        matrix[2][2]=value
    return matrix
def tictactoe(matrix):

    # checking in diagolnal from left side with index 00, 11, 22 
    arr1=[0,1,2]
    diag_left_X=0
    diag_left_O=0
    for i in arr1:
        if matrix[i][i]=="X":
            diag_left_X=diag_left_X+1
        elif matrix[i][i]=="O":
            diag_left_O=diag_left_O+1
    if diag_left_X==3:
        print("---------Hurray X is the winner -----")
        sys.exit()
    if diag_left_O==3:
        print("---------Hurray O is the winner -----")
        sys.exit()
    
    # checking in diagolnal from right side with index 02, 11,20
    arr2=["02","11","20"]
    diag_right_X=0
    diag_right_O=0
    for i in arr2:
        if matrix[int(i[0])][int(i[1])]=="X":
            diag_right_X=diag_right_X+1
        elif matrix[int(i[0])][int(i[1])]=="O":
            diag_right_O=diag_right_O+1
    if diag_right_X==3:
        print("---------Hurray X is the winner -----")
        sys.exit()
    if diag_right_O==3:
        print("---------Hurray O is the winner -----")
        sys.exit()
    

    # checking rows with index 00,01,02 --> 10,11,12 --> 20,21,22
    for i in range(3):
        x=0
        for j in range(3):
            if matrix[i][j]=="O":
                x=x+1
        if x==3:
            print("---------Hurray O is the winner -----")
            sys.exit()
        y=0
        for j in range(3):
            if matrix[i][j]=="X":
                y=y+1
        if y==3:
            print("---------Hurray X is the winner -----")
            sys.exit()
        
    #checking coloumn with index 00,10,20 --> 01,11,21 --> 02,12,22
    for i in range(3):
        x=0
        for j in range(3):
            if matrix[j][i]=="O":
                x=x+1
        if x==3:
            print("---------Hurray O is the winner -----")
            sys.exit()
        y=0
        for j in range(3):
            if matrix[j][i]=="X":
                y=y+1
        if y==3:
            print("---------Hurray X is the winner -----")
            sys.exit()

# Initialing the program 

print(" ___________________________________________________")
print("|            Welcome to TicTacToe Game              |")
print("|___________________________________________________|")
print("  ")
matrix=[['1','2','3'],['4','5','6'],['7','8','9']]
position=[[1,2,3],[4,5,6],[7,8,9]]
ifdupicate=[]
while True:
    value1=input("First User Choose the value ===> X,O : ")
    if value1=="X" or value1=="O":
        break
    print("----->You have choosen wrong choice")


if value1=="X" :
    print("The First User is ---->X")
    print("The second User is --->O")
    value2="O"
else:
    print("The First User is ---->O")
    print("The second User is --->X")
    value2="X"
print("Note:----> For Available Positions, the position number is shown  ")
print("=================================================================")
print(" ")
c=0
while True:        
    print("Curent values are : ")
    print(" ")
    for i in matrix:
        print(i)
    print(" ")

    print("User : ",value1)
    while True:
        i1=input(" Enter the position of the value : ")
        if (i1.isnumeric()):
            pos1=int(i1)
            if pos1 in ifdupicate:
                print("  ")
                print("    WARNING----->Trying to Re-Assign the value")
                print("    please Enter only Available position ")
                print("  ")
            elif pos1>9 or pos1<0:
                print(" ")
                print("    WARNING----->No such position")
                print(" ")
            else :
                ifdupicate.append(pos1)
                break
        else:
            print("    WARNING----->Enter only Integer")
    c=c+1
    matrix = Assign(matrix,value1,pos1)
    for i in matrix:
        print(i)
    print(" ")
    tictactoe(matrix)  #for every input we are checking the win possiblity
    if c==9:
        print("==============Game-Tie============")
        print("==================================")
        restart=int(input("Enter --->1 : To restart the game"))
        if restart==1:
            matrix=[['1','2','3'],['4','5','6'],['7','8','9']]
            ifdupicate=[]
            print("   ")
            for i in matrix:
                print(i)
        else:
            sys.exit()
    print("User : ",value2)
    while True:
        i2=input(" Enter the position of the value : ")
        if (i2.isnumeric()):
            pos2=int(i2)
            if pos2 in ifdupicate:
                print("  ")
                print("    WARNING----->Trying to Re-Assign the value ")
                print("    please Enter only Available position ")
            elif pos2>9 or pos2<0:
                print(" ")
                print("    WARNING----->No such position")
                print(" ")
            else :
                ifdupicate.append(pos2)
                break
        else:
            print("    WARNING----->Enter only positive Integer")
    c=c+1
    matrix = Assign(matrix,value2,pos2)
    for i in matrix:
        print(i)
    print(" ")
    tictactoe(matrix)   #for every input we are checking the win possiblity
    