"""
       Group A - Assignment 1
       In second year computer engineering class, group A students play cricket,
group B students play badminton and group C students play football. 
Write a python program using functions to compute following: - 
a)	List of students who play both cricket and badminton 
b)	List of students who play either cricket or badminton but not both 
c)	Number of students who play neither cricket nor badminton
d)	Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, Do not use SET built-in functions)

"""

def accept_set(A,Str): 
   n = int(input("Enter the total no. of student who play %s : "%Str))
   for i in range(n) :
      x = input("Enter the name of student %d who play %s : "%((i+1),Str))
      A.append(x)
   print("Set accepted successfully");

def display_set(A,Str): 
   n = len(A)
   if(n == 0) :
      print("\nGroup of Students who play %s =  { }"%Str)
   else :
      print("\nGroup of Students who play %s =  {"%Str,end=' ')
      for i in range(n-1) :
         print("%s,"%A[i],end=' ')
      print("%s }"%A[n-1]);
   
#<---------------------------------------------------------------------------------------->

# Function for finding intersection between two sets (A&B) , Common elements in both sets

def intersection(lst1,lst2):
    lst3=[]
    for val in lst1:
        if val in lst2:
            lst3.append(val)
    return lst3
#<------------------------------------------------------------------------------------------>

# Function for finding union of two sets (A|B), all elements from both set without repetation

def union(lst1,lst2): 
    lst3=lst1.copy()
    for val in lst2:
        if val not in lst3:
            lst3.append(val)
    return lst3



# Function for finding difference between two sets (A-B) , all elements from A which is not present in B

def diff(lst1,lst2):
    lst3=[]
    for val in lst1:
        if val not in lst2:
            lst3.append(val)
    return lst3

#<---------------------------------------------------------------------------------------------->

# Function for finding symmetric difference of two sets (A^B), set of elements which are in either of the sets A and B, but not in their intersection

def sym_diff(lst1,lst2):
    lst3=[]
    D1=diff(lst1,lst2)
    D2=diff(lst2,lst1)
    lst3=union(D1,D2)
    return lst3
a=[1,2,3,4,5]
b =[1,2,6,7]
			#a instersection b =[1,2]
			#a union b [1,2,3,4,5,6,7]
			#C=a-b = [3,4,5]
			#d=b-a = [6,7]
			#symm diff (A^B)= union(c,d)=[3,4,5,6,7]



#<------------------------------------------------------------------------------------------------>

# Functon for finding List of students who play both cricket and badminton

def CB(lst1,lst2):
    lst3=intersection(lst1,lst2)
    display_set(lst3," both Cricket and Badminton")
    
#<------------------------------------------------------------------------------------------------>

# Function for finding List of students who play either cricket or badminton but not both

def eCeB(lst1,lst2):
    lst3=sym_diff(lst1,lst2)
    display_set(lst3," either cricket or badminton but not both")

#<-------------------------------------------------------------------------------------------------->

# Function for finding Number of students who play neither cricket nor badminton

def nCnB(lst1,lst2,lst3):
    lst4=diff(lst3,union(lst1,lst2))
    display_set(lst4," neither cricket nor badminton")

#<--------------------------------------------------------------------------------------------------->

# Function for finding Number of students who play cricket and football but not badminton

def CBnF(lst1,lst2,lst3):
    lst4=diff(intersection(lst1,lst2),lst3)
    display_set(lst4,"cricket and football but not badminton")
          
def Main() :
   Cricket = []
   Badminton = []
   Football = []
   
   while True :
       print ("\t1 : Accept the Information")
       print ("\t2 : List of students who play both cricket and badminton")
       print ("\t3 : List of students who play either cricket or badminton but not both")
       print ("\t4 : Number of students who play neither cricket nor badminton")
       print ("\t5 : Number of students who play cricket and football but not badminton")
       print ("\t6 : Exit")
       ch = int(input("Enter your choice : "))
       if (ch == 6):
           print ("End of Program")
           break
       elif (ch==1):
           accept_set(Cricket,"Cricket")
           accept_set(Badminton,"Badminton")
           accept_set(Football,"Football")
           display_set(Cricket,"Cricket")
           display_set(Badminton,"Badminton")
           display_set(Football,"Football")           
       elif (ch==2):
           display_set(Cricket,"Cricket")
           display_set(Badminton,"Badminton")
           CB(Cricket,Badminton)
       elif (ch==3):
           display_set(Cricket,"Cricket")
           display_set(Badminton,"Badminton")
           eCeB(Cricket, Badminton)
           
       elif (ch==4):
           display_set(Cricket,"Cricket")
           display_set(Badminton,"Badminton")
           display_set(Football,"Football")
           nCnB(Cricket,Badminton,Football)
           
          
       elif (ch==5):
           display_set(Cricket,"Cricket")
           display_set(Football,"Football")
           display_set(Badminton,"Badminton")
           CBnF(Cricket,Football,Badminton)
       else :
           print ("Wrong choice entered !! Try again")

Main()

