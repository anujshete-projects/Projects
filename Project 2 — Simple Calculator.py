while True:
    a= int(input(""))
    b= int(input(""))
    op=input()
    if op=="+":
        print(f"{a}+{b}={a+b}")
    elif op=="-":
        print(f"{a}-{b}={a-b}")
    elif op=="*":
        print(f"{a}*{b}={a*b}")
    elif op=="%":
        print(f"{a}%{b}={a%b}")
    elif op=="//":
        print(f"{a}//{b}={a//b}")
    else:
        print("wrong input")
