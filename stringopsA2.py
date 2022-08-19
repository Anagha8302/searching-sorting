def first():
    str1 = input("Enter the string:")
    list1=str1.split()
    m=0
    word=0
    print(list1)
    for i in range (len(list1)):
    #len(list1[i])
        if m<len(list1[i]):
            m=len(list1[i])
            word=i
    print("a)The word with the longest length is:",list1[word])        

def second():
    str1=input("Enter the string:")
    char=input("Enter the character:")
    print(str1)
    counter=0
    for i in range (len(str1)):
        if char==str1[i]:
            counter+=1
    print("Character %s present %i times in string%s"%(char,counter,str1))

def third():
    str2=input("Enter the string:")
    lenstr2=len(str2)
    j=lenstr2-1
    flag=0
    for i in range(int(lenstr2/2+1)):
        if str2[i]==str2[j]:
            flag=1
        else:
            break
        j-=1
        if(flag==1):
            print("It is a Palindrome.")
        else:
            print("Not a Palindrome.")    

def fourth():
    str1=input("Enter the string:")
    sub1=input("Enter the substring:")
    sublen=len(sub1)
    index1=0
    j=0
    for i in range (len(str1)):
        if (sub1[j]==str1[i]):
            j=j+1
            if(j==sublen):
                index1=i-(sublen-1)
                break
            else:
                j=0
    print("The substring index is:",index1)

def fifth():
    str1=input("Enter string:")
    list1=str1.split()
    list2=set(list1)
    list3=list(list2)
    print(list1)
    print(list3)
    list4=[]
    list5=[]
    counter=0
    for i in range (len(list3)):
        counter=0
        for j in range (len(list1)):
            if(list3[i]==list1[j]):
                counter+=1
    list4=list3[i].counter
    list5.append(list4)

while True:
    ch=int(input("Enter your choice:"))
    if(ch==1):
        first()
    elif(ch==2):
        second()
    elif(ch==3):
        third()
    elif(ch==4):
        fourth()
    elif(ch==5):
        fifth()
    elif(ch==6):
        break





