import os
import math

# Mathematical operations

def add(a,b):return a+b
def sub(a,b):return a-b
def mul(a,b):return a*b
def divide(a,b):return a/b
def mod(a,b):return a%b
def sqrroot(a):return math.sqrt(a)
def power(a,b):return a**b
def cl():os.system("cls" if os.name == "nt" else "clear")

valid_choices={'1','2','3','4','5','6','7','8','9','10'}
history=[]
try:
    a=float(input("📥 Enter first number: "))
except:
    print("❌ Oops! That input is not valid.")
else:
    while True:
        print("1. ➕ Addition \n2. ➖ Subtraction \n3. ✖️ Multiplication  \n4. ➗ Divison  \n5. 📊 Modulo \n6. √ Square root\n7. ⚡ Power\n8.📜 history\n9.🧹 clear history\n10.🚪 Exit")
        choice = input("👉 Enter your choice: ")
        if choice in valid_choices:
            if choice == "1":
                try:
                    b = float(input("📥 Enter second number: "))
                    result = add(a, b)
                    history.append(f"{a} + {b} = {result}")
                    print(f"{a} + {b} = {result}")
                except:
                    print("❌ Oops! That input is not valid.")
                    exit()
            elif choice == "2":
                try:
                    b = float(input("📥 Enter second number: "))
                except:
                    print("❌ Oops! That input is not valid.")
                    exit()
                result = sub(a, b)
                history.append(f"{a} - {b} = {result}")
                print(f"{a} - {b} = {result}")
            elif choice == "3":
                try:
                    b = float(input("📥 Enter second number: "))
                except:
                    print("❌ Oops! That input is not valid.")
                    exit()
                result = mul(a, b)
                history.append(f"{a} * {b} = {result}")
                print(f"{a} * {b} = {result}")
            elif choice == "4":
                try:
                    b = float(input("📥 Enter second number: "))
                except:
                    print("❌ Oops! That input is not valid.")
                    exit()
                else:
                    if b!=0:
                        result = divide(a, b)
                        history.append(f"{a} / {b} = {result}")
                        print(f"{a} / {b} = {result}")
                    else:
                        print("⚠️ Error: cannot be divided by zero ")
                        continue
            elif choice == "5":
                try:
                    b = float(input("📥 Enter second number: "))
                except:
                    print("❌ Oops! That input is not valid.")
                    exit()
                else:
                    if b!=0:
                        result = mod(a, b)
                        history.append(f"{a} % {b} = {result}")
                        print(f"{a} % {b} = {result}")
                    elif b==0:
                        print("cannot perform modulo by zero ")
                        continue
            elif choice == "6":
                if a < 0:
                    print("Cannot calculate square root of negative number")
                    continue
                else:
                    result=sqrroot(a)
                    history.append(f"√{a} = {result}")
                    print(f"√{a} = {result}")
            elif choice=="7":
                try:
                    b=float(input("📥 Enter second number: "))
                except:
                    print("❌ Oops! That input is not valid.")
                    exit()
                else:
                    result = power(a, b)
                    history.append(f"{a} ** {b} = {result}")
                    print(f"{a} ** {b} = {result}")
            elif choice=="8":
                print("************ History **************")
                if history != []:
                    for i,item in enumerate (history,start=1):
                        print(f"\t{i}. {item}")
                else:
                    print("No history..")
                continue
            elif choice=="9":
                history.clear()
                print("🧹 History cleared successfully...")
                continue
            elif choice == "10":
                print("Thanks for using Mini calc!📱")
                print("👋 bye...")
                break
            try:
                c = input(f"Enter 'y' to continue calculation with {result} or 'n' to start new calculation or 'x' to exit: ")
            except:
                print("❌ Oops! That input is not valid...")
                break
            else:
                if c.lower() == "y":
                    a = result
                elif c.lower() == "n":
                    cl()
                    try:
                        a = float(input("📥 Enter a number: "))
                    except:
                        print("❌ Oops! That input is not valid...")
                        exit()
                elif c.lower() == "x":
                    print("Thanks for using Mini calc!📱")
                    print("👋 bye...")
                    break
                else:
                    print("❌ Oops! That input is not valid...")
                    break
        else:
            print("❌ Oops! That input is not valid! Try again...")