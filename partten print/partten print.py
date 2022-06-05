1)Problem Description
  In this program we will be coding a star box pattern which will have n number of stars in it rows and n of stars in column hence
   it will be a n x n square star pattern .
   The user will input a value, that will be used for determining the number of rows and columns of the pattern, 
   and than we will use “for loop”, for printing stars at the desired places 
   *****
   *****
   *****
   ***** 
   sol:-
   no=int(input("enter the no of rows:-"))
   for i in range(no):
   
    for j in range(no):
        print("*",end="")
    print()
    
 2)
 rombous star partten
 *****
  *****
   *****
    *****
     *****   
num = int (input ("Enter the number:")) 
 
for i in range (0, num):
    for j in range (1, i + 1):  # for space 
        print (" ", end = "") 
    for j in range (0, num):
        print ("*", end = "")  #  for print the star
    print () 
3)
  rectange star partten
  ******
  ******
  ******
  ******
  sol-
rows=int(input("Enter the no of rows:")) 
cols=int(input("enter the no of colms:"))
for i in range(rows):
    for j in range(cols):
        print("*",end=" ")
    print() 
 4)
   hollow rectange partten
   ******
   *    *
   *    *
   ******
no=int(input("enter the no of rows:-"))
no1=int(input("ente the no of cloms:-"))
for i in range(0,no):
    for j in range(0,no1):
        if i==0 or j==0 or i==no-1 or j==no1-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  
  5)
parallalogram partten-
 *****
  *****
   *****
    *****
     *****
  sol-
rows = int (input ("Enter rows:")) 
cols = int (input ("Enter Cols:")) 
 
for i in range (0, rows):
    for j in range (1, i + 1):
        print (" ", end = "") 
     for j in range (0, cols):
        print ("*", end = "") 
    print ()
6) mirrored rhombus partten
sol:-
no=int(input("enter the no:"))
for i in range(0,no):
    for j in range(0,no-i-1):
        print(" ",end="")
    for j in range(0,no):
        print("*",end=" ")
    print()  
7)tringle star pattern
    *
    * *
    * * *
    * * * *
sol=
no=int(input("enter the no:"))
for i in range(0,no):
    for j in range(0,i+1):
        print("*",end="")
    print()   
8)pyramid star partten
    *
  * * *
* * * * *
sol-
no=int(input("enter the no:"))
for i in range(0,no):
    for j in range(0,no-i-1):
        print(" ",end="")
    for j in range(0,i*2+1):
        print("*",end=" ")
    print()  
9)inverted pyramid star partten 
sol- 
no=int(input("enter the row:-"))
for i in range(0,no):
    for j in range(0,i):
        print(" ",end="")
    for j in range(i*2,no*2-1):
        print("*",end="")
    print()    
 

10)half diomond star parttern
*
* *
* * *
* * * *
* * * 
* *
*
slo-
num = int (input ("Enter the Number: ")) 
 
for i in range (0,num):  # half of the str
    for j in range(0,i+1):
        print("*",end="")
    print()
for i in range(1,num): # logic for another  haf str
    for j in range(0,num-i):
        print("*",end="")
    print()  
11) half star partern inverted
     *
   * * 
 * * *
   * *
     *
slo-
num = int (input ("Enter the Number: ")) 
 
for i in range (0,num):  
    for j in range(0,num-i-1):
        
        print(" ",end="")
    for j in range(0,i+1):
        print("*",end="")
    print()    
for i in range(0,num): # logic for another  haf str
    for i in range(0,i+1):
        print(" ",end="")
        
    for j in range(0,num-i-1):
        print("*",end="")
    print()
 12) dimond star pattern
     *
   * * *
 * * * * *
   * * *
     *
num = int(input("Enter the Number: "))

for i in range(0, num):
    for j in range(0, num-i-1):
        print(" ",end="")
    for j in range(0, i*2+1):
        print("*", end="")
    print()

for i in range(1, num):
    for j in range(0, i):
        print(" ",end="")
    for j in range(0, (num-i)*2-1):
        print("*", end="")
    print()s
13) print the squre no  pattern
1 1 1 1 
1 1 1 1
1 1 1 1 
1 1 1 1 
sol:- 
no=int(input("enter the no:"))
for i in range(1,no):
    for j in range(1,no):
        print("1",end=" ")
    print()  
14)
basic squre incrementing parttern
1 1 1 1
2 2 2 2
3 3 3 3 
4 4 4 4 
sol-
no=int(input("enter the no:"))
for i in range(1,no):
    for j in range(1,no):
        print(i,end=" ")
    print() 
15)internl varsity squre parttern
3 3 3 3 
3 1 1 3
3 2 2 3
3 3 3 3  
sol=
rows = int(input("Enter the Number of rows: "))
cols = int(input("Enter the Number of cols: "))

for i in range(0, rows):
    for j in range(0, cols):
        if i == 0 or j == 0 or j == cols-1 or i == rows - 1:
            print("3", end="")
        else:
            print(i, end="")
    print()
16)
Basic Right Triangle Number Pattern
1
2 3 
4 5 6 
7 8 9 10
slo-
no=int(input("enter the no:"))
k=1
for i in range(1,no):
    for j in range(1,i+1):
        print(k,end=" ")
        k+=1
    print()  
17)Basic Right Triangle Number Pattern(inverted)
10 9 8 7
6  5 4
3  2 
1


num = int(input("Enter the Number: "))

k=10

for i in range(0, num):
    for j in range(0, num-i):
        print(k, end=" ")
        k-=1
    print()   
18)basic incrementing tringle partern
6 6 6 6 6
5 5 5 5
4 4 4
3 3
2
slo:-
no=int(input("ente the no of rows:"))
k=0
for i in range(0,no):
    k+=1
for i in range(0,no):
    for j in range(0,no-i):
        print(k,end="")
    k-=1
    print()  
19)basic incrmenting tringle partten (inverted)
3
4 4 
5 5 5 
6 6 6 6
slo:-  
no=int(input("ente the no of rows:"))
k=3
for i in range(0,no):
    for j in range(0,i+1):
        print(k,end="")
    k+=1 
    print()    
    
  20)
  
Basic double incrementing Triangle Pattern initialised = 3
3
4  5 
6  7  8 
9  10 11 12   
slo:- 
no=int(input("enter the no of rows:"))
k=3
for i in range(0,no):
    for j  in range(0,i+1):
        print(k,end=" ")
        k+=1 
    print() 
    
    
    
21)
 
Basic incrementing Diamond Pattern(Inverted) initialised = 3
3
4 4 
5 5 5
6 6 6 6 
5 5 5
4 4
3
sol-
num = int(input("Enter the Number: "))
k = 3

for i in range(0, num):
    for j in range(0, i+1):
        print(k, end="")
    k = k + 1
    print()
k = k - 2
for i in range(0, num):
    for j in range(0, num-i-1):
        print(k, end="")
    k = k - 1
    print()  
22) Basic double incrementing Triangle Pattern initialised = 3
3
4 5
6 7 8 
9 10 11 12
6 7 8 
4 5 
3
sol-
 num = int(input("Enter the Number: "))
k = 3

for i in range(0, num):
    for j in range(0, i+1):
        print(k, end= " ")
        k = k + 1
    print()
k = k - 2
for i in range(0, num):
    for j in range(0, num-i-1):
        print(k, end= " ")
        k = k - 1
    print()  
  
24) Basic incrementing Diamond Pattern(Inverted Sandwich) initialised = 3 
3
4 4 
5 5 5
6 6 6 6
6 6 6 6  
5 5 5
4 4
3


slo-
no=int(input("enter the two no: "))
k=2
for i in range(0,no):
    for j in range(0,i+1):
        print(k,end=" ")
    k+=1 
    print()
k-=1 
for i in range(0,no):
    for j in range(0,no-i):
        print(k,end=" ")
    k+=1 
    print()
                        