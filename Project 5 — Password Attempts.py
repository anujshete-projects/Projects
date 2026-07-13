Password="pass@123"
count=1
while True :
    num=input("Enter the password")
    if num==Password:
        print("Password correct")
    elif count==4:
        print("access denied")
        break
    else:
        print(f"incorrect password, you have {4- count} left")
        count+=1
