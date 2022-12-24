from math import *

def check(user,inp):
    for i in user:
        if(i not in inp):
            return 1
    return 0

def q2_check(user,occ):
    for i in ((occ)):
        if(occ.index(i)%2==0 and user.count(i)!=(int(occ.index(i))+1)):
            print(i,occ.index(i))
            print(occ.count(i))
            return 0
    return 1


def q9_check(user,occ):
    for i in ((occ)):
        if(occ.index(i)%2==0 and user.count(i)!=(int(occ.index(i))+1)):
            return 0
    return 1


def q1_chechstart(user,start):
    for i in range(len(start)):
        if(user[i]!=start[i]):
            return 0
    return 1


def q7_chechstart(user,start):
    for i in range(len(start)):
        if(user[i]!=start[i]):
            return 0
    return 1



def q1_checkend(user,end):
    user_list=list(user)
    end_list=list(end)
    user_list.reverse()
    end_list.reverse()
    # print(user_list,end_list)
    for i in range(len(end_list)):
        if(user_list[i]!=end_list[i]):
            return 0
    return 1


def q7_checkend(user,end):
    user_list=list(user)
    end_list=list(end)
    user_list.reverse()
    end_list.reverse()
    # print(user_list,end_list)
    for i in range(len(end_list)):
        if(user_list[i]!=end_list[i]):
            return 0
    return 1





def Q1():#Strats/Ends with alphabet
    q1_input=input("Enter input aplphabets: ").split()

    q1_startswith=input("String must starts with alphabet: ")

    q1_endswith=input("String must ends with alphabet: ")

    q1_userstring=input("Enter String: ")
    
                
    if(check(q1_userstring, q1_input)==1):
        print("INVALID\n-> Entered string can't be recognised.\n")
        return 
    else:
        if(len(q1_startswith)!=0 and len(q1_endswith)==0):#only starts with
            if(q1_chechstart(q1_userstring, q1_startswith)==1):
                    print("VALID\n")
            else:
                print("INVALID\n-> As entered string does not starts with'"+q1_startswith+"'.\n")


    
        elif(len(q1_startswith)==0 and len(q1_endswith)!=0):
            if(q1_checkend(q1_userstring, q1_endswith)==1):
                    print("VALID\n")
            else:
                print("INVALID\n-> As entered string does not ends with'"+q1_endswith+"'.\n")

            
    
        elif(len(q1_startswith)!=0 and len(q1_endswith)!=0):
            if(q1_chechstart(q1_userstring, q1_startswith)==1 and q1_checkend(q1_userstring, q1_endswith)==1 ):
                    print("VALID\n")
            else:
                if(q1_chechstart(q1_userstring, q1_startswith)==0):
                    print("INVALID\n-> As entered string does not starts with'"+q1_startswith+"'.\n")
                elif(q1_checkend(q1_userstring, q1_endswith)==0):
                    print("INVALID\n-> As entered string does not ends with'"+q1_endswith+"'.\n")
                
                elif (q1_chechstart(q1_userstring, q1_startswith)==0 and q1_checkend(q1_userstring, q1_endswith)==0):
                    print("INVALID\n-> As entered string does not starts with'"+q1_startswith+"'. and does not ends with'"+q1_endswith+"'. \n")

            
 
# Q1()

#for occ, only use alphabets 
def Q2():# Occurence of alphabet
    q2_input=input("Enter input aplphabets: ").split()

    q2_occurencealpha=input("Enter occ alphabet: ").split()

    q2_count=[]
    for i in range(len(q2_occurencealpha)):
        print("Enter occurence of '"+q2_occurencealpha[i]+"' : ")
        n=int(input())
        q2_count.append(n)
    q2_countall=[]

    q2_userstring=input("Enter string: ")
    q2_userlist=list(q2_userstring)

    for i in q2_occurencealpha:
        q2_countall.append(q2_userlist.count(i))
  
    if(q2_countall==q2_count):
        print("VALID\n")
    
    else:
        print("INVALID\n-> Occurence of alphabets isn't equal to given occurences.\n")
# Q2()   

def Q3():#Must include string
    q3_input=input("Enter input aplphabets: ").split()

    q3_mustinclude=input("Enter string which must be included in input string: ")

    q3_num=int(input("Enter no. of times '"+q3_mustinclude+"' must occur: "))

    q3_userstring=input("Enter string: ")

    if(check(q3_userstring, q3_input)==1):
        print("INVALID\n-> Entered string can't be recognised.\n")
        return 
    else:
        if q3_userstring.count(q3_mustinclude)==q3_num:
            print("VALID\n")
        else:
            print("INVALID\n.->Entered string include '"+q3_mustinclude+"' string "+str(q3_userstring.count(q3_mustinclude))+" times.\n")

# Q3()


def Q4():#even & odd occ. 
    q4_input=input("Enter input aplphabets: ").split()

    q4_evenstring=input("Enter string which must occur even times: ")

    q4_oddstring=input("Enter string which must occur odd times: ")

    q4_userstring=input("Enter string: ")

    if(check(q4_userstring, q4_input)==1):
        print("INVALID\n-> Entered string can't be recognised.\n")
        return 
    else:
        if((q4_userstring.count(q4_evenstring))%2==0 and (q4_userstring.count(q4_oddstring))%2!=0):
            print("VALID\n")
        else:
            if ((q4_userstring.count(q4_evenstring))%2!=0):
                print("INVALID\n-> Enterd string contain '"+q4_evenstring+"' "+str(q4_userstring.count(q4_evenstring))+" times which is NOT an even number.\n")

            elif (((q4_userstring.count(q4_evenstring))%2!=0)): 
                print("INVALID\n-> Enterd string contain '"+q4_oddstring+"' "+str(q4_userstring.count(q4_oddstring))+" times which is NOT an odd number.\n")  
            
            elif ((q4_userstring.count(q4_evenstring))%2!=0 and ((q4_userstring.count(q4_evenstring))%2!=0)):
                print("INVALID\n-> Enterd string contain '"+q4_oddstring+"' "+str(q4_userstring.count(q4_oddstring))+" times which is NOT an odd number & contain '"+q4_evenstring+"' "+str(q4_userstring.count(q4_evenstring))+" times which is NOT an even number.\n")  
            

# Q4()


def Q5():# Inequalities of string
    q5_input=input("Enter input alphabets: ").split()

    q5_atleast=input("Enter alphabet which follws atleaast: ")

    q5_atleastnum=input("'"+q5_atleast+"' must occur atleast how many times: ")

    q5_atmost=input("Enter alphabet which follows atmost: ")

    q5_atmostnum=input("'"+q5_atmost+"' must occur atmost how many times: ")

    q5_userstring=input("Enter string: ")

    if(check(q5_userstring, q5_input)==1):
        print("INVALID\n-> Entered string can't be recognised.\n")
        return 
    else:
        if(len(q5_atleastnum)!=0 and len(q5_atmostnum)!=0):
            if(q5_userstring.count(q5_atleast)>=int(q5_atleastnum) and q5_userstring.count(q5_atmost)<=int(q5_atmostnum)):
                print("VALID\n")
            
            else:
                print("INVALID\n->Entered string contain '"+q5_atleast+"' "+str(q5_userstring.count(q5_atleast))+" times & "+q5_atmost+"' "+str(q5_userstring.count(q5_atmost))+" times.")
        
        elif(len(q5_atleastnum)==0 and len(q5_atmostnum)!=0):
            if(q5_userstring.count(q5_atmost)<=int(q5_atmostnum)):
                print("VALID\n")
            
            else:
                print("INVALID\n->Entered string contain '"+q5_atmost+"' "+str(q5_userstring.count(q5_atmost))+" times.\n")
        
        elif(len(q5_atleastnum)!=0 and len(q5_atmostnum)==0):
            if(q5_userstring.count(q5_atleast)>=int(q5_atleastnum)):
                print("VALID\n")
            
            else:
                print("INVALID\n->Entered string contain '"+q5_atleast+"' "+str(q5_userstring.count(q5_atleast))+" times.\n")


def Q6():#Do not contain 
    q6_input=input("Enter input alphabets: ").split()

    q6_notcontain=input("Enter string which should not be included in input string: ")

    q6_userstring=input("Enter string: ")
    if(check(q6_userstring, q6_input)==1):
        print("INVALID\n-> Entered string can't be recognised.\n")
        return 
    
    else:
        if(q6_userstring.count(q6_notcontain)==0):
            print("VALID\n")
        else:
            print("INVALID\n-> Entered string contain '"+q6_notcontain+"' in it.")

# Q6()


def Q7():#Must include and starts/ends with
    q7_input=input("Enter input alphabets: ").split()

    q7_occrenceofalpha=input("Enter string which must occur: ")#it is compulsory

    q7_nooccrence=input("Enter no. of occrences of '"+q7_occrenceofalpha+"' in input string: ")

    q7_startswith=input("String must starts with: ")

    q7_endswith=input("String must ends with: ")

    q7_userstring=input("Enter string: ")

    if(check(q7_userstring, q7_input)==1):
        print("INVALID\n-> Entered string can't be recognised.\n")
        return 
    
    else:
        if(len(q7_startswith)!=0 and len(q7_endswith)==0):
            if(q7_chechstart(q7_userstring, q7_startswith)==1 and q7_userstring.count(q7_occrenceofalpha)==int(q7_nooccrence)):
                print("VALID\n")

            else:
                c
        elif(len(q7_startswith)==0 and len(q7_endswith)!=0):
            if(q7_userstring[len(q7_userstring)-1]==q7_endswith and q7_userstring.count(q7_occrenceofalpha)==int(q7_nooccrence)):
                print("VALID\n")

            else:
                if(q7_chechstart(q7_userstring, q7_endswith)==0):
                    print("INVALID\n-> Entered string does not ends with'"+ q7_endsswith +"'.\n")
                
                elif(q7_userstring.count(q7_occrenceofalpha)!=int(q7_nooccrence)):
                    print("INVALID\n-> Entered string contain "+q7_occrenceofalpha+"' "+str(q7_userstring.count(q7_occrenceofalpha))+" times.\n")
                
                elif(q7_chechstart(q7_userstring, q7_endswith)==0 and q7_userstring.count(q7_occrenceofalpha)!=int(q7_nooccrence)):
                    print("INVALID\n-> Entered string does not ends with'"+q7_endswith+"'& contain "+q7_occrenceofalpha+"' "+str(q7_userstring.count(q7_occrenceofalpha))+" times.\n")
        
        

        elif(len(q7_startswith)!=0 and len(q7_endswith)!=0):
            if(q7_userstring[0]==q7_startswith and q7_userstring[len(q7_userstring)-1]==q7_endswith and q7_userstring.count(q7_occrenceofalpha)==int(q7_nooccrence)):
                print("VALID\n")
            
            else:

                if(q7_chechstart(q7_userstring, q7_startswith)==0):
                    print("INVALID\n-> Entered string does not starts with'"+q7_startswith+"'.\n")
                
                elif(q7_userstring.count(q7_occrenceofalpha)!=int(q7_nooccrence)):
                    print("INVALID\n-> Entered string contain "+q7_occrenceofalpha+"' "+str(q7_userstring.count(q7_occrenceofalpha))+" times.\n")
                
                elif(q7_chechstart(q7_userstring, q7_startswith)==0 and q7_userstring.count(q7_occrenceofalpha)!=int(q7_nooccrence)):
                    print("INVALID\n-> Entered string does not starts with'"+q7_startswith+"'& contain "+q7_occrenceofalpha+"' "+str(q7_userstring.count(q7_occrenceofalpha))+" times.\n")

                elif(q7_chechstart(q7_userstring, q7_endswith)==0):
                    print("INVALID\n-> Entered string does not ends with'"+q7_endsswith+"'.\n")
                
                elif(q7_userstring.count(q7_occrenceofalpha)!=int(q7_nooccrence)):
                    print("INVALID\n-> Entered string contain "+q7_occrenceofalpha+"' "+str(q7_userstring.count(q7_occrenceofalpha))+" times.\n")
                
                elif(q7_chechstart(q7_userstring, q7_endswith)==0 and q7_userstring.count(q7_occrenceofalpha)!=int(q7_nooccrence)):
                    print("INVALID\n-> Entered string does not ends with'"+q7_endswith+"'& contain "+q7_occrenceofalpha+"' "+str(q7_userstring.count(q7_occrenceofalpha))+" times.\n")
        

# Q7()

def Q8():# Contain + Not contain
    
    q8_input=input("Enter input alphabets: ").split()

    q8_contain=input("Enter string which must be included in input string: ")

    q8_notcontain=input("Enter string which should not be included in input string: ")

    q8_userstring=input("Enter string: ")

    if(check(q8_userstring, q8_input)==1):
        print("INVALID\n-> Entered string can't be recognised.\n")
        return 

    else:
        if(q8_userstring.count(q8_contain)!=0 and q8_userstring.count(q8_notcontain)==0):
            print("VALID\n")
        
        else:
            if(q8_userstring.count(q8_contain)==0):
                print("INVALID\n-> Entered string do NOTcontain '"+q8_contain+"' in it.\n")
            
            elif(q8_userstring.count(q8_notcontain)!=0):
                print("INVALID\n-> Entered string contain '"+q8_notcontain+"' in it.\n")
            
            elif (q8_userstring.count(q8_contain)==0 and q8_userstring.count(q8_notcontain)!=0):
                print("INVALID\n-> Entered string do NOTcontain '"+q8_contain+"' & .contain '"+q8_notcontain+"' in it.\n")
                

# Q8()

# def Q9(): # Must include + occurence of alphabet

#     q9_input=input("Enter input alphabets: ").split()


#     q9_mustinclude=input("Enter string which must be included in input string: ")

#     q9_occurencealpha=input("Enter alphabet which will occur mutiple times: ")
#     q9_listocc=list(q9_occurencealpha)
#     q9_listocc.append(" ")
#     for  i in range(len(q9_occurencealpha)+1):
#         if(i%2!=0):
#             print("Enter no. of occurence of "+q9_occurencealpha[i-1]+" in string: ")
#             n=int(input())
#             q9_listocc[i]=n 


#     q9_userstring=input("Enter string: ")
#     q9_listuser=list(q9_userstring)



#     if(check(q9_userstring, q9_input)==1):
#         print("INVALID\n")
#         return 
#     else:
#         if(q9_check(q9_listuser, q9_listocc)==1 and q9_userstring.count(q9_mustinclude)!=0):
#             print("VALID\n")
        
#         else:
#             print("INVALID\n")
        
# Q9()

def Q10():#Must include + inequalities of string

    q10_input=input("Enter input alphabets: ")

    q10_mustinclude=input("Enter string which must be included in input string: ")#must be filled

    q10_num=int(input("Enter no. of times '"+q10_mustinclude+"' must occur: "))

    q10_atleast=input("Enter string which follws atleaast: ")

    q10_atleastnum=input("'"+q10_atleast+"' must occur atleast how many times: ")

    q10_atmost=input("Enter string which follows atmost: ")

    q10_atmostnum=input("'"+q10_atmost+"' must occur atmost how many times: ")

    q10_userstring=input("Enter string: ")
    

    if(check(q10_userstring, q10_input)==1):
        print("INVALID\n-> Entered string can't be recognised.\n")
        return 
    else:
        if(len(q10_atleastnum)!=0 and len(q10_atmostnum)!=0):
            if(q10_userstring.count(q10_atleast)>=int(q10_atleastnum) and q10_userstring.count(q10_atmost)<=int(q10_atmostnum) and q10_userstring.count(q10_mustinclude)==q10_num):
                print("VALID\n")
            
            else:
                if (q10_userstring.count(q10_atleast)<int(q10_atleastnum)):
                    print("INVALID\n->Entered string contain '"+q10_atleast+"' "+str(q10_userstring.count(q10_atleastnum))+" times.\n")
                
                elif(q10_userstring.count(q10_atmost)>int(q10_atmostnum)):
                    print("INVALID\n->Entered string contain '"+q10_atmost+"' "+str(q5_userstring.count(q10_atmostnum))+" times.\n")
                
                elif(q10_userstring.count(q10_atleast)<int(q10_atleastnum) and q10_userstring.count(q10_atmost)>int(q10_atmostnum)):
                    print("INVALID\n->Entered string contain '"+q10_atleast+"' "+str(q5_userstring.count(q10_atleastnum))+" times &  contain '"+q10_atmost+"' "+str(q5_userstring.count(q10_atmostnum))+" times.\n")
                
                elif ( q10_userstring.count(q10_mustinclude)!=q10_num):
                    print("INVALID\n.->Entered string include '"+q10_mustinclude+"' string "+str((q10_userstring.count(q10_mustinclude)))+" times.\n")
                
                elif(q10_userstring.count(q10_atleast)<int(q10_atleastnum) and q10_userstring.count(q10_atmost)>int(q10_atmostnum) and q10_userstring.count(q10_mustinclude)!=q10_num):
                    print("INVALID\n.->Entered string include '"+q10_mustinclude+"' string "+str((q10_userstring.count(q10_mustinclude)))+" times & contain '"+q10_atleast+"' "+q10_userstring.count(q10_atleastnum)+" times &  contain '"+q10_atmost+"' "+str(q10_userstring.count(q10_atmostnum))+" times.\n")
            

                
        
        elif(len(q10_atleastnum)==0 and len(q10_atmostnum)!=0):
            if(q10_userstring.count(q10_atmost)<=int(q10_atmostnum) and q10_userstring.count(q10_mustinclude)==q10_num):
                print("VALID\n")
            
            else:
                if(q10_userstring.count(q10_atmost)>int(q10_atmostnum)):
                    print("INVALID\n->Entered string contain '"+q10_atmost+"' "+str(q5_userstring.count(q10_atmostnum))+" times.\n")
                
                elif ( q10_userstring.count(q10_mustinclude)!=q10_num):
                    print("INVALID\n.->Entered string include '"+q10_mustinclude+"' string "+str((q10_userstring.count(q10_mustinclude)))+" times.\n")
                
                elif (q10_userstring.count(q10_atmost)>int(q10_atmostnum) and q10_userstring.count(q10_mustinclude)!=q10_num):
                    print("INVALID\n.->Entered string include '"+q10_mustinclude+"' string "+str((q10_userstring.count(q10_mustinclude)))+" times & contain '"+q10_atmost+"' "+str(q10_userstring.count(q10_atmostnum))+" times.\n")
        
        elif(len(q10_atleastnum)!=0 and len(q10_atmostnum)==0):
            if(q10_userstring.count(q10_atleast)>=int(q10_atleastnum) and q10_userstring.count(q10_mustinclude)==q10_num):
                print("VALID\n")
            
            else:
                if (q10_userstring.count(q10_atleast)<int(q10_atleastnum)):
                    print("INVALID\n->Entered string contain '"+q10_atleast+"' "+str(q10_userstring.count(q10_atleastnum))+" times.\n")
                
                elif ( q10_userstring.count(q10_mustinclude)!=q10_num):
                    print("INVALID\n.->Entered string include '"+q10_mustinclude+"' string "+str((q10_userstring.count(q10_mustinclude)))+" times.\n")
                
                elif(q10_userstring.count(q10_atleast)<int(q10_atleastnum) and q10_userstring.count(q10_mustinclude)!=q10_num):
                     print("INVALID\n.->Entered string include '"+q10_mustinclude+"' string "+str((q10_userstring.count(q10_mustinclude)))+" times & contain '"+q10_atleast+"' "+str(q10_userstring.count(q10_atleastnum))+" times.\n")


# Q10()
n=0
print("\n*********************************************  STRING  ANALYZER  *********************************************") 
while(n!=10):
    print("\n\nChoose your problem type from conditions given below: \n")
    print("1. Starts with an string & Ends with an string.\t\t\t2. Occurence of alphabets in a string.\n3. Must include a string.\t\t\t\t\t4. Even & Odd Occurence of a string.\n5. Based on Inequalities of a string.\t\t\t\t6. Do NOT contain a string.\n7. Occurence of alphabets & starts/ends with a string.\t\t8. Contan & do NOT contain type.\n9. Must include a string & inequalities of a string.\t       10. Exit\n")

    n=int(input("Enter your choice: "))

    if(n==1):
        Q1()
        
    elif (n==2):
        Q2()
        
    elif (n==3):
        Q3()


    elif (n==4):
        Q4()


    elif (n==5):
        Q5()


    elif (n==6):
        Q6()


    elif (n==7):
        Q7()


    elif (n==8):
        Q8()


    elif (n==9):
        Q10()







