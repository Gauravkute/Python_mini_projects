k,j,d=0,0,0
email=input("Enter your email: ")
#add condition for to check is it correct or wrong
if(len(email)>=9): #check length of email
    if(email[0].isalpha()): #check if email first character is alphabet
        if(("@" in email) and (email.count("@")==1)): #check if email contains @
            if(email.endswith("@gmail.com")):    #see if email ends with @gmail.com
                for i in email:
                    if(i==i.isspace()):    #check for spaces in email
                        k=1
                    elif(i.isalpha()):
                        if(i==i.upper()):  #check if first letter is small or capital
                            j=1
                    elif(i.isdigit()):  
                        continue
                    elif(i=="_" or i=="." or i=="@"):
                        continue
                    else:
                        d=1
                if(k==1 or j==1 or d==1):
                    print("Wrong Email id 5 !!")
                else:
                    print(f'{email} is correct')
            else:
                print("Wrong Email id 4 !!")
        else:
            print("Wrong Email id 3 !!")
    else:
        print("Wrong Email id 2 !!")
else:
    print("Wrong Email id 1 !!")
