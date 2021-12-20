while True:
    print("1.calculator")
    print("2.aera finder")
    print("3.volume finder")
    print("4.exit")
    opt=int(input("select the option"))
    if opt==(1):
        while True:
            print("calculator")
            print("1.Add")
            print("2.multiple")
            print("3.divide")
            print("4.subtract")
            opt2=int(input("select the option"))
            if opt2==1:
                print("add")
                num1=int(input("enter the first number"))
                num2=int(input("enter the second number"))
                Add=num1+num2
                print("sum:",Add)
            elif opt2==2:
                print("multiple")
                num1=int(input("enter the first nimber"))
                num2=int(input("enter the second number"))
                multiple=num1*num2
                print(multiple)
            elif opt2==3:
                print("divide")
                num1=int(input("enter the first nimber"))
                num2=int(input("enter the second number"))
                divide=num1/num2
                print(divide)
            elif opt2==4:
                print("subtract")
                num1=int(input("enter the first nimber"))
                num2=int(input("enter the second number"))
                sub=num1-num2
                print(sub)
            else:
                print("invalid")
            back=input("do you want to go back to main menu")
            if back=="y":
                break
            else:
                continue
    elif opt==(2):
        while True:
            print("area")
            print("1.square")
            print("2.rectangle")
            print("3.triangle")
            print("4.circle")
            opt2=int(input("select the option"))
            if opt2==1:
                print("square")
                a=int(input("enter the first number"))
                area=a**2
                print(area)
            elif opt2==2:
                print("rectangle")
                l=int(input("enter the first nimber"))
                b=int(input("enter the second number"))
                area=l*b
                print(area)
            elif opt2==3:
                print("triangle")
                b=int(input("enter the first nimber"))
                h=int(input("enter the second number"))
                area=(b*h)/2
                print(area)
            elif opt2==4:
                print("circle")
                r=int(input("enter the first nimber"))
                area=3.14*(r**2)
                print(area)
            else:
                print("invalid")
            back=input("do you want to go back to main menu")
            if back=="y":
                break
            else:
                continue
    elif opt==(3):
        while True:
            print("volume")
            print("1.sphere")
            print("2.cylinder")
            print("3.cone")
            
            opt2=int(input("select the option"))
            if opt2==1:
                print("sphere")
                r=int(input("enter the  radius number"))
                v=(4/3)*(3.14*(r**3))
                print("volume:",v)
            elif opt2==2:
                print("cylinder")
                r=int(input("enter the radius nimber"))
                h=int(input("enter the height number"))
                volume=3.14*r*r*h
                print("volume:",volume)
            elif opt2==3:
                print("cone")
                r=int(input("enter the radius number"))
                h=int(input("enter the height number"))
                volume=(3.14*r*r*h)/3
                print("volume",volume)
            else:
                print("invalid")
            back=input("do you want to go back to main menu")
            if back=="y":
                break
            else:
                continue
    elif opt==(4):
        print("exit")
        break
    else:
        print("invalid opt")




