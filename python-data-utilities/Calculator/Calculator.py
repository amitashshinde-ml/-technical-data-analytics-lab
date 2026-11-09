"""
Calculator with history
"""
def main():
    while True:

        choice= input("""What do you want perform calculation (c), check the history (h), or clear the history (clr) : """)

        if choice=="c":
                calc_opr = input("Which calculation do you want to perform? /,*,-,+  : ")
                f_num = int(input("Provide first number  : "))
                s_num = int(input("Provide second number  : "))
                if calc_opr.strip()=='/' and s_num==0:
                    print(f"Invalid second number {s_num} for devision.")
                    continue

                calc_output = perf_cal(f_num,s_num,calc_opr)
                write_file(f_num,s_num,calc_opr,calc_output)
        elif choice=="h":
            read_history()
        elif choice == "clr":
            clear_file()
        else:
            print("Enter correct option - c , h , clr!!")
            continue

        if  input("Do you want to perform another operation? Y/N :").upper() == "N":
            break


def perf_cal(a: int, b: int, math_fun:str):
    if math_fun=='+':
        x= a+b
        print(f"Output of {a} {math_fun} {b} is {x}")
        return x
    elif math_fun=='*':
        x = a*b
        print(f"Output of {a} {math_fun} {b} is {x}")
        return x
    elif math_fun=='/':
        x= round(a/b,2)
        print(f"Output of {a} {math_fun} {b} is {x}")
        return x
    elif math_fun=='-':
        x= a-b
        print(f"Output of {a} {math_fun} {b} is {x}")
        return x
    else:
        return 'Incorrect function chosen'

def write_file(first_num, second_num, operator, output):
    with open("Calcs.txt","a") as fl:
        fl.write(f"{first_num} {operator} {second_num} = {output} \n")

def read_history():
    with open("Calcs.txt","r") as fl:
        hist = fl.readlines()
        if len(hist)==0:
            print("There is no history.")
        else:
            for line in hist:
                print(line.strip())

def clear_file():
    with open("Calcs.txt","w+") as fl:
        fl.close()
        print("History Cleared !!!")

if __name__=="__main__":
    main()