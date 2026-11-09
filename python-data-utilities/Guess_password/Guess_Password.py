import random

def main():
    easy_passwords = [
        "hello1",
        "test123"
    ]

    medium_passwords = [
        "Cat@123",
        "Dog#123",
        "Hello@1",
        "Test@12",
        "Abc@123"
    ]

    hard_passwords = [
        "C@t123!x",
        "D0g#123a",
        "H3llo@1X",
        "T3st@12!",
        "Abc#123X"
    ]
    while True:
        user_diff_choice=input("Which type of password do you want to guess today? Easy, Medium ,Hard : ")

        if user_diff_choice.title()=="Easy":
            comp_pwd=random.choice(easy_passwords)
        elif user_diff_choice.title()=="Medium":
            comp_pwd = random.choice(medium_passwords)
        elif user_diff_choice.title() == "Hard":
            comp_pwd = random.choice(hard_passwords)
        else:
            print("Select a correct difficulty level.")
            continue

        for num in range(1,4):
            usr_guess = input("Guess your password : ")

            result = check_guess_password(usr_guess,comp_pwd)
            print(f"You guessed - {"".join(result)}")

            if comp_pwd=="".join(result):
                print("Hurray!! you guessed it correctly")
                break
            else:
                if num<3:
                    choice2 = input(f"You failed. You have {3 - num} more attempts.Do you want to try to guess the same password? Y/N")
                    if  choice2.strip().lower() =='n':
                            break
                else:
                    print("Ohh, you failed to guess password in 3 attempts!!!")
                    break


        # Ask user if he wants to try to guess a another password
        if input("Do you want to guess another password?? Y/N  : ").strip().lower()=="n":
            break


def check_guess_password(user_guess, comp_pwd_str):
        user_guess_lst=list(user_guess.strip())
        comp_pwd_str_lst=list(comp_pwd_str.strip())
        match_result_list = ["_" for let in comp_pwd_str_lst]
        comp_pwd_str_lst_comp=comp_pwd_str_lst.copy()

        for u_letter in user_guess_lst:
            for num in range(len(comp_pwd_str_lst_comp)):
                if comp_pwd_str_lst_comp[num]==u_letter:
                    match_result_list[num]= u_letter
                    comp_pwd_str_lst_comp[num]="_" # to manage duplicate letter identification
                    break

        return match_result_list

if __name__=="__main__":
    main()